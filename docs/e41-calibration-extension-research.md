# E41 Research Dossier - Extending Calibration to Multi-Observable Targets

**Research dossier** (pre-round). This document records the E41 deep-research campaign: mapping every
introduced model parameter to a real-world observable with actual numbers for all 8 regions, so the
calibration can extend beyond the single 2023 TFR anchor and every parameter carries a checkable
prediction. Machine-readable payload (all values, sources, URLs, notes, the full synthesis and both
critiques): `reports/e41_calibration_targets_research.json`. Produced by a 20-agent workflow
(3 inventory readers → 9 observable-family researchers → synthesis → 2 adversarial critics → gap-fill);
16 of 20 agents completed - 4 gap-fill agents were lost to a session limit and their gaps remain open
research items listed below. **Nothing in this dossier has been applied to the model**: the protocol
below is a proposal awaiting the E41 round and user approval.

## Why

The behavioural core is calibrated to exactly one number per region - the 2023 TFR - through one fitted
parameter (`PB_SCALE_ENS`). The per-region state anchors C0 (coupling), RV0 (childlessness), S0
(security) and NORM0 (childfree-ideal norm) are hand-set judgment calls with no citations, and the rich
internal trajectories (channel states, births, dependency, the quantum/fec/tempo decomposition) are
computed every year and thrown away. E40 hardened the mathematics; E41 grounds the state.

## The targets (headline values; full provenance in the JSON)

| family | USA | France | Germany | Italy | Japan | Korea | Poland | Israel |
|---|---|---|---|---|---|---|---|---|
| cohort childlessness (women ~b.1965-78, share) | 0.165 | 0.14 | 0.20 | 0.23 | 0.27 | 0.19 | 0.103 | 0.078 |
| completed cohort fertility (b.~1975) | 2.22 | 2.03 | 1.58 | 1.43 | 1.43 | 1.59 | 1.60 | 3.09 |
| mean age at first birth 2023 (yr) | 27.5 | 29.1 | 29.8 | 31.8 | 31.0 | 33.0 | 28.4 | 27.7 |
| partnership share, women 25-39 (married+cohab) | 0.57 | 0.64 | 0.46 | 0.38 | 0.53 | 0.66 | 0.61 | 0.55 |
| childfree ideal share | 0.02 | 0.015 | 0.075 | 0.035 | 0.056 | 0.426 | 0.02 | - |
| tempo-adjusted TFR (B-F adjTFR, latest) | 1.82 | 1.87 | 1.42 | 1.45 | 1.42 | 1.01 | 1.46 | - |
| young-adult co-residence w/ parents 25-34 | 0.18 | 0.16 | 0.13 | 0.51 | 0.38 | 0.55 | 0.53 | 0.32 |
| period TFR 2023 (trajectory series in JSON) | 1.62 | 1.64 | 1.44 | 1.20 | 1.21 | 0.72 | 1.16 | 2.83 |
| crude marriage rate, latest (per 1000) | 6.1 | 3.5 | 4.2 | 2.9 | 3.9 | 4.4 | 3.6 | 5.5 |
| net migration rate (per 1000, 2023; gap-fill) | 3.9 | 1.4 | 7.2 | 2.5 | 1.4 | 1.7 | −0.2 | 1.1 |

Sources per family: HFD/VID (tempo-adjusted), Eurostat (`demo_find`, `ilc_lvps08`, `demo_nind`), OECD
Family Database (SF2.1/SF2.3/SF2.5), national offices (Destatis, ISTAT, INSEE, GUS, KOSIS/Statistics
Korea, Statistics Bureau of Japan/MHLW, Israel CBS, US Census/Pew/NCHS), UN WPP 2024 (local
`data/raw/unwpp`, incl. cohort ASFR diagonals computed locally), Sobotka/Testa/Miettinen for norms.
Two nulls remain (Israel childfree-ideal share, Israel adjTFR) - both flagged with where to look.

## The seven anchor replacements (synthesis)

1. **REAL[r][1] relabel** - the code comment says "mean age at first birth" but the values are UN WPP
   mean age at CHILDBEARING (MAC); relabel and re-pin to the on-disk 2023 MAC series
2. **Germany TFR rebase** - WPP 1.44 vs Destatis Zensus-rebased 1.38: adopt the national-office
   convention already applied to Poland (GUS) and Korea (KOSIS)
3. **C0 data-derived** - affine map from harmonized union share (endpoints Korea 0.52 / Israel 0.97
   preserved; Poland, Japan and Italy get interior corrections)
4. **RV0 derived** - `RV0 = 1 − (1 − p0_obs)/C0` from cohort childlessness (no longer hand-set)
5. **S0 operationalised** - gauge fixed from parental co-residence 25-34 (only S−S0 deviations enter
   the dynamics, so this is an operationalisation, not a fit)
6. **NORM0 decision fork** - (A) latent-index reinterpretation calibrated on observed ordering only,
   or (B) well relocation (structural - forces E25-E39 re-runs); recommendation: A this round
7. **PB0 cross-check** - keep the identity, add the independent check from completed cohort fertility;
   report `|PB0 − PB0_check|/PB0 < 10%` per region

## Protocol, harness, backtest (proposal)

- **Protocol** - staged, closed-form-first: Stage 0 definitions (labels, source conventions, the
  MAC-vs-MAB1 fork recorded but not acted on), Stage 1 static anchor replacement in dependency order
  (MAC → C0 → RV0 → PB0 auto-recompute + cross-check → PB_SCALE_ENS re-solve), later stages only with
  an optimizer over 3-4 scalars against the trajectory witnesses
