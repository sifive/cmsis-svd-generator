#!/usr/bin/env python3
# Copyleft (c) 2023 cmsis-svd-generator developers 
# SPDX-License-Identifier: Apache-2.0

from scripts.starfive_common import *

"""
This program generates CMSIS SVD xml for starfive JH7110 stg_syscon 
"""

def generate_registers_starfive_jh7110_stg_syscon(dts, peripheral):
    """Generate xml string for registers for starfive_stg_syscon peripheral"""
    txt = """\
              <registers>
"""

    txt += generate_register_sysconsaif_syscfg0()
    txt += generate_register_sysconsaif_syscfg4()
    txt += generate_register_sysconsaif_syscfg8()
    txt += generate_register_sysconsaif_syscfg12()
    txt += generate_register_sysconsaif_syscfg_full(16, "u0_cdn_usb_xhci_debug_bus", "", "[31:0]", "read-only")
    txt += generate_register_sysconsaif_syscfg_full(20, "u0_cdn_usb_xhci_debug_link_state", "", "[30:0]", "read-only")
    txt += generate_register_sysconsaif_syscfg24()
    txt += generate_register_sysconsaif_syscfg_full(28, "u0_e2_sft7110_nmi_0_rnmi_exception_vector", "", "[31:0]", "read-write")
    txt += generate_register_sysconsaif_syscfg_full(32, "u0_e2_sft7110_nmi_0_rnmi_interrupt_vector", "", "[31:0]", "read-write")
    txt += generate_register_sysconsaif_syscfg_full(36, "u0_e2_sft7110_reset_vector_0", "", "[31:0]", "read-write")
    txt += generate_register_sysconsaif_syscfg_full(40, "u0_e2_sft7110_wfi_from_tile_0", "", "[0:0]", "read-only")
    txt += generate_register_sysconsaif_syscfg_full(44, "u0_hifi4_altresetvec", "Reset Vector Address", "[31:0]", "read-write")
    txt += generate_register_sysconsaif_syscfg48()
    txt += generate_register_sysconsaif_syscfg_full(52, "u0_hifi4_pfaultinfo", "Fault Handling Signals", "[31:0]", "read-only")
    txt += generate_register_sysconsaif_syscfg56()
    txt += generate_register_sysconsaif_syscfg60()
    txt += generate_register_sysconsaif_syscfg_full(64, "u0_hifi4_scfg_dsp_slv_offset", "The value indicates the slave port remap address", "[31:0]", "read-write")
    txt += generate_register_sysconsaif_syscfg68()

    for idx in range(0, 8):
        bit_offset = idx * 32
        txt += generate_register_sysconsaif_syscfg_full(72 + (idx * 4), "u0_plda_pcie_axi4_mst0_aratomop_{}_{}".format(31 + bit_offset, bit_offset), "", "[31:0]", "read-only")

    txt += generate_register_sysconsaif_syscfg104()

    for idx in range(0, 2):
        bit_offset = idx * 32
        txt += generate_register_sysconsaif_syscfg_full(108 + (idx * 4), "u0_plda_pcie_axi4_mst0_aruser_{}_{}".format(31 + bit_offset, bit_offset), "", "[31:0]", "read-only")

    txt += generate_register_sysconsaif_syscfg116()
    txt += generate_register_sysconsaif_syscfg_full(120, "u0_plda_pcie_axi4_mst0_a2user_31_0", "", "[31:0]", "read-only")
    txt += generate_register_sysconsaif_syscfg124()
    txt += generate_register_sysconsaif_syscfg_full(128, "u0_plda_pcie_axi4_mst0_ruser", "", "[31:0]", "read-write")
    txt += generate_register_sysconsaif_syscfg_full(132, "u0_plda_pcie_axi4_mst0_wderr", "", "[7:0]", "read-only")

    for idx in range(0, 8):
        bit_offset = idx * 32
        txt += generate_register_sysconsaif_syscfg_full(136 + (idx * 4), "u0_plda_pcie_axi4_slv0_aratomop_{}_{}".format(31 + bit_offset, bit_offset), "", "[31:0]", "read-write")

    txt += generate_register_sysconsaif_syscfg168()
    txt += generate_register_sysconsaif_syscfg_full(172, "u0_plda_pcie_axi4_slv0_aruser_31_0", "", "[31:0]", "read-write")

    txt += generate_register_sysconsaif_syscfg176()
    txt += generate_register_sysconsaif_syscfg_full(180, "u0_plda_pcie_axi4_slv0_awuser_31_0", "", "[31:0]", "read-write")

    txt += generate_register_sysconsaif_syscfg184()
    txt += generate_register_sysconsaif_syscfg_full(188, "u0_plda_pcie_axi4_slv0_ruser", "", "[31:0]", "read-only")

    txt += generate_register_sysconsaif_syscfg192()
    txt += generate_register_sysconsaif_syscfg196()

    for idx in range(0, 26):
        bit_offset = idx * 32
        txt += generate_register_sysconsaif_syscfg_full(200 + (idx * 4), "u0_plda_pcie_k_phyparam_{}_{}".format(31 + bit_offset, bit_offset), "", "[31:0]", "read-write")

    txt += generate_register_sysconsaif_syscfg304()
    txt += generate_register_sysconsaif_syscfg_full(308, "u0_plda_pcie_local_interrupt_in", "", "[31:0]", "read-write")
    txt += generate_register_sysconsaif_syscfg312()

    for idx in range(0, 3):
        txt += generate_register_sysconsaif_syscfg_full(316 + (idx * 4), "u0_plda_pcie_pf{}_offset".format(idx), "", "[19:0]", "read-write")

    txt += generate_register_sysconsaif_syscfg328()
    txt += generate_register_sysconsaif_syscfg_full(332, "u0_plda_pcie_pl_pclk_rate", "", "[4:0]", "read-only")

    for idx in range(0, 2):
        bit_offset = idx * 32
        txt += generate_register_sysconsaif_syscfg_full(336 + (idx * 4), "u0_plda_pcie_pl_sideband_in_{}_{}".format(31 + bit_offset, bit_offset), "", "[31:0]", "read-only")

    for idx in range(0, 2):
        bit_offset = idx * 32
        txt += generate_register_sysconsaif_syscfg_full(344 + (idx * 4), "u0_plda_pcie_pl_sideband_out_{}_{}".format(31 + bit_offset, bit_offset), "", "[31:0]", "read-only")

    txt += generate_register_sysconsaif_syscfg352()

    for idx in range(0, 2):
        bit_offset = idx * 32
        txt += generate_register_sysconsaif_syscfg_full(356 + (idx * 4), "u0_plda_pcie_test_in_{}_{}".format(31 + bit_offset, bit_offset), "", "[31:0]", "read-write")

    for idx in range(0, 16):
        bit_offset = idx * 32
        txt += generate_register_sysconsaif_syscfg_full(364 + (idx * 4), "u0_plda_pcie_test_out_bridge_{}_{}".format(31 + bit_offset, bit_offset), "", "[31:0]", "read-only")

    for idx in range(0, 16):
        bit_offset = idx * 32
        txt += generate_register_sysconsaif_syscfg_full(428 + (idx * 4), "u0_plda_pcie_test_out_pcie_{}_{}".format(31 + bit_offset, bit_offset), "", "[31:0]", "read-only")

    txt += generate_register_sysconsaif_syscfg492()
    txt += generate_register_sysconsaif_syscfg500()

    for idx in range(0, 8):
        bit_offset = idx * 32
        txt += generate_register_sysconsaif_syscfg_full(504 + (idx * 4), "u0_plda_pcie_axi4_mst0_aratomop_{}_{}".format(31 + bit_offset, bit_offset), "", "[31:0]", "read-only")

    txt += generate_register_sysconsaif_syscfg536()

    txt += generate_register_sysconsaif_syscfg_full(540, "u1_plda_pcie_axi4_mst0_aruser_31_0", "", "[31:0]", "read-only")
    txt += generate_register_sysconsaif_syscfg_full(544, "u1_plda_pcie_axi4_mst0_aruser_52_32", "", "[20:0]", "read-only")

    txt += generate_register_sysconsaif_syscfg548()
    txt += generate_register_sysconsaif_syscfg_full(552, "u1_plda_pcie_axi4_mst0_awuser_31_0", "", "[31:0]", "read-only")
    txt += generate_register_sysconsaif_syscfg556()
    txt += generate_register_sysconsaif_syscfg_full(560, "u1_plda_pcie_axi4_mst0_ruser", "", "[31:0]", "read-write")
    txt += generate_register_sysconsaif_syscfg_full(564, "u1_plda_pcie_axi4_mst0_wderr", "", "[7:0]", "read-only")

    for idx in range(0, 8):
        bit_offset = idx * 32
        txt += generate_register_sysconsaif_syscfg_full(568 + (idx * 4), "u1_plda_pcie_axi4_slv0_aratomop_{}_{}".format(31 + bit_offset, bit_offset), "", "[31:0]", "read-write")

    txt += generate_register_sysconsaif_syscfg600()

    txt += generate_register_sysconsaif_syscfg_full(604, "u1_plda_pcie_axi4_slv0_aruser_31_0", "", "[31:0]", "read-write")

    txt += generate_register_sysconsaif_syscfg608()

    txt += generate_register_sysconsaif_syscfg_full(612, "u1_plda_pcie_axi4_slv0_awuser_31_0", "", "[31:0]", "read-write")

    txt += generate_register_sysconsaif_syscfg616()

    txt += generate_register_sysconsaif_syscfg_full(620, "u1_plda_pcie_axi4_slv0_ruser", "", "[31:0]", "read-only")

    txt += generate_register_sysconsaif_syscfg624()
    txt += generate_register_sysconsaif_syscfg628()

    for idx in range(0, 26):
        bit_offset = idx * 32
        txt += generate_register_sysconsaif_syscfg_full(632 + (idx * 4), "u1_plda_pcie_k_phyparam_{}_{}".format(31 + bit_offset, bit_offset), "", "[31:0]", "read-write")

    txt += generate_register_sysconsaif_syscfg736()

    txt += generate_register_sysconsaif_syscfg_full(740, "u1_plda_pcie_local_interrupt_in", "", "[31:0]", "read-write")

    txt += generate_register_sysconsaif_syscfg744()

    for idx in range(0, 3):
        txt += generate_register_sysconsaif_syscfg_full(748 + (idx * 4), "u1_plda_pcie_pf{}_offset".format(idx), "", "[19:0]", "read-write")

    txt += generate_register_sysconsaif_syscfg760()

    txt += generate_register_sysconsaif_syscfg_full(764, "u1_plda_pcie_pl_pclk_rate", "", "[4:0]", "read-only")

    for idx in range(0, 2):
        bit_offset = idx * 32
        txt += generate_register_sysconsaif_syscfg_full(768 + (idx * 4), "u1_plda_pcie_pl_sideband_in_{}_{}".format(31 + bit_offset, bit_offset), "", "[31:0]", "read-write")

    for idx in range(0, 2):
        bit_offset = idx * 32
        txt += generate_register_sysconsaif_syscfg_full(776 + (idx * 4), "u1_plda_pcie_pl_sideband_out_{}_{}".format(31 + bit_offset, bit_offset), "", "[31:0]", "read-write")

    txt += generate_register_sysconsaif_syscfg784()

    for idx in range(0, 2):
        bit_offset = idx * 32
        txt += generate_register_sysconsaif_syscfg_full(788 + (idx * 4), "u1_plda_pcie_test_in_{}_{}".format(31 + bit_offset, bit_offset), "", "[31:0]", "read-write")

    for idx in range(0, 16):
        bit_offset = idx * 32
        txt += generate_register_sysconsaif_syscfg_full(796 + (idx * 4), "u1_plda_pcie_test_out_bridge_{}_{}".format(31 + bit_offset, bit_offset), "", "[31:0]", "read-write")

    for idx in range(0, 16):
        bit_offset = idx * 32
        txt += generate_register_sysconsaif_syscfg_full(860 + (idx * 4), "u1_plda_pcie_test_out_pcie_{}_{}".format(31 + bit_offset, bit_offset), "", "[31:0]", "read-only")

    txt += generate_register_sysconsaif_syscfg924()
    txt += generate_register_sysconsaif_syscfg928()
    txt += generate_register_sysconsaif_syscfg932()

    return txt + """\
              </registers>
"""

