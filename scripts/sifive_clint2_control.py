#!/usr/bin/env python3
# Copyright (c) 2024 SiFive Inc.
# SPDX-License-Identifier: Apache-2.0

"""
This program generates CMSIS SVD xml for sifive clint2
"""


def generate_registers_sifive_clint2(dts):
    """Generate xml string for registers for sifive_clint2 peripheral"""
    cpus = dts.get_by_path("/cpus")
    txt = """\
              <registers>
"""

    hart_num = 0
    addr_num = 0x0000
    for cpu in cpus.child_nodes():
        if cpu.get_field("device_type") is not None:
            if cpu.get_fields("device_type")[0] == "cpu":
                hart = str(hart_num)
                addr = f"0x{addr_num:X}"
                txt += generate_registers_sifive_clint2_msip(hart, addr)
                hart_num += 1
                addr_num += 0x4

    hart_num = 0
    addr_num = 0x4000
    for cpu in cpus.child_nodes():
        if cpu.get_field("device_type") is not None:
            if cpu.get_fields("device_type")[0] == "cpu":
                hart = str(hart_num)
                addr = f"0x{addr_num:X}"
                txt += generate_registers_sifive_clint2_mtimecmp(hart, addr)
                hart_num += 1
                addr_num += 0x8

    addr_num = 0xBFF8
    addr = f"0x{addr_num:X}"
    txt += generate_registers_sifive_clint2_mtime(addr)

    txt += """\
              </registers>
"""
    return txt


def generate_registers_sifive_clint2_msip(hart, addr):
    """Generate xml string for sifive_clint2 msip register for specific hart"""
    return (
        """\
                <register>
                  <name>msip_"""
        + hart
        + """</name>
                  <description>MSIP Register for hart """
        + hart
        + """</description>
                  <addressOffset>"""
        + addr
        + """</addressOffset>
                </register>
"""
    )


def generate_registers_sifive_clint2_mtimecmp(hart, addr):
    """Generate xml string for sifive_clint2 mtimecmp register for specific hart"""
    return (
        """\
                <register>
                  <name>mtimecmp_"""
        + hart
        + """</name>
                  <description>MTIMECMP Register for hart """
        + hart
        + """</description>
                  <addressOffset>"""
        + addr
        + """</addressOffset>
                  <size>64</size>
                </register>
"""
    )


def generate_registers_sifive_clint2_mtime(addr):
    """Generate xml string for sifive_clint2 mtime register"""
    return (
        """\
                <register>
                  <name>mtime</name>
                  <description>MTIME Register</description>
                  <addressOffset>"""
        + addr
        + """</addressOffset>
                  <size>64</size>
                </register>
"""
    )
