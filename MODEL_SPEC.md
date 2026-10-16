# Model Specification

## Scope

This repository implements a reduced phenomenological model connecting the RFT invariant to a multiplicative photon-sector coupling.

## Invariant

$$
I_m(\theta)=-16\frac{3^{m-1}+1}{3^{m+1}+3}\sin^2\!\left(\frac{\theta}{2}\right).
$$

For $\theta=\pi/2$:

$$
I_m=-8\frac{3^{m-1}+1}{3^{m+1}+3},\qquad\lim_{m\to\infty}I_m=-\frac{8}{9}.
$$

Remainder:

$$
I_m+\frac{8}{9}=-\frac{16}{9(3^m+1)}.
$$

## Exact limit and finite-level remainder

For every integer \(m\geq1\) and real \(\theta\), the invariant defined above satisfies

\[
I_\infty(\theta):=\lim_{m\to\infty} I_m(\theta)
=-\frac{16}{9}\sin^2\!\left(\frac{\theta}{2}\right),
\]

and the exact remainder identity

\[
I_m(\theta)-I_\infty(\theta)
=-\frac{32}{9(3^m+1)}\sin^2\!\left(\frac{\theta}{2}\right).
\]

At \(\theta=\pi/2\), this reduces to the special case already recorded above. A derivation is given in [Exact Invariant Remainder Theorem](EXACT_INVARIANT_REMAINDER_THEOREM.md). The finite-level remainder identity and equivalent decomposition are machine-checked in Lean in [PR #2](https://github.com/RFT-SIRM/RFT-Cosmology-Genesis/pull/2); the limit operator itself is not yet formalized in Lean.

## Phenomenological coupling

$$
q_m=1+\epsilon\,I_m.
$$

The parameter $\epsilon$ is phenomenological. This repository does not establish a physical origin for it.

## Background response

$$
H_m^2(z)=H_0^2\big[\Omega_m(1+z)^3+(\Omega_\nu+q_m\Omega_\gamma)(1+z)^4+\Omega_{\Lambda,m}\big],
$$

$$
\Omega_{\Lambda,m}=1-\Omega_m-\Omega_\nu-q_m\Omega_\gamma.
$$

Angular scale: $\theta_{s,m}=r_{s,m}/\chi_m$.

## What is locked

- analytic $I_m(\theta)$ and $I_\infty=-8/9$
- definition of $q_m$
- unit tests on the invariant layer

## What is not claimed

- physical origin of $\epsilon$
- explanation of the observed CMB
- experimental validation
