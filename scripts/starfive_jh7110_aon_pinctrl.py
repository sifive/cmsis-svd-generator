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
            "aon_iomux_gpo{}_doen_cfg",
            "The selected OEN signal for GPIO{}. The register value indicates the selected GPIO (Output Enable) OEN index from GPIO OEN list 0-5. See Table 2-42: GPIO OEN List for AON_IOMUX for more information.",
            ["[2:0]", "[10:8]", "[18:16]", "[26:24]"]
        ),
        (
            "aon_iomux_gpo{}_dout_cfg",
            "The selected OEN signal for GPIO{}. The register value indicates the selected GPIO output signal list 0-9. See Table 2-42: GPIO OEN List for AON_IOMUX for more information.",
            ["[3:0]", "[11:8]", "[19:16]", "[27:24]"]
        ),
        (
            "aon_iomux_gpi_u0_pmu_io_event_stub_gpio_wakeup_{}_cfg",
            "The register value indicates the selected GPIO number + 2 (GPIO2-GPIO63, GPIO0 and GPIO1 are not available) for the input signal.",
            ["[2:0]", "[10:8]", "[18:16]", "[26:24]"]
        ),
        (
            "aon_gpioen_{}_reg",
            "Enable GPIO IRQ function.",
            ["[0:0]"]
        )
    ]
    for idx in range(0, len(name_desc_range)):
        (n, d, br) = name_desc_range[idx]
        ndra = [(n.format(i), d.format(i), br[i], "read-write") for i in range(0, len(br))]
        txt += generate_register_aon_iomux_cfgsaif_syscfg_fmux(idx, ndra)

    name_desc_access = [
        ("aon_gpiois_0_reg", "1: Edge trigger, 0: Level trigger", "read-write"),
        ("aon_gpioic_0_reg", "1: Do not clear the register, 0: Clear the register", "read-write"),
        ("aon_gpioibe_0_reg", "1: Trigger on both edges, 0: Trigger on a single edge", "read-write"),
        ("aon_gpioiev_0_reg", "1: Positive/Low, 0: Negative/High", "read-write"),
        ("aon_gpioie_0_reg", "1: Unmask, 0: Mask", "read-write"),
        ("aon_gpioris_0_reg", "Status of the edge trigger, can be cleared by writing gpioic.", "read-only"),
        ("aon_gpiomis_0_reg", "The masked GPIO IRQ status.", "read-only"),
        ("aon_gpio_in_sync2_0_reg", "Status of gpio_in after synchronization.", "read-only")
    ]
    for idx in range(4, 12):
        txt += generate_register_aon_iomux_cfgsaif_syscfg_ioirq(idx, name_desc_access[idx - 4])


    name_desc_range_access = [("padcfg_pad_testen_pos", "Power-on-Start (POS) enabler - 1: Enable active pull down for loss of core power, 0: Active pull-down capability disabled", "[0:0]", "read-write")]
    txt += generate_register_aon_iomux_cfgsaif_syscfg(48, name_desc_range_access)


    for idx in range(0, 4): 
        txt += generate_register_aon_iomux_cfgsaif_syscfg_padcfg(52 + (idx * 4), "rgpio{}".format(idx))

    name_desc_range_access = [
        ("padcfg_pad_rstn_smt", "Active high Schmitt (SMT) trigger selector - 0: No hysteresis, 1: Schmitt trigger enabled", "[0:0]", "read-write"),
        ("padcfg_pad_rstn_pos", "Power-on-Start (POS) enabler - 1: Enable active pull-down for loss of core power, 0: Active pull-down capability disabled", "[1:1]", "read-write"),
    ]
    txt += generate_register_aon_iomux_cfgsaif_syscfg(68, name_desc_range_access)

    desc = "Output Drive Strength (DS): * 00: The rated drive strength is 2 mA. * 01: The rated drive strength is 4 mA. * 10: The rated drive strength is 8 mA. * 11: The rated drive strength is 12 mA."

    name_desc_range_access = [
        [("padcfg_pad_rtc_ds", desc, "[1:0]", "read-write")],
        [("padcfg_pad_osc_ds", desc, "[1:0]", "read-write")]
    ]
    for idx in range(0, len(name_desc_range_access)):
        txt += generate_register_aon_iomux_cfgsaif_syscfg(76 + (idx * 8), name_desc_range_access[idx])

    name_desc_range_access = [
        [("padcfg_pad_gmac0_mdc_syscon", "", "[1:0]", "read-write")],
        [("padcfg_pad_gmac0_mdio_syscon", "", "[1:0]", "read-write")],
        [("padcfg_pad_gmac0_rxd0_syscon", "0: GMAC0 IO voltage select 3.3V, 1: GMAC0 IO voltage select 2.5V, 2: GMAC0 IO voltage select 1.8V", "[1:0]", "read-write")],
        [("padcfg_pad_gmac0_rxd1_syscon", "", "[1:0]", "read-write")],
        [("padcfg_pad_gmac0_rxd2_syscon", "", "[1:0]", "read-write")],
        [("padcfg_pad_gmac0_rxd3_syscon", "", "[1:0]", "read-write")],
        [("padcfg_pad_gmac0_rxdv_syscon", "", "[1:0]", "read-write")],
        [("padcfg_pad_gmac0_rxc_syscon", "", "[1:0]", "read-write")],
        [("padcfg_pad_gmac0_txd0_syscon", "", "[1:0]", "read-write")],
        [("padcfg_pad_gmac0_txd1_syscon", "", "[1:0]", "read-write")],
        [("padcfg_pad_gmac0_txd2_syscon", "", "[1:0]", "read-write")],
        [("padcfg_pad_gmac0_txd3_syscon", "", "[1:0]", "read-write")],
        [("padcfg_pad_gmac0_txen_syscon", "", "[1:0]", "read-write")],
        [("padcfg_pad_gmac0_txc_syscon", "", "[1:0]", "read-write")],
        [("pad_gmac0_rxc_func_sel", "Function selector of GMAC0_RXC: * Function 0: u0_aon_crg_clk_gmac0_rgmii_rx, * Function 1: u0_aon_crg_clk_gmac0_rmii_ref, * Function 2: None, * Function 3: None", "[1:0]", "read-write")]
    ]
    for idx in range(0, len(name_desc_range_access)):
        txt += generate_register_aon_iomux_cfgsaif_syscfg(88 + (idx * 4), name_desc_range_access[idx])

    return txt + """\
              </registers>
"""

