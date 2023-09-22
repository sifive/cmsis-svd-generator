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

    for idx in range(0, 9):
        txt += generate_register_noc_bus_oic_qch_clock_stop(60 + (idx * 4), 0x3c + (idx * 4), idx)

    txt += generate_register_sysconsaif_syscfg96()
    txt += generate_register_sysconsaif_syscfg100()

    for idx in range(0, 3):
        txt += generate_register_sysconsaif_reset_vector(104 + (idx * 8), 0x68 + (idx * 8), idx + 1, 0, 31, "[31:0]")
        txt += generate_register_sysconsaif_reset_vector(108 + (idx * 8), 0x6c + (idx * 8), idx + 1, 32, 35, "[3:0]")

    txt += generate_register_sysconsaif_reset_vector(128, 0x80, 4, 0, 31, "[31:0]")
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
    txt = """\
                <register>
                  <name>sys_sysconsaif_syscfg0</name>
                  <description>SYS SYSCONSAIF SYSCFG 0</description>
                  <addressOffset>0x0</addressOffset>
                  <size>32</size>
                  <fields>
"""

    txt += generate_field("scfg_e24_remap_haddr", "", "[3:0]", "read-write")
    txt += generate_field("scfg_hifi4_idma_remap_araddr", "", "[7:4]", "read-write")
    txt += generate_field("scfg_hifi4_idma_remap_awaddr", "", "[11:8]", "read-write")
    txt += generate_field("scfg_hifi4_sys_remap_araddr", "", "[15:12]", "read-write")
    txt += generate_field("scfg_hifi4_sys_remap_awaddr", "", "[19:16]", "read-write")
    txt += generate_field("scfg_jpg_remap_araddr", "", "[23:20]", "read-write")
    txt += generate_field("scfg_jpg_remap_awaddr", "", "[27:24]", "read-write")
    txt += generate_field("scfg_sd0_remap_araddr", "", "[31:28]", "read-write")

    return txt + """\
                  </fields>
                </register>
"""

def generate_register_sysconsaif_syscfg4():
    txt = """\
                <register>
                  <name>sys_sysconsaif_syscfg4</name>
                  <description>SYS SYSCONSAIF SYSCFG 4</description>
                  <addressOffset>0x4</addressOffset>
                  <size>32</size>
                  <fields>
"""

    txt += generate_field("scfg_sd1_remap_awaddr", "", "[3:0]", "read-write")
    txt += generate_field("scfg_sec_haddr_remap", "", "[7:4]", "read-write")
    txt += generate_field("scfg_usb_araddr_remap", "", "[11:8]", "read-write")
    txt += generate_field("scfg_usb_awaddr_remap", "", "[15:12]", "read-write")
    txt += generate_field("scfg_vdec_remap_awaddr", "", "[19:16]", "read-write")
    txt += generate_field("scfg_venc_remap_araddr", "", "[23:20]", "read-write")
    txt += generate_field("scfg_venc_remap_awaddr", "", "[27:24]", "read-write")
    txt += generate_field("scfg_vout0_remap_araddr", "", "[31:28]", "read-write")

    return txt + """\
                  </fields>
                </register>
"""

def generate_register_sysconsaif_syscfg8():
    txt = """\
                <register>
                  <name>sys_sysconsaif_syscfg8</name>
                  <description>SYS SYSCONSAIF SYSCFG 8</description>
                  <addressOffset>0x8</addressOffset>
                  <size>32</size>
                  <fields>
"""

    txt += generate_field("scfg_vout0_remap_awaddr", "", "[3:0]", "read-write")
    txt += generate_field("scfg_vout1_remap_araddr", "", "[7:4]", "read-write")
    txt += generate_field("scfg_vout1_remap_awaddr", "", "[11:8]", "read-write")

    return txt + """\
                  </fields>
                </register>
"""

