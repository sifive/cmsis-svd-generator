#!/usr/bin/env python3
# Copyleft (c) 2023 cmsis-svd-generator developers
# SPDX-License-Identifier: Apache-2.0

from scripts.starfive_common import *

"""
This program generates CMSIS SVD xml for arm PL022 (SPI) 
"""

def generate_registers_arm_pl022(dts, peripheral):
    """Generate xml string for registers for arm_pl022 peripheral"""
    txt = """\
              <registers>
"""

    txt += generate_register_ssp_cr0()
    txt += generate_register_ssp_cr1()
    txt += generate_register_ssp_dr()
    txt += generate_register_ssp_sr()
    txt += generate_register_ssp_cpsr()
    txt += generate_register_ssp_imsc()
    txt += generate_register_ssp_ris()
    txt += generate_register_ssp_mis()
    txt += generate_register_ssp_icr()
    txt += generate_register_ssp_dmacr()
    txt += generate_register_ssp_periph_id0()
    txt += generate_register_ssp_periph_id1()
    txt += generate_register_ssp_periph_id2()
    txt += generate_register_ssp_periph_id3()

    for i in range(4):
        txt += generate_register_ssp_pcell_id(i)

    return txt + """\
              </registers>
"""

def generate_register_ssp_cr0():
    return generate_register(
        "ssp_cr0",
        "SSPCR0 is control register 0 and contains five bit fields that control various functions within the PrimeCell SSP.",
        0x00,
        [
            (
                "dss",
                "Data Size Select - 0000, 0001, 0010: Reserved, 0011: 4-bit data, 0100: 5-bit data, 6-bit data, 0110: 7-bit data, 0111: 8-bit data, 1000: 9-bit data, 1001: 10-bit data, 1010: 11-bit data, 1011: 12-bit data, 1100: 13-bit data, 1101: 14-bit data, 1110: 15-bit data, 1111: 16-bit data",
                "[3:0]",
                "read-write"
            ),
            (
                "frf",
                "Frame format - 00: Motorola SPI frame format, 01: TI synchronous serial frame format, 10: National Microwire frame format, 11: Reserved",
                "[5:4]",
                "read-write"
            ),
            (
                "spo",
                "SSPCLKOUT polarity, applicable to Motorola SPI frame format only.",
                "[6:6]",
                "read-write"
            ),
            (
                "sph",
                "SSPCLKOUT phase, applicable to Motorola SPI frame format only.",
                "[6:6]",
                "read-write"
            ),
            (
                "scr",
                "Serial clock rate. The value SCR is used to generate the transmit and receive bit rate of the PrimeCell SSP. The bit rate is: (F[sspclk] / (CPSDVR * (1 + SCR))), where CPSDVSR is an even value from [2:254], programmed through the SSPCPSR register and SCR is a value from [0:255]",
                "[15:8]",
                "read-write"
            )
        ],
        16
    )

def generate_register_ssp_cr1():
    return generate_register(
        "ssp_cr1",
        "SSPCR1 is the control register 1 and contains four different bit fields, that control various functions within the PrimeCell SSP.",
        0x04,
        [
            (
                "lbm",
                "Loop back mode - 0: Normal serial port operation enabled, 1: Output of transmit serial shifter is connected to input of receive serial shifter internally",
                "[0:0]",
                "read-write"
            ),
            (
                "sse",
                "Synchronous serial port enable - 0: SSP operation disabled, 1: SSP operation enabled",
                "[1:1]",
                "read-write"
            ),
            (
                "ms",
                "Master or slave mode select. This bit can be modified only when the PrimeCell SSP is disabled, SSE=0 - 0: Device configured as master (default), 1: Device configured as slave",
                "[2:2]",
                "read-write"
            ),
            (
                "sod",
                "Slave-mode output disable. This bit is relevant only in the slave mode, MS=1. In multiple-slave systems, it is possible for an PrimeCell SSP master to broadcast a message to all slaves in the system while ensuring that only one slave drives data onto its serial output line. In such systems the RXD lines from multiple slaves could be tied together. To operate in such systems, the SOD bit can be set if the PrimeCell SSP slave is not supposed to drive the SSPTXD line - 0: SSP can drive the SSPTXD output in slave mode, 1: SSP must not drive the SSPTXD output in slave mode",
                "[3:3]",
                "read-write"
            )
        ],
        16
    )

def generate_register_ssp_dr():
    return generate_register(
        "ssp_dr",
        "SSPDR is the data register and is 16-bits wide. When SSPDR is read, the entry in the receive FIFO, pointed to by the current FIFO read pointer, is accessed. As data values are removed by the PrimeCell SSP receive logic from the incoming data frame, they are placed into the entry in the receive FIFO, pointed to by the current FIFO write pointer. When SSPDR is written to, the entry in the transmit FIFO, pointed to by the write pointer, is written to. Data values are removed from the transmit FIFO one value at a time by the transmit logic. It is loaded into the transmit serial shifter, then serially shifted out onto the SSPTXD pin at the programmed bit rate. When a data size of less than 16 bits is selected, the user must right-justify data written to the transmit FIFO. The transmit logic ignores the unused bits. Received data less than 16 bits is automatically right-justified in the receive buffer.",
        0x08,
        [
            (
                "data",
                "Transmit/Receive FIFO - Read: Receive FIFO, Write: Transmit FIFO. You must right-justify data when the PrimeCell SSP is programmed for a data size that is less than 16 bits. Unused bits at the top are ignored by transmit logic. The receive logic automatically right-justifies.",
                "[15:0]",
                "read-write"
            )
        ],
        16
    )