def generate_register_sysconsaif_syscfg0():
    txt = """\
                <register>
                  <name>stg_sysconsaif_syscfg0</name>
                  <description>STG SYSCONSAIF SYSCFG 0</description>
                  <addressOffset>0x0</addressOffset>
                  <size>32</size>
                  <fields>
"""

    for idx in range(0, 2):
        bit_range = "[{}:{}]".format(3 + (idx * 4), idx * 4)
        txt += generate_field("scfg_hprot_sd{}".format(idx), "", bit_range, "read-write")

    txt += generate_field("u0_cdn_usb_adp_en", "", "[8:8]", "read-only")
    txt += generate_field("u0_cdn_usb_adp_probe_ana", "", "[9:9]", "read-write")
    txt += generate_field("u0_cdn_usb_adp_probe_en", "", "[10:10]", "read-only")
    txt += generate_field("u0_cdn_usb_adp_sense_ana", "", "[11:11]", "read-write")
    txt += generate_field("u0_cdn_usb_adp_sense_en", "", "[12:12]", "read-only")
    txt += generate_field("u0_cdn_usb_adp_sink_current_en", "", "[13:13]", "read-only")
    txt += generate_field("u0_cdn_usb_adp_source_current_en", "", "[14:14]", "read-only")
    txt += generate_field("u0_cdn_usb_bc_en", "", "[15:15]", "read-only")
    txt += generate_field("u0_cdn_usb_chrg_vbus", "", "[16:16]", "read-write")
    txt += generate_field("u0_cdn_usb_dcd_comp_sts", "", "[17:17]", "read-write")
    txt += generate_field("u0_cdn_usb_dischrg_vbus", "", "[18:18]", "read-write")
    txt += generate_field("u0_cdn_usb_dm_vdat_ref_comp_en", "", "[19:19]", "read-only")
    txt += generate_field("u0_cdn_usb_dm_vdat_ref_comp_sts", "", "[20:20]", "read-write")
    txt += generate_field("u0_cdn_usb_dm_vlgc_comp_en", "", "[21:21]", "read-only")
    txt += generate_field("u0_cdn_usb_dm_vlgc_comp_sts", "", "[22:22]", "read-write")
    txt += generate_field("u0_cdn_usb_dp_vdat_ref_comp_en", "", "[23:23]", "read-only")
    txt += generate_field("u0_cdn_usb_dp_vdat_ref_comp_sts", "", "[24:24]", "read-write")
    txt += generate_field("u0_cdn_usb_host_system_err", "", "[25:25]", "read-write")
    txt += generate_field("u0_cdn_usb_hsystem_err_ext", "", "[26:26]", "read-only")
    txt += generate_field("u0_cdn_usb_idm_sink_en", "", "[27:27]", "read-only")
    txt += generate_field("u0_cdn_usb_idp_sink_en", "", "[28:28]", "read-only")
    txt += generate_field("u0_cdn_usb_idp_src_en", "", "[29:29]", "read-only")

    return txt + """\
                  </fields>
                </register>
"""

