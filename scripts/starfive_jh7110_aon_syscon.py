#!/usr/bin/env python3
# Copyleft (c) 2023 cmsis-svd-generator developers 
# SPDX-License-Identifier: Apache-2.0

from scripts.starfive_common import *

"""
This program generates CMSIS SVD xml for starfive JH7110 aon syscon
"""

def generate_registers_starfive_jh7110_aon_syscon(dts, peripheral):
    """Generate xml string for registers for starfive_aon_syscon peripheral"""
    txt = """\
              <registers>
"""

    txt += generate_register_aon_sysconsaif_syscfg_full(0, "aon_gp_reg", "", "[31:0]", "read-write")
    txt += generate_register_aon_sysconsaif_syscfg_full(4, "u0_boot_ctrl_boot_status", "", "[3:0]", "read-only")
    txt += generate_register_aon_sysconsaif_syscfg_full(8, "u0_boot_ctrl_boot_vector_31_0", "", "[31:0]", "read-only")
    txt += generate_register_aon_sysconsaif_syscfg12()

    for idx in range(0, 2):
        bit = idx * 32
        txt += generate_register_aon_sysconsaif_syscfg_full(16 + (idx * 4), "gmac5_axi64_ptp_timestamp_o_{}_{}".format(bit + 31, bit), "", "[31:0]", "read-only")

    txt += generate_register_aon_sysconsaif_syscfg24()
    txt += generate_register_aon_sysconsaif_syscfg_full(28, "u0_otpc_fl_func_lock", "", "[31:0]", "read-only")
    txt += generate_register_aon_sysconsaif_syscfg_full(32, "u0_otpc_fl_pll0_lock", "", "[31:0]", "read-only")
    txt += generate_register_aon_sysconsaif_syscfg_full(36, "u0_otpc_fl_pll1_lock", "", "[31:0]", "read-only")
    txt += generate_register_aon_sysconsaif_syscfg40()

    return txt + """\
              </registers>
"""

def generate_register_aon_sysconsaif_syscfg12():
    txt = """\
                <register>
                  <name>aon_sysconsaif_syscfg12</name>
                  <description>AON SYSCONSAIF SYSCFG 12</description>
                  <addressOffset>0xc</addressOffset>
                  <size>32</size>
                  <fields>
"""

    txt += generate_field("u0_boot_ctrl_boot_vector_35_32", "", "[3:0]", "read-only")
    txt += generate_fields_sram_config("gmac5_axi64_scfg_ram_cfg", 0x4)
    txt += generate_field("gmac5_axi64_mac_speed_o", "", "[17:16]", "read-only")

    desc = "Active PHY Selected. When you have multiple GMAC PHY interfaces in your configuration, this field indicates the sampled value of the PHY selector during reset de-assertion. Values: 0x0 - GMII or MII, 0x1 - RGMII, 0x2 - SGMII, 0x3 - TBI, 0x4 - RMII, 0x5 - RTBI, 0x6 - SMII, 0x7 - REVMII"

    txt += generate_field("gmac5_axi64_phy_intf_sel_i", desc, "[20:18]", "read-write")

    return txt + """\
                  </fields>
                </register>
"""

def generate_register_aon_sysconsaif_syscfg24():
    txt = """\
                <register>
                  <name>aon_sysconsaif_syscfg24</name>
                  <description>AON SYSCONSAIF SYSCFG 24</description>
                  <addressOffset>0x18</addressOffset>
                  <size>32</size>
                  <fields>
"""

    txt += generate_field("u0_otpc_chip_mode", "", "[0:0]", "read-only")
    txt += generate_field("u0_otpc_crc_pass", "", "[1:1]", "read-only")
    txt += generate_field("u0_otpc_dbg_enable", "", "[2:2]", "read-only")

    return txt + """\
                  </fields>
                </register>
"""

def generate_register_aon_sysconsaif_syscfg40():
    txt = """\
                <register>
                  <name>aon_sysconsaif_syscfg40</name>
                  <description>AON SYSCONSAIF SYSCFG 40</description>
                  <addressOffset>0x28</addressOffset>
                  <size>32</size>
                  <fields>
"""

    txt += generate_field("u0_otpc_fl_sec_boot_lmt", "", "[0:0]", "read-only")
    txt += generate_field("u0_otpc_fl_xip", "", "[1:1]", "read-only")
    txt += generate_field("u0_otpc_load_busy", "", "[2:2]", "read-only")
    txt += generate_field("u0_reset_ctrl_clr_reset_status", "", "[3:3]", "read-write")
    txt += generate_field("u0_reset_ctrl_pll_timecnt_finish", "", "[4:4]", "read-only")
    txt += generate_field("u0_reset_ctrl_rstn_sw", "", "[5:5]", "read-write")
    txt += generate_field("u0_reset_ctrl_sys_reset_status", "", "[9:6]", "read-only")

    return txt + """\
                  </fields>
                </register>
"""

def generate_register_aon_sysconsaif_syscfg_full(idx, field_name, field_desc, bit_range, access):
    name = "aon_sysconsaif_syscfg{}".format(idx)
    desc = "AON SYSCONSAIF SYSCFG {}".format(idx)
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
