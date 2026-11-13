"""Normalized higher SU(2) spectral trace defects from Evgeny's Theorem.

The H6/H8 formulas combine upstream Lean recurrences with exact symbolic
finite-level base-transition certificates. They are orientation-specific:
the standard numbering orientation oNum is used, with faceAxis compared to
the fixed-Z commuting control.

H10 is intentionally not duplicated here. Its exact affine coefficient is
still represented upstream as a finite trace expression, not an explicit
trigonometric polynomial.
"""
import math


def hilbert_dimension(level: int) -> int:
    """Return 2|V_m| = 3^(m+1) + 3 for an SU(2) gasket operator."""
    if level < 1:
        raise ValueError("level must be >= 1")
    return 3 ** (level + 1) + 3


def _cs(theta: float) -> tuple[float, float]:
    return math.cos(theta / 2), math.sin(theta / 2)


def _h6_base_and_constant(theta: float) -> tuple[float, float]:
    c, s = _cs(theta)
    d2 = -14592 * s**2 + 1344 * c * s**2 - 384 * s**3
    c6 = 4512 * s**2 + 192 * c * s**2 + 768 * s**3
    return d2, c6


def su2_trace_defect_h6(level: int, theta: float) -> float:
    """Return the exact all-angle H6 numbering-orientation defect (level >= 2)."""
    if level < 2:
        raise ValueError("the H6 closed formula is stated for level >= 2")
    d2, c6 = _h6_base_and_constant(theta)
    scale = 3 ** (level - 2)
    return scale * d2 + (scale - 1) * c6 / 2


def normalized_h6(level: int, theta: float) -> float:
    """Return the H6 trace defect divided by the SU(2) Hilbert dimension."""
    return su2_trace_defect_h6(level, theta) / hilbert_dimension(level)


def normalized_h6_limit(theta: float) -> float:
    """Return the exact limit of the normalized H6 trace defect."""
    c, s = _cs(theta)
    return (-12336 + 1440 * c) * s**2 / 27


def normalized_h6_remainder(level: int, theta: float) -> float:
    """Return normalized_h6(level, theta) - normalized_h6_limit(theta)."""
    if level < 2:
        raise ValueError("the H6 closed formula is stated for level >= 2")
    d2, c6 = _h6_base_and_constant(theta)
    return -(d2 + 5 * c6) / (9 * hilbert_dimension(level))


def _h8_base_and_constant(theta: float) -> tuple[float, float]:
    c, s = _cs(theta)
    d2 = (
        -1335552 * s**2
        + 244352 * c * s**2
        - 40064 * s**3
        + 64 * c * s**3
        + 1920 * s**4
    )
    c8 = (
        193600 * s**2
        + 75776 * c * s**2
        + 83712 * s**3
        - 512 * c * s**3
        + 192 * s**4
    )
    return d2, c8


def su2_trace_defect_h8(level: int, theta: float) -> float:
    """Return the exact all-angle H8 numbering-orientation defect (level >= 2)."""
    if level < 2:
        raise ValueError("the H8 closed formula is stated for level >= 2")
    d2, c8 = _h8_base_and_constant(theta)
    scale = 3 ** (level - 2)
    return scale * d2 + (scale - 1) * c8 / 2


def normalized_h8(level: int, theta: float) -> float:
    """Return the H8 trace defect divided by the SU(2) Hilbert dimension."""
    return su2_trace_defect_h8(level, theta) / hilbert_dimension(level)


def normalized_h8_limit(theta: float) -> float:
    """Return the exact limit of the normalized H8 trace defect."""
    c, s = _cs(theta)
    return (
        -1238752 * s**2
        + 282240 * c * s**2
        + 1792 * s**3
        - 192 * c * s**3
        + 2016 * s**4
    ) / 27


def normalized_h8_remainder(level: int, theta: float) -> float:
    """Return normalized_h8(level, theta) - normalized_h8_limit(theta)."""
    if level < 2:
        raise ValueError("the H8 closed formula is stated for level >= 2")
    d2, c8 = _h8_base_and_constant(theta)
    return -(d2 + 5 * c8) / (9 * hilbert_dimension(level))
