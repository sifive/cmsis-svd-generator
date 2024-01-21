#!/usr/bin/env python3
# Copyleft (c) 2023 cmsis-svd-generator developers
# SPDX-License-Identifier: Apache-2.0

from scripts.starfive_common import *

"""
This program generates CMSIS SVD xml for starfive JH7110 dmc phy
"""

def generate_registers_starfive_jh7110_dmc_phy(dts, peripheral):
    """Generate xml string for registers for starfive_dmc_phy peripheral"""
    txt = """\
              <registers>
"""

    txt += generate_register_arr("csr", "DDR Memory Control PHY CSR", 0x0, 512, 0x4)
    txt += generate_register_arr("base", "DDR Memory Control PHY Base register", 0x800, 512, 0x4)
    txt += generate_register_arr("ac_base", "DDR Memory Control PHY AC Base register", 0x1000, 2048, 0x4)

    return txt + """\
              </registers>
"""
