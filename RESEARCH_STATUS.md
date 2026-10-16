# Research Status

Status: exploratory computational research.

The repository records a reduced phenomenological construction and its reproducible numerical implementation.

### Established within this repository

- the invariant formula is implemented;
- its \(\theta=\pi/2\) limit is implemented;
- the finite-level remainder is tested;
- the phenomenological coupling is tested;
- the cosmological response functions are implemented;
- the current theorem branch's six-test Python suite passes in GitHub Actions;

### Exact mathematical statement added

The analytic limit and exact finite-level remainder are stated and proved in [EXACT_INVARIANT_REMAINDER_THEOREM.md](EXACT_INVARIANT_REMAINDER_THEOREM.md). The six-test Python suite passes on this branch. The finite-level remainder identity and equivalent decomposition are machine-checked in Lean on [PR #2](https://github.com/RFT-SIRM/RFT-Cosmology-Genesis/pull/2); the limit operator itself is not yet formalized in Lean.

### Not established

The repository does not establish observational agreement with the CMB or a physical cosmological interaction.

### Required next step

A full Boltzmann implementation and likelihood analysis are required before observational conclusions can be drawn.
