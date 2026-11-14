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


---

## 14. Session update — 2026-11-13 evening

This section supersedes the immediate "first task" in Section 13. It records the additional matched-accuracy Planck runs performed after the initial checkpoint. All results below are exploratory. No zero-CDM global minimum has been obtained.

### 14.1. Matched accuracy-0 Lambda-CDM control

A separate pair of Cobaya configurations was generated from the prior reference configuration. The preparation script confirmed byte-for-byte equivalent shared priors after YAML normalization, identical four likelihood components, and `lens_potential_accuracy = 0` for both models.

Run directory:

`~/Downloads/RFT-Planck-Runs/matched_accuracy0_20261113_195423/`

Configurations:

- `lcdm_accuracy0.yaml`
- `zero_cdm_accuracy0.yaml`
- later optimizer experiments: `zero_cdm_accuracy0_powell.yaml`, `zero_cdm_accuracy0_iminuit.yaml`

The Lambda control initialized and converged with Cobaya's BOBYQA minimizer:

| Parameter | Value |
|---|---:|
| \(H_0\) | 67.378533 |
| \(\Omega_bh^2\) | 0.022386 |
| \(\Omega_ch^2\) | 0.119961 |
| \(A_s\) | \(2.104359\times10^{-9}\) |
| \(n_s\) | 0.964929 |
| \(\tau\) | 0.055402 |
| \(A_{\rm planck}\) | 1.000802 |

- `minuslogpost = 481.302904`
- `chi2__CMB = 1013.292676`

Likelihood contributions:

| Component | \(\chi^2\) |
|---|---:|
| Planck low-\(\ell\) TT | 23.371598 |
| Planck low-\(\ell\) EE | 396.262456 |
| Plik-lite TTTEEE native | 584.941497 |
| Planck lensing native | 8.717125 |

This is the matched accuracy-0 control, not a publication-quality final fit. The same low-accuracy theory choice must be kept in mind when interpreting all comparisons below.

### 14.2. Explicit zero-CDM configuration

The zero-CDM YAML was checked directly:

`omch2 = 0.0`

The sampled parameters are:

`H0, ombh2, As, ns, tau, A_planck`

The neutrino assumptions remain standard and fixed:

- `mnu = 0.06 eV`
- `nnu = 3.046`

The common likelihood set remains:

- `planck_2018_lowl.TT`
- `planck_2018_lowl.EE`
- `planck_2018_highl_plik.TTTEEE_lite_native`
- `planck_2018_lensing.native`

The high-\(\ell\) likelihood is **native Plik-lite**, not the full original Planck Plik likelihood with its full nuisance-parameter model. Full Plik installation had not succeeded in the initial environment setup.

The CAMB setting remains:

`lens_potential_accuracy = 0`

This setting is deliberately matched between the Lambda-CDM and zero-CDM diagnostic runs. In the installed Cobaya/CAMB configuration, accuracy 0 also disables the nonlinear-source path previously observed at accuracy 1. It is not the final preferred theory accuracy for a publication-level result. Accuracy-1 zero-CDM runs have shown CAMB high-\(k\) extrapolation problems for some parameter points. Do not silently compare the two cosmologies using different theory settings.

### 14.3. Important diagnostic correction: finite-point handling

An early 16-point grid script used:

`make_finite=True`

Cobaya may replace non-finite likelihood/posterior values with finite penalty values in this mode. Therefore the early report "16/16 finite" is **not accepted as a raw-likelihood validity result**.

The correction was to repeat selected points with:

`make_finite=False`

Seven selected points were then evaluated directly and returned finite posterior and all four finite likelihood contributions. Subsequent scans recorded below also used `make_finite=False` and explicitly checked all four likelihoods plus finite `logpost`.

Do not reuse the earlier 16/16 statement as evidence that every point in that initial grid was a physically valid likelihood evaluation.

### 14.4. Zero-CDM direct-scan history

All rows below are **conditional grid/slice results**, not jointly optimized fits. Each scan fixed the parameters not explicitly varied. A best grid point is not a global minimum.

