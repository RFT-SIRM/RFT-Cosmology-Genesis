# Planck/CAMB Research Checkpoint — 2026-11-13

Status: exploratory numerical research.
This document records local computational results and their limitations.
It does not claim a detection, exclusion, or replacement of dark matter.

## 1. Purpose and scientific scope

This checkpoint preserves the current state of the Planck CMB investigation
so that subsequent work can continue without repeating completed checks.

The experiments compare:

1. A standard Lambda-CDM reference model.
2. Standard gravity with cold dark matter density fixed to zero.
3. Numerical variants of the CAMB lensing/non-linear calculation.

The zero-CDM experiment retains standard massive neutrinos:
`mnu = 0.06 eV`, `nnu = 3.046`.

It is therefore a test of removing cold dark matter (CDM), not a test
of removing every non-baryonic matter component.

The RFT photon-sector ansatz in this repository is still phenomenological.
No covariant perturbation equations, transfer functions, or physical
replacement for CDM have yet been implemented in CAMB or CLASS.

No conclusion that dark matter has been disproved is supported by this
checkpoint.

## 2. Repository and Git state at checkpoint creation

Repository: `RFT-SIRM/RFT-Cosmology-Genesis`

Observed local checkout before checkpoint:

- Local branch: `main`
- Local HEAD: `10648912b67586ae68a13c5c75f42d762a7b49a4`
- Remote `origin/main`: `739cff9d474913d00f5519b5e16d3ef592f9de57`
- Local main was 41 commits behind origin/main.
- Local main working tree was clean.

Separate PR #6 reference:

- PR head: `6d24e7cfb6190fc9605a949ca455ddfd2fbdfc89`
- Subject: integrate normalized higher-moment spectral diagnostics.
- PR #6 is separate from the Planck investigation.
- No review submissions or inline review threads were present at the
  time of the audit.
- The PR's local Python test run reported 58 passed.
- GitHub Actions runs for that PR head were previously observed successful.

The checkpoint is deliberately based on the audited remote `main`,
not on the stale local `main` and not on PR #6.

## 3. External computational environment

Machine:

- macOS 26.6
- Apple Silicon, arm64
- Python 3.14.2

Separate Python environment:

`~/.venvs/rft-camb-2.0.5-py314`

Packages:

- CAMB 2.0.5
- Cobaya 3.6.2
- NumPy 2.5.4
- SciPy 1.18.1
- GetDist 1.7.7
- clipy installed for native Planck likelihood support

Planck data package directory:

`~/Downloads/RFT-Planck-Packages`

The directory occupied approximately 58 MB at the time of the check.

Installed and evaluated likelihood components:

- `planck_2018_lowl.TT`
- `planck_2018_lowl.EE`
- `planck_2018_highl_plik.TTTEEE_lite_native`
- `planck_2018_lensing.native`

The high-frequency likelihood used here is the native Plik-lite variant.
It is not the full original Plik likelihood with its full nuisance parameter
set. Attempts to install the full likelihood did not complete successfully:
the archive endpoint returned a short non-archive response.

Cobaya successfully loaded CAMB from the existing Python wheel when
configured with `path: global`. Do not ask Cobaya to compile another CAMB
from source unless there is a specific reason.

The Planck runs were performed outside the repository. The environment,
downloaded data, YAML configurations, and raw output files have not yet
been packaged into a self-contained reproducibility bundle in Git.

## 4. Likelihood configuration

Common likelihood set:

- Planck low-ell TT
- Planck low-ell EE
- Planck high-ell Plik-lite TTTEEE native
- Planck 2018 native lensing

The main Lambda-CDM and zero-CDM comparisons used:

- CAMB theory, loaded globally
- `lens_potential_accuracy: 1` unless stated otherwise
- `mnu = 0.06`
- `nnu = 3.046`

For the optimized Lambda-CDM model, physical priors were:

| Parameter | Prior |
|---|---:|
| H0 | [40, 100] |
| ombh2 | [0.005, 0.040] |
| omch2 | [0, 0.5] |
| As | [5e-10, 5e-9] |
| ns | [0.8, 1.2] |
| tau | [0.01, 0.8] |

The Planck calibration parameter was:

`A_planck ~ Normal(loc=1.0, scale=0.0025)`

This calibration prior was explicitly checked and preserved in the
targeted Lambda-CDM refinement.

## 5. Best reproduced Lambda-CDM candidate

The best reproduced point found so far is:

| Parameter | Value |
|---|---:|
| H0 | 67.38743318 |
| ombh2 | 0.02238656669 |
| omch2 | 0.1199286798 |
| As | 2.104661429e-9 |
| ns | 0.9649573953 |
| tau | 0.05538225096 |
| A_planck | 1.000802224 |
| mnu | 0.06 |
| nnu | 3.046 |

