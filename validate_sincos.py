"""
Validation script: compare SinCos lookup values with math.sin/math.cos.
"""

import math
from sincos import SinCos


def calculated_sin(angle_deg: float) -> float:
    return math.sin(math.radians(angle_deg))


def calculated_cos(angle_deg: float) -> float:
    return math.cos(math.radians(angle_deg))


def main():
    print("SinCos validation: lookup vs calculated (math.sin/cos)")
    print("=" * 80)
    print(f"{'Angle (°)':<10} {'lookup_sin':<14} {'calc_sin':<14} {'sin_diff':<12} {'lookup_cos':<14} {'calc_cos':<14} {'cos_diff':<12}")
    print("-" * 80)

    max_sin_diff = 0.0
    max_cos_diff = 0.0
    test_angles = list(range(0, 361, 15))  # 0, 15, 30, ..., 360
    # Add some non-integer angles
    test_angles.extend([7.3, 22.7, 45.5, 63.8, 89.2, 180.5, 270.3])
    test_angles.sort()

    for angle in test_angles:
        ls = SinCos.lookup_sin(angle)
        lc = SinCos.lookup_cos(angle)
        cs = calculated_sin(angle)
        cc = calculated_cos(angle)
        sin_diff = abs(ls - cs)
        cos_diff = abs(lc - cc)
        max_sin_diff = max(max_sin_diff, sin_diff)
        max_cos_diff = max(max_cos_diff, cos_diff)
        print(f"{angle:<10.2f} {ls:<14.6f} {cs:<14.6f} {sin_diff:<12.2e} {lc:<14.6f} {cc:<14.6f} {cos_diff:<12.2e}")

    print("-" * 80)
    print(f"Max |lookup_sin - calc_sin|: {max_sin_diff:.2e}")
    print(f"Max |lookup_cos - calc_cos|: {max_cos_diff:.2e}")
    print("=" * 80)


if __name__ == "__main__":
    main()
