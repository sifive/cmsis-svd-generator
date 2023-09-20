#!/usr/bin/env python3
# Copyleft (c) 2023 cmsis-svd-generator developers
# SPDX-License-Identifier: Apache-2.0

"""
This program generates CMSIS SVD xml for starfive JH7110 trng
"""

def generate_registers_starfive_jh7110_trng(dts, peripheral):
    """Generate xml string for registers for starfive_trng peripheral"""

    txt = """\
              <registers>
"""

    txt += generate_register_trng_ctrl("ctrl");
    txt += generate_register_trng_stat("stat");
    txt += generate_register_trng_mode("mode");
    txt += generate_register_trng_smode("smode");
    txt += generate_register_trng_ie("ie");
    txt += generate_register_trng_istat("istat");

    for idx in range(0, 8):
        txt += generate_register_trng_rand("rand{}".format(idx), 0x20 + (idx * 4), idx)

    txt += generate_register_trng_auto_rqsts("auto_rqsts")
    txt += generate_register_trng_auto_age("auto_age")

    txt += """\
              </registers>
"""
    return txt

def generate_register_trng_ctrl(name):
    """Generate xml string for starfive_jh7110_trng """ + name + """ register"""
    return """\
                <register>
                  <name>""" + name + """</name>
                  <description>TRNG CTRL Register</description>
                  <addressOffset>0x0</addressOffset>
                  <size>32</size>
                  <fields>
                    <field>
                      <name>exec_nop</name>
                      <description>Execute a NOP instruction</description>
                      <bitRange>[0:0]</bitRange>
                      <access>read-write</access>
                    </field>
                    <field>
                      <name>gene_randnum</name>
                      <description>Generate a random number</description>
                      <bitRange>[1:1]</bitRange>
                      <access>read-write</access>
                    </field>
                    <field>
                      <name>exec_randreseed</name>
                      <description>Reseed the TRNG from noise sources</description>
                      <bitRange>[2:2]</bitRange>
                      <access>read-write</access>
                    </field>
                  </fields>
                </register>
"""


def generate_register_trng_stat(name):
    """Generate xml string for starfive_jh7110_trng """ + name + """ register"""
    txt = """\
                <register>
                  <name>stat</name>
                  <description>TRNG STAT Register</description>
                  <addressOffset>0x4</addressOffset>
                  <size>32</size>
                  <fields>
                    <field>
                      <name>nonce_mode</name>
                      <description>TRNG Nonce operating mode</description>
                      <bitRange>[2:2]</bitRange>
                      <access>read-only</access>
                    </field>
                    <field>
                      <name>r256</name>
                      <description>TRNG 256-bit random number operating mode</description>
                      <bitRange>[3:3]</bitRange>
                      <access>read-only</access>
                    </field>
                    <field>
                      <name>mission_mode</name>
                      <description>TRNG Mission Mode operating mode</description>
                      <bitRange>[8:8]</bitRange>
                      <access>read-only</access>
                    </field>
                    <field>
                      <name>seeded</name>
                      <description>TRNG Seeded operating mode</description>
                      <bitRange>[9:9]</bitRange>
                      <access>read-only</access>
                    </field>
"""

    # There are 8 RAND fields
    # FIXME: do these LAST_RESEED fields directly correspond to the RAND fields?
    # These fields are a best-guess based on the Linux char driver
    for idx in range(0, 8):
        # last reseed fields start at bit offset 16 (0x10 hex)
        txt += generate_field_last_reseed(0x10 + idx, idx)

    txt += """\
                    <field>
                      <name>srvc_rqst</name>
                      <description>TRNG Service Request</description>
                      <bitRange>[27:27]</bitRange>
                      <access>read-only</access>
                    </field>
                    <field>
                      <name>rand_generating</name>
                      <description>TRNG Random Number Generating Status</description>
                      <bitRange>[30:30]</bitRange>
                      <access>read-only</access>
                    </field>
                    <field>
                      <name>rand_seeding</name>
                      <description>TRNG Random Number Seeding Status</description>
                      <bitRange>[31:31]</bitRange>
                      <access>read-only</access>
                    </field>
                  </fields>
                </register>
"""

    return txt

def generate_register_trng_mode(name):
    """Generate xml string for starfive_jh7110_trng """ + name + """ register"""
    return """\
                <register>
                  <name>""" + name + """</name>
                  <description>TRNG MODE Register</description>
                  <addressOffset>0x8</addressOffset>
                  <size>32</size>
                  <fields>
                    <field>
                      <name>r256</name>
                      <description>256-bit operation mode: 0 - 128-bit mode, 1 - 256-bit mode</description>
                      <bitRange>[3:3]</bitRange>
                      <access>read-write</access>
                    </field>
                  </fields>
                </register>
"""

