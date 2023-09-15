#!/usr/bin/env python3
# Copyleft (c) 2023 cmsis-svd-generator developers 
# SPDX-License-Identifier: Apache-2.0

"""
This program generates CMSIS SVD xml for starfive JH7110 syscrg
"""

def generate_registers_starfive_jh7110_syscrg(dts, peripheral):
    """Generate xml string for registers for starfive_syscrg peripheral"""
    clock_namess = peripheral.get_fields("clock-names")
    cpus = dts.get_by_path("/cpus")
    txt = """\
              <registers>
"""

    txt += generate_registers_mux_sel("clk_cpu_root", "Clock CPU Root", 0x0, "clk_osc, clk_pll0")
    txt += generate_registers_divcfg("clk_cpu_core", "Clock CPU Core", 0x4, [7, 1, 1, 1])
    txt += generate_registers_divcfg("clk_cpu_bus", "Clock CPU Bus", 0x8, [2, 2, 2, 2])
    txt += generate_registers_mux_sel("clk_gpu_root", "Clock GPU Root", 0xc, "clk_pll2, clk_pll1")
    txt += generate_registers_mux_sel_divcfg("clk_peripheral_root", "Clock Peripheral Root", 0x10, "clk_pll0, clk_pll2", [2, 2, 2, 2])
    txt += generate_registers_mux_sel("clk_bus_root", "Clock Bus Root", 0x14, "clk_osc, clk_pll2")
    txt += generate_registers_divcfg("clk_nocstg_bus", "Clock NOCSTG Bus", 0x18, [3, 3, 3, 3])
    txt += generate_registers_divcfg("clk_axi_cfg0", "Clock AXI Configuration 0", 0x1c, [3, 3, 3, 3])
    txt += generate_registers_divcfg("clk_stg_axiahb", "Clock STG AXI AHB", 0x20, [2, 2, 2, 2])

    for idx in range(0, 2):
        txt += generate_registers_icg("clk_ahb{}".format(idx), "Clock AHB " + str(idx), 0x24 + (idx * 4))

    txt += generate_registers_divcfg("clk_apb_bus", "Clock APB Bus", 0x2c, [8, 4, 4, 4])
    txt += generate_registers_icg("clk_apb0", "Clock APB 0", 0x30)

    for idx in range(0, 3):
        txt += generate_registers_divcfg("clk_pll{}_div2".format(idx), "Clock PLL {} Divider 2".format(idx), 0x34 + (idx * 4), [2, 2, 2, 2])

    txt += generate_registers_divcfg("clk_audio_root", "Clock Audio Root", 0x40, [8, 2, 2, 2])
    txt += generate_registers_divcfg("clk_mclk_inner", "Clock MCLK Inner", 0x44, [64, 12, 12, 12])
    txt += generate_registers_mux_sel("clk_mclk", "Clock MCLK", 0x48, "clk_mclk_inner, clk_mclk_ext")
    txt += generate_registers_icg("clk_mclk_out", "Clock MCLK Out", 0x4c)
    txt += generate_registers_mux_sel_divcfg("clk_isp_2x", "Clock ISP 2x", 0x50, "clk_pll2, clk_pll1", [8, 2, 2, 2])
    txt += generate_registers_divcfg("clk_isp_axi", "Clock ISP AXI", 0x54, [4, 2, 2, 2])

    mdmt = [
            [62, 20, 16, 20],
            [62, 16, 16, 16],
            [62, 12, 12, 12],
    ]
    for idx in range(0, 3):
        txt += generate_registers_icg_divcfg("clk_gclk{}".format(idx), "Clock GCLK {}".format(idx), 0x58 + (idx * 4), mdmt[idx])


    for idx in range(0, 5):
        txt += generate_registers_icg("clk_u7mc_core{}".format(idx), "U7MC Core Clock {}".format(idx), 0x64 + (idx * 4))

    txt += generate_registers_icg("clk_u7mc_debug", "U7MC Debug Clock", 0x78)
    txt += generate_registers_divcfg("u7mc_rtc_toggle", "U7MC RTC Toggle", 0x7c, [6, 6, 6, 6])

    for idx in range(0, 5):
        txt += generate_registers_icg("clk_u7mc_trace{}".format(idx), "U7MC Trace Clock {}".format(idx), 0x80 + (idx * 4))

    txt += generate_registers_icg("clk_u7mc_trace_com", "U7MC Trace Clock COM", 0x94)
    txt += generate_registers_icg("clk_u0_sft7110_noc_bus_clk_cpu_axi", "clk_u0_sft7110_noc_bus_clk_cpu_axi", 0x98)
    txt += generate_registers_icg("clk_u0_sft7110_noc_bus_clk_axicfg0_axi", "clk_u0_sft7110_noc_bus_clk_axicfg0_axi", 0x9c)
    txt += generate_registers_divcfg("clk_osc_div2", "clk_osc_div2", 0xa0, [2, 2, 2, 2])
    txt += generate_registers_divcfg("clk_pll1_div4", "clk_pll1_div4", 0xa4, [2, 2, 2, 2])
    txt += generate_registers_divcfg("clk_pll1_div8", "clk_pll1_div8", 0xa8, [2, 2, 2, 2])
    txt += generate_registers_mux_sel("clk_ddr_bus", "clk_ddr_bus", 0xac, "clk_osc_div2, clk_pll1_div4, clk_pll1_div8")
    txt += generate_registers_icg("clk_u0_ddr_sft7110_clk_axi", "clk_u0_ddr_sfft7110_clk_axi", 0xb0)
    txt += generate_registers_divcfg("clk_gpu_core", "clk_gpu_core", 0xb4, [7, 3, 3, 3])
    txt += generate_registers_icg("clk_u0_img_gpu_core_clk", "clk_u0_img_gpu_core_clk", 0xb8)
    txt += generate_registers_icg("clk_u0_img_gpu_sys_clk", "clk_u0_img_gpu_sys_clk", 0xbc)
    txt += generate_registers_icg("clk_u0_img_gpu_clk_apb", "clk_u0_img_gpu_clk_apb", 0xc0)
    txt += generate_registers_icg_divcfg("clk_u0_gpu_rtc_toggle", "clk_u0_gpu_rtc_toggle", 0xc4, [12, 12, 12, 12])
    txt += generate_registers_icg("clk_u0_sft7110_noc_bus_clk_gpu_axi", "clk_u0_sft7110_noc_bus_clk_gpu_axi", 0xc8)
    txt += generate_registers_icg("clk_u0_dom_isp_top_clk_dom_isp_top_clk_ispcore_2x", "clk_u0_dom_isp_top_clk_dom_isp_top_clk_ispcore_2x", 0xcc)
    txt += generate_registers_icg("clk_u0_dom_isp_top_clk_dom_isp_top_clk_isp_axi", "clk_u0_dom_isp_top_clk_dom_isp_top_clk_isp_axi", 0xd0)
    txt += generate_registers_icg("clk_u0_sft7110_noc_bux_clk_isp_axi", "clk_u0_sft7110_noc_bux_clk_isp_axi", 0xd4)
    txt += generate_registers_divcfg("clk_hifi4_core", "clk_hifi4_core", 0xd8, [15, 3, 3, 3])
    txt += generate_registers_divcfg("clk_hifi4_axi", "clk_hifi4_axi", 0xdc, [2, 2, 2, 2])
    txt += generate_registers_icg("clk_u0_axi_cfg1_dec_clk_main", "clk_u0_axi_cfg1_dec_clk_main", 0xe0)
    txt += generate_registers_icg("clk_u0_axi_cfg1_dec_clk_ahb", "clk_u0_axi_cfg1_dec_clk_ahb", 0xe4)
    txt += generate_registers_icg("clk_u0_dom_vout_top_clk_dom_vout_top_clk_vout_src", "clk_u0_dom_vout_top_clk_dom_vout_top_clk_vout_src", 0xe8)
    txt += generate_registers_divcfg("clk_vout_axi", "Clock Video Output AXI", 0xec, [7, 2, 2, 2])
    txt += generate_registers_icg("clk_noc_display_axi", "Clock NOC Display AXI", 0xf0)
    txt += generate_registers_icg("clk_vout_ahb", "Clock Video Output AHB", 0xf4)
    txt += generate_registers_icg("clk_vout_axi", "Clock Video Output AXI", 0xf8)
    txt += generate_registers_icg("clk_vout_hdmi_tx0_mclk", "Clock Video Output HDMI TX0 MCLK", 0xfc)
    txt += generate_registers_divcfg("clk_vout_mipi_phy", "Clock Video Output MIPI PHY Reference", 0x100, [2, 2, 2, 2])
    txt += generate_registers_divcfg("clk_jpeg_codec_axi", "Clock JPEG Codec AXI", 0x104, [16, 6, 6, 6])
    txt += generate_registers_icg("clk_codaj12_axi", "CODAJ12 Clock AXI", 0x108)
    txt += generate_registers_icg_divcfg("clk_codaj12_core", "CODAJ12 Clock Core", 0x10c, [16, 6, 6, 6])
    txt += generate_registers_icg("clk_codaj12_apb", "CODAJ12 Clock APB", 0x110)
    txt += generate_registers_divcfg("clk_vdec_axi", "Clock Video Decoder AXI", 0x114, [7, 3, 3, 3])
    txt += generate_registers_icg("clk_wave511_axi", "Clock WAVE511 AXI", 0x118)
    txt += generate_registers_icg_divcfg("clk_wave511_bpu", "Clock WAVE511 BPU", 0x11c, [7, 3, 3, 3])
    txt += generate_registers_icg_divcfg("clk_wave511_vce", "Clock WAVE511 VCE", 0x120, [7, 2, 3, 2])
    txt += generate_registers_icg("clk_wave511_apb", "Clock WAVE511 APB", 0x124)
    txt += generate_registers_icg("clk_wave511_jpg_arb", "Clock WAVE511 JPG ARB", 0x128)
    txt += generate_registers_icg("clk_wave511_jpg_main", "Clock WAVE511 JPG Main", 0x12c)
    txt += generate_registers_icg("clk_noc_vdec_axi", "Clock NOC Video Decoder AXI", 0x130)
    txt += generate_registers_divcfg("clk_venc_axi", "Clock Video Encoder AXI", 0x134, [15, 5, 5, 5])
    txt += generate_registers_icg("clk_wave420l_axi", "Clock WAVE420L AXI", 0x138)
    txt += generate_registers_icg_divcfg("clk_wave420l_bpu", "Clock WAVE420L BPU", 0x13c, [15, 5, 5, 5])
    txt += generate_registers_icg_divcfg("clk_wave420l_vce", "Clock WAVE420L VCE", 0x140, [15, 5, 5, 5])
    txt += generate_registers_icg("clk_wave420l_apb", "Clock WAVE420L APB", 0x144)
    txt += generate_registers_icg("clk_noc_venc_axi", "Clock NOC Video Encoder AXI", 0x148)
    txt += generate_registers_icg("clk_axi_cfg0_dec_main_div", "Clock AXI Config 0 DEC Main Divider", 0x14c)
    txt += generate_registers_icg("clk_axi_cfg0_dec_main", "Clock AXI Config 0 DEC Main", 0x150)
    txt += generate_registers_icg("clk_axi_cfg0_dec_hifi4", "Clock AXI Config 0 DEC HIFI4", 0x154)
    txt += generate_registers_icg("clk_aximem_128b_axi", "Clock AXIMEM 128B AXI", 0x158)
    txt += generate_registers_icg("clk_qspi_ahb", "Clock QSPI AHB", 0x15c)
    txt += generate_registers_icg("clk_qspi_apb", "Clock QSPI APB", 0x160)
    txt += generate_registers_divcfg("clk_qspi_ref_src", "Clock QSPI Reference Source", 0x164, [16, 10, 10, 10])
    txt += generate_registers_icg_mux_sel("clk_qspi_ref", "Clock QSPI Reference", 0x168, "clk_osc, clk_qspi_ref_src")

    for idx in range(0, 2):
        txt += generate_registers_icg("clk_u{}_sd_ahb".format(idx), "U{} SD Clock AHB".format(idx), 0x16c + (idx * 0x4))

    for idx in range(0, 2):
        txt += generate_registers_icg_divcfg("clk_u{}_sd_card".format(idx), "U{} SD Card Clock".format(idx), 0x174 + (idx * 0x4), [15, 2, 2, 2])

    txt += generate_registers_divcfg("clk_usb_125m", "Clock USB 125M", 0x17c, [15, 8, 12, 10])
    txt += generate_registers_icg("clk_noc_stg_axi", "Clock NOC STG AXI", 0x180)
    txt += generate_registers_icg("clk_gmac5_axi64_ahb", "Clock GMAC 5 AXI 64 AHB", 0x184)
    txt += generate_registers_icg("clk_gmac5_axi64_axi", "Clock GMAC 5 AXI 64 AXI", 0x188)
    txt += generate_registers_divcfg("clk_gmac_src", "Clock GMAC Source", 0x18c, [7, 2, 2, 2])
    txt += generate_registers_divcfg("clk_gmac1_gtx", "Clock GMAC 1 GTX", 0x190, [15, 8, 12, 10])
    txt += generate_registers_divcfg("clk_gmac1_rmii_rtx", "Clock GMAC 1 RMII RTX", 0x194, [30, 2, 2, 2])
    txt += generate_registers_icg_divcfg("clk_gmac5_axi64_ptp", "Clock GMAC 5 AXI 64 PTP", 0x198, [31, 10, 15, 10])
    txt += generate_registers_dly_chain_sel("clk_gmac5_axi64_rx", "Clock GMAC 5 AXI 64 RX", 0x19c)
    txt += generate_registers_clk_polarity("clk_gmac5_axi64_rxi", "Clock GMAC 5 AXI 64 RX Inverter", 0x1a0)
    txt += generate_registers_icg_mux_sel("clk_gmac5_axi64_tx", "Clock GMAC 5 AXI 64 TX", 0x1a4, "clk_gmac1_gtxclk, clk_gmac1_rmii_rtx")
    txt += generate_registers_clk_polarity("clk_gmac5_axi64_txi", "Clock GMAC 5 AXI 64 TX Inverter", 0x1a8)
    txt += generate_registers_dly_chain_sel("clk_gmac1_gtxclk", "Clock GMAC 1 GTXC", 0x1ac)
    txt += generate_registers_icg_divcfg("clk_gmac0_gtx", "Clock GMAC 0 GTX", 0x1b0, [15, 8, 12, 10])
    txt += generate_registers_icg_divcfg("clk_gmac0_ptp", "Clock GMAC 0 PTP", 0x1b4, [31, 10, 15, 25])
    txt += generate_registers_icg_divcfg("clk_gmac_phy", "Clock GMAC PHY", 0x1b8, [31, 10, 15, 25])
    txt += generate_registers_dly_chain_sel("clk_gmac0_gtxclk", "Clock GMAC 0 GTXC", 0x1bc)
    txt += generate_registers_icg("clk_sys_iomux_pclk", "Clock SYS IOMUX PCLK", 0x1c0)
    txt += generate_registers_icg("clk_mbox_apb", "Clock Mailbox APB", 0x1c4)
    txt += generate_registers_icg("clk_internal_ctrl_apb", "Clock Internal Controller APB", 0x1c8)

    for idx in range(0, 2):
        txt += generate_registers_icg("clk_u{}_can_ctrl_apb".format(idx), "U{} Clock CAN Controller APB".format(idx), 0x1cc + (idx * 0xc))
        txt += generate_registers_icg_divcfg("clk_u{}_can_ctrl_tim".format(idx), "U{} Clock CAN Controller Timer".format(idx), 0x1d0 + (idx * 0xc), [24, 24, 6, 24])
        txt += generate_registers_icg_divcfg("clk_u{}_can_ctrl_can".format(idx), "U{} Clock CAN Controller CAN".format(idx), 0x1d4 + (idx * 0xc), [63, 8, 8, 8])

    txt += generate_registers_icg("clk_pwm_apb", "Clock PWM APB", 0x1e4)
    txt += generate_registers_icg("clk_wdt_apb", "Clock WDT APB", 0x1e8)
    txt += generate_registers_icg("clk_wdt", "Clock WDT", 0x1ec)
    txt += generate_registers_icg("clk_tim_apb", "Clock Timer APB", 0x1f0)

    for idx in range(0, 4):
        txt += generate_registers_icg("clk_tim{}".format(idx), "Clock Timer {}".format(idx), 0x1f4 + (idx * 4))

    txt += generate_registers_icg("clk_temp_sensor_apb", "Clock Temperature Sensor APB", 0x204)
    txt += generate_registers_icg_divcfg("clk_temp_sensor", "Clock Temperature Sensor", 0x208, [24, 24, 24, 24])

    for idx in range(0, 7):
        txt += generate_registers_icg("clk_u{}_spi_apb".format(idx), "U{} Clock SPI APB".format(idx), 0x20c + (idx * 4))

    for idx in range(0, 7):
        txt += generate_registers_icg("clk_u{}_i2c_apb".format(idx), "U{} Clock I2C APB".format(idx), 0x228 + (idx * 4))

    for idx in range(0, 3):
        txt += generate_registers_icg("clk_u{}_uart_apb".format(idx), "U{} Clock UART APB".format(idx), 0x244 + (idx * 8))
        txt += generate_registers_icg("clk_u{}_uart_core".format(idx), "U{} Clock UART Core".format(idx), 0x248 + (idx * 8))

    for idx in range(3, 6):
        txt += generate_registers_icg("clk_u{}_uart_apb".format(idx), "U{} Clock UART APB".format(idx), 0x244 + (idx * 8))
        txt += generate_registers_icg_divcfg("clk_u{}_uart_core".format(idx), "U{} Clock UART Core".format(idx), 0x248 + (idx * 8), [131071, 2560, 2560, 2560])

    txt += generate_registers_icg("clk_pwmdac_apb", "Clock PWMDAC APB", 0x274)
    txt += generate_registers_icg_divcfg("clk_pwmdac_core", "Clock PWMDAC Core", 0x278, [256, 12, 12, 12])

    txt += generate_registers_icg("clk_spdif_apb", "Clock SPDIF APB", 0x27c)
    txt += generate_registers_icg("clk_spdif_core", "Clock SPDIF Core", 0x280)

    for idx in range(0, 2):
        txt += generate_registers_icg("clk_u{}_i2s_tx_apb".format(idx), "U{} Clock I2S TX APB".format(idx), 0x284 + (idx * 0x1c))
        txt += generate_registers_icg_divcfg("clk_u{}_i2stx_4ch{}_bclk_mst".format(idx, idx), "U{} Clock I2S TX {} BCLK MST".format(idx, idx), 0x288 + (idx * 0x1c), [32, 4, 4, 4])
        txt += generate_registers_clk_polarity("clk_u{}_i2stx_4ch{}_bclk_mst_inv".format(idx, idx), "U{} Clock I2S TX {} BCLK MST Inverter".format(idx, idx), 0x28c + (idx * 0x1c))
        txt += generate_registers_mux_sel_divcfg("clk_i2stx{}_lrck_mst".format(idx), "Clock I2S TX {} LRCK MST".format(idx), 0x290 + (idx * 0x1c), "clk_i2stx_4ch0_bclk_mst_inv, clk_i2stx_4ch0_bclk_mst", [64, 64, 64, 64])
        txt += generate_registers_mux_sel("clk_u{}_i2stx_bclk".format(idx), "U{} Clock I2S TX BCLK".format(idx), 0x294 + (idx * 0x1c), "clk_i2stx_4ch{}_bclk_mst, clk_i2stx_bclk_ext".format(idx))
        txt += generate_registers_clk_polarity("clk_u{}_i2stx_bclk_neg".format(idx), "U{} Clock I2S TX BCLK Negative".format(idx), 0x298 + (idx * 0x1c))
        txt += generate_registers_mux_sel("clk_u{}_i2stx_lrck".format(idx), "U{} Clock I2S TX LRCK".format(idx), 0x29c + (idx * 0x1c), "clk_i2stx_4ch{}_lrck_mst, clk_i2stx_lrck_ext".format(idx))

    txt += generate_registers_icg("clk_i2s_apb", "Clock I2S APB", 0x2bc)
    txt += generate_registers_icg_divcfg("clk_i2s_bclk_mst", "Clock I2S BCLK MST", 0x2c0, [32, 4, 4, 4])
    txt += generate_registers_clk_polarity("clk_i2s_bclk_mst_inv", "Clock I2S BCLK MST Inverter", 0x2c4)
    txt += generate_registers_mux_sel_divcfg("clk_i2s_lrck_mst", "Clock I2S LRCK MST", 0x2c8, "clk_i2srx_3ch_bclk_mst_inv, clk_i2srx_3ch_bclk_mst", [64, 64, 64, 64])
    txt += generate_registers_mux_sel("clk_i2s_bclk", "Clock I2S BCLK", 0x2cc, "clk_i2srx_3ch_bclk_mst, clk_i2srx_3ch_bclk_ext")
    txt += generate_registers_clk_polarity("clk_i2s_bclk_neg", "Clock I2S BCLK Negative", 0x2d0)
    txt += generate_registers_mux_sel("clk_i2s_lrck", "Clock I2S LRCK", 0x2d4, "clk_i2srx_3ch_lrck_mst, clk_i2srx_3ch_lrck_ext")
    txt += generate_registers_icg_divcfg("clk_pdm_dmic", "Clock PDM DMIC", 0x2d8, [64, 8, 8, 8])

    txt += generate_registers_icg("clk_pdm_apb", "Clock PDM APB", 0x2dc)
    txt += generate_registers_icg("clk_tdm_ahb", "Clock TDM AHB", 0x2e0)
    txt += generate_registers_icg("clk_tdm_ahb", "Clock TDM APB", 0x2e4)
    txt += generate_registers_icg_divcfg("clk_tdm_internal", "Clock TDM Internal", 0x2e8, [64, 1, 1, 1])
    txt += generate_registers_mux_sel("clk_tdm", "Clock TDM", 0x2ec, "clk_tdm_internal, clk_tdm_ext")
    txt += generate_registers_clk_polarity("clk_tdm_neg", "Clock TDM Negative", 0x2f0)

    txt += generate_registers_divcfg("clk_jtag_cert_trng", "Clock JTAG Certification TRNG", 0x2f4, [4, 4, 4, 4])

    for idx in range(0, 4):
        name = "soft_rst{}_addr_sel".format(idx)
        desc = "Software RESET {} Address Selector".format(idx)
        txt += generate_registers_rst_sel(name, desc, idx, 0x2f8 + (idx * 4))

    for idx in range(0, 4):
        name = "syscrg_rst{}_status".format(idx)
        desc = "SYSCRG RESET Status {}".format(idx)
        txt += generate_registers_rst_sel(name, desc, idx, 0x308 + (idx * 4))

    txt += """\
              </registers>
"""
    return txt