def generate_register_sysconsaif_syscfg12():
    txt = """\
                <register>
                  <name>sys_sysconsaif_syscfg12</name>
                  <description>SYS SYSCONSAIF SYSCFG 12: Set the GPIO voltage of all the 4 GPIO groups in this register</description>
                  <addressOffset>0xc</addressOffset>
                  <size>32</size>
                  <fields>
"""

    txt += generate_field("scfg_vout0_remap_awaddr_gpio0", "0: GPIO Group 0 (GPIO21-35) voltage select 3.3V, 1: GPIO Group 0 (GPIO21-35) voltage select 1.8V", "[0:0]", "read-write")

    txt += generate_field("scfg_vout0_remap_awaddr_gpio1", "0: GPIO Group 1 (GPIO36-63) voltage select 3.3V, 1: GPIO Group 1 (GPIO36-63) voltage select 1.8V", "[1:1]", "read-write")

    txt += generate_field("scfg_vout0_remap_awaddr_gpio2", "0: GPIO Group 2 (GPIO0-6) voltage select 3.3V, 1: GPIO Group 2 (GPIO0-6) voltage select 1.8V", "[2:2]", "read-write")

    txt += generate_field("scfg_vout0_remap_awaddr_gpio3", "0: GPIO Group 3 (GPIO7-20) voltage select 3.3V, 1: GPIO Group 3 (GPIO7-20) voltage select 1.8V", "[3:3]", "read-write")

    return txt + """\
                  </fields>
                </register>
"""

def generate_register_sysconsaif_syscfg16():
    txt = """\
                <register>
                  <name>sys_sysconsaif_syscfg16</name>
                  <description>SYS SYSCONSAIF SYSCFG 16</description>
                  <addressOffset>0x10</addressOffset>
                  <size>32</size>
                  <fields>
"""
    txt += generate_field("u0_coda12_o_cur_inst_a", "Tie 0 in JPU internal, do not care", "[1:0]", "read-only")
    txt += generate_field("u0_wave511_o_vpu_idle", "VPU monitoring signal", "[2:2]", "read-only")
    txt += generate_field("u0_can_ctrl_can_fd_enable", "", "[3:3]", "read-write")
    txt += generate_field("u0_can_ctrl_host_ecc_disable", "", "[4:4]", "read-write")
    txt += generate_field("u0_can_ctrl_host_if", "", "[23:5]", "read-only")
    txt += generate_field("u0_cdns_qspi_scfg_qspi_sclk_dlychain_sel", "des_qspi_sclk_dla: clock delay", "[28:24]", "read-only")

    return txt + """\
                  </fields>
                </register>
"""

def generate_register_sysconsaif_syscfg20():
    txt = """\
                <register>
                  <name>sys_sysconsaif_syscfg20</name>
                  <description>SYS SYSCONSAIF SYSCFG 20</description>
                  <addressOffset>0x14</addressOffset>
                  <size>32</size>
                  <fields>
"""

    for (name, base) in [("u0_cdns_qspi_scfg_sram_config", 0), ("u0_cdns_spdif_scfg_sram_config", 12)]:
        txt += generate_fields_sram_config(name, base)

    txt += generate_field("u0_cdns_spdif_trmodeo", "1 for transmitter 0 for receiver", "[24:24]", "read-only")
    txt += generate_field("u0_i2c_ic_en", "I2C interface enable", "[25:25]", "read-only")
    txt += generate_field("u0_sdio_data_strobe_phase_ctrl", "Data strobe delay chain select", "[30:26]", "read-write")
    txt += generate_field("u0_sdio_hbig_endian", "AHB bus interface endianness: 1: Big-endian AHB bus interface, 0: Little-endian AHB bus interface", "[31:31]", "read-write")

    return txt + """\
                  </fields>
                </register>
"""

def generate_register_sysconsaif_syscfg24():
    txt = """\
                <register>
                  <name>sys_sysconsaif_syscfg24</name>
                  <description>SYS SYSCONSAIF SYSCFG 24</description>
                  <addressOffset>0x18</addressOffset>
                  <size>32</size>
                  <fields>
"""

    txt += generate_field("u0_sdio_m_hbig_endian", "AHB master bus interface endianess: 1: Big-endian AHB bus interface, 0: Little-endian AHB bus interface", "[0:0]", "read-write")
    txt += generate_field("u0_i2srx_3ch_adc_ena", "", "[1:1]", "read-write")
    txt += generate_field("u0_intmem_rom_sram_scfg_disable_rom", "", "[2:2]", "read-write")
    txt += generate_fields_sram_config("u0_intmem_rom_sram_sram_config", 3)
    txt += generate_field("u0_jtag_daisy_chain_jtag_en_0", "", "[15:15]", "read-write")
    txt += generate_field("u0_jtag_daisy_chain_jtag_en_1", "", "[16:16]", "read-write")
    txt += generate_field("u0_pdrstn_split_sw_usbpipe_plugen", "", "[17:17]", "read-write")
    txt += generate_field("u0_pll_wrap_pll0_cpi_bias", "", "[20:18]", "read-write")
    txt += generate_field("u0_pll_wrap_pll0_cpp_bias", "", "[23:21]", "read-write")
    txt += generate_field("u0_pll_wrap_pll0_dacpd", "", "[24:24]", "read-write")
    txt += generate_field("u0_pll_wrap_pll0_dsmpd", "", "[25:25]", "read-write")

    return txt + """\
                  </fields>
                </register>
"""

