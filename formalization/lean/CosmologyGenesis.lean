import Mathlib

/-!
# Cosmology-Genesis: exact invariant remainder

This file formalizes an algebraic identity for the invariant defined in the
Python model. It does not formalize a physical interaction or observational
claim. The index is assumed positive because the source formula uses m - 1.
-/

noncomputable def rftInvariant (m : ℕ) (θ : ℝ) : ℝ :=
  -16 * (((3 : ℝ) ^ (m - 1) + 1) / ((3 : ℝ) ^ (m + 1) + 3)) *
    Real.sin (θ / 2) ^ 2

theorem rftInvariant_remainder
    (m : ℕ) (hm : 1 ≤ m) (θ : ℝ) :
    rftInvariant m θ + (16 / 9) * Real.sin (θ / 2) ^ 2 =
      -(32 / (9 * ((3 : ℝ) ^ m + 1))) * Real.sin (θ / 2) ^ 2 := by
  have hm0 : m - 1 + 1 = m := by omega
  have hpow : (3 : ℝ) ^ (m - 1) * 3 = (3 : ℝ) ^ m := by
    rw [← pow_succ, hm0]
  have hden : (3 : ℝ) ^ (m + 1) + 3 =
      3 * ((3 : ℝ) ^ m + 1) := by
    rw [pow_succ]
    ring
  have hnum : (3 : ℝ) ^ (m - 1) + 1 =
      ((3 : ℝ) ^ m + 3) / 3 := by
    rw [← hpow]
    ring
  have hnonzero : (3 : ℝ) ^ m + 1 ≠ 0 := by
    positivity
  unfold rftInvariant
  rw [hnum, hden]
  field_simp [hnonzero]
  ring

theorem rftInvariant_exact_decomposition
    (m : ℕ) (hm : 1 ≤ m) (θ : ℝ) :
    rftInvariant m θ =
      -(16 / 9) * Real.sin (θ / 2) ^ 2
        - (32 / (9 * ((3 : ℝ) ^ m + 1))) * Real.sin (θ / 2) ^ 2 := by
  have h := rftInvariant_remainder m hm θ
  linarith