def generate_registers_mux_sel(name, desc, addr, field_desc):
    """Generate xml string for starfive_jh7110_syscrg """ + name + """ register"""
    return """\
                <register>
                  <name>""" + name + """</name>
                  <description>""" + desc + """</description>
                  <addressOffset>""" + "0x{:x}".format(addr) + """</addressOffset>
                  <size>32</size>
                  <fields>
""" + generate_field_mux_sel(field_desc) + """\
                  </fields>
                </register>
"""

def generate_registers_divcfg(name, desc, addr, mdmt):
    """Generate xml string for starfive_jh7110_syscrg """ + name + """ register"""

    return """\
                <register>
                  <name>""" + name + """</name>
                  <description>""" + desc + """</description>
                  <addressOffset>""" + "0x{:x}".format(addr) + """</addressOffset>
                  <size>32</size>
                  <fields>
""" + generate_field_divcfg(mdmt) + """\
                  </fields>
                </register>
"""

def generate_registers_mux_sel_divcfg(name, desc, addr, field_desc, mdmt):
    """Generate xml string for starfive_jh7110_syscrg """ + name + """ register"""

    return """\
                <register>
                  <name>""" + name + """</name>
                  <description>""" + desc + """</description>
                  <addressOffset>""" + "0x{:x}".format(addr) + """</addressOffset>
                  <size>32</size>
                  <fields>
""" + generate_field_mux_sel(field_desc) + """\
""" + generate_field_divcfg(mdmt) + """\
                  </fields>
                </register>
"""

