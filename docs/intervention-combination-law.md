# How interventions combine: the log-TFR bilinear law

**The law in one line**: interventions are ADDITIVE IN LOG-TFR across independent channels (Bongaarts multiplicativity), and the only genuine interaction is the departure from log-additivity - the mixed second derivative of the log-TFR response, `I(A,B) = f_A^T H f_B`, with `H` read straight off the calibrated core, never hand-set.

## Overview

The campaign combines interventions into multi-lever bundles, and how their effects compose was handled by plumbing the user rejected - hand-set synergy constants, `cap_sum` caps, and leave-one-out output arithmetic. This document replaces all of it with a law that falls out of the core's own equations. The core's per-agent fertility is a product of bounded channel factors,

```
TFR = C · (1 − ρ) · P̄ · fec(τ) · (1 − k_BF · dτ)
```

so on the log scale the channels are additive. That single fact - the same multiplicativity Bongaarts built the proximate-determinants model on (`TFR = TF · Cm · Cc · Ca · Ci`) - is the whole combination law. Everything the plumbing called "synergy" is either (a) the curvature of `exp()` misread on the raw scale, or (b) a real, sign-correct, measurable departure from log-additivity that the model produces on its own.

## The equations

Write the endpoint log-TFR response to a 9-channel forcing vector `f` (the `interventions.CHANNELS` amplitudes `fS, fC, fPb, fTau, fRV, fN, fq, fF, fScar`) as `L(f) = log TFR(f)`. Expand about the calibrated 2023 baseline `f = 0`:

```
L(f) = L(0) + g·f + ½ f^T H f + …          g = ∇L(0),  H = ∇²L(0)
```

**Orthogonal-channel baseline (Bongaarts / log-additive).** If channels do not share a TFR factor and do not couple through the ODE, `H` is zero off its diagonal and `L` is a sum of per-channel terms - `log TFR = log C + log(1−ρ) + log P̄ + log fec(τ) + log(1−k_BF dτ)`. Combining independent levers is exact addition in log-TFR, i.e. multiplication of their TFR factors. This is the honest null model.

**The genuine interaction (bilinear form).** For two disjoint single-channel pushes `f_A`, `f_B`, the interaction is the mixed Hessian block:

```
I(A,B) = L(f_A + f_B) − L(f_A) − L(f_B) + L(0)  ≈  f_A^T H f_B
```

`I > 0` is synergy, `I < 0` is saturation, `I = 0` is independence - Caswell's exact reading of the mixed second derivative of a matrix-population growth rate. `I(A,B)` is measurable directly (four model runs) and is what should replace every plumbing constant.

**The raw-scale artifact (why the plumbing was fooled).** Because TFR is multiplicative, two positive pushes look super-additive on the RAW ΔTFR scale even with zero true interaction:

```
ΔTFR_joint − ΔTFR_A − ΔTFR_B = TFR₀ · (e^{L_A} − 1)(e^{L_B} − 1) > 0
```

This is pure `exp()` curvature, not synergy. The leave-one-out ratio `full / Σmarginals` reads > 1 for this reason on 67 of 117 bundles (49 of them above 1.05) - an artifact of the scale, removed exactly by moving to log-TFR.

**N interventions.** A bundle `f = Σ_a f_a` combines as exact measured solo main effects plus the sum of pairwise bilinear interactions (`combine.predict_bundle`):

```
L(f) ≈ L(0) + Σ_a [L(f_a) − L(0)] + Σ_{a<b} f_a^T H f_b
```

Main effects are the EXACT measured solo log-effects, so a single-channel bundle reduces exactly to its scalar result (baseline-preserving); only the cross-channel coupling is the quadratic residual.

## The three mechanistic sources of interaction

All three are the structure of `H`, computed from `emergent.py` by central finite differences on `run_cal` (`combine.grad_hess`), never asserted.

**1. Same-channel saturation - the diagonal of H (negative).** Two pushes on one bounded link compose sub-additively. In the basin (Germany, France) every diagonal entry is negative: `diag(H)_Germany = [−2.45, −3.05, −0.55, 0, −1.38, −107.7]` for `(fS, fC, fPb, fTau, fRV, fN)`. The coupling state `C` has a fixed ceiling `C_thr` and the `log(1−ρ)` factor is concave, so pushing them harder yields less - the honest, self-generated saturation the `cap_sum` plumbing tried to fake. One caveat on the `fN` entry: the norm channel sits on a double-well fixed point, so `L` has a kink at `fN = 0` and its second difference does not converge as `O(h²)` - the `−107.7` magnitude is step-dependent and only its SIGN is a reproducible model quantity (see Limitations). The other five diagonals converge cleanly.

