"""
Timing script: measure 10,000 and 100,000 lookups vs math.sin/cos calculations.
"""

import math
import time
from sincos import SinCos


def calculated_sin(angle_deg: float) -> float:
    return math.sin(math.radians(angle_deg))


def calculated_cos(angle_deg: float) -> float:
    return math.cos(math.radians(angle_deg))


# Use monotonic() for CircuitPython (no perf_counter); works on CPython too
def time_lookups(n: int, angles_deg: list) -> float:
    start = time.monotonic()
    for a in angles_deg:
        SinCos.lookup_sin(a)
        SinCos.lookup_cos(a)
    return time.monotonic() - start


def time_calculations(n: int, angles_deg: list) -> float:
    start = time.monotonic()
    for a in angles_deg:
        calculated_sin(a)
        calculated_cos(a)
    return time.monotonic() - start


def main():
    # Reuse a list of angles so we measure pure lookup/calc cost
    # Mix of angles in 0-360 to exercise all quadrants
    base_angles = [i * 1.7 for i in range(212)]  # 0, 1.7, 3.4, ... (covers 0-360)

    for n in [10_000, 100_000]:
        # Repeat base_angles to get exactly n sin+cos evaluations (n pairs)
        pairs_needed = n
        angles_deg = (base_angles * ((pairs_needed // len(base_angles)) + 1))[:pairs_needed]

        lookup_time = time_lookups(n, angles_deg)
        calc_time = time_calculations(n, angles_deg)

        print(f"--- {n:,} lookups / calculations ---")
        print(f"  Lookup (SinCos):     {lookup_time:.4f} s  ({n / lookup_time:,.0f} pairs/s)")
        print(f"  Calculation (math):  {calc_time:.4f} s  ({n / calc_time:,.0f} pairs/s)")
        if calc_time > 0:
            ratio = lookup_time / calc_time
            print(f"  Lookup vs calc:      {ratio:.2f}x")
        print()

    print("Done.")


if __name__ == "__main__":
    main()
