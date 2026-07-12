# Structural Decline-Bias: Root-Cause Analysis and Toy Findings (E51)

A contrarian, equations-first re-examination of the five open decline-bias defects in the shipped
behavioural core (`src/sci_demographic_collapse/emergent.py`), attacking the CAUSES (DEF-1/2/3/4/6)
rather than the recuperation SYMPTOM (DEF-5, whose bolt-on was promotion-DECLINED at E50). For each
defect the central question is defect-vs-feature: is the down-drift / ratchet / antinatal-only well an
artifact to be symmetrised, or is it the model correctly encoding that these societies are declining -
so that removing it makes the E41 2000-2023 backtest WORSE? A fix is a real fix only if it improves the
backtest (fewer sign-misses AND lower chi2/dof on the recoveries) WITHOUT breaking the 2023 calibration,
without letting Korea spuriously recover, and without wrecking the recorded guard suite. Otherwise the
honest verdict is REFUTED-AS-DEFECT - the "defect" was a feature.

## Headline

The decline-bias is, to the precision the backtest can adjudicate, largely CORRECTLY-FIT SIGNAL, not
artifact. Four of the five defects are REFUTED-AS-DEFECT and the fifth is subsumed. The single most
important number: zeroing all four secular drift terms sends the backtest chi2/dof from 3.68 to 8.39
(2.3x WORSE), and when the fit is set FREE to choose any sign (secular bounds widened to admit up-drift),
it pins secC and secS to their maximum-DOWN rails (secC=0.010, secS=0.010) and keeps secPb=0.012 and
secTau=0.019 down - NOT ONE of the four secular terms selects the up direction. The data actively wants
MORE decline in every channel, not less.

A second number is the whole story of the missed recoveries: that free, lower-chi2 fit (3.22, better than
baseline 3.68) makes the recoveries WORSE, not better - recovery RMSE rises to 0.265 from 0.124, and every
region's net 2000-2019 change turns negative. chi2 and recovery-fit are in direct TENSION: a single shared
secular drift that fits the large collapses (Korea -0.56, USA -0.35) necessarily over-suppresses the
recoverers (Germany +0.155, Israel +0.113). The recovery miss is a pooling problem, not a missing up-well.

The framing that the core "cannot turn up" is itself too strong. At the shipped drift the model produces
a small universal tempo-transient RISE over 2000-2023 (every region +0.008 to +0.078). The recovery SIGN
is only "missed" after the WLS fit forces a strong SHARED secular down-drift to fit the large collapses
(Korea -0.56, USA -0.35). A single global drift cannot fit the collapsers and the recoverers at once, so
it compromises at strong-down and over-suppresses the recoverers. The missed recoveries are a POOLING /
heterogeneity problem plus a genuine missing TRANSIENT recuperation (postponement-recuperation, the DEF-5
symptom) - neither of which the structural symmetrisations DEF-1/2/3/6 supplies.

## Toy results summary (measured this round)

Backtest at the REFIT optimum unless noted. Baseline is the faithful port of the current shipped core
(all 13 guards green). Recovery RMSE = RMS signed net-2000-2019 error over the 4 recovery regions
(Germany, Italy, Poland, Israel); observed nets +0.155 / +0.010 / +0.049 / +0.113. Lower chi2/dof and
lower recovery RMSE are both required for a KEEP.

| fix | chi2/dof | R1 misses | recovery RMSE | Korea 2019 (falls) | cal drift (post-resolve) | verdict |
|---|---|---|---|---|---|---|
| baseline (shipped core) | 3.684 | 6 | 0.124 | 0.829 (yes) | - | reference |
| DEF-1 zero secular (no refit) | 8.393 | - | - | - | - | REFUTED (2.3x worse) |
| DEF-1 free bounds (up allowed) | 3.221 | 4 | 0.265 | 0.835 (yes) | - | FEATURE (fit pins max-down) |
| DEF-2 signed dependency | 3.684 | 6 | 0.124 | 0.829 (yes) | 1e-6 | REFUTED (inert) |
| DEF-3 tri-well + Israel anchor | 3.681 | 6 | 0.124 | 0.828 (yes) | 1e-6 (3.1e-3 pre) | REFUTED (inert) |
| DEF-6 two-child parity well | 4.26 | 3 | 0.062 | 0.781 (yes) | 0.020 (BREAKS) | REMOVE (non-selective) |
| JOINT (DEF-1+2+3+6) | 7.784 | 4 | 0.047 | 0.683 (R2 FAIL) | 0.015 (BREAKS) | REMOVE |

