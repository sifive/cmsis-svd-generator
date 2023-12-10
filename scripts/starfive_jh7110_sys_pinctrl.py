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

    name = "gpo_doen_{}".format(idx)
    desc = "SYS IOMUX CFG SAIF SYSCFG FMUX {} DOEN".format(idx)

    ndra = [
        (
            "doen_{}".format((idx * 4) + i),
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

    name = "gpo_dout_{}_{}".format(gpo_base, gpo_end)
    desc = "SYS IOMUX CFG SAIF SYSCFG FMUX GPIO {}-{} DOUT".format(gpo_base, gpo_end)
    addr = idx * 4

    ndra = [
        (
            "dout_{}".format(gpo_base + i),
            "The selected output signal for GPIO{}. The register value indicates the selected GPIO output index signal index from GPIO output signal list 0-107. See Table 2-41: GPIO OEN List for SYS_IOMUX (on page 97) for more information.".format(gpo_base + i),
            "[{}:{}]".format((i * 8) + 6, i * 8),
            "read-write",
        )
        for i in range(4)
    ]

    return generate_register(name, desc, addr, ndra, 32, reset_values[idx - base])

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
            "wave511_uart_rxsin",
            "can_rxd_0",
            "usb_over_current",
            "spdif_spdi_fi",
        ],
        [ # 33
            "jtag_trstn",
            "hdmi_cec_sda",
            "hdmi_ddc_scl",
            "hdmi_ddc_sda",
        ],
        [ # 34
            "hdmi_hpd",
            "i2c_clk_0",
            "i2c_data_0",
            "sdio_detect_0",
        ],
        [ # 35
            "sdio_int_0",
            "sdio_write_prt_0",
            "uart_sin_0",
            "hifi4_jtck_0",
        ],
        [ # 36
            "hifi4_jtdi",
            "hifi4_jtms",
            "hifi4_jtrstn",
            "jtag_tdi",
        ],
        [ # 37
            "jtag_tms",
            "pdm_dmic_0",
            "pdm_dmic_1",
            "audio_i2srx_0",
        ],
        [ # 38
            "audio_i2srx_1",
            "audio_i2srx_2",
            "spi_clkin_0",
            "spi_fssin_0",
        ],
        [ # 39
            "spi_rxd_0",
            "jtag_tck",
            "mclk",
            "i2srx_bclk_slv_0",
        ],
        [ # 40
            "i2srx_lrck_slv_0",
            "i2stx_bclk_slv_0",
            "i2stx_lrck_slv_0",
            "tdm_clk_slv_0",
        ],
        [ # 41
            "pcm_rxd_0",
            "pcm_synon_0",
            "can_rxd_1",
            "i2c_clk_1",
        ],
        [ # 42
            "i2c_data_1",
            "sdio_detect_1",
            "sdio_int_1",
            "sdio_write_prt_1",
        ],
        [ # 43
            "sdio_ccmd_1",
            "sdio_cdata_0",
            "sdio_cdata_1",
            "sdio_cdata_2",
        ],
        [ # 44
            "sdio_cdata_3",
            "sdio_cdata_4",
            "sdio_cdata_5",
            "sdio_cdata_6",
        ],
        [ # 45
            "sdio_cdata_7",
            "sdio_data_strobe",
            "uart_cts_1",
            "uart_sin_1",
        ],
        [ # 46
            "spi_clkin_1",
            "spi_fssin_1",
            "spi_rxd_1",
            "i2c_clk_2",
        ],
        [ # 47
            "i2c_data_2",
            "uart_cts_2",
            "uart_sin_2",
            "spi_clkin_2",
        ],
        [ # 48
            "spi_fssin_2",
            "spi_rxd_2",
            "i2c_clk_3",
            "i2c_data_3",
        ],
        [ # 49
            "uart_sin_3",
            "spi_clkin_3",
            "spi_fssin_3",
            "spi_rxd_3",
        ],
        [ # 50
            "i2c_clk_4",
            "i2c_data_4",
            "uart_cts_4",
            "uart_sin_4",
        ],
        [ # 51
            "spi_clkin_4",
            "spi_fssin_4",
            "spi_rxd_4",
            "i2c_clk_5",
        ],
        [ # 52
            "i2c_data_5",
            "uart_cts_5",
            "uart_sin_5",
            "spi_clkin_5",
        ],
        [ # 53
            "spi_fssin_5",
            "spi_rxd_5",
            "i2c_clk_6",
            "i2c_data_6",
        ],
        [ # 54
            "spi_clkin_6",
            "spi_fssin_6",
            "spi_rxd_6",
            "",
        ],
    ]

    gpi_base = (idx - base) * 4

    name = "gpi_{}".format(idx - base)
    desc = """SYS IOMUX CFG SAIF SYSCFG FMUX GPIO GPI {} - The register can be used to configure the selected GPIO connector number for input signals. The signal name is indicated in the "Name" column of the following table per StarFive naming conventions. For example, name "u0_WAVE511_i_uart_rxsin_cfg" indicates the corresponding input signal is "u0_WAVE511.i_uart_rxsin". See GPIO Input Signals (on page 107) for a complete list of the input GPIO signals.""".format(gpi_base)
    addr = idx * 4

    ndra = [
        (
            field_names[idx - base][i],
            "The register value indicates the selected GPIO number + 2 (GPIO2 - GPIO63, GPIO0 and GPIO1 are not available) for the input signal.",
            "[{}:{}]".format((i * 8) + 6, i * 8),
            "read-write",
        )
        for i in range(4) if field_names[idx - base][i]
    ]

    return generate_register(name, desc, addr, ndra, 32, reset_values[idx - base])

