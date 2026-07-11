# OT Novelty Sweep

Literature sweep testing whether this project's three uses of optimal transport (OT) are novel in demography or adjacent social science. The sweep is written to protect a future methodology paper from a referee, not to flatter the project - where prior art exists it is credited precisely, and novelty is claimed only where the search found no anticipation.

The three claims under test:

- **A** - Wasserstein-2 calibration of a mechanistic population-dynamics model: fitting a demographic simulation by minimizing W2 (L2 between quantile functions) on observables, instead of least-squares / moment-matching / MCMC (project E12)
- **B** - OT-based cohort memory / intergenerational path integral: because the 1-D optimal map is the monotone rank-preserving rearrangement, a birth cohort keeps its quantile identity as the distribution shifts, so its childhood-environment exposure can be integrated Lagrangian-style down a Lexis line to drive a marriageability state (project `ot.py`, E30)
- **C** - differentiable quantile-flow reparametrisation `theta = Q_phi(u)`: carrying model states as monotone quantile functions, giving the reparameterisation trick, exact 1-D W2, McCann interpolation and W2-gradient-flow-as-L2-flow all at once (project `flow.py`)

## Closest works found

| Work | Year / venue | What it transports | Closest to | Distance from claim |
|---|---|---|---|---|
| Bernton, Jacob, Gerber, Robert - "ABC with the Wasserstein distance" (and 2017 "On parameter estimation with the Wasserstein distance") | 2019, JRSS-B | Empirical distribution of *simulated* vs *observed* data; minimum-expected-Wasserstein estimator for generative models | **A** | The direct methodological ancestor: fitting a simulation by minimizing Wasserstein. Not demographic, and generic-generative rather than a mechanistic cohort model |
| Gunsilius - "Distributional Synthetic Controls" | 2023, Econometrica | Quantile function of a treated unit as a weighted average of control quantile functions; minimizes squared W2 via quantile-on-quantile regression | **A** | Same numerical device (W2 on quantile functions as the fitting objective) but for causal counterfactuals, not model calibration |
| Petersen & Müller - Fréchet regression; Wasserstein autoregressive models (Zhang et al. 2020); arXiv 2508.17235 (Wasserstein vs life-expectancy gap) | 2019+ | Age-at-death / density distributions as points in Wasserstein space (regression, forecasting, description) | **A** | The demographic-domain anchor - mortality distributions treated as Wasserstein-space objects. But regression/forecasting of distributions, not calibrating a mechanistic simulation |
| Bunne et al. - JKOnet, "Proximal OT Modeling of Population Dynamics" | 2022, AISTATS | A population's distribution along time; fits an energy so the JKO trajectory matches observed distributions | **A** and **B** | Calibrates dynamics by OT (A) and carries Lagrangian OT trajectories (B), but for single-cell biology, Eulerian energy-fitting, no cohort exposure integral |
| Galichon school: "Optimal Transport Methods in Economics" (2016); Galichon-Salanié; Choo-Siow (2006); Chiappori-McCann-Nesheim (2010) | 2006-2016 | Mass across a *matching* (who marries whom) as a Monge-Kantorovich / regularized-OT problem | context for **B** | The demography-adjacent economics OT anchor. Transports across a matching, not along a cohort; mechanically distinct from all three claims but the natural citation bridge for the marriage / marriageability framing |
| Multivariate Quantile Function Forecaster (Amazon, 2022); monotone / invertible normalizing flows; Wasserstein-gradient-flow = L2-gradient-flow-on-quantiles (classical 1-D OT, Bonnotte) | 2019-2023 | A distribution held as its (monotone) quantile function, differentiable in parameters | **C** | Every building block of claim C is standard ML / 1-D-OT. The representation is not novel as a technique |

## Verdict per claim

**Claim A - Wasserstein-2 calibration: PARTIALLY ANTICIPATED (method known; mechanistic-demographic application fresh).**
The method - estimate a model's parameters by minimizing a Wasserstein distance between model output and data - is established. Bernton et al. (2019) is the canonical minimum-Wasserstein / Wasserstein-ABC estimator for generative models, and Gunsilius (2023) uses the exact device this project uses (squared W2 = quantile-on-quantile L2) as an econometric objective. In demography specifically, Petersen-Müller Fréchet/Wasserstein regression and the Wasserstein-autoregressive line already place mortality and fertility distributions in Wasserstein space. What the search did *not* find is this objective used to calibrate a *mechanistic cohort/Leslie population-dynamics simulation* - the existing demographic OT work is descriptive or regression/forecasting, and the existing calibration work (Bernton, JKOnet) is non-demographic. So claim A should be framed as a known estimator applied to a setting where it has not, to my finding, been applied - a contribution of application and packaging, not of method. Do not call the W2-quantile calibration itself novel.

