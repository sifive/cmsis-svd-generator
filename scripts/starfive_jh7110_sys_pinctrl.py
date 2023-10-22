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

    for idx in range(16):
        txt += generate_register_fmux_gpo_doen(idx)

    for idx in range(16, 32):
        txt += generate_register_fmux_gpo_dout(idx, 16)

    for idx in range(32, 55):
        txt += generate_register_fmux_gpi(idx, 32)

    txt += generate_registers_ioirq()
    txt += generate_registers_padcfg()
    txt += generate_registers_func_sel()

    return txt + """\
              </registers>
"""

def generate_register_fmux_gpo_doen(idx):
    reset_values = [
        #        0           1           2           3
        0x08010101, 0x00010001, 0x07010100, 0x00000101,
        #        4           5           6           7
        0x01000000, 0x00000000, 0x00000000, 0x00000000,
        #        8           9          10          11
        0x00000000, 0x23220605, 0x01000001, 0x01000001,
        #       12          13          14          15
        0x0e010d0d, 0x1d011c1c, 0x25012424, 0x29012828,
    ]

    name = "gpo_doen{}".format(idx)
    desc = "SYS IOMUX CFG SAIF SYSCFG FMUX {} DOEN".format(idx)

    ndra = [
        (
            "gpo{}_doen".format((idx * 4) + i), 
            "The selected OEN signal for GPIO{}. The register value indicates the selected GPIO (Output Enable) OEN index from GPIO OEN list 0-49. See Table 2-41: GPIO OEN List for SYS_IOMUX (on page 97) for more information.".format((idx * 4) + i),
            "[{}:{}]".format((i * 8) + 5, i * 8),
            "read-write",
        )
        for i in range(4)
    ]

    return generate_register(name, desc, idx * 4, ndra, 32, reset_values[idx])

def generate_register_fmux_gpo_dout(idx, base):
    reset_values = [
        #       16          17          18          19
        0x16000000, 0x00001400, 0x15000000, 0x00000000,
        #       20          21          22          23
        0x20000000, 0x00550000, 0x00000000, 0x00000000,
        #       24          25          26          27
        0x0d000000, 0x54530f0e, 0x004e4f00, 0x005b5c00,
        #       28          29          30          31
        0x20001e1f, 0x4b00494a, 0x58005657, 0x5f005d5e,
    ]

    gpo_base = (idx - base) * 4
    gpo_end = gpo_base + 3

    name = "gpo_dout{}_{}".format(gpo_base, gpo_end)
    desc = "SYS IOMUX CFG SAIF SYSCFG FMUX GPIO {}-{} DOUT".format(gpo_base, gpo_end)
    addr = "0x{:x}".format(idx * 4)

    ndra = [
        (
            "gpo{}_dout".format(gpo_base + i), 
            "The selected output signal for GPIO{}. The register value indicates the selected GPIO output index signal index from GPIO output signal list 0-107. See Table 2-41: GPIO OEN List for SYS_IOMUX (on page 97) for more information.".format(gpo_base + i),
            "[{}:{}]".format((i * 8) + 6, i * 8),
            "read-write",
        )
        for i in range(4)
    ]

    return generate_register(name, desc, idx * 4, ndra, 32, reset_values[idx - base])

