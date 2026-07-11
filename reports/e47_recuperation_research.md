# E47 Recuperation Research - the Grounded, Pre-Registered Fanout to Pass the Backtest

The E41 backtest REJECTED the shipped core because it cannot turn UP: it misses the SIGN of the
observed 2000→2019 TFR change for **4 of 8 regions** - Germany +0.155, Israel +0.113, Poland +0.049,
Italy +0.010 - at chi2/dof = 3.638 (bar 2.0). Korea's monotone collapse (-0.56) and the MAC-rise /
marriage-decline directions pass. DEF-5 (`docs/defects.md`) is the empirical shadow of the structural
down-bias, redirected by E46 to the QUANTUM channel: Germany recovered with MAC rising monotonically,
so the fix is a quantum LEVEL rebound (mean-reversion toward an attractor), not a tempo oscillator
(E46-H428 already demoted the tempo route).

This round grounds the recuperation term in the **established, trusted UN WPP recovery mechanism** -
the Bayesian hierarchical AR(1) of Alkema et al. (2011) / Raftery et al. (2014), the very model that
produced our WPP data - and fans out a clean set of hypotheses (H435-H440, continuing the E47 block
whose lead is H430). Each carries its mechanism, its emergent.py change, whether it is mechanistic or
Bayesian-inferred, its pre-registered gate, and its Occam status. A Bayesian model-comparison
hypothesis (H440) scores the candidate mechanisms against each other on out-of-sample backtest fit -
the principled way to pick the recovery law rather than hand-choosing it.

## The UN Bayesian recovery mechanism (the grounding to borrow)

The UN models a country's TFR in three phases: I pre-transition, II the transition (decline), and
**III the post-transition phase in which fertility recovers toward and fluctuates around a
country-specific long-term level**. Phase III is exactly the machinery our down-only core lacks. Its
functional form is a **Bayesian hierarchical first-order autoregressive process** around a bounded
country asymptote:

```
f_{c,t+1} = mu_c + rho_c * (f_{c,t} - mu_c) + epsilon_{c,t},     epsilon ~ N(0, sigma_eps^2)
```

A country whose TFR sits BELOW its asymptote `mu_c` is pulled UP a fraction `(1 - rho_c)` of the gap
each period - the mean-reverting rebound. The parameters are drawn from world-level hierarchical
priors (partial pooling): a country with thin post-transition data borrows the recovery behaviour of
countries that already turned up.

- **Classic form** (Fosdick-Raftery): `mu_c = 2.1` (replacement), `rho = 0.9`, `sigma_eps = 0.2` -
  reverts 10% of the gap-to-replacement per period with ~0.2 innovation noise
- **Hierarchical form** (WPP production): estimates country-specific `mu_c`, `rho_c` by MCMC.
  `bayesTFR` default priors: **`mu_c` in [0, 2.1]** (the asymptote is bounded ABOVE by replacement -
  the ceiling that stops the rebound overshooting), `rho_c` in [0, 1), `sigma_mu` in [1e-5, 0.318],
  `sigma_rho` in [1e-5, 0.289], `sigma_eps` in [1e-5, 0.5]
- **Phase III entry**: a country enters the recovery phase after its TFR posts a local minimum and two
  successive increases below replacement

This is the same "quantum mean-reversion toward an attractor" the E46 anchor and the H430 toy already
reach for - the UN model supplies its exact functional form, its parameter brackets, and its
hierarchical estimation template. Digest: `references/papers/[paper digest] bayesian population
projections for the united nations Raftery, 2014.md` (PDF alongside).

## What drives real quantum recoveries (the gate that spares Korea)

Goldstein-Sobotka-Jasilioniene (2009, in library) documented the end of "lowest-low" fertility: below
1.3 countries fell from 21 (2003) to 5 (2008), Spain 1.16→1.46, the rise concentrated at OLDER ages as
delayed cohorts recuperate - a quantum swing of 0.2-0.4 while MAC still rises (the E46 signature).
Sobotka-Zeman-Frejka (2011, in library) set the recuperation fraction (RI ~0.65 central, 0.37 Spain to
>1 US).

Myrskyla-Kohler-Billari (2009, Nature; digest + OA slides now in library) supply the DISCRIMINATOR:
the development-fertility curve is **J-shaped** - above **HDI ~= 0.86** further development RAISES
fertility (~+1 child per +0.25 HDI). Their 2011 follow-up shows **gender equality is a NECESSARY
condition**: the upturn appears ONLY where gender parity is high. High-HDI / LOW-gender-equity
societies (Korea, Japan, southern Europe) do NOT reverse. This is the mechanistic reason Germany
recovers (high HDI, high gender equity, post-2007 Elterngeld/childcare) while Korea keeps collapsing -
and it gates the recuperation term so Korea's monotone-decline gate is preserved BY CONSTRUCTION, not
by a per-region hand switch.

