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
# Angles computed in-loop from range to avoid allocating a large list (OOM).
def time_lookups(n: int, angle_min: float, angle_max: float) -> float:
    step = (angle_max - angle_min) / n if n else 0
    start = time.monotonic()
    for i in range(n):
        a = angle_min + i * step
        SinCos.lookup_sin(a)
        SinCos.lookup_cos(a)
    return time.monotonic() - start


def time_calculations(n: int, angle_min: float, angle_max: float) -> float:
    step = (angle_max - angle_min) / n if n else 0
    start = time.monotonic()
    for i in range(n):
        a = angle_min + i * step
        calculated_sin(a)
        calculated_cos(a)
    return time.monotonic() - start


def main():
    # Angle range 0-360 to exercise all quadrants; no list allocation
    angle_min = 0.0
    angle_max = 360.0

    for n in [10_000, 100_000]:
        lookup_time = time_lookups(n, angle_min, angle_max)
        calc_time = time_calculations(n, angle_min, angle_max)

        print("--- %d lookups / calculations ---" % n)
        print("  Lookup (SinCos):     %.4f s  (%.0f pairs/s)" % (lookup_time, n / lookup_time))
        print("  Calculation (math):  %.4f s  (%.0f pairs/s)" % (calc_time, n / calc_time))
        if calc_time > 0:
            ratio = lookup_time / calc_time
            print("  Lookup vs calc:      %.2fx" % ratio)
        print()

    print("Done.")


if __name__ == "__main__":
    main()
