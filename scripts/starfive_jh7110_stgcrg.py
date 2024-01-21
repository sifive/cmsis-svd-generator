#!/usr/bin/env python3
# Copyleft (c) 2023 cmsis-svd-generator developers 
# SPDX-License-Identifier: Apache-2.0

from scripts.starfive_common import *

"""
This program generates CMSIS SVD xml for starfive JH7110 stgcrg
"""

def generate_registers_starfive_jh7110_stgcrg(dts, peripheral):
    """Generate xml string for registers for starfive_stgcrg peripheral"""
    clock_namess = peripheral.get_fields("clock-names")
    cpus = dts.get_by_path("/cpus")

    txt = """\
              <registers>
"""

    txt += generate_registers_icg("clk_hifi4_core", "Clock HIFI4 Core", 0x0)
    txt += generate_registers_icg("clk_usb_apb", "Clock USB APB", 0x4)
    txt += generate_registers_icg("clk_usb_utmi_apb", "Clock USB UTMI APB", 0x8)
    txt += generate_registers_icg("clk_usb_axi", "Clock USB AXI", 0xc)
    txt += generate_registers_icg_divcfg("clk_usb_ipm", "Clock USB AXI", 0x10, [2, 2, 2, 2])
    txt += generate_registers_icg_divcfg("clk_usb_stb", "Clock USB STB", 0x14, [4, 4, 4, 4])
    txt += generate_registers_icg("clk_usb_app125", "Clock USB APP 125", 0x18)
    txt += generate_registers_divcfg("clk_usb_refclk", "Clock USB Reference Clock", 0x1c, [2, 2, 2, 2])

    for idx in range(0, 2):
        txt += generate_registers_icg("clk_u{}_pcie_axi_mst0".format(idx), "U{} Clock PCIe AXI MST 0".format(idx), 0x20 + (idx * 0xc))
        txt += generate_registers_icg("clk_u{}_pcie_apb".format(idx), "U{} Clock PCIe APB".format(idx), 0x24 + (idx * 0xc))
        txt += generate_registers_icg("clk_u{}_pcie_tl".format(idx), "U{} Clock PCIe TL".format(idx), 0x28 + (idx * 0xc))

    txt += generate_registers_icg("clk_pcie01_slv_dec_main", "Clock PCIe 01 SLV DEC Main", 0x38)
    txt += generate_registers_icg("clk_sec_hclk", "Clock Security HCLK", 0x3c)
    txt += generate_registers_icg("clk_sec_misc_ahb", "Clock Security Miscellaneous AHB", 0x40)

    for idx in range(0, 2):
        txt += generate_registers_icg("clk_stg_mtrx_group{}_main".format(idx), "Clock STG MTRX Group {} Main".format(idx), 0x44 + (idx * 0xc))
        txt += generate_registers_icg("clk_stg_mtrx_group{}_bus".format(idx), "Clock STG MTRX Group {} Bus".format(idx), 0x48 + (idx * 0xc))
        txt += generate_registers_icg("clk_stg_mtrx_group{}_stg".format(idx), "Clock STG MTRX Group {} STG".format(idx), 0x4c + (idx * 0xc))

    txt += generate_registers_icg("clk_stg_mtrx_group1_hifi", "Clock STG MTRX Group 1 HIFI", 0x5c)
    txt += generate_registers_icg_divcfg("clk_e2_rtc", "Clock E2 RTC", 0x60, [24, 24, 24, 24])
    txt += generate_registers_icg("clk_e2_core", "Clock E2 Core", 0x64)
    txt += generate_registers_icg("clk_e2_dbg", "Clock E2 DBG", 0x68)
    txt += generate_registers_icg("clk_dma_axi", "Clock DMA AXI", 0x6c)
    txt += generate_registers_icg("clk_dma_ahb", "Clock DMA AHB", 0x70)
    txt += generate_registers_rst_stat("soft_rst_addr_sel", "Software RESET Address Selector", 0x74)
    txt += generate_registers_rst_stat("stgcrg_rst_stat", "STGCRG RESET Status", 0x78)

    txt += """\
              </registers>
"""
    return txt
