import math

import pytest

from src.cosmology import (
    C_KM_S,
    H0,
    E,
    H,
    OMEGA_GAMMA,
    OMEGA_M,
    OMEGA_NU,
    R,
    omega_lambda,
    peak_positions,
    q_m,
    sound_speed,
    theta_s,
)
from src.model import invariant


@pytest.mark.parametrize(
    "level,theta,epsilon",
    [
        (1, 0.0, 0.0),
        (1, math.pi / 2, 0.01),
        (3, math.pi, 0.01),
        (5, math.pi / 2, -0.02),
    ],
)
def test_photon_coupling_matches_the_invariant_ansatz(level, theta, epsilon):
    assert math.isclose(
        q_m(level, theta, epsilon),
        1.0 + epsilon * invariant(level, theta),
        rel_tol=0,
        abs_tol=1e-15,
    )


@pytest.mark.parametrize(
    "level,theta,epsilon",
    [
        (1, 0.0, 0.0),
        (2, math.pi / 2, 0.01),
        (5, math.pi, -0.02),
    ],
)
def test_background_is_flat_and_h_normalized_at_z_zero(level, theta, epsilon):
    q = q_m(level, theta, epsilon)
    assert math.isclose(
        omega_lambda(level, theta, epsilon),
        1.0 - OMEGA_M - OMEGA_NU - q * OMEGA_GAMMA,
        rel_tol=0,
        abs_tol=1e-15,
    )
    assert math.isclose(E(0.0, level, theta, epsilon), 1.0, rel_tol=0, abs_tol=1e-14)
    assert math.isclose(H(0.0, level, theta, epsilon), H0, rel_tol=0, abs_tol=1e-12)


def test_baryon_photon_ratio_has_inverse_q_scaling():
    level, theta = 3, math.pi / 2
    q = q_m(level, theta, 0.01)
    uncoupled = R(1000.0, level, theta, 0.0)
    coupled = R(1000.0, level, theta, 0.01)
    assert math.isclose(coupled, uncoupled / q, rel_tol=1e-14, abs_tol=0)


@pytest.mark.parametrize("redshift", [0.0, 10.0, 1000.0])
def test_sound_speed_is_positive_and_below_c_over_sqrt3(redshift):
    speed = sound_speed(redshift, 3, math.pi / 2, 0.01)
    assert 0.0 < speed < C_KM_S / math.sqrt(3.0)


def test_zero_epsilon_recovers_one_reference_background_independent_of_level_and_angle():
    theta_star_a = theta_s(1, 0.0, 0.0)
    theta_star_b = theta_s(5, math.pi, 0.0)
    assert math.isclose(theta_star_a, theta_star_b, rel_tol=1e-13, abs_tol=1e-14)
    assert math.isclose(
        theta_star_a,
        0.010398277795403768,
        rel_tol=2e-9,
        abs_tol=1e-12,
    )


def test_peak_scaling_returns_baseline_at_control_theta_s():
    theta_star = theta_s(1, 0.0, 0.0)
    baseline = (220.6, 538.1, 809.8, 1147.8)
    actual = peak_positions(2, math.pi / 2, 0.0, theta_star, baseline)
    assert all(
        math.isclose(a, b, rel_tol=1e-13, abs_tol=1e-12)
        for a, b in zip(actual, baseline)
    )
