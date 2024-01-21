#!/usr/bin/env python3
# Copyleft (c) 2023 cmsis-svd-generator developers 
# SPDX-License-Identifier: Apache-2.0

from scripts.starfive_common import *

"""
This program generates CMSIS SVD xml for starfive JH7110 pmu
"""

def generate_registers_starfive_jh7110_pmu(dts, peripheral):
    """Generate xml string for registers for starfive_pmu peripheral"""

    txt = """\
              <registers>
"""

    txt += generate_register_hard_event()
    txt += generate_register_soft_turn_on_power_mode()
    txt += generate_register_soft_turn_off_power_mode()
    txt += generate_register_timeout_seq_thd()

    for i in range(3):
        txt += generate_register_pdc(i)

    txt += generate_register_sw_encourage()
    txt += generate_register_tim()
    txt += generate_register_pch_bypass()
    txt += generate_register_pch_pstate()
    txt += generate_register_pch_timeout()
    txt += generate_register_lp_timeout()
    txt += generate_register_hard_turn_on_power_mode()
    txt += generate_register_current_power_mode()
    txt += generate_register_current_seq_state()
    txt += generate_register_event_status()
    txt += generate_register_int_status()
    txt += generate_register_hw_event_crd()
    txt += generate_register_encourage_type_crd()
    txt += generate_register_pch_active()

    return txt + """\
              </registers>
"""

def generate_register_hard_event():
    descs = [
        "RTC event encourage turn-on sequence",
        "GMAC event encourage turn-on sequence", 
        "RFU"
    ] 

    for i in range(4):
        descs.append("RGPIO{} event encourage turn-on sequence".format(i))

    descs.append("GPU event")

    ndra = [
        ("hard_event_{}_on_mask".format(i), "{}, 1: mask hardware event, 0: enable hardware event".format(descs[i]), "[{}:{}]".format(i, i), "read-write") for i in range(len(descs))
    ]

    return generate_register("hard_event_turn_on_mask", "Hardware Event Turn-On Mask", 0x4, ndra)

def generate_register_soft_turn_on_power_mode():
    ndra = generate_fields_power_mode("on")
    return generate_register("soft_turn_on_power_mode", "Software Turn-On Power Mode", 0xc, ndra)

def generate_register_soft_turn_off_power_mode():
    ndra = generate_fields_power_mode("off")
    return generate_register("soft_turn_off_power_mode", "Software Turn-Off Power Mode", 0x10, ndra)

def generate_register_timeout_seq_thd():
    return generate_register("timeout_seq_thd", "Threshold Sequence Timeout", 0x14, [("timeout_seq_thd", "Threshold Sequence Timeout", "[15:0]", "read-write")])

def generate_register_pdc(idx):
    pd = idx * 3
    dirs = ["off", "on"]
    ndra = []

    for i in range(3):
        for d in range(len(dirs)):
            bit = (i * 10) + (d * 5)
            ndra.append(("pd{}_{}_cas".format(pd + i, dirs[d]), "Power domain {} turn-{} cascade. The register value indicates the power-{} sequence of this domain. 0 means the highest priority. System only accepts value from 0 to 7, any other value is invalid.".format(pd + i, dirs[d], dirs[d]), "[{}:{}]".format(bit + 4, bit), "read-write"))

    return generate_register("pdc{}".format(idx), "Powerdomain Cascade {}".format(idx), 0x18 + (idx * 4), ndra)

def generate_register_sw_encourage():
    return generate_register("sw_encourage", "Software Encouragement", 0x44, [("sw_encourage", "Software Encouragement", "[7:0]", "read-write")])

def generate_register_tim():
    ndra = [
        ("seq_done_mask", "Mask the sequence complete event. 0: mask, 1: unmask", "[0:0]", "read-write"),
        ("hw_req_mask", "Mask the hardware encouragement request. 0: mask, 1: unmask", "[1:1]", "read-write"),
        ("sw_fail_mask", "Mask the software encouragement failure event. 0: mask, 1: unmask", "[3:2]", "read-write"),
        ("hw_fail_mask", "Mask the hardware encouragement failure event. 0: mask, 1: unmask", "[5:4]", "read-write"),
        ("pch_fail_mask", "Mask the P-channel encouragement failure event. 0: mask, 1: unmask", "[8:6]", "read-write"),
    ]

    return generate_register("tim", "TIMER Interrupt Mask", 0x48, ndra)