def generate_register_ssp_sr():
    return generate_register(
        "ssp_sr",
        "SSPSR is a RO status register that contains bits that indicate the FIFO fill status and the PrimeCell SSP busy status.",
        0x0c,
        [
            (
                "tfe",
                "Transmit FIFO empty, RO - 0: Transmit FIFO is not empty, 1: Transmit FIFO is empty.",
                "[0:0]",
                "read-only"
            ),
            (
                "tnf",
                "Transmit FIFO not full, RO - 0: Transmit FIFO is full, 1: Transmit FIFO is not full.",
                "[1:1]",
                "read-only"
            ),
            (
                "rne",
                "Receive FIFO not empty, RO - 0: Receive FIFO is empty, 1: Receive FIFO is not empty.",
                "[2:2]",
                "read-only"
            ),
            (
                "rff",
                "Receive FIFO full, RO - 0: Receive FIFO is not full, 1: Receive FIFO is full.",
                "[3:3]",
                "read-only"
            ),
            (
                "bsy",
                "PrimeCell SSP busy flag, RO - 0: SSP is idle, 1: SSP is currently transmitting and/or receiving a frame or the transmit FIFO is not empty.",
                "[4:4]",
                "read-only"
            )
        ],
        16
    )

def generate_register_ssp_cpsr():
    return generate_register(
        "ssp_cpsr",
        "SSPCPSR is the clock prescale register and specifies the division factor by which the input SSPCLK must be internally divided before further use. The value programmed into this register must be an even number between [2:254]. The least significant bit of the programmed number is hard-coded to zero. If an odd number is written to this register, data read back from this register has the least significant bit as zero.",
        0x10,
        [
            (
                "cpsdvsr",
                "Clock prescale divisor. Must be an even number from 2-254, depending on the frequency of SSPCLK. The least significant bit always returns zero on reads.",
                "[7:0]",
                "read-write"
            )
        ],
        16
    )

def generate_register_ssp_imsc():
    return generate_register(
        "ssp_imsc",
        "The SSPIMSC register is the interrupt mask set or clear register. It is a RW register. On a read this register gives the current value of the mask on the relevant interrupt. A write of 1 to the particular bit sets the mask, enabling the interrupt to be read. A write of 0 clears the corresponding mask. All the bits are cleared to 0 when reset.",
        0x14,
        [
            (
                "rorim",
                "Receive overrun interrupt mask - 0: Receive FIFO written to while full condition interrupt is masked, 1: Receive FIFO written to while full condition interrupt is not masked",
                "[0:0]",
                "read-write"
            ),
            (
                "rtim",
                "Receive timeout interrupt mask - 0: Receive FIFO not empty and no read prior to timeout period interrupt is masked, 1: Receive FIFO not empty and no read prior to timeout period interrupt is not masked",
                "[1:1]",
                "read-write"
            ),
            (
                "rxim",
                "Receive FIFO interrupt mask - 0: Receive FIFO half full or less condition interrupt is masked, 1: Receive FIFO half full or less condition interrupt is not masked",
                "[2:2]",
                "read-write"
            ),
            (
                "txim",
                "Transmit FIFO interrupt mask - 0: Transmit FIFO half empty or less condition interrupt is masked, 1: Transmit FIFO half empty or less condition interrupt is not masked",
                "[2:2]",
                "read-write"
            )
        ],
        16
    )

def generate_register_ssp_ris():
    return generate_register(
        "ssp_ris",
        "The SSPRIS register is the raw interrupt status register. It is a RO register. On a read this register gives the current raw status value of the corresponding interrupt prior to masking. A write has no effect.",
        0x18,
        [
            (
                "rorris",
                "Gives the raw interrupt state, prior to masking, of the SSPRORINTR interrupt",
                "[0:0]",
                "read-only"
            ),
            (
                "rtris",
                "Gives the raw interrupt state, prior to masking, of the SSPRTINTR interrupt",
                "[1:1]",
                "read-only"
            ),
            (
                "rxris",
                "Gives the raw interrupt state, prior to masking, of the SSPRXINTR interrupt",
                "[2:2]",
                "read-only"
            ),
            (
                "txris",
                "Gives the raw interrupt state, prior to masking, of the SSPTXINTR interrupt",
                "[3:3]",
                "read-only"
            )
        ],
        16
    )

