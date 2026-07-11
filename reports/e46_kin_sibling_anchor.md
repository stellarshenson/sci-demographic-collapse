# E46 - Kin and Sibling Support as a Fertility-Raising Channel

Grounds the hypothesis that a mutual-support network of kin and siblings (shared childcare, shared
cost, social capital, social learning) raises the capacity and willingness to have children, and
decides whether it is worth a dedicated channel in the emergent model. The model's TFR identity is
`TFR = C·(1-rho)·Pbar·fec(tau)·max(1 - kBF·dtau, 0)` with channels coupling `C`, childlessness
`rho`, parity `Pbar`, tempo `tau`, plus economic security `S` and the social norm `N`. The mechanism
splits cleanly into an *intergenerational* claim (having siblings raises your own fertility) and a
*within-generation availability-of-help* claim (kin who can help raise the next birth), and the
literature treats the two very differently.

## The three strongest effect sizes

- **Kin-childcare -> next-birth (availability of help)**: in China, mothers who use grandparental
  childcare have **~4x higher odds of a second birth** than those who do not (Zhang-Emery 2023, PLOS
  ONE, hazard model, peak risk ~48 months). In the Netherlands, frequent grandparental childcare
  raised the probability of a further birth from **35% to 66% (~+31 percentage points)** over 8-10
  years (Kaptijn-Thomese 2010, logit 1.286, p<0.05). Both are *parity-progression* effects; neither
  produced *first* births in the childless
- **Sibling's birth -> own first-birth hazard (contagion, timing)**: a sibling's birth raises the
  respondent's own first-birth hazard for **~3 years then fades**, net of parental fertility and
  shared family frailty, stronger when the sibling is older; **null for second births** (Lyngstad-
  Prskawetz 2010, Demography, 110,000 Norwegian sibling pairs). This is a tempo/synchronisation pulse
  on entry into parenthood, not a lift to completed family size
- **Siblings -> completed fertility (transmission)**: the naive correlation is **+0.078 children per
  sibling (men) / +0.096 (women)**, but the causal twin-instrument estimate collapses to **+0.041
  (men, n.s.) / -0.042 (women, marginal)** - essentially zero, slightly negative for women (Kolk
  2015, Demographic Research, Swedish registers)

## Causal or confounded

- **The intergenerational "family size is self-reinforcing" claim is confounded, not causal.** Kolk's
  twin instrument removes the ~0.08-0.10 raw correlation entirely: an exogenous extra sibling does not
  raise, and for women mildly lowers, completed fertility. The observed clustering of large families
  across generations is shared preferences and socioeconomic status, which regional/preference
  heterogeneity in the model already carries
- **The within-generation availability-of-help claim is real but observational.** The ~4x odds
  (China) and +31pp (Netherlands) effects survive controls but not selection - grandparents who help
  are chosen, and willing helpers cluster with fertile intentions - so the magnitudes are upper
  bounds. Sear-Mace (2008), reviewing 45 natural-fertility populations, confirm the *mechanism* (in
  almost all studies at least one relative improves child survival; maternal grandmother in 69% of
  cases; elder siblings as helpers-at-the-nest), but the outcome there is child *survival* in
  high-mortality settings, not the fertility *rate* in low-mortality ones
- **The sibling-contagion effect is causal but small and temporary.** Lyngstad-Prskawetz net out
  transmission and still find a first-birth pulse - but it fades within three years and does nothing
  to parity, so it is a timing effect, kin to the existing norm/contagion channel (E43 `N`,
  Balbo-Barban friends)

## Resource-dilution counter-term

The counter-direction is genuine and already visible inside the same evidence. Blake's resource-
dilution model - finite parental time, attention and money split across more children - predicts that
more siblings *lower* per-child investment and outcomes, and Kolk's causal estimate for women (-0.042)
is exactly that signature. So the intergenerational channel is not merely null on average; it carries
an offsetting negative arm. Any kin-support term added to the model must therefore be net of a
dilution counter-term, and the intergenerational (sibling-count -> own parity) arm should be treated
as approximately zero, not positive.