def generate_register_aon_iomux_cfgsaif_syscfg_fmux(idx, name_desc_range_access):
    name = "aon_iomux_cfgsaif_syscfg_fmux{}".format(idx)
    desc = "AON IOMUX CFG SAIF SYSCFG FMUX {}".format(idx)
    addr = "0x{:x}".format(idx * 4)

    txt = """\
                <register>
                  <name>""" + name + """</name>
                  <description>""" + desc + """</description>
                  <addressOffset>""" + addr + """</addressOffset>
                  <size>32</size>
                  <fields>
"""

    for i in range(0, len(name_desc_range_access)):
        (name, desc, bit_range, access) = name_desc_range_access[i]
        txt += generate_field(name, desc, bit_range, access)

    return txt + """\
                  </fields>
                </register>
"""

def generate_register_aon_iomux_cfgsaif_syscfg_ioirq(idx, name_desc_access):
    name = "aon_iomux_cfgsaif_syscfg_ioirq{}".format(idx)
    desc = "AON IOMUX CFG SAIF SYSCFG IOIRQ {}".format(idx)
    addr = "0x{:x}".format(idx * 4)

    txt = """\
                <register>
                  <name>""" + name + """</name>
                  <description>""" + desc + """</description>
                  <addressOffset>""" + addr + """</addressOffset>
                  <size>32</size>
                  <fields>
"""

    (name, desc, access) = name_desc_access
    txt += generate_field(name, desc, "[3:0]", access)

    return txt + """\
                  </fields>
                </register>
"""

def generate_register_aon_iomux_cfgsaif_syscfg(idx, name_desc_range_access):
    name = "aon_iomux_cfgsaif_syscfg{}".format(idx)
    desc = "AON IOMUX CFG SAIF SYSCFG {}".format(idx)
    addr = "0x{:x}".format(idx)

    txt = """\
                <register>
                  <name>""" + name + """</name>
                  <description>""" + desc + """</description>
                  <addressOffset>""" + addr + """</addressOffset>
                  <size>32</size>
                  <fields>
"""

    for i in range(0, len(name_desc_range_access)):
        (name, desc, bit_range,  access) = name_desc_range_access[i]
        txt += generate_field(name, desc, bit_range, access)

    return txt + """\
                  </fields>
                </register>
"""

def generate_register_aon_iomux_cfgsaif_syscfg_padcfg(idx, pin):
    name = "aon_iomux_cfgsaif_syscfg{}".format(idx)
    desc = "AON IOMUX CFG SAIF SYSCFG {}".format(idx)
    addr = "0x{:x}".format(idx)

    txt = """\
                <register>
                  <name>""" + name + """</name>
                  <description>""" + desc + """</description>
                  <addressOffset>""" + addr + """</addressOffset>
                  <size>32</size>
                  <fields>
"""

    name_desc_range = [
            ("ie", "Input Enable (IE) Controller - 1: Enable the receiver, 0: Disable the receiver", "[0:0]"),
            ("ds", "Output Drive Strength (DS) - 00: The rated drive strength is 2 mA, 01: The rated drive strength is 4 mA, 10: The rated drive strength is 8 mA, 11: The rated drive strength is 12 mA", "[2:1]"),
            ("pu", "Pull-Up (PU) settings - 1: Yes, 0: No", "[3:3]"),
            ("pd", "Pull-Down (PD) settings - 1: Yes, 0: No", "[4:4]"),
            ("slew", "Slew Rate Control - 0: Slow (Half frequency), 1: Fast", "[5:5]"),
            ("smt", "Active high Schmitt (SMT) trigger selector - 0: No hysteresis, 1: Schmitt trigger ebabled", "[6:6]"),
            ("pos", "Power-on-Start (POS) enabler - 1: Enable active pull down for loss of core power, 0: Active pull-down capability disabled", "[7:7]"),
    ]

    for idx in range(0, len(name_desc_range)):
        (name, desc, bit_range) = name_desc_range[idx]
        txt += generate_field("padcfg_pad_{}_{}".format(pin, name), desc, bit_range, "read-write")

    return txt + """\
                  </fields>
                </register>
"""
