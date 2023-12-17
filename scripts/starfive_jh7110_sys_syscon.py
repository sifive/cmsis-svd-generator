#!/usr/bin/env python3
# Copyleft (c) 2023 cmsis-svd-generator developers 
# SPDX-License-Identifier: Apache-2.0

from scripts.starfive_common import *

"""
This program generates CMSIS SVD xml for starfive JH7110 sys_syscon 
"""

def generate_registers_starfive_jh7110_sys_syscon(dts, peripheral):
    """Generate xml string for registers for starfive_sys_syscon peripheral"""
    txt = """\
              <registers>
"""

    txt += generate_register_sysconsaif_syscfg0()
    txt += generate_register_sysconsaif_syscfg4()
    txt += generate_register_sysconsaif_syscfg8()
    txt += generate_register_sysconsaif_syscfg12()
    txt += generate_register_sysconsaif_syscfg16()
    txt += generate_register_sysconsaif_syscfg20()
    txt += generate_register_sysconsaif_syscfg24()
    txt += generate_register_sysconsaif_syscfg28()
    txt += generate_register_sysconsaif_syscfg32()
    txt += generate_register_sysconsaif_syscfg36()
    txt += generate_register_sysconsaif_syscfg40()
    txt += generate_register_sysconsaif_syscfg44()
    txt += generate_register_sysconsaif_syscfg48()
    txt += generate_register_sysconsaif_syscfg52()
    txt += generate_register_sysconsaif_syscfg56()

    for idx in range(9):
        txt += generate_register_noc_bus_oic_qch_clock_stop(15 + idx, 0x3c + (idx * 4), idx)

    txt += generate_register_sysconsaif_syscfg96()
    txt += generate_register_sysconsaif_syscfg100()

    for idx in range(3):
        txt += generate_register_sysconsaif_reset_vector(26 + (2 * idx), 0x68 + (idx * 8), idx + 1, 0, 31, 0)
        txt += generate_register_sysconsaif_reset_vector(27 + (2 * idx), 0x6c + (idx * 8), idx + 1, 32, 35, 0)

    txt += generate_register_sysconsaif_reset_vector(32, 0x80, 4, 0, 31, 0)
    txt += generate_register_sysconsaif_syscfg132()
    txt += generate_register_sysconsaif_syscfg136()
    txt += generate_register_sysconsaif_syscfg140()
    txt += generate_register_sysconsaif_syscfg144()
    txt += generate_register_sysconsaif_syscfg148()
    txt += generate_register_sysconsaif_syscfg152()
    txt += generate_register_sysconsaif_syscfg156()

    return txt + """\
              </registers>
"""

def generate_register_sysconsaif_syscfg0():
    return generate_register("sys_syscfg_0", "SYS SYSCONSAIF SYSCFG 0", 0x0, [
        ("e24_remap_haddr", "", "[3:0]", "read-write"),
        ("hifi4_idma_remap_araddr", "", "[7:4]", "read-write"),
        ("hifi4_idma_remap_awaddr", "", "[11:8]", "read-write"),
        ("hifi4_sys_remap_araddr", "", "[15:12]", "read-write"),
        ("hifi4_sys_remap_awaddr", "", "[19:16]", "read-write"),
        ("jpg_remap_araddr", "", "[23:20]", "read-write"),
        ("jpg_remap_awaddr", "", "[27:24]", "read-write"),
        ("sd0_remap_araddr", "", "[31:28]", "read-write")
    ])

def generate_register_sysconsaif_syscfg4():
    return generate_register("sys_syscfg_1", "SYS SYSCONSAIF SYSCFG 4", 0x4, [
        ("sd1_remap_awaddr", "", "[3:0]", "read-write"),
        ("sec_haddr_remap", "", "[7:4]", "read-write"),
        ("usb_araddr_remap", "", "[11:8]", "read-write"),
        ("usb_awaddr_remap", "", "[15:12]", "read-write"),
        ("vdec_remap_awaddr", "", "[19:16]", "read-write"),
        ("venc_remap_araddr", "", "[23:20]", "read-write"),
        ("venc_remap_awaddr", "", "[27:24]", "read-write"),
        ("vout0_remap_araddr", "", "[31:28]", "read-write")
    ])

def generate_register_sysconsaif_syscfg8():
    return generate_register("sys_syscfg_2", "SYS SYSCONSAIF SYSCFG 8", 0x8, [
        ("vout0_remap_awaddr", "", "[3:0]", "read-write"),
        ("vout1_remap_araddr", "", "[7:4]", "read-write"),
        ("vout1_remap_awaddr", "", "[11:8]", "read-write")
    ])

