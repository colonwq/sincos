"""
CI: compare SinCos table lookup to math.sin/cos at the effective integer degree.

SinCos reduces angle mod 360 and rounds to the nearest degree before lookup;
for the angles below, that matches int(round(angle % 360)).
"""

import math

import pytest

from sincos import SinCos

CI_ANGLES_DEG = (0, 40, 80, 270, 355, 365)

# Static table uses 4 significant digits; allow small absolute error vs full-precision math.
_MAX_ABS_ERR = 5e-4


def _effective_degree(angle: float) -> int:
    return int(round(angle % 360))


@pytest.mark.parametrize("angle_deg", CI_ANGLES_DEG)
def test_lookup_sin_matches_computed(angle_deg: int) -> None:
    deg = _effective_degree(float(angle_deg))
    expected = math.sin(math.radians(deg))
    got = SinCos.lookup_sin(float(angle_deg))
    assert got == pytest.approx(expected, abs=_MAX_ABS_ERR), (
        f"lookup_sin({angle_deg}): got {got}, expected ~{expected} (deg={deg})"
    )


@pytest.mark.parametrize("angle_deg", CI_ANGLES_DEG)
def test_lookup_cos_matches_computed(angle_deg: int) -> None:
    deg = _effective_degree(float(angle_deg))
    expected = math.cos(math.radians(deg))
    got = SinCos.lookup_cos(float(angle_deg))
    assert got == pytest.approx(expected, abs=_MAX_ABS_ERR), (
        f"lookup_cos({angle_deg}): got {got}, expected ~{expected} (deg={deg})"
    )
