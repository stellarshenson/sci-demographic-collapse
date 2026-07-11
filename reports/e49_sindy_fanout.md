# E49 - Data-Driven Discovery of Fertility Dynamics (SINDy / Neural ODE)

**The question**: can the coupled vector field be DISCOVERED from the demographic data, instead
of hand-written? Every dynamical term in the shipped model is analyst-imposed (the cubic norm
well, the coupling relaxations, the recuperation term we are now adding). This round asks whether
the governing equations of national fertility dynamics can instead be *recovered from data* by
sparse identification of nonlinear dynamics (SINDy, Brunton-Proctor-Kutz 2016) or a neural ODE
(Chen et al. 2018) - still explicit terms, but data-discovered, not imposed.

**Why it matters (two payoffs).**
- *Scientifically*: "I recovered the governing equations of fertility dynamics from data" is a
  methodological CLAIM, not a synthesis - meaningfully more novel than anything the campaign has
  done, and the closest thing to the emergent coupled model the analyst actually wanted.
- *Transferably (the market-research payoff)*: if a system's dynamics can be captured from thin
  data, you need FAR FEWER observations to forecast it - the field generalizes where curve-fitting
  cannot. In market research this is the beautiful corollary: **capture a market's dynamics once
  and predict its moves from a handful of points, cutting the cost of building reports by a large
  factor.** Demography is the testbed; the claim is general few-shot forecasting via discovered
  dynamics.

**The honest, severe caveat (pre-registered, not hidden)**: 8 countries x ~70 annual points is
THIN data for a 7-dimensional nonlinear system. SINDy will happily overfit or return a degenerate
field; a neural ODE will interpolate and fail to extrapolate. **This round may return a negative
result, and that is a legitimate outcome** - "the dynamics of national fertility are not
recoverable from the available data, and here is the data-sufficiency floor that says so" is a
real, publishable chapter. Every hypothesis carries an honest-negative branch.

## The validation-first discipline

No real-data claim is trusted until the method passes on SYNTHETIC ground truth. The shipped
`emergent.py` IS a known dynamical system - generate clean trajectories from it and ask whether
SINDy/neural-ODE can recover the equations we know are there. If the method cannot recover a known
field from abundant clean data, it has no hope on thin real data, and we stop. This is the H441
gate on everything downstream.

## The ten hypotheses (H441-H450)

### Act I - Can it work at all? (synthetic ground truth)

- **H441 (identifiability floor)** - SINDy recovers the emergent.py governing equations from
  ABUNDANT clean synthetic data (many long trajectories from the model itself). Bar: the
  discovered field reproduces the true term structure (correct active terms, coefficients within
  20%) on >= 5/7 channels. Honest-negative: if even clean-data recovery fails, data-driven
  discovery is off the table for this system - report the identifiability floor and stop.
- **H442 (noise robustness)** - weak-form / integral SINDy (Messenger-Bortz) recovers the field
  under observation noise matched to real TFR measurement error (~1-2%). Bar: term-structure
  recovery survives to the real-data noise level; locate the noise ceiling where it breaks.
- **H443 (data-sufficiency scaling)** - quantify the recovery accuracy as a function of
  (trajectories x length): the curve N(L) that says how much data suffices. Bar: report the
  minimum (trajectories, length) for term-structure recovery. **This IS the market-research
  payoff, quantified** - "M trajectories of L points suffice to capture the dynamics."

### Act II - The data-efficiency claim (the transferable core)

- **H444 (multi-trajectory pooling)** - pooling the 8 countries as trajectories of ONE shared
  system recovers the field with far fewer points-per-country than fitting each alone. Bar:
  pooled recovery accuracy at 8 x L beats single-trajectory at 8L by a material margin - the
  formal statement of "shared dynamics need less data per series." The market-research thesis.
- **H445 (few-shot transfer)** - discover the field on 7 countries, then predict the 8th from
  only its first ~10 years, beating a naive extrapolation and a per-country curve fit. Bar:
  held-out forecast RMSE materially below both baselines. The "predict a new market from a
  handful of points because we captured the dynamics" claim, tested. Caveat: this is within-regime
  interpolation (the held-out region shares the trapped-low-fertility regime), not new-regime
  transfer - the out-of-regime region (Israel) blows up.

