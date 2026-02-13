"""
Demonstration of SinCos lookup_sin and lookup_cos.
Prints values for integer angles 1 to 90 and 5 non-whole number angles.
"""

from sincos import SinCos


def main():
    print("SinCos lookup demonstration")
    print("=" * 60)
    print(f"{'Angle (°)':<12} {'lookup_sin':<14} {'lookup_cos':<14}")
    print("-" * 60)

    # Integer angles 1 to 90
    for angle in range(1, 91):
        s = SinCos.lookup_sin(angle)
        c = SinCos.lookup_cos(angle)
        print(f"{angle:<12.1f} {s:<14.6f} {c:<14.6f}")

    # Five non-whole number values
    non_whole = [7.3, 22.7, 45.5, 63.8, 89.2]
    print("-" * 60)
    print("Non-whole number angles (rounded to nearest degree for lookup):")
    print("-" * 60)
    for angle in non_whole:
        s = SinCos.lookup_sin(angle)
        c = SinCos.lookup_cos(angle)
        print(f"{angle:<12.2f} {s:<14.6f} {c:<14.6f}")

    print("=" * 60)


if __name__ == "__main__":
    main()