DEF-4 (rate-constant refit, Israel held out): holding Israel out shifts only kTau by 0.00095 (~1.7%);
kC/decl/gS_C invariant. SUBSUMED - Israel as a recovery-velocity constraint moves nothing material.

Note the two "movers" sit at opposite ends of ONE tradeoff: recovery RMSE falls monotonically as the
quantum is lifted (DEF-1-free 0.265 -> baseline 0.124 -> DEF-6 0.062 -> joint 0.047) while chi2/dof and
Korea degrade with it. No configuration reaches the lower-left corner (both chi2/dof < 3.68 AND recovery
RMSE < 0.124). Overall fit and recovery fit are in irreducible tension through the single shared quantum
level - the numerical definition of the pooling problem, and the answer to the round: the decline-bias
cannot be symmetrised away for free.

## Method - the harness

`scratchpad/toy_bias_harness.py` ports the E41 backtest runner (`notebooks/37-kj-e41-backtest.ipynb`)
into a standalone module and wraps it in a `BiasModel` whose five fixes are baseline-preserving toggles.
The `_estep_vec` override reproduces the shipped step BIT-FOR-BIT with every toggle off (verified: worst
per-channel diff 0.0 across all 8 regions x 4 secular-clock values), so any deviation is attributable to
the fix alone. MAC and marriage-witness residuals reproduce the recorded backtest artifact bit-for-bit
(e.g. Germany MAC 2.48, MAR 0.99), confirming the C and tau trajectories are exact; a few-percent Pb
vintage micro-drift shifts the quantum LEVEL slightly, which only matters for the knife-edge sign race
(below). All 13 hypothesis guards pass on this baseline.

Per fix we measure, at the REFIT optimum (WLS over the 4 global params secC/secPb/secTau/kTau, Huber,
the frozen exclusions): chi2/dof; R1 sign-misses; the per-recovery-region signed net 2000-2019 model TFR
vs observed (the robust MAGNITUDE metric); Korea's 2019 level and monotonicity; and, for structural
fixes, the 2023 calibration drift after re-solving PB_SCALE_ENS.

### A note on the fragile sign race (why R1 is not the metric of record)

At the shipped drift the model's net 2000-2019 change is a small POSITIVE number for all 8 regions - the
tempo-transient rise (tau relaxes upward fastest in year 2000, so the Bongaarts-Feeney factor
`1 - kBF*dtau` suppresses TFR most at the window start and lifts it as postponement decelerates). Whether
a borderline region lands at -0.005 or +0.007 over 23 years flips its R1 verdict, and a within-tolerance
Pb difference is enough to tip it. On the current shipped core the faithful baseline shows R1 = 6 misses
(USA, Germany, Italy, Korea, Poland, Israel) at the refit optimum, vs the recorded artifact's 4 (Germany,
Italy, Poland, Israel) - the composition differs because the sign is a knife-edge, not because the
machinery differs. The ROBUST signal is the magnitude: Germany's observed +0.155 and Israel's +0.113 are
large and the model's ~0 clearly under-produces them; Italy +0.010 and Poland +0.049 are within the
sign-race noise. Verdicts below rest on magnitude (recovery RMSE) and chi2/dof, with R1 reported for
continuity and flagged where fragile.

---

## DEF-1 - all four secular drift terms point down

