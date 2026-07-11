# DEF-8 Magnitude Fanout - Pre-Registered Hypotheses H451-H463

The E47 recuperation passes the SIGN gate but fails the MAGNITUDE clause (chi2/dof 3.93 -> 4.83, RMSE
0.213 -> 0.219; DEF-8). The diagnostic (`reports/def8_magnitude_research.md`) already settled the
user's load-bearing question: **complete-pooling shrinkage is NOT the dominant cause** - it explains
~27% of the miss, the prior is too loose to over-regularize (4% of posterior precision), and even a
fully de-pooled per-region fit (RMSE 0.207) stays WORSE than the down-only baseline (0.198). The miss
is dominated by the uncalibrated Israel pronatal well (single-region, error 2.4x) and by the up-pull
acting as a level-bias confound on gated decliners. This fanout pre-registers the fixes that follow
from that diagnosis, across three stances plus a state-space act.

**Numbering**: H435-H440 reserved (quantum-probe), H441-H450 reserved (SINDy). This round is H451-H463.

**Scoring convention (all acts)**: score on MAGNITUDE, out-of-sample where possible. Two reference
bars: E47 in-sample pooled RMSE **0.219**, and the honest held-out (fit 2000-2011, score 2012-2023)
shared-pool RMSE **0.208** (the number any de-pooling must beat to justify its extra parameters). Every
hypothesis carries the hard constraints: must NOT break the sign gate (misses <= 1 of 8) and must NOT
lift Korea out of its monotone collapse. **Occam gate (governing rule)**: KEEP only if the fix
demonstrably lowers held-out magnitude RMSE materially (>= 0.010 vs the relevant baseline) AND holds
sign + Korea; else REMOVE and record the negative.

---

## Act I - Mainstream (the standard partial-pooling cures)

### H451 - Partial-pooling hierarchical recovery strength

- **Claim**: replacing the single shared `g_rec` with a hierarchical `g_rec_r ~ Normal(mu_g, tau_g)`
  (Gelman half-Cauchy on `tau_g`) is the textbook cure for complete-pooling shrinkage and lowers the
  magnitude RMSE
- **Equation**: `g_rec_r ~ Normal(mu_g, tau_g)`, `tau_g ~ HalfCauchy(0, 0.05)`, `mu_g ~ Normal(0, 0.05)`;
  per-region pull `dPb += dt * g_rec_r * gate_r * max(mu_c - quantum, 0)`
- **Pass bar**: held-out RMSE < 0.198 (beats E47's 0.208 by >= 0.010) with sign + Korea held
- **Prediction**: partial pooling lands between complete-pool (0.208) and no-pool (0.229 held-out);
  the toy already shows no-pool is WORSE out-of-sample, so partial pooling most likely lands ~0.208-0.229
  and does NOT clear the bar; `tau_g` posterior likely small (data prefer pooling)
- **Honest-negative**: if `tau_g -> 0` (data want complete pooling) or partial-pool fails to beat the
  shared pool, pooling was never the problem - prune, keep E47's single `g_rec`, record that the
  regularization was correctly calibrated
- **Occam gate**: KEEP only on a material held-out win; the diagnostic predicts REMOVE

### H452 - Per-region data-derived asymptote

- **Claim**: the single shared `mu_c = 1.8` mismatches heterogeneous rebound ceilings; replacing it
  with each region's Alkema-Raftery / Sobotka Phase III asymptote fits the depths
- **Equation**: `mu_c_r` set from each region's estimated post-transition ceiling (held out of the fit,
  data-derived), pull uses `max(mu_c_r - quantum, 0)`
- **Pass bar**: held-out RMSE improvement >= 0.010 attributable to `mu_c` freeing, over shared-1.8
- **Prediction**: in-sample the free `mu_c` bought only +0.0064; a data-fixed `mu_c_r` will buy less;
  unlikely to clear a material bar out-of-sample
- **Honest-negative**: if data-derived asymptotes do not materially beat 1.8, the shared ceiling was
  adequate - prune
