# RFT-Cosmology-Genesis

[![CI](https://github.com/RFT-SIRM/RFT-Cosmology-Genesis/actions/workflows/ci.yml/badge.svg)](https://github.com/RFT-SIRM/RFT-Cosmology-Genesis/actions/workflows/ci.yml)
[![Status](https://img.shields.io/badge/status-phenomenological%20baseline-blue)](./RESEARCH_STATUS.md)
[![Reproducibility](https://img.shields.io/badge/reproducibility-locked-green)](./RESULTS.md)
[![License](https://img.shields.io/badge/license-Apache--2.0-orange)](./LICENSE)

## Purpose

`RFT-Cosmology-Genesis` records a reproducible **Pass-1 phenomenological** calculation that maps the intensive spectral invariant from the RFT mathematical line into an explicit photon-sector coupling ansatz and evaluates its **background / geometric** CMB response.

**This repository does not claim that the coupling is a physical cosmological interaction or that it explains the observed CMB.**

## Mathematical input

\[
I_m(\theta)=-16\frac{3^{m-1}+1}{3^{m+1}+3}\sin^2\!\left(\frac{\theta}{2}\right).
\]

At \(\theta=\pi/2\):

\[
I_\infty=-\frac{8}{9}.
\]

Pass-1 coupling:

\[
q_m=1+\epsilon\,I_m.
\]

Implementation: `src/model.py` (invariant / coupling), `src/cosmology.py` (background integrals and peak mapping).

## Scientific status

| Layer | Location |
|-------|----------|
| Mathematical input | `src/model.py` |
| Phenomenological assumptions | `MODEL_SPEC.md` |
| Numerical implementation | `src/cosmology.py` |
| Reference results | `RESULTS.md` |
| Limitations | `LIMITATIONS.md` |
| Research status | `RESEARCH_STATUS.md` |

A prior analysis reported three independent numerical routes agreeing to approximately \(2.9\times10^{-15}\) on a control value of \(\theta_*\). That figure is preserved as a **reference result**, not silently relabeled as an independent reproduction in this repo.

## Reproduction

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m pytest -q
```

Expected: `4 passed`.

## Repository map

| Path | Role |
|------|------|
| `src/model.py` | invariant, limit, remainder, coupling |
| `src/cosmology.py` | H(z), sound horizon, theta_s, peak map |
| `tests/test_model.py` | locked unit tests |
| `MODEL_SPEC.md` | model specification |
| `RESULTS.md` | reference numbers |
| `LIMITATIONS.md` | what is not claimed |
| `EXPERT_REVIEW.md` | review notes |
| `.github/workflows/ci.yml` | CI |

## Related repositories

- [Evgeny-Theorem](https://github.com/RFT-SIRM/Evgeny-Theorem)
- [RFT-QPU-Sierpinski](https://github.com/RFT-SIRM/RFT-QPU-Sierpinski)
- [RFT-Invariant-Battery.](https://github.com/RFT-SIRM/RFT-Invariant-Battery.)

## License

Apache-2.0 — see `LICENSE`.