def generate_register_sysconsaif_syscfg28():
    txt = """\
                <register>
                  <name>sys_sysconsaif_syscfg28</name>
                  <description>SYS SYSCONSAIF SYSCFG 28</description>
                  <addressOffset>0x1c</addressOffset>
                  <size>32</size>
                  <fields>
"""

    txt += generate_field("u0_pll_wrap_pll0_fbdiv", "", "[11:0]", "read-write")

    return txt + """\
                  </fields>
                </register>
"""

def generate_register_sysconsaif_syscfg32():
    txt = """\
                <register>
                  <name>sys_sysconsaif_syscfg32</name>
                  <description>SYS SYSCONSAIF SYSCFG 32</description>
                  <addressOffset>0x20</addressOffset>
                  <size>32</size>
                  <fields>
"""

    txt += generate_field("u0_pll_wrap_pll0_frac", "", "[23:0]", "read-write")
    txt += generate_field("u0_pll_wrap_pll0_gvco_bias", "", "[25:24]", "read-write")
    txt += generate_field("u0_pll_wrap_pll0_lock", "", "[26:26]", "read-only")
    txt += generate_field("u0_pll_wrap_pll0_pd", "", "[27:27]", "read-write")
    txt += generate_field("u0_pll_wrap_pll0_postdiv1", "", "[29:28]", "read-write")
    txt += generate_field("u0_pll_wrap_pll0_postdiv2", "", "[31:30]", "read-write")

    return txt + """\
                  </fields>
                </register>
"""

def generate_register_sysconsaif_syscfg36():
    txt = """\
                <register>
                  <name>sys_sysconsaif_syscfg36</name>
                  <description>SYS SYSCONSAIF SYSCFG 36</description>
                  <addressOffset>0x24</addressOffset>
                  <size>32</size>
                  <fields>
"""

    txt += generate_field("u0_pll_wrap_pll0_prediv", "", "[5:0]", "read-write")
    txt += generate_field("u0_pll_wrap_pll0_testen", "", "[6:6]", "read-write")
    txt += generate_field("u0_pll_wrap_pll0_testsel", "", "[8:7]", "read-write")
    txt += generate_field("u0_pll_wrap_pll1_cpi_bias", "", "[11:9]", "read-write")
    txt += generate_field("u0_pll_wrap_pll1_cpp_bias", "", "[14:12]", "read-write")
    txt += generate_field("u0_pll_wrap_pll1_dacpd", "", "[15:15]", "read-write")
    txt += generate_field("u0_pll_wrap_pll1_dsmpd", "", "[16:16]", "read-write")
    txt += generate_field("u0_pll_wrap_pll1_fbdiv", "", "[28:17]", "read-write")

    return txt + """\
                  </fields>
                </register>
"""

def generate_register_sysconsaif_syscfg40():
    txt = """\
                <register>
                  <name>sys_sysconsaif_syscfg40</name>
                  <description>SYS SYSCONSAIF SYSCFG 40</description>
                  <addressOffset>0x28</addressOffset>
                  <size>32</size>
                  <fields>
"""

    txt += generate_field("u0_pll_wrap_pll1_frac", "", "[23:0]", "read-write")
    txt += generate_field("u0_pll_wrap_pll1_gvco_bias", "", "[25:24]", "read-write")
    txt += generate_field("u0_pll_wrap_pll1_lock", "", "[26:26]", "read-only")
    txt += generate_field("u0_pll_wrap_pll1_pd", "", "[27:27]", "read-write")
    txt += generate_field("u0_pll_wrap_pll1_postdiv1", "", "[29:28]", "read-write")
    txt += generate_field("u0_pll_wrap_pll1_postdiv2", "", "[31:30]", "read-write")

    return txt + """\
                  </fields>
                </register>
"""