def generate_registers_icg(name, desc, addr):
    """Generate xml string for starfive_jh7110_syscrg """ + name + """ register"""

    return """\
                <register>
                  <name>""" + name + """</name>
                  <description>""" + desc + """</description>
                  <addressOffset>""" + "0x{:x}".format(addr) + """</addressOffset>
                  <size>32</size>
                  <fields>
""" + generate_field_icg() + """\
                  </fields>
                </register>
"""

def generate_registers_icg_divcfg(name, desc, addr, mdmt):
    """Generate xml string for starfive_jh7110_syscrg """ + name + """ register"""

    return """\
                <register>
                  <name>""" + name + """</name>
                  <description>""" + desc + """</description>
                  <addressOffset>""" + "0x{:x}".format(addr) + """</addressOffset>
                  <size>32</size>
                  <fields>
""" + generate_field_icg() + """\
""" + generate_field_divcfg(mdmt) + """\
                  </fields>
                </register>
"""

def generate_registers_icg_mux_sel(name, desc, addr, field_desc):
    """Generate xml string for starfive_jh7110_syscrg """ + name + """ register"""

    return """\
                <register>
                  <name>""" + name + """</name>
                  <description>""" + desc + """</description>
                  <addressOffset>""" + "0x{:x}".format(addr) + """</addressOffset>
                  <size>32</size>
                  <fields>
""" + generate_field_icg() + """\
""" + generate_field_mux_sel(field_desc) + """\
                  </fields>
                </register>
"""

