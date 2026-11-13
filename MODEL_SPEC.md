# Model Specification

## Scope

This repository implements a reduced phenomenological model connecting the RFT H⁴ spectral invariant to a multiplicative photon-sector coupling. The model is a background/acoustic-scale calculation, not a full Boltzmann solver.

## Invariant

$$
I_m(\theta)=-16\frac{3^{m-1}+1}{3^{m+1}+3}
\sin^2\!\left(\frac{\theta}{2}\right).
$$

For $\theta=\pi/2$,

$$
I_m=-8\frac{3^{m-1}+1}{3^{m+1}+3},
\qquad
\lim_{m\to\infty}I_m=-\frac89.
$$

Remainder:

$$
I_m+\frac89=-\frac{16}{9(3^m+1)}.
$$

## Exact limit and finite-level remainder

For every integer $m\geq1$ and real $\theta$, the invariant defined above satisfies

$$
I_\infty(\theta):=\lim_{m\to\infty} I_m(\theta)
=-\frac{16}{9}\sin^2\!\left(\frac{\theta}{2}\right),
$$

and the exact remainder identity

$$
I_m(\theta)-I_\infty(\theta)
=-\frac{32}{9(3^m+1)}\sin^2\!\left(\frac{\theta}{2}\right).
$$

At $\theta=\pi/2$, this reduces to the special case already recorded above. A derivation is given in [Exact Invariant Remainder Theorem](EXACT_INVARIANT_REMAINDER_THEOREM.md). The finite-level remainder identity, equivalent decomposition, and convergence theorem are all in main and machine-checked in [CosmologyGenesis.lean](formalization/lean/CosmologyGenesis.lean). The source H⁴ matrix theorem is independently machine-checked in [Evgeny's Theorem](https://github.com/RFT-SIRM/Evgeny-Theorem/blob/main/formalization/EvgenyTheorem/TildeEntries.lean). The local Lean project formalizes the scalar invariant and does not import the upstream operator project.

## Higher spectral moments

The SU(2) H⁶ and H⁸ trace defects have all-angle recurrence theorems plus exact symbolic finite base-transition certificates. Their normalized finite-level formulas, limits, and remainders are implemented in [src/spectral_moments.py](src/spectral_moments.py). The SU(2) H¹⁰ recurrence and affine form are also unconditional Lean theorems upstream, but the exact coefficient remains in finite trace-expression form.

The separate scalar signed-Z₂ H¹⁰ experiment in Phi-Genesis is a different operator with a different proof boundary. See [Spectral Moment Dossier](SPECTRAL_MOMENT_DOSSIER.md).

**Only H⁴ currently enters the phenomenological cosmological coupling.** H⁶, H⁸, and H¹⁰ are retained as independent spectral diagnostics; this repository does not assign them physical coupling constants.

## Phenomenological coupling

$$
q_m=1+\epsilon I_m.
$$

The parameter $\epsilon$ is phenomenological. This repository does not establish a physical origin for it.

## Background response

$$
H_m^2(z)=H_0^2\left[
\Omega_m(1+z)^3+
(\Omega_\nu+q_m\Omega_\gamma)(1+z)^4+
\Omega_{\Lambda,m}\right],
$$

$$
\Omega_{\Lambda,m}=1-\Omega_m-\Omega_\nu-q_m\Omega_\gamma.
$$

Angular scale: $\theta_{s,m}=r_{s,m}/\chi_m$.

## What is implemented and tested

- analytic H⁴ invariant, exact limit, and finite-level remainder;
- H⁶/H⁸ normalized trace-defect formulas and their exact finite-level remainders;
- definition of $q_m$ and present-day background closure;
- sound-speed, sound-horizon, comoving-distance, and acoustic-scale functions;
- baseline and higher-moment regression tests.

## What is not claimed

- physical origin of $\epsilon$;
- explanation of the observed CMB;
- full TT/TE/EE spectrum or likelihood fit;
- experimental validation;
- a physical coupling of H⁶, H⁸, or H¹⁰.