def generate_register_sysconsaif_syscfg44():
    txt = """\
                <register>
                  <name>sys_sysconsaif_syscfg44</name>
                  <description>SYS SYSCONSAIF SYSCFG 44</description>
                  <addressOffset>0x2c</addressOffset>
                  <size>32</size>
                  <fields>
"""

    txt += generate_field("u0_pll_wrap_pll1_prediv", "", "[5:0]", "read-write")
    txt += generate_field("u0_pll_wrap_pll1_testen", "", "[6:6]", "read-write")
    txt += generate_field("u0_pll_wrap_pll1_testsel", "", "[8:7]", "read-write")
    txt += generate_field("u0_pll_wrap_pll2_cpi_bias", "", "[11:9]", "read-write")
    txt += generate_field("u0_pll_wrap_pll2_cpp_bias", "", "[14:12]", "read-write")
    txt += generate_field("u0_pll_wrap_pll2_dacpd", "", "[15:15]", "read-write")
    txt += generate_field("u0_pll_wrap_pll2_dsmpd", "", "[16:16]", "read-write")
    txt += generate_field("u0_pll_wrap_pll2_fbdiv", "", "[28:17]", "read-write")

    return txt + """\
                  </fields>
                </register>
"""

def generate_register_sysconsaif_syscfg48():
    txt = """\
                <register>
                  <name>sys_sysconsaif_syscfg48</name>
                  <description>SYS SYSCONSAIF SYSCFG 48</description>
                  <addressOffset>0x30</addressOffset>
                  <size>32</size>
                  <fields>
"""

    txt += generate_field("u0_pll_wrap_pll2_frac", "", "[23:0]", "read-write")
    txt += generate_field("u0_pll_wrap_pll2_gvco_bias", "", "[25:24]", "read-write")
    txt += generate_field("u0_pll_wrap_pll2_lock", "", "[26:26]", "read-only")
    txt += generate_field("u0_pll_wrap_pll2_pd", "", "[27:27]", "read-write")
    txt += generate_field("u0_pll_wrap_pll2_postdiv1", "", "[29:28]", "read-write")
    txt += generate_field("u0_pll_wrap_pll2_postdiv2", "", "[31:30]", "read-write")

    return txt + """\
                  </fields>
                </register>
"""

def generate_register_sysconsaif_syscfg52():
    txt = """\
                <register>
                  <name>sys_sysconsaif_syscfg52</name>
                  <description>SYS SYSCONSAIF SYSCFG 52</description>
                  <addressOffset>0x34</addressOffset>
                  <size>32</size>
                  <fields>
"""

    txt += generate_field("u0_pll_wrap_pll2_prediv", "", "[5:0]", "read-write")
    txt += generate_field("u0_pll_wrap_pll2_testen", "", "[6:6]", "read-write")
    txt += generate_field("u0_pll_wrap_pll2_testsel", "", "[8:7]", "read-write")
    txt += generate_field("u0_pll_wrap_syscfg_test_pll_mode", "PLL test mode, only used for PLL BIST through jtag2apb", "[9:9]", "read-write")
    txt += generate_field("u0_saif_audio_sdin_mux_scfg_i2sdin_sel", "", "[17:10]", "read-write")
    txt += generate_field("u0_sft7110_noc_bus_clock_gating_off", "", "[18:18]", "read-write")

    for idx in range(0, 6):
        txt += generate_fields_noc_bus_oic_evemon(idx, 19 + (idx * 2))

    txt += generate_field_noc_bus_oic_evemon("start", 6, 31, "read-write")

    return txt + """\
                  </fields>
                </register>
"""

def generate_register_sysconsaif_syscfg56():
    txt = """\
                <register>
                  <name>sys_sysconsaif_syscfg56</name>
                  <description>SYS SYSCONSAIF SYSCFG 56</description>
                  <addressOffset>0x38</addressOffset>
                  <size>32</size>
                  <fields>
"""

    txt += generate_field_noc_bus_oic_evemon("trigger", 6, 0, "read-only")

    for idx in range(7, 9):
        txt += generate_fields_noc_bus_oic_evemon(idx, 1 + (idx * 2))

    for idx in range(0, 5):
        name = "u0_sft7110_noc_bus_oic_ignore_modifiable_{}".format(idx)

        bit = 5 + idx
        bit_range = "[{}:{}]".format(bit, bit)

        txt += generate_field(name, "", bit_range, "read-write") 

    return txt + """\
                  </fields>
                </register>
"""

