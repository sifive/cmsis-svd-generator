#!/usr/bin/env python3
# Copyright (c) 2019 SiFive Inc.
# SPDX-License-Identifier: Apache-2.0

"""
This program generates CMSIS SVD xml given the devicetree for the core
"""

import argparse
import logging
import os
import sys
import inspect
import pydevicetree
from scripts.arm_pl022 import generate_registers_arm_pl022
from scripts.cdns_qspi_nor import generate_registers_cdns_qspi
from scripts.riscv_clint0_control import generate_registers_riscv_clint0
from scripts.sifive_clic0_control import generate_registers_sifive_clic0
from scripts.riscv_plic0_control import generate_registers_riscv_plic0
from scripts.snps_designware_i2c import generate_registers_snps_designware_i2c
from scripts.snps_dw_apb_uart import generate_registers_snps_dw_apb_uart
from scripts.starfive_common import generate_interrupt
from scripts.starfive_jh7110_dmc_ctrl import generate_registers_starfive_jh7110_dmc_ctrl
from scripts.starfive_jh7110_dmc_phy import generate_registers_starfive_jh7110_dmc_phy
from scripts.starfive_jh7110_pmu import generate_registers_starfive_jh7110_pmu
from scripts.starfive_jh7110_stgcrg import generate_registers_starfive_jh7110_stgcrg
from scripts.starfive_jh7110_syscrg import generate_registers_starfive_jh7110_syscrg
from scripts.starfive_jh7110_aoncrg import generate_registers_starfive_jh7110_aoncrg
from scripts.starfive_jh7110_aon_pinctrl import generate_registers_starfive_jh7110_aon_iomux_cfg
from scripts.starfive_jh7110_aon_syscon import generate_registers_starfive_jh7110_aon_syscon
from scripts.starfive_jh7110_stg_syscon import generate_registers_starfive_jh7110_stg_syscon
from scripts.starfive_jh7110_sys_pinctrl import generate_registers_starfive_jh7110_sys_iomux_cfg
from scripts.starfive_jh7110_sys_syscon import generate_registers_starfive_jh7110_sys_syscon
from scripts.starfive_jh7110_trng import generate_registers_starfive_jh7110_trng

def parse_arguments(argv):
    """Parse the arguments into a dictionary with argparse"""
    arg_parser = argparse.ArgumentParser(description="Generate CMSIS SVD files from Devicetrees")

    arg_parser.add_argument("-d", "--dts", required=True,
                            help="The path to the Devicetree for the target")
    arg_parser.add_argument("-o", "--output", required=True,
                            type=argparse.FileType('w'),
                            help="The path of the CMSIS SVD file to output")
    arg_parser.add_argument("-l", "--log", required=False,
                            default="WARN",
                            type=str,
                            help="The path of the CMSIS SVD file to output")

    return arg_parser.parse_args(argv)

def generate_device(dts):
    """Generate xml string for device"""
    root = dts.root()
    model = root.get_field("model")
    print("Generating CMSIS SVD file for '" + model + "' model")

    return """\
        <?xml version="1.0" encoding="utf-8"?>
        <device schemaVersion="1.3" xmlns:xs="http://www.w3.org/2001/XMLSchema-instance" xs:noNamespaceSchemaLocation="CMSIS-SVD.xsd">
          <name>""" + get_name_as_id(model) + """</name>
          <version>0.1</version>
          <description>From """ + model + """,model device generator</description>
          <addressUnitBits>8</addressUnitBits>
          <width>32</width>
          <size>32</size>
          <access>read-write</access>
          <peripherals>
""" + generate_peripherals(dts) + """\
          </peripherals>
        </device>
"""