**Claim B - OT-based cohort memory / intergenerational path integral: NOVEL (search found no anticipation; caveat below).**
No work found combines the rank-preservation of the 1-D optimal map with a cohort path integral. The ingredients each exist separately - the method of characteristics for the McKendrick-von Foerster / renewal PDE, cohort accounting, frailty/heterogeneity models, and Lagrangian OT trajectories (JKOnet) - but the specific device (the monotone optimal map preserves quantile rank, therefore a birth cohort retains its identity as the environment distribution shifts, therefore its childhood exposure can be integrated along its Lexis line into a marriageability driver) is not in the literature the sweep reached. Honest caveat: this is a fairly *natural* composition of known pieces, so a referee could argue it is folklore; absence of a hit is not proof of absence. Claim novelty as "a construction we have not seen," not as a hard first.

**Claim C - differentiable quantile-flow reparametrisation: KNOWN (as a technique); novelty only in the state-carrier role.**
`theta = Q_phi(u)` with u uniform is the quantile-function view of the reparameterisation trick; monotone/normalizing-flow quantile parameterisations are standard (e.g. the Multivariate Quantile Function Forecaster and the monotone-flow literature); and "W2 gradient flow = L2 gradient flow on the quantile function" is a textbook fact of 1-D optimal transport. The four properties the project bundles (reparameterisation, exact W2, McCann interpolation, degenerate-limit baseline preservation) are individually established. The only unclaimed ground is using this object as the *state variable of a mechanistic demographic model*. Present claim C as an engineering choice grounded in known OT, not as a methodological novelty; over-claiming here is the easiest referee target.

## Recommended related-work framing

A methodology paper should bridge four literatures explicitly rather than present OT as new to demography:

- **Wasserstein / minimum-distance estimation** - Bernton et al. (2019) and the Wasserstein-ABC line as the parent of claim A; state plainly that the project inherits this estimator and contributes its use inside a mechanistic cohort model
- **Distributions-as-objects in demography** - Petersen-Müller Fréchet regression, Wasserstein autoregressive density time series, and the age-at-death-in-Wasserstein-space work; this is the demographic anchor and the honest "adjacent prior art" for claim A - cite it up front, do not wave it away
- **OT in economics / matching** - the Galichon school (2016 book, Galichon-Salanié, Choo-Siow, Chiappori-McCann-Nesheim) as the demography-adjacent OT tradition and the conceptual home of the marriage-market / marriageability framing behind claim B, while distinguishing rank-preserving cohort transport from matching-based transport
- **Quantile-function / normalizing-flow representations and 1-D OT** - the reparameterisation trick, monotone normalizing flows, and the W2 = L2-on-quantiles identity as the grounding for claim C; frame claim C as adopting these, with the contribution being the demographic state-carrier, not the representation

The paper's defensible novelty concentrates in **claim B** (the cohort path-integral construction) and in the *composition* - a single quantile-flow object that is simultaneously the calibration target (A), the cohort-memory carrier (B), and the differentiable model state (C) inside one mechanistic demographic model. Frame the contribution as the integration, not as any one of the three ingredients.

## Limitations of this sweep

- **Coverage** - web search over Google Scholar surface results, arXiv, and journal abstracts (Demographic Research, Demography, Population Studies, Econometrica, JRSS-B, biostatistics venues). No paywalled full texts were read; matches rest on titles, abstracts, and search-engine summaries. A close anticipation buried in a paper body without matching keywords would be missed
- **Keyword risk for claim B** - the construction has no settled name, so it is the hardest to disprove by keyword search; a "NOVEL" verdict here is "no hit found," weaker than a proof of absence. The natural-composition caveat stands
- **Date** - conducted July 2026; the fast-moving OT-in-statistics and distributional-econometrics literatures may already contain closer 2025-2026 work than surfaced
- **Language / venue** - English-language sources only; demographic OT work in other languages or in working-paper series not indexed by the search was not reached
- **Not adversarially exhaustive** - roughly a dozen targeted queries, not a systematic PRISMA-style review; treat the verdicts as a strong first screen, not a settled priority claim
