import Mathlib

open Filter

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

/-- The finite-level invariant converges to its exact algebraic limit.
We index levels by m + 1 so every term uses a positive level without
natural-number subtraction. This is a mathematical limit of the defined
formula, not a physical or observational claim. -/
theorem rftInvariant_tendsto (θ : ℝ) :
    Tendsto (fun m : ℕ => rftInvariant (m + 1) θ) atTop
      (nhds (-(16 / 9) * Real.sin (θ / 2) ^ 2)) := by
  have hpow : Tendsto (fun m : ℕ => (3 : ℝ) ^ m) atTop atTop :=
    tendsto_pow_atTop_atTop_of_one_lt (by norm_num : (1 : ℝ) < 3)
  have hshift : Tendsto (fun m : ℕ => m + 1) atTop atTop :=
    tendsto_atTop_add_const_right _ 1 tendsto_id
  have hpowShift : Tendsto (fun m : ℕ => (3 : ℝ) ^ (m + 1)) atTop atTop :=
    hpow.comp hshift
  have hdenAdd : Tendsto (fun m : ℕ => (3 : ℝ) ^ (m + 1) + 1) atTop atTop :=
    tendsto_atTop_add_const_right _ 1 hpowShift
  have hden : Tendsto (fun m : ℕ => 9 * ((3 : ℝ) ^ (m + 1) + 1)) atTop atTop :=
    hdenAdd.const_mul_atTop (by norm_num : (0 : ℝ) < 9)
  have hcoef : Tendsto
      (fun m : ℕ => -(32 : ℝ) / (9 * ((3 : ℝ) ^ (m + 1) + 1)))
      atTop (nhds 0) := by
    simpa [div_eq_mul_inv, mul_comm] using
      (tendsto_const_nhds (x := (-32 : ℝ))).mul
        (tendsto_inv_atTop_zero.comp hden)
  let s : ℝ := Real.sin (θ / 2) ^ 2
  have hrem : Tendsto
      (fun m : ℕ => (-(32 : ℝ) / (9 * ((3 : ℝ) ^ (m + 1) + 1))) * s)
      atTop (nhds 0) := by
    simpa using hcoef.mul (tendsto_const_nhds (x := s))
  have hdecomp : (fun m : ℕ => rftInvariant (m + 1) θ) =
      fun m => (-(16 / 9) * s) +
        (-(32 : ℝ) / (9 * ((3 : ℝ) ^ (m + 1) + 1))) * s := by
    funext m
    rw [rftInvariant_exact_decomposition (m + 1) (by omega) θ]
    dsimp [s]
    ring
  rw [hdecomp]
  simpa [s] using (tendsto_const_nhds (x := -(16 / 9) * s)).add hrem
