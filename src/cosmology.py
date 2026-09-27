import math
from scipy.integrate import quad

C_KM_S = 299792.458

OMEGA_B_H2 = 0.02237
OMEGA_C_H2 = 0.1200
H0 = 67.36
N_EFF = 3.046
Z_STAR = 1089.92

OMEGA_M = (OMEGA_B_H2 + OMEGA_C_H2) / (H0 / 100.0) ** 2
OMEGA_B = OMEGA_B_H2 / (H0 / 100.0) ** 2

# Radiation density convention used by the Pass-1 calculation.
OMEGA_GAMMA = 2.469e-5 / (H0 / 100.0) ** 2
OMEGA_NU = OMEGA_GAMMA * 0.22710731766 * N_EFF


def q_m(m: int, theta: float, epsilon: float) -> float:
    from .model import invariant
    return 1.0 + epsilon * invariant(m, theta)


def omega_lambda(m: int, theta: float, epsilon: float) -> float:
    q = q_m(m, theta, epsilon)
    return 1.0 - OMEGA_M - OMEGA_NU - q * OMEGA_GAMMA


def E(z: float, m: int, theta: float, epsilon: float) -> float:
    q = q_m(m, theta, epsilon)
    ol = omega_lambda(m, theta, epsilon)
    value = (
        OMEGA_M * (1.0 + z) ** 3
        + (OMEGA_NU + q * OMEGA_GAMMA) * (1.0 + z) ** 4
        + ol
    )
    return math.sqrt(value)


def H(z: float, m: int, theta: float, epsilon: float) -> float:
    return H0 * E(z, m, theta, epsilon)


def R(z: float, m: int, theta: float, epsilon: float) -> float:
    q = q_m(m, theta, epsilon)
    return 3.0 * OMEGA_B / (4.0 * q * OMEGA_GAMMA * (1.0 + z))


def sound_speed(z: float, m: int, theta: float, epsilon: float) -> float:
    return C_KM_S / math.sqrt(3.0 * (1.0 + R(z, m, theta, epsilon)))


def sound_horizon(m: int, theta: float, epsilon: float) -> float:
    f = lambda z: sound_speed(z, m, theta, epsilon) / H(z, m, theta, epsilon)
    return quad(f, Z_STAR, math.inf, epsabs=1e-10, epsrel=1e-10, limit=500)[0]


def comoving_distance(m: int, theta: float, epsilon: float) -> float:
    f = lambda z: C_KM_S / H(z, m, theta, epsilon)
    return quad(f, 0.0, Z_STAR, epsabs=1e-9, epsrel=1e-10, limit=500)[0]


def theta_s(m: int, theta: float, epsilon: float) -> float:
    return sound_horizon(m, theta, epsilon) / comoving_distance(m, theta, epsilon)


def peak_positions(
    m: int,
    theta: float,
    epsilon: float,
    baseline_theta_s: float,
    baseline_peaks=(220.6, 538.1, 809.8, 1147.8),
):
    scale = baseline_theta_s / theta_s(m, theta, epsilon)
    return tuple(p * scale for p in baseline_peaks)