def generate_register_sysconsaif_syscfg4():
    txt = """\
                <register>
                  <name>stg_sysconsaif_syscfg4</name>
                  <description>STG SYSCONSAIF SYSCFG 4</description>
                  <addressOffset>0x4</addressOffset>
                  <size>32</size>
                  <fields>
"""

    txt += generate_field("u0_cdn_usb_lowest_belt", "LTM interface to software", "[11:0]", "read-only")
    txt += generate_field("u0_cdn_usb_ltm_host_req", "LTM interface to software", "[12:12]", "read-only")
    txt += generate_field("u0_cdn_usb_ltm_host_req_halt", "LTM interface to software", "[13:13]", "read-write")
    txt += generate_field("u0_cdn_usb_mdctrl_clk_sel", "", "[14:14]", "read-write")
    txt += generate_field("u0_cdn_usb_mdctrl_clk_status", "", "[15:15]", "read-only")
    txt += generate_field("u0_cdn_usb_mode_strap", "Can onlly be changed when pwrup_rst_n is low", "[18:16]", "read-write")
    txt += generate_field("u0_cdn_usb_otg_suspendm", "", "[19:19]", "read-write")
    txt += generate_field("u0_cdn_usb_otg_suspendm_byps", "", "[20:20]", "read-write")
    txt += generate_field("u0_cdn_usb_phy_bvalid", "", "[21:21]", "read-only")
    txt += generate_field("u0_cdn_usb_pll_en", "", "[22:22]", "read-write")
    txt += generate_field("u0_cdn_usb_refclk_mode", "", "[23:23]", "read-write")

    for idx in range(0, 3):
        ltr = chr(ord('a') + idx)
        bit = 24 + idx
        bit_range = "[{}:{}]".format(bit, bit)

        txt += generate_field("u0_cdn_usb_rid_{}_comp_sts".format(ltr), "", bit_range, "read-write")

    txt += generate_field("u0_cdn_usb_rid_float_comp_en", "", "[27:27]", "read-only")
    txt += generate_field("u0_cdn_usb_rid_float_comp_sts", "", "[28:28]", "read-write")
    txt += generate_field("u0_cdn_usb_rid_gnd_comp_sts", "", "[29:29]", "read-write")
    txt += generate_field("u0_cdn_usb_rid_nonfloat_comp_en", "", "[30:30]", "read-only")
    txt += generate_field("u0_cdn_usb_rx_dm", "", "[31:31]", "read-only")

    return txt + """\
                  </fields>
                </register>
"""

def generate_register_sysconsaif_syscfg8():
    txt = """\
                <register>
                  <name>stg_sysconsaif_syscfg8</name>
                  <description>STG SYSCONSAIF SYSCFG 8</description>
                  <addressOffset>0x8</addressOffset>
                  <size>32</size>
                  <fields>
"""

    txt += generate_field("u0_cdn_usb_rx_dp", "", "[0:0]", "read-only")
    txt += generate_field("u0_cdn_usb_rx_rcv", "", "[1:1]", "read-only")
    txt += generate_field("u0_cdn_usb_self_test", "For software bist_test", "[2:2]", "read-write")
    txt += generate_field("u0_cdn_usb_sessend", "", "[3:3]", "read-only")
    txt += generate_field("u0_cdn_usb_sessvalid", "", "[4:4]", "read-only")
    txt += generate_field("u0_cdn_usb_sof", "", "[5:5]", "read-only")
    txt += generate_field("u0_cdn_usb_test_bist", "For software bist_test", "[6:6]", "read-only")
    txt += generate_field("u0_cdn_usb_usbdev_main_power_off_ack", "", "[7:7]", "read-only")
    txt += generate_field("u0_cdn_usb_usbdev_main_power_off_ready", "", "[8:8]", "read-only")
    txt += generate_field("u0_cdn_usb_usbdev_main_power_off_req", "", "[9:9]", "read-write")
    txt += generate_field("u0_cdn_usb_usbdev_main_power_on_ready", "", "[10:10]", "read-only")
    txt += generate_field("u0_cdn_usb_usbdev_main_power_on_req", "", "[11:11]", "read-only")
    txt += generate_field("u0_cdn_usb_usbdev_main_power_on_valid", "", "[12:12]", "read-write")
    txt += generate_field("u0_cdn_usb_usbdev_power_off_ack", "", "[13:13]", "read-only")
    txt += generate_field("u0_cdn_usb_usbdev_power_off_ready", "", "[14:14]", "read-only")
    txt += generate_field("u0_cdn_usb_usbdev_power_off_req", "", "[15:15]", "read-write")
    txt += generate_field("u0_cdn_usb_usbdev_power_on_ready", "", "[16:16]", "read-only")
    txt += generate_field("u0_cdn_usb_usbdev_power_on_req", "", "[17:17]", "read-only")
    txt += generate_field("u0_cdn_usb_usbdev_power_on_valid", "", "[18:18]", "read-write")
    txt += generate_field("u0_cdn_usb_utmi_dmpulldown_sit", "", "[19:19]", "read-write")
    txt += generate_field("u0_cdn_usb_utmi_dppulldown_sit", "", "[20:20]", "read-write")
    txt += generate_field("u0_cdn_usb_utmi_fslsserialmode_sit", "", "[21:21]", "read-write")
    txt += generate_field("u0_cdn_usb_utmi_hostdisconnect_sit", "", "[22:22]", "read-only")
    txt += generate_field("u0_cdn_usb_utmi_iddig_sit", "", "[23:23]", "read-only")
    txt += generate_field("u0_cdn_usb_utmi_idpullup_sit", "", "[24:24]", "read-write")
    txt += generate_field("u0_cdn_usb_utmi_linestate_sit", "", "[26:25]", "read-only")
    txt += generate_field("u0_cdn_usb_utmi_opmode_sit", "", "[28:27]", "read-write")
    txt += generate_field("u0_cdn_usb_utmi_rxactive_sit", "", "[29:29]", "read-only")
    txt += generate_field("u0_cdn_usb_utmi_rxerror_sit", "", "[30:30]", "read-only")
    txt += generate_field("u0_cdn_usb_utmi_rxvalid_sit", "", "[31:31]", "read-only")

    return txt + """\
                  </fields>
                </register>
"""

