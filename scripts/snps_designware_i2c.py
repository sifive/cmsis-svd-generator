#!/usr/bin/env python3
# Copyleft (c) 2023 cmsis-svd-generator developers
# SPDX-License-Identifier: Apache-2.0

from scripts.starfive_common import *

"""
This program generates CMSIS SVD xml for designware I2C
"""

def generate_registers_snps_designware_i2c(dts, peripheral):
    """Generate xml string for registers for designware_i2c peripheral"""
    txt = """\
              <registers>
"""

    txt += generate_register("con", "DesignWare I2C CON", 0x00, [
        ("master", "I2C Master Connection - 0: Slave, 1: Master", "[0:0]", "read-write"),
        ("speed", "I2C Speed - 01: Standard, 10: Fast, 11: High", "[2:1]", "read-write"),
        ("slave_10bitaddr", "I2C Slave 10-bit Address - 0: False, 1: True", "[3:3]", "read-write"),
        ("master_10bitaddr", "I2C Master 10-bit Address - 0: False, 1: True", "[4:4]", "read-write"),
        ("restart_en", "I2C Restart Enable - 0: False, 1: True", "[5:5]", "read-write"),
        ("slave_disable", "I2C Slave Disable - 0: False, 1: True", "[6:6]", "read-write"),
        ("stop_det_ifaddressed", "I2C Stop DET If Addressed - 0: False, 1: True", "[7:7]", "read-write"),
        ("tx_empty_ctrl", "I2C TX Empty Control - 0: False, 1: True", "[8:8]", "read-write"),
        ("rx_fifo_full_hld_ctrl", "I2C RX FIFO Full Hold Control - 0: False, 1: True", "[9:9]", "read-write"),
        ("bus_clear_ctrl", "I2C Bus Clear Control - 0: False, 1: True", "[11:11]", "read-write"),
    ])
    txt += generate_register("tar", "DesignWare I2C TAR", 0x04, [
        ("address_7bit", "Target address, 7-bit mode", "[6:0]", "read-write"),
        ("address_10bit", "Target address, 10-bit mode", "[9:0]", "read-write"),
        ("mode", "Target addressing mode - 0: 7-bit, 1: 10-bit", "[12:12]", "read-write")
    ])
    txt += generate_register("sar", "DesignWare I2C SAR", 0x08, [
        ("address_7bit", "Slave address, 7-bit mode", "[6:0]", "read-write"),
        ("address_10bit", "Slave address, 10-bit mode", "[9:0]", "read-write"),
    ])
    txt += generate_register("data_cmd", "DesignWare I2C Data Command", 0x10, [
        ("dat", "Data Command Data Byte", "[7:0]", "read-write"),
        ("read", "Data Command READ Bit - 0: Write, 1: Read", "[8:8]", "read-write"),
        ("stop", "Data Command STOP Bit - 0: Non-terminal DATA command byte, 1: Terminal DATA command byte", "[9:9]", "read-write"),
        ("restart", "Data Command RESTART Bit - 0: Do not restart the transfer, 1: Restart the transfer", "[10:10]", "read-write"),
        ("first_data_byte", "Data Command First Data Byte - 0: False, 1: True", "[11:11]", "read-write"),
    ])
    txt += generate_register("ss_scl_hcnt", "DesignWare I2C SS SCL HCNT", 0x14, [
        ("ss_scl_hcnt", "", "[31:0]", "read-write")
    ])
    txt += generate_register("ss_scl_lcnt", "DesignWare I2C SS SCL LCNT", 0x18, [
        ("ss_scl_lcnt", "", "[31:0]", "read-write")
    ])
    txt += generate_register("fs_scl_hcnt", "DesignWare I2C FS SCL HCNT", 0x1c, [
        ("fs_scl_hcnt", "", "[31:0]", "read-write")
    ])
    txt += generate_register("fs_scl_lcnt", "DesignWare I2C FS SCL LCNT", 0x20, [
        ("fs_scl_lcnt", "", "[31:0]", "read-write")
    ])
    txt += generate_register("hs_scl_hcnt", "DesignWare I2C HS SCL HCNT", 0x24, [
        ("hs_scl_hcnt", "", "[31:0]", "read-write")
    ])
    txt += generate_register("hs_scl_lcnt", "DesignWare I2C HS SCL LCNT", 0x28, [
        ("hs_scl_lcnt", "", "[31:0]", "read-write")
    ])
    txt += generate_register("intr_stat", "DesignWare I2C Interrupt Status", 0x2c, generate_intr_fields("read-only"))
    txt += generate_register("intr_mask", "DesignWare I2C Interrupt Mask", 0x30, generate_intr_fields("read-write"))
    txt += generate_register("raw_intr_stat", "DesignWare I2C Raw Interrupt Status", 0x34, generate_intr_fields("read-only"))
    txt += generate_register("rx_tl", "DesignWare I2C RX TL", 0x38, [
        ("rx_tl", "", "[31:0]", "read-write")
    ])
    txt += generate_register("tx_tl", "DesignWare I2C TX TL", 0x3c, [
        ("tx_tl", "", "[31:0]", "read-write")
    ])
    txt += generate_register("clr_intr", "DesignWare I2C Clear Interrrupt", 0x40, generate_intr_fields("read-write"))
    txt += generate_register("clr_rx_under", "DesignWare I2C Clear RX Underrun", 0x44, [("clr_rx_under", "", "[31:0]", "read-write")])
    txt += generate_register("clr_rx_over", "DesignWare I2C Clear RX Overrun", 0x48, [
        ("clr_rx_over", "", "[31:0]", "read-write")
    ])
    txt += generate_register("clr_tx_over", "DesignWare I2C Clear TX Overrun", 0x4c, [
        ("clr_tx_over", "", "[31:0]", "read-write")
    ])
    txt += generate_register("clr_rd_req", "DesignWare I2C Clear Read Request", 0x50, [
        ("clr_rd_req", "", "[31:0]", "read-write")
    ])
    txt += generate_register("clr_tx_abrt", "DesignWare I2C Clear TX Abort", 0x54, [
        ("clr_tx_abrt", "", "[31:0]", "read-write")
    ])
    txt += generate_register("clr_rx_done", "DesignWare I2C Clear RX Done", 0x58, [
        ("clr_rx_done", "", "[31:0]", "read-write")
    ])
    txt += generate_register("clr_activity", "DesignWare I2C Clear Activity", 0x5c, [
        ("clr_activity", "", "[31:0]", "read-write")
    ])
    txt += generate_register("clr_stop_det", "DesignWare I2C Clear Stop DET", 0x60, [
        ("clr_stop_det", "", "[31:0]", "read-write")
    ])
    txt += generate_register("clr_start_det", "DesignWare I2C Clear Start DET", 0x64, [
        ("clr_start_det", "", "[31:0]", "read-write")
    ])
    txt += generate_register("clr_gen_call", "DesignWare I2C Clear General Call", 0x68, [
        ("clr_gen_call", "", "[31:0]", "read-write")
    ])
    txt += generate_register("enable", "DesignWare I2C Enable", 0x6c, [
        ("abort", "", "[1:1]", "read-write")
    ])
    txt += generate_register("status", "DesignWare I2C Status", 0x70, [
        ("activity", "", "[0:0]", "read-only"),
        ("tfe", "", "[2:2]", "read-only"),
        ("rfne", "", "[3:3]", "read-only"),
        ("master_activity", "", "[5:5]", "read-only"),
        ("slave_activity", "", "[6:6]", "read-only")
    ])
    txt += generate_register("txflr", "DesignWare I2C TX Failure", 0x74, [
        ("txflr", "", "[31:0]", "read-write")
    ])
    txt += generate_register("rxflr", "DesignWare I2C RX Failure", 0x78, [
        ("rxflr", "", "[31:0]", "read-write")
    ])
    txt += generate_register("sda_hold", "DesignWare I2C SDA Hold", 0x7c, [
        ("sda_hold", "", "[31:0]", "read-write")
    ])
    # From linux i2c-designware-core: only expected abort codes are listed here
    # Refer to the datasheet for the full list
    txt += generate_register("tx_abrt_source", "DesignWare I2C TX Abort Source", 0x80, [
        ("b7_addr_noack", "", "[0:0]", "read-only"),
        ("b10_addr1_noack", "", "[1:1]", "read-only"),
        ("b10_addr2_noack", "", "[2:2]", "read-only"),
        ("txdata_noack", "", "[3:3]", "read-only"),
        ("gcall_noack", "", "[4:4]", "read-only"),
        ("gcall_read", "", "[5:5]", "read-only"),
        ("sbyte_ackdet", "", "[7:7]", "read-only"),
        ("sbyte_norstrt", "", "[9:9]", "read-only"),
        ("b10_rd_norstrt", "", "[10:10]", "read-only"),
        ("master_dis", "", "[11:11]", "read-only"),
        ("arb_lost", "", "[12:12]", "read-only"),
        ("slave_flush_txfifo", "", "[13:13]", "read-only"),
        ("slave_arblost", "", "[14:14]", "read-only"),
        ("slave_rd_intx", "", "[15:15]", "read-only")
    ])
    txt += generate_register("enable_status", "DesignWare I2C Enable Status", 0x9c, [
        ("activity", "", "[0:0]", "read-write"),
        ("tfe", "", "[2:2]", "read-write"),
        ("rfne", "", "[3:3]", "read-write"),
        ("master_activity", "", "[5:5]", "read-write"),
        ("slave_activity", "", "[6:6]", "read-write")
    ])
    txt += generate_register("clr_restart_det", "DesignWare I2C Clear Restart DET", 0xa8, [
        ("clr_restart_det", "", "[31:0]", "read-write")
    ])
    txt += generate_register("comp_param_1", "DesignWare I2C Compatibility Parameter 1", 0xf4, [
        ("speed", "Speed mask - 01: Standard, 10: Full, 11: High", "[3:2]", "read-only")
    ])
    # Hold MIN Version: eg. 0x3131312a ( "111*" == v1.11* )
    txt += generate_register("comp_version", "DesignWare I2C Compatibility Version", 0xf8, [
        ("comp_version", "", "[31:0]", "read-only")
    ])
    # I2C Type: 0x44570140 ( "DW" + 0x0140 )
    txt += generate_register("comp_type", "DesignWare I2C Compatibility Type", 0xfc, [
        ("comp_type", "", "[31:0]", "read-only")
    ])

    return txt + """\
              </registers>
"""

def generate_intr_fields(access):
    return [
        ("rx_under", "RX FIFO Underrun", "[0:0]", access),
        ("rx_over", "RX FIFO Overrun", "[1:1]", access),
        ("rx_full", "RX FIFO Full", "[2:2]", access),
        ("tx_over", "TX FIFO Overrun", "[3:3]", access),
        ("tx_empty", "TX FIFO Empty", "[4:4]", access),
        ("rd_req", "Read Request", "[5:5]", access),
        ("tx_abrt", "TX Abort", "[6:6]", access),
        ("rx_done", "RX Done", "[7:7]", access),
        ("activity", "Activity", "[8:8]", access),
        ("stop_det", "Stop DET", "[9:9]", access),
        ("start_det", "Start DET", "[10:10]", access),
        ("gen_call", "General Call", "[11:11]", access),
        ("restart_det", "Restart DET", "[12:12]", access),
        ("mst_on_hold", "Master on Hold", "[13:13]", access)
    ]