def generate_register_sysconsaif_syscfg12():
    return generate_register("sys_syscfg_3", "SYS SYSCONSAIF SYSCFG 12: Set the GPIO voltage of all the 4 GPIO groups in this register", 0xc, [
        ("vout0_remap_awaddr_gpio0", "0: GPIO Group 0 (GPIO21-35) voltage select 3.3V, 1: GPIO Group 0 (GPIO21-35) voltage select 1.8V", "[0:0]", "read-write"),
        ("vout0_remap_awaddr_gpio1", "0: GPIO Group 1 (GPIO36-63) voltage select 3.3V, 1: GPIO Group 1 (GPIO36-63) voltage select 1.8V", "[1:1]", "read-write"),
        ("vout0_remap_awaddr_gpio2", "0: GPIO Group 2 (GPIO0-6) voltage select 3.3V, 1: GPIO Group 2 (GPIO0-6) voltage select 1.8V", "[2:2]", "read-write"),
        ("vout0_remap_awaddr_gpio3", "0: GPIO Group 3 (GPIO7-20) voltage select 3.3V, 1: GPIO Group 3 (GPIO7-20) voltage select 1.8V", "[3:3]", "read-write")
    ])

def generate_register_sysconsaif_syscfg16():
    return generate_register("sys_syscfg_4", "SYS SYSCONSAIF SYSCFG 16", 0x10, [
        ("coda12_cur_inst", "Tie 0 in JPU internal, do not care", "[1:0]", "read-only"),
        ("wave511_vpu_idle", "VPU monitoring signal", "[2:2]", "read-only"),
        ("can_ctrl_fd_enable_0", "", "[3:3]", "read-write"),
        ("can_ctrl_host_ecc_disable_0", "", "[4:4]", "read-write"),
        ("can_ctrl_host_if_0", "", "[23:5]", "read-only"),
        ("qspi_sclk_dlychain_sel", "des_qspi_sclk_dla: clock delay", "[28:24]", "read-only")
    ])

def generate_register_sysconsaif_syscfg20():
    fields = generate_fields_list_sram_config("u0_cdns_qspi_scfg_sram_config", 0)
    fields.extend(generate_fields_list_sram_config("u0_cdns_spdif_scfg_sram_config", 12))
    fields.extend([
        ("spdif_trmodeo", "1 for transmitter 0 for receiver", "[24:24]", "read-only"),
        ("i2c_ic_en", "I2C interface enable", "[25:25]", "read-only"),
        ("sdio_data_strobe_phase_ctrl", "Data strobe delay chain select", "[30:26]", "read-write"),
        ("sdio_hbig_endian", "AHB bus interface endianness: 1: Big-endian AHB bus interface, 0: Little-endian AHB bus interface", "[31:31]", "read-write")
    ])
    return generate_register("sys_syscfg_5", "SYS SYSCONSAIF SYSCFG 20", 0x14, fields)

def generate_register_sysconsaif_syscfg24():
    fields = [
        ("sdio_m_hbig_endian", "AHB master bus interface endianess: 1: Big-endian AHB bus interface, 0: Little-endian AHB bus interface", "[0:0]", "read-write"),
        ("i2srx_adc_en", "", "[1:1]", "read-write"),
        ("intmem_rom_sram_scfg_disable_rom", "", "[2:2]", "read-write")
    ]

    fields.extend(generate_fields_list_sram_config("u0_intmem_rom_sram_sram_config", 3))

    fields.extend([
        ("jtag_daisy_chain_en_0", "", "[15:15]", "read-write"),
        ("jtag_daisy_chain_en_1", "", "[16:16]", "read-write"),
        ("pdrstn_usbpipe_plugen", "", "[17:17]", "read-write"),
        ("pll0_cpi_bias", "", "[20:18]", "read-write"),
        ("pll0_cpp_bias", "", "[23:21]", "read-write"),
        ("pll0_dacpd", "", "[24:24]", "read-write"),
        ("pll0_dsmpd", "", "[25:25]", "read-write")
    ])

    return generate_register("sys_syscfg_6", "SYS SYSCONSAIF SYSCFG 24", 0x18, fields)

def generate_register_sysconsaif_syscfg28():
    return generate_register("sys_syscfg_7", "SYS SYSCONSAIF SYSCFG 28", 0x1c, [("pll0_fbdiv", "", "[11:0]", "read-write")])