def generate_register_sysconsaif_syscfg12():
    txt = """\
                <register>
                  <name>stg_sysconsaif_syscfg12</name>
                  <description>STG SYSCONSAIF SYSCFG 12</description>
                  <addressOffset>0xc</addressOffset>
                  <size>32</size>
                  <fields>
"""

    txt += generate_field("u0_cdn_usb_utmi_rxvalidh_sit", "", "[0:0]", "read-only")
    txt += generate_field("u0_cdn_usb_utmi_sessvld", "", "[1:1]", "read-write")
    txt += generate_field("u0_cdn_usb_utmi_termselect_sit", "", "[2:2]", "read-write")
    txt += generate_field("u0_cdn_usb_utmi_tx_dat_sit", "", "[3:3]", "read-write")
    txt += generate_field("u0_cdn_usb_utmi_tx_enable_n_sit", "", "[4:4]", "read-write")
    txt += generate_field("u0_cdn_usb_utmi_tx_se0_sit", "", "[5:5]", "read-write")
    txt += generate_field("u0_cdn_usb_utmi_txbitstuffenable_sit", "", "[6:6]", "read-write")
    txt += generate_field("u0_cdn_usb_utmi_txready_sit", "", "[7:7]", "read-only")
    txt += generate_field("u0_cdn_usb_utmi_txvalid_sit", "", "[8:8]", "read-write")
    txt += generate_field("u0_cdn_usb_utmi_txvalidh_sit", "", "[9:9]", "read-write")
    txt += generate_field("u0_cdn_usb_utmi_vbusvalid_sit", "", "[10:10]", "read-only")
    txt += generate_field("u0_cdn_usb_utmi_xcvrselect_sit", "", "[12:11]", "read-write")
    txt += generate_field("u0_cdn_usb_utmi_vdm_src_en", "", "[13:13]", "read-only")
    txt += generate_field("u0_cdn_usb_utmi_vdp_src_en", "", "[14:14]", "read-only")
    txt += generate_field("u0_cdn_usb_wakeup", "", "[15:15]", "read-write")
    txt += generate_field("u0_cdn_usb_xhc_d0_ack", "", "[16:16]", "read-only")
    txt += generate_field("u0_cdn_usb_xhc_d0_req", "", "[17:17]", "read-write")

    return txt + """\
                  </fields>
                </register>
"""

def generate_register_sysconsaif_syscfg24():
    txt = """\
                <register>
                  <name>stg_sysconsaif_syscfg24</name>
                  <description>STG SYSCONSAIF SYSCFG 24</description>
                  <addressOffset>0x18</addressOffset>
                  <size>32</size>
                  <fields>
"""

    txt += generate_field("u0_cdn_usb_xhci_debug_sel", "", "[4:0]", "read-write")
    txt += generate_field("u0_cdn_usb_xhci_main_power_off_ack", "", "[5:5]", "read-only")
    txt += generate_field("u0_cdn_usb_xhci_main_power_off_req", "", "[6:6]", "read-only")
    txt += generate_field("u0_cdn_usb_xhci_main_power_on_ready", "", "[7:7]", "read-write")
    txt += generate_field("u0_cdn_usb_xhci_main_power_on_req", "", "[8:8]", "read-only")
    txt += generate_field("u0_cdn_usb_xhci_main_power_on_valid", "", "[9:9]", "read-write")
    txt += generate_field("u0_cdn_usb_xhci_power_off_ack", "", "[10:10]", "read-only")
    txt += generate_field("u0_cdn_usb_xhci_power_off_ready", "", "[11:11]", "read-only")
    txt += generate_field("u0_cdn_usb_xhci_power_off_req", "", "[12:12]", "read-write")
    txt += generate_field("u0_cdn_usb_xhci_power_on_ready", "", "[13:13]", "read-only")
    txt += generate_field("u0_cdn_usb_xhci_power_on_req", "", "[14:14]", "read-only")
    txt += generate_field("u0_cdn_usb_xhci_power_on_valid", "", "[15:15]", "read-write")
    txt += generate_field("u0_e2_sft7110_cease_from_tile_0", "", "[16:16]", "read-only")
    txt += generate_field("u0_e2_sft7110_debug_from_tile_0", "", "[17:17]", "read-only")
    txt += generate_field("u0_e2_sft7110_halt_from_tile_0", "", "[18:18]", "read-only")

    return txt + """\
                  </fields>
                </register>
"""

