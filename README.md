# RFT-Cosmology-Genesis

![CI](https://github.com/RFT-SIRM/RFT-Cosmology-Genesis/actions/workflows/ci.yml/badge.svg)
![Status](https://img.shields.io/badge/status-phenomenological%20baseline-blue)
![Reproducibility](https://img.shields.io/badge/reproducibility-locked-green)
![License](https://img.shields.io/badge/license-Apache--2.0-orange)

## Purpose

`RFT-Cosmology-Genesis` records a reproducible Pass-1 phenomenological calculation that maps the intensive invariant used by the RFT mathematical work into an explicit photon-sector coupling ansatz and evaluates its background/geometric CMB response.

**This repository does not claim that the coupling is a physical cosmological interaction or that it explains the observed CMB.**

## Model

\[
I_m(\theta)=-16\frac{3^{m-1}+1}{3^{m+1}+3}\sin^2(\theta/2).
\]

At \(\theta=\pi/2\):

\[
I_\infty=-8/9.
\]

The Pass-1 coupling is

\[
q_m=1+\epsilon I_m.
\]

The resulting background, sound horizon, distance, angular sound scale, and fixed-phase acoustic multipole mapping are implemented in `src/`.

## Scientific status

The repository separates:

- mathematical input;
- phenomenological assumptions;
- numerical implementation;
- reference results;
- limitations;
- future observational tests.

The supplied prior analysis reports three independent numerical routes agreeing to approximately `2.9e-15` in the control value of `theta_*`. That result is preserved as a reference result and is not silently relabeled as an independent reproduction.

## Reproduction

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest -q

### Команда 8 — CI + лицензия

```bash
cat > .github/workflows/ci.yml <<'EOF'
name: CI

on:
  push:
  pull_request:

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.11"
      - run: python -m pip install --upgrade pip
      - run: pip install -r requirements.txt
      - run: pytest -q