| Scan | Varied parameters and fixed context | Raw finite points | Best point in that scan | \(\chi^2_{\rm CMB}\) |
|---|---|---:|---|---:|
| Initial raw spot checks | selected \(H_0,\Omega_bh^2\) points at the original Lambda-like \(A_s,n_s,\tau\) | 7/7 | multiple test points | see terminal record |
| \(A_s\)-\(\tau\), coarse | \(H_0=99,\Omega_bh^2=0.039,n_s=0.964929,A_{\rm planck}=1.000802368\); \(6\times7\) grid | 23/42 | \(A_s=0.90\times10^{-9},\tau=0.16\) | 162,753.090 |
| \(A_s\)-\(\tau\), refine 1 | same fixed context; \(5\times4\) grid | 18/20 | \(A_s=0.95\times10^{-9},\tau=0.18\) | 162,635.444 |
| \(A_s\)-\(\tau\), refine 2 | same fixed context; \(5\times5\) grid | 25/25 | \(A_s=0.975\times10^{-9},\tau=0.19\) | 162,615.333 |
| \(H_0,\Omega_bh^2,n_s\) | \(A_s=0.975\times10^{-9},\tau=0.19,A_{\rm planck}=1.000802368\); \(3^3\) grid | 24/27 | \(H_0=99,\Omega_bh^2=0.036,n_s=0.99\) | 157,410.839 |
| Geometry/tilt coarse boundary | same fixed \(A_s,\tau,A_{\rm planck}\); \(H_0=98,99,99.8\), \(\Omega_bh^2=0.030,0.033,0.036\), \(n_s=0.99,1.04,1.09\) | 9/27 | \(H_0=99.8,\Omega_bh^2=0.030,n_s=0.99\) | 151,578.209 |
| Geometry/tilt near high \(H_0\) | same fixed \(A_s,\tau,A_{\rm planck}\); \(H_0=99,99.5,99.9\), \(\Omega_bh^2=0.020,0.025,0.030\), \(n_s=0.98,0.99,1.00\) | 27/27 | \(H_0=99.9,\Omega_bh^2=0.025,n_s=1.00\) | 147,645.007 |
| High-prior-edge scan | same fixed \(A_s,\tau,A_{\rm planck}\); \(H_0=99.5,99.9,99.99\), \(\Omega_bh^2=0.010,0.015,0.020,0.025\), \(n_s=1.00,1.02,1.04\) | 30/36 | \(H_0=99.99,\Omega_bh^2=0.020,n_s=1.02\) | 145,618.989 |
| \(A_s\)-\(\tau\) at high \(H_0\) | \(H_0=99.99,\Omega_bh^2=0.020,n_s=1.02,A_{\rm planck}=1.000802368\); \(5\times5\) grid | 15/25 | \(A_s=0.95\times10^{-9},\tau=0.19\) | 144,312.649 |
| \(A_s\)-\(\tau\), local refine | same fixed context; \(5\times5\) grid | 23/25 | \(A_s=0.9375\times10^{-9},\tau=0.205\) | 143,164.217 |
| \(A_s\)-\(\tau\), next refine | same fixed context; \(5\times5\) grid | 17/25 | \(A_s=0.9625\times10^{-9},\tau=0.225\) | 143,039.393 |
| \(A_s\)-\(\tau\), next refine | same fixed context; \(5\times5\) grid | 17/25 | \(A_s=0.9875\times10^{-9},\tau=0.24\) | 143,017.440 |
| \(H_0,\Omega_bh^2\), posterior-focused | \(A_s=0.9875\times10^{-9},n_s=1.02,\tau=0.24,A_{\rm planck}=1.001302368\); \(3\times5\) grid | 15/15 | \(H_0=99.9999,\Omega_bh^2=0.019\) | **142,929.394** |

Additional direct scans around \(A_s,\tau\) and \(n_s\) confirmed that the best points repeatedly lie close to the allowed upper boundary in \(H_0\), with elevated \(n_s\), high \(\tau\), and sub-Lambda values of \(A_s\). The grid outputs, rather than this summary table, remain the primary numerical record in the conversation.

#### Current best observed zero-CDM candidate

The best observed point by both likelihood \(\chi^2_{\rm CMB}\) and posterior among the supplied direct scans is the 15-point \(H_0,\Omega_bh^2\) scan:

| Parameter | Value |
|---|---:|
| \(H_0\) | 99.9999 |
| \(\Omega_bh^2\) | 0.019 |
| \(\Omega_ch^2\) | 0 (fixed) |
| \(A_s\) | \(0.9875\times10^{-9}\) |
| \(n_s\) | 1.02 |
| \(\tau\) | 0.240 |
| \(A_{\rm planck}\) | 1.001302368 |
| `minuslogpost` | 71,440.130664 |
| `chi2__CMB` from the four likelihoods | **142,929.393522** |

Likelihood contributions:

| Component | \(\chi^2\) |
|---|---:|
| Planck low-\(\ell\) TT | 165.496742 |
| Planck low-\(\ell\) EE | 435.096748 |
| Plik-lite TTTEEE native | 132,870.966945 |
| Planck lensing native | 9,457.833087 |
| **Total** | **142,929.393522** |

Plik-lite contributes about 92.96% of this total. The matched Lambda-CDM accuracy-0 control has \(\chi^2_{\rm CMB}=1013.292676\). The ratio of these two reported values is about 141.05, with a raw difference of about 141,916.10.

**Interpretation limit:** this is a best *observed conditional grid point*, not an optimized zero-CDM fit or a global minimum. It lies essentially at the upper prior boundary \(H_0=100\), and its \(n_s=1.02\), \(\tau=0.24\) are extreme relative to the Lambda-CDM control. The ratio and difference are not a calibrated exclusion significance, and no \(p\)-value or sigma exclusion may be inferred from them. The Lambda-CDM candidate is optimized; the zero-CDM point is not. This is not a like-for-like comparison of two independently established global minima.

### 14.5. Local parameter-displacement diagnostics

At the base point

- \(H_0=99.99\)
- \(\Omega_bh^2=0.020\)
- \(A_s=0.9875\times10^{-9}\)
- \(n_s=1.02\)
- \(\tau=0.240\)
- \(A_{\rm planck}=1.000802368\)

the direct evaluation gave:

- `minuslogpost = 71484.069859`
- `chi2__CMB = 143017.440290`

One-parameter displacements (all other parameters fixed) showed:

| Displacement | \(\Delta(-\log P)\) relative to base | Raw \(\chi^2_{\rm CMB}\) |
|---|---:|---:|
| \(H_0=99.8\) | +22.8255 | 143,063.091 |
| \(H_0=99.9\) | +10.9841 | 143,039.408 |
| \(\Omega_bh^2=0.019\) | -38.5783 | 142,940.284 |
| \(\Omega_bh^2=0.021\) | invalid | — |
| \(A_s=0.9625\times10^{-9}\) | invalid | — |
| \(A_s=1.0125\times10^{-9}\) | +112.6180 | 143,242.676 |
| \(n_s=1.01\) | +385.7683 | 143,788.977 |
| \(n_s=1.03\) | invalid | — |
| \(\tau=0.23\) | +78.0092 | 143,173.459 |
| \(\tau=0.25\) | +39.4911 | 143,096.422 |
| \(A_{\rm planck}=1.000302368\) | +1.0077 | 143,019.544 |
| \(A_{\rm planck}=1.001302368\) | -0.6713 | 143,015.929 |

This local displacement table was centered on the base point with \(A_{\rm planck}=1.000802368\); the later best-posterior scan used \(A_{\rm planck}=1.001302368\). Do not mix those two points.

The later \(H_0,\Omega_bh^2\) scan kept \(A_s,n_s,\tau,A_{\rm planck}\) at the values listed for the current best candidate and ranked all 15 valid points by Cobaya posterior. It produced \(H_0=99.9999,\Omega_bh^2=0.019\) as the best of that scan.

### 14.6. Optimizer attempts — no valid zero-CDM minimum yet

#### BOBYQA

The first zero-CDM BOBYQA run began from the Lambda-like point and failed after 13 evaluations:

- one or more low-\(\ell\) EE proposals were rejected as out of range;
- Py-BOBYQA reported exit flag \(-3\), singular interpolation linear system;
- no reproducible minimum was produced.

The printed `xmin = [0, 0, -1, 0, 0, 0]` is in the optimizer's internal transformed coordinates, not the physical cosmological parameters. The printed objective is not a valid minimum.

#### SciPy Powell

A separate `zero_cdm_accuracy0_powell.yaml` was created, starting from \(H_0=99,\Omega_bh^2=0.039\). Powell printed "Optimization terminated successfully", but the function value was the floating-point maximum (\(\sim1.79769\times10^{308}\)); many low-\(\ell\) EE points were rejected. Cobaya then recomputed the alleged minimum and obtained \(-\infty\), failing its reproducibility check. **This is a failed run, not a fit.**

#### iminuit / MIGRAD

Installed in the dedicated environment:

- `iminuit 2.33.0`
- installed by pip into `~/.venvs/rft-camb-2.0.5-py314`
- no repository dependency files were modified.

A separate `zero_cdm_accuracy0_iminuit.yaml` was created, starting at:

- \(H_0=99.99,\Omega_bh^2=0.020,A_s=0.9875\times10^{-9},n_s=1.02,\tau=0.24,A_{\rm planck}=1.000802368\).

Cobaya test initialization succeeded. MIGRAD computed a finite initial FCN of 71,484.06986, but during its first iteration Cobaya received NaN values for all six parameters and raised:

`Got non-finite parameter values: H0, ombh2, As, ns, tau, A_planck = nan`

No MIGRAD minimum was returned. This failure has not yet been diagnosed; do not label it as a physics result.

### 14.7. Current working interpretation

1. The standard-gravity, fixed-zero-CDM model can evaluate all four selected likelihoods at a substantial set of parameter points.
2. The optimizer failures are numerical/domain/parameterization failures; none yields a valid zero-CDM minimum.
3. Conditional grid search has reduced the fixed-point mismatch by more than an order of magnitude compared with the initial Lambda-like zero-CDM point. However, the best conditional point still has \(\chi^2_{\rm CMB}\approx1.4293\times10^5\), dominated by the Plik-lite high-\(\ell\) likelihood.
4. The current best candidate pushes \(H_0\) to the upper prior edge and uses extreme \(n_s\) and \(\tau\). This indicates tension with the model/data combination, but also demonstrates that the restricted model is trying to exploit prior boundaries. It must not be presented as a physically viable cosmological solution.
5. Because the zero-CDM point is not optimized, the large \(\Delta\chi^2\) versus the optimized Lambda-CDM control is only a diagnostic contrast, not an exclusion statistic.
6. The calculation uses accuracy-0 CAMB and native Plik-lite. It is not yet a definitive Planck likelihood analysis, and the result cannot disprove all dark matter, all non-baryonic matter, or dark energy.
7. The RFT photon-sector ansatz is not yet implemented as a covariant perturbation theory in CAMB or CLASS. It has not been tested as a physical replacement for CDM.

### 14.8. Handoff plan — ordered next actions

Do these in order. Do not skip directly to another broad optimizer run.

**A. Preserve and reproduce the current candidate**

1. Keep this checkpoint branch as the durable record. Do not modify local `main`, remote `main`, or PR #6.
2. In the same dedicated venv, directly re-evaluate the current best candidate with `make_finite=False`, `cached=False`, and all four likelihoods. Confirm the parameter values and \(\chi^2\) contributions in Section 14.4.
3. Repeat that exact point at least once in a fresh Cobaya model instance to check deterministic reproducibility.
4. Save the exact YAML, stdout/stderr, Python/Cobaya/CAMB/iminuit versions, and the terminal outputs under the existing run directory. Do not overwrite any earlier result files.

**B. Diagnose why both Powell and MIGRAD failed**

