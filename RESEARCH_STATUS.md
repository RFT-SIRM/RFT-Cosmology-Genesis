# Research Status

**Status:** exploratory computational research with an exact H⁴ mathematical input and a reduced phenomenological cosmology layer.

The project separates source theorems, normalized spectral diagnostics, numerical implementation, and physical assumptions. A result in one layer is not evidence for a claim in another.

## Established mathematical input

- Evgeny's Theorem proves the SU(2) H⁴ trace defect for every refinement level $m\geq1$ and real angle.
- Dividing by the SU(2) Hilbert-space dimension $N_m=3^{m+1}+3$ gives the H⁴ invariant used here.
- This repository machine-checks the scalar finite-level remainder, exact decomposition, and convergence theorem in formalization/lean/CosmologyGenesis.lean.
- H⁶ and H⁸ have upstream Lean recurrence theorems plus exact symbolic finite base-transition certificates. Their normalized finite-level formulas, limits, and remainders are now implemented and regression-tested in src/spectral_moments.py.
- H¹⁰ in Evgeny's Theorem has an unconditional Lean recurrence for $m\geq4$ and an affine formula for $m\geq5$. Its exact coefficient remains a finite trace expression rather than an expanded trigonometric polynomial.
- Phi-Genesis has a separate scalar signed-Z₂ H¹⁰ line. A November 4 checkpoint records an all-level derivation, but it is not Lean-formalized and the public summary has not yet been reconciled with that checkpoint. See [SPECTRAL_MOMENT_DOSSIER.md](SPECTRAL_MOMENT_DOSSIER.md).

## Implemented computational layer

- H⁴ invariant and phenomenological coupling in src/model.py;
- reduced background expansion, sound horizon, comoving distance, acoustic scale, and scaled peak-position proxy in src/cosmology.py;
- normalized H⁶/H⁸ diagnostics and their exact algebraic finite-level remainders in src/spectral_moments.py;
- regression tests for invariant, higher-moment reference values, background normalization, sound-speed behavior, and the zero-coupling acoustic-scale control.

The local H⁴ Lean project does not import the upstream Evgeny-Theorem Lean package. Its scalar definition is separately formalized and linked to the upstream matrix theorem through the documented normalization.

## Not established

- a physical derivation of the photon-sector parameter $\epsilon$;
- a derivation of the ansatz $q_m=1+\epsilon I_m$ from a cosmological action or field equations;
- a full Boltzmann treatment of recombination, diffusion damping, and perturbation evolution;
- a TT/TE/EE likelihood or Bayesian posterior for $\epsilon$;
- observational evidence that the proposed coupling exists or explains the CMB;
- a justified physical coupling of H⁶, H⁸, or H¹⁰ to any cosmological sector.

## Required next scientific steps

1. Independently review the higher-moment proof boundaries and preserve the distinction between SU(2) and signed-Z₂ operators.
2. Derive or reject a physical mechanism for the H⁴ photon-sector ansatz; do not add higher-moment coupling coefficients without such a derivation.
3. Validate the reduced background calculations against a documented baseline.
4. Only then proceed to a full Boltzmann implementation and observational likelihood analysis.
