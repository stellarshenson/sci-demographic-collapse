# Scientific Methods Inventory

A running log of the scientific machinery - equations, theorems, estimators, numerical schemes - used across the demographic-collapse campaign, with what each is, where it is applied in the model, and the key reference. Terse by design; this is an inventory, not a tutorial. Entries are appended as new machinery enters the campaign. The plain-language companion is the README's "How the simulation actually works" walkthrough, which shows how these pieces fit together in one lap of the machine.

## Demographic core (age structure and renewal)

- **McKendrick-von Foerster PDE** - the continuous age-structured population balance $\partial_t n(a,t) + \partial_a n(a,t) = -\mu(a,t)\,n(a,t)$; the transport term is the derivative along a cohort life-line; the demographic backbone is this equation. Ref: McKendrick 1926; von Foerster 1959
- **Sharpe-Lotka renewal equation** - the boundary condition / integral form for births, $n(0,t)=\int_0^\infty \beta(a,t)\,n(a,t)\,\mathrm{d}a$; the source of the intrinsic growth rate. Ref: Sharpe & Lotka 1911; Lotka 1939
- **Leslie matrix / cohort-component projection** - the discrete finite-difference form of McKendrick-von Foerster (one-year age×time bins); `coremodel.leslie_step`. Ref: Leslie 1945
- **Method of characteristics** - solving the renewal PDE along cohort life-lines (the Lexis diagonal); the conceptual basis for cohort tracking and the per-cohort path integral. Ref: standard PDE theory; Lexis 1875
- **Stable population theory / eigenstructure** - the dominant Leslie eigenvalue $\lambda_1$ is the intrinsic growth rate ($r=\ln\lambda_1$), its eigenvector the stable age pyramid; every study region has $\lambda_1<1$
- **Keyfitz population momentum** - growth built into a non-stationary pyramid, computed from the stable eigenvector; finite and depleting. Ref: Keyfitz 1971
- **Rogers-Castro migration schedule** - a parametric age curve (labour-force peak + childhood echo) for net migration by age; `coremodel.rogers_castro`. Ref: Rogers & Castro 1981
- **Life-table survival ratios** - $S_a = L(a)/L(a-1)$, the aging operator's Markov backbone

## Fertility decomposition

- **Total fertility rate (TFR) and quantum-tempo split** - period TFR mixes recoverable postponement (tempo) and structural completed fertility (quantum)
- **Bongaarts-Feeney tempo-quantum decomposition** - $\text{adjTFR}=\text{TFR}/(1-r)$ with $r$ the rate of rise of mean age at childbearing; separates a mirage bump from a permanent loss. Implemented on the *realized* annual change $\Delta\tau_{\text{realized}}$ (post-clip) with a floor at zero (the E40 fix; the pre-fix core summed sub-step rates and applied exactly 4x the documented rate, with an unguarded factor that could go negative). Ref: Bongaarts & Feeney 1998
- **Skew-normal ASFR reconstruction** - a two-parameter (mean age, quantum-scaled) age-specific fertility profile reconstructing single-year ASFR to within 3% of peak
- **Fecundability decay** - $\mathrm{fec}(\tau)=\exp(-0.03\max(\tau-30,0))$, the age penalty on conception

## Behavioural dynamical system

- **Coupled first-order ODE system** - the behavioural layer: observable channels $C,\rho,\bar P,\tau,S,N,q$ each with its own dynamics (six relaxations toward moving targets plus the bistable norm), composed as $\text{TFR}=C(1-\rho)\bar P\,\mathrm{fec}(\tau)\,\max(1-k_{BF}\Delta\tau_{\text{realized}},0)$; nine equations in all with the cohort memory integral and the composition law; `emergent.EmergentModel`
- **Quarter-year forward-Euler substepping with physical clips** - the integrator: 4 substeps/year, each state clipped post-step to its physical range ($C\in[0.02,0.999]$, $\rho\in[0,0.6]$, $\bar P\ge 1$, $\tau\in[24,40]$, $S\in[0.05,0.95]$, $N\in[0,1]$, $q\in[-1,1]$); first-order convergent under substep halving (verified post-E40)
- **Step-invariant observable rule** - an observable must be a function of the state trajectory, never of the integrator's internals; any quantity summed over substeps is suspect until proven step-invariant (the E40 standing lesson - the pre-fix tempo factor summed substep rates and was integrator-dependent)
- **Soft-bistable double-well potential** - the coupling trap near the empirical TFR-1.5 ridge; gives the two-basin fate shape (the Seldon manifold)
- **Bistable contagion with hysteresis** - the social-norm state $N$: $\dot N=-a_N(N-N_{lo})(N-\theta_N)(N-N_{hi})+f_N$, two stable wells, an unstable tipping point, a crossing push locks in. Ref: Schlogl 1972 (cubic bistable); Centola tipping ~25%
- **Separatrix / basin of attraction** - the fate boundary in the (birth-rate, security) plane; the Seldon manifold ridge; measured at 1.47-1.66, matching the cited TFR-1.5 trap. Ref: Lutz et al. (low-fertility trap)
- **Fixed-point stability analysis** - linearisation about a channel's equilibrium to classify wells vs tipping points (used to make the norm state baseline-preserving)

