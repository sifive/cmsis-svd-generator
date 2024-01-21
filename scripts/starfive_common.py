import logging

def generate_registers_mux_sel(name, desc, addr, field_desc):
    """Generate xml string for starfive_jh7110_syscrg """ + name + """ register"""
    return generate_register(name, desc, addr, [generate_field_mux_sel(field_desc)])

def generate_registers_divcfg(name, desc, addr, mdmt):
    """Generate xml string for starfive_jh7110_syscrg """ + name + """ register"""
    return generate_register(name, desc, addr, [generate_field_divcfg(mdmt)])

def generate_registers_mux_sel_divcfg(name, desc, addr, field_desc, mdmt):
    """Generate xml string for starfive_jh7110_syscrg """ + name + """ register"""
    return generate_register(name, desc, addr, [
        generate_field_mux_sel(field_desc),
        generate_field_divcfg(mdmt)
    ])

def generate_registers_icg(name, desc, addr):
    """Generate xml string for starfive_jh7110_syscrg """ + name + """ register"""
    return generate_register(name, desc, addr, [generate_field_icg()])

def generate_registers_icg_divcfg(name, desc, addr, mdmt):
    """Generate xml string for starfive_jh7110_syscrg """ + name + """ register"""
    return generate_register(name, desc, addr, [
        generate_field_icg(),
        generate_field_divcfg(mdmt)
    ])

def generate_registers_icg_mux_sel(name, desc, addr, field_desc):
    """Generate xml string for starfive_jh7110_syscrg """ + name + """ register"""
    return generate_register(name, desc, addr, [
        generate_field_icg(),
        generate_field_mux_sel(field_desc)
    ])

def generate_registers_dly_chain_sel(name, desc, addr):
    """Generate xml string for starfive_jh7110_syscrg """ + name + """ register"""
    return generate_register(name, desc, addr, [generate_field_dly_chain_sel()])

def generate_registers_clk_polarity(name, desc, addr):
    """Generate xml string for starfive_jh7110_syscrg """ + name + """ register"""
    return generate_register(name, desc, addr, [generate_field_clk_polarity()])

def generate_registers_rst_sel(name, desc, idx, addr):
    """Generate xml string for starfive_jh7110_syscrg """ + name + """ register"""
    return generate_register(name, desc, addr, generate_field_rst_sel(idx))

def generate_registers_rst_stat(name, desc, addr):
    """Generate xml string for starfive_jh7110_stgcrg """ + name + """ register"""
    return generate_register(name, desc, addr, generate_field_rst_stat())

def generate_registers_aon_rst_sel(name, desc, addr):
    """Generate xml string for starfive_jh7110_syscrg """ + name + """ register"""
    return generate_register(name, desc, addr, generate_field_aon_rst_sel())

