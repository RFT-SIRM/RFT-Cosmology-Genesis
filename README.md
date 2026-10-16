# RFT-Cosmology-Genesis

[![CI](https://img.shields.io/github/actions/workflow/status/RFT-SIRM/RFT-Cosmology-Genesis/ci.yml?branch=main&style=for-the-badge&label=CI)](https://github.com/RFT-SIRM/RFT-Cosmology-Genesis/actions/workflows/ci.yml)
[![Status](https://img.shields.io/badge/status-phenomenological%20baseline-2563eb?style=for-the-badge)](./RESEARCH_STATUS.md)
[![Reproducibility](https://img.shields.io/badge/reproducibility-locked-16a34a?style=for-the-badge)](./RESULTS.md)
[![License](https://img.shields.io/badge/license-Apache%202.0-ea580c?style=for-the-badge)](./LICENSE)
[![Python](https://img.shields.io/badge/python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org)

## Purpose

`RFT-Cosmology-Genesis` records a reproducible **Pass-1 phenomenological** calculation that maps the intensive spectral invariant from the RFT mathematical line into an explicit photon-sector coupling ansatz and evaluates its **background / geometric** CMB response.

**This repository does not claim that the coupling is a physical cosmological interaction or that it explains the observed CMB.**

## Mathematical input

$$
I_m(\theta)=-16\frac{3^{m-1}+1}{3^{m+1}+3}\sin^2\!\left(\frac{\theta}{2}\right).
$$

At $\theta=\pi/2$:

$$
I_\infty=-\frac{8}{9}.
$$

Pass-1 coupling:

$$
q_m=1+\epsilon\,I_m.
$$

Implementation: [`src/model.py`](./src/model.py), [`src/cosmology.py`](./src/cosmology.py).

## Mathematical theorem

[![Exact remainder theorem](https://img.shields.io/badge/theorem-exact%20finite--level%20remainder-0f766e?style=for-the-badge)](./EXACT_INVARIANT_REMAINDER_THEOREM.md)

The invariant has an exact algebraic limit and finite-level remainder. The derivation, assumptions, and scope are documented in [Exact Invariant Remainder Theorem](./EXACT_INVARIANT_REMAINDER_THEOREM.md). This is an analytic theorem about the defined formula; it is **not** a claim of a machine-checked Lean proof or an observationally established cosmological law.

## Scientific status

| Layer | Location |
|-------|----------|
| Mathematical input | [`src/model.py`](./src/model.py) |
| Exact invariant theorem | [`EXACT_INVARIANT_REMAINDER_THEOREM.md`](./EXACT_INVARIANT_REMAINDER_THEOREM.md) |
| Phenomenological assumptions | [`MODEL_SPEC.md`](./MODEL_SPEC.md) |
| Numerical implementation | [`src/cosmology.py`](./src/cosmology.py) |
| Reference results | [`RESULTS.md`](./RESULTS.md) |
| Limitations | [`LIMITATIONS.md`](./LIMITATIONS.md) |
| Research status | [`RESEARCH_STATUS.md`](./RESEARCH_STATUS.md) |

Reference numerical agreement on control $\theta_*$: approximately $2.9\times10^{-15}$ (prior analysis; preserved as reference).

## Reproduction

    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
    python -m pytest -q

Previously recorded baseline: 4 passed. Two theorem-regression tests have been added on this branch; the new total awaits CI confirmation.

## Related repositories

- [Evgeny-Theorem](https://github.com/RFT-SIRM/Evgeny-Theorem)
- [RFT-QPU-Sierpinski](https://github.com/RFT-SIRM/RFT-QPU-Sierpinski)
- [RFT-Invariant-Battery.](https://github.com/RFT-SIRM/RFT-Invariant-Battery.)

## License

Apache-2.0 — see [`LICENSE`](./LICENSE).