def generate_register_sysconsaif_syscfg48():
    txt = """\
                <register>
                  <name>stg_sysconsaif_syscfg48</name>
                  <description>STG SYSCONSAIF SYSCFG 48</description>
                  <addressOffset>0x30</addressOffset>
                  <size>32</size>
                  <fields>
"""

    txt += generate_field("u0_hifi4_breakin", "Debug signal", "[0:0]", "read-write")
    txt += generate_field("u0_hifi4_breakinack", "Debug signal", "[1:1]", "read-only")
    txt += generate_field("u0_hifi4_breakout", "Debug signal", "[2:2]", "read-only")
    txt += generate_field("u0_hifi4_breakoutack", "Debug signal", "[3:3]", "read-write")
    txt += generate_field("u0_hifi4_debugmode", "Debug signal", "[4:4]", "read-only")
    txt += generate_field("u0_hifi4_doubleexceptionerror", "Fault Handling Signals", "[5:5]", "read-only")
    txt += generate_field("u0_hifi4_iram0loadstore", "Indicates that iram0 works", "[6:6]", "read-only")
    txt += generate_field("u0_hifi4_iram1loadstore", "Indicates that iram1 works", "[7:7]", "read-only")
    txt += generate_field("u0_hifi4_ocdhaltonreset", "Debug signal", "[8:8]", "read-write")
    txt += generate_field("u0_hifi4_pfatalerror", "Fault Handling Signals", "[9:9]", "read-only")

    return txt + """\
                  </fields>
                </register>
"""

def generate_register_sysconsaif_syscfg56():
    txt = """\
                <register>
                  <name>stg_sysconsaif_syscfg56</name>
                  <description>STG SYSCONSAIF SYSCFG 56</description>
                  <addressOffset>0x38</addressOffset>
                  <size>32</size>
                  <fields>
"""

    txt += generate_field("u0_hifi4_pfaultinfovalid", "Fault Handling Signals", "[0:0]", "read-only")
    txt += generate_field("u0_hifi4_prid", "Module ID", "[16:1]", "read-write")
    txt += generate_field("u0_hifi4_pwaitmode", "Wait Mode", "[17:17]", "read-only")
    txt += generate_field("u0_hifi4_runstall", "Run Stall", "[18:18]", "read-write")

    return txt + """\
                  </fields>
                </register>
"""

def generate_register_sysconsaif_syscfg60():
    txt = """\
                <register>
                  <name>stg_sysconsaif_syscfg60</name>
                  <description>STG SYSCONSAIF SYSCFG 60</description>
                  <addressOffset>0x3c</addressOffset>
                  <size>32</size>
                  <fields>
"""

    txt += generate_field("u0_hifi4_scfg_dsp_mst_offset_master", "Indicates that master port remap address", "[11:0]", "read-write")
    txt += generate_field("u0_hifi4_scfg_dsp_mst_offset_dma", "Indicates the DMA port remap address", "[27:16]", "read-write")

    return txt + """\
                  </fields>
                </register>
"""

def generate_register_sysconsaif_syscfg68():
    txt = """\
                <register>
                  <name>stg_sysconsaif_syscfg68</name>
                  <description>STG SYSCONSAIF SYSCFG 68</description>
                  <addressOffset>0x44</addressOffset>
                  <size>32</size>
                  <fields>
"""

    txt += generate_fields_sram_config("u0_hifi4_scfg_sram_config", 0)
    txt += generate_field("u0_hifi4_statvectorsel", "When the value is 1, it indicates that the AltResetVec is valid", "[12:12]", "read-write")
    txt += generate_field("u0_hifi4_trigin_idma", "DMA port trigger", "[13:13]", "read-write")
    txt += generate_field("u0_hifi4_trigout_idma", "DMA port trigger", "[14:14]", "read-only")
    txt += generate_field("u0_hifi4_xocdmode", "Debug signal", "[15:15]", "read-only")
    txt += generate_field("u0_plda_pcie_align_detect", "", "[16:16]", "read-only")

    return txt + """\
                  </fields>
                </register>
"""

def generate_register_sysconsaif_syscfg104():
    txt = """\
                <register>
                  <name>stg_sysconsaif_syscfg104</name>
                  <description>STG SYSCONSAIF SYSCFG 104</description>
                  <addressOffset>0x68</addressOffset>
                  <size>32</size>
                  <fields>
"""

    txt += generate_field("u0_plda_pcie_axi4_mst0_aratomop_257_256", "", "[1:0]", "read-only")
    txt += generate_field("u0_plda_pcie_axi4_mst0_arfunc", "", "[16:2]", "read-only")
    txt += generate_field("u0_plda_pcie_axi4_mst0_arregion", "", "[20:17]", "read-only")

    return txt + """\
                  </fields>
                </register>
"""

def generate_register_sysconsaif_syscfg116():
    txt = """\
                <register>
                  <name>stg_sysconsaif_syscfg116</name>
                  <description>STG SYSCONSAIF SYSCFG 116</description>
                  <addressOffset>0x74</addressOffset>
                  <size>32</size>
                  <fields>
"""

    txt += generate_field("u0_plda_pcie_axi4_mst0_awfunc", "", "[14:0]", "read-only")
    txt += generate_field("u0_plda_pcie_axi4_mst0_awregion", "", "[18:15]", "read-only")

    return txt + """\
                  </fields>
                </register>
"""

def generate_register_sysconsaif_syscfg124():
    txt = """\
                <register>
                  <name>stg_sysconsaif_syscfg124</name>
                  <description>STG SYSCONSAIF SYSCFG 124</description>
                  <addressOffset>0x7c</addressOffset>
                  <size>32</size>
                  <fields>
"""

    txt += generate_field("u0_plda_pcie_axi4_mst0_awuser_42_32", "", "[10:0]", "read-only")
    txt += generate_field("u0_plda_pcie_axi4_mst0_rderr", "", "[18:11]", "read-write")

    return txt + """\
                  </fields>
                </register>
"""

def generate_register_sysconsaif_syscfg168():
    txt = """\
                <register>
                  <name>stg_sysconsaif_syscfg168</name>
                  <description>STG SYSCONSAIF SYSCFG 168</description>
                  <addressOffset>0xa8</addressOffset>
                  <size>32</size>
                  <fields>
"""

    txt += generate_field("u0_plda_pcie_axi4_slv0_aratomop_257_256", "", "[1:0]", "read-write")
    txt += generate_field("u0_plda_pcie_axi4_slv0_arfunc", "", "[16:2]", "read-write")
    txt += generate_field("u0_plda_pcie_axi4_slv0_arregion", "", "[20:17]", "read-write")

    return txt + """\
                  </fields>
                </register>
"""

def generate_register_sysconsaif_syscfg176():
    txt = """\
                <register>
                  <name>stg_sysconsaif_syscfg176</name>
                  <description>STG SYSCONSAIF SYSCFG 176</description>
                  <addressOffset>0xb0</addressOffset>
                  <size>32</size>
                  <fields>
"""

    txt += generate_field("u0_plda_pcie_axi4_slv0_aruser_40_32", "", "[8:0]", "read-write")
    txt += generate_field("u0_plda_pcie_axi4_slv0_awfunc", "", "[23:9]", "read-write")
    txt += generate_field("u0_plda_pcie_axi4_slv0_awregion", "", "[27:24]", "read-write")

    return txt + """\
                  </fields>
                </register>
"""