**Location.** `PARAMS` secC=0.0007, secPb=0.0010, secTau=0.006, secS=0.0010 (emergent.py:148-159).
Applied in `_estep_vec`: `Ceq ... - secC*100*tn` (line 572; :275 in scalar `_estep`),
`dPb ... - secPb*100*tn` (:576), `dtau ... + secTau*100*tn` (:578), `dS ... - secS` (:570). The clock is
`tn = (year-2023)/100`.

**Mechanism of the bias.** Three of the four are tn-gated: they vanish at 2023 (tn=0) and activate going
forward, so the 2023 calibrated state is not a neutral fixed point but the START of a glide path -
secC/secPb subtract from the C/Pb equilibrium (quantum glides down), secTau adds to the tau target (MAC
glides up, the fec knee bites). The fourth, secS, is a FLAT, always-on drag on security (NOT tn-gated),
permanently pinning S below S0 by secS/kS ~ 0.017, which feeds C down (via gS_C) and tau up (via gTau).
Every one points fertility down; none moves any channel up.

**Artifact or correctly-fit signal? FEATURE (decisive).** The backtest FITS secC/secPb/secTau, and it is
the one part of the machinery the data directly adjudicates. In the standard down-only bounds the fit
drives secC UP 0.0007 -> 0.0025 (3.6x) and secPb UP 0.0010 -> 0.011-0.014 (11-14x). Zeroing all four (no
refit) sends chi2/dof 3.68 -> 8.39 (2.3x worse). The clincher is the free-bounds refit: with secular
bounds WIDENED to admit up-drift (secC in [-0.01,0.01], secPb in [-0.02,0.02], secTau in [-0.06,0.06],
secS in [-0.01,0.01]), the fit selects secC=0.010 (pinned to the maximum-DOWN rail), secS=0.010 (max-down
rail), secPb=0.012, secTau=0.019 - every single term down, two on their down-rails, none up. chi2/dof even
IMPROVES to 3.22. So the down-drift is not merely tolerated by the data; the data demands it and would take
more. Direction of the down-drift is EMPIRICALLY GROUNDED and under-strength at the shipped values.

**The tension that IS the missed recovery.** That free, lower-chi2 fit makes the recoveries WORSE: net
2000-2019 turns negative for all 8 regions (Germany +0.155 obs vs -0.121 model, err -0.276; Israel +0.113
vs -0.219, err -0.332), recovery RMSE 0.124 -> 0.265. Lowering chi2 (fitting the collapsers) and fitting
the recoveries pull in opposite directions through the ONE shared drift - the numerical signature of the
pooling problem. The recovery is not blocked by a missing up-structure; it is crowded out by a shared
down-drift that the collapsers demand.

**Why the "fix" cannot produce recoveries.** A secular drift is monotone for ANY sign. The observed
recoveries are an interior trough-then-rise (a quantum rebound while MAC still rises - Bongaarts-Sobotka
2012, Goldstein 2009). No monotone term of any sign can make a U; sign-flipping the drift just swaps one
monotone glide for another. So DEF-1's proposed fix is orthogonal to the phenomenon it is meant to fix,
and its actual effect (zeroing) worsens the fit.

**Verdict-so-far: REFUTED-AS-DEFECT (feature).** The secular down-drift on C and Pb is correctly-fit
signal; the recovery lives in the transient rebound, not in the slow trend's sign.

---

## DEF-2 - the age-structure feedback is a one-way ratchet

**Location.** `dep_pen = dep_fb * max(dep - dep0, 0)` at emergent.py:390 (`run`), :542 (`run_dist`),
:718 (`run_ens`); the backtest computes the same expression in its own loop. `dep_pen` enters `dS` as a
subtraction, so an aging pyramid (dep > dep0) depresses security S.

**Mechanism of the bias.** The `max(.,0)` clip keeps only the headwind. A YOUNGER pyramid (dep < dep0)
gives `dep_pen = 0` and therefore no security boost - the demographic-dividend tailwind (a rising
support ratio easing the resource cost of childrearing - Lee & Mason 2006 / Mason NTA) is clipped. The
only endogenous macro-feedback in the model is sign-restricted to decline.