def generate_register_trng_smode(name):
    """Generate xml string for starfive_jh7110_trng """ + name + """ register"""
    return """\
                <register>
                  <name>""" + name + """</name>
                  <description>TRNG SMODE Register</description>
                  <addressOffset>0xc</addressOffset>
                  <size>32</size>
                  <fields>
                    <field>
                      <name>nonce_mode</name>
                      <description>Nonce operation mode</description>
                      <bitRange>[2:2]</bitRange>
                      <access>read-write</access>
                    </field>
                    <field>
                      <name>mission_mode</name>
                      <description>Mission operation mode</description>
                      <bitRange>[8:8]</bitRange>
                      <access>read-write</access>
                    </field>
                    <field>
                      <name>max_rejects</name>
                      <description>TRNG Maximum Rejects</description>
                      <bitRange>[31:16]</bitRange>
                      <access>read-write</access>
                    </field>
                  </fields>
                </register>
"""

def generate_register_trng_ie(name):
    """Generate xml string for starfive_jh7110_trng """ + name + """ register"""
    return """\
                <register>
                  <name>""" + name + """</name>
                  <description>TRNG Interrupt Enable Register</description>
                  <addressOffset>0x10</addressOffset>
                  <size>32</size>
                  <fields>
                    <field>
                      <name>rand_rdy_en</name>
                      <description>RAND Ready Enable</description>
                      <bitRange>[0:0]</bitRange>
                      <access>read-write</access>
                    </field>
                    <field>
                      <name>seed_done_en</name>
                      <description>Seed Done Enable</description>
                      <bitRange>[1:1]</bitRange>
                      <access>read-write</access>
                    </field>
                    <field>
                      <name>lfsr_lockup_en</name>
                      <description>LFSR Lockup Enable</description>
                      <bitRange>[4:4]</bitRange>
                      <access>read-write</access>
                    </field>
                    <field>
                      <name>glbl_en</name>
                      <description>Global Enable</description>
                      <bitRange>[31:31]</bitRange>
                      <access>read-write</access>
                    </field>
                  </fields>
                </register>
"""

def generate_register_trng_istat(name):
    """Generate xml string for starfive_jh7110_trng """ + name + """ register"""
    return """\
                <register>
                  <name>""" + name + """</name>
                  <description>TRNG Interrupt Status Register</description>
                  <addressOffset>0x14</addressOffset>
                  <size>32</size>
                  <fields>
                    <field>
                      <name>rand_rdy</name>
                      <description>RAND Ready Enable</description>
                      <bitRange>[0:0]</bitRange>
                      <access>read-only</access>
                    </field>
                    <field>
                      <name>seed_done</name>
                      <description>Seed Done Enable</description>
                      <bitRange>[1:1]</bitRange>
                      <access>read-only</access>
                    </field>
                    <field>
                      <name>lfsr_lockup_en</name>
                      <description>LFSR Lockup Enable</description>
                      <bitRange>[4:4]</bitRange>
                      <access>read-only</access>
                    </field>
                  </fields>
                </register>
"""

def generate_register_trng_rand(name, addr, idx):
    """Generate xml string for starfive_jh7110_trng """ + name + """ register"""

    desc = "TRNG RAND {} Status Register".format(idx)
    addr_offset = "0x{:x}".format(addr)

    return """\
                <register>
                  <name>""" + name + """</name>
                  <description>""" + desc + """</description>
                  <addressOffset>""" + addr_offset + """</addressOffset>
                  <size>32</size>
                  <fields>
                    <field>
                      <name>rand</name>
                      <description>Random number bits</description>
                      <bitRange>[31:0]</bitRange>
                      <access>read-only</access>
                    </field>
                  </fields>
                </register>
"""

def generate_register_trng_auto_rqsts(name):
    """Generate xml string for starfive_jh7110_trng """ + name + """ register"""

    return """\
                <register>
                  <name>""" + name + """</name>
                  <description>Auto-reseeding after random number requests by host reaches specified counter: 0 - disable counter, other - reload value for internal counter</description>
                  <addressOffset>0x60</addressOffset>
                  <size>32</size>
                  <fields>
                    <field>
                      <name>rqsts</name>
                      <description>Threshold number of reseed requests for auto-reseed counter</description>
                      <bitRange>[31:0]</bitRange>
                      <access>read-write</access>
                    </field>
                  </fields>
                </register>
"""

def generate_register_trng_auto_age(name):
    """Generate xml string for starfive_jh7110_trng """ + name + """ register"""

    return """\
                <register>
                  <name>""" + name + """</name>
                  <description>Auto-reseeding after specified timer countdowns to 0: 0 - disable timer, other - reload value for internal timer</description>
                  <addressOffset>0x64</addressOffset>
                  <size>32</size>
                  <fields>
                    <field>
                      <name>age</name>
                      <description>Countdown value for auto-reseed timer</description>
                      <bitRange>[31:0]</bitRange>
                      <access>read-write</access>
                    </field>
                  </fields>
                </register>
"""

def generate_field_last_reseed(bit, idx):
    name = "last_reseed{}".format(idx)
    desc = "TRNG Last Reseed {} status".format(idx)
    bit_range = "[{}:{}]".format(bit, bit)

    return """\
                    <field>
                      <name>""" + name + """</name>
                      <description>""" + desc + """</description>
                      <bitRange>""" + bit_range + """</bitRange>
                      <access>read-only</access>
                    </field>
"""