def generate_registers_ioirq():
    txt = generate_register("ioirq_0", "Enable GPIO IRQ function", 0xdc, [
        ("gpen_0", "1: Enable, 0: Disable", "[0:0]", "read-write")
    ])

    d_fn_fd_a = [
        ("GPIO Interrupt Edge Trigger Selector", "is_{}", "1: Edge trigger, 0: Level trigger", "read-write"),
        ("GPIO Interrupt Clear", "ic_{}", "1: Do not clear the register, 0: Clear the register", "read-write"),
        ("GPIO Interrupt Both Edge Trigger Selector", "ibe_{}", "1: Trigger on both edges, 0: Trigger on a single edge", "read-write"),
        ("GPIO Interrupt Edge Value", "iev_{}", "1: Positive/Low, 0: Negative/High", "read-write"),
        ("GPIO Interrupt Edge Mask Selector", "ie_{}", "1: Unmask, 0: Mask", "read-write"),
        ("GPIO Register Interrupt Status", "ris_{}", "Status of the edge trigger. The register can be cleared by writing gpio ic", "read-only"),
        ("GPIO Masked Interrupt Status", "mis_{}", "The masked GPIO IRQ status", "read-only"),
        ("GPIO Synchronization Status", "in_sync2_{}", "Status of the gpio_in after synchronization", "read-only"),
    ]

    for idx in range(len(d_fn_fd_a)):
        (desc, field_name, field_desc, access) = d_fn_fd_a[idx]

        addr_idx = 0xe0 + (idx * 8)
        txt += generate_register(
            "ioirq_{}".format((idx * 2) + 1),
            "SYS IOMUX CFGSAIF SYSCFG IOIRQ {}: {}".format(addr_idx, desc),
            addr_idx,
            [(field_name.format(0), field_desc, "[31:0]", access)]
        )

        addr_idx += 4
        txt += generate_register(
            "ioirq_{}".format((idx * 2) + 2),
            "SYS IOMUX CFGSAIF SYSCFG IOIRQ {}: {}".format(addr_idx, desc),
            addr_idx,
            [(field_name.format(1), field_desc, "[31:0]", access)]
        )

    return txt

def generate_registers_padcfg():
    txt = ""

    for idx in range(64):
        txt += generate_register_padcfg(idx, "gpio_{}".format(idx))

    txt += generate_register_padcfg(64, "sd0_clk")
    txt += generate_register_padcfg(65, "sd0_cmd")

    for idx in range(8):
        txt += generate_register_padcfg(66 + idx, "sd0_data_{}".format(idx))

    txt += generate_register_padcfg(74, "sd0_strb")

    names = [
        "mdc", "mdio", "rxd_0", "rxd_1", "rxd_2", "rxd_3", "rxdv",
        "rxc", "txd_0", "txd_1", "txd_2", "txd_3", "txen", "txc",
    ]
    for idx in range(len(names)):
        name = "gmac1_{}".format(names[idx])
        desc = "GPIO GMAC1 {} Pad Configuration".format(names[idx].upper())
        ndra = [("cfg", "", "[1:0]", "read-write")]

        txt += generate_register(name, desc, 0x24c + (idx * 4), ndra, 32, 0x2)

    txt += generate_register_padcfg(89, "qspi_sclk")
    txt += generate_register_padcfg(90, "qspi_csn_0")

    for idx in range(4):
        txt += generate_register_padcfg(91 + idx, "qspi_data_{}".format(idx))

    return txt