- **Occam gate**: KEEP only if `mu_c_r` beats shared-1.8 AND beats a freely-fit `mu_c` per region
  (i.e. the grounding, not just the freedom, earns it)

### H453 - Explicit magnitude likelihood (fit depth and timing, not sign)

- **Claim**: E47's selector sorts on sign-misses (the quantity the arm was tuned to zero); a selector
  scored on the full-trajectory magnitude likelihood is the honest test and will re-rank the mechanisms
- **Equation**: select by chi2/dof (or elpd) on the full 2000-2023 trajectory, not by sign-miss count
- **Pass bar**: the magnitude-selected model has chi2/dof <= 3.93 (does not worsen baseline) while
  holding sign + Korea
- **Prediction**: the honest selector REJECTS the recuperation on magnitude (it is above baseline) and
  selects the down-only baseline or a near-zero `g_rec` - i.e. it correctly declines the term
- **Honest-negative (the likely finding)**: the magnitude-honest likelihood picks baseline/near-zero
  recovery - the recuperation is a sign-only fix; record it as such, do not ship it as a magnitude fix
- **Occam gate**: this IS the Occam adjudicator for the whole fanout - the term ships on magnitude only
  if it clears this

---

## Act II - Contrarian (attack the premise)

### H454 - The magnitude should NOT be fit: per-region tuning is fitting noise [MAKE-OR-BREAK]

- **Claim**: 8 countries x ~20 years is too thin to identify per-region recovery depth; per-region
  tuning overfits and the honest RMSE-worsening is the correct price of a real-but-coarse mechanism
- **Test**: leave-one-region-out and held-out-years - does per-region `g_rec_r` beat the shared pool
  OUT-OF-SAMPLE?
- **Pass bar**: per-region held-out RMSE < shared-pool held-out RMSE (0.208) - i.e. de-pooling
  generalizes
- **Prediction**: the toy already shows NO - per-region held-out 0.229 > pool 0.208; Germany's
  2000-2011 fit gives `g_rec = -0.075` and craters on the post-2011 recovery. Per-region tuning loses
  out-of-sample (Gelman few-groups lesson)
- **Honest-negative branch (here the positive branch)**: if per-region DID generalize, depth is real
  and fittable and the mainstream act is warranted
- **Occam gate**: if de-pooling loses out-of-sample, KEEP the shared pool and RECORD the honest
  RMSE-worsening as the correct price of a coarse-but-real sign mechanism - and PRUNE the entire
  de-pooling / state-space program (H451/H452/H461/H462) as pre-empted

### H455 - Recovery depth is unidentifiable (only the sign is)

- **Claim**: from this data only the recovery SIGN is identifiable; depth is not separable - tie to the
  E49 SINDy excitation-floor finding that low-amplitude signal below the noise floor is unrecoverable
- **Test**: are the per-region `g_rec_r` posteriors well-separated, or do they overlap so much that a
  single `g_rec` lies inside every region's CI?
- **Pass bar**: DEPTH is declared identifiable only if the per-region 90% CIs are mutually exclusive
  for at least Germany vs Poland (the deepest vs shallowest true recoveries)
- **Prediction**: the CIs overlap heavily; the shared `g_rec` CI [0.025, 0.059] already spans the
  per-region point estimates (Germany 0.01-0.02, Poland 0.04-0.12) - depth is not separable at n=20yr
- **Honest-negative**: if per-region depth CIs ARE well-separated and exclude each other, depth is
  identifiable - then H451/H452 are justified and should be run
- **Occam gate**: if unidentifiable, no per-region depth model can be trusted - prune to the shared
  sign mechanism

### H456 - The chi2/dof worsening is dominated by ONE region [cheapest first probe]

- **Claim**: the magnitude miss is a single-region, error-model artifact (Israel's uncalibrated
  pronatal well), not a systemic mechanism failure
- **Test**: recompute pooled chi2/dof and RMSE (a) excluding Israel and (b) with Israel's well
  recalibrated to its observed rebound ceiling instead of a fixed +0.06/yr