def generate_register_sysconsaif_syscfg32():
    return generate_register("sys_syscfg_8", "SYS SYSCONSAIF SYSCFG 32", 0x20, [
        ("pll0_frac", "", "[23:0]", "read-write"),
        ("pll0_gvco_bias", "", "[25:24]", "read-write"),
        ("pll0_lock", "", "[26:26]", "read-only"),
        ("pll0_pd", "", "[27:27]", "read-write"),
        ("pll0_postdiv1", "", "[29:28]", "read-write"),
        ("pll0_postdiv2", "", "[31:30]", "read-write")
    ])

def generate_register_sysconsaif_syscfg36():
    return generate_register("sys_syscfg_9", "SYS SYSCONSAIF SYSCFG 36", 0x24, [
        ("pll0_prediv", "", "[5:0]", "read-write"),
        ("pll0_testen", "", "[6:6]", "read-write"),
        ("pll0_testsel", "", "[8:7]", "read-write"),
        ("pll1_cpi_bias", "", "[11:9]", "read-write"),
        ("pll1_cpp_bias", "", "[14:12]", "read-write"),
        ("pll1_dacpd", "", "[15:15]", "read-write"),
        ("pll1_dsmpd", "", "[16:16]", "read-write"),
        ("pll1_fbdiv", "", "[28:17]", "read-write")
    ])

def generate_register_sysconsaif_syscfg40():
    return generate_register("sys_syscfg_10", "SYS SYSCONSAIF SYSCFG 40", 0x28, [
        ("pll1_frac", "", "[23:0]", "read-write"),
        ("pll1_gvco_bias", "", "[25:24]", "read-write"),
        ("pll1_lock", "", "[26:26]", "read-only"),
        ("pll1_pd", "", "[27:27]", "read-write"),
        ("pll1_postdiv1", "", "[29:28]", "read-write"),
        ("pll1_postdiv2", "", "[31:30]", "read-write")
    ])

def generate_register_sysconsaif_syscfg44():
    return generate_register("sys_syscfg_11", "SYS SYSCONSAIF SYSCFG 44", 0x2c, [
        ("pll1_prediv", "", "[5:0]", "read-write"),
        ("pll1_testen", "", "[6:6]", "read-write"),
        ("pll1_testsel", "", "[8:7]", "read-write"),
        ("pll2_cpi_bias", "", "[11:9]", "read-write"),
        ("pll2_cpp_bias", "", "[14:12]", "read-write"),
        ("pll2_dacpd", "", "[15:15]", "read-write"),
        ("pll2_dsmpd", "", "[16:16]", "read-write"),
        ("pll2_fbdiv", "", "[28:17]", "read-write")
    ])

def generate_register_sysconsaif_syscfg48():
    return generate_register("sys_syscfg_12", "SYS SYSCONSAIF SYSCFG 48", 0x30, [
        ("pll2_frac", "", "[23:0]", "read-write"),
        ("pll2_gvco_bias", "", "[25:24]", "read-write"),
        ("pll2_lock", "", "[26:26]", "read-only"),
        ("pll2_pd", "", "[27:27]", "read-write"),
        ("pll2_postdiv1", "", "[29:28]", "read-write"),
        ("pll2_postdiv2", "", "[31:30]", "read-write")
    ])

def generate_register_sysconsaif_syscfg52():
    fields = [
        ("pll2_prediv", "", "[5:0]", "read-write"),
        ("pll2_testen", "", "[6:6]", "read-write"),
        ("pll2_testsel", "", "[8:7]", "read-write"),
        ("pll_test_mode", "PLL test mode, only used for PLL BIST through jtag2apb", "[9:9]", "read-write"),
        ("audio_i2sdin_sel", "", "[17:10]", "read-write"),
        ("noc_bus_clock_gating_off", "", "[18:18]", "read-write")
    ]

    for idx in range(0, 6):
        fields.extend(generate_fields_noc_bus_oic_evemon(idx, 19 + (idx * 2)))

    fields.append(generate_field_noc_bus_oic_evemon("start", 6, 31, "read-write"))

    return generate_register("sys_syscfg_13", "SYS SYSCONSAIF SYSCFG 52", 0x34, fields)

