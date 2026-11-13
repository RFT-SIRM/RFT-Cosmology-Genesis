# Results

## Reproducible computational results

The Python workflow runs the full pytest suite. It now covers:

- H⁴ invariant and exact remainder regression checks;
- H⁶/H⁸ finite-level trace-defect references from Evgeny's Theorem;
- exact normalized H⁶/H⁸ limit-plus-remainder identities;
- background closure and $H(0)=H_0$;
- inverse-$q_m$ scaling of the baryon-photon ratio;
- sound-speed bounds and the zero-coupling acoustic-scale control.

See [GitHub Actions](https://github.com/RFT-SIRM/RFT-Cosmology-Genesis/actions) for the run associated with a particular commit.

## Exact H⁴ invariant theorem

The exact algebraic limit is

$$
I_\infty(\theta)=-\frac{16}{9}\sin^2(\theta/2),
$$

with exact remainder

$$
I_m-I_\infty
=-\frac{32}{9(3^m+1)}\sin^2(\theta/2).
$$

The finite-level remainder, exact decomposition, and convergence theorem are machine-checked in the local Lean project. The upstream matrix trace identity is machine-checked in Evgeny's Theorem. These are mathematical statements about the defined operators and scalar invariant; they do not establish a cosmological interaction.

## Normalized higher-moment diagnostics

The normalized H⁶ and H⁸ formulas are implemented in src/spectral_moments.py. Their finite-level values at $\theta=\pi/2$, levels 2–4, match the reference trace-defect values recorded in the upstream Evgeny-Theorem/docs/HIGHER_MOMENTS.md. Their exact limits and finite-level remainders are checked by algebraic regression tests.

For H¹⁰, Evgeny's Theorem proves an unconditional affine recurrence from level 5. After division by $N_m=3^{m+1}+3$, its limit and remainder are known in terms of the exact level-five trace coefficient. That coefficient is not yet expanded into a trigonometric polynomial and is deliberately not duplicated as an invented formula here.

The scalar signed-Z₂ H¹⁰ calculation in Phi-Genesis is a separate operator. Its November 4 checkpoint records an all-level derivation that is not Lean-formalized; the published higher-moment summary remains conservative pending reconciliation and independent review. See [SPECTRAL_MOMENT_DOSSIER.md](SPECTRAL_MOMENT_DOSSIER.md).

## Acoustic-scale baseline audit

With the committed constants and $\epsilon=0$, the model is independent of $m$ and $\theta$. Direct evaluation of the committed integration formulas gives

$$
r_s=144.47524851266485,\qquad
\chi=13894.151642738916,
$$

$$
\theta_s=0.010398277795403768.
$$

The previous archival value 0.010398572693481 is not reproduced by this zero-coupling control. The difference is approximately $2.94898\times10^{-7}$, or 28.36 ppm relative to the current result. The earlier note did not record enough parameter/provenance detail to identify its origin, so it is retained only as an unverified historical reference. The current implementation value is now pinned by a regression test.

## Interpretation and observational status

The calculation demonstrates numerical behavior of a specified reduced phenomenological model. It does not demonstrate that the photon-sector coupling exists in nature.

No full Boltzmann treatment or Planck, ACT, SPT, BAO, supernova, lensing, or joint likelihood fit is implemented. No observational detection or constraint on $\epsilon$ is claimed.