- **Pass bar**: if excluding / recalibrating Israel removes >= 60% of the pool-vs-base worsening, the
  miss is single-region
- **Prediction**: CONFIRMED by the diagnostic - Israel's RMSE goes 0.156 -> 0.367 under the fixed well,
  ~0.21 of error in its own column, dominating the +0.0214 pooled worsening; recalibrating that ONE
  constant removes most of the magnitude miss
- **Honest-negative**: if the miss persists with Israel excluded, it is systemic across the recovering
  regions - then the mechanism, not the error model, is at fault (escalate to Act I)
- **Occam gate**: if single-region, the "fix" is to recalibrate the Israel well (one scalar), NOT to
  build hierarchical or state-space machinery - the cheapest admissible fix wins

---

## Act III - Heretical (unconventional mechanisms)

### H457 - The miss is a composition (tempo/cohort) artifact the sign test masks

- **Claim**: the depth error is not the recuperation's fault but a period-tempo component in the
  observed rebound that a quantum-only term mis-times
- **Equation**: decompose the per-region residual into quantum vs tempo (dtau) contributions; if depth
  error correlates with tempo, add a bounded tempo carry (E40-safe, floored)
- **Pass bar**: the residual-vs-tempo correlation explains >= 0.010 of RMSE when re-timed
- **Prediction**: PARTIAL - Germany's recovery is quantum (E46, MAC rose monotonically), so tempo
  cannot rescue its depth; Italy/Poland residuals may carry some period structure
- **Honest-negative**: if the residual is white / uncorrelated with tempo, composition is not the
  story - prune
- **Occam gate**: KEEP a tempo carry only if it cuts magnitude RMSE without reintroducing the E40
  Bongaarts-Feeney defect (no substep rate-sum, factor floored at 0)

### H458 - Non-parametric per-region recovery, and what it costs

- **Claim**: drop the parametric shared-strength model for a free per-region recovery path (a smooth
  residual spline), and measure what the model LOSES in interpretability and generalization
- **Equation**: replace `g_rec * max(mu_c - quantum, 0)` with a per-region smooth `f_r(t)` fit to the
  residual
- **Pass bar**: the non-parametric held-out RMSE must beat the shared pool (0.208) to justify the loss
  of a mechanism
- **Prediction**: fits in-sample trivially, generalizes WORSE (overfit thin data), and loses all
  mechanistic interpretability and any forward-prediction claim
- **Honest-negative (the point)**: it does not beat the pool out-of-sample and forfeits interpretability
  - record that free-form recovery is not the answer, the parametric mechanism is preferred even when
  it fits worse
- **Occam gate**: REMOVE unless the held-out win is large enough to pay for losing the mechanism

### H459 - The asymptote is endogenous (couples to the region's norm well)

- **Claim**: a region recovers toward its own norm-well floor (the N state, DEF-3), not a universal
  1.8/2.1; the asymptote is endogenous, which also replaces the ad-hoc Israel constant with a mechanism
- **Equation**: `mu_c_r = g(N_r)` - the pronatal (low-N) well sets a high attractor for Israel, the
  antinatal (high-N) well a low one for Korea/Italy; the pull reverts toward `mu_c_r(N)`
- **Pass bar**: N-coupled `mu_c` beats BOTH shared-1.8 AND a freely-fit per-region `mu_c` out-of-sample
  (fewer free parameters, mechanism-grounded), and it must subsume the Israel well (H432) rather than
  add to it
- **Prediction**: promising for Israel - the pronatal N-well is its real attractor, so this could
  replace the overshooting +0.06/yr constant that H456 flags with a self-limiting mechanism
- **Honest-negative**: if N-coupled `mu_c` does not beat a free `mu_c`, the endogeneity adds nothing -
  prune to the simpler asymptote
- **Occam gate**: KEEP only if it both lowers magnitude RMSE and retires the Israel well (one mechanism
  replacing two ad-hoc terms is the Occam win)

### H460 - Null: recuperation is a sign-only correction, accept DEF-8 as residual

