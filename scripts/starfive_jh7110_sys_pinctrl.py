#!/usr/bin/env python3
# Copyleft (c) 2023 cmsis-svd-generator developers 
# SPDX-License-Identifier: Apache-2.0

from scripts.starfive_common import *

"""
This program generates CMSIS SVD xml for starfive JH7110 sys iomux cfg
"""

def generate_registers_starfive_jh7110_sys_iomux_cfg(dts, peripheral):
    """Generate xml string for registers for starfive_sys_iomux_cfg peripheral"""
    txt = """\
              <registers>
"""

    for idx in range(0, 55):
        txt += generate_register_sys_iomux_cfgsaif_syscfg_fmux(idx)

    txt += generate_register_sys_iomux_cfgsaif_syscfg_ioirq_full(55, "sys_gpioen_0_reg", "Enable GPIO IRQ function", "[0:0]", "read-write") 

    name_desc_access = [
        ("sys_gpiois_{}_reg", "1: Edge trigger, 0: Level trigger", "read-write"), 
        ("sys_gpioic_{}_reg", "1: Do not clear the register, 0: Clear the register", "read-write"), 
        ("sys_gpioibe_{}_reg", "1: Trigger on both edges, 0: Trigger on a single edge", "read-write"), 
        ("sys_gpioiev_{}_reg", "1: Positive/Low, 0: Negative/High", "read-write"), 
        ("sys_gpioie_{}_reg", "1: Unmask, 0: Mask", "read-write"), 
        ("sys_gpioris_{}_reg", "Status of the edge trigger. The register can be cleared by writing gpio ic", "read-only"), 
        ("sys_gpiomis_{}_reg", "The masked GPIO IRQ status", "read-only"), 
        ("sys_gpio_in_sync2_{}_reg", "Status of the gpio_in after synchronization", "read-only"), 
    ]

    for idx in range(0, len(name_desc_access)):
        (name, desc, access) = name_desc_access[idx]

        addr_idx = 56 + (idx * 2)
        txt += generate_register_sys_iomux_cfgsaif_syscfg_ioirq_full(addr_idx, name.format(0), desc, "[31:0]", access)

        addr_idx += 1
        txt += generate_register_sys_iomux_cfgsaif_syscfg_ioirq_full(addr_idx, name.format(1), desc, "[31:0]", access)

    for idx in range(0, 64):
        txt += generate_register_sys_iomux_cfgsaif_syscfg_padcfg(288 + (idx * 4), "gpio{}".format(idx))

    txt += generate_register_sys_iomux_cfgsaif_syscfg_padcfg(544, "sd0_clk")
    txt += generate_register_sys_iomux_cfgsaif_syscfg_padcfg(548, "sd0_cmd")

    for idx in range(0, 8):
        txt += generate_register_sys_iomux_cfgsaif_syscfg_padcfg(552 + (idx * 4), "sd0_data{}".format(idx))

    txt += generate_register_sys_iomux_cfgsaif_syscfg_padcfg(584, "sd0_strb")

    names = ["mdc", "mdio", "rxd0", "rxd1", "rxd2", "rxd3", "rxdv", "rxc", "txd0", "txd1", "txd2", "txd3","txen", "txc"]
    for idx in range(0, len(names)):
        txt += generate_register_sys_iomux_cfgsaif_syscfg_full(588 + (idx * 4), "padcfg_pad_gmac1_{}_syscon".format(names[idx]), "", "[1:0]", "read-write")

    txt += generate_register_sys_iomux_cfgsaif_syscfg_padcfg(644, "qspi_sclk")
    txt += generate_register_sys_iomux_cfgsaif_syscfg_padcfg(648, "qspi_csn0")

    for idx in range(0, 4):
        txt += generate_register_sys_iomux_cfgsaif_syscfg_padcfg(652 + (idx * 4), "qspi_data{}".format(idx))

    name_func_range_access = [("pad_gmac1_rxc", "GMAC", "[1:0]", "read-write")]
    for idx in range(0, 10):
        bit = 2 + (idx * 3)
        name_func_range_access.append(("pad_gpio1{}".format(idx), "GPIO", "[{}:{}]".format(bit + 2, bit), "read-write"))

    txt += generate_register_sys_iomux_cfgsaif_syscfg_func_sel(668, name_func_range_access)

    name_func_range_access = [("pad_gpio{}".format(20 + i), "GPIO", "[{}:{}]".format((i * 3) + 2, i * 3), "read-write") for i in range(0, 10)]
    txt += generate_register_sys_iomux_cfgsaif_syscfg_func_sel(672, name_func_range_access)

    name_func_range_access = [("pad_gpio{}".format(30 + i), "GPIO", "[{}:{}]".format((i * 3) + 2, i * 3), "read-write") for i in range(0, 11)]
    txt += generate_register_sys_iomux_cfgsaif_syscfg_func_sel(676, name_func_range_access)

    name_func_range_access = [("pad_gpio{}".format(41 + i), "GPIO", "[{}:{}]".format((i * 3) + 2, i * 3), "read-write") for i in range(0, 11)]
    txt += generate_register_sys_iomux_cfgsaif_syscfg_func_sel(680, name_func_range_access)

    name_func_range_access = [("pad_gpio{}".format(52 + i), "GPIO", "[{}:{}]".format((i * 2) + 1, i * 2), "read-write") for i in range(0, 3)]

    for i in range(4, 11):
        bit = i * 3
        name_func_range_access.append(("pad_gpio{}".format(52 + i), "GPIO", "[{}:{}]".format(bit + 2, bit), "read-write"))

    name_func_range_access.append(("pad_gpio63", "GPIO", "[31:30]", "read-write"))
    txt += generate_register_sys_iomux_cfgsaif_syscfg_func_sel(684, name_func_range_access)

    name_func_range_access = [("pad_gpio6", "GPIO", "[1:0]", "read-write")]
    for i in range(1, 4):
        name_func_range_access.append(("pad_gpio{}".format(6 + i), "GPIO", "[{}:{}]".format((i * 3) + 2, i * 3), "read-write"))

    idx = [0, 10, 11, 1, 2, 3, 4]
    for i in range(0, len(idx)):
        bit = 11 + (i * 3)
        name_func_range_access.append(("u0_dom_isp_top_u0_vin_dvp_data_c{}".format(idx[i]), "DVP_DATA", "[{}:{}]".format(bit + 2, bit), "read-write"))

    txt += generate_register_sys_iomux_cfgsaif_syscfg_func_sel(688, name_func_range_access)

    name_func_range_access = [("u0_dom_isp_top_u0_vin_dvp_data_c{}".format(5 + i), "DVP_DATA", "[{}:{}]".format((i * 3) + 2, i * 3), "read-write") for i in range(0, 5)]
    name_func_range_access.append(("u0_dom_isp_top_u0_vin_dvp_hvalid_c", "DVP_HSYNC", "[17:15]", "read-write"))
    name_func_range_access.append(("u0_dom_isp_top_u0_vin_dvp_vvalid_c", "DVP_VSYNC", "[20:18]", "read-write"))
    name_func_range_access.append(("u0_sys_crg_dvp_clk", "DVP_CLK", "[23:21]", "read-write"))

    txt += generate_register_sys_iomux_cfgsaif_syscfg_func_sel(692, name_func_range_access)

    return txt + """\
              </registers>
"""