def generate_register_sysconsaif_syscfg184():
    txt = """\
                <register>
                  <name>stg_sysconsaif_syscfg184</name>
                  <description>STG SYSCONSAIF SYSCFG 184</description>
                  <addressOffset>0xb8</addressOffset>
                  <size>32</size>
                  <fields>
"""

    txt += generate_field("u0_plda_pcie_axi4_slv0_awuser_40_32", "", "[8:0]", "read-write")
    txt += generate_field("u0_plda_pcie_axi4_slv0_rderr", "", "[16:9]", "read-only")

    return txt + """\
                  </fields>
                </register>
"""

def generate_register_sysconsaif_syscfg192():
    txt = """\
                <register>
                  <name>stg_sysconsaif_syscfg192</name>
                  <description>STG SYSCONSAIF SYSCFG 192</description>
                  <addressOffset>0xc0</addressOffset>
                  <size>32</size>
                  <fields>
"""

    txt += generate_field("u0_plda_pcie_axi4_slv0_wderr", "", "[7:0]", "read-write")
    txt += generate_field("u0_plda_pcie_axi4_slvl_arfunc", "", "[22:8]", "read-only")

    return txt + """\
                  </fields>
                </register>
"""

def generate_register_sysconsaif_syscfg196():
    txt = """\
                <register>
                  <name>stg_sysconsaif_syscfg196</name>
                  <description>STG SYSCONSAIF SYSCFG 196</description>
                  <addressOffset>0xc4</addressOffset>
                  <size>32</size>
                  <fields>
"""

    txt += generate_field("u0_plda_pcie_axi4_slvl_awfunc", "", "[14:0]", "read-write")
    txt += generate_field("u0_plda_pcie_bus_width_o", "", "[16:15]", "read-only")
    txt += generate_field("u0_plda_pcie_bypass_codec", "", "[17:17]", "read-write")
    txt += generate_field("u0_plda_pcie_ckref_src", "", "[19:18]", "read-write")
    txt += generate_field("u0_plda_pcie_clk_sel", "", "[21:20]", "read-write")
    txt += generate_field("u0_plda_pcie_clkreq", "", "[22:22]", "read-write")

    return txt + """\
                  </fields>
                </register>
"""

def generate_register_sysconsaif_syscfg304():
    txt = """\
                <register>
                  <name>stg_sysconsaif_syscfg304</name>
                  <description>STG SYSCONSAIF SYSCFG 304</description>
                  <addressOffset>0x130</addressOffset>
                  <size>32</size>
                  <fields>
"""

    txt += generate_field("u0_plda_pcie_k_phyparam_839_832", "", "[7:0]", "read-write")
    txt += generate_field("u0_plda_pcie_k_rp_nep", "", "[8:8]", "read-write")
    txt += generate_field("u0_plda_pcie_l1sub_entack", "", "[9:9]", "read-only")
    txt += generate_field("u0_plda_pcie_l1sub_entreq", "", "[10:10]", "read-write")

    return txt + """\
                  </fields>
                </register>
"""

def generate_register_sysconsaif_syscfg312():
    txt = """\
                <register>
                  <name>stg_sysconsaif_syscfg312</name>
                  <description>STG SYSCONSAIF SYSCFG 312</description>
                  <addressOffset>0x138</addressOffset>
                  <size>32</size>
                  <fields>
"""

    txt += generate_field("u0_plda_pcie_mperstn", "", "[0:0]", "read-write")
    txt += generate_field("u0_plda_pcie_pcie_ebuf_mode", "", "[1:1]", "read-write")
    txt += generate_field("u0_plda_pcie_pcie_phy_test_cfg", "", "[24:2]", "read-write")
    txt += generate_field("u0_plda_pcie_pcie_rx_eq_training", "", "[25:25]", "read-write")
    txt += generate_field("u0_plda_pcie_pcie_rxterm_en", "", "[26:26]", "read-write")
    txt += generate_field("u0_plda_pcie_pcie_tx_onezeros", "", "[27:27]", "read-write")

    return txt + """\
                  </fields>
                </register>
"""

def generate_register_sysconsaif_syscfg328():
    txt = """\
                <register>
                  <name>stg_sysconsaif_syscfg328</name>
                  <description>STG SYSCONSAIF SYSCFG 328</description>
                  <addressOffset>0x148</addressOffset>
                  <size>32</size>
                  <fields>
"""

    txt += generate_field("u0_plda_pcie_pf3_offset", "", "[19:0]", "read-write")
    txt += generate_field("u0_plda_pcie_phy_mode", "", "[21:20]", "read-write")
    txt += generate_field("u0_plda_pcie_pl_clkrem_allow", "", "[22:22]", "read-write")
    txt += generate_field("u0_plda_pcie_pl_clkreq_oen", "", "[23:23]", "read-only")
    txt += generate_field("u0_plda_pcie_pl_equ_phase", "", "[25:24]", "read-only")
    txt += generate_field("u0_plda_pcie_pl_ltssm", "", "[30:26]", "read-only")

    return txt + """\
                  </fields>
                </register>
"""

def generate_register_sysconsaif_syscfg352():
    txt = """\
                <register>
                  <name>stg_sysconsaif_syscfg352</name>
                  <description>STG SYSCONSAIF SYSCFG 352</description>
                  <addressOffset>0x160</addressOffset>
                  <size>32</size>
                  <fields>
"""

    txt += generate_field("u0_plda_pcie_pl_wake_in", "", "[0:0]", "read-write")
    txt += generate_field("u0_plda_pcie_pl_wake_oen", "", "[1:1]", "read-only")
    txt += generate_field("u0_plda_pcie_rx_standby_0", "", "[2:2]", "read-only")

    return txt + """\
                  </fields>
                </register>
"""

def generate_register_sysconsaif_syscfg492():
    txt = """\
                <register>
                  <name>stg_sysconsaif_syscfg492</name>
                  <description>STG SYSCONSAIF SYSCFG 492</description>
                  <addressOffset>0x1ec</addressOffset>
                  <size>32</size>
                  <fields>
"""

    txt += generate_field("u0_plda_pcie_test_sel", "", "[3:0]", "read-write")
    txt += generate_field("u0_plda_pcie_tl_clock_freq", "", "[25:4]", "read-write")

    return txt + """\
                  </fields>
                </register>
"""

def generate_register_sysconsaif_syscfg496():
    txt = """\
                <register>
                  <name>stg_sysconsaif_syscfg496</name>
                  <description>STG SYSCONSAIF SYSCFG 496</description>
                  <addressOffset>0x1f0</addressOffset>
                  <size>32</size>
                  <fields>
"""

    txt += generate_field("u0_plda_pcie_tl_ctrl_hotplug", "", "[15:0]", "read-only")
    txt += generate_field("u0_plda_pcie_tl_report_hotplug", "", "[31:16]", "read-write")

    return txt + """\
                  </fields>
                </register>
"""