def generate_register_noc_bus_oic_qch_clock_stop(cfg, addr, idx):
    name = "sys_sysconsaif_syscfg{}".format(cfg)
    desc = "SYS SYSCONSAIF SYSCFG {}".format(cfg) 
    address = "0x{:x}".format(addr)

    txt = """\
                <register>
                  <name>""" + name + """</name>
                  <description>""" + desc + """</description>
                  <addressOffset>""" + address + """</addressOffset>
                  <size>32</size>
                  <fields>
"""

    txt += generate_field("u0_sft7110_noc_bus_oic_qch_clock_stop_threshold_{}".format(idx), "", "[31:0]", "read-write")

    return txt + """\
                  </fields>
                </register>
"""

def generate_register_sysconsaif_syscfg96():
    txt = """\
                <register>
                  <name>sys_sysconsaif_syscfg96</name>
                  <description>SYS SYSCONSAIF SYSCFG 96</description>
                  <addressOffset>0x60</addressOffset>
                  <size>32</size>
                  <fields>
"""

    txt += generate_field("u0_tdm16slot_clkpol", "", "[0:0]", "read-only")
    txt += generate_field("u0_tdm16slot_pcm_ms", "", "[1:1]", "read-only")

    for idx in range(0, 3):
        bit = 2 + (idx * 10)

        bit_range = "[{}:{}]".format(bit + 4, bit)
        txt += generate_field("u0_trace_mtx_scfg_c{}_in0_ctl".format(idx), "", bit_range, "read-write")

        bit_range = "[{}:{}]".format(bit + 9, bit + 5)
        txt += generate_field("u0_trace_mtx_scfg_c{}_in1_ctl".format(idx), "", bit_range, "read-write")

    return txt + """\
                  </fields>
                </register>
"""

def generate_register_sysconsaif_syscfg100():
    txt = """\
                <register>
                  <name>sys_sysconsaif_syscfg100</name>
                  <description>SYS SYSCONSAIF SYSCFG 100</description>
                  <addressOffset>0x64</addressOffset>
                  <size>32</size>
                  <fields>
"""

    for idx in range(3, 5):
        bit = 0 + ((idx - 3) * 10)

        bit_range = "[{}:{}]".format(bit + 4, bit)
        txt += generate_field("u0_trace_mtx_scfg_c{}_in0_ctl".format(idx), "", bit_range, "read-write")

        bit_range = "[{}:{}]".format(bit + 9, bit + 5)
        txt += generate_field("u0_trace_mtx_scfg_c{}_in1_ctl".format(idx), "", bit_range, "read-write")

    for idx in range(0, 5):
        name = "u0_u7mc_sft7110_cease_from_tile_{}".format(idx)
        bit = 20 + idx

        txt += generate_field(name, "", "[{}:{}]".format(bit, bit), "read-only") 

    for idx in range(0, 5):
        name = "u0_u7mc_sft7110_halt_from_tile_{}".format(idx)
        bit = 25 + idx

        txt += generate_field(name, "", "[{}:{}]".format(bit, bit), "read-only") 

    return txt + """\
                  </fields>
                </register>
"""

def generate_register_sysconsaif_reset_vector(num, addr, idx, start, end, bit_range):
    name = "sys_sysconsaif_syscfg{}".format(num)
    desc = "SYS SYSCONSAIF SYSCFG {}".format(num)

    txt = """\
                <register>
                  <name>""" + name + """</name>
                  <description>""" + desc + """</description>
                  <addressOffset>""" + "0x{:x}".format(addr) + """</addressOffset>
                  <size>32</size>
                  <fields>
"""

    txt += generate_field_reset_vector(idx, start, end, bit_range)

    return txt + """\
                  </fields>
                </register>
"""