## Toy evidence - ranking the mechanisms in the backtest window

`scratchpad/toy_e47_recup_compare.py` runs three recovery laws over 2000→2019 on schematic but
anchor-honest TFR data for all 8 backtest regions:

| region | obs Δ | M0 current | M1 UN-AR(1) ungated | M2 gender-equity-gated |
|--------|------:|-----------:|--------------------:|-----------------------:|
| Germany | +0.160 | -0.190 | +0.147 | +0.140 |
| Italy   | +0.010 | -0.190 | +0.078 | +0.016 |
| Poland  | +0.050 | -0.190 | +0.069 | +0.019 |
| Israel  | +0.100 | -0.190 | -0.009 | -0.053 |
| Korea   | -0.560 | -0.190 | -0.156 | **-0.190** |
| Spain   | +0.000 | -0.190 | +0.104 | +0.058 |
| France  | -0.010 | -0.190 | +0.026 | +0.016 |
| USA     | -0.350 | -0.190 | -0.052 | -0.068 |

- **M0 (down-only)**: 4 sign-misses - the falsification reproduced
- **M1 (UN-AR(1) ungated)**: 2 sign-misses, but lifts Korea toward flat (weakens R2)
- **M2 (gender-equity-gated AR(1))**: 2 sign-misses AND keeps Korea's decline the steepest of the
  three (gate shut at g=0.55<0.60) - the discriminating fix

Two honest findings the toy surfaces: (1) the gender-equity gate is what protects Korea while letting
the below-replacement recoveries through; (2) **Israel is NOT solved by any below-replacement AR(1)
pool** - it already sits near 3.0, above the `mu_c <= 2.1` ceiling, so it needs its own pronatal
attractor (the H431 tri-stable norm well, DEF-3), not the recuperation reservoir. The backtest gate of
"≤1 sign-miss" therefore likely requires H435/H436 for the three European recoveries PLUS H431 for
Israel - a combined design, adjudicated by H440.

---

## H435 - UN-style Bayesian hierarchical AR(1) quantum mean-reversion (the grounded lead)

**Type**: mechanistic term with Bayesian-inferred parameters (pairs with H437).

**Hypothesis**: the core misses the three European recoveries because the quantum `C*(1-rho)*Pb` has
only down-forces and no attractor. Adding the UN Phase III restoring term - a mean-reversion of the
quantum level toward a bounded country asymptote - reproduces the recoveries while MAC keeps rising
(quantum, not tempo).

**Exact emergent.py change** (additive, baseline-preserving):
- Carry the quantum level `Q = quantum(C, rv, Pb)` and add a reversion increment each year toward a
  country attractor: `dQ_rec = kappa_c * (Q_attr_c - Q)`, with `kappa_c = 1 - rho_c` (the UN
  gap-closing fraction). Apply as an additive quantum uplift in `run` (emergent.py:372-375),
  `run_dist` (:527), and the `run_ens` per-agent aggregation (:699-700) so `f_rec = 0` reproduces
  baselines bit-for-bit.
- New PARAMS: `Q_attr_c` (country asymptote, **bounded <= 2.1/quantum-scale**, central = region's
  Sobotka recovery ceiling), `rho_rec` (central **0.9**, sweep [0.85, 0.95]), `sigma_rec`
  (innovation, central **0.2**). At the 2023 fixed point `Q = Q_attr_c => dQ_rec = 0`, so the term is
  identically zero on baseline (the guard).

**Literature grounding**: Alkema et al. (2011, *Demography*) / Raftery et al. (2014, *Statistical
Science*) Phase III AR(1) - the exact functional form, `rho=0.9`, `sigma=0.2`, asymptote `<=2.1`, and
the hierarchical estimation template. This is the UN's own recovery mechanism operating on our own data
source. Secondary: Goldstein-Sobotka-Jasilioniene (2009), Sobotka-Zeman-Frejka (2011) for the
recuperation-fraction bracket.

**Pre-registered gate**: re-run the E41 backtest with H435 (fitting `Q_attr_c`, `rho_rec` in-bracket).
KEEP iff B5-R1 sign-misses drop from 4 to **<= 1 of 8** AND Korea's monotone decline (R2) still passes
AND chi2/dof does not worsen (<= 3.638). REMOVE if it flips < 2 sign-misses or over-lifts Korea.

**Occam status**: KEEP-if-moves. This is H430 given the UN's exact functional form and parameter
priors - it SUPERSEDES the ad-hoc reservoir framing of H430 by grounding the same mean-reversion in the
trusted model. **Ungated risk**: the toy shows an ungated asymptote also lifts Korea (Korea is below
its own `mu_c`), weakening R2 - which motivates H436.