- **Claim**: the recuperation is admissible as a SIGN fix only; magnitude is out of scope for this
  mechanism; keep E47 as-is and document DEF-8 as an accepted residual
- **Test**: does ANY of H451-H459 / H461-H463 clear a material held-out magnitude improvement over the
  shared pool (0.208)?
- **Pass bar**: this null STANDS unless some fix beats 0.198 held-out with sign + Korea held
- **Prediction**: given the diagnostic (best de-pooled fit still above baseline; de-pooling loses
  out-of-sample), the null is the likely survivor - modulo H456 (recalibrating Israel's well, which is
  an error-model fix not a mechanism change)
- **Honest-negative**: if a fix DOES clear the bar, H460 is refuted and that fix ships
- **Occam gate**: the null is the default; the burden is on every other hypothesis to beat it

---

## Act IV - State-space / filtering (does it move the numbers?)

Reuses E47's already-reviewed grid-posterior code and the existing 64-strand ensemble (already a
particle cloud for an ensemble/particle filter over the full state). Each is toy-tested cheaply via the
established linear-in-`g_rec` emulator before any recommendation.

### H461 - Per-region grid / point-mass filter for g_rec_r

- **Claim**: E47's static grid posterior (prior x likelihood on a scalar grid, cumsum-normalised) is
  the STATIC case of a point-mass filter; adding a predict->update time recursion per region (push the
  `g_rec_r` grid mass through the ODE transition, re-weight by observed TFR each step) yields a
  time-resolved recovery-uncertainty band and a better estimate
- **Equation**: predict `p_t^-(g) = (p_{t-1} * N(0, sigma_walk^2))(g)`; update
  `p_t(g) propto p_t^-(g) * N(TFR_obs_t | model(g, t), sigma_obs)`
- **Pass bar**: per-region grid-filtered `g_rec_r` beats the shared-pool E47 fit on out-of-sample
  (leave-one-region-out / held-years) magnitude RMSE by >= 0.010
- **Prediction**: FAILS - the toy shows the filter's best held-out RMSE 0.221 (sigma_walk 0.03) beats
  the static per-region 0.229 but never the shared pool 0.208; a filter over a CONSTANT parameter with
  linear-Gaussian observation collapses to the static posterior, so the recursion only helps if
  `g_rec` is genuinely time-varying, which it is not enough to matter here
- **Honest-negative**: if the recursion does not beat the one-shot per-region fit AND does not beat the
  pool, the filter adds nothing over a static estimate - prune it (the time-resolved band remains a free
  by-product if any per-region fit is ever kept)
- **Occam gate**: REMOVE - the diagnostic already shows no material out-of-sample gain

### H462 - Mechanistic POMP with partial pooling

- **Claim**: recast the recuperation as a partially-observed Markov process - the ODE stays the
  transition (interpretability preserved), plus an explicit observation model separating process from
  observation noise, with partial pooling `g_rec_r ~ Normal(mu_g, tau_g)`; this gives a real likelihood
  (fixing E47's circular sign-first model comparison) and an honest error model (fixing the chi2/dof
  ambiguity)
- **Equation**: state `x_t` (the 7-channel ensemble) evolves by the ODE + process noise `eta_t`;
  observation `TFR_obs_t = h(x_t) + epsilon_t`, `epsilon_t ~ N(0, sigma_obs^2)`; hierarchical
  `g_rec_r ~ Normal(mu_g, tau_g)`
- **Pass bar**: the POMP likelihood + partial pooling beats E47 out-of-sample (held-out RMSE < 0.198)
  AND holds sign + Korea
- **Prediction**: FAILS on magnitude - the honest error model will attribute most of the residual to
  OBSERVATION noise (the single-region Israel overshoot + the decliner level confound), so the
  mechanism likelihood will not improve the fit; it matches a plain hierarchical prior on the current
  grid fit