def generate_register_fmux_gpi(idx, base):
    reset_values = [
        #       32          33          34          35
        0x00000000, 0x00000002, 0x00272600, 0x0b080000,
        #       36          37          38          39
        0x040f0e0c, 0x00000006, 0x32330000, 0x00000334,
        #       40          41          42          43
        0x00000000, 0x00000000, 0x00000000, 0x00000000,
        #       44          45          46          47
        0x00000000, 0x00000000, 0x00383637, 0x002a2d00,
        #       48          49          50          51
        0x29280000, 0x3c3a3b15, 0x2e310000, 0x00403e3f,
        #       52          53          54
        0x00000000, 0x00000000, 0x00000000,
    ]

    field_names = [
        [ # 32
            "u0_WAVE511_i_uart_rxsin_cfg",
            "u0_can_ctrl_rxd_cfg",
            "u0_cdn_usb_over_current_n_io_cfg",
            "u0_cdns_spdif_spdi_fi_cfg",
        ],
        [ # 33
            "u0_clkrst_src_bypass_jtag_trstn_cfg",
            "u0_dom_vout_top_u0_hdmi_tx_pin_cec_sda_in_cfg",
            "u0_dom_vout_top_u0_hdmi_tx_pin_ddc_scl_in_cfg",
            "u0_dom_vout_top_u0_hdmi_tx_pin_ddc_sda_in_cfg",
        ],
        [ # 34
            "u0_dom_vout_top_u0_hdmi_tx_pin_hpd_cfg",
            "u0_i2c_ic_clk_in_a_cfg",
            "u0_i2c_ic_data_in_a_cfg",
            "u0_sdio_card_detect_n_cfg",
        ],
        [ # 35
            "u0_sdio_card_int_n_cfg",
            "u0_sdio_card_write_prt_cfg",
            "u0_uart_sin_cfg",
            "u0_hifi4_jtck_cfg",
        ],
        [ # 36
            "u0_hifi4_jtdi_cfg",
            "u0_hifi4_jtms_cfg",
            "u0_hifi4_jtrstn_cfg",
            "u0_jtag_certification_tdi_cfg",
        ],
        [ # 37
            "u0_jtag_certification_tms_cfg",
            "u0_pdm_4mic_dmic0_din_cfg",
            "u0_pdm_4mic_dmic1_din_cfg",
            "u0_saif_audio_sdin_mux_i2srx_ext_sdin0_cfg",
        ],
        [ # 38
            "u0_saif_audio_sdin_mux_i2srx_ext_sdin1_cfg",
            "u0_saif_audio_sdin_mux_i2srx_ext_sdin2_cfg",
            "u0_ssp_spi_sspclkin_cfg",
            "u0_ssp_spi_sspfssin_cfg",
        ],
        [ # 39
            "u0_ssp_spi_ssprxd_cfg",
            "u0_sys_crg_clk_jtag_tck_cfg",
            "u0_sys_crg_ext_mclk_cfg",
            "u0_sys_crg_i2srx_bclk_slv_cfg",
        ],
        [ # 40
            "u0_sys_crg_i2srx_lrck_slv_cfg",
            "u0_sys_crg_i2stx_bclk_slv_cfg",
            "u0_sys_crg_i2stx_lrck_slv_cfg",
            "u0_sys_crg_tdm_clk_slv_cfg",
        ],
        [ # 41
            "u0_tdm16slot_pcm_rxd_cfg",
            "u0_tdm16slot_pcm_synon_cfg",
            "u1_can_ctrl_rxd_cfg",
            "u1_i2c_ic_clk_in_a_cfg",
        ],
        [ # 42
            "u1_i2c_ic_data_in_a_cfg",
            "u1_sdio_card_detect_n_cfg",
            "u1_sdio_card_int_n_cfg",
            "u1_sdio_card_write_prt_cfg",
        ],
        [ # 43
            "u1_sdio_ccmd_in_cfg",
            "u1_sdio_cdata_in_0_cfg",
            "u1_sdio_cdata_in_1_cfg",
            "u1_sdio_cdata_in_2_cfg",
        ],
        [ # 44
            "u1_sdio_cdata_in_3_cfg",
            "u1_sdio_cdata_in_4_cfg",
            "u1_sdio_cdata_in_5_cfg",
            "u1_sdio_cdata_in_6_cfg",
        ],
        [ # 45
            "u1_sdio_cdata_in_7_cfg",
            "u1_sdio_data_strobe_cfg",
            "u1_uart_cts_n_cfg",
            "u1_uart_sin_cfg",
        ],
        [ # 46
            "u1_ssp_spi_ssp_clkin_cfg",
            "u1_ssp_spi_sspfssin_cfg",
            "u1_ssp_spi_ssprxd_cfg",
            "u2_i2c_ic_clk_in_a_cfg",
        ],
        [ # 47
            "u2_i2c_ic_data_in_a_cfg",
            "u2_uart_cts_n_cfg",
            "u2_uart_sin_cfg",
            "u2_ssp_spi_sspclkin_cfg",
        ],
        [ # 48
            "u2_ssp_spi_sspfssin_cfg",
            "u2_ssp_spi_ssprxd_cfg",
            "u3_i2c_ic_clk_in_a_cfg",
            "u3_i2c_ic_data_in_a_cfg",
        ],
        [ # 49
            "u3_uart_sin_cfg",
            "u3_ssp_spi_sspclkin_cfg",
            "u3_ssp_spi_sspfssin_cfg",
            "u3_ssp_spi_ssprxd_cfg",
        ],
        [ # 50
            "u4_i2c_ic_clk_in_a_cfg",
            "u4_i2c_ic_data_in_a_cfg",
            "u4_uart_cts_n_cfg",
            "u4_uart_sin_cfg",
        ],
        [ # 51
            "u4_ssp_spi_sspclkin_cfg",
            "u4_ssp_spi_sspfssin_cfg",
            "u4_ssp_spi_ssprxd_cfg",
            "u5_i2c_ic_clk_in_a_cfg",
        ],
        [ # 52
            "u5_i2c_ic_data_in_a_cfg",
            "u5_uart_cts_n_cfg",
            "u5_uart_sin_cfg",
            "u5_ssp_spi_sspclkin_cfg",
        ],
        [ # 53
            "u5_ssp_spi_sspfssin_cfg",
            "u5_ssp_spi_ssprxd_cfg",
            "u6_i2c_ic_clk_in_a_cfg",
            "u6_i2c_ic_data_in_a_cfg",
        ],
        [ # 54
            "u6_ssp_spi_sspclkin_cfg",
            "u6_ssp_spi_sspfssin_cfg",
            "u6_ssp_spi_ssprxd_cfg",
            "",
        ],
    ]

    gpi_base = (idx - base) * 4

    name = "gpi{}".format(gpi_base)
    desc = """SYS IOMUX CFG SAIF SYSCFG FMUX GPIO GPI {} - The register can be used to configure the selected GPIO connector number for input signals. The signal name is indicated in the "Name" column of the following table per StarFive naming conventions. For example, name "u0_WAVE511_i_uart_rxsin_cfg" indicates the corresponding input signal is "u0_WAVE511.i_uart_rxsin". See GPIO Input Signals (on page 107) for a complete list of the input GPIO signals.""".format(gpi_base)

    ndra = [
        (
            field_names[idx - base][i], 
            "The register value indicates the selected GPIO number + 2 (GPIO2 - GPIO63, GPIO0 and GPIO1 are not available) for the input signal.",
            "[{}:{}]".format((i * 8) + 6, i * 8),
            "read-write",
        )
        for i in range(4) if field_names[idx - base][i]
    ]

    return generate_register(name, desc, idx * 4, ndra, 32, reset_values[idx - base])

