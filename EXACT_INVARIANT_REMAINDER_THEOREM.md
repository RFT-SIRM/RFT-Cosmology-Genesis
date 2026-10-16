# Exact Invariant Remainder Theorem

[![Mathematical status](https://img.shields.io/badge/math-exact%20algebraic%20identity-0f766e?style=for-the-badge)](./MODEL_SPEC.md)
[![Verification](https://img.shields.io/badge/verification-symbolic%20derivation%20%2B%20tests-2563eb?style=for-the-badge)](./RESULTS.md)
[![Physical interpretation](https://img.shields.io/badge/physical%20claim-not%20established-d97706?style=for-the-badge)](./LIMITATIONS.md)

## Statement

For every integer \(m\geq1\) and real angle \(\theta\), define

\[
I_m(\theta)=-16\frac{3^{m-1}+1}{3^{m+1}+3}
\sin^2\!\left(\frac{\theta}{2}\right).
\]

Then the exact finite-level remainder relative to its limit is

\[
\boxed{
I_m(\theta)-I_\infty(\theta)
=-\frac{32}{9(3^m+1)}
\sin^2\!\left(\frac{\theta}{2}\right)
}
\]

where

\[
\boxed{
I_\infty(\theta):=\lim_{m\to\infty}I_m(\theta)
=-\frac{16}{9}\sin^2\!\left(\frac{\theta}{2}\right).
}
\]

In particular, at \(\theta=\pi/2\),

\[
I_\infty(\pi/2)=-\frac89,
\qquad
I_m(\pi/2)+\frac89=-\frac{16}{9(3^m+1)}.
\]

## Proof

Write \(s^2=\sin^2(\theta/2)\). Since

\[
3^{m-1}+1=\frac{3^m+3}{3},
\qquad
3^{m+1}+3=3(3^m+1),
\]

the defining expression becomes

\[
\begin{aligned}
I_m(\theta)
&=-\frac{16(3^m+3)}{9(3^m+1)}s^2\\
&=-\frac{16}{9}\left(1+\frac{2}{3^m+1}\right)s^2\\
&=-\frac{16}{9}s^2-\frac{32}{9(3^m+1)}s^2.
\end{aligned}
\]

Because \(3^m+1\to\infty\), the second term tends to zero. This proves the limit and the exact remainder identity. Substituting \(\sin^2(\pi/4)=1/2\) gives the stated special case. \(\square\)

## Consequence for the phenomenological coupling

For a fixed finite parameter \(\epsilon\), define

\[
q_m(\theta)=1+\epsilon I_m(\theta).
\]

The algebraic limit is therefore

\[
q_\infty(\theta)=1-\frac{16\epsilon}{9}
\sin^2\!\left(\frac{\theta}{2}\right),
\]

and its finite-level remainder is

\[
q_m(\theta)-q_\infty(\theta)
=-\frac{32\epsilon}{9(3^m+1)}
\sin^2\!\left(\frac{\theta}{2}\right).
\]

This consequence follows only from the stated definition of \(q_m\); it does not establish a physical origin for \(\epsilon\).

## Verification boundary

- The proof above is an exact algebraic derivation from the repository's stated invariant.
- The Python tests check representative finite levels and angles; tests are computational checks, not a substitute for the displayed proof.
- A Lean formalization of the exact finite-level remainder identity and equivalent decomposition is available in [PR #2](https://github.com/RFT-SIRM/RFT-Cosmology-Genesis/pull/2), in `formalization/lean/CosmologyGenesis.lean`. GitHub Actions successfully built the `CosmologyGenesis` target on that branch. PR #2 remains open and unmerged, so the formalization is proposed and machine-checked in its PR branch, not yet part of `main`.
- The Lean file proves the algebraic remainder identity and exact decomposition. It does not yet formalize the limit operator itself or establish any physical cosmology claim.
- The result is not a theorem about the observed CMB, dark matter, dark energy, or a physical interaction. Those claims require independent model derivation and observational testing.
- The document records the mathematical claim and its scope; it does not itself establish legal novelty, patentability, priority, or ownership. The repository's Apache-2.0 license remains applicable to material covered by it.

## Reproduction

Run:

```bash
python -m pytest -q
```

See [model specification](MODEL_SPEC.md), [results](RESULTS.md), [limitations](LIMITATIONS.md), and [research status](RESEARCH_STATUS.md).
