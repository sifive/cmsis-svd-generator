#!/usr/bin/env python3
# Copyleft (c) 2023 cmsis-svd-generator developers
# SPDX-License-Identifier: Apache-2.0

from scripts.starfive_common import *

"""
This program generates CMSIS SVD xml for cadence QSPI
"""

def generate_registers_cdns_qspi(dts, peripheral):
    """Generate xml string for registers for cadence_qspi peripheral"""
    txt = """\
              <registers>
"""
    txt += generate_register("config", "Cadence QSPI Configuration", 0x00, [
        ("enable", "Enable the QSPI controller", "[0:0]", "read-write"),
        ("enb_dir_acc_ctrl", "Enable direct access controller", "[7:7]", "read-write"),
        ("decode", "Enable the QSPI decoder", "[9:9]", "read-write"),
        ("chipselect", "Chip select - CS0: 0b1110, CS1: 0b1101, CS2: 0b1011, CS3: 0b0111", "[13:10]", "read-write"),
        ("dma", "Enable Direct Memory Access", "[15:15]", "read-write"),
        ("baud", "Set the QSPI BAUD rate divisor", "[22:19]", "read-write"),
        ("dtr_proto", "Enable DTR Protocol", "[24:24]", "read-write"),
        ("dual_opcode", "Enable Dual Opcode Mode", "[30:30]", "read-write"),
        ("idle", "Set Idle", "[31:31]", "read-write"),
    ])

    txt += generate_register("rd_instr", "Cadence QSPI Read Instruction", 0x04, [
        ("opcode", "Instruction Opcode", "[7:0]", "read-write"),
        ("type_instr", "Type of Instruction", "[9:8]", "read-write"),
        ("type_addr", "Type of Address", "[13:12]", "read-write"),
        ("type_data", "", "[17:16]", "read-write"),
        ("mode_en", "Mode ", "[20:20]", "read-write"),
        ("dummy", "Send dummy signal to stall the device", "[28:24]", "read-write"),
    ])

    txt += generate_register("wr_instr", "Cadence QSPI Write Instruction", 0x08, [
        ("opcode", "Instruction Opcode", "[7:0]", "read-write"),
        ("type_addr", "Type of Address", "[13:12]", "read-write"),
        ("type_data", "", "[17:16]", "read-write"),
    ])

    txt += generate_register("delay", "Cadence QSPI Delay", 0x0c, [
        ("tslch", "TSLCH Delay Value", "[7:0]", "read-write"),
        ("tchsh", "TCHSH Delay Value", "[15:8]", "read-write"),
        ("tsd2d", "TSD2D Delay Value", "[23:16]", "read-write"),
        ("tshsl", "TSHSL Delay Value", "[31:24]", "read-write"),
    ])

    txt += generate_register("read_capture", "Cadence QSPI Read Capture", 0x10, [
        ("bypass", "Bypass the Read Capture", "[0:0]", "read-write"),
        ("delay", "Read Capture Delay Value", "[4:1]", "read-write"),
    ])

    txt += generate_register("size", "Cadence QSPI Size Configuration", 0x14, [
        ("address", "Address Size in Bytes", "[3:0]", "read-write"),
        ("page", "Page Size in Bytes", "[15:4]", "read-write"),
        ("block", "Block Size in Bytes", "[21:16]", "read-write"),
    ])

    txt += generate_register("sram_partition", "Cadence QSPI SRAM Partition Size", 0x18, [
        ("size", "Partition size in bytes", "[31:0]", "read-write"),
    ])

    txt += generate_register("indirect_trigger", "Cadence QSPI Indirect Trigger Address", 0x1c, [
        ("address", "", "[31:0]", "read-write"),
    ])

    txt += generate_register("dma", "Cadence QSPI Direct Memory Access", 0x20, [
        ("single", "", "[7:0]", "read-write"),
        ("burst", "", "[15:8]", "read-write"),
    ])

    txt += generate_register("remap", "Cadence QSPI Remap Address", 0x24, [
        ("address", "", "[31:0]", "read-write"),
    ])

    txt += generate_register("mode_bit", "Cadence QSPI Mode Bit(s)", 0x28, [
        ("mode", "", "[31:0]", "read-write"),
    ])

    txt += generate_register("sdram_level", "Cadence QSPI SDRAM Level", 0x2c, [
        ("rd", "SDRAM Read Level", "[15:0]", "read-only"),
        ("wr", "SDRAM Write Level", "[31:16]", "read-only"),
    ])

    txt += generate_register("wr_completion_ctrl", "Cadence QSPI Write Completion Control", 0x38, [
        # FIXME: fill out the remaining control fields. This is the only field in the Linux driver.
        ("disable_auto_poll", "SPI NAND flashes require the address of the status register to be passed in the Read SR command. Also, some SPI NOR flashes like the Cypress Semper flash expect a 4-byte dummy address in the Read SR command in DTR mode. But this controller does not support address phase in the Read SR command when doing auto-HW polling. So, disable write completion polling on the controller's side. spi-nand and spi-nor will take care of polling the status register.", "[14:14]", "read-write"),
    ])

    txt += generate_register("irq_status", "Cadence QSPI IRQ Status", 0x40, [
        ("mode_err", "Mode error interrupt", "[0:0]", "read-write"),
        ("underflow", "Buffer underflow interrupt", "[1:1]", "read-write"),
        ("ind_comp", "Indirect computation interrupt", "[2:2]", "read-write"),
        ("ind_rd_reject", "Indirect read rejection interrupt", "[3:3]", "read-write"),
        ("wr_protected_err", "Write protected error interrupt", "[4:4]", "read-write"),
        ("illegal_ahb_err", "Illegal AHB clock error interrupt", "[5:5]", "read-write"),
        ("watermark", "Watermark interrupt", "[6:6]", "read-write"),
        ("ind_sram_full", "Indirect SRAM full interrupt", "[12:12]", "read-write"),
    # Reset value: (0b1_1111_1111_1111)
    ], 32, 0x1ffff)

    txt += generate_register("irq_mask", "Cadence QSPI IRQ Mask", 0x44, [
        ("mode_err", "Mode error interrupt", "[0:0]", "read-write"),
        ("underflow", "Buffer underflow interrupt", "[1:1]", "read-write"),
        ("ind_comp", "Indirect computation interrupt", "[2:2]", "read-write"),
        ("ind_rd_reject", "Indirect read rejection interrupt", "[3:3]", "read-write"),
        ("wr_protected_err", "Write protected error interrupt", "[4:4]", "read-write"),
        ("illegal_ahb_err", "Illegal AHB clock error interrupt", "[5:5]", "read-write"),
        ("watermark", "Watermark interrupt", "[6:6]", "read-write"),
        ("ind_sram_full", "Indirect SRAM full interrupt", "[12:12]", "read-write"),
    # Reset value: (IND_COMP | WATERMARK | UNDERFLOW)
    ], 32, 0x46)

    txt += generate_register("indirect_rd", "Cadence QSPI Indirect Read", 0x60, [
        ("start", "Start indirect read", "[0:0]", "read-write"),
        ("cancel", "Cancel indirect read", "[1:1]", "read-write"),
        ("done", "Indirect read done", "[5:5]", "read-write"),
    ])

    txt += generate_register("indirect_rd_watermark", "Cadence QSPI Indirect Read Watermark", 0x64, [
        ("watermark", "", "[31:0]", "read-write"),
    ])

    txt += generate_register("indirect_rd_start_addr", "Cadence QSPI Indirect Read Start Address", 0x68, [
        ("address", "", "[31:0]", "read-write"),
    ])

    txt += generate_register("indirect_rd_bytes", "Cadence QSPI Indirect Read Bytes", 0x6c, [
        ("bytes", "", "[31:0]", "read-write"),
    ])

    txt += generate_register("indirect_wr", "Cadence QSPI Indirect Write", 0x70, [
        ("start", "Start indirect write", "[0:0]", "read-write"),
        ("cancel", "Cancel indirect write", "[1:1]", "read-write"),
        ("done", "Indirect write done", "[5:5]", "read-write"),
    ])

    txt += generate_register("indirect_wr_watermark", "Cadence QSPI Indirect Write Watermark", 0x74, [
        ("watermark", "", "[31:0]", "read-write"),
    ])

    txt += generate_register("indirect_wr_start_addr", "Cadence QSPI Indirect Write Start Address", 0x78, [
        ("address", "", "[31:0]", "read-write"),
    ])

    txt += generate_register("indirect_wr_bytes", "Cadence QSPI Indirect Write Bytes", 0x7c, [
        ("bytes", "", "[31:0]", "read-write"),
    ])

    txt += generate_register("cmd_ctrl", "Cadence QSPI Command Control", 0x90, [
        ("execute", "Execute-in-Place (XIP)", "[0:0]", "read-write"),
        ("in_progress", "Command in progress", "[1:1]", "read-write"),
        ("dummy", "Dummy command", "[11:7]", "read-write"),
        ("wr_bytes", "Write bytes", "[14:12]", "read-write"),
        ("wr_en", "Write enable", "[15:15]", "read-write"),
        ("add_bytes", "Add command bytes", "[17:16]", "read-write"),
        ("addr_en", "Address enable", "[19:19]", "read-write"),
        ("rd_bytes", "Read bytes", "[22:20]", "read-write"),
        ("rd_en", "Read enable", "[23:23]", "read-write"),
        ("opcode", "Command opcode", "[31:24]", "read-write"),
    ])

    txt += generate_register("cmd_address", "Cadence QSPI Command Address", 0x94, [
        ("address", "", "[31:0]", "read-write"),
    ])

    txt += generate_register("cmd_read_at_lower", "Cadence QSPI Command Read at Lower", 0xa0, [
        ("read_at_lower", "", "[31:0]", "read-write"),
    ])

    txt += generate_register("cmd_read_at_upper", "Cadence QSPI Command Read at Upper", 0xa4, [
        ("read_at_upper", "", "[31:0]", "read-write"),
    ])

    txt += generate_register("cmd_write_at_lower", "Cadence QSPI Command Write at Lower", 0xa8, [
        ("write_at_lower", "", "[31:0]", "read-write"),
    ])

    txt += generate_register("cmd_write_at_upper", "Cadence QSPI Command Write at Upper", 0xac, [
        ("write_at_upper", "", "[31:0]", "read-write"),
    ])

    txt += generate_register("polling_status", "Cadence QSPI Polling Status", 0xb0, [
        ("status", "", "[15:0]", "read-write"),
        ("dummy", "", "[20:16]", "read-write"),
    ])

    txt += generate_register("ext_lower", "Cadence QSPI Extension Lower", 0xe0, [
        ("stig", "", "[15:0]", "read-write"),
        ("write", "", "[23:16]", "read-write"),
        ("read", "", "[31:24]", "read-write"),
    ])

    return txt + """\
              </registers>
"""
