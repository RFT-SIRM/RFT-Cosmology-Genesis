# Spectral moment lineage and the cosmology boundary

**Purpose.** This dossier connects the spectral results already present in Evgeny's Theorem and Phi-Genesis to the reduced cosmological model in this repository. It records the mathematical objects and their proof boundaries. It does not promote a spectral calculation to a physical interaction.

## 1. Common operator dimension and normalization

For the Sierpiński-gasket graph at refinement level $m$,

$$
|V_m|=\frac{3^{m+1}+3}{2}.
$$

The SU(2)-valued operator acts on a two-component state at each graph vertex, so its Hilbert-space dimension is

$$
N_m=2|V_m|=3^{m+1}+3.
$$

In Evgeny's Theorem, the p-th trace defect compares the face-axis configuration with the fixed-Z commuting control. For $p=6,8,10$, the Lean definitions defectO6, defectO8, and defectO10 are evaluated in the standard numbering orientation oNum. Below, $D_m^{(p)}(\theta)$ denotes that orientation-specific trace defect. It is not a generic statement about every possible vertex ordering.

## 2. H⁴: the exact input already used by Cosmology-Genesis

Evgeny's Theorem proves, for every $m\geq1$ and real $\theta$,

$$
\Delta_m^{(4)}(\theta)
=-16(3^{m-1}+1)\sin^2\!\left(\frac{\theta}{2}\right).
$$

The theorem is EvgenyTheorem.traceDefect_closed in the upstream Lean formalization. Dividing by $N_m$ gives the invariant used here:

$$
I_m(\theta)=\frac{\Delta_m^{(4)}(\theta)}{N_m}
=-16\frac{3^{m-1}+1}{3^{m+1}+3}
\sin^2\!\left(\frac{\theta}{2}\right).
$$

Its exact limit and finite-level remainder are

$$
I_\infty(\theta)=-\frac{16}{9}\sin^2\!\left(\frac{\theta}{2}\right),
\qquad
I_m-I_\infty
=-\frac{32}{9(3^m+1)}\sin^2\!\left(\frac{\theta}{2}\right).
$$

Cosmology-Genesis has its own Lean definition of this scalar formula and machine-checks the remainder, decomposition, and convergence. It does **not** import the upstream Evgeny-Theorem Lean package or re-prove the construction of the full SU(2) graph operator. The source theorem and the local scalar formalization are therefore linked, but remain separate Lean projects.

