# sci-demographic-collapse

*Why the modern world is quietly running out of children - and what, if anything, can be done about it. A computer model, and the story it tells.*

[![CI](https://github.com/stellarshenson/sci-demographic-collapse/actions/workflows/ci.yml/badge.svg)](https://github.com/stellarshenson/sci-demographic-collapse/actions/workflows/ci.yml)
[![Python 3.13](https://img.shields.io/badge/Python-3.13-3776AB.svg?logo=python&logoColor=white)](https://www.python.org/)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.12-EE4C2C.svg?logo=pytorch&logoColor=white)](https://pytorch.org/)
[![Pyro](https://img.shields.io/badge/Pyro-1.9-8A2BE2.svg)](https://pyro.ai/)
[![ArviZ](https://img.shields.io/badge/ArviZ-1.2-8A2BE2.svg)](https://www.arviz.org/)
[![SciPy](https://img.shields.io/badge/SciPy-1.18-8CAAE6.svg?logo=scipy&logoColor=white)](https://scipy.org/)
[![NumPy](https://img.shields.io/badge/NumPy-2.5-013243.svg?logo=numpy&logoColor=white)](https://numpy.org/)
[![Questions](https://img.shields.io/badge/questions%20asked-300%2B-2ea44f.svg)](docs/experiments/demographic-collapse-experiments.md)
[![the danger line](https://img.shields.io/badge/the%20danger%20line-1.5%20children-critical.svg)](docs/experiments/demographic-collapse-experiments.md)

In Asimov's *Foundation* novels, Hari Seldon forecasts a civilization by reading the behaviour of billions at once - one person is unpredictable, the average of a million is not. This project is a small, real version of that idea, aimed at a crisis nearly every rich country shares: not enough children to replace itself. The model does not predict any single country's future; it maps the forces under the headlines and shows where each country stands.

## The fate map

The whole argument in one picture. **On the raw numbers, extinction is the default outcome for a modern society. Survival is the exception - a narrow margin a civilisation has to reach and then keep earning.**

<!-- Seldon's manifold: the flagship image, the thesis in one glance. -->
![Seldon's manifold seen from above - a glowing hot-white ridge divides a dark-purple extinction basin (low birth rate) from a bright-green survival zone (above about 1.5 children); Korea, China, Spain, Poland, Italy and Japan glow red deep in the basin, Germany and Czechia sit amber on the edge, the United States, France, Brazil, India and Saudi Arabia reach the green, and Israel sits farthest right of all at 2.83 - the one developed nation above replacement](reports/figures/story_manifold.png)

This is **Seldon's manifold**, the model's fate map seen from above: birth rate left to right, the security a society gives its young bottom to top, a dark-purple extinction basin and a green survival zone split by a ridge at about 1.5 children per woman. Most of the great powers are already on the wrong side of it; Israel, alone among developed nations, is deep in the green.

## The dividing line: 1.5 children per woman

Take one country that starts close to the ridge - the United States - and vary one thing: how hard, and how steadily, it tries to lift its birth rate. Below a critical effort every path slides into the decline basin; above it, every path climbs into recovery.

<!-- Two futures: the USA under a fan of sustained pushes, decline (rose) vs recovery (teal). -->
![The same country under a fan of efforts - the strongest push climbs into recovery, the weakest slides into decline, split by the narrow ridge at about 1.5 children](reports/figures/story_two_futures.png)

Two facts about that landscape. Most of it tilts downward: roughly two of every three swept futures end in decline, so staying up has to be earned continuously. And the ridge is precise: about 1.5 children per woman, against the roughly 2.1 needed to hold level - the whole margin between shrinking manageably and passing self-rescue is half a child. Demographers had placed the same 1.5 danger line from real-world data (Lutz et al., 2006) before the model, built independently, put its ridge in the same spot.

Where the great powers stand today:

- **United States, 1.62** - just on the safe side, held there by immigration alone
- **Europe, about 1.5** - on the ridge itself
- **China, 1.2** - over the edge
- **South Korea, 0.7** - far down the collapse slope, the lowest birth rate any country has ever recorded

## What collapse looks like

There is no plague or war in this story, and no single catastrophic year. Collapse is a long, quiet subtraction: a village loses its school, then its clinic, then its last shop; the median age climbs until the country spends more on its endings than its beginnings; each generation arrives smaller than the one that raised it.

Here is the birth rate itself, if today's levels simply continued, across seven economies over the next eighty years:

<!-- What collapse looks like: baseline birth-rate decline to 2100 across seven economies, Korea toward 0.5. -->
![Birth rates keep falling across seven economies - the United States and France highest near 1.4, Germany and Poland in the middle, Korea steepest of all, down to 0.5 children per woman](reports/figures/story_collapse.png)

On the same immigration-free arithmetic, Korea ends the century at roughly a quarter of its present size, Italy and Japan near a third, and even the United States and France lose close to a third of themselves. Nobody holds level.

## Why it happens

Three causes, in order of size. The largest, by a wide margin: fewer people pair up. Children overwhelmingly come from stable couples, and a rising share of people never become parents at all (Sobotka, 2017). The second: people start later. The average age at a first child has moved from the low twenties into the thirties, and fertility falls with age - postpone long enough and some intended children are never born. The third, and smallest: a genuine drop in how many children people want.

## Population momentum

A population is a shape - a stack of age groups - and that shape carries momentum. A young country keeps growing for decades after its birth rate falls below replacement, because so many people are only now reaching childbearing age. An old country starts shrinking the moment the rate drops, and would keep shrinking for a generation even if every couple returned to replacement tomorrow.

So the near future is largely already written: Korea's population in 2050 was decided in the 1990s. The model also catches the United States mid-crossing - it has already moved from the growing kind of country to the shrinking kind, and immigration alone now holds its numbers level.

## Interventions that work

Immigration is the only remedy that pays off inside a single lifetime: a newcomer arrives already grown, of working and child-bearing age, and fills the hollow middle of the pyramid immediately. Remove it from the arithmetic and the United States looks much like Europe. But migration reshuffles the world's existing young; it does not repair why a country stopped producing its own.

For that repair, the model weighed every proposed fix against the record of the places that have tried it. The winners are unglamorous: they lower the true, lifelong cost of raising a child, and they let people pair off and parent without wrecking a career. Seven keep recurring:

- **Marriageable young men** - restore the economic prospects of young men; the marriage market still sorts on them, and their relative decline stops couples forming (detail below)
- **Real childcare** - a job and a child stop being a forced choice
- **An honest split of the housework** between women and men
- **Family housing** the young can actually afford
- **Security for the young** - a footing stable enough to start a family on
- **Relationship skills taught in school** - communication, conflict, managing money together
- **Shorter work hours** - aimed at the punishing schedules of Korea and Japan

Their common feature is durability: they change the standing conditions of a life, and the effect lasts.

**The marriageable-men lever, in detail.** Men's earnings gate whether a couple forms: when young men's *relative* earnings fall, fewer unions form and fewer children follow. In US manufacturing towns hit by Chinese import competition, births fell **6.1 per thousand** women and marriages **4.2 percent** (Autor, Dorn & Hanson, 2019) - Wilson's "marriageable men" (1987). The out-of-wedlock share is the mechanism: in US fracking towns a clean earnings boost raised births about **3 percent** inside and outside marriage alike, with no change in the marriage rate (Kearney & Wilson, 2018). So the lever lifts the West *more* than the East: in Germany or the United States two in five births happen outside marriage, and a better footing turns into children through whatever partnership people are in; Korea and Japan gate almost everything behind marriage (one birth in forty outside it; Goldscheider et al., 2015), so from 0.72 the lever moves the dial without crossing the ridge.

<!-- The marriageable-men lever on the calibrated core (E36 broad male drive at I=30): bends every path, lifts the near-ridge West toward 1.5 (Germany ~1.49, USA ~1.66), leaves the deep basins below (Korea ~0.44, Poland ~1.16); a men-only lift roughly halves the effect. -->
![The same lever - restoring men's economic prospects - bends the line upward in Korea, Poland, Germany and the United States alike; it lifts the near-ridge West back toward the ridge but leaves the deep basins of Korea and Poland well below it](reports/figures/story_one_lever.png)

The lever politicians reach for first - cash - fails: a baby bonus buys a brief flurry of births, mostly children brought forward, then evaporates; it shifts the *timing* of births, not their *number* (receipts in the myths section). Two popular cures actively backfire: pro-natal poster campaigns, and sending women back to "traditional roles" - the societies with the most old-fashioned housework split have the *lowest* fertility.

## Cost-effectiveness of the fixes

Ranked by improvement per unit of money and effort, the winners are almost free - the same short list for every country:

- **Recognise unmarried couples in law**, the same as married ones - almost costless, and the best value of anything tested. A wedding has become a "capstone" couples feel they must be affluent to afford (Cherlin, 2004), so they wait for a marriage that may never arrive. France's PACS civil union did this; about **63%** of French children are now born outside marriage (INSEE)
- **Teach relationships in school** - conflict resolution, communication, family money. Cheap and well evidenced: in a randomised trial of 476 Army couples, **2.0%** of program couples had divorced a year on against **6.2%** of controls (Stanley et al., 2010), and across 4,574 couples money arguments were the strongest single predictor of divorce (Dew et al., 2012)
- **Nudge the culture toward fairness at home.** In a low-fertility country a birth happens roughly only when *both* partners want it (Doepke & Kindermann, 2019), and a mother carrying a full job plus most of the housework says *not yet*. The model rates easing that burden two to three times more cost-effective than equal-cost cash
- **Take the sharp edges off inequality.** A wide income gap makes every child ruinously expensive - tutoring, coaching, enrichment (Doepke & Zilibotti, 2019). South Korea pours some \$20 billion a year into private cram schools (Statistics Korea), about a tenth of household income, and has the lowest birth rate on Earth
- **Build family housing the young can afford** - build, rather than subsidise prices: a \$10,000 rise in house prices lifts births about **5%** among owners and cuts them **2.4%** among renters (Dettling & Kearney, 2014), so price subsidies transfer births from the young to the old. Housing demand is also endogenous to coupling - singles need a dwelling each where a couple shares one - so as coupling declines, Korea's household demand grows about **27%** by century's end, eating a +10% building program nearly three times over; every lever that helps couples form frees dwellings, funding roughly a tenth of its own gain

> [!IMPORTANT]
> **The male prospects problem**<br><br>Restoring young men's economic prospects is absent from this list because it is the *costliest* lever, not the largest: narrowing inequality lifts births more in every country - **+0.70** against **+0.27** in Korea, **+0.59** against **+0.43** in Germany, the male lever's best case (E36). It has two re-simulated limits: it *saturates* - the market sorts on *relative* standing, and lifting Korea to the ridge on men's earnings alone would take an income gain no economy has ever delivered - and a raise landing only on men widens the inequality that suppresses births, **cutting the effect roughly in half**; the strong form is broad-based and gender-balanced (Doepke & Kindermann, 2019). What the lever uniquely has is its aim: it reaches the one margin the broad reforms miss, and narrowing inequality delivers it cheaply.
>
> The harder barrier is cultural: accepting that young men - the group long assumed to hold the advantages - are now the ones whose prospects most need repair. If young men cannot form couples, the births do not follow.

These fixes help most when a country starts early. Cash ranks dead last for value. The chart below runs every lever through the same model for seven countries, including Poland - Europe's lowest-low at 1.16 by its own statistical office (GUS), below the higher UN estimate.

<!-- What each fix buys: every E20 lever on the calibrated core, ΔTFR at 2125 across seven nations - heatmap, rows by average effect. -->
![What each fix buys, country by country - the lift in the birth rate from every lever across seven nations, from inequality compression and childcare at the top to cash at the bottom](reports/figures/story_cheapest_fixes.png)

The male lever against the strongest broad fix, nation by nation:

<!-- The male lever vs narrowing inequality (the strongest E20 lever), both on the calibrated core, ΔTFR at 2125. -->
![The male-income lever measured against narrowing inequality, nation by nation - inequality lifts births more in every country, widest in Korea (+0.69 vs +0.28), narrowest in the near-ridge West](reports/figures/story_male_prospects.png)

## How fixes combine

Partly. A birth rate is the *product* of the things underneath it, so on a logarithmic scale independent levers add, plus one term measuring genuine reinforcement or interference. Two fixes pulling *different* channels - economic footing and a fair housework split - reinforce; two pulling the *same* channel saturate. An earlier round believed it had found dramatic "super-additive" bundles; a closer look showed the natural upward curve of a product and almost no real synergy. Stack levers that work through different mechanisms.

## Popular remedies that fail the evidence

This project does not take a side. Births, deaths and the shape of an age pyramid answer only to cause and effect, and several findings below will comfort one political camp and irritate another. The remedies the evidence does not support:

- **The myth of a return to tradition** - that the male-breadwinner, stay-at-home-mother family would raise births. The reverse: the most lopsided housework splits have the lowest fertility - South Korea at **0.72** and Japan at **1.21**, where married women do roughly **80%** of unpaid domestic work - and the more equal Nordic homes ran near **1.7-1.9** for decades. The women's-employment-versus-fertility correlation, strongly *negative* in 1980, flipped *positive* by the 2000s as men began sharing the load (Esping-Andersen & Billari, 2015; Goldscheider et al., 2015)
- **The myth of restricting divorce.** When US states adopted *unilateral* divorce, female suicide fell **8-16%**, domestic violence by about **a third**, and intimate-partner homicide of women around **10%** (Stevenson & Wolfers, 2006) - and restricting exit buys no extra births. Raising the cost of leaving removes the bargaining that lets couples de-escalate; in the model every lock-in lever backfires
- **The myth of the baby bonus.** South Korea spent on the order of **\$270 billion** over two decades while its birth rate fell from about **1.3 to 0.72**. Hungary spends about **5% of GDP** a year and bought a rebound that a timing-versus-quantity split shows is mostly postponed births returning (this campaign's E16 finding)
- **The myth that people simply stopped wanting children.** Across Europe the ideal family size people report still runs near **2.1-2.3** children against an actual rate around **1.5** - a "child gap" of **half a child** that desire cannot explain. The largest cause is that fewer people ever pair into the stable couples children mostly come from (Sobotka, 2017)
- **The myth of the permanent immigration fix.** Immigration holds some countries level today - strip it out and the United States' population shortfall widens by about **85%** (this campaign's E5 finding) - but it reshuffles the world's *existing* young, and the UN's replacement-migration study found ageing societies would need inflows many times any historical level. The planet as a whole cannot immigrate its way out

## Random fluctuations and tipping risk

Social attitudes wobble year to year; we measured that wobble from the world's marriage statistics and fed it into the simulation as genuine noise. The norm channel's equation is an exact double well, so the escape mathematics of physics - Kramers' law, most-probable paths - applies without approximation, and the simulation reproduces the theory's escape times to within half a percent:

```math
dN = -V'(N)\,dt + \sqrt{2\varepsilon}\,dB, \qquad \mathbb{E}[\tau_{\text{esc}}] \simeq \frac{2\pi}{\sqrt{V''(N_{\text{well}})\,|V''(N_{\text{tip}})|}}\; e^{\Delta V/\varepsilon}.
```

Under this noise the drift defines a least-action rule - the probability of a trajectory is weighed by how far it departs from the drift, so rare events concentrate on the cheapest path and a norm intervention is priced by the action it removes from the barrier:

```math
S[\varphi] = \frac{1}{4}\int \big(\dot\varphi + V'(\varphi)\big)^2 dt, \qquad P \sim e^{-S/\varepsilon}.
```

Three findings. **The asymmetry favours collapse**: falling *into* the cultural trap costs about 3.2 times less action than climbing out, so turbulence alone slowly ratchets countries the wrong way - doing nothing is a policy with a direction. **Outcomes become probabilities**: Germany, outside the trap on the deterministic map, carries roughly a **1-in-8 chance this century** of drifting in on turbulence alone; no trapped country has any meaningful chance of drifting *out* by luck. **Tipping usually arrives without warning**: the celebrated early-warning signals - rising variance and memory before a tipping point - are essentially invisible at a realistic forty years of annual data (detection power of a few percent), and even under ideal slow drift two thirds of the tips in our ensembles arrived unheralded. After the fact the pair does separate drift from turbulence: variance up with flat memory means noise; both up means the edge is near.

The policy reading: watch dispersion, not just averages - the population's spread announces a tip slightly before its mean crosses - and do not wait for an alarm that will probably never ring. A push either crosses the cultural threshold or mostly evaporates: go decisively or endow permanently; the worst value is the half-hearted middle.

## Israel, the exception

Israel holds at **2.83** children per woman, above replacement and alone in the developed world (UN WPP 2024) - the closest thing demography has to a natural experiment, so we calibrated it into the model as an eighth country (E37). The success is **not the ultra-Orthodox**: without the Haredi, secular and traditional Jewish Israelis still hold at or above replacement - secular Jews near **1.98**, the highest of any secular society on Earth, robust to controls for women's work and education (Okun, 2017; Weinreb, Taub Center, 2024).

The model locates it in coupling. Give South Korea Israel's **coupling** - near-universal, stable partnership - and its projected birth rate jumps **+0.35**; give it Israel's low childfree norm or low childlessness instead and nothing moves (-0.001, +0.008). Israel's pronatal culture is couples that form and stay formed - the exact channel every winning lever above already pulls. The copyable pieces are bounded: universal IVF is barely 4% of births (Birenbaum-Carmeli, 2016), and the childcare bundle behind 61% female employment is the gender-equity lever this project already ranks highest. Run it all through the model and a collapsing country reaches the 1.5 ridge, short of 2.83 - the rest is age structure, desired family size and the Haredi subculture, none of them under government control.

## Method: how the model was built and tested

The steps:

1. **Started with a hypothesis** - that a population collapses less because of low fertility alone than because of *when* the fall arrives and how old the society already is
2. **Wrote it as equations and built a simulation** that plays each population out year by year, every rate grounded in published research
3. **Calibrated to real data** until it reproduced recorded birth rates and age structures, then made predictions stated so they could be proved wrong
4. **Tested out of sample** - on data the model never saw, and against real shocks: the 2008 recession, the COVID dip, Korea's 1997 crisis, German reunification
5. **Kept what worked and stayed honest about what didn't** - the backbone reproduces real history; the behavioural layer is a simplified instrument
6. **Mapped the recovery/decline dividing line** and confirmed it lands where independent demographers put the danger line, at about 1.5
7. **Pre-registered 478 testable claims across fifty-two rounds** (E1-E52; three rounds audit the campaign itself), committing to success criteria *before* each run - each fix scored analytically, then simulated for generations, because a lever strong in year one can fade, revert or backfire
8. **Rated levers by cost to society** - money, coercion and side effects - and stripped winning bundles to the smallest, cheapest set that keeps most of the benefit

Technical summary. At the heart is a system of **seven coupled first-order differential equations** - pairing, childbearing, birth timing, economic security, the social norm and partner-marriageability pushing on one another - rolled forward a year at a time and fed into a **Leslie matrix** age projection with a **Rogers-Castro** migration curve, a **Bongaarts-Feeney** tempo correction and a **soft-bistable double-well** coupling trap; calibration is **Bayesian**, by the **reparameterisation trick** (Kingma & Welling, 2014) with an exact **one-dimensional Wasserstein** loss. Every equation is laid out in the walkthrough below. Roughly **89 source papers and 130+ structured digests** anchor the parameters; the data is **UN World Population Prospects 2024**; the campaign runs to **478 pre-registered hypotheses across 52 rounds**, all on a graphics card, so thousands of scenarios finish in seconds.

None of this arrived on the first try. The equations were rebuilt more than once, and a late rigor audit (E40) caught the birth-timing term applying **four times its documented strength** - fixed at the source, recalibrated, every headline number re-verified; the lever rankings survived, and the corrected, several-times-smaller "tempo mirage" is the figure to trust. A pre-registered test against the last 23 years of real data recorded the failure as prominently as the passes: the model re-tells Korea's collapse faithfully but has **no mechanism for recovery episodes** - Germany's and Poland's mid-2000s upturns are beyond it - so its forward runs rank collapse scenarios and levers, and forecast no recoveries. A large share of the 478 hypotheses came back **PARTIAL or REFUTED** (cash bonuses, tutoring bans, top-down propaganda among the casualties), which is why the SUPPORTED ones are more than wishful thinking.

**What this is: mature exploratory research.** The demographic backbone - ageing, momentum, the ranking of countries - is validated ground. The behavioural layer that turns a policy into a birth rate is a deliberately simplified research instrument, tuned to reproduce how real populations have behaved before it is trusted to say anything new: good enough to rank the forces at work and compare levers, not to forecast any nation's future to the decimal place.

## Conclusions

Outcomes depend on position and timing. A country still near the ridge - the United States, France, even Italy - can genuinely turn itself around if the effort is early, broad and built to last. A country far down the slope - Korea, Japan - can with the same maximal effort only soften a collapse into a decline; its base of young people is too thin for a single century to refill. The window closes one generation at a time, which is why the decisions that matter most are being taken now.

The model's value is triage: it identifies which levers are worth detailed study before money is spent on them. Nearly half of the 478 hypotheses came back PARTIAL or REFUTED; that filtering *is* the deliverable. The natural next step is to take each surviving lever to a real setting: one country, its registry data, and the things this pass had to simplify - family law, housing supply, the education arms race, migration.

> [!NOTE]
> The model and the narrative around it are the subjective view of the researcher, not a settled forecast. The researcher is now compiling a full summary of every intervention - strengths, weaknesses, side effects, costs, the policy that delivers it and the mechanics of how it works.

## Simulation internals: the equations and the yearly loop

Everything above came out of one simulation. This section lists the full equation system and walks through one simulated year. Every piece of mathematics named along the way is catalogued, with its reference, in the [scientific foundations inventory](docs/scientific-methods.md).

**The entire system.** Nine equations: seven coupled channel dynamics, one intergenerational memory, and the composition law that turns the channels into children.

```math
\begin{aligned}
\dot S &= k_S\bigl(S_0 + f_S - \Pi_{\text{dep}} - S\bigr) - \varepsilon_S
  &&\text{security}\\[3pt]
\dot C &= k_C\bigl(C^{\star} - C\bigr)
  - d\,\frac{\max(C_{\text{thr}}-C,\,0)\,\max(C-C_{\text{floor}},\,0)}{C_{\text{thr}}-C_{\text{floor}}}
  &&\text{coupling, with trap}\\[3pt]
&\qquad C^{\star} = C_0 + g_{SC}\,(S-S_0) + g_{qC}\,q + f_C - \varepsilon_C\,t \\[3pt]
\dot{\bar P} &= k_P\bigl(\bar P_0 + g_P\,f_P - \varepsilon_P\,t - \bar P\bigr)
  &&\text{parity}\\[3pt]
\dot\tau &= k_\tau\bigl(\tau_0 + g_\tau\,(S_0 - S) + f_\tau + \varepsilon_\tau\,t - \tau\bigr)
  &&\text{tempo}\\[3pt]
\dot\rho &= k_\rho\bigl(\rho_0 + g_\rho \max(\tau-30,\,0) - 0.05\,(S-S_0) + \lambda_\rho\,(N-N_0) + f_\rho - \rho\bigr)
  &&\text{childlessness}\\[3pt]
\dot N &= -a_N\,(N-N_{\text{lo}})(N-\theta_N)(N-N_{\text{hi}}) + f_N
  &&\text{norm, double-well}\\[3pt]
\dot q &= k_q\bigl(f_q + A - q\bigr)
  &&\text{marriageability}\\[3pt]
J &= \int_{\text{childhood}} \bigl[\,w_F\,(f_F + \phi\,q) - w_{\text{scar}}\,f_{\text{scar}}\,\bigr]\,\mathrm{d}s,
  \qquad A = g_A\,\langle J \rangle_{\text{ages 27-45}}
  &&\text{memory}\\[3pt]
\text{TFR} &= C\,(1-\rho)\,\bar P\;\mathrm{fec}(\tau)\;\max\bigl(1 - k_{BF}\,\Delta\tau,\;0\bigr),
  \qquad \mathrm{fec}(\tau) = e^{-0.03\,\max(\tau-30,\,0)}
  &&\text{composition}
\end{aligned}
```

Reading the system: six of the seven channel equations are *relaxations* - drift toward a moving target at speed $k$, the way coffee cools - and the mechanics live in four places. The coupling equation carries the **trap**: a decline well that switches on below $C_{\text{thr}}=0.66$, so low partnership is pulled lower still - the source of the two-basin fate map. The norm $N$ is the one non-relaxation: a cubic **double-well** (wells at $N_{\text{lo}}=0.14$ and $N_{\text{hi}}=0.42$, tipping point $\theta_N=0.25$) - push a society across it and it does not drift back. The **memory** pair $J, A$ integrates each cohort's childhood environment down its life-line and hands the completed integral to the marriage market 27-45 years later. And the **composition law multiplies**: every channel is a gate and a zero anywhere zeroes the product - no amount of cash rescues a society where couples do not form - while the Bongaarts-Feeney factor parks births in the future as $\tau$ rises, the mechanism behind the baby-bonus illusion. The $f_\bullet$ symbols are the **nine policy wires**; every lever tested in this project is a pattern of pushes on these wires, nothing else.

**Calibration anchors.** Each country enters as measured anchors - 2023 TFR and mean age at childbearing (UN WPP 2024; national offices where they disagree), lifetime ever-in-union coupling $C_0$, cohort childlessness $\rho_0$, security $S_0$, starting norm-well $N_0$; rate constants and gains come from 58 source papers. One identity closes the loop: the parity anchor is *solved* - $\bar P_0 = \text{TFR}_{2023} / \bigl(C_0(1-\rho_0)\mathrm{fec}(\tau_0)\bigr)$ - so the model starts from reality.

### Step-by-step simulation explainer

The forecast engine is exactly the yearly loop below: the numerical integration of the coupled behavioural equations handing a fertility schedule to the exact Leslie step. Everything else - the strand spread, the transport metric, the quantile representation, the noise layer - calibrates that engine, averages it honestly, or quantifies its uncertainty.

**State.** Two age vectors `N_f, N_m` (101 single-year classes, in thousands), plus **64 copies ("strands") of the seven behavioural channels** `(C, rho, Pbar, tau, S, N, q)`, plus two scalars: the dependency penalty and the cohort-memory drive.

**Setup, once per country:**

1. Load the observed data: UN WPP population by age and sex, survival ratios, the age-specific fertility profile, sex ratio at birth
2. Set each channel's starting value from a named observable (partnership share, cohort childlessness, mean age at childbearing, ...)
3. Spread each channel across the 64 strands by Latin-hypercube stratification, with `sigma` the channel's measured population dispersion (age at first birth: 3 years). The strand set is the exact 64-point quantile grid of the channel's marginal - a quadrature, not a sample; no randomness is drawn during a run
4. Solve the parity rescale so the year-one TFR equals the observed 2023 value. **OT is the calibration loss**: on the line, `W2^2` is the squared distance between the model's and the observed quantile functions, penalising location, spread and tails rather than the mean alone - this fit closed the prediction gap from 0.26 to 0.018 child where moment fits had not. OT never forecasts: every prediction comes from integrating the dynamics below; OT only scores the output

**One year, repeated 102 times (2023 to 2125):**

1. Read the year's policy forcing (levers ramp: zero for two years, full by year twelve; cash erodes exponentially afterwards)
2. Integrate the seven channel equations in four steps of dt = 0.25, clipping every state to its physical box after each step
3. Form each strand's fertility by the composition law `TFR = C * (1 - rho) * Pbar * fec(tau) * max(1 - kBF * dtau, 0)`, where `dtau` is the realized annual change of tau, never the integrator's sub-steps; average the 64 strands
4. Build the year's fertility schedule: each strand rescales the observed age profile to its own TFR and shifts it along the age axis by its own tempo deviation; average the 64 profiles
5. Leslie step: age every class by its survival ratio, add the newborn cohort, split by sex ratio. The baseline runs migration-free; migration is a lever to test
6. Feedback one: the new pyramid's dependency ratio, in excess of 2023, becomes next year's security drag
7. Feedback two: push this year's behavioural environment into the cohort memory. A cohort born in year `b` accumulates `J(b)` = the mean environment over its ages 0-17; the mean of `J` over the cohorts aged 27-45 drives marriageability

**Judging a lever:** run baseline and lever, identical in every other bit; the verdict is the difference - size at the century mark, durability (peak vs lasting effect, the mirage detector), side effects on the other channels. Every hypothesis states its pass/fail bar before the run, and the verdict-bearing numbers are pinned by a regression guard suite.

**Why 64 strands instead of one average agent:** near the norm tipping point the population splits - some strands cross, some hold - and the average of the per-strand fertilities differs from the fertility of the average state. And because the strands are deterministic, a lever verdict is the difference of two exact runs, with no sampling noise.

**Differentiability**: distributions are stored as quantile functions `theta = Q_phi(u)`, so gradients pass through sampling - the reparameterisation trick generalised to any shape; how much of this machinery ships is decided in the next section.

## Model structure: the two layers

Two layers, and a bridge between them. The **behavioural layer** is the ODE system above (tempo correction: Bongaarts & Feeney, 1998).

The **demographic backbone** is the **Leslie** operator (Leslie, 1945) - and Leslie is exactly the finite-difference form of the **McKendrick-von Foerster / Sharpe-Lotka renewal PDE** (McKendrick, 1926; von Foerster, 1959; Sharpe & Lotka, 1911; Lotka, 1939),

```math
\frac{\partial n(a,t)}{\partial t} + \frac{\partial n(a,t)}{\partial a} = -\mu(a,t)\,n(a,t), \qquad n(0,t) = \int_{0}^{\infty} \beta(a,t)\,n(a,t)\,\mathrm{d}a.
```

The transport term is the derivative *along a cohort's life-line* - the Lexis diagonal (Lexis, 1875) - and the boundary integral is the Lotka renewal condition. The age half of the model already **is** this PDE, solved along its characteristics.

**The bridge: the renewal PDE's cohort structure is delivered to the ODE system as an optimal-transport (OT) component** (Villani, 2009). Each behavioural channel can be carried as a free-form distribution $\rho(\theta,t)$ whose dynamics are a Wasserstein-2 gradient flow, the JKO scheme (Jordan, Kinderlehrer & Otto, 1998),

```math
\rho_{k+1} = \arg\min_{\rho}\ \mathcal{F}[\rho] + \frac{1}{2\tau}\,W_2^2\!\left(\rho,\rho_k\right),
```

with interventions and selection expressed as transport maps: a policy is a pushforward $T_\sharp\rho$, a selection cutoff a truncation, a targeted intervention a transport of the low-$q$ tail upward. Each channel's distribution is a **1-D normalising flow** - a monotone quantile function $\theta = Q_\phi(u)$, $u\sim\mathrm{Uniform}(0,1)$ (Rezende & Mohamed, 2015; monotone-spline flows, Durkan et al., 2019) - which keeps the **reparameterisation trick** (Kingma & Welling, 2014) alive for any shape, with implicit-reparameterisation gradients for the non-analytic case (Figurnov, Mohamed & Mnih, 2018), so the population stays differentiable end-to-end for calibration.

**The tradeoff, and the honest verdict.** An Eulerian PDE on a grid smears cohorts through numerical diffusion and its cost explodes with each added channel. The Lagrangian route - the method of characteristics - follows cohort *particles* down their life-lines: mass-conserving, diffusion-free. OT makes it exact and cheap: in one dimension the optimal plan is the monotone rearrangement, $W_2$ is the $L^2$ distance between quantile functions - the quantity that closed the calibration gap - and the morph between two population states is displacement interpolation (McCann, 1997); no cost matrix, no Sinkhorn iteration. The verdict is split: where the population's shape decides the outcome - each cohort's own life-course exposures, or a policy that *selects* rather than shifts - the machinery earns its place, and the intergenerational channel could not be written without it; but lifting the *whole* core onto it moved fertility by less than a thousandth of a child, so that lift was tested and cut. An elegant construction is kept only when it moves the numbers.

### Numerical solution and cohort trajectories

The equations above define a **vector field** on the seven-channel state space; a model year is one lap of that field plus one exact accounting step of the age pyramid.

**How the differential equations are solved.** Three answers. The age-structure PDE is solved analytically by the method of characteristics: cohorts propagate in closed form along their (age, time) diagonals, with the renewal integral imposed algebraically at the border each year. Only the COEFFICIENTS are discretised (rates held piecewise-constant within each year, exactly how the data arrives), never the differential operator: the one-year Leslie map is the exact solution of that piecewise-constant problem, and no finite-difference PDE solver exists in the code. The seven behavioural ODEs have no closed form and are integrated numerically (forward Euler, four steps of dt = 0.25 per year, states clipped to physical ranges). The bistable norm admits analytic treatment of its noise-driven escapes, and the numerics reproduce Kramers' escape law to 0.4% - the closed form validates the integrator where both exist.

**Cohorts are the particles of that characteristics solution**: a cohort born in year b travels its own diagonal through the (age, time) plane, and its childhood is a genuine path integral along that trajectory:

```math
J(b) = \frac{1}{18}\sum_{a=0}^{17} \mathrm{env}(b+a).
```

A parent cohort's *completed* integral sets the initial condition of the child cohort's line - how a childhood exposure, such as a father-figure deficit, is transmitted to the next generation. This is why the model catches generational reversals: a lever that flatters today's adults while souring today's childhoods flips sign about twenty years later, when the soured cohorts arrive.

## Project documentation

- **The scientific foundations** - every equation, theorem, estimator and numerical scheme in the model, catalogued with its reference: [`docs/scientific-methods.md`](docs/scientific-methods.md)
- **The evidence log** - all 478 questions put to the model and how each turned out: [`docs/experiments/demographic-collapse-experiments.md`](docs/experiments/demographic-collapse-experiments.md)
- **The reference library** - the papers and grounded distributions behind the model ([`references/`](references/)), including composed proxy blueprints for levers no one has run a clean experiment on ([`references/proxies/`](references/proxies/))

## Run it

```bash
make install     # set up the environment and install the package
make test        # run the tests
```

## Makefile and project map

- `make install` / `make test` / `make lint` / `make format` / `make build` / `make clean` - the usual developer commands (`make help` lists them all)

```
├── data/raw            <- the source population data (United Nations, World Bank, and others)
├── notebooks           <- the investigation end to end
├── src                 <- the reusable model code
├── docs                <- the story, the design, the intervention guide, the evidence log
├── reports/figures     <- every chart the notebooks produced
└── references/papers   <- the research papers behind the findings, with plain-language summaries
```
