# DEF-8 - Is the Magnitude Miss Caused by the Bayesian Regularization? (Diagnostic)

The E47 recuperation term passes the backtest SIGN gate (misses 4 -> 0, Korea preserved) but
FAILS the MAGNITUDE clause: chi2/dof worsens 3.93 -> 4.83, pooled RMSE 0.213 -> 0.219. The user's
load-bearing question: is that wrong magnitude caused by the Bayesian REGULARIZATION - the complete
pooling (one shared `g_rec`) and the single shared asymptote `mu_c = 1.8` shrinking every region to a
common recovery strength? This report answers it with a standalone toy that imports the shipped
`emergent.py`, reproduces the E47 notebook-local `RecupModel` and backtest, and de-pools the term
step by step. Scripts: `scratchpad/toy_def8_pooling.py`, `scratchpad/toy_def8_filter.py`; results
`scratchpad/def8_pooling_results.json`, `scratchpad/def8_filter_results.json`.

## The regularization verdict: NO

**Complete-pooling shrinkage is NOT the dominant cause of the wrong magnitudes.** De-pooling the
recovery strength recovers less than a third of the miss, and even a fully free per-region fit stays
WORSE than the down-only baseline - the mechanism cannot pay for itself on magnitude no matter how
freely it is fit.

Four regimes, pooled RMSE over all 8 regions x 24 years (in-sample):