## Verdict: is it worth a model channel

**Partial - one arm yes, two arms no.**

- **Do not add a sibling-count -> parity (`Pbar`) multiplier.** The clean causal test (Kolk) says the
  effect is ~zero to slightly negative once confounds are removed, and resource dilution offsets it.
  A self-reinforcing family-size feedback into `Pbar` would encode a confounded correlation as
  structure - exactly the failure mode this project audits for. The model's regional heterogeneity
  already reproduces family-size clustering
- **Do not add a sibling-contagion driver as a new channel.** The Lyngstad-Prskawetz effect is a
  short-run first-birth timing pulse already covered in kind by the norm/contagion channel `N`
  (E43) and the friends-contagion evidence (Balbo-Barban). At most it is a small recalibration of
  `N`, not a new state
- **A kin-childcare availability term is defensible, on the cost/security side, if wired carefully.**
  The ~4x-odds / +31pp effects are the mechanism's real force, and they act by lowering the effective
  cost and work-family conflict of the *next* birth - i.e. relieving the suppression that `S`
  (economic security / youth-precarity) already represents. It would enter as a modifier that raises
  effective `S` (or lowers the `S`-mediated drag on parity progression) where kin availability is
  high, with a **secondary, smaller lift to coupling `C`**, and **explicitly net of a
  resource-dilution counter-term**. It must not touch entry into parenthood (`rho`/`C` first-birth),
  since both anchor studies find no effect on the childless

## How it would couple

- **Primary: security `S`** - kin availability lowers the cost/precarity drag on progression to the
  next parity (the channel through which the ~4x / +31pp effects act). This is a modifier on `S`, not
  a new state variable
- **Secondary: coupling `C`** - a small lift, since shared childcare and kin social capital modestly
  raise the willingness (not just capacity) to progress
- **Not `Pbar` directly, and not first-birth `rho`/`C`** - the causal evidence rejects a structural
  parity multiplier and finds no effect on the childless
- **Counter-term: resource dilution** - the coupling must carry an offsetting negative arm (finite
  per-child investment; Kolk's -0.042 for women), so the net sign is small and saturating, consistent
  with this project's "effects compete, nothing stacks linearly" discipline
- **Magnitude for calibration**: treat the observational ~4x odds / +31pp as an upper bound on the
  next-birth availability effect; the causal intergenerational arm as ~0; the contagion arm as a
  ~3-year timing pulse folded into `N`. A conservative net kin-support modifier is a modest,
  saturating uplift to effective `S` in high-kin-availability regions, not a headline driver of the
  collapse

## Sources

- Zhang & Emery (2023), *Grandparental childcare and second births in China*, PLOS ONE 18(6):
  e0286496 (OA) - `[paper] grandparental childcare second births China Zhang Emery, 2023.pdf`
- Kaptijn, Thomese, van Tilburg & Liefbroer (2010), *How Grandparents Matter*, Human Nature 21(4):
  393-405 (PMC full text) - link-only digest
- Lyngstad & Prskawetz (2010), *Do siblings' fertility decisions influence each other?*, Demography
  47(4): 923-934 (paywalled) - link-only digest
- Kolk (2015), *The causal effect of an additional sibling on completed fertility*, Demographic
  Research 32(51): 1409-1420 (OA) - `[paper] additional sibling completed fertility twins Kolk, 2015.pdf`
- Sear & Mace (2008), *Who keeps children alive?*, Evolution and Human Behavior 29(1): 1-18 (LSE OA)
  - `[paper] who keeps children alive kin child survival Sear Mace, 2008.pdf`
- Blake (1981, 1989), resource-dilution / quantity-quality trade-off - counter-term reference
- Balbo & Barban (2014), friends-contagion (already in library) - contagion analog for `N`