def generate_register_sysconsaif_syscfg56():
    fields = [generate_field_noc_bus_oic_evemon("trigger", 6, 0, "read-only")]

    for idx in range(7, 9):
        fields.extend(generate_fields_noc_bus_oic_evemon(idx, 1 + (idx * 2)))

    for idx in range(0, 5):
        name = "noc_bus_oic_ignore_modifiable_{}".format(idx)

        bit = 5 + idx
        bit_range = "[{}:{}]".format(bit, bit)

        fields.append((name, "", bit_range, "read-write")) 

    return generate_register("sys_syscfg_14", "SYS SYSCONSAIF SYSCFG 56", 0x38, fields)

def generate_register_noc_bus_oic_qch_clock_stop(cfg, addr, idx):
    name = "sys_syscfg_{}".format(cfg)
    desc = "SYS SYSCONSAIF SYSCFG {}".format(cfg * 4) 

    return generate_register(name, desc, addr, [
        ("noc_bus_oic_qch_clock_stop_threshold_{}".format(idx), "", "[31:0]", "read-write")
    ])

def generate_register_sysconsaif_syscfg96():
    fields = [
        ("tdm16slot_clkpol", "", "[0:0]", "read-only"),
        ("tdm16slot_pcm_ms", "", "[1:1]", "read-only")
    ]

    for idx in range(3):
        bit = 2 + (idx * 10)

        bit_range = "[{}:{}]".format(bit + 4, bit)
        fields.append(("u0_trace_mtx_in0_{}".format(idx), "", bit_range, "read-write"))

        bit_range = "[{}:{}]".format(bit + 9, bit + 5)
        fields.append(("u0_trace_mtx_in1_{}".format(idx), "", bit_range, "read-write"))

    return generate_register("sys_syscfg_24", "SYS SYSCONSAIF SYSCFG 96", 0x60, fields)

def generate_register_sysconsaif_syscfg100():
    fields = []
    for idx in range(3, 5):
        bit = 0 + ((idx - 3) * 10)

        bit_range = "[{}:{}]".format(bit + 4, bit)
        fields.append(("u0_trace_mtx_scfg_c{}_in0_ctl".format(idx), "", bit_range, "read-write"))

        bit_range = "[{}:{}]".format(bit + 9, bit + 5)
        fields.append(("u0_trace_mtx_scfg_c{}_in1_ctl".format(idx), "", bit_range, "read-write"))

    for idx in range(0, 5):
        name = "u0_cease_from_tile_{}".format(idx)
        bit = 20 + idx

        fields.append((name, "", "[{}:{}]".format(bit, bit), "read-only")) 

    for idx in range(0, 5):
        name = "u0_halt_from_tile_{}".format(idx)
        bit = 25 + idx

        fields.append((name, "", "[{}:{}]".format(bit, bit), "read-only")) 

    return generate_register("sys_syscfg_25", "SYS SYSCONSAIF SYSCFG 100", 0x64, fields)

def generate_register_sysconsaif_reset_vector(num, addr, idx, start, end, start_bit):
    name = "sys_syscfg_{}".format(num)
    desc = "SYS SYSCONSAIF SYSCFG {}".format(num)
    fields = generate_fields_reset_vector(idx, start, end, start_bit)

    return generate_register(name, desc, addr, fields) 

def generate_register_sysconsaif_syscfg132():
    fields = generate_fields_reset_vector(4, 32, 35, 0)

    for idx in range(1, 5):
        bit = 3 + idx
        bit_range = "[{}:{}]".format(bit, bit)

        fields.append(("u0_suppress_fetch_{}".format(idx), "", bit_range, "read-write"))

    for idx in range(0, 5):
        bit = 8 + idx
        bit_range = "[{}:{}]".format(bit, bit)

        fields.append(("u0_wfi_from_tile_{}".format(idx), "", bit_range, "read-write"))

    fields.extend(generate_fields_list_sram_config("u0_vdec_intsram_sram_config", 13))

    return generate_register("sys_syscfg_33", "SYS SYSCONSAIF SYSCFG 132", 0x84, fields)

def generate_register_sysconsaif_syscfg136():
    fields = generate_fields_list_sram_config("u0_venc_intsram_sram_config", 0)
    fields.extend([
        ("wave420l_ipu_current_buffer", "This signal indicates which buffer is currently active so that the VPU can correctly use the ipu_end_of_row signal for row counter.", "[14:12]", "read-write"),
        ("wave420l_ipu_end_of_row", "This signal is flipped every time when the IPU completes writing a row.", "[15:15]", "read-write"),
        ("wave420l_ipu_new_frame", "This signal is flipped every time when the IPU completes writing a new frame.", "[16:16]", "read-write"),
        ("wave420l_vpu_idle", "VPU monitoring signal. This signal gives out an opposite value of VPU_BUSY register.", "[17:17]", "read-only"),
        ("can_ctrl_fd_enable_1", "", "[18:18]", "read-write"),
        ("can_ctrl_host_ecc_disable_1", "", "[19:19]", "read-write")
    ])

    return generate_register("sys_syscfg_34", "SYS SYSCONSAIF SYSCFG 136", 0x88, fields)