Sources: [Evgeny's theorem statement](https://github.com/RFT-SIRM/Evgeny-Theorem/blob/main/THEOREM.md), [upstream Lean proof guide](https://github.com/RFT-SIRM/Evgeny-Theorem/blob/main/formalization/README.md), [local Lean file](formalization/lean/CosmologyGenesis.lean).

## 3. H⁶ and H⁸: exact all-angle normalized limits

The upstream note [Higher spectral moments](https://github.com/RFT-SIRM/Evgeny-Theorem/blob/main/docs/HIGHER_MOMENTS.md) defines $c=\cos(\theta/2)$ and $s=\sin(\theta/2)$.

For H⁶, the Lean recurrence is proved for $m\geq3$. An exact Gaussian-integer polynomial certificate supplies the exceptional transition $m=2\to3$. Together they give, for every $m\geq2$,

$$
D_m^{(6)}
=3^{m-2}D_2^{(6)}
+\frac{3^{m-2}-1}{2}C_6,
$$

where

$$
D_2^{(6)}=-14592s^2+1344cs^2-384s^3,
$$

$$
C_6=4512s^2+192cs^2+768s^3.
$$

Equivalently,

$$
D_m^{(6)}
=-(12336\cdot3^{m-2}+2256)s^2
 +(1440\cdot3^{m-2}-96)cs^2-384s^3.
$$

The normalized H⁶ diagnostic is

$$
J_m^{(6)}=\frac{D_m^{(6)}}{N_m}.
$$

The exact limit and exact finite-level remainder follow algebraically:

$$
J_\infty^{(6)}
=\frac{-12336+1440c}{27}s^2,
$$

$$
J_m^{(6)}-J_\infty^{(6)}
=-\frac{D_2^{(6)}+5C_6}{9N_m}.
$$

For H⁸, the Lean recurrence is also proved for $m\geq3$, and an exact sparse-polynomial certificate supplies the transition $m=2\to3$. For every $m\geq2$,

$$
D_m^{(8)}
=3^{m-2}D_2^{(8)}
+\frac{3^{m-2}-1}{2}C_8,
$$

with

$$
\begin{aligned}
D_2^{(8)}={}&-1335552s^2+244352cs^2-40064s^3\\
&+64cs^3+1920s^4,
\end{aligned}
$$

$$
\begin{aligned}
C_8={}&193600s^2+75776cs^2+83712s^3\\
&-512cs^3+192s^4.
\end{aligned}
$$

Thus

$$
\begin{aligned}
J_\infty^{(8)}=\frac{1}{27}\big(&-1238752s^2+282240cs^2\\
&+1792s^3-192cs^3+2016s^4\big),
\end{aligned}
$$

and

$$
J_m^{(8)}-J_\infty^{(8)}
=-\frac{D_2^{(8)}+5C_8}{9N_m}.
$$

**Proof boundary.** The all-level recurrences are Lean theorems. The exceptional finite H⁶/H⁸ base transitions are exact symbolic certificates outside the Lean kernel. The combined formulas and normalized limits are consequences of those two pieces; they are not being described as single Lean-kernel theorems.

The Python module [src/spectral_moments.py](src/spectral_moments.py) implements the H⁶/H⁸ finite-level formulas, normalized limits, and exact remainder expressions. Its regression tests compare the finite-level outputs with the independent upstream trace table at levels 2–4 and $\theta=\pi/2$.

## 4. H¹⁰ in Evgeny's Theorem: unconditional recurrence, unexpanded coefficient

The tenth-moment source has a stronger formal status than a numerical extrapolation. The Lean development proves the required radius-four corner transport through degree nine for both configurations. The theorem H10TransportAll_proved supplies the transport hypothesis, and the final declarations give an unconditional recurrence for $m\geq4$:

$$
D_{m+1}^{(10)}
=3D_m^{(10)}+C_{10}^{(5)}(\theta).
$$

The resulting affine formula holds for every $m\geq5$:

$$
D_m^{(10)}
=3^{m-5}\left(D_5^{(10)}+\frac{C_{10}^{(5)}}{2}\right)
-\frac{C_{10}^{(5)}}{2}.
$$

Here $C_{10}^{(5)}$ is the exact finite level-five trace expression named defectO10_num_residual_constant. It has not yet been simplified to an explicit trigonometric polynomial.

Normalizing by $N_m$ still yields an exact limit in terms of that finite trace coefficient:

$$
J_\infty^{(10)}
=\frac{D_5^{(10)}+C_{10}^{(5)}/2}{729},
$$

$$
J_m^{(10)}-J_\infty^{(10)}
=-\frac{D_5^{(10)}+122C_{10}^{(5)}}{243N_m},
\qquad m\geq5.
$$

The source theorem is unconditional in Lean. The coefficient's current trace-expression form is a presentation and simplification boundary, not an extra hypothesis in the recurrence. This repository deliberately does not duplicate an artificial H¹⁰ trigonometric polynomial or pretend that the coefficient has already been expanded.

Sources: [H¹⁰ source map and status](https://github.com/RFT-SIRM/Evgeny-Theorem/blob/main/docs/HIGHER_MOMENTS.md), [FinalClosed10.lean](https://github.com/RFT-SIRM/Evgeny-Theorem/blob/main/formalization/EvgenyTheorem/FinalClosed10.lean), [GlueTrace10.lean](https://github.com/RFT-SIRM/Evgeny-Theorem/blob/main/formalization/EvgenyTheorem/GlueTrace10.lean).

## 5. Phi-Genesis H¹⁰: a different operator and a status discrepancy to preserve

Phi-Genesis contains a separate scalar signed-graph experiment. Its operator is

$$
L_m=D_m-A_{s,m},
$$

with a deterministic GF(2) signing: hole-boundary parity constraints are solved by the lexicographic pivot convention, and non-pivot edge variables are set to zero. It is **not** the noncommutative SU(2) operator used by Evgeny's Theorem.

For generation mask $t=(t_1,\ldots,t_m)$, the November 4 checkpoint records the all-level derivation

$$
F_{m+1}(t_1,\ldots,t_m,d)
=3F_m(t_1,\ldots,t_m)+Q(a,b,c,d),
\quad m\geq3,
$$

where $a=t_1,\ b=t_2,\ c=t_3$, and

$$
\begin{aligned}
Q={}&127182024+89195520a+73945440b-145153920ab\\
&+55360c-150880ac+40320bc-39680abc\\
&+d(115347760-110022480a+10024960b\\
&\qquad-20854720ab+320c-640ac).
\end{aligned}
$$

For the full-flux difference $D_m=F_m(1,\ldots,1)-F_m(0,\ldots,0)$, that checkpoint derives

$$
D_{m+1}=3D_m+12387360,\qquad m\geq3,
$$

and consequently

$$
D_m=555046440\cdot3^{m-3}-6193680.
$$

If that all-level derivation is accepted, normalization per graph vertex gives

$$
\lim_{m\to\infty}\frac{D_m}{|V_m|}
=\frac{370030960}{27}.
$$

**Status must be read carefully.** The file [H10_ALL_LEVEL_CHECKPOINT_2026-11-04.md](https://github.com/RFT-SIRM/Phi-Genesis/blob/main/computational/higher_moments_z2/H10_ALL_LEVEL_CHECKPOINT_2026-11-04.md) records a geometric/inductive all-level derivation and its finite exact checks. It is not a Lean-kernel proof. The public summary [docs/higher-moments-z2.md](https://github.com/RFT-SIRM/Phi-Genesis/blob/main/docs/higher-moments-z2.md) still describes the recurrence conservatively as finite computational evidence and lists all-level proof/formalization as open. The two documents therefore need reconciliation and independent proof review before this result is promoted as a theorem in another project.

There is a further invariance caveat: hole-boundary parities do not determine the whole signed cocycle. The H¹⁰ coefficient belongs to the specified deterministic representative, not to hole flux alone. The November 3 follow-up records boundary-invisible edge flips that preserve the hole constraints but change H¹⁰.

The identity

$$
\operatorname{Tr}((L\otimes I_2)^{10})=2\operatorname{Tr}(L^{10})
$$

does not identify this scalar signed-Z₂ defect with the SU(2) axis-orientation defect. Their operators, boundary data, recurrences, and coefficients must remain separate.

Sources: [Phi-Genesis H¹⁰ implementation](https://github.com/RFT-SIRM/Phi-Genesis/blob/main/phi_genesis/higher_moments_z2.py), [finite signed-Z₂ H¹⁰ dossier](https://github.com/RFT-SIRM/Phi-Genesis/blob/main/docs/higher-moments-z2.md), [November 4 all-level checkpoint](https://github.com/RFT-SIRM/Phi-Genesis/blob/main/computational/higher_moments_z2/H10_ALL_LEVEL_CHECKPOINT_2026-11-04.md).

## 6. Phi-Genesis Schur line: related spectrum, not a moment theorem

Phi-Genesis also has a distinct Schur-complement programme for the bottom of a Sierpiński signless Laplacian. Its Lean proofs establish the signed/signless gauge relation, a global eigenvalue lower bound of 1, a bootstrap interval, uniqueness of the selected A1 root in that interval for levels $N\geq6$, and convergence of the least eigenvalues into the interval.

The reported value near $1.3091289202808134218886\ldots$, the approximately $0.4939504899$ quadratic-increment ratio, and the E/A1 splitting are high-precision numerical observations from the exact recursion. The exact limit, its closed form, and the quadratic increment law are not established. This Schur work is not the H⁶/H⁸/H¹⁰ trace expansion and is not used by the current cosmology model.

Sources: [Schur proof map](https://github.com/RFT-SIRM/Phi-Genesis/blob/main/computational/spectral_gap_theta_2pi/PROOF_MAP.md), [high-precision recursion record](https://github.com/RFT-SIRM/Phi-Genesis/blob/main/computational/spectral_gap_theta_2pi/HIGH_PRECISION_2026-11-06.md).

## 7. What enters cosmology now—and what does not

The current Pass-1 model uses only the normalized H⁴ invariant:

$$
q_m=1+\epsilon I_m.
$$

The H⁶/H⁸ normalized diagnostics are now available as reproducible mathematical outputs, and the H¹⁰ normalized limit has an exact trace-expression representation. They are **not** additional terms in $q_m$. No coefficients $\epsilon_6,\epsilon_8,\epsilon_{10}$ are introduced.

A physical extension would need to derive, rather than assume:

1. which operator observable couples to which cosmological sector;
2. why that coupling has the proposed functional form;
3. the allowed parameter domain and stability conditions;
4. the corresponding background and perturbation equations;
5. the observable consequences that can distinguish it from the baseline model.

Until that derivation exists, the higher moments are retained as independent spectral diagnostics. This preserves the mathematical results without turning them into unsupported physical claims.