def generate_register_ssp_mis():
    return generate_register(
        "ssp_mis",
        "The SSPMIS register is the masked interrupt status register. It is a RO register. On a read this register gives the current masked status value of the corresponding interrupt. A write has no effect.",
        0x1c,
        [
            (
                "rormis",
                "Gives the receive over run masked interrupt status, after masking, of the SSPRORINTR interrupt",
                "[0:0]",
                "read-only"
            ),
            (
                "rtmis",
                "Gives the receive timeout masked interrupt state, after masking, of the SSPRTINTR interrupt",
                "[1:1]",
                "read-only"
            ),
            (
                "rxmis",
                "Gives the receive FIFO masked interrupt state, after masking, of the SSPRXINTR interrupt",
                "[2:2]",
                "read-only"
            ),
            (
                "txmis",
                "Gives the transmit FIFO masked interrupt state, after masking, of the SSPTXINTR interrupt",
                "[3:3]",
                "read-only"
            )
        ],
        16
    )

def generate_register_ssp_icr():
    return generate_register(
        "ssp_icr",
        "The SSPICR register is the interrupt clear register and is write-only. On a write of 1, the corresponding interrupt is cleared. A write of 0 has no effect.",
        0x20,
        [
            (
                "roric",
                "Clears the SSPRORINTR interrupt",
                "[0:0]",
                "read-write"
            ),
            (
                "rtic",
                "Clears the SSPRTINTR interrupt",
                "[1:1]",
                "read-write"
            )
        ],
        16
    )

def generate_register_ssp_dmacr():
    return generate_register(
        "ssp_dmacr",
        "The SSPDMACR register is the DMA control register. It is a RW register. All the bits are cleared to 0 on reset.",
        0x24,
        [
            (
                "rxdmae",
                "Receive DMA Enable. If this bit is set to 1, DMA for the receive FIFO is enabled.",
                "[0:0]",
                "read-write"
            ),
            (
                "txdmae",
                "Transmit DMA Enable. If this bit is set to 1, DMA for the transmit FIFO is enabled.",
                "[1:1]",
                "read-write"
            )
        ],
        16
    )

def generate_register_ssp_periph_id0():
    return generate_register(
        "ssp_periph_id0",
        "The SSPPeriphID0 register is hard-coded and the fields within the register determine reset value. The SSPPeriphID0-3 registers are four 8-bit registers, that span address locations 0xFE0 to 0xFEC. The registers can conceptually be treated as a single 32-bit register.",
        0xfe0,
        [
            (
                "part_number0",
                "These bits read back as 0x22",
                "[7:0]",
                "read-only"
            )
        ],
        16
    )

def generate_register_ssp_periph_id1():
    return generate_register(
        "ssp_periph_id1",
        "The SSPPeriphID1 register is hard-coded and the fields within the register determine reset value. The SSPPeriphID0-3 registers are four 8-bit registers, that span address locations 0xFE0 to 0xFEC. The registers can conceptually be treated as a single 32-bit register.",
        0xfe4,
        [
            (
                "part_number1",
                "These bits read back as 0x0",
                "[3:0]",
                "read-only"
            ),
            (
                "designer0",
                "These bits read back as 0x1",
                "[7:4]",
                "read-only"
            )
        ],
        16
    )

def generate_register_ssp_periph_id2():
    return generate_register(
        "ssp_periph_id2",
        "The SSPPeriphID2 register is hard-coded and the fields within the register determine reset value. The SSPPeriphID0-3 registers are four 8-bit registers, that span address locations 0xFE0 to 0xFEC. The registers can conceptually be treated as a single 32-bit register.",
        0xfe8,
        [
            (
                "designer1",
                "These bits read back as 0x4",
                "[3:0]",
                "read-only"
            ),
            (
                "revision",
                "These bits return the peripheral revision",
                "[7:4]",
                "read-only"
            )
        ],
        16
    )

def generate_register_ssp_periph_id3():
    return generate_register(
        "ssp_periph_id3",
        "The SSPPeriphID3 register is hard-coded and the fields within the register determine reset value. The SSPPeriphID0-3 registers are four 8-bit registers, that span address locations 0xFE0 to 0xFEC. The registers can conceptually be treated as a single 32-bit register.",
        0xfec,
        [
            (
                "configuration",
                "These bits read back as 0x80",
                "[7:0]",
                "read-only"
            )
        ],
        16
    )

def generate_register_ssp_pcell_id(num):
    magic = [0x0d, 0xf0, 0x05, 0xb1]

    return generate_register(
        "ssp_pcell_id{}".format(num),
        "The SSPPCellID0-3 registers are four 8-bit wide registers, that span address locations 0xFF0-0xFFC. The registers can conceptually be treated as a 32-bit register. The register is used as a standard cross-peripheral identification system. The SSPPCellID register is set to 0xB105F00D.",
        0xff0 + (num * 4),
        [
            (
                "ssp_pcell_id{}".format(num),
                "The bits are read as 0x{:X}".format(magic[num]),
                "[7:0]",
                "read-only"
            )
        ],
        16
    )