def generate_register_sysconsaif_syscfg140():
    fields = [("can_ctrl_host_if_1", "", "[18:0]", "read-only")]
    fields.extend(generate_fields_list_sram_config("u1_gmac5_axi64_scfg_ram_cfg", 19))

    return generate_register("sys_syscfg_35", "SYS SYSCONSAIF SYSCFG 140", 0x8c, fields)

def generate_register_sysconsaif_syscfg144():
    return generate_register("sys_syscfg_36", "SYS SYSCONSAIF SYSCFG 144", 0x90, [
        ("gmac5_axi64_mac_speed", "", "[1:0]", "read-only"),
        ("gmac5_axi64_phy_intf_sel", "Active PHY Selected | When you have multiple GMAC PHY interfaces in your configuration, this field indicates the sampled value of the PHY selector during reset de-assertion. | Values: 0x0:(GMII or MII), 0x01:RGMII, 0x2:SGMII, 0x3:TBI, 0x4:RMII, 0x5:RTBI, 0x6:SMII, 0x7:REVMII", "[4:2]", "read-write")
    ])

def generate_register_sysconsaif_syscfg148():
    return generate_register("sys_syscfg_37", "SYS SYSCONSAIF SYSCFG 148", 0x94, [
        ("gmac5_axi64_ptp_timestamp_0_31", "", "[31:0]", "read-only")
    ])

def generate_register_sysconsaif_syscfg152():
    return generate_register("sys_syscfg_38", "SYS SYSCONSAIF SYSCFG 152", 0x98, [
        ("gmac5_axi64_ptp_timestamp_32_63", "", "[31:0]", "read-only")
    ])

def generate_register_sysconsaif_syscfg156():
    fields = [
        ("i2c_ic_en_1", "I2C interface enable.", "[0:0]", "read-only"),
        ("sdio_data_strobe_phase_ctrl_1", "Data strobe delay chain select.", "[5:1]", "read-write"),
        ("sdio_hbig_endian_1", "AHB bus interface endianness: 1: Big-endian AHB bus interface, 0: Little-endian AHB bus interface", "[6:6]", "read-write"),
        ("sdio_m_hbig_endian_1", "AHB bus interface endianness: 1: Big-endian AHB bus interface, 0: Little-endian AHB bus interface", "[7:7]", "read-write"),
        ("reset_ctrl_clr_reset_status_1", "", "[8:8]", "read-write"),
        ("reset_ctrl_pll_timecnt_finish_1", "", "[9:9]", "read-only"),
        ("reset_ctrl_rstn_sw_1", "", "[10:10]", "read-write"),
        ("reset_ctrl_sys_reset_status_1", "", "[14:11]", "read-only")
    ]

    for idx in range(2, 7):
        bit = 13 + idx
        bit_range = "[{}:{}]".format(bit, bit)

        fields.append(("i2c_ic_en_{}".format(idx), "I2C interface enable.", bit_range, "read-only")) 

    return generate_register("sys_syscfg_39", "SYS SYSCONSAIF SYSCFG 156", 0x9c, fields)

def generate_fields_noc_bus_oic_evemon(idx, bit):
    return [
        generate_field_noc_bus_oic_evemon("start", idx, bit, "read-write"),
        generate_field_noc_bus_oic_evemon("trigger", idx, bit + 1, "read-only")
    ]

def generate_field_noc_bus_oic_evemon(field, idx, bit, access):
    name = "noc_bus_oic_evemon_{}_{}".format(field, idx)
    bitfield = "[{}:{}]".format(bit, bit)

    return (name, "", bitfield, access)

def generate_fields_reset_vector(idx, start, end, start_bit):
    vectors = [int(i) for i in range(start, end + 1)]

    return [
        (
            "reset_vector_{}_{}".format(idx, vectors[i]),
            "U0 U74MC Reset Vector {}: {}".format(idx, vectors[i]),
            "[{}:{}]".format(start_bit + i, start_bit + i),
            "read-write",
        )
        for i in range(len(vectors))
    ]