def generate_registers_dly_chain_sel(name, desc, addr):
    """Generate xml string for starfive_jh7110_syscrg """ + name + """ register"""
    return """\
                <register>
                  <name>""" + name + """</name>
                  <description>""" + desc + """</description>
                  <addressOffset>""" + "0x{:x}".format(addr) + """</addressOffset>
                  <size>32</size>
                  <fields>
""" + generate_field_dly_chain_sel() + """\
                  </fields>
                </register>
"""

def generate_registers_clk_polarity(name, desc, addr):
    """Generate xml string for starfive_jh7110_syscrg """ + name + """ register"""
    return """\
                <register>
                  <name>""" + name + """</name>
                  <description>""" + desc + """</description>
                  <addressOffset>""" + "0x{:x}".format(addr) + """</addressOffset>
                  <size>32</size>
                  <fields>
""" + generate_field_clk_polarity() + """\
                  </fields>
                </register>
"""

def generate_registers_rst_sel(name, desc, idx, addr):

    """Generate xml string for starfive_jh7110_syscrg """ + name + """ register"""

    return """\
                <register>
                  <name>""" + name + """</name>
                  <description>""" + desc + """</description>
                  <addressOffset>""" + "0x{:x}".format(addr) + """</addressOffset>
                  <size>32</size>
""" + generate_field_rst_sel(idx) + """\
                </register>
"""