- **Honest-negative**: if a mechanistic SSM matches a plain hierarchical fit, the SSM machinery is
  interpretability-neutral overhead - Occam prefers the simpler hierarchical fit (H451). Its real value,
  if kept, is the honest likelihood that settles H453/H434, not a magnitude gain
- **Occam gate**: KEEP the honest-likelihood framing only if it changes a verdict (H453/H434); REMOVE
  the state-space machinery if it does not beat the hierarchical fit on magnitude

### H463 - Does filtering "get a hold", or just diffuse interpretability? (adjudicator)

- **Claim**: a head-to-head decides whether the state-space formulation substantially helps MAGNITUDE
  while preserving interpretability, or merely diffuses it for no fit gain
- **Test**: score on the same held-out magnitude metric: (a) E47 shared pool, (b) static per-region,
  (c) per-region grid filter, (d) POMP + partial pooling, (e) a black-box latent-linear SSM (the
  interpretability-diffusing control / floor)
- **Pass bar**: the mechanistic options (c, d) either beat (a, b) materially (>= 0.010) or are pruned;
  the black-box (e) must beat the mechanistic options by a WIDE margin or is rejected outright
- **Prediction**: from the toy, (a) 0.208, (b) 0.229, (c) 0.221 - the mechanistic filter does NOT beat
  the shared pool; (d) predicted to match the hierarchical fit; (e) the black-box will overfit worse
  still. The pre-registered expectation is that the whole filtering act is PRUNED, keeping the shared
  pool
- **Honest-negative (the pre-registered expectation)**: filtering is pruned cleanly - it does not move
  the numbers, so interpretability is not worth trading; record the negative
- **Occam gate**: KEEP nothing from Act IV unless (c) or (d) clears the material out-of-sample bar; the
  black-box (e) exists only to prove the mechanistic options are not merely losing to a more flexible
  fitter

---

## Recommended ordering and the make-or-break gate

The single make-or-break gate is **H454** (does per-region depth generalize out-of-sample?) because it
gates whether ANY de-pooling or state-space fix is admissible at all. The diagnostic already predicts
it FAILS - per-region tuning loses to the shared pool out-of-sample - which pre-empts the entire
mainstream and state-space program (H451, H452, H461, H462). Run it first and cheaply.

Paired with it, run **H456** (is the miss one region - Israel?) as the cheapest first probe: if
recalibrating the single Israel pronatal-well constant removes most of the magnitude miss, the fix is
one scalar, not any hierarchical or filtering machinery, and DEF-8 largely closes without touching the
recuperation mechanism at all.

1. **H456** - recalibrate/exclude Israel's well; measure how much of the miss is that one region
   (cheapest, diagnostic-confirmed)
2. **H454** - the make-or-break: per-region vs pooled out-of-sample; if de-pooling loses (predicted),
   PRUNE Act I and Act IV wholesale and keep the shared pool
3. **H455** - is depth even identifiable at n=20yr; if not, no depth model is trustworthy
4. **H453** - the honest magnitude likelihood as the Occam adjudicator; likely selects baseline / near-
   zero recovery, confirming the term is sign-only
5. **H459** - the one heretical fix worth a run: endogenous N-coupled asymptote that could retire the
   Israel well (H456) with a mechanism rather than a recalibrated constant - the only route that could
   both lower magnitude RMSE and reduce parameter count
6. **H460** - the null the whole fanout must beat; the diagnostic makes it the favourite
7. **H451 / H452 / H461 / H462** - run ONLY if H454 shows per-region generalizes; otherwise pruned
8. **H457 / H458 / H463** - diagnostic / control arms, run to record the negatives cleanly

**Bottom line**: the diagnostic points away from the regularization and toward two concrete, cheap
targets - recalibrate the Israel pronatal well (H456) and, optionally, make its asymptote endogenous
(H459) - while H454 is the pre-registered gate that most likely prunes the entire de-pooling / state-
space program by showing it does not generalize. The honest expected outcome of this fanout is that
DEF-8 closes not by de-regularizing g_rec but by fixing one over-fired region and accepting the
recuperation as the sign-only mechanism it is (H460).