Independent reevaluation with the same four likelihood components gave:

`minuslogposterior = 480.557313418801`

`chi2__CMB = 1011.801531412812`

Likelihood contributions:

| Component | log-likelihood |
|---|---:|
| Planck lowl TT | -11.695325492630 |
| Planck lowl EE | -198.128174890915 |
| Planck Plik-lite TTTEEE | -291.694922201996 |
| Planck lensing native | -4.382343120865 |

Cobaya's derived `chi2__CMB` in these runs is consistent with
`-2 * sum(loglikes)` for the listed likelihood components.

Important distinction:

- `chi2__CMB` is the likelihood-derived comparison quantity used here.
- The `chi-sq` text in Cobaya's `.minimum` output is not the same quantity:
  it is twice the minimized negative log-posterior and includes the prior
  contribution according to the optimizer's objective.

The candidate was obtained by one targeted BOBYQA run started exactly
from a previously identified local minimum, with:

- `max_evals = 5000`
- `rhoend = 1e-7`
- one starting point

Its posterior and likelihood were independently reevaluated using the
same model and priors. The difference from the previous local candidate was:

- `delta minuslogposterior = -0.016559651696`
- `delta chi2__CMB = -0.033082333592`

This is the best reproduced candidate found so far, not a proof of a
global minimum. Earlier multi-start searches exhibited non-negligible
spread among local minima.

Previously recorded best minima:

| Search | Starts | Best minuslogposterior |
|---|---:|---:|
| Pilot | 2 | 480.590275 |
| Refined | 3 | 480.964326 |
| Local | 6 | 480.573873 |
| Tight | 8 | 480.695312 |
| Targeted from Local | 1 | 480.557313 |

The one-start targeted result should not be described as a globally
validated fit.

## 6. Initial CAMB fixed-parameter smoke test

A fixed-parameter CAMB smoke test produced:

| Model | 100 theta_star | Age [Gyr] |
|---|---:|---:|
| CDM reference | 1.041127395 | 13.796856 |
| Zero CDM, other inputs fixed | 0.716601427 | 21.508912 |

This was a fixed-input diagnostic, not a parameter fit or likelihood
comparison. It should not be confused with the later Cobaya results.

## 7. Zero-CDM fixed-point likelihood results

At the best reproduced Lambda-CDM cosmological parameters, CDM was set
to zero while the other cosmological inputs were kept fixed.

With `lens_potential_accuracy = 1`:

`chi2__CMB = 2009653.1619018477`

Likelihood contributions:

| Component | log-likelihood |
|---|---:|
| Planck lowl TT | -56.1487894722 |
| Planck lowl EE | -198.6557065968 |
| Planck Plik-lite TTTEEE | -1003649.3647954802 |
| Planck lensing native | -922.4116593746 |

All four likelihoods returned finite values at this fixed point.
The dominant mismatch was in the high-ell Plik-lite component.

This is a fixed-parameter diagnostic, not an optimized zero-CDM fit.

A corresponding run with `lens_potential_accuracy = 0` gave:

`chi2__CMB = 2009767.4318740780`

Again, this is not an optimized fit.

For comparison, the Lambda-CDM reference point gave:

| CAMB option | Lambda-CDM chi2__CMB |
|---|---:|
| `lens_potential_accuracy = 1` | 1011.8015314128 |
| `lens_potential_accuracy = 0` | 1013.3482243351 |

The difference in Lambda-CDM alone is approximately 1.547.
For zero CDM, changing the option changed the fixed-point chi2 by
approximately 114.270.

Therefore, do not compare a zero-CDM result computed with
`lens_potential_accuracy = 0` against a Lambda-CDM result computed with
`lens_potential_accuracy = 1` as though they were generated with identical
theory settings.

## 8. CAMB high-k extrapolation problem

For zero CDM with a lower baryon density:

`ombh2 = 0.015`

and `lens_potential_accuracy = 1`, CAMB raised:

`MatterPowerData_k: cannot extrapolate rising high-k matter power tail
from k/h=7.7907 to requested k/h=100.00`

The same error occurred in each isolated Planck likelihood because all
components depend on the same CAMB theory calculation.

For the same low-baryon point with `lens_potential_accuracy = 0`,
the calculation completed, but:

`chi2__CMB = 2550377.5428053988`

This large value is also only a fixed-point diagnostic.

Observed CAMB wrapper state:

| Option | non_linear_sources |
|---|---|
| `lens_potential_accuracy = 1` | True |
| `lens_potential_accuracy = 0` | False |

CAMB documentation describes `nonlinear` as an option of
`set_for_lmax`; when left as `None`, its default behavior is tied to
`lens_potential_accuracy`. See:

- https://camb.readthedocs.io/en/latest/model.html
- https://camb.readthedocs.io/en/latest/nonlinear.html
- https://github.com/CobayaSampler/cobaya/blob/master/cobaya/theories/camb/camb.py

Do not silently disable nonlinear lensing corrections only for zero CDM.
Any approximation change must be applied consistently to both models
and its effect on the predicted spectra must be quantified.

## 9. Zero-CDM optimizer failure

An eight-start BOBYQA run with very broad initial reference distributions
did not yield a valid minimum.

Observed symptoms:

- some low-ell EE proposals were rejected as out of range;
- several evaluations caused CAMB high-k extrapolation errors;
- Py-BOBYQA reported overflow warnings;
- multiple runs failed with singular interpolation linear systems;
- Cobaya eventually reported `-inf` / the maximum floating-point sentinel
  and could not reproduce the minimum.

That run must be treated as failed. It produced no usable optimized
zero-CDM likelihood result.

A fixed-point scan returned finite likelihoods for 4 of 8 tested points.
A high-H0 point produced invalid low-EE multipoles; some low-baryon points
caused the CAMB high-k error under the nonlinear-source setting.

No statistical conclusion about the best achievable zero-CDM fit can be
drawn from the failed optimizer run.

## 10. Current scientific conclusions

Supported by the calculations:

1. The installed CAMB/Cobaya/Planck-lite environment can evaluate all four
   likelihood components for the reproduced Lambda-CDM point.
2. A fixed zero-CDM point using the same cosmological parameters as the
   Lambda-CDM candidate produces an extremely poor Plik-lite likelihood.
3. Some zero-CDM parameter combinations trigger CAMB high-k extrapolation
   errors or invalid low-ell likelihood inputs.
4. `lens_potential_accuracy` materially affects both the CAMB nonlinear
   source handling and the resulting likelihood.

Not established:

1. A successful best fit for zero CDM.
2. A global Lambda-CDM minimum.
3. A statistically calibrated exclusion significance for zero CDM.
4. A full Plik (non-lite) Planck comparison.
5. An ACT, SPT, DESI BAO, supernova, or joint likelihood comparison.
6. A physical RFT replacement for the gravitational role of CDM.
7. Any claim that dark matter or dark energy has been disproved.

## 11. Required next steps

1. Diagnose the CAMB high-k request and nonlinear-source behavior at
   zero CDM. Do not suppress the error by arbitrary extrapolation.
2. Test equivalent CAMB theory settings for Lambda-CDM and zero CDM.
   Quantify the effect of linear versus nonlinear lensing on both.
3. Reparameterize the primordial amplitude using a numerically sensible
   variable such as `logA = ln(1e10 As)` if appropriate, preserving the
   same physical prior on As.
4. Find a finite, physically defensible region of zero-CDM parameter
   space before attempting another multi-start minimization.
5. Obtain a valid optimized zero-CDM likelihood and independently
   reevaluate the saved minimum.
6. Compare the same data, likelihood implementation, nuisance treatment,
   and theory accuracy across the two models.
7. Calibrate the statistical comparison, taking account of the fact that
   zero CDM is a boundary point of the non-negative CDM parameter space.
8. Cross-check important results with an independent Boltzmann solver
   such as CLASS before making strong claims.
9. Derive a consistent RFT perturbation framework before attempting
   to represent the RFT photon-sector ansatz as a physical alternative
   cosmology.

## 12. Local artifacts and execution paths

The observed local run files are under:

`~/Downloads/RFT-Planck-Runs/`

Relevant files include:

- `lcdm_local_seeded.yaml`
- `lcdm_local_seeded.minimum`
- `lcdm_local_seeded.minimum.txt`
- `lcdm_tight.yaml`
- `zero_cdm_pilot.yaml`

Planck data:

`~/Downloads/RFT-Planck-Packages/`

Python environment:

`~/.venvs/rft-camb-2.0.5-py314/`

These are local external artifacts, not committed inputs. A future
reproduction bundle should include sanitized YAML files, package/version
manifests, commands, and checksums for downloaded data where licensing
permits.

## 13. Session handoff

Resume from this checkpoint.

Do not repeat the successful CAMB installation, Planck-native likelihood
installation, or the initial four-likelihood initialization unless the
environment changes.

First task: diagnose and test CAMB nonlinear/high-k behavior for zero CDM
with matched Lambda-CDM controls.

Do not launch another broad zero-CDM BOBYQA run until the finite theory
domain and likelihood behavior are understood.

Do not modify the physical model or claim a dark-matter exclusion based
on fixed-parameter diagnostics.

Keep the Planck research log separate from PR #6. The next repository
change should remain documentation-first unless a reproducible code
change is fully tested.