1. Inspect the installed Cobaya 3.6.2 source around `minuslogp_transf`, `affine_transform`, `inv_affine_transform`, the transformed bounds, and the iminuit call. Use the exact installed source, not assumptions based on generic Minuit examples.
2. Reproduce the current starting point and probe small positive/negative coordinate displacements in the same internal transformed parameterization. Check if NaNs arise from bound transforms, finite-penalty behavior for invalid likelihood points, or the likelihood itself.
3. Verify whether `A_planck`'s unbounded Gaussian prior and its affine transform contribute to the failure. Do not replace it by an arbitrary hard prior without a scientific justification.
4. Determine which low-\(\ell\) likelihood boundaries reject points as \(H_0,\Omega_bh^2,A_s,n_s,\tau\) move. The observed invalid points include low-EE and low-TT rejections; record each separately.
5. Do not accept an optimizer's "success" unless Cobaya's independent minimum reproduction succeeds and a direct raw likelihood evaluation reproduces the same finite result.

**C. Improve optimization only after the domain is mapped**

1. Keep the exact same data, likelihood set, theory settings, and physical priors for both models.
2. If rescaling a variable such as \(A_s\), preserve the intended prior exactly, including the Jacobian if changing variables. Do not silently replace a uniform prior in \(A_s\) by a uniform prior in \(\log A_s\).
3. Consider a staged fit only if fixed-parameter and subspace tests support it. A reduced fit that fixes nuisance/cosmological parameters must be labeled conditional, not full-model.
4. Try one minimizer configuration at a time. Store it under a fresh output prefix. First test initialization, then run once, then inspect the full result. Never launch multiple minimizers in parallel.
5. Require direct raw likelihood re-evaluation of any candidate and, ideally, independent starts before calling it a robust minimum.

**D. Upgrade the scientific comparison**

1. Resolve the CAMB high-\(k\) extrapolation/nonlinear-source issue for accuracy 1. Do not suppress extrapolation warnings or silently turn nonlinear corrections off in only one model.
2. Repeat matched Lambda-CDM and zero-CDM calculations at a defensible theory accuracy and quantify convergence against accuracy 0.
3. Obtain the full Planck Plik likelihood if the data/package can be reliably installed; retain Plik-lite results separately and label them accurately.
4. Cross-check the best spectra using an independent Boltzmann solver such as CLASS.
5. Compare actual \(C_\ell^{TT}\), \(C_\ell^{TE}\), and \(C_\ell^{EE}\) residuals, not only the scalar likelihood total. Identify which multipoles and spectra drive the large Plik-lite penalty.
6. Add independent observational constraints such as BAO and other suitable probes only after the CMB comparison is numerically stable. Check that extreme \(H_0,n_s,\tau\) solutions are consistent with the added data.
7. Calibrate model comparison statistically only after independently validated best fits exist. Since \(\Omega_ch^2=0\) is a boundary of the non-negative parameter space, do not apply an ordinary interior-parameter likelihood-ratio significance formula without checking its validity.

**E. Test RFT as a physical model rather than a label**

1. Derive a covariant background and perturbation framework with explicit conservation laws and degrees of freedom.
2. Derive the perturbation evolution and transfer functions required by a Boltzmann solver.
3. Implement the model in a solver or a verified external interface.
4. Fit its parameters against the same likelihoods and priors, with all nuisance treatments documented.
5. Compare predictive performance to Lambda-CDM on held-out or independent data where appropriate.

### 14.9. Exact environment and file handoff

Machine/environment previously reported:

- macOS 26.6, Apple Silicon arm64
- Python 3.14.2
- venv: `~/.venvs/rft-camb-2.0.5-py314`
- CAMB 2.0.5
- Cobaya 3.6.2
- iminuit 2.33.0 (installed during this session)
- NumPy 2.5.4, SciPy 1.18.1, GetDist 1.7.7
- `clipy` installed for native Planck likelihoods

Run directory:

`~/Downloads/RFT-Planck-Runs/matched_accuracy0_20261113_195423/`

Key files:

- `lcdm_accuracy0.yaml`
- `zero_cdm_accuracy0.yaml`
- `zero_cdm_accuracy0_powell.yaml`
- `zero_cdm_accuracy0_iminuit.yaml`

Earlier data and run directories remain:

- `~/Downloads/RFT-Planck-Packages/`
- `~/Downloads/RFT-Planck-Runs/`

All numerical run artifacts remain outside the Git repository. The commit associated with this update records the results and next-step plan; it does not include Planck data, local venv files, or raw Cobaya outputs.

### 14.10. Repository safety at this update

The documentation update is intended for the existing branch:

`research/planck-cmb-checkpoint-2026-11-13`

The branch had previously been verified as one commit ahead of remote `main`, zero commits behind, based on:

`739cff9d474913d00f5519b5e16d3ef592f9de57`

Only the checkpoint Markdown file was to be updated in that documentation commit. At that handoff, the branch had not yet been authorized for merging into `main`; that historical instruction is superseded by the user's later explicit request to review and merge the checkpoint after validation. PR #6 remains separate. Verify the branch comparison again after committing.

---

## 14.11. Session update — extended zero-CDM direct scans (2026-11-13, late session)

This section supersedes the "Current best observed zero-CDM candidate" in Section 14.4. Earlier scan rows and optimizer failures remain historical records; they are not deleted.

### Evaluation protocol

The subsequent calculations continued with the same matched accuracy-0 model:

- `omch2 = 0.0` (fixed).
- `lens_potential_accuracy = 0`.
- Likelihoods: low-\(\ell\) TT, low-\(\ell\) EE, native Plik-lite TTTEEE, and native Planck lensing.
- Direct calls used `make_finite=False` and `cached=False`.
- A point was accepted only if `logpost` and all four named likelihood contributions were finite.
- Points returning \(-\infty\), NaN, incomplete likelihood dictionaries, or exceptions were not ranked.