def generate_registers_ioirq():
    txt = generate_register("ioirq0", "Enable GPIO IRQ function", 0xdc, [
        ("gpioen0", "1: Enable, 0: Disable", "[0:0]", "read-write")
    ])

    d_fn_fd_a = [
        ("GPIO Interrupt Edge Trigger Selector", "gpiois{}", "1: Edge trigger, 0: Level trigger", "read-write"), 
        ("GPIO Interrupt Clear", "gpioic{}", "1: Do not clear the register, 0: Clear the register", "read-write"), 
        ("GPIO Interrupt Both Edge Trigger Selector", "gpioibe{}", "1: Trigger on both edges, 0: Trigger on a single edge", "read-write"), 
        ("GPIO Interrupt Edge Value", "gpioiev{}", "1: Positive/Low, 0: Negative/High", "read-write"), 
        ("GPIO Interrupt Edge Mask Selector", "gpioie{}", "1: Unmask, 0: Mask", "read-write"), 
        ("GPIO Register Interrupt Status", "gpioris{}", "Status of the edge trigger. The register can be cleared by writing gpio ic", "read-only"), 
        ("GPIO Masked Interrupt Status", "gpiomis{}", "The masked GPIO IRQ status", "read-only"), 
        ("GPIO Synchronization Status", "gpio_in_sync2_{}", "Status of the gpio_in after synchronization", "read-only"),
    ]

    for idx in range(len(d_fn_fd_a)):
        (desc, field_name, field_desc, access) = d_fn_fd_a[idx]

        addr_idx = 56 + (idx * 2)
        txt += generate_register(
            "ioirq{}".format((idx * 2) + 1),
            "SYS IOMUX CFGSAIF SYSCFG IOIRQ {}: {}".format(addr_idx, desc),
            addr_idx,
            [(field_name.format(0), field_desc, "[31:0]", access)]
        )

        addr_idx += 1
        txt += generate_register(
            "ioirq{}".format((idx * 2) + 2),
            "SYS IOMUX CFGSAIF SYSCFG IOIRQ {}: {}".format(addr_idx, desc),
            addr_idx,
            [(field_name.format(1), field_desc, "[31:0]", access)]
        )

    return txt