def generate_interrupt(device, name, desc = ""):
    irq_map = {
        "jh7110": {
            "gmac_lpi0": 0,
            "gmac_pmt0": 1,
            "gmac_sbd0": 2,
            "gmac_sbd_tx0": 3,
            "gmac_sbd_rx0": 4,
            "rtc_hms_ms_pulse": 5,
            "rtc_hms_one_sec_pulse": 6,
            "rtc": 7,
            "wave511": 8,
            "codaj12": 9,
            "wave420l": 10,
            "noc_bus0": 11,
            "noc_bus1": 12,
            "noc_bus2": 13,
            "ddr_asp": 14,
            "ddr_cooldown": 15,
            "ddr_hightemp": 16,
            "ddr_overtemp": 17,
            "ddr_phy": 18,
            "ddr_phy_freq": 19,
            "qspi": 20,
            "mailbox0": 21,
            "mailbox1": 22,
            "sec_algc": 23,
            "sec_dmac": 24,
            "sec_trng": 25,
            "otpc": 26,
            "uart0": 27,
            "uart1": 28,
            "uart2": 29,
            "i2c0": 30,
            "i2c1": 31,
            "i2c2": 32,
            "spi0": 33,
            "spi1": 34,
            "spi2": 35,
            "reserved0": 36,
            "i2srx0": 37,
            "i2srx1": 38,
            "i2srx2": 39,
            "uart3": 40,
            "uart4": 41,
            "uart5": 42,
            "i2c3": 43,
            "i2c4": 44,
            "i2c5": 45,
            "i2c6": 46,
            "spi3": 47,
            "spi4": 48,
            "spi5": 49,
            "spi6": 50,
            "pcie0": 51,
            "pcie1": 52,
            "i2stx0": 53,
            "i2stx1": 54,
            "pwm0": 55,
            "pwm1": 56,
            "pwm2": 57,
            "pwm3": 58,
            "pwm4": 59,
            "pwm5": 60,
            "pwm6": 61,
            "pwm7": 62,
            "wdt": 63,
            "timer0": 64,
            "timer1": 65,
            "timer2": 66,
            "timer3": 67,
            "dma": 68,
            "sdio0": 69,
            "sdio1": 70,
            "sdio1": 70,
            "gmac_lpi1": 71,
            "gmac_pmt1": 72,
            "gmac_sbd1": 73,
            "gmac_sbd_tx1": 74,
            "gmac_sbd_rx1": 75,
            "temp_sensor": 76,
            "gpu_os": 77,
            "gpu_pow": 78,
            "spdif": 79,
            "aon_iomux": 80,
            "sys_iomux": 81,
            "isp0": 82,
            "isp1": 83,
            "isp2": 84,
            "isp3": 85,
            "isp_vin_axird": 86,
            "isp_vin_axiwr": 87,
            "isp_vin": 88,
            "isp_vin_err": 89,
            "vout0": 90,
            "vout1": 91,
            "vout2": 92,
            "vout3": 93,
            "vout4": 94,
            "usb0": 95,
            "usb1": 96,
            "usb2": 97,
            "usb3": 98,
            "usb4": 99,
            "usb5": 100,
            "usb6": 101,
            "usb7": 102,
            "usb_irqs0": 103,
            "usb_irqs1": 104,
            "usb_otg": 105,
            "pmu": 106,
            "can0": 107,
            "can1": 108,
            "int": 109,
            "reserved1": 110,
            "reserved2": 111,
            "reserved3": 112,
            "reserved4": 113,
            "reserved5": 114,
            "reserved6": 115,
            "reserved7": 116,
            "reserved8": 117,
            "reserved9": 118,
            "reserved10": 119,
            "reserved11": 120,
            "reserved12": 121,
            "reserved13": 122,
            "reserved14": 123,
            "reserved15": 124,
            "reserved16": 125,
            "reserved17": 126,
        }
    }


    try:
        value = str(irq_map[device][name])
    except:
        logging.debug("no IRQ map entry for device: {}, name: {}".format(device, name))
        return ""

    txt = """\
              <interrupt>
                <name>""" + name + """</name>
"""

    if len(desc) != 0:
        txt += """\
                <description>""" + desc + """</description>
"""

    txt += """\
                <value>""" + value + """</value>
              </interrupt>
"""

    return txt

def generate_register(name, desc, addr, field_name_desc_range_access, size=32, reset_value=0):
    txt = """\
                <register>
                  <name>""" + name + """</name>
                  <description>""" + desc + """</description>
                  <addressOffset>""" + "0x{:x}".format(addr) + """</addressOffset>
                  <size>""" + str(size) + """</size>
                  <resetValue>""" + str(reset_value) + """</resetValue>
                  <fields>
"""

    for (n, d, r, a) in field_name_desc_range_access:
        txt += generate_field(n, d, r, a)

    return txt + """\
                  </fields>
                </register>
"""

def generate_register_arr(name, desc, addr, dim, dim_inc, reset_value=0):
    return """\
                <register>
                  <dim>""" + str(dim) + """</dim>
                  <dimIncrement>""" + "{:#x}".format(dim_inc) + """</dimIncrement>
                  <name>""" + name + """[%s]</name>
                  <description>""" + desc + """</description>
                  <addressOffset>""" + "{:#x}".format(addr) + """</addressOffset>
                  <resetValue>""" + str(reset_value) + """</resetValue>
                </register>
"""

def generate_field(name, desc, bit_range, access):
    if len(desc) == 0:
        desc = name

    return """\
                    <field>
                      <name>""" + name + """</name>
                      <description>""" + desc + """</description>
                      <bitRange>""" + bit_range + """</bitRange>
                      <access>""" + access + """</access>
                    </field>
"""

