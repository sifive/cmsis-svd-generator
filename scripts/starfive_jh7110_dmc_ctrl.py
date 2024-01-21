#!/usr/bin/env python3
# Copyleft (c) 2023 cmsis-svd-generator developers
# SPDX-License-Identifier: Apache-2.0

from scripts.starfive_common import *

"""
This program generates CMSIS SVD xml for starfive JH7110 dmc ctrl
"""

def generate_registers_starfive_jh7110_dmc_ctrl(dts, peripheral):
    """Generate xml string for registers for starfive_dmc_ctrl peripheral"""
    txt = """\
              <registers>
"""

    txt += generate_register_arr("csr", "DDR Memory Control CSR register", 0x0, 1024, 0x4)
    txt += generate_register_arr("sec", "DDR Memory Control SEC register", 0x1000, 1024, 0x4)

    return txt + """\
              </registers>
"""
