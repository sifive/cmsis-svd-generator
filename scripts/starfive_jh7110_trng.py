#!/usr/bin/env python3
# Copyleft (c) 2023 cmsis-svd-generator developers
# SPDX-License-Identifier: Apache-2.0

from scripts.starfive_common import *

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

    for idx in range(8):
        txt += generate_register_trng_rand("rand_{}".format(idx), 0x20 + (idx * 4), idx)

    txt += generate_register_trng_auto_rqsts("auto_rqsts")
    txt += generate_register_trng_auto_age("auto_age")

    txt += """\
              </registers>
"""
    return txt

def generate_register_trng_ctrl(name):
    """Generate xml string for starfive_jh7110_trng """ + name + """ register"""
    return generate_register(name, "TRNG CTRL Register", 0x0, [
        ("exec_nop", "Execute a NOP instruction", "[0:0]", "read-write"),
        ("gen_rand", "Generate a random number", "[1:1]", "read-write"),
        ("reseed", "Reseed the TRNG from noise sources", "[2:2]", "read-write")
    ])

def generate_register_trng_stat(name):
    """Generate xml string for starfive_jh7110_trng """ + name + """ register"""
    fields = [
        ("nonce_mode", "TRNG Nonce operating mode", "[2:2]", "read-only"),
        ("r256", "TRNG 256-bit random number operating mode", "[3:3]", "read-only"),
        ("mission_mode", "TRNG Mission Mode operating mode", "[8:8]", "read-only"),
        ("seeded", "TRNG Seeded operating mode", "[9:9]", "read-only")
    ]

    # There are 8 RAND fields
    # FIXME: do these LAST_RESEED fields directly correspond to the RAND fields?
    # These fields are a best-guess based on the Linux char driver
    for idx in range(8):
        # last reseed fields start at bit offset 16 (0x10 hex)
        bit = 0x10 + idx
        fields.append((
            "last_reseed_{}".format(idx),
            "TRNG Last Reseed {} status".format(idx),
            "[{}:{}]".format(bit, bit),
            "read-only"
        ))

    fields.extend([
        ("srvc_rqst", "TRNG Service Request", "[27:27]", "read-only"),
        ("rand_generating", "TRNG Random Number Generating Status", "[30:30]", "read-only"),
        ("rand_seeding", "TRNG Random Number Seeding Status", "[31:31]", "read-only")
    ])

    return generate_register(name, "TRNG STAT Register", 0x4, fields)

def generate_register_trng_mode(name):
    """Generate xml string for starfive_jh7110_trng """ + name + """ register"""
    return generate_register(name, "TRNG MODE Register", 0x8, [
        ("r256", "256-bit operation mode: 0 - 128-bit mode, 1 - 256-bit mode", "[3:3]", "read-write")
    ])

def generate_register_trng_smode(name):
    """Generate xml string for starfive_jh7110_trng """ + name + """ register"""
    return generate_register(name, "TRNG SMODE Register", 0xc, [
        ("nonce_mode", "Nonce operation mode", "[2:2]", "read-write"),
        ("mission_mode", "Mission operation mode", "[8:8]", "read-write"),
        ("max_rejects", "TRNG Maximum Rejects", "[31:16]", "read-write")
    ])

def generate_register_trng_ie(name):
    """Generate xml string for starfive_jh7110_trng """ + name + """ register"""
    return generate_register(name, "TRNG Interrupt Enable Register", 0x10, [
        ("rand_rdy_en", "RAND Ready Enable", "[0:0]", "read-write"),
        ("seed_done_en", "Seed Done Enable", "[1:1]", "read-write"),
        ("lfsr_lockup_en", "LFSR Lockup Enable", "[4:4]", "read-write"),
        ("glbl_en", "Global Enable", "[31:31]", "read-write")
    ])

def generate_register_trng_istat(name):
    """Generate xml string for starfive_jh7110_trng """ + name + """ register"""
    return generate_register(name, "TRNG Interrupt Status Register", 0x14, [
        ("rand_rdy", "RAND Ready Enable", "[0:0]", "read-only"),
        ("seed_done", "Seed Done Enable", "[1:1]", "read-only"),
        ("lfsr_lockup_en", "LFSR Lockup Enable", "[4:4]", "read-only")
    ])

def generate_register_trng_rand(name, addr, idx):
    """Generate xml string for starfive_jh7110_trng """ + name + """ register"""
    return generate_register(name, "TRNG RAND {} Status Register".format(idx), addr, [("rand", "Random number bits", "[31:0]", "read-only")])

def generate_register_trng_auto_rqsts(name):
    """Generate xml string for starfive_jh7110_trng """ + name + """ register"""
    return generate_register(
        name,
        "Auto-reseeding after random number requests by host reaches specified counter: 0 - disable counter, other - reload value for internal counter",
        0x60,
        [("rqsts", "Threshold number of reseed requests for auto-reseed counter", "[31:0]", "read-write")],
    )

def generate_register_trng_auto_age(name):
    """Generate xml string for starfive_jh7110_trng """ + name + """ register"""
    return generate_register(
        name,
        "Auto-reseeding after specified timer countdowns to 0: 0 - disable timer, other - reload value for internal timer",
        0x64,
        [("age", "Countdown value for auto-reseed timer", "[31:0]", "read-write")],
    )