#pylint: disable=too-many-locals
def generate_peripherals(dts):
    """Generate xml string for peripherals"""
    txt = ""
    soc = dts.get_by_path("/soc")
    idx = {}

    for peripheral in soc.child_nodes():
        if peripheral.get_field("compatible") is not None:
            compatibles = peripheral.get_fields("compatible")
            for compatible in compatibles:
                idx[compatible] = 0

    for peripheral in soc.child_nodes():
        if peripheral.get_field("compatible") is not None:
            reg = peripheral.get_fields("reg")

            if reg is None:
                reg_cells = 0
            else:
                reg_cells = len(peripheral.get_fields("reg").values)

            exp_reg_cells = peripheral.address_cells() + peripheral.size_cells()

            if peripheral.get_fields("reg") is not None and reg_cells % exp_reg_cells != 0:
                logging.debug("Unexpected number of reg cells {}, expected {}".format(reg_cells, exp_reg_cells)) 
                continue

            compatibles = peripheral.get_fields("compatible")

            reg_names = {}
            if peripheral.get_field("reg-names") is not None:
                reg_names = peripheral.get_fields("reg-names")
            else:
                reg_names = {""}

            for comp in compatibles:
                for reg in reg_names:
                    if len(reg) == 0:
                        rn = ""
                    else:
                        rn = "_" + reg

                    regmap_root = os.path.abspath(os.path.dirname(sys.argv[0]))
                    regmap_name = get_name_as_id(comp) + rn + ".svd"
                    regmap_path = os.path.join(regmap_root, "regmaps", regmap_name)
                    script_name = get_name_as_id(comp) + rn + ".py"
                    script_path = os.path.join(regmap_root, "scripts", script_name)

                    logging.debug("Compatible: {}".format(comp))
                    logging.debug("    Regmap path: {}".format(regmap_path))
                    logging.debug("    Script path: {}".format(script_path))

                    if "clint" in comp and not os.path.exists(script_path):
                        regmap_path = ""
                        script_path = os.path.join(regmap_root, "scripts", "riscv_clint0_control.py")
                    elif "plic" in comp and not os.path.exists(script_path):
                        regmap_path = ""
                        script_path = os.path.join(regmap_root, "scripts", "riscv_plic0_control.py")
                    elif "clic" in comp and not os.path.exists(script_path):
                        regmap_path = ""
                        script_path = os.path.join(regmap_root, "scripts", "sifive_clic0_control.py")

                    if os.path.exists(regmap_path):
                        ext = str(idx[comp])
                        logging.info("Regmap path: {}".format(regmap_path))
                        txt += generate_peripheral(dts, peripheral, comp, ext, reg, regmap_path)
                        idx[comp] += 1
                    elif os.path.exists(script_path):
                        ext = str(idx[comp])
                        logging.info("Script path: {}".format(script_path))
                        txt += generate_peripheral(dts, peripheral, comp, ext, reg, script_path)
                        idx[comp] += 1
                    else:
                        ext = str(idx[comp])
                        txt += generate_peripheral(dts, peripheral, comp, ext, reg, "")
                        idx[comp] += 1

    return txt

#pylint: disable=too-many-arguments
def generate_peripheral(dts, peripheral, comp, ext, reg, regmap_path):
    """Generate xml string for peripheral"""
    reg_dict = peripheral.get_reg()

    if reg_dict is None:
        logging.debug("No peripheral found for {}".format(peripheral))
        return ""

    reg_pair = reg_dict.get_by_name(reg)

    addr_cells = peripheral.address_cells()
    size_cells = peripheral.size_cells()
    group_size = addr_cells + size_cells

    if reg_pair is None and len(reg_dict.values) == group_size:
        # no reg-names field was present, so parse according to the spec
        reg_pair = [reg_dict.values[addr_cells - 1], reg_dict.values[group_size - 1]]
    elif reg_pair is None:
        logging.debug("Malformed DTS entry: {}".format(peripheral))
        # malformed DTS, give up
        return ""

    reg_desc = comp + """,""" + reg
    logging.info("Emitting registers for '" + peripheral.name + "' soc peripheral node")

    if regmap_path.endswith("arm_pl022.py"):
        name = "spi{}".format(ext)
    elif regmap_path.endswith("cdns_qspi_nor.py"):
        name = "qspi".format(ext)
    elif regmap_path.endswith("riscv_clint0_control.py"):
        name = "clint"
    elif regmap_path.endswith("riscv_plic0_control.py"):
        name = "plic"
    elif regmap_path.endswith("sifive_clic0_control.py"):
        name = "clic"
    elif regmap_path.endswith("snps_dw_apb_uart.py"):
        name = "uart{}".format(ext)
    elif regmap_path.endswith("snps_designware_i2c.py"):
        name = "i2c{}".format(ext)
    elif regmap_path.endswith("starfive_jh7110_pmu.py"):
        name = "pmu"
    elif regmap_path.endswith("starfive_jh7110_syscrg.py"):
        name = "syscrg"
    elif regmap_path.endswith("starfive_jh7110_stgcrg.py"):
        name = "stgcrg"
    elif regmap_path.endswith("starfive_jh7110_aoncrg.py"):
        name = "aoncrg"
    elif regmap_path.endswith("starfive_jh7110_aon_pinctrl.py"):
        name = "aon_pinctrl"
    elif regmap_path.endswith("starfive_jh7110_aon_syscon.py"):
        name = "aon_syscon"
    elif regmap_path.endswith("starfive_jh7110_stg_syscon.py"):
        name = "stg_syscon"
    elif regmap_path.endswith("starfive_jh7110_sys_pinctrl.py"):
        name = "sys_pinctrl"
    elif regmap_path.endswith("starfive_jh7110_sys_syscon.py"):
        name = "sys_syscon"
    elif regmap_path.endswith("starfive_jh7110_pwm.py") or regmap_path.endswith("starfive_jh7110_pwm.svd"):
        name = "pwm"
    elif regmap_path.endswith("starfive_jh7110_trng.py"):
        name = "trng"
    elif regmap_path.endswith("starfive_jh7110_dmc_ctrl.py"):
        name = "dmc_ctrl"
    elif regmap_path.endswith("starfive_jh7110_dmc_phy.py"):
        name = "dmc_phy"
    else:
        name = "{}_{}".format(get_name_as_id(comp), ext)

    return """\
            <peripheral>
              <name>""" + name + """</name>
              <description>From """ + reg_desc + """ peripheral generator</description>
              <baseAddress>""" + "0x{:X}".format(reg_pair[0]) + """</baseAddress>
              <addressBlock>
                <offset>0</offset>
                <size>""" + "0x{:X}".format(reg_pair[1]) + """</size>
                <usage>registers</usage>
              </addressBlock>
""" + generate_interrupt("jh7110", name) + """\
""" + generate_registers(dts, peripheral, regmap_path) + """\
            </peripheral>
"""