def generate_field_mux_sel(field_desc):
    return (
        "clk_mux_sel",
        "Clock multiplexing selector: " + field_desc,
        "[29:24]",
        "read-write",
    )

def generate_field_divcfg(mdmt):
    field_desc = "Clock divider coefficient: Max={}, Default={}, Min={}, Typical={}".format(mdmt[0], mdmt[1], mdmt[2], mdmt[3])

    return ("clk_divcfg", field_desc, "[23:0]", "read-write")

def generate_field_icg():
    return ("clk_icg", "1: Clock enable, 0: Clock disable", "[31:31]", "read-write")

def generate_field_dly_chain_sel():
    desc = "Selector delay chain stage number, totally 32 stages, -50 ps each stage. The register value indicates the delay chain stage number. For example, diy_chain_sel=1 means to delay 1 stage."

    return ("dly_chain_sel", desc, "[23:0]", "read-write")

def generate_field_clk_polarity():
    return ("clk_polarity", "1: Clock inverter, 0: Clock buffer", "[30:30]", "read-write") 

def generate_field_rst_sel(idx):
    names = [
        [
            "u0_jtag2apb_presetn", "u0_sys_syscon_presetn", "u0_sys_iomux_presetn", "u0_bus",
            "u0_debug", "u0_core_0", "u0_core_1", "u0_core_2",
            "u0_core3", "u0_core4", "u0_core_st_0", "u0_core_st_1",
            "u0_core_st_2", "u0_core_st_3", "u0_core_st_4", "u0_trace_0",
            "u0_trace_1", "u0_trace_2", "u0_trace_3", "u0_trace_4",
            "u0_trace_com", "u0_img_gpu_apb", "u0_img_gpu_doma", "u0_noc_bus_apb",
            "u0_noc_bus_axicfg0", "u0_noc_bus_cpu_axi", "u0_noc_bus_disp_axi", "u0_noc_bus_gpu_axi",
            "u0_noc_bus_isp_axi", "u0_noc_bus_ddrc", "u0_noc_bus_stg_axi", "u0_noc_bus_vdec_axi",
        ],
        [
            "u0_noc_bus_venc_axi", "u0_axi_cfg1_dec_ahb", "u0_axi_cfg1_dec_main", "u0_axi_cfg0_dec_main",
            "u0_axi_cfg0_dec_main_div", "u0_axi_cfg0_dec_hifi4", "u0_ddr_axi", "u0_ddr_osc",
            "u0_ddr_apb", "u0_isp_top", "u0_isp_axi", "u0_vout_src",
            "u0_codaj12_axi", "u0_codaj12_core", "u0_codaj12_apb", "u0_wave511_axi",
            "u0_wave511_bpu", "u0_wave511_vce", "u0_wave511_apb", "u0_vdec_jpg_arb",
            "u0_vdec_jpg_arb_main", "u0_aximem_128b_axi", "u0_wave420l_axi", "u0_wave420l_bpu",
            "u0_wave420l_vce", "u0_wave420l_apb", "u1_aximem", "u2_aximem",
            "u0_intmem_rom_sram", "u0_qspi_ahb", "u0_qspi_apb", "u0_qspi_ref",
        ],
        [
            "u0_sdio_ahb", "u1_sdi_ahb", "u1_gmac5_axi64", "u1_gmac5_axi64_hresetn",
            "u0_mailbox_presetn", "u0_spi_apb", "u1_spi_apb", "u2_spi_apb",
            "u3_spi_apb", "u4_spi_apb", "u5_spi_apb", "u6_spi_apb",
            "u0_i2c_apb", "u1_i2c_apb", "u2_i2c_apb", "u3_i2c_apb",
            "u4_i2c_apb", "u5_i2c_apb", "u6_i2c_apb", "u0_uart_apb",
            "u0_uart_core", "u1_uart_apb", "u1_uart_core", "u2_uart_apb",
            "u2_uart_core", "u3_uart_apb", "u3_uart_core", "u4_uart_apb",
            "u4_uart_core", "u5_uart_apb", "u6_uart_core", "u0_spdif_apb",
        ],
        [
            "u0_pwmdac_apb", "u0_pdm_4mic_dmic", "u0_pdm_4mic_apb", "u0_i2srx_apb",
            "u0_i2srx_bclk", "u0_i2stx_apb", "u0_i2stx_bclk", "u1_i2stx_apb",
            "u1_i2stx_bclk", "u0_tdm16slot_ahb", "u0_tdm16slot_tdm", "u0_tdm16slot_apb",
            "u0_pwm_apb", "u0_dskit_wdt_rstn_apb", "u0_dskit_wdt", "u0_can_ctrl_apb",
            "u0_can_ctrl", "u0_can_ctrl_timer", "u1_can_ctrl_apb", "u1_can_ctrl_can",
            "u1_can_ctrl_timer", "u0_si5_timer_apb", "u0_si5_timer_0", "u0_si5_timer_1",
            "u0_si5_timer_2", "u0_si5_timer_3", "u0_int_ctrl_apb", "u0_temp_sensor_apb",
            "u0_temp_sensor", "u0_jtag_rst", "", "",
        ],
    ]

    desc = "1: Assert reset, 0: De-assert reset"

    return [(names[idx][i], desc, "[{}:{}]".format(i, i), "read-write") for i in range(32) if len(names[idx][i]) != 0]

