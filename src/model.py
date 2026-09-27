import math


def invariant(m: int, theta: float) -> float:
    if m < 1:
        raise ValueError("m must be >= 1")
    return -16.0 * (3 ** (m - 1) + 1) / (3 ** (m + 1) + 3) * math.sin(theta / 2) ** 2


def invariant_pi_over_2(m: int) -> float:
    return -8.0 * (3 ** (m - 1) + 1) / (3 ** (m + 1) + 3)


def invariant_limit() -> float:
    return -8.0 / 9.0


def coupling(m: int, theta: float, epsilon: float) -> float:
    return 1.0 + epsilon * invariant(m, theta)


def invariant_remainder_pi_over_2(m: int) -> float:
    return invariant_pi_over_2(m) - invariant_limit()
