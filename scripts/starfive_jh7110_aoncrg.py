#!/usr/bin/env python3
# Copyleft (c) 2023 cmsis-svd-generator developers 
# SPDX-License-Identifier: Apache-2.0

from scripts.starfive_common import *

"""
This program generates CMSIS SVD xml for starfive JH7110 aoncrg
"""

def generate_registers_starfive_jh7110_aoncrg(dts, peripheral):
    """Generate xml string for registers for starfive_aoncrg peripheral"""
    txt = """\
              <registers>
"""

    txt += generate_registers_divcfg("clk_osc", "Oscillator Clock", 0x0, [4, 4, 4, 4])
    txt += generate_registers_mux_sel("clk_aon_apb", "AON APB Function Clock", 0x4, "clk_osc_div4, clk_osc") 
    txt += generate_registers_icg("clk_ahb_gmac5", "AHB GMAC5 Clock", 0x8)
    txt += generate_registers_icg("clk_axi_gmac5", "AXI GMAC5 Clock", 0xc)
    txt += generate_registers_divcfg("clk_gmac0_rmii_rtx", "GMAC0 RMII RTX Clock", 0x10, [30, 2, 2, 2])
    txt += generate_registers_mux_sel("clk_gmac5_axi64_tx", "GMAC5 AXI64 Clock Transmitter", 0x14, "u0_sys_crg_clk_gmac0_gtxclk, clk_gmac0_rmii_rtx") 
    txt += generate_registers_clk_polarity("clk_gmac5_axi64_txi", "GMAC5 AXI64 Clock Transmission Inverter", 0x18) 
    txt += generate_registers_dly_chain_sel("clk_gmac5_axi64_rx", "GMAC5 AXI64 Clock Receiver", 0x1c) 
    txt += generate_registers_clk_polarity("clk_gmac5_axi64_rxi", "GMAC5 AXI64 Clock Receiving Inverter", 0x20) 
    txt += generate_registers_icg("clk_optc_apb", "OPTC APB Clock", 0x24)
    txt += generate_registers_icg("clk_rtc_hms_apb", "RTC HMS APB Clock", 0x28)
    txt += generate_registers_divcfg("clk_rtc_internal", "RTC Internal Clock", 0x2c, [1022, 750, 750, 750])
    txt += generate_registers_mux_sel("clk_rtc_hms_osc32k", "RTC HMS Clock Oscillator 32K", 0x30, "clk_rtc, clk_rtc_internal") 
    txt += generate_registers_icg("clk_rtc_hms_cal", "RTC HMS Clock Calculator", 0x34)
    txt += generate_registers_aon_rst_sel("soft_rst_addr_sel", "Software RESET Address Selector", 0x38)
    txt += generate_registers_aon_rst_sel("aoncrg_rst_status", "AONCRG RESET Status", 0x3c)

    txt += """\
              </registers>
"""
    return txt