def generate_register_sys_iomux_cfgsaif_syscfg_fmux(idx):
    name = "sys_iomux_cfgsaif_syscfg_fmux{}".format(idx)
    desc = "SYS IOMUX CFG SAIF SYSCFG FMUX {}".format(idx)
    addr = "0x{:x}".format(idx * 4)

    txt = """\
                <register>
                  <name>""" + name + """</name>
                  <description>""" + desc + """</description>
                  <addressOffset>""" + addr + """</addressOffset>
                  <size>32</size>
                  <fields>
"""

    for i in range(0, 4):
        field_idx = (idx * 4) + i
        field_name = "sys_iomux_gpo{}_doen_cfg".format(field_idx)
        field_desc = "The selected OEN signal for GPIO{}. The register value indicates the selected GPIO (Output Enable) OEN index from GPIO OEN list 0-49. See Table 2-41: GPIO OEN List for SYS_IOMUX (on page 97) for more information.".format(field_idx)

        bit = i * 8
        bit_range = "[{}:{}]".format(bit + 5, bit)

        txt += generate_field(field_name, field_desc, bit_range, "read-write")

    return txt + """\
                  </fields>
                </register>
"""

def generate_register_sys_iomux_cfgsaif_syscfg_padcfg(idx, pin):
    name = "sys_iomux_cfgsaif_syscfg{}".format(idx)
    desc = "SYS IOMUX CFG SAIF SYSCFG {}".format(idx)
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

