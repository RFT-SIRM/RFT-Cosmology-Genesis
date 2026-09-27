import math

from src.model import (
    coupling,
    invariant,
    invariant_limit,
    invariant_pi_over_2,
    invariant_remainder_pi_over_2,
)


def test_invariant_benchmark():
    assert math.isclose(invariant(1, math.pi / 2), -4.0 / 3.0, rel_tol=0, abs_tol=1e-15)


def test_asymptotic_limit():
    assert math.isclose(invariant_pi_over_2(50), -8.0 / 9.0, rel_tol=0, abs_tol=1e-12)
    assert invariant_limit() == -8.0 / 9.0


def test_exact_remainder():
    for m in (1, 2, 3, 10, 20):
        expected = -16.0 / (9.0 * (3**m + 1))
        assert math.isclose(
            invariant_remainder_pi_over_2(m),
            expected,
            rel_tol=0,
            abs_tol=1e-14,
        )


def test_coupling_definition():
    m = 10
    theta = math.pi / 2
    epsilon = 0.01
    assert math.isclose(
        coupling(m, theta, epsilon),
        1.0 + epsilon * invariant(m, theta),
        rel_tol=0,
        abs_tol=1e-15,
    )