## Bayesian calibration and inference

- **Reparameterisation trick** - pathwise-differentiable sampling $\theta=g_\phi(\varepsilon)$, $\varepsilon\sim p(\varepsilon)$; fits whole distributions, not point estimates. Ref: Kingma & Welling 2014
- **Variational free energy / ELBO** - the first calibration objective ($\mathcal F=-\text{ELBO}$, Pyro SVI); failed by posterior collapse
- **Posterior collapse (diagnosed)** - the per-point KL drives the innovation scale $\tau\to0$, flattening the latent trend; the diagnosed cause of the +0.2/+0.3 over-prediction
- **Wasserstein Auto-Encoder / InfoVAE($\alpha{=}1$)** - penalises only the aggregate posterior, preserving latent mutual information; the fix that closed the gap. Ref: Tolstikhin et al. 2018; Zhao et al. 2019
- **Exact one-dimensional Wasserstein-2 loss** - the winning calibration penalty ($W_2$ between sorted quantiles); closed the in-sample 2023 gap to ~0.018, MI-usage 0.96
- **Maximum-mean-discrepancy (RBF-MMD)** - the third arm of the calibration-objective tournament (lost to exact 1-D $W_2$). Ref: Gretton et al. 2012
- **Local-linear-trend state-space model** - the latent quantum trend prior in the calibration
- **Hierarchical drift-pooling** - partial pooling of the latent drift across regions; lifted held-out TFR coverage 50%→100%

## Optimal transport (distribution evolution)

- **Wasserstein-2 metric** - $W_2(P,Q)$; the distance between population states; the campaign's calibration and distribution-morph metric. Ref: Villani 2009
- **1-D optimal transport = monotone rearrangement** - in one dimension the optimal plan is order-preserving, $W_2=\lVert F_P^{-1}-F_Q^{-1}\rVert_{L^2}$ (quantile-function $L^2$); closed-form, no Sinkhorn; `ot.Dist.W2`
- **McCann displacement interpolation** - the Wasserstein geodesic (the morph), $F_t^{-1}=(1-t)F_0^{-1}+tF_1^{-1}$; `ot.Dist.interpolate`. Ref: McCann 1997
- **Wasserstein barycenter** - quantile-averaged blend of distributions; `ot.Dist.barycenter`. Ref: Agueh & Carlier 2011
- **Wasserstein gradient flow / JKO scheme** - distribution dynamics as $\rho_{k+1}=\arg\min_\rho \mathcal F[\rho]+\frac{1}{2\tau}W_2^2(\rho,\rho_k)$; the behavioural distribution evolution. Ref: Jordan, Kinderlehrer & Otto 1998
- **Fokker-Planck as a gradient flow** - the continuity equation $\partial_t\rho+\nabla\!\cdot(\rho v)=0$ realised as the particle-advection form; `ot.Dist.advect`
- **Pushforward / transport maps** - interventions and selection as $T_\sharp\rho$ (a policy shift, a truncation); `ot.Dist.pushforward`
- **Implicit reparameterisation gradients** - differentiate through a quantile/CDF where $\theta=g(\varepsilon)$ is not explicit (mixtures, empirical): $\partial_\phi\theta=-(\partial_\phi F)/(\partial_\theta F)$; the bridge that keeps non-Gaussian families differentiable. Ref: Figurnov, Mohamed & Mnih 2018
- **Monotone quantile-flow (1-D normalizing flow)** - the planned distributional-core representation $\theta=Q_\phi(u)$, $u\sim\text{Uniform}$; unifies reparameterisation, OT, gradient flow and empirical↔parametric fitting in one differentiable object. Ref: Rezende & Mohamed 2015 (flows); Durkan et al. 2019 (splines)

