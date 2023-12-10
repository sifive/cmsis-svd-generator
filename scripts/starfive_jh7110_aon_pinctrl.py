#!/usr/bin/env python3
# Copyleft (c) 2023 cmsis-svd-generator developers 
# SPDX-License-Identifier: Apache-2.0

from scripts.starfive_common import *

"""
This program generates CMSIS SVD xml for starfive JH7110 aon iomux cfg
"""

def generate_registers_starfive_jh7110_aon_iomux_cfg(dts, peripheral):
    """Generate xml string for registers for starfive_aon_iomux_cfg peripheral"""
    txt = """\
              <registers>
"""

    name_desc_range = [
        (
            "gpo_doen_{}",
            "The selected OEN signal for GPIO{}. The register value indicates the selected GPIO (Output Enable) OEN index from GPIO OEN list 0-5. See Table 2-42: GPIO OEN List for AON_IOMUX for more information.",
            ["[2:0]", "[10:8]", "[18:16]", "[26:24]"]
        ),
        (
            "gpo_dout_{}",
            "The selected OEN signal for GPIO{}. The register value indicates the selected GPIO output signal list 0-9. See Table 2-42: GPIO OEN List for AON_IOMUX for more information.",
            ["[3:0]", "[11:8]", "[19:16]", "[27:24]"]
        ),
        (
            "gpi_pmu_wakeup_{}",
            "The register value indicates the selected GPIO number + 2 (GPIO2-GPIO63, GPIO0 and GPIO1 are not available) for the input signal.",
            ["[2:0]", "[10:8]", "[18:16]", "[26:24]"]
        ),
        (
            "gpen_{}",
            "Enable GPIO IRQ function.",
            ["[0:0]"]
        )
    ]
    for idx in range(len(name_desc_range)):
        (n, d, br) = name_desc_range[idx]
        ndra = [(n.format(i), d.format(i), br[i], "read-write") for i in range(len(br))]
        txt += generate_register_aon_iomux_cfgsaif_syscfg_fmux(idx, ndra)

    name_desc_access = [
        ("is", "1: Edge trigger, 0: Level trigger", "read-write"),
        ("ic", "1: Do not clear the register, 0: Clear the register", "read-write"),
        ("ibe", "1: Trigger on both edges, 0: Trigger on a single edge", "read-write"),
        ("iev", "1: Positive/Low, 0: Negative/High", "read-write"),
        ("ie", "1: Unmask, 0: Mask", "read-write"),
        ("ris", "Status of the edge trigger, can be cleared by writing gpioic.", "read-only"),
        ("mis", "The masked GPIO IRQ status.", "read-only"),
        ("in_sync2", "Status of gpio_in after synchronization.", "read-only")
    ]
    for idx in range(len(name_desc_access)):
        txt += generate_register_aon_iomux_cfgsaif_syscfg_ioirq(idx, 16 + (idx * 4), name_desc_access[idx])


    txt += generate_register("testen", "AON IOMUX CFG SAIF SYSCFG 48", 48, [
        (
            "testen_pos",
            "Power-on-Start (POS) enabler - 1: Enable active pull down for loss of core power, 0: Active pull-down capability disabled",
            "[0:0]",
            "read-write"
        )
    ])

    for idx in range(4): 
        txt += generate_register_aon_iomux_cfgsaif_syscfg_padcfg(idx, 52 + (idx * 4))

    txt += generate_register("rstn", "AON IOMUX CFG SAIF SYSCFG 68", 68, [
        ("smt", "Active high Schmitt (SMT) trigger selector - 0: No hysteresis, 1: Schmitt trigger enabled", "[0:0]", "read-write"),
        ("pos", "Power-on-Start (POS) enabler - 1: Enable active pull-down for loss of core power, 0: Active pull-down capability disabled", "[1:1]", "read-write"),
    ])

    desc = "Output Drive Strength (DS): * 00: The rated drive strength is 2 mA. * 01: The rated drive strength is 4 mA. * 10: The rated drive strength is 8 mA. * 11: The rated drive strength is 12 mA."

    txt += generate_register("rtc", "AON IOMUX CFG SAIF SYSCFG 76", 76, [("ds", desc, "[1:0]", "read-write")])
    txt += generate_register("osc", "AON IOMUX CFG SAIF SYSCFG 84", 84, [("ds", desc, "[1:0]", "read-write")])

    name_desc_range_access = [
        ("gmac0_mdc", "", "[1:0]", "read-write"),
        ("gmac0_mdio", "", "[1:0]", "read-write"),
        ("gmac0_rxd0", "0: GMAC0 IO voltage select 3.3V, 1: GMAC0 IO voltage select 2.5V, 2: GMAC0 IO voltage select 1.8V", "[1:0]", "read-write"),
        ("gmac0_rxd1", "", "[1:0]", "read-write"),
        ("gmac0_rxd2", "", "[1:0]", "read-write"),
        ("gmac0_rxd3", "", "[1:0]", "read-write"),
        ("gmac0_rxdv", "", "[1:0]", "read-write"),
        ("gmac0_rxc", "", "[1:0]", "read-write"),
        ("gmac0_txd0", "", "[1:0]", "read-write"),
        ("gmac0_txd1", "", "[1:0]", "read-write"),
        ("gmac0_txd2", "", "[1:0]", "read-write"),
        ("gmac0_txd3", "", "[1:0]", "read-write"),
        ("gmac0_txen", "", "[1:0]", "read-write"),
        ("gmac0_txc", "", "[1:0]", "read-write"),
        ("gmac0_rxc_func_sel", "Function selector of GMAC0_RXC: * Function 0: u0_aon_crg_clk_gmac0_rgmii_rx, * Function 1: u0_aon_crg_clk_gmac0_rmii_ref, * Function 2: None, * Function 3: None", "[1:0]", "read-write")
    ]
    for idx in range(len(name_desc_range_access)):
        (name, desc, bit_range, access) = name_desc_range_access[idx]
        addr = 88 + (idx * 4)

        txt += generate_register(name, "AON IOMUX CFG SAIF SYSCFG {}".format(addr), addr, [("value", desc, bit_range, access)]) 

    return txt + """\
              </registers>
"""