- **Observability harness** - additive `trajectories` dict on `run()/run_ens()/run_cal()` (existing
  keys unchanged): all 7 channel states per year, the TFR decomposition (quantum/fec/tempo/dtau,
  model-adjTFR), and the currently-discarded Leslie observables (births, deaths, total population,
  dependency ratio, dep_pen) - every introduced parameter then has a named, checkable prediction
- **Backtest 2000-2023** - a rejection test, not a fit: initialize a 2000-era state from the same
  observable families (earlier vintages, on-disk WPP MAC 2000, cohort childlessness of ~b.1955-60) and
  demand the model reproduce the observed TFR path and marriage-decline witness

## What the critics flagged (must be resolved in the E41 round)

Both adversaries returned MAJOR-revisions verdicts on the synthesis (18 blocker/major findings; all in
the JSON). The recurring ones: the cohort-to-state lag (cohort childlessness describes women born
1965-78, not the 2023 period state - Korea worst), the partnership harmonisation gap (marriage-only
census values vs cohabitation-inclusive definitions across regions), backtest degeneracy (secC/secPb
trade off on monotone declines), PB_SCALE_ENS as silent absorber (if |scale−1| grows after re-anchoring,
the exercise re-labelled error rather than removing it - make it a reported diagnostic), and the
Germany-TFR source fork moving the region relative to the TFR-1.5 ridge. Open research gaps from the
lost gap-fill agents: parity distributions (0/1/2/3+) beyond the aggregates, Israel norm/adjTFR nulls,
and q/scarring-channel observables (structurally hard - likely `fix_type=none`).

## Wave 2 - blocker resolution outcome (v2)

The 18 findings were driven through a resolver → synthesis → re-critique workflow (`wf_53322579-da8`,
19 agents, 0 errors); the full disposition table, protocol v2, delivered values and both re-critiques
are persisted at `reports/e41_blocker_resolutions.json`. Every finding now carries a disposition: 9
RESOLVED with delivered data, 9 AMENDED with replacement protocol text, none left OPEN, zero remaining
BLOCKER. Both adversarial critics re-ran to a MINOR-REVISIONS verdict.

- **Three blockers cleared** - C0F0 (C-construct) reproduced then resolved by design: the period
  feasibility screen is PB0 ≥ 1.15 (= 1 + SIGMA_CAL[Pb]), checked 8/8; Korea alone decouples to a
  period-epoch pair C0=0.70 / RV0=0.09 (PB0=1.236) grounded in Yoo 2026, Demographic Research 54(3)
  (tempo-adjusted marriage quantum PPEM\* 0.698, 2023); C1F0 (q channel) gets the Wilson
  marriageable-men family MM = SR(25-44)·male-emp(25-54) for 8 regions × 2000/2010/2023, flat for 6/8
  so the q=0 baseline gains support; C1F1 (migration) validated 80/80 against on-disk WPP and wired as
  observed NetMigrations × Rogers-Castro for the 2000-2023 backtest only, forward runs stay
  natural-increase-only
- **New observable families delivered** (41 values, 13 families): annual live births 8×2019-2025
  (national offices, 2025 provisional), completed-cohort parity 0/1/2/3+ for the 5 null regions,
  Israel adjTFR computed locally (tempo gap +0.165 collapsing to ~0 by 2022-23 → Israel's ~2.9 TFR is
  quantum not tempo), old-age dependency OADR 8×2000-2023, fecundity slope cross-checked against
  Leridon 2004, ideal-zero norm points where a same-instrument panel exists
- **Protocol v2** (7 stages, closed-form first) - Stage 0 definitions → Stage 1 static anchors → Stage
  2 re-anchor PB_SCALE_ENS → Stage 3 dynamics (only optimizer stage) → Stage 3b epoch-matched cohort
  composition check → Stage 4 kBF adjudicated on GAP DYNAMICS (G = 1 − TFR/adjTFR), not levels → Stage
  5 re-verdict gate + honesty table + guard re-baselining; the discredited |PB_SCALE_ENS−1| honesty
  metric is deleted and replaced by a per-stage PB0-convergence table against the epoch-matched cohort
  reference
- **Residual MAJORs (not blockers) - deferred to Wave 3 as caveats**: the two round-2 critics still
  flag a handful of MAJOR revisions, all on the C0F0 Korea/Israel decoupling - the Korea PB0 moves
  away from 1 so its honesty-table gap widens and must be disclosed; the delivered ideal-zero ordering
  puts Korea at the bottom, which sits awkwardly with option A's "NORM0 is a latent index on observed
  ordering" justification; Israel's cohort childlessness (p0≈0.11 at 40-44) is contested by its own
  source and leaves the feasibility margin thin; the Korea RV0 band edge sits against a census-exact
  0.065. None reopen a blocker; each is a Wave-3 implementation decision, recorded in the disposition
- **Remaining gaps** (13, unchanged scope) - Poland late-cohort p0 bracketed 0.10-0.20, the E30
  scar/intergenerational block stays unobserved (intervention-only), norm well stiffness fits only as
  stiff (all ideal series flat), migration identically zero for forward runs, several parity fine-splits
  live only in supplementary tables

## Status

Wave 1 (research) and Wave 2 (blocker resolution) complete and persisted; model untouched. Every
blocker is cleared and protocol v2 is written, but the re-critique closed at MINOR-REVISIONS, not a
fully clean bar - a residual MAJOR set on the C0F0 decoupling is recorded as Wave-3 caveats rather
than silently marked resolved. Wave 3 (implementation: anchor replacement, guard re-baselining,
additive observability harness, 2000→2023 rejection backtest) is USER-GATED and not started.