def generate_registers(dts, peripheral, regmap_path):
    if regmap_path == "":
        logging.debug("No regmap file found for {}".format(peripheral))
        logging.debug("\tRegmap path: {}".format(regmap_path))
        # FIXME: instead of just giving up here, attempt to parse register data from the DTS
        return ""

    """Generate xml string for registers from regmap file or generator code"""
    if regmap_path.endswith("arm_pl022.py"):
        return generate_registers_arm_pl022(dts, peripheral)
    if regmap_path.endswith("cdns_qspi_nor.py"):
        return generate_registers_cdns_qspi(dts, peripheral)
    if regmap_path.endswith("riscv_clint0_control.py"):
        return generate_registers_riscv_clint0(dts)
    if regmap_path.endswith("sifive_clic0_control.py"):
        return generate_registers_sifive_clic0(dts, peripheral)
    if regmap_path.endswith("riscv_plic0_control.py"):
        return generate_registers_riscv_plic0(dts, peripheral)
    if regmap_path.endswith("snps_designware_i2c.py"):
        return generate_registers_snps_designware_i2c(dts, peripheral)
    if regmap_path.endswith("snps_dw_apb_uart.py"):
        return generate_registers_snps_dw_apb_uart(dts, peripheral)
    if regmap_path.endswith("starfive_jh7110_dmc_ctrl.py"):
        return generate_registers_starfive_jh7110_dmc_ctrl(dts, peripheral)
    if regmap_path.endswith("starfive_jh7110_dmc_phy.py"):
        return generate_registers_starfive_jh7110_dmc_phy(dts, peripheral)
    if regmap_path.endswith("starfive_jh7110_pmu.py"):
        return generate_registers_starfive_jh7110_pmu(dts, peripheral)
    if regmap_path.endswith("starfive_jh7110_syscrg.py"):
        return generate_registers_starfive_jh7110_syscrg(dts, peripheral)
    if regmap_path.endswith("starfive_jh7110_stgcrg.py"):
        return generate_registers_starfive_jh7110_stgcrg(dts, peripheral)
    if regmap_path.endswith("starfive_jh7110_aoncrg.py"):
        return generate_registers_starfive_jh7110_aoncrg(dts, peripheral)
    if regmap_path.endswith("starfive_jh7110_aon_pinctrl.py"):
        return generate_registers_starfive_jh7110_aon_iomux_cfg(dts, peripheral)
    if regmap_path.endswith("starfive_jh7110_aon_syscon.py"):
        return generate_registers_starfive_jh7110_aon_syscon(dts, peripheral)
    if regmap_path.endswith("starfive_jh7110_stg_syscon.py"):
        return generate_registers_starfive_jh7110_stg_syscon(dts, peripheral)
    if regmap_path.endswith("starfive_jh7110_sys_pinctrl.py"):
        return generate_registers_starfive_jh7110_sys_iomux_cfg(dts, peripheral)
    if regmap_path.endswith("starfive_jh7110_sys_syscon.py"):
        return generate_registers_starfive_jh7110_sys_syscon(dts, peripheral)
    if regmap_path.endswith("starfive_jh7110_trng.py"):
        return generate_registers_starfive_jh7110_trng(dts, peripheral)

    logging.debug("Reading registers from regmap file: {}".format(regmap_path))

    regmap_file = open(regmap_path, "r")
    txt = ""
    for line in regmap_file:
        txt += """              """ + line
    return txt

def get_name_as_id(name):
    """Get name as legal svd identifier"""
    return name.replace(",", "_").replace("-", "_")

def main(argv):
    """Parse arguments, extract data, and render clean cmsis svd xml to file"""


    parsed_args = parse_arguments(argv)

    # set the logging level from the command line
    numeric_level = getattr(logging, parsed_args.log.upper(), None)
    if not isinstance(numeric_level, int):
        raise ValueError('Invalid log level: %s' % parsed_args.log)
    logging.basicConfig(level=numeric_level)

    dts = pydevicetree.Devicetree.parseFile(parsed_args.dts, followIncludes=True)
    text = generate_device(dts)
    output = inspect.cleandoc(text)
    parsed_args.output.write(output)
    parsed_args.output.close()

if __name__ == "__main__":
    main(sys.argv[1:])
