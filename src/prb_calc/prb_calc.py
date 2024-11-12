from math import ceil
from src.prb_calc import mcs_tables_5_1_3_1
from src.prb_calc import bw
from src.prb_calc import symbol_table

# Computes the maximum speed (in bps) for a given cell
def to_bps(
        is_uplink: bool,
        mcs: int, 
        numerology: int, 
        bandwidth: int, 
        scaling_factor: float = 1.0, 
        mimo: int = 1, 
        symbol_format: int = 5, 
        is_tdd: bool = True, 
        use_flex_sym: bool = True, 
        mcs_table: int = 0
        ) -> float:
    if is_uplink:
        overhead = 0.08
    else:
        overhead = 0.14
    result = 1.0
    # vlayers
    result *= mimo
    # Qm
    result *= mcs_tables_5_1_3_1[mcs_table][mcs].modulation_order
    # f
    result *= scaling_factor
    # Rmax
    result *= mcs_tables_5_1_3_1[mcs_table][mcs].target_code_rate / 1024
    # T
    result *= 14 * (2**numerology) * (10**3)
    result *= 12
    # Nprb
    result *= bw[bandwidth][numerology]
    # OH
    result *= 1 - overhead
    if is_tdd:
        symbol_ratio: float = 0.0
        if is_uplink:
            symbol_ratio += symbol_table[symbol_format].uplink
        else:
            symbol_ratio += symbol_table[symbol_format].downlink
        if use_flex_sym:
            symbol_ratio += symbol_table[symbol_format].flexible
        result *= symbol_ratio
    return result

# Computes the minimum percentage of PRBs required to achieve a given speed (in
# bps)
def to_prb(
        speed: float, 
        is_uplink: bool, 
        mcs: int, 
        numerology: int, 
        bandwidth: int, 
        scaling_factor: float = 1.0, 
        mimo: int = 1, 
        symbol_format: int = 5, 
        is_tdd: bool = True, 
        use_flex_sym: bool = True, 
        mcs_table: int = 0
        ) -> int:
    total_speed: float = to_bps(is_uplink, mcs, numerology, bandwidth, mimo=mimo, scaling_factor=scaling_factor, symbol_format=symbol_format, is_tdd=is_tdd, use_flex_sym=use_flex_sym, mcs_table=mcs_table)
    return ceil((speed/total_speed) / 100)
