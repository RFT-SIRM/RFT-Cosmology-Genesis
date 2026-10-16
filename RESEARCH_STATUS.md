# Research Status

Status: exploratory computational research.

The repository records a reduced phenomenological construction and its reproducible numerical implementation.

### Established within this repository

- the invariant formula is implemented;
- its \(\theta=\pi/2\) limit is implemented;
- the finite-level remainder is tested;
- the phenomenological coupling is tested;
- the cosmological response functions are implemented;
- the previously committed test suite was recorded as passing; the new regression tests are awaiting CI confirmation;

### Exact mathematical statement added

The analytic limit and exact finite-level remainder are now stated and proved in [EXACT_INVARIANT_REMAINDER_THEOREM.md](EXACT_INVARIANT_REMAINDER_THEOREM.md). Python regression tests were added for representative levels and angles. This statement is **not** represented as Lean-formalized; machine verification would require a separate Lean development and successful build.

### Not established

The repository does not establish observational agreement with the CMB or a physical cosmological interaction.

### Required next step

A full Boltzmann implementation and likelihood analysis are required before observational conclusions can be drawn.
