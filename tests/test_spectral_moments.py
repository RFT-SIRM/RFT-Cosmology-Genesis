import math

import pytest

from src.spectral_moments import (
    hilbert_dimension,
    normalized_h6,
    normalized_h6_limit,
    normalized_h6_remainder,
    normalized_h8,
    normalized_h8_limit,
    normalized_h8_remainder,
    su2_trace_defect_h6,
    su2_trace_defect_h8,
)


@pytest.mark.parametrize(
    "level,expected",
    [
        (2, -6956.588745030516),
        (3, -18274.354980121832),
        (4, -52227.653685396537),
    ],
)
def test_h6_formula_matches_evgeny_theorem_reference(level, expected):
    actual = su2_trace_defect_h6(level, math.pi / 2)
    assert math.isclose(actual, expected, rel_tol=2e-12, abs_tol=1e-8)


@pytest.mark.parametrize(
    "level,expected",
    [
        (2, -595053.284942481667),
        (3, -1632052.331668503582),
        (4, -4743049.471846580505),
    ],
)
def test_h8_formula_matches_evgeny_theorem_reference(level, expected):
    actual = su2_trace_defect_h8(level, math.pi / 2)
    assert math.isclose(actual, expected, rel_tol=2e-12, abs_tol=1e-7)


def test_su2_hilbert_dimension_matches_graph_convention():
    assert [hilbert_dimension(m) for m in range(1, 5)] == [12, 30, 84, 246]


@pytest.mark.parametrize("theta", [0.0, math.pi / 4, math.pi / 2, math.pi, 2 * math.pi])
@pytest.mark.parametrize("level", [2, 3, 8])
def test_h6_exact_normalized_limit_and_remainder(theta, level):
    assert math.isclose(
        normalized_h6(level, theta),
        normalized_h6_limit(theta) + normalized_h6_remainder(level, theta),
        rel_tol=2e-12,
        abs_tol=2e-8,
    )


@pytest.mark.parametrize("theta", [0.0, math.pi / 4, math.pi / 2, math.pi, 2 * math.pi])
@pytest.mark.parametrize("level", [2, 3, 8])
def test_h8_exact_normalized_limit_and_remainder(theta, level):
    assert math.isclose(
        normalized_h8(level, theta),
        normalized_h8_limit(theta) + normalized_h8_remainder(level, theta),
        rel_tol=2e-12,
        abs_tol=2e-7,
    )


@pytest.mark.parametrize("function", [normalized_h6, normalized_h8])
def test_higher_moment_closed_forms_reject_uncovered_level_one(function):
    with pytest.raises(ValueError):
        function(1, math.pi / 2)