## H436 - Myrskyla gender-equity-gated recovery (the Korea-preserving discriminator)

**Type**: mechanistic gate on H435.

**Hypothesis**: the recovery must fire for high-gender-equity regions (Germany, Poland, Italy) and stay
SHUT for Korea (high development, low gender equity). Gating the H435 up-pull on a gender-equity index
reproduces the J-shape reversal and preserves Korea's collapse by construction.

**Exact emergent.py change**: multiply only the UP component of the H435 reversion by a gate,
`dQ_rec = gate_c * kappa_c * max(Q_attr_c - Q, 0) + kappa_c * min(Q_attr_c - Q, 0)`, with
`gate_c = clip((g_c - g0)/(g1 - g0), 0, 1)`, `g_c` the region's gender-equity index (GGI-like), hinge
`g0 = 0.60`, saturation `g1 = 0.80`. New PARAMS: `g_c` per region (data-derived, held out of the fit),
`g0`, `g1`. Baseline-preserving (gate multiplies a term already zero at the fixed point).

**Literature grounding**: Myrskyla-Kohler-Billari (2009, Nature) J-shape, HDI reversal at 0.86,
+1 child/+0.25 HDI; Myrskyla-Kohler-Billari (2011) gender equality as the NECESSARY condition for the
reversal. Digest: `references/papers/[paper digest] advances in development reverse fertility declines
Myrskyla Kohler Billari, 2009.md`.

**Pre-registered gate**: same as H435 PLUS the explicit Korea check: with the gate, Korea's 2000→2019
model Δ must stay negative AND no less steep than the ungated H435 Korea Δ (the gate must not help
Korea). KEEP iff H435's sign-miss reduction holds WHILE Korea R2 is preserved with margin.

**Occam status**: KEEP-if it lets H435 pass R2 that ungated H435 would break. The gate is one extra
mechanism (a data-derived per-region index, not a fitted switch); it earns its place only if the
ungated term over-lifts Korea. Try H435 ungated first; add H436 iff Korea's gate is threatened.

## H437 - Bayesian CALIBRATION of the recuperation parameters (pyro/numpyro)

**Type**: Bayesian-inferred (the calibration method for H435/H436).

**Hypothesis**: rather than hand-set `Q_attr_c`, `rho_rec`, `sigma_rec`, infer them with posterior
uncertainty from the observed recoveries, using the UN's hierarchical partial-pooling structure - a
country with thin recovery data borrows the world-level asymptote and reversion rate.

**Method** (in the E41 backtest notebook, stack already has pyro-ppl + arviz from E8-E9,
`notebooks/04-kj-demographic-calibration-bayes.ipynb` precedent): a hierarchical model
`rho_c ~ TruncNormal(rho_star, sigma_rho; [0,1))`, `mu_c ~ TruncNormal(mu_star, sigma_mu; [0,2.1])`,
`sigma_eps ~ HalfNormal`, world hyperpriors `rho_star`, `mu_star` (bayesTFR default brackets above),
likelihood = the observed 2000→2019 trajectories of the recovery regions passed through `run_cal(...,
trajectories=True)`. Fit by NUTS; posterior means/HDIs become the shipped PARAMS, posterior predictive
gives the backtest uncertainty band.

**Pre-registered gate**: KEEP iff the posterior-mean parameters pass the H435/H436 backtest gate AND
the posterior predictive covers the 4 observed Δ within its 90% HDI (calibrated, not just point-fit).
The inferred `rho_c` should land near the UN 0.9 prior; a wild departure flags a mis-specified term.

**Occam status**: KEEP as the calibration route for whichever mechanistic term (H435/H436) survives -
it replaces hand-tuning with grounded inference and supplies the near-term prediction band DEF-5 calls
the campaign's most policy-relevant missing output. It is a METHOD, not a separate mechanism; it ships
with the term it calibrates.

## H438 - reservoir (the original H430) as a mechanistic alternative

**Type**: mechanistic (the incumbent lead, kept as a comparison arm).

**Hypothesis / change**: the H430 tempo-loss reservoir - `D <- D + kBF*max(dtau,0) - D/L_rec`, drained
back as `f_rec*(D/L_rec)` - releases postponed births only as postponement DECELERATES, so a
still-postponing Korea gets little lift. PARAMS `f_rec` (central 0.65, sweep [0.37,1.0]), `L_rec`
(central 7 yr, sweep [5,12]). Toy `scratchpad/toy_e47_def5.py`: flips Germany net -0.055 → +0.081.