def generate_register_padcfg(idx, name):
    addr = 0x120 + (idx * 4)
    desc = "SYS IOMUX CFG SAIF SYSCFG PADCFG {}: {}".format(addr, name.upper())

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

    return generate_register(name, desc, addr, ndra, 32, reset_values[idx])

def generate_registers_func_sel():
    # 0
    nfras = [[("pad_gmac1_rxc", "GMAC", "[1:0]", "read-write")]]

    for idx in range(0, 10):
        bit = 2 + (idx * 3)
        nfras[0].append(("pad_gpio_1{}".format(idx), "GPIO", "[{}:{}]".format(bit + 2, bit), "read-write"))

    # 1
    nfras.append([
        (
            "pad_gpio_{}".format(20 + i),
            "GPIO",
            "[{}:{}]".format((i * 3) + 2, i * 3),
            "read-write"
        )
        for i in range(10)
    ])

    # 2
    nfras.append([
        (
            "pad_gpio_{}".format(30 + i),
            "GPIO",
            "[{}:{}]".format((i * 3) + 2, i * 3),
            "read-write"
        )
        for i in range(11)
    ])

    # 3
    nfras.append([
        (
            "pad_gpio_{}".format(41 + i),
            "GPIO",
            "[{}:{}]".format((i * 3) + 2, i * 3),
            "read-write"
        )
        for i in range(11)
    ])

    # 4
    nfras.append([
        (
            "pad_gpio_{}".format(52 + i),
            "GPIO",
            "[{}:{}]".format((i * 2) + 1, i * 2),
            "read-write"
        )
        for i in range(3)
    ])

    for i in range(4, 11):
        bit = i * 3
        nfras[4].append(("pad_gpio_{}".format(52 + i), "GPIO", "[{}:{}]".format(bit + 2, bit), "read-write"))

    nfras[4].append(("pad_gpio63", "GPIO", "[31:30]", "read-write"))

    # 5
    nfras.append([("pad_gpio_6", "GPIO", "[1:0]", "read-write")])

    for i in range(1, 4):
        nfras[5].append(
            (
                "pad_gpio_{}".format(6 + i),
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
                "vin_dvp_data_{}".format(idx[i]),
                "DVP_DATA",
                "[{}:{}]".format(bit + 2, bit),
                "read-write"
            )
        )

    # 6
    nfras.append([
        (
            "vin_dvp_data_{}".format(5 + i),
            "DVP_DATA",
            "[{}:{}]".format((i * 3) + 2, i * 3),
            "read-write"
        )
        for i in range(5)
    ])

    nfras[6].append(("vin_dvp_hvalid", "DVP_HSYNC", "[17:15]", "read-write"))
    nfras[6].append(("vin_dvp_vvalid", "DVP_VSYNC", "[20:18]", "read-write"))
    nfras[6].append(("dvp_clk", "DVP_CLK", "[23:21]", "read-write"))

    txt = ""

    for idx in range(len(nfras)):
        txt += generate_register_sys_iomux_cfgsaif_syscfg_func_sel(idx, nfras[idx])

    return txt

def generate_register_sys_iomux_cfgsaif_syscfg_func_sel(idx, name_func_range_access):
    name = "func_sel_{}".format(idx)
    addr = 668 + (idx * 4)
    desc = "SYS IOMUX CFG SAIF SYSCFG {}".format(addr)

    func_desc = {
            "GMAC": "Function selector of GMAC1_RXC: * Function 0: u0_sys_crg.clk_gmac1_rgmii_rx, * Function 1: u0_sys_crg.clk_gmac1_rmii_ref, * Function 2: None, * Function 3: None",
            "GPIO": "GPIO function selector: * Function 0: See Function Description no page 84 for more information, * Function 1: See Full Multiplexing for more information, * Function 2: See Function 2 for more information, * Function 3: See Function 3 for more information",
            "DVP_DATA": "Function Selector of DVP_DATA[idx], see Function 2 for more information",
            "DVP_HSYNC": "Function Selector of DVP_HSYNC, see Function 2 for more information",
            "DVP_VSYNC": "Function Selector of DVP_VSYNC, see Function 2 for more information",
            "DVP_CLK": "Function Selector of DVP_CLK, see Function 2 for more information",
    }

    ndra = [(n, func_desc[f], r, a) for (n, f, r, a) in name_func_range_access]

    return generate_register(name, desc, addr, ndra)
