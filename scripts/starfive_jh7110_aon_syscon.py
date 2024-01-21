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
    txt += generate_register_aon_sysconsaif_syscfg_full(1, "u0_boot_ctrl_boot_status", "", "[3:0]", "read-only")
    txt += generate_register_aon_sysconsaif_syscfg_full(2, "u0_boot_ctrl_boot_vector_0_31", "", "[31:0]", "read-only")
    txt += generate_register_aon_sysconsaif_syscfg12()

    for idx in range(2):
        bit = idx * 32
        txt += generate_register_aon_sysconsaif_syscfg_full(4 + idx, "gmac5_axi64_ptp_timestamp_o_{}_{}".format(bit, bit + 31), "", "[31:0]", "read-only")

    txt += generate_register_aon_sysconsaif_syscfg24()
    txt += generate_register_aon_sysconsaif_syscfg_full(7, "u0_otpc_fl_func_lock", "", "[31:0]", "read-only")
    txt += generate_register_aon_sysconsaif_syscfg_full(8, "u0_otpc_fl_pll0_lock", "", "[31:0]", "read-only")
    txt += generate_register_aon_sysconsaif_syscfg_full(9, "u0_otpc_fl_pll1_lock", "", "[31:0]", "read-only")
    txt += generate_register_aon_sysconsaif_syscfg40()

    return txt + """\
              </registers>
"""

def generate_register_aon_sysconsaif_syscfg12():
    fields = [("u0_boot_ctrl_boot_vector_35_32", "", "[3:0]", "read-only")]
    fields.extend(generate_fields_list_sram_config("gmac5_axi64_scfg_ram_cfg", 0x4))
    fields.extend([
        ("gmac5_axi64_mac_speed_o", "", "[17:16]", "read-only"),
        (
            "gmac5_axi64_phy_intf_sel_i",
            "Active PHY Selected. When you have multiple GMAC PHY interfaces in your configuration, this field indicates the sampled value of the PHY selector during reset de-assertion. Values: 0x0 - GMII or MII, 0x1 - RGMII, 0x2 - SGMII, 0x3 - TBI, 0x4 - RMII, 0x5 - RTBI, 0x6 - SMII, 0x7 - REVMII",
            "[20:18]",
            "read-write",
        )
    ])
    return generate_register("aon_syscfg_3", "AON SYSCONSAIF SYSCFG 12", 0xc, fields)

def generate_register_aon_sysconsaif_syscfg24():
    return generate_register("aon_syscfg_6", "AON SYSCONSAIF SYSCFG 24", 0x18, [
        ("u0_otpc_chip_mode", "", "[0:0]", "read-only"),
        ("u0_otpc_crc_pass", "", "[1:1]", "read-only"),
        ("u0_otpc_dbg_enable", "", "[2:2]", "read-only")
    ])

def generate_register_aon_sysconsaif_syscfg40():
    return generate_register("aon_syscfg_10", "AON SYSCONSAIF SYSCFG 40", 0x28, [
        ("u0_otpc_fl_sec_boot_lmt", "", "[0:0]", "read-only"),
        ("u0_otpc_fl_xip", "", "[1:1]", "read-only"),
        ("u0_otpc_load_busy", "", "[2:2]", "read-only"),
        ("u0_reset_ctrl_clr_reset_status", "", "[3:3]", "read-write"),
        ("u0_reset_ctrl_pll_timecnt_finish", "", "[4:4]", "read-only"),
        ("u0_reset_ctrl_rstn_sw", "", "[5:5]", "read-write"),
        ("u0_reset_ctrl_sys_reset_status", "", "[9:6]", "read-only")
    ])

def generate_register_aon_sysconsaif_syscfg_full(idx, field_name, field_desc, bit_range, access):
    name = "aon_syscfg_{}".format(idx)
    addr = idx * 4
    desc = "AON SYSCONSAIF SYSCFG {}".format(addr)

    return generate_register(name, desc, addr, [(field_name, field_desc, bit_range, access)])