def generate_register_sysconsaif_syscfg500():
    txt = """\
                <register>
                  <name>stg_sysconsaif_syscfg500</name>
                  <description>STG SYSCONSAIF SYSCFG 500</description>
                  <addressOffset>0x1f4</addressOffset>
                  <size>32</size>
                  <fields>
"""

    txt += generate_field("u0_plda_pcie_tx_pattern", "", "[1:0]", "read-write")
    txt += generate_field("u0_plda_pcie_usb3_bus_width", "", "[3:2]", "read-write")
    txt += generate_field("u0_plda_pcie_usb3_phy_enable", "", "[4:4]", "read-write")
    txt += generate_field("u0_plda_pcie_usb3_rate", "", "[6:5]", "read-write")
    txt += generate_field("u0_plda_pcie_usb3_rx_standby", "", "[7:7]", "read-write")
    txt += generate_field("u0_plda_pcie_xwdecerr", "", "[8:8]", "read-only")
    txt += generate_field("u0_plda_pcie_xwerrclr", "", "[9:9]", "read-write")
    txt += generate_field("u0_plda_pcie_xwslverr", "", "[10:10]", "read-only")

    txt += generate_fields_sram_config("u0_sec_top_sramcfg", 11)

    txt += generate_field("u0_plda_pcie_align_detect", "", "[23:23]", "read-only")

    return txt + """\
                  </fields>
                </register>
"""

def generate_register_sysconsaif_syscfg536():
    txt = """\
                <register>
                  <name>stg_sysconsaif_syscfg536</name>
                  <description>STG SYSCONSAIF SYSCFG 536</description>
                  <addressOffset>0x218</addressOffset>
                  <size>32</size>
                  <fields>
"""

    txt += generate_field("u0_plda_pcie_axi4_mst0_aratomop_257_256", "", "[1:0]", "read-only")
    txt += generate_field("u0_plda_pcie_axi4_mst0_arfunc", "", "[16:2]", "read-only")
    txt += generate_field("u0_plda_pcie_axi4_mst0_arregion", "", "[20:17]", "read-only")

    return txt + """\
                  </fields>
                </register>
"""

def generate_register_sysconsaif_syscfg548():
    txt = """\
                <register>
                  <name>stg_sysconsaif_syscfg548</name>
                  <description>STG SYSCONSAIF SYSCFG 548</description>
                  <addressOffset>0x224</addressOffset>
                  <size>32</size>
                  <fields>
"""

    txt += generate_field("u1_plda_pcie_axi4_mst0_awfunc", "", "[14:0]", "read-only")
    txt += generate_field("u1_plda_pcie_axi4_mst0_awregion", "", "[18:15]", "read-only")

    return txt + """\
                  </fields>
                </register>
"""

def generate_register_sysconsaif_syscfg556():
    txt = """\
                <register>
                  <name>stg_sysconsaif_syscfg556</name>
                  <description>STG SYSCONSAIF SYSCFG 556</description>
                  <addressOffset>0x22c</addressOffset>
                  <size>32</size>
                  <fields>
"""

    txt += generate_field("u1_plda_pcie_axi4_mst0_awuser_42_32", "", "[10:0]", "read-only")
    txt += generate_field("u1_plda_pcie_axi4_mst0_rderr", "", "[18:11]", "read-write")

    return txt + """\
                  </fields>
                </register>
"""

def generate_register_sysconsaif_syscfg600():
    txt = """\
                <register>
                  <name>stg_sysconsaif_syscfg600</name>
                  <description>STG SYSCONSAIF SYSCFG 600</description>
                  <addressOffset>0x258</addressOffset>
                  <size>32</size>
                  <fields>
"""

    txt += generate_field("u1_plda_pcie_axi4_mst0_aratomop_257_256", "", "[1:0]", "read-write")
    txt += generate_field("u1_plda_pcie_axi4_slv0_arfunc", "", "[16:2]", "read-write")
    txt += generate_field("u1_plda_pcie_axi4_slv0_arregion", "", "[20:17]", "read-write")

    return txt + """\
                  </fields>
                </register>
"""

def generate_register_sysconsaif_syscfg608():
    txt = """\
                <register>
                  <name>stg_sysconsaif_syscfg608</name>
                  <description>STG SYSCONSAIF SYSCFG 608</description>
                  <addressOffset>0x260</addressOffset>
                  <size>32</size>
                  <fields>
"""

    txt += generate_field("u1_plda_pcie_axi4_slv0_aruser_40_32", "", "[8:0]", "read-write")
    txt += generate_field("u1_plda_pcie_axi4_slv0_awfunc", "", "[23:9]", "read-write")
    txt += generate_field("u1_plda_pcie_axi4_slv0_awregion", "", "[27:24]", "read-write")

    return txt + """\
                  </fields>
                </register>
"""

def generate_register_sysconsaif_syscfg616():
    txt = """\
                <register>
                  <name>stg_sysconsaif_syscfg616</name>
                  <description>STG SYSCONSAIF SYSCFG 616</description>
                  <addressOffset>0x268</addressOffset>
                  <size>32</size>
                  <fields>
"""

    txt += generate_field("u1_plda_pcie_axi4_slv0_awuser_40_32", "", "[8:0]", "read-write")
    txt += generate_field("u1_plda_pcie_axi4_slv0_rderr", "", "[16:9]", "read-only")

    return txt + """\
                  </fields>
                </register>
"""

def generate_register_sysconsaif_syscfg624():
    txt = """\
                <register>
                  <name>stg_sysconsaif_syscfg624</name>
                  <description>STG SYSCONSAIF SYSCFG 624</description>
                  <addressOffset>0x270</addressOffset>
                  <size>32</size>
                  <fields>
"""

    txt += generate_field("u1_plda_pcie_axi4_slv0_wderr", "", "[7:0]", "read-write")
    txt += generate_field("u1_plda_pcie_axi4_slvl_arfunc", "", "[22:8]", "read-write")

    return txt + """\
                  </fields>
                </register>
"""