def generate_register_aon_iomux_cfgsaif_syscfg_fmux(idx, name_desc_range_access):
    name = "fmux_{}".format(idx)
    addr = idx * 4
    desc = "AON IOMUX CFG SAIF SYSCFG FMUX {}".format(addr)

    return generate_register(name, desc, addr, name_desc_range_access) 

def generate_register_aon_iomux_cfgsaif_syscfg_ioirq(idx, addr, name_desc_access):
    name = "ioirq_{}".format(idx)
    desc = "AON IOMUX CFG SAIF SYSCFG IOIRQ {}".format(addr)
    (n, d, a) = name_desc_access

    return generate_register(name, desc, addr, [(n, d, "[3:0]", a)])

def generate_register_aon_iomux_cfgsaif_syscfg_padcfg(idx, addr):
    name = "rgpio_{}".format(idx)
    desc = "AON IOMUX CFG SAIF SYSCFG {}".format(addr)

    name_desc_range = [
            ("ie", "Input Enable (IE) Controller - 1: Enable the receiver, 0: Disable the receiver", "[0:0]"),
            ("ds", "Output Drive Strength (DS) - 00: The rated drive strength is 2 mA, 01: The rated drive strength is 4 mA, 10: The rated drive strength is 8 mA, 11: The rated drive strength is 12 mA", "[2:1]"),
            ("pu", "Pull-Up (PU) settings - 1: Yes, 0: No", "[3:3]"),
            ("pd", "Pull-Down (PD) settings - 1: Yes, 0: No", "[4:4]"),
            ("slew", "Slew Rate Control - 0: Slow (Half frequency), 1: Fast", "[5:5]"),
            ("smt", "Active high Schmitt (SMT) trigger selector - 0: No hysteresis, 1: Schmitt trigger ebabled", "[6:6]"),
            ("pos", "Power-on-Start (POS) enabler - 1: Enable active pull down for loss of core power, 0: Active pull-down capability disabled", "[7:7]"),
    ]
    fields = [(n, d, r, "read-write") for (n, d, r) in name_desc_range]

    return generate_register(name, desc, addr, fields)