**Artifact or correctly-fit signal? A REAL asymmetry, but INERT on the gate.** Over 2000-2023 every
region's old-age dependency rises monotonically (population aging), so `dep > dep0` every year and
`max(dep-dep0,0) == (dep-dep0)` exactly. Measured: the signed and clipped forms are bit-near-identical,
max series delta 6.8e-4 (a transient migrant-driven dip in USA/Israel only, immaterial). AT THE REFIT
OPTIMUM the signed dividend is indistinguishable from baseline: chi2/dof 3.684 (= baseline 3.684),
recovery RMSE 0.1236 (= baseline 0.124), calibration drift 6e-5 before re-solve (already inside the 5e-4
guard) and 1e-6 after. The dividend branch only activates when a pyramid YOUNGS, which no region did
in-window; it can bite only in a FORWARD run after an intervention first reverses a pyramid - a slow,
second-order effect the demographic-dividend literature itself frames as a multi-decade window.

**Verdict-so-far: REFUTED-AS-DEFECT for the backtest (forward-only note).** The clip is a genuine
asymmetry worth a documented forward-run caveat, but it moves no backtest number and no recorded verdict,
so by Occam it is not a shipped fix.

---

## DEF-3 - the norm channel is antinatal-only (no pronatal well)

**Location.** `NORM0` per region (emergent.py:107-116); wells Nlo=0.14, Nhi=0.42, unstable tip thN=0.25
(PARAMS:171-173); the cubic double-well `dN = -aN*(N-Nlo)*(N-thN)*(N-Nhi) + fN` at :284 / :518 / :580;
the coupling `lam_rho*(N-NORM0)` inside `drv`.

**Mechanism of the bias.** The double-well has a childfree lock-in (Nhi) and an untrapped low well (Nlo)
but NO stable well below Nlo - a pronatal norm cannot lock in. The campaign's richest, most-developed
channel (E25/E38/E43/E44/E45) points only down. There is no structural home for a self-reinforcing
pronatal subculture (Israel/Haredi - Okun 2017, Kaufmann-Goujon-Skirbekk 2012, Amish Greksa-Korbin 2002).

**Artifact or correctly-fit signal? A real structural-completeness gap, but INERT on the hindcast.** Each
region starts snapped to its well, so `N = NORM0` is a fixed point and `lam_rho*(N-NORM0) = 0` at 2023.
During the backtest nothing forces N (fN=0), so N is frozen and the norm channel contributes nothing to
the 2000-2019 dynamics. Adding a third well below Nlo changes the potential landscape but N still does not
move unless pushed. Measured: the tri-well leaves the backtest series within 8e-3 of baseline (a
second-order curvature perturbation from imperfect mid-well matching, not a recovery force). The Israel
re-anchor is instructive: re-pinning NORM0[Israel] to 0.02 WITHOUT the tri-well makes Israel WORSE
(net +0.008 -> -0.023) because 0.02 is not a fixed point of the cubic - N drifts UP toward Nlo, raising
childlessness; WITH the tri-well 0.02 becomes a genuine well and Israel sits still (net +0.005 ~ baseline
+0.008), confirming the pronatal anchor needs the third well to be stable but is INERT on the hindcast
either way. AT THE REFIT OPTIMUM the tri-well is indistinguishable from baseline: chi2/dof 3.681 (=
baseline 3.684), recovery RMSE 0.124, Korea 0.828 (falls). The one wrinkle: the imperfect mid-well
match perturbs the 2023 baseline (calibration drift 3.1e-3, above the 5e-4 guard), which a PB_SCALE_ENS
re-solve restores to 1e-6 - a shipped tri-well must pin the mid-well fixed point exactly at NORM0.

**Verdict-so-far: REFUTED-AS-DEFECT for the backtest (forward-durability value only).** The missing
pronatal well is a real asymmetry and the right structural home for a durable pronatal cascade, but its
relevance is a FORWARD norm-lever durability verdict (the E47-H431 gate), not the hindcast. It moves no
backtest number.