def generate_register_sysconsaif_syscfg132():
    txt = """\
                <register>
                  <name>sys_sysconsaif_syscfg132</name>
                  <description>SYS SYSCONSAIF SYSCFG 132</description>
                  <addressOffset>0x84</addressOffset>
                  <size>32</size>
                  <fields>
"""

    txt += generate_field_reset_vector(4, 32, 35, "[3:0]")

    for idx in range(1, 5):
        bit = 3 + idx
        bit_range = "[{}:{}]".format(bit, bit)

        txt += generate_field("u0_u7mc_sft7110_suppress_fetch_{}".format(idx), "", bit_range, "read-write")

    for idx in range(0, 5):
        bit = 8 + idx
        bit_range = "[{}:{}]".format(bit, bit)

        txt += generate_field("u0_u7mc_sft7110_wfi_from_tile_{}".format(idx), "", bit_range, "read-write")

    txt += generate_fields_sram_config("u0_vdec_intsram_sram_config", 13)

    return txt + """\
                  </fields>
                </register>
"""

def generate_register_sysconsaif_syscfg136():
    txt = """\
                <register>
                  <name>sys_sysconsaif_syscfg136</name>
                  <description>SYS SYSCONSAIF SYSCFG 136</description>
                  <addressOffset>0x88</addressOffset>
                  <size>32</size>
                  <fields>
"""

    txt += generate_fields_sram_config("u0_venc_intsram_sram_config", 0)
    txt += generate_field("u0_wave420l_i_ipu_current_buffer", "This signal indicates which buffer is currently active so that the VPU can correctly use the ipu_end_of_row signal for row counter.", "[14:12]", "read-write")
    txt += generate_field("u0_wave420l_i_ipu_end_of_row", "This signal is flipped every time when the IPU completes writing a row.", "[15:15]", "read-write")
    txt += generate_field("u0_wave420l_i_ipu_new_frame", "This signal is flipped every time when the IPU completes writing a new frame.", "[16:16]", "read-write")
    txt += generate_field("u0_wave420l_o_vpu_idle", "VPU monitoring signal. This signal gives out an opposite value of VPU_BUSY register.", "[17:17]", "read-only")
    txt += generate_field("u1_can_ctrl_can_fd_enable", "", "[18:18]", "read-write")
    txt += generate_field("u1_can_ctrl_host_ecc_disable", "", "[19:19]", "read-write")

    return txt + """\
                  </fields>
                </register>
"""

def generate_register_sysconsaif_syscfg140():
    txt = """\
                <register>
                  <name>sys_sysconsaif_syscfg140</name>
                  <description>SYS SYSCONSAIF SYSCFG 140</description>
                  <addressOffset>0x8c</addressOffset>
                  <size>32</size>
                  <fields>
"""

    txt += generate_field("u1_can_ctrl_host_if", "", "[18:0]", "read-only")
    txt += generate_fields_sram_config("u1_gmac5_axi64_scfg_ram_cfg", 19)

    return txt + """\
                  </fields>
                </register>
"""

def generate_register_sysconsaif_syscfg144():
    txt = """\
                <register>
                  <name>sys_sysconsaif_syscfg144</name>
                  <description>SYS SYSCONSAIF SYSCFG 144</description>
                  <addressOffset>0x90</addressOffset>
                  <size>32</size>
                  <fields>
"""

    txt += generate_field("u1_gmac5_axi64_mac_speed_0", "", "[1:0]", "read-only")
    txt += generate_field("u1_gmac5_axi64_phy_intf_sel_i", "Active PHY Selected | When you have multiple GMAC PHY interfaces in your configuration, this field indicates the sampled value of the PHY selector during reset de-assertion. | Values: 0x0:(GMII or MII), 0x01:RGMII, 0x2:SGMII, 0x3:TBI, 0x4:RMII, 0x5:RTBI, 0x6:SMII, 0x7:REVMII", "[4:2]", "read-write")

    return txt + """\
                  </fields>
                </register>
"""

def generate_register_sysconsaif_syscfg148():
    txt = """\
                <register>
                  <name>sys_sysconsaif_syscfg148</name>
                  <description>SYS SYSCONSAIF SYSCFG 148</description>
                  <addressOffset>0x94</addressOffset>
                  <size>32</size>
                  <fields>
"""

    txt += generate_field("u1_gmac5_axi64_ptp_timestamp_o_31_0", "", "[31:0]", "read-only")

    return txt + """\
                  </fields>
                </register>
"""

def generate_register_sysconsaif_syscfg152():
    txt = """\
                <register>
                  <name>sys_sysconsaif_syscfg152</name>
                  <description>SYS SYSCONSAIF SYSCFG 152</description>
                  <addressOffset>0x98</addressOffset>
                  <size>32</size>
                  <fields>
"""

    txt += generate_field("u1_gmac5_axi64_ptp_timestamp_o_63_32", "", "[31:0]", "read-only")

    return txt + """\
                  </fields>
                </register>
"""