The recurring Cobaya warning that direct `get_model` evaluation ignores the `output` and `sampler` blocks is expected for these direct likelihood probes; the model theory and likelihood blocks were loaded.

### New best observed conditional grid point

The latest refinement varied \(\Omega_bh^2\), \(A_s\), and \(n_s\) on a \(3\times3\times3\) grid, holding the other parameters fixed. All 27 points had finite posterior and all four finite likelihood contributions.

| Parameter | Value |
|---|---:|
| \(H_0\) | 100.0 (upper prior boundary) |
| \(\Omega_bh^2\) | 0.01885 |
| \(\Omega_ch^2\) | 0 (fixed) |
| \(A_s\) | \(0.990\times10^{-9}\) |
| \(n_s\) | 1.026 |
| \(\tau\) | 0.24195 |
| \(A_{\rm planck}\) | 1.0008 |

- \(\text{minuslogpost} = 71202.824908506\)
- \(\chi^2_{\rm CMB} = 142454.950997361\)

Likelihood contributions:

| Component | \(\chi^2\) |
|---|---:|
| Planck low-\(\ell\) TT | 175.662245 |
| Planck low-\(\ell\) EE | 435.067184 |
| Native Plik-lite TTTEEE | 132375.342744 |
| Planck lensing native | 9468.878824 |
| **Total** | **142454.950997361** |

Within this 27-point grid, the five best points were:

| \(\Omega_bh^2\) | \(A_s/10^{-9}\) | \(n_s\) | \(-\log P\) | \(\chi^2_{\rm CMB}\) |
|---:|---:|---:|---:|---:|
| 0.01885 | 0.9900 | 1.02600 | 71202.824909 | 142454.950997 |
| 0.01875 | 0.9900 | 1.02600 | 71203.559371 | 142456.419922 |
| 0.01880 | 0.9900 | 1.02600 | 71203.622560 | 142456.546300 |
| 0.01885 | 0.9925 | 1.02600 | 71210.947472 | 142471.196125 |
| 0.01880 | 0.9925 | 1.02600 | 71212.217464 | 142473.736108 |

Relative to the best point from the immediately preceding 27-point grid \((-\log P=71213.302120083,\ \chi^2=142475.905420515)\), the improvement is 10.477211577 in \(-\log P\) and 20.954423154 in \(\chi^2\).

This is a best observed conditional grid point, **not** a jointly optimized fit and not a global minimum. It remains at the \(H_0\) prior boundary and uses elevated \(n_s\) and \(\tau\). The large Plik-lite contribution still dominates the total. The numerical ratio to the matched Lambda-CDM control is only a raw diagnostic contrast; it is not a calibrated exclusion significance because the zero-CDM point is not an optimized fit and the control/zero-CDM minima are not on equal footing.

### Other late-session scans

A \((\tau,A_{\rm planck})\) slice was examined with \(H_0=100\), \(\Omega_bh^2=0.019\), \(A_s=0.9875\times10^{-9}\), and \(n_s=1.025\) fixed:

- The initial 20-point scan had 6 finite points. Its best point was \(\tau=0.241\), \(A_{\rm planck}=1.001302368\), with \(-\log P=71239.141041945\) and \(\chi^2_{\rm CMB}=142527.414278255\).
- A subsequent \(6\times6\) refinement had 27/36 finite points. Its best point was \(\tau=0.24195\), \(A_{\rm planck}=1.0008\), with \(-\log P=71237.170675129\) and \(\chi^2_{\rm CMB}=142523.642530607\).

These are conditional slice results and do not beat the new grid point above. Their fixed parameter context differs from the later \((\Omega_bh^2,A_s,n_s)\) refinement.

The raw stdout of the latest 27-point scan was saved outside the repository at `~/Downloads/RFT-Planck-Runs/matched_accuracy0_20261113_195423/zero_cdm_grid_refinement_02.log` (77 lines, approximately 3.9 KB at the time of inspection). The repository checkpoint records the summary; the external log remains the detailed local terminal artifact.

### Updated optimizer status

No optimizer has yet returned a valid zero-CDM minimum:

- BOBYQA: failed (singular interpolation system / invalid domain probes).
- SciPy Powell: apparent termination at the maximum floating-point sentinel, then Cobaya's independent re-evaluation returned \(-\infty\); failed.
- iminuit 2.33.0 / MIGRAD: initialization succeeded and its initial objective was finite, but the first update generated NaN values for all six sampled parameters; failed.

The MIGRAD failure mechanism is still **unresolved**. Parameter-bound transformations, affine scaling, treatment of invalid likelihood points, and the unbounded Gaussian \(A_{\rm planck}\) prior are diagnostic hypotheses only; none has yet been established as the cause.

### Next actions from this point

1. Reproduce the new best grid point twice in fresh direct model instances with `make_finite=False,cached=False`, and save the full per-likelihood results.
2. Inspect the exact installed Cobaya 3.6.2 source for `affine_transform`, `inv_affine_transform`, `minuslogp_transf`, transformed bounds, and the call into iminuit. Record the source line numbers and code before proposing a change.
3. Probe the objective in the same transformed coordinates used by Cobaya, first at the candidate and then at small positive/negative coordinate displacements. Check both finite and invalid-domain evaluations.
4. Do not replace invalid likelihood values with the maximum-float sentinel. Use a finite, documented barrier/penalty only if it preserves the feasible-region objective and is validated against the raw likelihood; alternatively constrain the trial region so invalid proposals are never generated.
5. Only after those tests, run one bounded/staged optimizer configuration under a fresh output prefix. A staged fit must be labeled conditional if any parameters are fixed.
6. Directly re-evaluate any candidate minimum, check independent-start reproducibility, then expand the scientific comparison to matched higher theory accuracy, full Plik if available, spectra residuals, and independent data. No dark-matter exclusion claim is supported at this stage.

