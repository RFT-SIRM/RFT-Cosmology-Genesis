# Model Specification

## Scope

This repository implements a reduced phenomenological model connecting the RFT invariant to a multiplicative photon-sector coupling.

## Invariant

For the model used here,

\[
I_m(\theta)=
-16\frac{3^{m-1}+1}{3^{m+1}+3}
\sin^2\left(\frac{\theta}{2}\right).
\]

For \(\theta=\pi/2\),

\[
I_m=-8\frac{3^{m-1}+1}{3^{m+1}+3},
\qquad
\lim_{m\to\infty}I_m=-\frac89.
\]

The finite-level remainder is

\[
I_m+\frac89=-\frac{16}{9(3^m+1)}.
\]

## Phenomenological coupling

The implemented ansatz is

\[
q_m=1+\epsilon I_m.
\]

The parameter \(\epsilon\) is phenomenological. This repository does not establish a physical origin for it.

## Cosmological calculation

The code evaluates the resulting reduced background quantities and derives:

- sound horizon;
- comoving distance;
- angular sound scale;
- fixed-phase acoustic multipole rescaling.

The acoustic peak calculation uses the supplied baseline multipoles as reference inputs. It is therefore a response calculation, not a full CMB parameter fit.

## Numerical scope

This model is not a replacement for a Boltzmann code. Recombination, full perturbation evolution, polarization, lensing, neutrino anisotropic stress, parameter covariance, and likelihood evaluation are outside the present implementation.
