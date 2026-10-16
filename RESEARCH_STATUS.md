# Research Status

Status: exploratory computational research.

The repository records a reduced phenomenological construction and its reproducible numerical implementation.

### Established within this repository

- the invariant formula is implemented;
- its \(\theta=\pi/2\) limit is implemented;
- the finite-level remainder is tested;
- the phenomenological coupling is tested;
- the cosmological response functions are implemented;
- the six-test Python suite passes in GitHub Actions on `main`;

### Exact mathematical statement added

The analytic limit and exact finite-level remainder are stated and proved in [EXACT_INVARIANT_REMAINDER_THEOREM.md](EXACT_INVARIANT_REMAINDER_THEOREM.md). The six-test Python suite passes on `main`. The finite-level remainder identity and equivalent decomposition are machine-checked in Lean and merged via [PR #2](https://github.com/RFT-SIRM/RFT-Cosmology-Genesis/pull/2). The Lean convergence theorem is proposed in [PR #3](https://github.com/RFT-SIRM/RFT-Cosmology-Genesis/pull/3), and its Lean build and Python CI passed on theorem-code commit (`bca050c`); the subsequent documentation-only commit leaves the Lean source unchanged. It remains unmerged pending review.

### Not established

The repository does not establish observational agreement with the CMB or a physical cosmological interaction.

### Required next step

A full Boltzmann implementation and likelihood analysis are required before observational conclusions can be drawn.