The current scientific status remains exploratory: the best observed zero-CDM grid point is not a global best fit, and no statistically calibrated model exclusion has been established.


---

## 14.12. Session update — reproducibility and MIGRAD diagnostics (2026-11-14 morning)

This update records new numerical checks performed in the existing local
environment. It supersedes no cosmological fit: no valid optimized zero-CDM
minimum has been obtained. All optimizer experiments below are diagnostic
and conditional.

### Reproduction of the best observed conditional grid point

The current best observed conditional grid point from Section 14.11 was
evaluated twice using fresh Cobaya model instances, with
`make_finite=False` and `cached=False`.

Environment:

- Cobaya 3.6.2
- CAMB 2.0.5
- NumPy 2.5.4
- SciPy 1.18.1
- Python 3.14 (arm64 environment)
- iminuit 2.33.0

Both independent evaluations returned exactly the same displayed values:

- `minuslogposterior = 71202.82490850563`
- `chi2__CMB = 142454.95099736075`
- difference between fresh model instances: `0.0`
- difference from the checkpoint value: approximately `-2.62e-10`

The individual likelihood-derived chi-squared contributions were:

| Component | `chi2` |
|---|---:|
| Planck low-\(\ell\) TT | 175.662245228572 |
| Planck low-\(\ell\) EE | 435.067184170785 |
| Native Plik-lite TTTEEE | 132375.342744373309 |
| Planck lensing native | 9468.878823588093 |
| **Total** | **142454.950997360750** |

The returned prior contribution was
`logpriors = 24.650590174739307`. Thus the difference between
\(\chi^2/2\) and the negative log-posterior is accounted for by the
reported prior contribution. This confirms deterministic reproducibility
of this point, not that it is an optimized or global minimum.

### Inspection of the installed Cobaya/iminuit transformations

The exact installed Cobaya 3.6.2 source was inspected. Its minimizer uses

\[
x_i = \frac{p_i-p_{i,0}}{s_i}
\]

and maps back with clipping to the physical parameter bounds. It passes
the transformed bounds to `iminuit.minimize`.

The installed iminuit 2.33.0 wrapper constructs
`Minuit(wrapped_fun, x0, grad=wrapped_grad)`, sets the limits, and sets
`m.errors` only when an explicit `options["eps"]` is supplied.

An important correction to the preliminary interpretation: the
documentation for the wrapper describes an `eps` option whose documented
default is 1, but Cobaya does not pass that option and the wrapper does not
assign it in this case. Direct inspection of the constructed Minuit object
showed the actual default step errors to be:

`[0.1, 0.1, 0.1, 0.1, 0.1, 0.1]`.

The transformed initial point is the origin. The transformed bounds and
available room on the positive side are:

| Parameter | Internal lower bound | Internal upper bound | Positive room from start |
|---|---:|---:|---:|
| \(H_0\) | -6.9270485297 | 0.001154700538 | 0.001154700538 |
| \(\Omega_bh^2\) | -2.9692299558 | 3.9589732744 | 3.9589732744 |
| \(A_s\) | -0.7505553499 | 6.1776478803 | 6.1776478803 |
| \(n_s\) | -3.8105117767 | 3.1176914536 | 3.1176914536 |
| \(\tau\) | -2.0170718265 | 4.9111314037 | 4.9111314037 |
| \(A_{\rm planck}\) | -26.7363001804 | 23.5268281801 | 23.5268281801 |

The initial Minuit step of 0.1 is about 86.60 times the available
positive internal room for \(H_0\). The other five parameters do not
have a comparable step-to-boundary ratio.

Small one-coordinate probes remained finite on both sides for all six
parameters. This rules out a non-finite objective at the starting point
or at those particular local probe points.

### MIGRAD step-size and fixed-\(H_0\) experiments

Two short six-parameter MIGRAD probes were compared:

- Default Minuit steps: all six `m.errors = 0.1`.
- Reduced \(H_0\) step: `eps = [0.0001, 0.1, 0.1, 0.1, 0.1, 0.1]`.

Both runs eventually produced non-finite internal coordinates. Reducing
the initial \(H_0\) step by a factor of 1000 did not resolve the failure.
The individual recorded finite objective evaluations do not establish
that the minimizer's internal state remained valid.

A further diagnostic fixed \(H_0=99.99\) in Minuit and left the other
five parameters free. This also failed. In that conditional run:

- The initial objective was finite:
  `71484.069858565563`.
- Calls 1–23 evaluated finite objective values.
- Calls 24 and 25 returned the maximum finite IEEE-754 double,
  approximately \(1.7976931348623157\times10^{308}\), at trial points
  with \(n_s\) close to or above the upper prior region.
- Call 26 returned a finite objective,
  `71457.638174474938`.
- Minuit then passed internal coordinates
  `[0, nan, nan, nan, nan, nan]` to the objective.

The maximum-double values are finite as floating-point numbers, but they
are penalty/sentinel-scale objective values and must not be interpreted as
valid likelihood evaluations. Fixing \(H_0\) did not prevent the NaN
failure, so the failure cannot be attributed solely to the \(H_0\)
boundary.