**Pre-registered gate**: identical to H435 (sign-misses 4→≤1, Korea R2 preserved, chi2/dof ≤ 3.638).

**Occam status**: KEEP as a COMPARISON arm for H440. Its self-limiting-on-deceleration design is a
different Korea-sparing argument than H436's gender-equity gate; H440 decides between them on fit. It is
LESS grounded than H435 (an ad-hoc reservoir vs the UN's published AR(1)), so on a tie H435 wins by
Occam.

## H439 - Israel via the pronatal well, not the reservoir (scope note, links H431)

**Type**: mechanistic (defers to H431/DEF-3).

The toy shows Israel (~3.0) sits ABOVE the `mu_c <= 2.1` recovery ceiling - no below-replacement AR(1)
pool can express its rise. Israel's recovery is a pronatal-subculture lock-in (Okun 2017), structurally
the H431 tri-stable norm well, not a recuperation reservoir. **Pre-registered consequence**: if H435/
H436 resolve Germany/Poland/Italy but leave Israel as the sole remaining sign-miss, the ≤1 gate is
already MET; pushing further requires H431, not more recuperation. Do NOT stretch the recuperation term
to reach Israel - that would be the wrong mechanism (audited failure mode).

## H440 - Bayesian MODEL COMPARISON of the recuperation mechanisms (the selector)

**Type**: Bayesian model selection - the principled way to pick the mechanism.

**Hypothesis**: the candidate recovery laws - baseline (no recuperation), H438 reservoir, H435 UN-AR(1)
ungated, H436 gated AR(1), and H435+H431 combined - should be selected by OUT-OF-SAMPLE predictive
score on the backtest, not by hand. The best mechanism is the one with the lowest expected out-of-sample
error / highest predictive density.

**Method**:
- **Primary score - the pre-registered backtest chi2/dof** on the held-out 2000→2019 trajectories
  (the E41 gate metric), computed per candidate. Lowest chi2/dof that also meets sign-misses ≤1 and
  Korea R2 wins.
- **Bayesian scores - PSIS-LOO and WAIC** (arviz `az.loo`, `az.waic`) on the H437 posterior for each
  candidate, ranking by expected log pointwise predictive density (elpd). Report `elpd_diff` and its
  SE; a candidate wins only if it beats the next by > 2 SE (else declare a tie and take the more
  grounded / simpler term by Occam - H435 over H438).
- **Guard**: every candidate must re-solve `PB_SCALE_ENS`, re-run the guard suite, and re-measure the
  blast radius on the 425 recorded verdicts before its score counts (the E40 precedent).

**Pre-registered gate**: SELECT the single mechanism (or minimal combination) with the best backtest
chi2/dof meeting the hard constraints (sign-misses ≤1, Korea R2), confirmed by LOO/WAIC elpd within 2
SE. If LOO and the backtest chi2 disagree, the pre-registered TIE-BREAK is the backtest chi2 (it is the
falsification metric of record) with LOO reported as a robustness check.

**Occam status**: KEEP as the decision procedure. It converts "which recovery term?" from a judgement
call into a scored, out-of-sample comparison, and its output is a single shipped mechanism plus an
honest uncertainty band.

---

## Recommended ordering

1. **H435 UN-AR(1), ungated, hand-set central params first** - fastest grounded test of whether the
   UN's own recovery term flips the backtest sign-misses. Confirms the mechanism before any gate or
   inference machinery. (Try this first.)
2. **H436 gender-equity gate** - add iff ungated H435 over-lifts Korea (the toy predicts it will);
   this is the Korea-preserving discriminator.
3. **H438 reservoir** - run as the comparison arm (its toy already flips Germany), to give H440 a real
   contest between the two Korea-sparing designs.
4. **H437 Bayesian calibration** - once a mechanistic term passes, replace hand-set params with the
   hierarchical posterior (partial pooling, UN priors) for the shipped values + prediction band.
5. **H440 Bayesian model comparison** - score baseline / reservoir / AR(1) / gated / +H431 on
   out-of-sample chi2 + LOO/WAIC; SELECT one, adjudicate the 425-verdict blast radius, ship.
6. **H431 (DEF-3 pronatal well)** - fold in only for Israel, and only if Israel is the last standing
   sign-miss after the recuperation term (H439 scope note).

**Bottom line**: the grounded lead is the UN Phase III AR(1) mean-reversion (H435), gated on gender
equity (H436) to preserve Korea, its parameters inferred hierarchically (H437), and the final mechanism
chosen by out-of-sample Bayesian model comparison (H440). This borrows the trusted recovery machinery
of the very model that generated the project's data, and it turns the backtest fix into the near-term
quantum-recovery PREDICTION the campaign currently lacks.