def generate_registers_padcfg():
    txt = ""

    for idx in range(64):
        txt += generate_register_padcfg(idx, "gpio{}".format(idx))

    txt += generate_register_padcfg(64, "sd0_clk")
    txt += generate_register_padcfg(65, "sd0_cmd")

    for idx in range(8):
        txt += generate_register_padcfg(66 + (idx * 4), "sd0_data{}".format(idx))

    txt += generate_register_padcfg(74, "sd0_strb")

    names = [
        "mdc", "mdio", "rxd0", "rxd1", "rxd2", "rxd3", "rxdv",
        "rxc", "txd0", "txd1", "txd2", "txd3", "txen", "txc",
    ]
    for idx in range(len(names)):
        name = "padcfg_gmac1_{}_syscon".format(names[idx])
        desc = "GPIO GMAC1 {} Pad Configuration".format(names[idx].upper())
        ndra = [("padcfg_pad_gmac1_{}_syscon".format(names[idx]), "", "[1:0]", "read-write")]

        txt += generate_register(name, desc,  75 + (idx * 4), ndra, 32, 0x2)

    txt += generate_register_padcfg(89, "qspi_sclk")
    txt += generate_register_padcfg(90, "qspi_csn0")
 
    for idx in range(0, 4):
        txt += generate_register_padcfg(91 + (idx * 4), "qspi_data{}".format(idx))

    return txt

def generate_register_padcfg(idx, pin):
    name = "padcfg_{}".format(pin)
    addr = 288 + (idx * 4)
    desc = "SYS IOMUX CFG SAIF SYSCFG PADCFG {}: {}".format(addr, pin.upper())
    base = 72

    reset_values = [
        # GPIO DATA
        #  0     1     2     3     4     5     6     7
        0x11, 0x09, 0x01, 0x01, 0x09, 0x00, 0x09, 0x01,
        #  8     9    10    11    12    13    14    15
        0x01, 0x09, 0x01, 0x01, 0x09, 0x09, 0x01, 0x01,
        # 16    17    18    19    20    21    22    23
        0x01, 0x01, 0x09, 0x09, 0x01, 0x01, 0x01, 0x01,
        # 24    25    26    27    28    29    30    31
        0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01,
        # 32    33    34    35    36    37    38    39
        0x01, 0x00, 0x01, 0x11, 0x09, 0x09, 0x09, 0x09,
        # 40    41    42    43    44    45    46    47
        0x09, 0x09, 0x09, 0x09, 0x09, 0x09, 0x09, 0x09,
        # 48    49    50    51    52    53    54    55
        0x09, 0x01, 0x01, 0x01, 0x09, 0x01, 0x01, 0x01,
        # 56    57    58    59    60    61    62    63
        0x09, 0x01, 0x01, 0x01, 0x09, 0x01, 0x01, 0x01,
        # SD0 CMD
        0x01,
        # SD0 DATA
        #  0     1     2     3     4     5     6     7
        0x09, 0x01, 0x01, 0x09, 0x09, 0x01, 0x01, 0x01,
        # SD0 STRB
        0x01,
        # Placeholders for non-PADCFG registers
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        # QSPI
        0x01,
        # QSPI CSn0
        0x08,
        # QSPI DATA
        #  0     1     2     3     4     5     6     7
        0x01, 0x01, 0x01, 0x01, 0x09, 0x01, 0x01, 0x01,
    ]

    ndra = [
        ("ie", "Input Enable (IE) Controller - 1: Enable the receiver, 0: Disable the receiver", "[0:0]", "read-write"),
        ("ds", "Output Drive Strength (DS) - 00: The rated drive strength is 2 mA, 01: The rated drive strength is 4 mA, 10: The rated drive strength is 8 mA, 11: The rated drive strength is 12 mA", "[2:1]", "read-write"),
        ("pu", "Pull-Up (PU) settings - 1: Yes, 0: No", "[3:3]", "read-write"),
        ("pd", "Pull-Down (PD) settings - 1: Yes, 0: No", "[4:4]", "read-write"),
        ("slew", "Slew Rate Control - 0: Slow (Half frequency), 1: Fast", "[5:5]", "read-write"),
        ("smt", "Active high Schmitt (SMT) trigger selector - 0: No hysteresis, 1: Schmitt trigger ebabled", "[6:6]", "read-write"),
        ("pos", "Power-on-Start (POS) enabler - 1: Enable active pull down for loss of core power, 0: Active pull-down capability disabled", "[7:7]", "read-write"),
    ]

    return generate_register(name, desc, addr, ndra, 32, reset_values[idx - base]) 