**2. Cross-channel coupling - the off-diagonal of H (the ODE Jacobian).** Because `L` is a sum of per-channel logs, the entire off-diagonal comes from the channel-state map `x(f)` - the ODE couples security→coupling (`gS_C`), marriageability→coupling (`gqC`), norm→childlessness (`lam_rho`), security→tempo (`gTau`). The numerically estimated `H` reproduces exactly this wiring. Germany's off-diagonals:

```
          fS      fC     fPb    fTau     fRV      fN
 fS    -2.45   -5.14   -0.21   +0.02   +0.42   +1.06
 fC    -5.14   -3.05   -0.24   +0.02   +0.34   +0.80
 fPb   -0.21   -0.24   -0.55    0.00   +0.08   +0.20
 fRV   +0.42   +0.34   +0.08   -0.02   -1.38   -3.75
 fN    +1.06   +0.80   +0.20   -0.05   -3.75 -107.69
```

The largest off-diagonal is `H[fS, fC] = −5.14` - the coupling archetype, security and coupling sharing the bounded `C` link. The next is `H[fRV, fN] = −3.75` - the `lam_rho` norm→childlessness coupling. `fPb` (parity, a pure multiplicative factor with no ODE coupling) has near-zero off-diagonals - it combines cleanly, as the log-additive baseline predicts. `fTau` is nearly decoupled. The interaction pattern is the coupling operator, not a table of guesses.

**3. Threshold synergy - the curvature of the bistable separatrix (positive, and only near the ridge).** The norm `N` follows cubic double-well dynamics and the coupling `C` has a soft-bistable trap. Near a tipping point the fixed-point response is a saddle-node - `dx*/df` blows up as the well flattens - so two sub-threshold pushes can jointly tip the state across the separatrix. This shows as the diagonal of `H` flipping POSITIVE and large in a trapped region. Korea (deep in the trap) versus Germany (in the basin):

```
diag(H)  fS      fC      fPb   fTau   fRV     fN
Korea  +39.98  -44.62  -0.15   0.00  -0.67  +106.90     ← threshold: accelerating returns
Germany -2.45   -3.05  -0.55   0.00  -1.38  -107.69     ← saturation: diminishing returns
```

The same security channel has `∂²L/∂f_S² = +40` in trapped Korea and `−2.5` in the German basin (both well-converged) - this is the quantitative headline. The norm channel flips the same way in SIGN (positive in trapped Korea, negative in the German basin) but its magnitude is not a reproducible number (the `fN` kink above). The sign of the interaction is a property of manifold position - the model's own bistability, not a hand-tuned "near-ridge bonus".

## Numerical verification

Triad mean over Korea/Germany/France, scored on `run_cal` (`scratchpad/combine_verify.py` → `reports/combine_verification.json`). `raw_ratio = full / Σsolo` is the plumbing's metric; `I_meas` is the honest log-departure `L(bundle) − ΣL(solo)`; `I_bilin` is `Σ f_a^T H f_b`; `artifact` is the `exp()` curvature term.

| bundle | raw ΔTFR | raw_ratio (plumbing) | I_meas (log) | I_bilin | exp-artifact | honest class |
|---|---|---|---|---|---|---|
| IV1 universal childcare `fS,fC` | +0.568 | 0.869 | −0.154 | −0.047 | −0.086 | saturate |
| E18-H144 compress×lottery `fS,fC` | +0.598 | 0.859 | −0.185 | −0.057 | −0.098 | saturate |
| E18-H145 in-kind×permanence `fS,fC` | +0.654 | 0.832 | −0.259 | −0.080 | −0.133 | saturate |
| E18-H146 universal+statefund×de-risk `fS,fC` | +0.626 | 0.845 | −0.222 | −0.068 | −0.115 | saturate |
| H215 polygyny subsidy (5-channel) | −0.806 | 0.947 | −0.369 | +0.151 | +0.045 | saturate |
| H216 polygyny dev-regime (4-channel) | +0.267 | **1.278** | **+0.172** | +0.087 | +0.058 | **synergy (real)** |
| SYN-Cq coupling×quantum `fS,fPb` | +0.946 | **1.190** | **−0.027** | +0.267 | +0.151 | **artifact (not synergy)** |
| SYN-QN quantum×norm `fPb,fN` | +0.410 | 1.077 | +0.027 | +0.047 | +0.029 | synergy (mild) |
| SYN-SN coupling×norm-tip `fS,fN` | +0.549 | 1.063 | −0.002 | +0.430 | +0.033 | log-additive |

**What the plumbing could not do, and the law can.** The raw ratio does not separate synergy from artifact: H216 (raw 1.278) is genuine synergy (`I_meas +0.172`), while SYN-Cq (raw 1.190) is pure `exp()` artifact (`I_meas −0.027`, opposite sign) - same raw band, opposite truth. The log-scale `I_meas` splits them in every case. This is exactly the E16/E18 blocker: SYN-Cq is the "1.19 super-additive" reading whose honest interaction is slightly NEGATIVE. The scale correction resolves it with no free parameters.

