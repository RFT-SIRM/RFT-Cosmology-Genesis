# Results

## Reproducible computational results

GitHub Actions reports **6 passed** on this branch, including two regression-test functions for the exact remainder theorem.

Reference checks include:

- exact finite-level invariant expression;
- asymptotic limit \(I_\infty=-8/9\);
- finite-level remainder;
- coupling definition.

## Exact invariant theorem

The repository now documents an analytic derivation of the limit \(I_\infty(\theta)=-\frac{16}{9}\sin^2(\theta/2)\) and exact remainder \(I_m-I_\infty=-\frac{32}{9(3^m+1)}\sin^2(\theta/2)\). GitHub Actions reports six passing Python tests. The finite-level remainder identity and equivalent decomposition are machine-checked in Lean on [PR #2](https://github.com/RFT-SIRM/RFT-Cosmology-Genesis/pull/2); the limit operator itself is not yet formalized in Lean.

## Interpretation

The calculation demonstrates numerical behavior of the specified reduced model. It does not demonstrate that the phenomenological coupling exists in nature.

Previously reported values from the development calculation include a control angular sound scale near

`theta_* = 0.010398572693481`

for the specified reference setup. These values must be treated as model/reference outputs unless independently reproduced from the committed implementation.

## Observational status

No Planck, ACT, SPT, BAO, supernova, lensing, or joint likelihood fit is implemented in this repository.

A full observational constraint is therefore not claimed.