---

## DEF-4 - rate constants calibrated only on collapse

**Location.** The dynamic rate constants kC=0.08, decl=0.05, C_thr=0.66, C_floor=0.24, gS_C=0.9,
kTau=0.06 (PARAMS), fit in E19 on the 7 sub-replacement regions; Israel is a placed point (period-epoch
pair, low-well NORM0 by fiat, C0=0.97).

**Mechanism of the bias.** The E19 dynamics fit never saw a rising trajectory, so the recovery-velocity
constants are unconstrained by any recovery. Note the coupling trap `decl*max(C_thr-C,0)*max(C-C_floor,0)`
only bites for C between C_floor=0.24 and C_thr=0.66 (the collapsing regions); Israel's C0=0.97 sits ABOVE
the trap (the decl term is identically 0), so the model DOES represent Israel's healthy basin - it simply
never used a recovery to calibrate the SPEED of one.

**Artifact or correctly-fit signal? An identifiability concern, not a mechanism, and DOWNSTREAM of the
structural down-bias.** Refitting the rate constants cannot make a down-only system rise; it only
redistributes residuals. The probe (refit kC/decl/gS_C/kTau on all 8 vs holding Israel out) lands the
decisive way: holding Israel out shifts ONLY kTau by 0.00095 (~1.7%); kC, decl and gS_C are bit-identical
in and out (all pinned to their probe bounds). Israel as a recovery-velocity constraint moves nothing
material (well under a 20% bar) - exactly because Israel's C0=0.97 sits above the coupling trap and does
not constrain the trap constants.

**Verdict-so-far: SUBSUMED (not an independent fix).** DEF-4 is real as a data-coverage caveat but is not
a mechanism the backtest can act on without a restoring term; it is downstream of DEF-5.

---

## DEF-6 - fertility-raising channels thin, lowering channels rich

**Location.** `dPb = kPb*(PB0 + gPb*fPb - secPb*100*tn - Pb)` (linear, emergent.py:279 / :502 / :576) and
`dS` (linear), versus the rich nonlinear C (the coupling trap), N (the double-well), tau (the fec knee),
and q (the cohort memory). The channels that would carry recovery are thin linear scalars with downward
drift; recovery cannot cascade, collapse can.

**The fix moves the numbers, but non-discriminatingly.** At shipped params (isolating the well), replacing
the linear parity relaxation with a two-child bistable well (wells at the depressed baseline and a
two-child plateau ~2.0, tip 1.72) lifts the net 2000-2019 change for EVERY region: Germany +0.068 ->
+0.099, but also decline-region USA +0.078 -> +0.096 and Japan +0.035 -> +0.068, Italy +0.021 -> +0.066,
Poland +0.041 -> +0.084, Israel +0.008 -> +0.083. No region crosses the tip 1.72 to cascade to the
two-child well, so the "lift" is not a cascade -
it is the double-well restoring force near the LOW well being weaker than the linear kPb relaxation, i.e.
a quantum-softener whose strength is set by the arbitrary well stiffness. It raises decliners and
recoverers alike.

**At the refit optimum it improves recovery MAGNITUDE but fails every KEEP bar.** Recovery RMSE halves,
0.124 -> 0.062 (Germany err -0.082, Italy +0.032, Poland +0.061, Israel -0.062) - a genuine
recovery-magnitude improvement. But (a) overall chi2/dof WORSENS 3.68 -> 4.26 (over-fits recoveries,
under-fits collapses); (b) it wrong-signs DECLINE regions (USA net +0.066, Japan +0.033, both observed
declines); (c) it BREAKS the 2023 calibration and PB_SCALE_ENS cannot restore it - drift 0.020 AFTER
re-solve (40x the 5e-4 guard), because the two-child well makes the low well `pb0 = PB0*pb_scale` a
self-referential moving target the parity rescale cannot cleanly solve; and (d) it double-counts DEF-3's
pronatal well (the E47-H433 shared-channel confound). The recovery-magnitude gain is elegance that moves
the numbers for the wrong reason - a non-discriminating global lift, not a selective recovery mechanism.