def generate_registers_func_sel():
    # 0
    nfras = [[("pad_gmac1_rxc", "GMAC", "[1:0]", "read-write")]]

    for idx in range(0, 10):
        bit = 2 + (idx * 3)
        nfras[0].append(("pad_gpio1{}".format(idx), "GPIO", "[{}:{}]".format(bit + 2, bit), "read-write"))

    # 1
    nfras.append([
        (
            "pad_gpio{}".format(20 + i),
            "GPIO",
            "[{}:{}]".format((i * 3) + 2, i * 3),
            "read-write"
        )
        for i in range(0, 10)
    ])

    # 2
    nfras.append([
        (
            "pad_gpio{}".format(30 + i),
            "GPIO",
            "[{}:{}]".format((i * 3) + 2, i * 3),
            "read-write"
        )
        for i in range(0, 11)
    ])

    # 3
    nfras.append([
        (
            "pad_gpio{}".format(41 + i),
            "GPIO",
            "[{}:{}]".format((i * 3) + 2, i * 3),
            "read-write"
        )
        for i in range(0, 11)
    ])

    # 4
    nfras.append([
        (
            "pad_gpio{}".format(52 + i),
            "GPIO",
            "[{}:{}]".format((i * 2) + 1, i * 2),
            "read-write"
        )
        for i in range(0, 3)
    ])

    for i in range(4, 11):
        bit = i * 3
        nfras[4].append(("pad_gpio{}".format(52 + i), "GPIO", "[{}:{}]".format(bit + 2, bit), "read-write"))

    nfras[4].append(("pad_gpio63", "GPIO", "[31:30]", "read-write"))

    # 5
    nfras.append([("pad_gpio6", "GPIO", "[1:0]", "read-write")])

    for i in range(1, 4):
        nfras[5].append(
            (
                "pad_gpio{}".format(6 + i),
                "GPIO",
                "[{}:{}]".format((i * 3) + 2, i * 3),
                "read-write"
            )
        )

    idx = [0, 10, 11, 1, 2, 3, 4]
    for i in range(len(idx)):
        bit = 11 + (i * 3)
        nfras[5].append(
            (
                "u0_dom_isp_top_u0_vin_dvp_data_c{}".format(idx[i]),
                "DVP_DATA",
                "[{}:{}]".format(bit + 2, bit),
                "read-write"
            )
        )

    # 6
    nfras.append([
        (
            "u0_dom_isp_top_u0_vin_dvp_data_c{}".format(5 + i),
            "DVP_DATA",
            "[{}:{}]".format((i * 3) + 2, i * 3),
            "read-write"
        )
        for i in range(5)
    ])

    nfras[6].append(("u0_dom_isp_top_u0_vin_dvp_hvalid_c", "DVP_HSYNC", "[17:15]", "read-write"))
    nfras[6].append(("u0_dom_isp_top_u0_vin_dvp_vvalid_c", "DVP_VSYNC", "[20:18]", "read-write"))
    nfras[6].append(("u0_sys_crg_dvp_clk", "DVP_CLK", "[23:21]", "read-write"))

    txt = ""

    for idx in range(len(nfras)):
        txt += generate_register_sys_iomux_cfgsaif_syscfg_func_sel(idx, nfras[idx])

    return txt

def generate_register_sys_iomux_cfgsaif_syscfg_func_sel(idx, name_func_range_access):
    name = "func_sel{}".format(idx)
    desc = "SYS IOMUX CFG SAIF SYSCFG {}".format(idx)
    addr = 668 + (idx * 4)

    func_desc = {
            "GMAC": "Function selector of GMAC1_RXC: * Function 0: u0_sys_crg.clk_gmac1_rgmii_rx, * Function 1: u0_sys_crg.clk_gmac1_rmii_ref, * Function 2: None, * Function 3: None",
            "GPIO": "GPIO function selector: * Function 0: See Function Description no page 84 for more information, * Function 1: See Full Multiplexing for more information, * Function 2: See Function 2 for more information, * Function 3: See Function 3 for more information",
            "DVP_DATA": "Function Selector of DVP_DATA[idx], see Function 2 for more information",
            "DVP_HSYNC": "Function Selector of DVP_HSYNC, see Function 2 for more information",
            "DVP_VSYNC": "Function Selector of DVP_VSYNC, see Function 2 for more information",
            "DVP_CLK": "Function Selector of DVP_CLK, see Function 2 for more information",
    }

    ndra = [("{}_func_sel".format(n), func_desc[f], r, a) for (n, f, r, a) in name_func_range_access]

    return generate_register(name, desc, addr, ndra)