## Population heterogeneity and cohorts

- **Latin-hypercube ensemble (K=64)** - the production heterogeneity: each channel spread by a stratified inverse-normal quantile marginal, decorrelated across channels via seeded permutations; $\sigma\to0$ reproduces the scalar core to machine precision; spreads are the literature-grounded `SIGMA_CAL` (age-at-first-birth sd ~3yr the widest), and one per-region parity rescale (`PB_SCALE_ENS`, ~1.02-1.04) re-anchors the dispersed year-1 TFR to 2023 REAL exactly; `emergent.run_ens` / `run_cal`
- **Reparameterisation-to-buckets** - lift a scalar channel to $\theta=\mu+\sigma\varepsilon$ discretised into population buckets; `population.PopChannel`
- **Gauss-Hermite quadrature** - the bucketing nodes/weights for a Gaussian population ($\langle f\rangle=\sum_k w_k f(\theta_k)$); `population.PopChannel`, `ot.Dist.from_gaussian`
- **Jensen gap** - $\langle f\rangle - f(\langle\theta\rangle)$, the heterogeneity correction where the channel is nonlinear; measured +0.093 (66% relative) off-threshold - material where thresholds bite
- **Tail selection** - truncation/reweighting of a distribution's tail (a cutoff or preference threshold on a channel); `population.PopChannel.select`, `ot.Dist.select`
- **Cohort path integral** - the Lagrangian method-of-characteristics form of the intergenerational memory: each cohort accumulates $J(u)=\int_{\text{birth}}^{t}\mathrm{effect}(\theta_u(s))\,\mathrm{d}s$ down its life-line; a parent cohort's completed integral sets the child cohort's initial condition; `ot.CohortMemory`. Replaces the earlier aggregate mean-field lag - deepens and persists the intergenerational cost (compounding)
- **Distributed lag / convolution** - the earlier mean-field intergenerational memory (superseded by the cohort path integral)

## Causal identification and evaluation (from the literature and the campaign)

- **Natural experiments** - the campaign's causal anchors: Autor-Dorn-Hanson China trade shock and Kearney-Wilson fracking boom (marriageable-men), Bauernschuster universal childcare, Tertilt polygyny/monogamy, Edlund sex-ratio-to-crime, Ebenstein kibbutz privatisation
- **Elasticities** - dimensionless response coefficients used to size levers (e.g. marriageable-men elasticity ~0.2-0.4; crime-to-sex-ratio ~3.4)
- **Defection parameter $\delta$ and side-effect cost vectors** - $\Delta\text{TFR}_{\text{net}}=\text{gross}\cdot(1-\delta)+\text{backfire}(\delta)$; models evasion (the sign can flip) and stacks each lever's named side-cost (E16)
- **Ablation / leave-one-out** - marginal contribution of a lever inside a bundle; separates load-bearing from redundant/collinear levers (E20, E24)
- **Interaction-discovery matrix** - pairwise $I(A,B)=\text{effect}(A{+}B)-\text{effect}(A)-\text{effect}(B)$; classifies super-additive / antagonistic / sign-flip interactions (E28, E29)
- **Swept response curves** - each hypothesis's experiment is a swept lever curve; the verdict is on the optimum type (interior / corner / sign-flip), e.g. the Tertilt low-development sign-flip (E17, E28)

## Methodology and discipline

- **Pre-registration and falsifiability** - hypotheses stated with a bar before the run; out-of-sample tests (the technology hypotheses failed their ≥25% bar at 17%)
- **Simulation-then-ablation protocol** - every hypothesis is (1) analytically digested, (2) simulated on the coupled model over four generations on the Korea/Germany/France triad, (3) ablated - no verdict is assigned by assertion
- **Naive-baseline delta convention** - every result reported as a delta against an explicit no-intervention baseline
- **Composite cost metric** - $0.40\,\text{fiscal}+0.35\,\text{coercion}+0.25\,\text{side}$; the E20 cost axis for the least-cost-lever (harbinger) ranking
- **Baseline-preserving extension** - a new channel enters as a deviation identically zero at the calibrated reference, so baselines are unchanged (verified ~3e-7) with no re-fit; used for the norm state $N$ and the marriageability/intergenerational memory
- **Modelling discipline** - mandated order: equations → parameters → literature-grounded distributions → coupled system → stress-test → simulation last