def generate_register_sysconsaif_syscfg156():
    txt = """\
                <register>
                  <name>sys_sysconsaif_syscfg156</name>
                  <description>SYS SYSCONSAIF SYSCFG 156</description>
                  <addressOffset>0x9c</addressOffset>
                  <size>32</size>
                  <fields>
"""

    txt += generate_field("u1_i2c_ic_en", "I2C interface enable.", "[0:0]", "read-only")

    txt += generate_field("u1_sdio_data_strobe_phase_ctrl", "Data strobe delay chain select.", "[5:1]", "read-write")

    txt += generate_field("u1_sdio_hbig_endian", "AHB bus interface endianness: 1: Big-endian AHB bus interface, 0: Little-endian AHB bus interface", "[6:6]", "read-write")

    txt += generate_field("u1_sdio_m_hbig_endian", "AHB bus interface endianness: 1: Big-endian AHB bus interface, 0: Little-endian AHB bus interface", "[7:7]", "read-write")

    txt += generate_field("u1_reset_ctrl_clr_reset_status", "", "[8:8]", "read-write")
    txt += generate_field("u1_reset_ctrl_pll_timecnt_finish", "", "[9:9]", "read-only")
    txt += generate_field("u1_reset_ctrl_rstn_sw", "", "[10:10]", "read-write")
    txt += generate_field("u1_reset_ctrl_sys_reset_status", "", "[14:11]", "read-only")

    for idx in range(2, 7):
        bit = 13 + idx
        bit_range = "[{}:{}]".format(bit, bit)

        txt += generate_field("u{}_i2c_ic_en".format(idx), "I2C interface enable.", bit_range, "read-only") 

    return txt + """\
                  </fields>
                </register>
"""

def generate_fields_sram_config(name, base):
    txt = generate_field("{}_slp".format(name), "SRAM/ROM configuration. SLP: sleep enable, high active, default is low.", "[{}:{}]".format(base, base), "read-write")

    txt += generate_field("{}_sram_config_sd".format(name), "SRAM/ROM configuration. SD: shutdown enable, high active, default is low.", "[{}:{}]".format(base + 1, base + 1), "read-write")

    txt += generate_field("{}_rtsel".format(name), "SRAM/ROM configuration. RTSEL: timing setting for debug purpose, default is 2'b01.", "[{}:{}]".format(base + 3, base + 2), "read-write")
    txt += generate_field("{}_ptsel".format(name), "SRAM/ROM configuration. PTSEL: timing setting for debug purpose, default is 2'b01.", "[{}:{}]".format(base + 5, base + 4), "read-write")
    txt += generate_field("{}_trb".format(name), "SRAM/ROM configuration. TRB: timing setting for debug purpose, default is 2'b01.", "[{}:{}]".format(base + 7, base + 6), "read-write")

    txt += generate_field("{}_wtsel".format(name), "SRAM/ROM configuration. WTSEL: timing setting for debug purpose, default is 2'b01.", "[{}:{}]".format(base + 9, base + 8), "read-write")
    txt += generate_field("{}_vs".format(name), "SRAM/ROM configuration. VS: timing setting for debug purpose, default is 1'b1.", "[{}:{}]".format(base + 10, base + 10), "read-write")

    txt += generate_field("{}_vg".format(name), "SRAM/ROM configuration. VG: timing setting for debug purpose, default is 1'b1.", "[{}:{}]".format(base + 11, base + 11), "read-write")

    return txt

def generate_fields_noc_bus_oic_evemon(idx, bit):
    txt = generate_field_noc_bus_oic_evemon("start", idx, bit, "read-write") 
    return txt + generate_field_noc_bus_oic_evemon("trigger", idx, bit + 1, "read-only")

def generate_field_noc_bus_oic_evemon(field, idx, bit, access):
    name = "u0_sft7110_noc_bus_oic_evemon_{}_{}".format(idx, field)
    bitfield = "[{}:{}]".format(bit, bit)

    return generate_field(name, "", bitfield, access)

def generate_field_reset_vector(idx, start, end, bit_range):
    return generate_field("u0_u7mc_sft7110_reset_vector_{}_{}_{}".format(idx, end, start), "", bit_range, "read-write")
