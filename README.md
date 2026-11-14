# RFT-Cosmology-Genesis

[![CI](https://img.shields.io/github/actions/workflow/status/RFT-SIRM/RFT-Cosmology-Genesis/ci.yml?branch=main&style=for-the-badge&label=CI)](https://github.com/RFT-SIRM/RFT-Cosmology-Genesis/actions/workflows/ci.yml)
[![Status](https://img.shields.io/badge/status-phenomenological%20baseline-2563eb?style=for-the-badge)](./RESEARCH_STATUS.md)
[![Reproducibility](https://img.shields.io/badge/reproducibility-tracked-0f766e?style=for-the-badge)](./RESULTS.md)
[![License](https://img.shields.io/badge/license-Apache%202.0-ea580c?style=for-the-badge)](./LICENSE)
[![Python](https://img.shields.io/badge/python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org)

## Purpose

RFT-Cosmology-Genesis contains two deliberately separate research tracks:

1. **RFT Pass-1 phenomenological model.** It maps the intensive spectral invariant from the RFT mathematical line into a photon-sector coupling ansatz and evaluates a reduced **background / acoustic-scale** response.
2. **Exploratory standard-gravity Planck/CAMB diagnostics.** A separate external calculation compares a Lambda-CDM reference with fixed-zero-CDM trial points using Planck 2018 low-ell TT/EE, native Plik-lite TTTEEE, and native lensing likelihoods. Its numerical record is in [the Planck/CAMB research checkpoint](./research/PLANCK_CMB_CHECKPOINT_2026-11-13.md).

These tracks are not a single fitted model. The RFT photon-sector ansatz has not been implemented as a covariant perturbation model in CAMB or CLASS and has not been tested as a physical replacement for CDM. The zero-CDM optimizer has not produced a valid optimized minimum; its reported candidates and likelihood-domain studies remain exploratory. The Planck experiment uses native **Plik-lite**, not the full Planck Plik likelihood.

**No claim is made that the RFT coupling is a physical cosmological interaction, that it explains the observed CMB, or that dark matter has been disproved.** No Planck likelihood constraint on the RFT coupling parameter epsilon has been established.

## Mathematical input

$$
I_m(\theta)=-16\frac{3^{m-1}+1}{3^{m+1}+3}
\sin^2\!\left(\frac{\theta}{2}\right).
$$

At $\theta=\pi/2$,

$$
I_\infty=-\frac89.
$$

Pass-1 coupling:

$$
q_m=1+\epsilon I_m.
$$

Implementation: [src/model.py](./src/model.py), [src/cosmology.py](./src/cosmology.py).

## Mathematical theorem

[![Exact remainder theorem](https://img.shields.io/badge/theorem-exact%20finite--level%20remainder-0f766e?style=for-the-badge)](./EXACT_INVARIANT_REMAINDER_THEOREM.md)

The exact H⁴ trace defect originates in [Evgeny's Theorem](https://github.com/RFT-SIRM/Evgeny-Theorem/blob/main/THEOREM.md) and is machine-checked upstream for every $m\geq1$ and real angle. This repository independently formalizes the resulting scalar invariant, its exact finite-level remainder, decomposition, and convergence in [CosmologyGenesis.lean](./formalization/lean/CosmologyGenesis.lean). The local Lean project does not import the upstream operator formalization. The finite-level identity and convergence theorem are both already merged in main; [PR #2](https://github.com/RFT-SIRM/RFT-Cosmology-Genesis/pull/2) and [PR #3](https://github.com/RFT-SIRM/RFT-Cosmology-Genesis/pull/3) are historical introduction points, not open work.

## Spectral moment lineage

The H⁶ and H⁸ results from Evgeny's Theorem now have reproducible normalized finite-level formulas, exact limits, and exact remainders in [src/spectral_moments.py](./src/spectral_moments.py). The H¹⁰ recurrence is also Lean-proved upstream, with its exact coefficient retained as a finite trace expression.

[**Read the spectral moment dossier**](./SPECTRAL_MOMENT_DOSSIER.md)

The dossier also distinguishes the separate scalar signed-Z₂ H¹⁰ programme and Schur-boundary spectral work in Phi-Genesis. These are not interchangeable with the noncommutative SU(2) moments. No higher-moment term has been added to the cosmological coupling.

## Scientific status

| Layer | Location |
|---|---|
| H⁴ mathematical input | [src/model.py](./src/model.py) |
| Exact H⁴ theorem and remainder | [EXACT_INVARIANT_REMAINDER_THEOREM.md](./EXACT_INVARIANT_REMAINDER_THEOREM.md) |
| H⁶/H⁸ normalized diagnostics | [src/spectral_moments.py](./src/spectral_moments.py) |
| Cross-project proof boundaries | [SPECTRAL_MOMENT_DOSSIER.md](./SPECTRAL_MOMENT_DOSSIER.md) |
| Phenomenological assumptions | [MODEL_SPEC.md](./MODEL_SPEC.md) |
| Numerical implementation | [src/cosmology.py](./src/cosmology.py) |
| Reproducible results | [RESULTS.md](./RESULTS.md) |
| Limitations | [LIMITATIONS.md](./LIMITATIONS.md) |
| Research status | [RESEARCH_STATUS.md](./RESEARCH_STATUS.md) |
| Exploratory Planck/CAMB diagnostics | [research/PLANCK_CMB_CHECKPOINT_2026-11-13.md](./research/PLANCK_CMB_CHECKPOINT_2026-11-13.md) |

## Reproduction

    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
    python -m pytest -q

The Python CI workflow runs the complete pytest suite. The Lean workflow builds the scalar H⁴ formalization when Lean sources or its workflow change. See the latest [GitHub Actions runs](https://github.com/RFT-SIRM/RFT-Cosmology-Genesis/actions).

The external Planck/CAMB experiment is not reproduced by `pytest`: its YAML configurations, Planck data package, Python environment, and raw Cobaya logs are stored outside this repository. The checkpoint records the tested versions, likelihood definitions, numerical results, and limitations.

## Related repositories

- [Evgeny-Theorem](https://github.com/RFT-SIRM/Evgeny-Theorem)
- [Phi-Genesis](https://github.com/RFT-SIRM/Phi-Genesis)
- [RFT-QPU-Sierpinski](https://github.com/RFT-SIRM/RFT-QPU-Sierpinski)
- [RFT-Invariant-Battery.](https://github.com/RFT-SIRM/RFT-Invariant-Battery.)

## License

Apache-2.0 — see [LICENSE](./LICENSE).