def generate_field_mux_sel(field_desc):
    return """\
                    <field>
                      <name>clk_mux_sel</name>
                      <description>Clock multiplexing selector: """ + field_desc + """</description>
                      <bitRange>[29:24]</bitRange>
                      <access>read-write</access>
                    </field>
"""

def generate_field_divcfg(mdmt):
    field_desc = "Clock divider coefficient: Max=" + str(mdmt[0])
    field_desc += ", Default=" + str(mdmt[1])
    field_desc += ", Min=" + str(mdmt[2])
    field_desc += ", Typical=" + str(mdmt[3])

    return """\
                    <field>
                      <name>clk_divcfg</name>
                      <description>""" + field_desc + """</description>
                      <bitRange>[23:0]</bitRange>
                      <access>read-write</access>
                    </field>
"""

def generate_field_icg():
    return """\
                    <field>
                      <name>clk_icg</name>
                      <description>1: Clock enable, 0: Clock disable</description>
                      <bitRange>[31:31]</bitRange>
                      <access>read-write</access>
                    </field>
"""

def generate_field_dly_chain_sel():
    return """\
                    <field>
                      <name>dly_chain_sel</name>
                      <description>Selector delay chain stage number, totally 32 stages, -50 ps each stage. The register value indicates the delay chain stage number. For example, diy_chain_sel=1 means to delay 1 stage.</description>
                      <bitRange>[23:0]</bitRange>
                      <access>read-write</access>
                    </field>
"""