### Current interpretation and limits

The diagnostics establish:

1. The best observed conditional point is reproducible in two fresh
   Cobaya model instances.
2. The actual default Minuit step errors are 0.1, not 1.
3. The \(H_0\) internal upper bound is unusually close to the starting
   point, but reducing its initial step alone did not cure MIGRAD.
4. Fixing \(H_0\) also did not cure MIGRAD.
5. In the fixed-\(H_0\) run, maximum-double penalty-scale objective
   returns were observed immediately before Minuit generated NaN
   coordinates.

The sequence in item 5 makes the handling of invalid trial points and
very large penalty values a priority for further investigation. It does
**not** yet prove that the sentinel values are the sole cause of the NaNs:
the internal Minuit state, gradient/Hessian updates, parameter limits,
and likelihood-domain transitions still need to be isolated.

No zero-CDM optimizer result is accepted as a minimum. No likelihood
component or physical model has been changed. The accuracy-0/native
Plik-lite limitations and all scientific interpretation limits from
Sections 14.11 and earlier remain in force.

### Logs retained outside the repository

The following raw logs remain in the local run directory and are
intentionally not committed:

- `candidate_reproduction_20261114_081708.log`
- `cobaya_transform_source_20261114_082312.log`
- `migrad_affine_probe_20261114_082844.log`
- `migrad_step_comparison_20261114_083521.log`
- `migrad_fixed_H0_probe_20261114_083655.log`

Directory:

`~/Downloads/RFT-Planck-Runs/matched_accuracy0_20261113_195423/`

No Planck data, virtual-environment files, raw logs, YAML experiment
configurations, or source-code changes are included in this documentation
update.

### Diagnostic actions recorded before Section 14.13

**Status update (2026-11-14, Section 14.13):** actions 1 and 2 below have been completed. Raw replay with `make_finite=False` identified native `planck_2018_lowl.TT` as the rejecting component at FCN24 and FCN25; the multipole-domain violations and conditional `n_s` boundary are recorded in Section 14.13. Action 3 is partly resolved: the raw `-inf` likelihood and the later non-finite Minuit coordinates have been distinguished, but the precise cause of Minuit's NaN proposal remains open. Actions 4 and 5 remain future work.

1. Trace the exact Cobaya code path that converts invalid posterior or
   likelihood evaluations into the maximum-double objective value.
2. Re-evaluate the two recorded invalid trial points with raw
   `make_finite=False` likelihood calls and identify which likelihood
   component rejects each point.
3. Instrument the objective boundary to distinguish a non-finite physical
   likelihood, a finite penalty sentinel, and a non-finite internal
   Minuit coordinate.
4. Only after identifying that path, test a numerically safe treatment
   of invalid trial points or a feasible-domain parameterization. Do not
   alter physical priors or silently cap objective values.
5. Re-run one optimizer experiment at a time and accept a minimum only
   after Cobaya's independent recomputation and direct likelihood
   reevaluation agree.

The current status remains exploratory: the conditional point is
reproducible, but a valid optimized zero-CDM fit and a statistically
calibrated model comparison remain unresolved.


---
## 14.13. Session update — native low-ell TT domain and MIGRAD diagnosis (2026-11-14)

This update records the raw-likelihood replay and the fixed-parameter
spectral-domain scan performed after Section 14.12. It diagnoses the
maximum-float objective values seen in the fixed-H0 MIGRAD experiment.
It does not produce a zero-CDM fit and does not modify any prior,
likelihood, theory setting, or physical model.

### Environment and configuration

The calculations used the existing external environment:

- Python 3.14.2
- CAMB 2.0.5
- Cobaya 3.6.2
- iminuit 2.33.0
- NumPy 2.5.4
- SciPy 1.18.1
- pytest 9.2.0

The tested configuration was
`zero_cdm_accuracy0_iminuit.yaml` in
`~/Downloads/RFT-Planck-Runs/matched_accuracy0_20261113_195423/`.
It fixes `omch2 = 0`, uses `lens_potential_accuracy = 0`, and includes
native Planck low-ell TT, low-ell EE, Plik-lite TTTEEE, and lensing.

The repository was on `main` at `8a2c928`; the worktree was clean.
The local repository test suite passed: **58 passed**.

### Installed low-ell TT rejection rule

The installed implementation was inspected in:

`cobaya/likelihoods/planck_2018_lowl/TT.py`

For each multipole from ell = 2 through ell = 29, it forms the calibrated
theory spectrum and checks it against the stored spline bounds. The
likelihood returns `-inf` if any value falls below its lower bound or above
its upper bound. Only after that check does it evaluate the Gaussianizing
spline derivative; a negative derivative also returns `-inf`.

The order of these checks matters. A derivative sampled outside the
permitted spline interval is not an independent explanation of the
rejection: the actual likelihood exits at the preceding bounds check.

### Raw replay of MIGRAD trial points

The two maximum-float trial points were re-evaluated with
`make_finite = False` and `cached = False`. The prior and CAMB theory
calculation were finite in both cases. Low-ell EE, Plik-lite TTTEEE,
and lensing were also finite. The low-ell TT component alone returned
`-inf`.