def generate_field_rst_stat():
    names = [
        "u0_stg_syscon_presetn", "u0_hifi4_core", "u0_hifi4_axi", "u0_sec_top_hreesetn",
        "u0_e2_core", "u0_dma_axi", "u0_dma_ahb", "u0_usb_axi",
        "u0_usb_apb", "u0_usb_utmi_apb", "u0_usb_pwrup", "u0_pcie_axi_mst0",
        "u0_pcie_axi_slv0", "u0_pcie_axi_slv", "u0_pci_brg", "u0_pcie_pcie",
        "u0_pcie_apb", "u1_pcie_axi_mst0", "u1_pcie_axi_slv0", "u1_pcie_axi_slv",
        "u1_pcie_brg", "u1_pcie_pcie", "u1_pcie_apb",
    ]

    desc = "1: Assert reset, 0: De-assert reset"

    return [(names[i], desc, "[{}:{}]".format(i, i), "read-write") for i in range(23)]

def generate_field_aon_rst_sel():
    names = [
            "gmac5_axi64_axi", "gmac5_axi64_ahb", "aon_iomux_presetn", "pmu_apb",
            "pmu_wkup", "rtc_hms_apb", "rtc_hms_cal", "rtc_hms_osc32k",
    ]

    desc = "1: Assert reset, 0: De-assert reset"

    return [(names[i], desc, "[{}:{}]".format(i, i), "read-write") for i in range(8)]

def generate_fields_list_sram_config(name, base):
    return [
        ("{}_slp".format(name), "SRAM/ROM configuration. SLP: sleep enable, high active, default is low.", "[{}:{}]".format(base, base), "read-write"),
        ("{}_sd".format(name), "SRAM/ROM configuration. SD: shutdown enable, high active, default is low.", "[{}:{}]".format(base + 1, base + 1), "read-write"),
        ("{}_rtsel".format(name), "SRAM/ROM configuration. RTSEL: timing setting for debug purpose, default is 2'b01.", "[{}:{}]".format(base + 3, base + 2), "read-write"),
        ("{}_ptsel".format(name), "SRAM/ROM configuration. PTSEL: timing setting for debug purpose, default is 2'b01.", "[{}:{}]".format(base + 5, base + 4), "read-write"),
        ("{}_trb".format(name), "SRAM/ROM configuration. TRB: timing setting for debug purpose, default is 2'b01.", "[{}:{}]".format(base + 7, base + 6), "read-write"),
        ("{}_wtsel".format(name), "SRAM/ROM configuration. WTSEL: timing setting for debug purpose, default is 2'b01.", "[{}:{}]".format(base + 9, base + 8), "read-write"),
        ("{}_vs".format(name), "SRAM/ROM configuration. VS: timing setting for debug purpose, default is 1'b1.", "[{}:{}]".format(base + 10, base + 10), "read-write"),
        ("{}_vg".format(name), "SRAM/ROM configuration. VG: timing setting for debug purpose, default is 1'b1.", "[{}:{}]".format(base + 11, base + 11), "read-write")
    ]