def generate_register_sysconsaif_syscfg628():
    txt = """\
                <register>
                  <name>stg_sysconsaif_syscfg628</name>
                  <description>STG SYSCONSAIF SYSCFG 628</description>
                  <addressOffset>0x274</addressOffset>
                  <size>32</size>
                  <fields>
"""

    txt += generate_field("u1_plda_pcie_axi4_slvl_awfunc", "", "[14:0]", "read-write")
    txt += generate_field("u1_plda_pcie_bus_width_o", "", "[16:15]", "read-only")
    txt += generate_field("u1_plda_pcie_bypass_codec", "", "[17:17]", "read-write")
    txt += generate_field("u1_plda_pcie_ckref_src", "", "[19:18]", "read-write")
    txt += generate_field("u1_plda_pcie_clk_sel", "", "[21:20]", "read-write")
    txt += generate_field("u1_plda_pcie_clkreq", "", "[22:22]", "read-write")

    return txt + """\
                  </fields>
                </register>
"""

def generate_register_sysconsaif_syscfg736():
    txt = """\
                <register>
                  <name>stg_sysconsaif_syscfg736</name>
                  <description>STG SYSCONSAIF SYSCFG 736</description>
                  <addressOffset>0x2e0</addressOffset>
                  <size>32</size>
                  <fields>
"""

    txt += generate_field("u1_plda_pcie_k_phyparam_839_832", "", "[7:0]", "read-write")
    txt += generate_field("u1_plda_pcie_k_rp_nep", "", "[8:8]", "read-write")
    txt += generate_field("u1_plda_pcie_l1sub_entack", "", "[9:9]", "read-only")
    txt += generate_field("u1_plda_pcie_l1sub_entreq", "", "[10:10]", "read-write")

    return txt + """\
                  </fields>
                </register>
"""

def generate_register_sysconsaif_syscfg744():
    txt = """\
                <register>
                  <name>stg_sysconsaif_syscfg744</name>
                  <description>STG SYSCONSAIF SYSCFG 744</description>
                  <addressOffset>0x2e8</addressOffset>
                  <size>32</size>
                  <fields>
"""

    txt += generate_field("u1_plda_pcie_mperstn", "", "[0:0]", "read-write")
    txt += generate_field("u1_plda_pcie_pcie_ebuf_mode", "", "[1:1]", "read-write")
    txt += generate_field("u1_plda_pcie_pcie_phy_test_cfg", "", "[24:2]", "read-write")
    txt += generate_field("u1_plda_pcie_pcie_rx_eq_training", "", "[25:25]", "read-write")
    txt += generate_field("u1_plda_pcie_pcie_rxterm_en", "", "[26:26]", "read-write")
    txt += generate_field("u1_plda_pcie_pcie_tx_oneszeros", "", "[27:27]", "read-write")

    return txt + """\
                  </fields>
                </register>
"""

def generate_register_sysconsaif_syscfg760():
    txt = """\
                <register>
                  <name>stg_sysconsaif_syscfg760</name>
                  <description>STG SYSCONSAIF SYSCFG 760</description>
                  <addressOffset>0x2f8</addressOffset>
                  <size>32</size>
                  <fields>
"""

    txt += generate_field("u1_plda_pcie_pf3_offset", "", "[19:0]", "read-write")
    txt += generate_field("u1_plda_pcie_phy_mode", "", "[21:20]", "read-write")
    txt += generate_field("u1_plda_pcie_pl_clkrem_allow", "", "[22:22]", "read-write")
    txt += generate_field("u1_plda_pcie_pl_clkreq_oen", "", "[23:23]", "read-only")
    txt += generate_field("u1_plda_pcie_pl_equ_phase", "", "[25:24]", "read-only")
    txt += generate_field("u1_plda_pcie_pl_ltssm", "", "[30:26]", "read-only")

    return txt + """\
                  </fields>
                </register>
"""

def generate_register_sysconsaif_syscfg784():
    txt = """\
                <register>
                  <name>stg_sysconsaif_syscfg784</name>
                  <description>STG SYSCONSAIF SYSCFG 784</description>
                  <addressOffset>0x310</addressOffset>
                  <size>32</size>
                  <fields>
"""

    txt += generate_field("u1_plda_pcie_pl_wake_in", "", "[0:0]", "read-write")
    txt += generate_field("u1_plda_pcie_pl_wake_oen", "", "[1:1]", "read-only")
    txt += generate_field("u1_plda_pcie_rx_standby_o", "", "[2:2]", "read-only")

    return txt + """\
                  </fields>
                </register>
"""

def generate_register_sysconsaif_syscfg924():
    txt = """\
                <register>
                  <name>stg_sysconsaif_syscfg924</name>
                  <description>STG SYSCONSAIF SYSCFG 924</description>
                  <addressOffset>0x39c</addressOffset>
                  <size>32</size>
                  <fields>
"""

    txt += generate_field("u1_plda_pcie_test_sel", "", "[3:0]", "read-write")
    txt += generate_field("u1_plda_pcie_tl_clock_freq", "", "[25:4]", "read-write")

    return txt + """\
                  </fields>
                </register>
"""

def generate_register_sysconsaif_syscfg928():
    txt = """\
                <register>
                  <name>stg_sysconsaif_syscfg928</name>
                  <description>STG SYSCONSAIF SYSCFG 928</description>
                  <addressOffset>0x3a0</addressOffset>
                  <size>32</size>
                  <fields>
"""

    txt += generate_field("u1_plda_pcie_tl_ctrl_hotplug", "", "[15:0]", "read-only")
    txt += generate_field("u1_plda_pcie_tl_report_hotplug", "", "[31:16]", "read-write")

    return txt + """\
                  </fields>
                </register>
"""

def generate_register_sysconsaif_syscfg932():
    txt = """\
                <register>
                  <name>stg_sysconsaif_syscfg932</name>
                  <description>STG SYSCONSAIF SYSCFG 932</description>
                  <addressOffset>0x3a4</addressOffset>
                  <size>32</size>
                  <fields>
"""

    txt += generate_field("u1_plda_pcie_tx_pattern", "", "[1:0]", "read-write")
    txt += generate_field("u1_plda_pcie_usb3_bus_width", "", "[3:2]", "read-write")
    txt += generate_field("u1_plda_pcie_usb3_phy_enable", "", "[4:4]", "read-write")
    txt += generate_field("u1_plda_pcie_usb3_rate", "", "[6:5]", "read-write")
    txt += generate_field("u1_plda_pcie_usb3_rx_standby", "", "[7:7]", "read-write")
    txt += generate_field("u1_plda_pcie_xwdecerr", "", "[8:8]", "read-only")
    txt += generate_field("u1_plda_pcie_xwerrclr", "", "[9:9]", "read-write")
    txt += generate_field("u1_plda_pcie_xwslverr", "", "[10:10]", "read-only")

    return txt + """\
                  </fields>
                </register>
"""

def generate_register_sysconsaif_syscfg_full(idx, field_name, field_desc, bit_range, access):
    name = "stg_sysconsaif_syscfg{}".format(idx)
    desc = "STG SYSCONSAIF SYSCFG {}".format(idx)
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