**Sign correctness.** Same-archetype coupling pairs (`fS,fC`) are correctly negative (saturation) in all regions; the genuine cross-regime synergy (H216) is correctly positive. The threshold sign-flip is visible per region even on the pair interaction: the `fS,fC` saturation is weakest in trapped Korea (`I_meas = −0.115`) and deepest in the German basin (`−0.186`), because Korea's positive diagonal curvature partly offsets the shared-wire saturation.

**Shared eigenstructure with the culture-bearer Φ.** `H` is symmetric; its eigenvectors are coherent channel BUNDLES, not raw axes. Germany's eigen-decomposition gives a dominant norm mode (essentially `fN`+`fRV`; its eigenvalue inherits the `fN`-magnitude caveat, so read the mode COMPOSITION not the number) and a well-converged coupling mode (−7.9, the `fS`+`fC` bundle), with `fPb` nearly isolated. These bundles - {security, coupling} and {norm, childlessness} - are the same coupled directions the culture-bearer operator `Φ = r·V·Λ·V⁻¹` is built on, because both are governed by the one channel-coupling submatrix of the ODE (`gS_C`, `lam_rho`, `gqC`, `gTau`). The eigenvectors `V` that diagonalise how culture transmits also diagonalise how interventions combine: push along an eigenvector and the response stays in that mode with zero cross-interaction; the interaction between two raw-channel pushes is their overlap through the off-diagonal, i.e. their non-alignment with `V`. One operator, two phenomena. The correspondence is structural (`Φ` acts on the 7-dim trait vector, `H` on the 9-dim forcing; they share the coupling block), not a bit-identical matrix.

## Honest limitations

The elegant form SURVIVED as the correct SCALE and STRUCTURE, and was CORRECTED in one respect: the bilinear `f^T H f` is a local (small-signal) approximation, exact as amplitude → 0 (self-test: `I_meas = −0.0087` vs `I_bilin = −0.0123` at small pushes) but only a qualitative indicator at real bundle amplitude through the bounded and bistable channels. In the table its SIGN agrees with the exact `I_meas` for the same-archetype coupling bundles, H216 and SYN-QN, but it over- or wrong-signs the large-amplitude, stiff-channel probes (SYN-Cq, SYN-SN, H215) where a single push moves `fC` by ~1 or drives `fN` near its tip. The `fN` diagonal is the extreme case: because `L` has a kink at `fN = 0` (the norm channel starts on a double-well fixed point), its central second difference does not converge as `O(h²)` - halving the step drives the quotient from −32 to −108 to −408 - so the `fN` own-curvature has a well-defined SIGN but no reproducible magnitude, and the reported `±107` is a step artifact, not a model constant. This is Caswell's own caveat sharpened: a second-order truncation is not merely inaccurate but ill-defined where the response is non-smooth. So the operational law is:

- **Combine on the log scale, always** - `L(bundle) = Σ measured solo log-effects + interaction`. This is exact and kills the multiplicative artifact with no parameters.
- **Measure the interaction directly** as `I = L(A∪B) − L(A) − L(B) + L(0)` (four runs). This is the honest number; it replaces every hand-set synergy constant and `cap_sum`.
- **Use `H = ∇²L(0)` for structure, not magnitude** - its off-diagonal names which channels couple (the ODE Jacobian), its diagonal signs saturation vs threshold, and its eigenvectors are the archetype bundles shared with `Φ`. Near the ridge, trust the direct `I`, not the quadratic form.

Elegance moved the numbers - it removed the artifact, separated synergy from saturation where the plumbing could not, and produced the separatrix sign-flip from the model itself - but it did not survive as a precise closed-form predictor at bundle scale, and that is reported rather than decorated.

## Files

- `src/sci_demographic_collapse/combine.py` - the law: `log_tfr`, `grad_hess` (numerical `g`, `H`), `predict`, `predict_bundle`, `interaction`, `raw_curvature_artifact`, with a self-test (`python -m sci_demographic_collapse.combine`)
- `scratchpad/combine_verify.py` - the triad verification producing the table
- `reports/combine_verification.json` - per-region and triad `I_meas` / `I_bilin` / artifact + full `H` diagonals
- `references/papers/[paper] second derivatives of population growth rate Shyu Caswell, 2016.pdf` (+ digest) - the Hessian-of-λ / mixed-partial interaction grounding
- `references/papers/[paper] synergy null-interaction Hill response surfaces, 2016.pdf` (+ digest) - synergy as departure from the multiplicative null
- `references/papers/[paper] proximate determinants of fertility lecture notes Rodriguez, 2017.pdf` (+ digest) - Bongaarts multiplicativity and its interaction factor