def generate_register_pch_bypass():
    return generate_register("pch_bypass", "P-channel Bypass", 0x4c, [("pch_bypass", "Bypass P-channel. 0: enable p-channel, 1: bypass p-channel", "[0:0]", "read-write")])

def generate_register_pch_pstate():
    return generate_register("pch_pstate", "P-channel PSTATE", 0x50, [("pch_pstate", "P-channel state set", "[4:0]", "read-write")])

def generate_register_pch_timeout():
    return generate_register("pch_timeout", "P-channel Timeout Threshold", 0x54, [("pch_timeout", "P-channel waiting device acknowledge timeout.", "[7:0]", "read-write")])

def generate_register_lp_timeout():
    return generate_register("lp_timeout", "LP Cell Control Timeout Threshold", 0x58, [("lp_timeout", "LP Cell Control signal waiting carries acknowledge timeout.", "[7:0]", "read-write")])

def generate_register_hard_turn_on_power_mode():
    ndra = generate_fields_power_mode("on")
    return generate_register("hard_turn_on_power_mode", "Hardware Turn-On Power Mode", 0x5c, ndra)

def generate_register_current_power_mode():
    ndra = generate_fields_power_mode("on")
    return generate_register("current_power_mode", "Current Power Mode", 0x80, ndra)

def generate_register_current_seq_state():
    return generate_register("current_seq_state", "Current Sequence State", 0x84, [("power_mode_cur", "Current sequence state.", "[1:0]", "read-only")])

def generate_register_event_status():
    ndra = [
        ("seq_done_event", "Sequence complete.", "[0:0]", "read-only"),
        ("hw_req_event", "Hardware encouragement request.", "[1:1]", "read-only"),
        ("sw_fail_event", "Software encouragement failure.", "[3:2]", "read-only"),
        ("hw_fail_event", "Hardware encouragement failure.", "[5:4]", "read-only"),
        ("pch_fail_event", "P-channel failure.", "[8:6]", "read-only"),
    ]

    return generate_register("event_status", "PMU Event Status", 0x88, ndra)

def generate_register_int_status():
    ndra = [
        ("seq_done_event", "Sequence complete.", "[0:0]", "read-only"),
        ("hw_req_event", "Hardware encouragement request.", "[1:1]", "read-only"),
        ("sw_fail_event", "Software encouragement failure.", "[3:2]", "read-only"),
        ("hw_fail_event", "Hardware encouragement failure.", "[5:4]", "read-only"),
        ("pch_fail_event", "P-channel failure.", "[8:6]", "read-only"),
    ]

    return generate_register("int_status", "PMU Interrupt Status", 0x8c, ndra)

def generate_register_hw_event_crd():
    return generate_register("hw_event_crd", "Hardware Event Record", 0x90, [("hw_event_crd", "Hardware Event Record.", "[7:0]", "read-only")])

def generate_register_encourage_type_crd():
    return generate_register("encourage_type_crd", "Hardware Event Type Record", 0x94, [("encourage_type_crd", "Hardware/Software encouragement type record. 0: Software, 1: Hardware.", "[0:0]", "read-only")])

def generate_register_pch_active():
    return generate_register("pch_active", "P-channel PACTIVE Status", 0x98, [("pch_active", "P-channel PACTIVE status.", "[10:0]", "read-only")])

def generate_fields_power_mode(mode):
    names = ["systop", "cpu", "gpua", "vdec", "vout", "isp", "venc"]
    return [("{}_power_mode".format(names[i]), "{} turn-{} power mode.".format(names[i].upper(), mode), "[{}:{}]".format(i, i), "read-write") for i in range(len(names))]