| regime | what is freed | pooled RMSE | chi2/dof |
|---|---|---:|---:|
| `base` | down-only shipped core (no recuperation) | 0.1981 | 3.93 |
| `pool_E47` | shared `g_rec = 0.042`, shared `mu_c = 1.8` (E47's actual regime) | 0.2195 | 4.82 |
| `grec` | per-region `g_rec_r`, shared `mu_c` (no pooling on strength) | 0.2138 | 4.57 |
| `full` | per-region `g_rec_r` AND per-region `mu_c_r` (no pooling at all) | 0.2074 | 4.30 |

Decomposition of the +0.0214 total worsening (`pool_E47 - base`):

- **pooling / shrinkage of `g_rec`** (`pool -> grec`): +0.0057 - only **27%** of the miss
- **single shared asymptote `mu_c`** (`grec -> full`): +0.0064 - another **30%**
- **functional-form floor** (`full`, everything de-pooled): 0.2074 - **still +0.0093 ABOVE the
  down-only baseline (0.1981)**

The two regularization knobs the user named - complete pooling and the single asymptote - together
explain ~57% of the gap between the E47 fit and the best per-region fit, but that best per-region fit
is itself worse than doing nothing. **Freeing the regularization does not fix the magnitude; it just
shrinks a penalty that should not have been paid.** So over-regularization is a contributor, not the
cause.

## The prior is too loose to be over-regularizing either

E47's grid posterior uses a `Normal(0, 0.05)` prior with likelihood sigma 0.03 and response slope
2.871. Working in `g_rec` units:

- likelihood SD 0.0104, prior SD 0.0500, posterior SD 0.0102
- prior -> posterior contraction 4.89x
- the prior contributes **4.2%** of the posterior precision; the likelihood 95.8% (precision ratio
  22.9x)

The posterior is likelihood-dominated - the prior barely shrinks the estimate (posterior median 0.042
sits at the MLE). So the `sigma = 0.05` prior scale is NOT doing meaningful shrinkage relative to the
likelihood; it is not the source of the magnitude miss. The regularization that matters is the
POOLING (one `g_rec` for all regions), not the prior tightness - and pooling explains only ~27%.

## What actually dominates the miss: one region and a confound

The per-region RMSE table locates the damage precisely:

| region | gate | obs 2000-2019 | base | pool_E47 | full | note |
|---|---|---:|---:|---:|---:|---|
| Israel | GATED | +0.113 | 0.156 | **0.367** | 0.367 | pronatal well OVERSHOOTS, error 2.4x |
| Korea | shut | -0.587 | 0.368 | 0.368 | 0.368 | gate-shut, untouched (separate baseline miss) |
| USA | GATED | -0.346 | 0.252 | 0.236 | 0.199 | up-pull IMPROVES a decliner - level confound |
| France | GATED | -0.049 | 0.192 | 0.177 | 0.100 | same level confound |
| Germany | GATED | +0.155 | 0.105 | 0.112 | 0.100 | the poster recovery, barely moved / slightly worse |
| Italy | GATED | +0.010 | 0.095 | 0.077 | 0.066 | genuine small gain |
| Poland | GATED | +0.070 | 0.169 | 0.066 | 0.065 | the one clean win |
| Japan | shut | -0.023 | 0.075 | 0.075 | 0.075 | gate-shut, untouched |

Two mechanisms, not shrinkage, dominate:

- **The Israel pronatal well (H432) is the single biggest magnitude wrecker.** Israel's fixed
  `+0.06/yr` familism lift is uncalibrated and OVERSHOOTS: its RMSE more than doubles, 0.156 -> 0.367,
  and per-region `g_rec`/`mu_c` fitting does nothing for it (the well is a separate constant, not the
  `g_rec` channel). Israel alone adds ~0.21 of RMSE in its own column - it drives the pooled worsening
  more than the entire pooling effect. The contrarian "one region dominates the chi2" hypothesis is
  CONFIRMED before it is even pre-registered.
- **The up-pull fires on gated decliners (USA EQ 0.65, France 0.70) as a level-bias confound.**
  USA's observed 2000-2019 change is -0.346, yet its best `g_rec_r` is +0.16 (grid ceiling) toward
  `mu_c = 2.0` - a positive recovery pull is REDUCING USA's error because the down-only baseline
  undershoots the early-2000s level (~2.05). The term is compensating a baseline LEVEL mis-specification,
  not tracking a recovery. That is a confound: the magnitude "improvement" on USA/France is the term
  doing the wrong job for the right-looking reason.

Meanwhile Germany - the recovery the whole mechanism was built for - is essentially unmoved (0.105 ->
0.100) and E47's shared pull slightly WORSENS it. The recuperation buys almost nothing on the two
clean European recoveries (Germany, Italy) and its one real win is Poland.

## Out-of-sample: de-pooling makes magnitude WORSE (the state-space probe)

Fitting on 2000-2011 and scoring held-out magnitude on 2012-2023 (`toy_def8_filter.py`, using E47's
established linear-in-`g_rec` response as an exact two-point emulator):

| method | held-out 2012-2023 pooled RMSE |
|---|---:|
| E47 shared pool (`g_rec = 0.042`) | **0.2082** |
| static per-region `g_rec_r` | 0.2287 |
| per-region point-mass FILTER (best, random-walk sigma 0.03) | 0.2206 |

**Per-region tuning generalizes WORSE than the shared pool out-of-sample.** Germany is the tell: its
2000-2011 fit gives `g_rec = -0.075` (its recovery is post-2011), which then does terribly on the
held-out decade (0.251 vs the pool's 0.065). This is Gelman's few-groups lesson exactly - with thin
per-group data, no-pooling overfits and can lose to complete pooling; the cure is PARTIAL pooling, not
no-pooling. The filter (adding a predict->update time recursion over the `g_rec_r` grid) improves
monotonically as it is allowed to track time-variation but never beats the simplest shared pool. The
state-space formulation "gets a hold" only marginally and does not move the numbers - a clean
pre-registered prune.

## Grounding digested

- **Gelman (2006), "Prior distributions for variance parameters in hierarchical models"**, Bayesian
  Analysis 1(3) - downloaded OA, digest in library. The complete-pooling corner is `tau_g -> 0`; with
  few groups `tau_g` is weakly identified and the prior on it does real work; use half-t / half-Cauchy,
  never inverse-gamma; uniform(0, A) proper for J >= 3. Directly grounds the partial-pooling fanout.
- **Alkema et al. (2011) / Raftery et al. (2014)**, the UN WPP Bayesian hierarchical Phase III AR(1) -
  already in library (`[paper digest] bayesian population projections ... Raftery, 2014.md`). Supplies
  the country-specific asymptote `mu_c` and reversion `rho_c` estimated by partial pooling - the
  data-derived per-region asymptote the mainstream act calls for.

Both were already cited by E47; no new non-OA sources were needed. Only the Gelman paper was newly
downloaded (it is the load-bearing partial-pooling-for-few-groups reference).

## Bottom line for the fanout

The magnitude miss is not a shrinkage artifact - it is (1) the uncalibrated Israel pronatal well
(single-region, gate the whole thing on this), (2) the up-pull as a level confound on gated decliners,
and (3) a functional-form floor that sits above the down-only baseline. The make-or-break question is
therefore the CONTRARIAN one: is recovery DEPTH identifiable from 8 countries x ~20 years at all, or is
per-region magnitude fitting just fitting noise that generalizes worse than pooling? The mainstream
partial-pooling cure is worth one clean test, but the diagnostic predicts it will only claw back ~0.006
of RMSE - short of clearing the bar - unless it is paired with fixing Israel's well and de-confounding
the decliner level bias.