**Verdict-so-far: MOVES the recovery magnitude but REMOVE by Occam.** Fails on overall chi2, on
calibration preservation, on selectivity (wrong-signs the decliners), and on orthogonality (confounds
DEF-3). It is the mirror of DEF-1-free: DEF-1-free minimises chi2 by pushing quantum DOWN (recoveries
worst, 0.265); DEF-6 minimises recovery RMSE by pushing quantum UP (chi2 worst, 4.26). Same shared knob,
opposite ends - neither reaches both.

---

## Joint fix and interactions

Effects compete; the down-terms interact. Turning on the joint structural set (DEF-1 zeroed + DEF-2 signed
+ DEF-3 tri-well + DEF-6 parity well, refitting kTau with the secular frozen off) gives chi2/dof 7.784
(2.1x the baseline 3.68), R1 4 sign-misses (USA, France, Japan, Korea - the DECLINE regions), recovery
RMSE 0.047 (the best recovery fit of any config), Korea 2019 = 0.683 which BREAKS the R2 gate (0.235 below
0.918, > 0.15, and no longer falling 2015-2019), and calibration drift 0.015 after re-solve (30x the
guard, broken). Every region's net turns positive (+0.072 to +0.117): the zeroed secular (DEF-1) and the
parity lift (DEF-6) COMPOUND to push the whole quantum up, which fits the recoveries but catastrophically
misses the collapses and drives Korea out of its basin.

**Interaction.** On the recovery axis DEF-1 (down) and DEF-6 (up) OPPOSE, and DEF-6 wins in the joint
(recovery RMSE 0.047, the lowest). On the chi2 axis they are near-additive with a small negative
interaction: pure zeroed-secular scores 8.39, DEF-6 alone +0.58 over baseline, yet the joint is 7.78 -
DEF-6's lift plus the kTau refit claws back ~0.6-1.2 of DEF-1's zeroing damage but nowhere near enough.
DEF-2 and DEF-3 are inert and contribute nothing. The joint therefore has no clean interaction that
rescues the fit; it simply confirms the Pareto tension: maximising recovery fit destroys collapse fit,
Korea, and calibration at once.

## Grounding digested

- `[paper digest] recent rise european fertility tempo Bongaarts Sobotka, 2012` and
  `[paper digest] end of lowest-low fertility Goldstein Sobotka Jasilioniene, 2009` - the European rise is
  postponement-RECUPERATION (a quantum rebound while MAC still rises), i.e. a transient, not a reversal of
  a secular decline. This is why symmetrising the slow drift (DEF-1) cannot reproduce it and why the down-
  drift itself is not the culprit
- `[paper digest] postponement recuperation cohort fertility Sobotka Zeman Frejka, 2011` - the
  recuperation index; the recovery magnitude is a per-region quantity, grounding the DEF-4 heterogeneity
  reading
- `[paper digest] demographic dividend overview Mason NTA` (Lee & Mason 2006; downloaded this round) - the
  age-structure effect is signed and symmetric in principle but a slow multi-decade window; grounds DEF-2's
  forward-only, inert-on-hindcast verdict
- `[paper digest] Israel religiosity and fertility Jews Okun, 2017`,
  `[paper digest] end of secularization demographic projection Kaufmann Goujon Skirbekk, 2012`,
  `[paper digest] old order amish fertility Greksa Korbin, 2002` - documented self-reinforcing pronatal
  subcultures, the empirical case for DEF-3's third well (a forward-durability structure)
- `[paper digest] low fertility trap hypothesis Lutz Skirbekk Testa, 2006`,
  `[paper digest] two-child family ideal Europe Sobotka Beaujouan, 2014`,
  `[paper digest] cultural evolution of fertility decline Colleran, 2016` - the nonlinear social-multiplier
  / tipping basis for DEF-3 and DEF-6, and the reason a single well suffices (shipping both double-counts)