### Act III - Structure and interpretability

- **H446 (physics-informed discovery)** - impose the known Leslie transport (age structure is not
  in question) and discover ONLY the behavioral coupling terms; constraining to the known
  structure makes discovery tractable on thin data where unconstrained SINDy fails. Bar:
  constrained recovery succeeds at a data level where unconstrained (H441-scale) does not.
- **H447 (interpretability / sparsity)** - the discovered behavioral terms are SPARSE and map onto
  recognizable mechanisms (a coupling relaxation, a bistable term), not a dense black box. Bar:
  the active-term count is within a small factor of the hand-written model AND the terms are
  human-readable. This is the axis on which SINDy beats a neural ODE.
- **H448 (neural-ODE comparison)** - a neural ODE fits the training data better than SINDy but
  generalizes worse (held-out and few-shot) and is not interpretable - the accuracy-vs-
  interpretability-vs-extrapolation tradeoff. Bar: neural-ODE in-sample RMSE < SINDy, but
  out-of-sample / few-shot RMSE > SINDy; report the tradeoff honestly either way.

### Act IV - The honest reckoning and the deepest question

- **H449 (degeneracy / overfitting detection)** - the pre-registered failure test: on the REAL
  thin data (8 x ~70), does SINDy return a degenerate or overfit field (unstable, non-generalizing,
  coefficient variance exploding under cross-validation)? Bar: a pre-registered degeneracy
  criterion (LOO coefficient stability, forecast blow-up); if it fires, the honest report is "not
  recoverable from the available data," with H443's floor as the quantitative reason.
- **H450 (the emergence test)** - the deepest question: does a discovered field REPRODUCE the
  emergent behaviours we hand-wrote - bistability, the tipping trap, the recovery - or are those
  behaviours NOT discoverable from data? Bar: test whether the discovered field exhibits the
  double-well / tipping structure. If yes, emergence is recoverable (the analyst's dream); if no,
  the hand-written structure was doing load-bearing work the data cannot supply - itself a
  profound, honest finding about the limits of data-driven demography.

## The market-research transfer (why this is worth doing even if it fails on demography)

H443, H444, H445 form a self-contained claim independent of the fertility application:
**discovered dynamics enable few-shot forecasting.** If pooling short trajectories of a shared
system recovers the vector field (H444), and a held-out series is predictable from a handful of
points (H445), then the same protocol applied to market time-series promises forecasting a new
market/product/segment from far less data than curve-fitting needs - because the DYNAMICS, once
captured, transfer. The data-sufficiency curve (H443) is the cost-reduction factor made explicit.
Demography, with its thin data and known ground truth, is the honest stress test: if it works
here, it works where data is richer; if it fails here, H443's floor tells you exactly how much
data the method needs before it pays.

## Discipline

- **Validation-first**: H441 gates everything. No real-data claim without synthetic recovery.
- **Honest-negative is a result**: every hypothesis has a pre-registered failure branch; "not
  recoverable, here is the floor" is reported as prominently as a success.
- **Occam**: a discovered field is KEPT over the hand-written model only if it forecasts held-out
  data better AND is no less interpretable; else the hand-written model stands and the negative is
  recorded.
- **Grounding**: SINDy (Brunton-Proctor-Kutz, PNAS 2016), weak-form SINDy (Messenger-Bortz 2021),
  SINDy-PI (Kaheman-Kutz), neural ODEs (Chen et al., NeurIPS 2018), multi-trajectory / ensemble
  SINDy (Fasel et al. 2022) - papers to download + digest in Phase 0.
- **Tooling**: `pysindy` (add to the stack), `torchdiffeq` for the neural-ODE arm; standalone in
  scratchpad first, notebook `44-kj-e49-sindy.ipynb` when the synthetic gate (H441) passes.

## Recommended ordering

H441 (can it recover a known field from clean data?) is the make-or-break gate - run it first and
alone. If it passes: H442 (noise) -> H443 (data floor) -> H444 (pooling) -> H445 (few-shot) are
the data-efficiency spine and the market-research payoff. H446-H448 characterise structure and the
neural-ODE alternative. H449-H450 are the honest reckoning. If H441 FAILS on clean data, stop and
report the identifiability floor - that negative alone is a legitimate finding.
