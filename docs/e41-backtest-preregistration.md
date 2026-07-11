# E41 Backtest Pre-Registration - 2000→2023 Rejection Test

Pre-registered pass/fail bars for the E41 Wave-3 backtest (protocol v2 Stages 3, 3b, 4), written
BEFORE the run per W3.4. The backtest is a REJECTION test of the calibrated core's drift structure,
not a fit of the production model: results are recorded whichever way they land. Executed in
`notebooks/37-kj-e41-backtest.ipynb`; machine results in `reports/e41_backtest_results.json`.

## Design (frozen)

- **Runner** - the calibrated ensemble core (K=64, seed 0, SIGMA_CAL, PB_SCALE_ENS), started at the
  year-2000 pyramid/Sx/ASFR/SRB (on-disk WPP), with the secular clock shifted: tn = (year−2023)/100
  runs from −0.23 to 0, so the model's 2023 state IS the Stage-1 anchor state by construction
- **2000 init per channel** - tau = observed WPP MAC 2000; q = Wilson MM q(2000) (C1F0, eps 0.3);
  C = C0 + 23·secC, Pb = (PB0·pb_scale) + 23·secPb (the candidate drift's own 2000 equilibrium);
  rv = RV0 (declared - no b.1955-60 cohort observable was delivered; sensitivity ±0.02 reported);
  N = NORM0 (declared - all ideal series flat, norm wells stiff); S = S0 (gauge)
- **Migration** - observed WPP NetMigrations (thousands, `scratchpad/c1f1_netmigration_2000_2023.json`)
  × the normalized Rogers-Castro schedule, added in `leslie_step` - backtest ONLY, forward runs stay
  natural-increase-only; post-migration bins must be non-negative every region-year (tripwire)
- **Fitted parameters** - global {secC, secPb, secTau, kTau} (4 params, shared across regions),
  bounded: secC ∈ [0, 0.01], secPb ∈ [0, 0.02], secTau ∈ [0, 0.06], kTau ∈ [0.01, 0.3]
- **Loss** - WLS over the retained window: TFR residuals (annual on-disk WPP; Poland on GUS, Korea on
  KOSIS delivered points) with s_eff = √(0.03² + 0.08²) = 0.0854 (s_struct = 0.08 declared, C0F8);
  MAC residuals (annual on-disk WPP) with s_MAC = 0.15 yr; marriage witness (crude marriage rate,
  delivered 5-point series) as normalized-decline residuals (C_t/C_2000 vs CMR_t/CMR_2000) with
  s_M = 5%; weights 1 / 1 / 0.5; residuals standardized then Huber (delta = 1.345)
- **Exclusions (declared before the first loss eval)** - Germany 2006-2016 and Japan 2006-2015
  (Tier-2 qualitative episodes), COVID 2020-2022, all series
- **Out of scope (named follow-on)** - PROMOTION of the fitted drift constants into the shipped
  PARAMS is not part of this round: it would re-open every forward-run verdict. The fitted values
  are recorded as the backtest's finding only; the shipped model keeps its constants

## Bars

- **B1 (Stage 3, WLS gate)** - chi2/dof ≤ 2 on the retained window at the fitted optimum
  (dof = N − 4). If exceeded: s_struct = 0.08 is FALSIFIED for this model class - no WLS rejection
  verdict is issued and rejection authority passes to the Tier-2 battery (B5); the chi2/dof value
  is recorded either way
- **B2 (Stage 3b, cohort composition)** - the b.1975 spliced pseudo-cohort CFR gap
  |CFR_model − CFR_obs|/CFR_obs < 0.10 per region, 8/8. CFR_obs = the b.1975 ASFR diagonal from
  on-disk `fertility_by_age1.csv` (ages 15@1990 → 48@2023), cross-checked to the delivered CFR
  family (tol 0.05); CFR_model = observed splice ages 15-24 (1990-1999, pre-window) + backtest
  birth profiles ages 25-48. A failure indicts that region's quantum composition - LOG, do not tune
- **B3 (Stage 4, kBF adjudication)** - scored on GAP DYNAMICS only (level-scoring banned, C0F1):
  chi2_G(kBF) = Σ[(kBF·dtau_model − G_obs)/sigma_G]², G_obs = 1 − TFR/adjTFR,
  sigma_G = 0.1·TFR/adjTFR², both sides 3-yr smoothed, grid {0.4, 0.6, 0.8, 1.0}. WINDOW DEVIATION
  (named): the delivered adjTFR series span 2011-2022, not the protocol's 2000-2019 - the window is
  the delivered span ∩ [2000, 2019] (COVID years excluded); France (no series) and Israel (null)
  are excluded, leaving 6 regions. KEEP kBF = 0.6 unless the argmin beats chi2_G(0.6) by > 4.0;
  a move returns to Stage 2 once and updates the kBF guard + tempo-bump band in the same commit
- **B4 (migration tripwire)** - non-negative post-migration population bins for every region-year;
  any violation aborts and is recorded
- **B5 (Tier-2 rejection battery, qualitative)** - the model is REJECTED on the backtest iff any of:
  (R1) the SIGN of the observed 2000→2019 TFR change is missed for ≥ 2 of 8 regions;
  (R2) Korea's monotone decline is missed (model TFR(2019) not within 0.15 of observed 0.918, or
  the model path rises over 2015-2019 while the observed path falls);
  (R3) the MAC direction is missed (model tau must RISE 2000→2023 in all 8 regions, as observed);
  (R4) the marriage-witness direction is missed (model C declines 2000→2023 in ≥ 6 of 8 regions
  wherever the observed crude marriage rate declined)
- **B6 (honesty)** - the per-region-year (G_model, G_obs, sigma_G) triples, the chi2_G grid, the
  standardized-residual distribution, and any systematic residual sign are recorded in the results
  JSON; a systematic tempo-residual sign is logged as a scope finding, not tuned away

## Interpretation grid (frozen)

- B1 pass + B5 pass → the drift structure is CONSISTENT with the observed 23-year paths (the round
  records the fitted constants and their gap to the shipped defaults as a finding)
- B1 fail + B5 pass → s_struct falsified: the model tracks direction and magnitude qualitatively
  but the declared error model understates structure; recorded, no rejection verdict
- B5 fail (any R) → the backtest REJECTS the core's drift structure; the failure mode is named in
  the experiments log and the SOTA's validity-domain section is amended
- B2 failures indict the named region's quantum composition (scope finding); B3 moves kBF only
  through its own gate