| Trial | n_s | Raw log-prior | Low-ell TT | TT domain result |
|---|---:|---:|---:|---|
| FCN24 | 1.199769401717 | 24.444700071804 | `-inf` | 18 of 28 multipoles below lower bounds |
| FCN25 | 1.034092220841 | 24.643710486001 | `-inf` | only ell = 15 below its lower bound |
| FCN26 control | 1.020707608396 | 24.649967157091 | -85.878233388549 | all 28 multipoles inside bounds |

At FCN24, the multipoles below their lower spline bounds were:

`5, 7, 9, 10, 11, 12, 14, 15, 17, 18, 19, 23, 24, 25, 26, 27, 28, 29`.

The smallest lower-bound margin was approximately `-182.3947415`
at ell = 15. The theory values themselves were finite; no upper-bound
violation or non-finite C_l was found.

At FCN25, the only violation was:

| Quantity | Value |
|---|---:|
| ell | 15 |
| Theory D_15^TT after calibration | 372.5417141618 |
| Native TT lower spline bound | 386.8925568207 |
| Margin | -14.3508426589 |

At FCN26, all multipoles passed the domain check. The closest point was
again ell = 15, with a positive margin of `4.285950904695`.

For FCN24 and FCN25, the other three log-likelihood components remained
finite. Therefore the raw posterior rejection at these two points is
directly attributable to the native low-ell TT spline-domain check, not
to the prior, a failed CAMB call, or the other three likelihoods.

### Conditional n_s boundary at fixed FCN26 parameters

A one-dimensional scan varied only `n_s`; all other parameters were held
at their FCN26 values:

| Parameter | Fixed value |
|---|---:|
| H0 | 99.99 |
| ombh2 | 0.01999994830543 |
| As | 9.874936082854e-10 |
| tau | 0.2400036089221 |
| A_planck | 1.000804852608 |
| omch2 | 0 (fixed) |

A 17-point scan bracketed the first domain transition between:

- in-domain: `n_s = 1.02321722322944`
- out-of-domain: `n_s = 1.02405376150725`

Bisection refinement gave the conditional boundary:

`n_s* = 1.02374434007214`, controlled by the lower spline bound at
ell = 15.

At this boundary the calibrated theory value at ell = 15 equals the
lower bound, approximately `386.8925568207`. The one-sided checks were:

| n_s | ell = 15 lower-bound margin | Native TT log-likelihood |
|---:|---:|---:|
| 1.02374424007214 | +0.000140336123 | -88.876818635622 |
| 1.02374444007214 | -0.000140336076 | `-inf` |

This is a **conditional numerical support boundary** for the installed
native low-ell TT likelihood with the other five parameters fixed as
listed. It is not a universal upper limit on n_s, not a prior bound, not
a physical exclusion, and not a likelihood boundary mapped over the full
six-dimensional parameter space.

### What this establishes about MIGRAD — and what remains open

Established:

1. The maximum-float objective values in the fixed-H0 MIGRAD trial
   correspond to raw posterior evaluations of `-inf`.
2. In the two replayed trials, the rejection is caused by the native
   low-ell TT spline lower bounds.
3. FCN25 fails because of a single low-ell TT multipole, ell = 15.
4. FCN24 fails at 18 multipoles.
5. A small change in n_s across the conditional FCN26 boundary is
   sufficient to change the native TT likelihood from finite to `-inf`.

Not established:

1. Why Minuit subsequently generated non-finite internal coordinates.
   The invalid likelihood evaluations precede that event, but this
   sequence alone does not prove that the maximum-float penalty is its
   sole cause.
2. The feasible region when n_s, H0, ombh2, As, tau, and A_planck vary
   together.
3. A valid optimized zero-CDM minimum.
4. A statistically calibrated exclusion of zero CDM.
5. Any constraint on the RFT photon-sector coupling epsilon.

The 12 negative spline derivatives reported by the separate diagnostic
for FCN24 were evaluated at theory values already outside the allowed
spline bounds. They are not counted as an additional likelihood failure
mechanism because the installed likelihood returns at the earlier
bounds check.

### Raw local artifacts

The following diagnostic outputs remain outside Git in
`~/Downloads/RFT-Planck-Runs/matched_accuracy0_20261113_195423/`:

- `migrad_step_comparison_20261114_083521.log`
- `migrad_fixed_H0_probe_20261114_083655.log`
- `migrad_affine_probe_20261114_082844.log`
- `migrad_raw_replay_20261114.log`
- `lowl_tt_domain_diagnostic_20261114.log`
- `lowl_tt_ns_boundary_20261114.log`

Planck data, local virtual-environment files, YAML configurations, and
raw logs are not included in the repository.

### Ordered next work

1. Map the feasible low-ell TT region in coupled slices, starting with
   `(n_s, ombh2)` around the FCN26 point while holding the other
   parameters fixed. Accept points only after raw `make_finite=False`
   evaluation and explicit inspection of all four likelihoods.
2. Extend the slice to `As` and `tau` only after the first two-dimensional
   map is understood. Keep the original priors, CAMB settings, and
   likelihood implementation unchanged.
3. Separate the native TT support boundary from the low-ell EE support
   boundary; do not combine them into one generic "invalid point" label.
4. Only then test a constrained or staged optimizer. Any fixed-parameter
   stage must be labelled conditional, and every candidate must be
   independently re-evaluated with raw likelihoods.
5. Keep the unresolved Minuit NaN transition as a separate numerical
   issue until a direct reproduction identifies its cause.

No likelihood boundary was widened, no invalid likelihood was replaced
with a hand-chosen finite value, and no optimizer result was promoted
to a fitted cosmological minimum.