def generate_field_clk_polarity():
    return """\
                    <field>
                      <name>clk_polarity</name>
                      <description>1: Clock inverter, 0: Clock buffer</description>
                      <bitRange>[30:30]</bitRange>
                      <access>read-write</access>
                    </field>
"""

def generate_field_rst_sel(idx):
    names = [
        [
            "rstn_u0_jtag2apb_presetn", "rstn_u0_sys_syscon_presetn", "rstn_u0_sys_iomux_presetn", "rst_u0_u7mc_sft7110_rst_bus",
            "rst_u0_u7mc_sft7110_debug_reset", "rst_u0_u7mc_sft7110_rst_core0", "rst_u0_u7mc_sft7110_rst_core1", "rst_u0_u7mc_sft7110_rst_core2",
            "rst_u0_u7mc_sft7110_rst_core3", "rst_u0_u7mc_sft7110_rst_core4", "rst_u0_u7mc_sft7110_rst_core0_st", "rst_u0_u7mc_sft7110_rst_core1_st",
            "rst_u0_u7mc_sft7110_rst_core2_st", "rst_u0_u7mc_sft7110_rst_core3_st", "rst_u0_u7mc_sft7110_rst_core4_st", "rst_u0_u7mc_sft7110_trace_rst0",
            "rst_u0_u7mc_sft7110_trace_rst1", "rst_u0_u7mc_sft7110_trace_rst2", "rst_u0_u7mc_sft7110_trace_rst3", "rst_u0_u7mc_sft7110_trace_rst4",
            "rst_u0_u7mc_sft7110_trace_com_rst", "rst_u0_img_gpu_rstn_apb", "rst_u0_img_gpu_rstn_doma", "rst_u0_u7mc_sft7110_noc_bus_reset_apb_bus_n",
            "rst_u0_u7mc_sft7110_noc_bus_reset_axicfg0_axi_n", "rst_u0_u7mc_sft7110_noc_bus_reset_cpu_axi_n", "rst_u0_u7mc_sft7110_noc_bus_reset_disp_axi_n", "rst_u0_u7mc_sft7110_noc_bus_reset_gpu_axi_n",
            "rst_u0_u7mc_sft7110_noc_bus_reset_isp_axi_n", "rst_u0_u7mc_sft7110_noc_bus_reset_ddrc_n", "rst_u0_u7mc_sft7110_noc_bus_reset_stg_axi_n", "rst_u0_u7mc_sft7110_noc_bus_reset_vdec_axi_n",
        ],
        [
            "rstn_u0_sft7100_noc_bus_reset_venc_axi_n", "rstn_u0_axi_cfg1_dec_rstn_ahb", "rstn_u0_axi_cfg1_dec_rstn_main", "rstn_u0_axi_cfg0_dec_rstn_main",
            "rstn_u0_axi_cfg0_dec_rstn_main_div", "rstn_u0_axi_cfg0_dec_rstn_hifi4", "rstn_u0_ddr_sft7110_rstn_axi", "rstn_u0_ddr_sft7110_rstn_osc",
            "rstn_u0_ddr_sft7110_rstn_apb", "rstn_u0_dom_isp_top_rstn_dom_isp_top_ip_top_reset_n", "rstn_u0_dom_isp_top_rstn_dom_isp_top_rstn_isp_axi", "rstn_u0_dom_vout_top_rstn_dom_vout_top_rstn_vout_src",
            "rstn_u0_codaj12_rstn_axi", "rstn_u0_codaj12_rstn_core", "rstn_u0_codaj12_rstn_apb", "rstn_u0_wave511_rstn_axi",
            "rstn_u0_wave511_rstn_bpu", "rstn_u0_wave511_rstn_vce", "rstn_u0_wave511_rstn_apb", "rstn_u0_vdec_jpg_arb_jpgresetn",
            "rstn_u0_vdec_jpg_arb_mainresetn", "rstn_u0_aximem_128b_rstn_axi", "rstn_u0_wave420l_rstn_axi", "rstn_u0_wave420l_rstn_bpu",
            "rstn_u0_wave420l_rstn_vce", "rstn_u0_wave420l_rstn_apb", "rstn_u1_aximem_128b_rstn_axi", "rstn_u2_aximem_128b_rstn_axi",
            "rstn_u0_intmem_rom_sram_rstn_rom", "rstn_u0_cdns_qspi_rstn_ahb", "rstn_u0_cdns_qspi_rstn_apb", "rstn_u0_cdns_qspi_rstn_ref",
        ],
        [
            "rstn_u0_sdio_rstn_ahb", "rstn_u1_sdi_rstn_ahb", "rstn_u1_gmac5_axi64_aresetn_i", "rstn_u1_gmac5_axi64_hresetn_n",
            "rstn_u0_mailbox_presetn", "rstn_u0_ssp_spi_rstn_apb", "rstn_u1_ssp_spi_rstn_apb", "rstn_u2_ssp_spi_rstn_apb",
            "rstn_u3_ssp_spi_rstn_apb", "rstn_u4_ssp_spi_rstn_apb", "rstn_u5_ssp_spi_rstn_apb", "rstn_u6_ssp_spi_rstn_apb",
            "rstn_u0_i2c_rstn_apb", "rstn_u1_i2c_rstn_apb", "rstn_u2_i2c_rstn_apb", "rstn_u3_i2c_rstn_apb",
            "rstn_u4_i2c_rstn_apb", "rstn_u5_i2c_rstn_apb", "rstn_u6_i2c_rstn_apb", "rstn_u0_uart_rstn_apb",
            "rstn_u0_uart_rstn_core", "rstn_u1_uart_rstn_apb", "rstn_u1_uart_rstn_core", "rstn_u2_uart_rstn_apb",
            "rstn_u2_uart_rstn_core", "rstn_u3_uart_rstn_apb", "rstn_u3_uart_rstn_core", "rstn_u4_uart_rstn_apb",
            "rstn_u4_uart_rstn_core", "rstn_u5_uart_rstn_apb", "rstn_u6_uart_rstn_core", "rstn_u0_cdns_spdif_rstn_apb",
        ],
        [
            "rstn_u0_pwmdac_rstn_apb", "rstn_u0_pdm_4mic_rstn_dmic", "rstn_u0_pdm_4mic_rstn_apb", "rstn_u0_i2srx_3ch_rstn_apb",
            "rstn_u0_i2srx_3ch_rstn_bclk", "rstn_u0_i2srx_3ch_rstn_apb", "rstn_u0_i2stx_4ch_rstn_bclk", "rstn_u1_i2stx_4ch_rstn_apb",
            "rstn_u1_i2stx_4ch_rstn_bclk", "rstn_u0_tdm16slot_rstn_ahb", "rstn_u0_tdm16slot_rstn_tdm", "rstn_u0_tdm16slot_rstn_apb",
            "rstn_u0_pwm_8ch_rstn_apb", "rstn_u0_dskit_wdt_rstn_apb", "rstn_u0_dskit_wdt_rstn_wdt", "rstn_u0_can_ctrl_rstn_apb",
            "rstn_u0_can_ctrl_rstn_can", "rstn_u0_can_ctrl_rstn_timer", "rstn_u1_can_ctrl_rstn_apb", "rstn_u1_can_ctrl_rstn_can",
            "rstn_u1_can_ctrl_rstn_timer", "rstn_u0_si5_timer_rstn_apb", "rstn_u0_si5_timer_rstn_timer0", "rstn_u0_si5_timer_rstn_time10",
            "rstn_u0_si5_timer_rstn_timer2", "rstn_u0_si5_timer_rstn_timer3", "rstn_u0_int_ctrl_rstn_apb", "rstn_u0_temp_sensor_rstn_apb",
            "rstn_u0_temp_sensor_rstn_temp", "rstn_u0_jtag_certification_rst_n", "", "",
        ],
    ]
    txt = """\
                  <fields>
"""
    for i in range(0, 32):
        if len(names[idx][i]) == 0:
            continue

        bit_range = "[{}:{}]".format(i, i)
        txt += """\
                    <field>
                      <name>""" + names[idx][i] + """</name>
                      <description>1: Assert reset, 0: De-assert reset</description>
                      <bitRange>""" + bit_range + """</bitRange>
                      <access>read-write</access>
                    </field>
"""

    return txt + """\
                  </fields>
"""