def generate_register_sys_iomux_cfgsaif_syscfg_func_sel(idx, name_func_range_access):
    name = "sys_iomux_cfgsaif_syscfg{}".format(idx)
    desc = "SYS IOMUX CFG SAIF SYSCFG {}".format(idx)
    addr = "0x{:x}".format(idx)

    txt = """\
                <register>
                  <name>""" + name + """</name>
                  <description>""" + desc + """</description>
                  <addressOffset>""" + addr + """</addressOffset>
                  <size>32</size>
                  <fields>
"""

    for (name, func, bit_range, access) in name_func_range_access:
        txt += generate_field_sys_iomux_cfgsaif_syscfg_func_sel(name, func, bit_range, access)

    return txt + """\
                  </fields>
                </register>
"""

def generate_register_sys_iomux_cfgsaif_syscfg_ioirq_full(idx, field_name, field_desc, bit_range, access):
    name = "sys_iomux_cfgsaif_syscfg_ioirq{}".format(idx)
    desc = "SYS IOMUX CFG SAIF SYSCFG IOIRQ {}".format(idx)
    addr = "0x{:x}".format(idx * 4)

    txt = """\
                <register>
                  <name>""" + name + """</name>
                  <description>""" + desc + """</description>
                  <addressOffset>""" + addr + """</addressOffset>
                  <size>32</size>
                  <fields>
"""

    txt += generate_field(field_name, field_desc, bit_range, access)

    return txt + """\
                  </fields>
                </register>
"""

def generate_register_sys_iomux_cfgsaif_syscfg_full(idx, field_name, field_desc, bit_range, access):
    name = "sys_iomux_cfgsaif_syscfg{}".format(idx)
    desc = "SYS IOMUX CFG SAIF SYSCFG {}".format(idx)
    addr = "0x{:x}".format(idx)

    txt = """\
                <register>
                  <name>""" + name + """</name>
                  <description>""" + desc + """</description>
                  <addressOffset>""" + addr + """</addressOffset>
                  <size>32</size>
                  <fields>
"""

    txt += generate_field(field_name, field_desc, bit_range, access)

    return txt + """\
                  </fields>
                </register>
"""

def generate_field_sys_iomux_cfgsaif_syscfg_func_sel(name, func, bit_range, access):
    func_desc = {
            "GMAC": "Function selector of GMAC1_RXC: * Function 0: u0_sys_crg.clk_gmac1_rgmii_rx, * Function 1: u0_sys_crg.clk_gmac1_rmii_ref, * Function 2: None, * Function 3: None",
            "GPIO": "GPIO function selector: * Function 0: See Function Description no page 84 for more information, * Function 1: See Full Multiplexing for more information, * Function 2: See Function 2 for more information, * Function 3: See Function 3 for more information",
            "DVP_DATA": "Function Selector of DVP_DATA[idx], see Function 2 for more information",
            "DVP_HSYNC": "Function Selector of DVP_HSYNC, see Function 2 for more information",
            "DVP_VSYNC": "Function Selector of DVP_VSYNC, see Function 2 for more information",
            "DVP_CLK": "Function Selector of DVP_CLK, see Function 2 for more information",
    }

    return generate_field("{}_func_sel".format(name), func_desc[func], bit_range, access)  
