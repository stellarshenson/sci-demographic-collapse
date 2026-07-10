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

## Status

Research complete and persisted; model untouched; E41 round (implementation + verification against
these targets) not yet started. The 2 remaining nulls and the lost gap-fills are the first work items
of the round.
