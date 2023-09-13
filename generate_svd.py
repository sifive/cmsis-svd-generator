#!/usr/bin/env python3
# Copyright (c) 2019 SiFive Inc.
# SPDX-License-Identifier: Apache-2.0

"""
This program generates CMSIS SVD xml given the devicetree for the core
"""

import argparse
import os
import sys
import inspect
import pydevicetree
from scripts.riscv_clint0_control import generate_registers_riscv_clint0
from scripts.sifive_clic0_control import generate_registers_sifive_clic0
from scripts.riscv_plic0_control import generate_registers_riscv_plic0

def parse_arguments(argv):
    """Parse the arguments into a dictionary with argparse"""
    arg_parser = argparse.ArgumentParser(description="Generate CMSIS SVD files from Devicetrees")

    arg_parser.add_argument("-d", "--dts", required=True,
                            help="The path to the Devicetree for the target")
    arg_parser.add_argument("-o", "--output", required=True,
                            type=argparse.FileType('w'),
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
            if peripheral.get_fields("reg") is not None and len(peripheral.get_fields("reg").values) % (peripheral.address_cells() + peripheral.size_cells()) != 0:
                continue

            compatibles = peripheral.get_fields("compatible")

            reg_names = {}
            if peripheral.get_field("reg-names") is not None:
                reg_names = peripheral.get_fields("reg-names")
            else:
                reg_names = {"reg"}

            for comp in compatibles:
                for reg in reg_names:
                    regmap_root = os.path.abspath(os.path.dirname(sys.argv[0]))
                    regmap_name = get_name_as_id(comp) + "_" + reg + ".svd"
                    regmap_path = os.path.join(regmap_root, "regmaps", regmap_name)
                    script_name = get_name_as_id(comp) + "_" + reg + ".py"
                    script_path = os.path.join(regmap_root, "scripts", script_name)

                    if "clint0" in comp and not os.path.exists(script_path):
                        script_path = os.path.join(regmap_root, "scripts", "riscv_clint0_control.py") 
                    elif "plic0" in comp and not os.path.exists(script_path):
                        script_path = os.path.join(regmap_root, "scripts", "riscv_plic0_control.py") 
                    elif "clic0" in comp and not os.path.exists(script_path):
                        script_path = os.path.join(regmap_root, "scripts", "sifive_clic0_control.py") 

                    if os.path.exists(regmap_path):
                        ext = str(idx[comp])
                        txt += generate_peripheral(dts, peripheral, comp, ext, reg, regmap_path)
                        idx[comp] += 1
                    elif os.path.exists(script_path):
                        ext = str(idx[comp])
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
        return ""

    reg_pair = reg_dict.get_by_name(reg)

    addr_cells = peripheral.address_cells()
    size_cells = peripheral.size_cells()
    group_size = addr_cells + size_cells

    if reg_pair is None and len(reg_dict.values) == group_size:
        # no reg-names field was present, so parse according to the spec
        reg_pair = [reg_dict.values[addr_cells - 1], reg_dict.values[group_size - 1]]
    elif reg_pair is None:
        # malformed DTS, give up
        return ""

    reg_desc = comp + """,""" + reg
    print("Emitting registers for '" + peripheral.name + "' soc peripheral node")

    return """\
            <peripheral>
              <name>""" + get_name_as_id(comp) + """_""" + ext + """</name>
              <description>From """ + reg_desc + """ peripheral generator</description>
              <baseAddress>""" + "0x{:X}".format(reg_pair[0]) + """</baseAddress>
              <addressBlock>
                <offset>0</offset>
                <size>""" + "0x{:X}".format(reg_pair[1]) + """</size>
                <usage>registers</usage>
              </addressBlock>
""" + generate_registers(dts, peripheral, regmap_path) + """\
            </peripheral>
"""

def generate_registers(dts, peripheral, regmap_path):
    if regmap_path == "":
        # FIXME: instead of just giving up here, attempt to parse register data from the DTS
        return ""

    """Generate xml string for registers from regmap file or generator code"""
    if regmap_path.endswith("riscv_clint0_control.py"):
        return generate_registers_riscv_clint0(dts)
    if regmap_path.endswith("sifive_clic0_control.py"):
        return generate_registers_sifive_clic0(dts, peripheral)
    if regmap_path.endswith("riscv_plic0_control.py"):
        return generate_registers_riscv_plic0(dts, peripheral)

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
    dts = pydevicetree.Devicetree.parseFile(parsed_args.dts, followIncludes=True)
    text = generate_device(dts)
    output = inspect.cleandoc(text)
    parsed_args.output.write(output)
    parsed_args.output.close()

if __name__ == "__main__":
    main(sys.argv[1:])
