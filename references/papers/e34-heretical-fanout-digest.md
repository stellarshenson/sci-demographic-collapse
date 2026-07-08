# [Research digest] E34 - Heretical & Coercive Natalism Fanout (H314-H338)

**Round**: E34 (contrarian / heretical fanout)  **Hypotheses**: H314-H338 (25)<br>
**Scope**: coercive, zealous, theocratic and structural natalism across POLICY, CULTURE, RELIGION, ZEAL<br>
**Model interface**: channel-forcing vector `f={...}` + defection δ∈[0,1] + named side-effect cost<br>
**Purpose**: stress-test the campaign's own findings (coupling keystone; cash mirage; coercion backfires; structure beats psychology; establishment-religion inert under high security) against the most extreme levers in the historical record and one fictional maximum (Gilead)

## Overview

This round deliberately goes to the edge of the design space - the levers that decent liberal policy discourse refuses to say out loud - and grounds each in a real historical analogue wherever one exists. The unifying question: does ZEAL buy fertility that CASH cannot, and if so, through which channel, and at what cost on the metrics we care about (women's autonomy, coercion, pluralism, fiscal, welfare)?

The honest answer the evidence returns is a sharp bimodal split, and it maps cleanly onto the campaign's existing spine:

- **Coercion, penalties and bans REFUTE almost uniformly.** Severity without certainty is zero deterrence; people evade (high δ), and the autonomy/rights cost is enormous even when the raw fertility signal is real. Romania's Decree 770 is the archetype: a 1.9→3.7 crude-birth-rate spike in one year that fully reverted and left the highest maternal-mortality rate in Europe. Singapore's eugenic Graduate Mothers Scheme was rescinded within a year under electoral revolt. Iran's contraception rollback did not restore target fertility. Abortion bans (SB8, Dobbs, Poland) produce a small (+3-4%), spatially concentrated, and in Poland temporary bump - real but far below the coercion cost, and confirming the E25 interior-optimum refutation that bans overshoot.
- **A FEW un-buyable, devotion- or structure-based levers genuinely SUPPORT.** The Georgian Patriarch's third-child baptism is the cleanest positive outlier in the modern record: +28% births in two years, entirely in married and third-order fertility, driven by a sacred act that literally cannot be purchased or faked (δ≈0). Demeny/proxy voting supports as a structural commitment device (Boffa et al. show a Pareto improvement via future-oriented spending). Sacralising motherhood as a NORM - without the penalty attached - re-expresses the norm channel the way religion does under Norris-Inglehart, and is the transferable core of the Georgia case.

The dividing line is not religion-vs-secular or zeal-vs-restraint. It is **whether the lever operates by removing options (backfires, high δ, autonomy cost) or by re-pricing a norm people are free to decline (works, δ≈0, low cost).** Zeal helps only in the second mode; in the first it is just coercion with a higher stake, and weaponisation tracks the stake.

## Channel legend (fertility-raising sign)

`fN` norm (NEGATIVE = pronatal, lowers childfree-ideal) · `fC` coupling (+) · `fPb` parity (+) · `fTau` tempo (NEGATIVE = earlier) · `fRV` childlessness (NEGATIVE = less) · `fS` security (+) · `fq` marriageability (+) · `fF` father investment (+) · `fScar` relationship conflict (NEGATIVE = less)

Magnitudes are on a rough per-channel TFR-forcing scale (|m|≲0.4 strong, ~0.1-0.2 moderate, ≲0.05 weak), calibrated to the cited effect size. δ is the evasion fraction (bans/coercion high; un-buyable/structural ≈0).

## Cross-generational spine (the reason E34 needs the path integral)

The model now tracks per-cohort effects through `ot.CohortMemory`: each year's childhood environment `env = wF*fF - wScar*fScar` is integrated over a birth cohort's childhood and fed 27-45 years later into marriageability `q`, which gates coupling `C`. So any lever that moves father investment (`fF`), relationship conflict/scarring (`fScar`), or the NORM (`fN`) the next cohort inherits carries a DELAYED, compounding, or REVERSING signature that a static ΔTFR cannot see.

Every hypothesis below therefore carries two extra fields:

- **cross_gen** - the gen-1-vs-gen-4 story: does the contemporary effect survive, compound, or reverse a generation later, and through which channel (fF/fScar into the childhood-env integral, or the norm N transmitted into the next cohort's fertility basin)?
- **intergen_sign** - does the lever's sign FLIP across generations (SUPPORTED-now → REFUTED-later, or the reverse)?

**The batch thesis, centred on Romania's Decrețel generation: coercion can win the first generation and lose the third.** A forced gen-1 birth spike that is resented, institutionalised and orphanage-scarred (high fScar, low fF) transmits a damaged cohort into the path integral, so run_cal shows the gen-1 boost REVERSING into a deeper gen-3-4 collapse - a sign-flip invisible to any contemporary metric. The mirror image is the un-buyable-devotion set (Georgia baptism, sacralised-motherhood norm, high-retention community): these transmit POSITIVELY forward (fF+, low fScar, pronatal norm inherited) and hold or compound. **Coercion reverses; devotion compounds** - that contrast is the payoff and the reason the path integral was built.

---

## The 25 hypotheses

### H314 - Decree 770 total ban (abortion + contraception)
- **Mechanism**: criminalise abortion and contraception to force births; the pure coercion maximum in the modern demographic record
- **f** = { fPb: +0.15, fTau: -0.05, fRV: -0.05 } (raw forcing) → net collapses under δ
- **δ** = 0.75 (clandestine abortion returned within years; illegal-abortion maternal deaths soared)
- **Side-effect cost**: { women's autonomy/rights: -0.9 (catastrophic), welfare: -0.4 (highest maternal mortality in Europe) }
- **Analogue**: Romania, Ceausescu 1966. TFR 1.9→3.7 (1966→67), the 1967-68 cohort the largest in Romanian history, back near baseline by 1983; 100k-170k children in orphanages by 1989 ([Wikipedia, Decree 770](https://en.wikipedia.org/wiki/Decree_770); [1980s-1990s Romanian orphans phenomenon](https://en.wikipedia.org/wiki/1980s%E2%80%931990s_Romanian_orphans_phenomenon))
- **cross_gen**: THE canonical reversal. Gen-1 is a genuine fPb+ spike (TFR 1.9→3.7). But the forced cohort is resented and institutionalised - Bucharest Early Intervention Project documents 7-9 point IQ loss, insecure attachment, elevated psychopathology persisting to adulthood - so it enters the path integral as high fScar + low fF. That damaged env, integrated over childhood and fed forward ~27-45 yr, depresses the next cohort's marriageability `q` and coupling `C`. The "Decrețel" grew up to spearhead the 1989 revolution that overturned the regime AND to drive a deeper post-1989 fertility collapse. run_cal signature: gen-1 boost, gen-3-4 undershoot below the no-policy baseline
- **intergen_sign**: FLIPS - SUPPORTED-looking at gen-1 (raw ΔTFR positive) → REFUTED by gen-3-4 (scarring transmitted through fScar/fF reverses the sign); the flip is the whole point
- **Verdict-LEAN**: **REFUTED** - the canonical mirage-then-collapse AND the canonical cross-generational reversal; δ eats the contemporary gain, the path integral eats the next generation, and the autonomy cost is total

### H315 - Mutterkreuz honour decoration (pronatal medal)
- **Mechanism**: state honour (Mother's Cross, bronze/silver/gold by child count) to re-price motherhood as national service via the norm channel, no penalty
- **f** = { fN: -0.05, fPb: +0.03 }
- **δ** = 0.1 (nothing to evade; also nothing much to gain)
- **Side-effect cost**: { pluralism: -0.3 (racial-eugenic eligibility), coercion: -0.2 }
- **Analogue**: Nazi Germany, Cross of Honour of the German Mother, 1938. CBR 14.7 (1933)→19.7 (1938) but historians attribute most of the rise to the abortion ban and marriage loans, not the medal ([History.com](https://www.history.com/this-day-in-history/december-16/hitler-institutes-the-mothers-cross); [Grokipedia](https://grokipedia.com/page/Cross_of_Honour_of_the_German_Mother))
- **cross_gen**: weak-but-honest forward transmission. A pure-honour norm (fN-) is inherited by the next cohort's basin without scarring - no fScar/fF damage - but the signal is small, and the racial-eugenic framing poisons the norm it transmits. Net gen-4 ≈ gen-1 (both near zero)
- **intergen_sign**: no flip - weak and stable; PARTIAL now, PARTIAL later
- **Verdict-LEAN**: **PARTIAL** - pure-honour norm nudge is weak and confounded by the coercive package around it; the medal itself moved little

### H316 - Childlessness tax + Mother-Heroine medals
- **Mechanism**: penalise the childless (tax on childless/1-2-child adults) while honouring the prolific (Mother Heroine at 10+); penalty + honour combined
- **f** = { fN: -0.05, fPb: +0.05, fRV: -0.03 }
- **δ** = 0.3 (tax is a flat penalty, weak behavioural pull; wartime demographic confound)
- **Side-effect cost**: { women's autonomy/rights: -0.3, coercion: -0.3 }
- **Analogue**: USSR, childlessness tax (1941, amended) + Mother Heroine title (1944), ~430,000 awarded ([Wikipedia, Mother Heroine](https://en.wikipedia.org/wiki/Mother_Heroine))
- **cross_gen**: the penalty arm breeds resentment that transmits forward (mild fScar+ on the coerced), while the honour arm is inert; wartime cohort confound dominates either signal. Gen-4 slightly worse than gen-1 through the resentment channel
- **intergen_sign**: weak flip risk - marginally SUPPORTED-ish at gen-1, drifts toward REFUTED via the penalty's transmitted resentment, but too small and confounded to resolve cleanly
- **Verdict-LEAN**: **PARTIAL** - the penalty arm is coercion-adjacent (backfires per campaign finding); the honour arm is inert; heavy wartime/postwar confound

### H317 - Eugenic Graduate Mothers Scheme (selective natalism)
- **Mechanism**: reward high-"quality" (graduate) mothers with school-priority and tax breaks while subsidising sterilisation of the poor - fertility raising conditioned on class/IQ
- **f** = { fPb: +0.03 } (graduate subgroup only), net near zero population-wide
- **δ** = 0.4 (target group declines to comply; scheme repudiated)
- **Side-effect cost**: { pluralism: -0.8 (overt eugenics), women's autonomy/rights: -0.5 }
- **Analogue**: Singapore 1984; rescinded within a year after electoral backlash cost the PAP seats; national TFR still fell to 1.42 by 1986 ([Wikipedia, Population planning in Singapore](https://en.wikipedia.org/wiki/Population_planning_in_Singapore))
- **cross_gen**: transmits a divisive class/racial norm forward (fN poisoned) plus a legitimacy wound; the sterilised-poor cohort is permanently smaller while the resented graduate-preference norm depresses the basin. Gen-4 worse via a fractured, stratified norm inheritance
- **intergen_sign**: no positive flip - REFUTED now, REFUTED later and arguably worse (the eugenic norm compounds the harm forward)
- **Verdict-LEAN**: **REFUTED** - eugenic conditioning triggers immediate political revolt; the autonomy+pluralism cost is disqualifying and the fertility effect is nil

### H318 - Sacred third-child baptism (un-buyable devotion)
- **Mechanism**: the Patriarch personally baptises and godfathers every 3rd+ child of married Orthodox couples - a sacred, non-fungible honour that cannot be bought, faked, or means-tested; forces the norm + parity channels for married couples only
- **f** = { fPb: +0.35, fN: -0.15, fC: +0.10 }
- **δ** = 0.05 (there is nothing to evade and the reward is intrinsically un-gameable)
- **Side-effect cost**: { pluralism: -0.15 (Orthodox-married conditioned), women's autonomy/rights: -0.05 (voluntary) }
- **Analogue**: Georgia, Patriarch Ilia II, from 2007-08. Births 49k(2007)→57k(2008)→63k(2009), +28% in two years; entire rise in MARRIED fertility, third-order births nearly doubled, ~34.5% of 3rd+ births baptised ([IFS](https://ifstudies.org/blog/in-georgia-a-religiously-inspired-baby-boom); [Lyman Stone, Medium](https://medium.com/migration-issues/did-the-promise-of-baptism-really-boost-fertility-in-georgia-cf534d92615c))
- **cross_gen**: the mirror image of Decree 770 - devotion COMPOUNDS. Births occur inside intact, married, high-commitment households (fF+, low fScar), so the cohort enters the path integral with a HEALTHY childhood-env, raising its later marriageability `q` and coupling `C`, and it inherits the pronatal sacred norm (fN-) directly. Gen-4 holds or exceeds gen-1; the norm self-propagates without renewed intervention
- **intergen_sign**: no flip - SUPPORTED now, SUPPORTED (or stronger) later; the positive transmission is the reason it is the batch's anchor case
- **Verdict-LEAN**: **SUPPORTED** - the campaign's un-buyable-devotion existence proof; devotion×(δ≈0) is exactly why it works where cash (mirage) fails, and it compounds forward rather than reversing

### H319 - Contraception rollback / pronatalist reversal
- **Mechanism**: defund and prohibit family planning, ban sterilisation and free contraceptives to raise fertility by removing means
- **f** = { fPb: +0.05, fTau: -0.03 } raw; net small
- **δ** = 0.5 (private-market contraception + demand persists; TFR did not return to target)
- **Side-effect cost**: { women's autonomy/rights: -0.6, welfare: -0.3 (unsafe abortion, inequality) }
- **Analogue**: Iran post-2012 (Khamenei declares prior policy "wrong"); modern contraceptive use fell 67%→31% but TFR stayed near/below replacement ([Family planning in Iran, Wikipedia](https://en.wikipedia.org/wiki/Family_planning_in_Iran); [Tandfonline critical review](https://www.tandfonline.com/doi/full/10.1080/26410397.2023.2257075))
- **cross_gen**: mistimed/unwanted births carry elevated fScar and depressed fF into the integral (resented pregnancies, constrained mothers), so the small gen-1 signal decays and the transmitted resentment + eroded autonomy norm depress the next cohort's basin. Gen-4 below gen-1
- **intergen_sign**: FLIPS weakly - a small positive at gen-1 → negative by gen-3-4 as the unwanted-childhood signal transmits forward
- **Verdict-LEAN**: **REFUTED** - removing options does not create demand; autonomy cost high, effect small, δ large, and what little it forces reverses forward

### H320 - Lifetime tax exemption for 4+ children
- **Mechanism**: permanent income-tax exemption for mothers of 4+, plus car/housing subsidy - the richest fiscal pronatalist package in the OECD; operates via security + parity
- **f** = { fS: +0.10, fPb: +0.08, fTau: -0.08 (tempo pull-forward inflates period TFR) }
- **δ** = 0.15 (some timing-gaming; benefit is real but conditional on high parity)
- **Side-effect cost**: { fiscal: -0.5 (~5% GDP, top-5 OECD family spending) }
- **Analogue**: Hungary 2019-20 Family Protection Action Plan. TFR 1.25(2010)→1.59(2021), +27%, but heavily tempo-inflated and expensive per marginal birth ([IFS](https://ifstudies.org/blog/is-hungary-experiencing-a-policy-induced-baby-boom); [N-IUSSP](https://www.niussp.org/fertility-and-reproduction/evaluating-pronatalist-policies-with-tfr-brings-misleading-conclusions-examples-fromhungary/))
- **cross_gen**: benign but decaying. The security arm (fS+) improves childhood-env slightly (some fF+ via reduced financial stress, no scarring), so a modest positive transmits; but the tempo arm is pure pull-forward that borrows gen-2 births into gen-1 and reverses as those births fail to appear later. Net gen-4 ≈ tempo-corrected small positive, well below the gen-1 headline
- **intergen_sign**: partial flip on the tempo component only - the period-TFR headline overstates gen-1 and the quantum-adjusted forward signal is smaller; the security component does not flip
- **Verdict-LEAN**: **PARTIAL** - real but partly tempo mirage; the cash-is-a-mirage finding applies with a security discount; not nothing, not the escape

### H321 - Covenant marriage / abolish no-fault divorce
- **Mechanism**: raise the exit cost of marriage (mandatory counselling, fault-only divorce) to lengthen unions and thereby raise fertility
- **f** = { fC: +0.03, fScar: +0.10 (WRONG SIGN - traps conflict, RAISES it) }
- **δ** = 0.6 (near-zero voluntary uptake; couples simply don't choose it)
- **Side-effect cost**: { women's autonomy/rights: -0.4 (exit-cost falls on the abused), welfare: -0.2 }
- **Analogue**: Louisiana covenant marriage 1997 (also AZ, AR) - tiny uptake; contradicts the Stevenson-Wolfers exit-valve (no-fault divorce REDUCED spousal violence/suicide by restoring bargaining) ([Covenant marriage, Wikipedia](https://en.wikipedia.org/wiki/Covenant_marriage); Stevenson-Wolfers 2006, in-project digest)
- **cross_gen**: the exit-valve backfire is a fScar ENGINE across generations - trapping high-conflict couples raises childhood exposure to parental conflict (fScar+, fF effectively down as fathers disengage), which the integral carries forward to depress the next cohort's coupling. A lever that barely moves gen-1 actively damages gen-3-4
- **intergen_sign**: FLIPS toward worse - inert/slightly-negative at gen-1 → more negative by gen-4 as trapped-conflict childhoods transmit; classic hidden-cost sign deterioration
- **Verdict-LEAN**: **REFUTED** - raising exit cost removes the de-escalation that keeps couples together; the valve backfires, no one opts in, and the trapped-conflict childhoods scar the next generation

### H322 - Demeny / parental proxy voting (franchise by children)
- **Mechanism**: give parents a proxy vote per child - a structural commitment device that tilts the whole polity toward child-friendly spending, raising security endogenously; un-buyable, δ≈0
- **f** = { fS: +0.12, fN: -0.05 }
- **δ** = 0.03 (structural; nothing to evade)
- **Side-effect cost**: { pluralism: -0.15 (one-person-one-vote tension), fiscal: +0.1 (reallocates, doesn't burn) }
- **Analogue**: Demeny's proposal; Boffa, Reggiani, Rizzolli, Trombetta model proxy voting as a commitment device that raises future-oriented spending, childcare, and fertility - a Pareto improvement for non-parents too ([SSRN 4612742](https://papers.ssrn.com/sol3/Delivery.cfm/4612742.pdf?abstractid=4612742); [Demeny voting, Wikipedia](https://en.wikipedia.org/wiki/Demeny_voting))
- **cross_gen**: structurally compounding. By tilting the polity toward child-friendly spending it raises fS for the CHILDHOOD environment of the next cohort (better childcare, early-years investment), improving the env integral and feeding forward into higher marriageability. The pro-child norm is also inherited. Gen-4 > gen-1 - one of the few genuinely compounding levers
- **intergen_sign**: no flip, positive drift - SUPPORTED now, more SUPPORTED later as the reallocated investment matures in the next cohort
- **Verdict-LEAN**: **SUPPORTED** - the rare structural, un-buyable, low-coercion lever; works because it re-prices the political norm, not the individual, and compounds forward

### H323 - Child-linked pension (internalise the pension externality)
- **Mechanism**: make pension entitlement rise with children raised, correcting the free-rider externality where the childless consume the next generation's labour; conscription/tax exemptions for parents are the same family
- **f** = { fS: +0.08, fPb: +0.05 }
- **δ** = 0.1 (structural; modest pull)
- **Side-effect cost**: { fiscal: -0.2, welfare: -0.1 (penalises the involuntarily childless) }
- **Analogue**: Boldrin-De Nardi-Jones - pay-as-you-go pensions explain a large share of the fertility decline (pension≈10% GDP ↔ −0.7 to −1.6 TFR); corrective instruments exist but are thin ([BDJ 2005, in-project digest])
- **cross_gen**: slow-compounding and benign. Child-linked pensions raise old-age security tied to the next generation, a structural fS+ with no scarring; the effect is inherently multi-decadal so its signature is almost entirely in the forward direction (gen-2-4), barely visible at gen-1. Holds and mildly compounds
- **intergen_sign**: no flip - the sign is stable positive but the magnitude is back-loaded; a static gen-1 ΔTFR understates it
- **Verdict-LEAN**: **PARTIAL** - the externality is real and large; the corrective lever is structurally sound but empirically thin and slow

### H324 - State-run matchmaking / assortative markets
- **Mechanism**: public dating/matchmaking agencies to fix thin marriage markets, raising coupling and effective marriageability
- **f** = { fC: +0.08, fq: +0.06 }
- **δ** = 0.2 (voluntary; take-up modest)
- **Side-effect cost**: { women's autonomy/rights: -0.05 (low if voluntary) }
- **Analogue**: Singapore SDU, Japan/Korea municipal konkatsu programmes - modest, non-transformative; coupling is the keystone but the state is a weak matchmaker
- **cross_gen**: neutral-to-mildly-positive forward. Matches formed voluntarily carry no scarring; if they produce intact households they transmit fF+ weakly forward, but the instrument is too weak to move the cohort env much. Gen-4 ≈ gen-1, both small
- **intergen_sign**: no flip - stable weak positive across generations
- **Verdict-LEAN**: **PARTIAL** - right channel (coupling), weak instrument; helps at the margin, does not bend fate

### H325 - Bride-price / dowry revival (marriage-payment lever)
- **Mechanism**: revive marriage payments to accelerate and universalise marriage, intending to raise fertility
- **f** = { fC: +0.05, fPb: -0.05 (bride price REDUCES fertility pressure - wrong sign in monogamy) }
- **δ** = 0.3
- **Side-effect cost**: { women's autonomy/rights: -0.4 (commodification), welfare: -0.2 }
- **Analogue**: rural Senegal - higher bride price REDUCES fertility pressure, robust to controls, effect strongest for economically dependent women; DRC finds no fertility link ([Tandfonline, Bride Price and Fertility Senegal](https://www.tandfonline.com/doi/full/10.1080/00220388.2016.1208178))
- **cross_gen**: transmits a commodifying gender norm forward (girls priced as transfers), degrading the inherited fN and women's-autonomy environment; combined with the near-zero-to-negative contemporary sign, gen-4 is no better and the norm damage compounds
- **intergen_sign**: no positive flip - REFUTED now, REFUTED later with a worsening norm-transmission tail
- **Verdict-LEAN**: **REFUTED** - the sign is ambiguous-to-negative and the commodification cost is high; not a usable lever in a modern monogamous market

### H326 - Legalise polygamy as a fertility lever
- **Mechanism**: permit plural marriage so high-status men father more children, intending aggregate fertility gain
- **f** = { fPb: -0.10 (per-woman fertility FALLS with more co-wives), fq: -0.05 (starves the male marriage market) }
- **δ** = 0.2
- **Side-effect cost**: { women's autonomy/rights: -0.5, coercion: -0.3 }
- **Analogue**: sub-Saharan DHS and LDS historical data - per-woman fertility DECLINES with wife-rank and number of co-wives (~1 child fewer in Kenya/Ivory Coast); LDS plural wives had fewer children ([PubMed, Polygyny and fertility SSA](https://pubmed.ncbi.nlm.nih.gov/12315486/))
- **cross_gen**: compounds NEGATIVELY. Polygyny starves the young-male marriage market (unmarried surplus men, fq-), a distortion that propagates forward, and co-wife/half-sibling households carry weaker per-child paternal investment (fF-) into the integral. Gen-4 worse than the already-negative gen-1
- **intergen_sign**: no flip - REFUTED now, more REFUTED later; the marriage-market imbalance is self-reinforcing across cohorts
- **Verdict-LEAN**: **REFUTED** - the per-woman sign is negative; polygyny lowers not raises the TFR object, and unbalances the marriage market

### H327 - Lower the marriage / consent age
- **Mechanism**: reduce legal marriage age to lengthen the reproductive window and raise completed fertility
- **f** = { fTau: -0.20 (earlier first birth), fPb: +0.15 (more completed births) }
- **δ** = 0.1 (mechanically effective)
- **Side-effect cost**: { women's autonomy/rights: -0.9 (catastrophic), welfare: -0.6 (health, education, IPV) }
- **Analogue**: 15-country study - women marrying before 18 begin childbearing earlier and have more children; but systematic reviews document severe health/education/autonomy harm ([BMC Public Health, health consequences of child marriage](https://pmc.ncbi.nlm.nih.gov/articles/PMC8845223/))
- **cross_gen**: the gen-1 fertility gain is real but the child brides become mothers with truncated education, high IPV exposure and low agency, so their children inherit a low-fF, elevated-fScar, low-human-capital env - the integral carries this forward as depressed marriageability and a damaged autonomy norm. Gen-3-4 erodes toward or below baseline
- **intergen_sign**: FLIPS on welfare-adjusted terms - raw-fertility SUPPORTED at gen-1 → REFUTED by gen-3-4 once the scarred-childhood transmission is counted (and disqualified on autonomy grounds regardless)
- **Verdict-LEAN**: **REFUTED** - the mechanism "works" at gen-1 and that is exactly why it is disqualified; the autonomy+welfare cost dwarfs any birth gain and the scarred cohort reverses it forward (heretical by construction)

### H328 - Abortion ban (Dobbs / SB8 / Poland)
- **Mechanism**: restrict abortion to convert averted-abortion pregnancies into births
- **f** = { fPb: +0.05, fRV: -0.03 } (small, concentrated on low-access populations)
- **δ** = 0.4 (travel, pills, cross-border; Poland effect reverted in ~20 weeks)
- **Side-effect cost**: { women's autonomy/rights: -0.6, welfare: -0.3 (infant/maternal mortality up) }
- **Analogue**: Texas SB8 ~+9,800 births / +3% in 2022 ([JHU](https://publichealth.jhu.edu/2023/measuring-impacts-of-sb8-in-texas)); post-Dobbs +3-4% concentrated in low-access states ([ScienceDirect, effects of post-Dobbs bans](https://www.sciencedirect.com/science/article/pii/S0047272724000604)); Poland 2021 decline temporary, reverted in ~20 weeks ([WNE WP475](https://www.wne.uw.edu.pl/application/files/5817/4661/9129/WNE_WP475.pdf))
- **cross_gen**: the marginal births are disproportionately to low-access, low-resource, unwanted-pregnancy households - exactly the profile that enters the integral with elevated fScar and low fF; the Turnaway-study logic (denied-abortion children fare worse) means the small gen-1 bump transmits a below-average childhood-env forward. Gen-3-4 gives back the gen-1 gain
- **intergen_sign**: FLIPS - small positive at gen-1 → negative-leaning by gen-3-4 through the unwanted-child transmission channel
- **Verdict-LEAN**: **PARTIAL→REFUTED** - a small, real, spatially-concentrated bump that confirms the E25 interior-optimum refutation (bans overshoot the optimum); autonomy+welfare cost far exceeds the birth signal and the marginal cohort reverses forward

### H329 - Conscription exemption / national service for parents
- **Mechanism**: exempt parents from mandatory service (or reward service-completion with child benefits), pricing parenthood as a civic substitute
- **f** = { fPb: +0.03, fS: +0.03 }
- **δ** = 0.2
- **Side-effect cost**: { pluralism: -0.15, welfare: -0.05 }
- **Analogue**: speculative; loosely Israel (service culture coexists with high TFR 3.0 but driven by religiosity/community, not the exemption) - no clean causal identification
- **cross_gen**: neutral forward - a voluntary civic-exchange nudge with no scarring; if it produces intact parented households it transmits a weak fF+/fS+ forward, but the effect is small and evidence-free. Gen-4 ≈ gen-1
- **intergen_sign**: no flip - stable weak positive, if any
- **Verdict-LEAN**: **PARTIAL** - plausible small parity nudge, no clean evidence; the Israel TFR outlier is norm/community, not the service rule

### H330 - Gilead: established coercive theocratic natalism
- **Mechanism**: total state theocracy that assigns reproductive labour by force - the coercion maximum; every channel forced simultaneously by law and violence
- **f** = { fPb: +0.30, fRV: -0.20, fN: -0.20 } raw → annihilated by δ and resistance
- **δ** = 0.85 (maximal evasion, sabotage, exit, and legitimacy collapse; weaponisation tracks the stake)
- **Side-effect cost**: { women's autonomy/rights: -1.0 (total), coercion: -1.0, pluralism: -1.0 }
- **Analogue**: fictional (Atwood), but the historical scaling law is Decree 770 × Iran × Singapore - each coercive maximum reverted and de-legitimised
- **cross_gen**: the maximal reversal - Decree 770 taken to the limit. Any forced gen-1 births occur in a regime of total coercion, so the entire cohort is raised in a maximally scarred, resented, low-agency environment (fScar saturated, fF collapsed), transmitting the deepest possible damage into the integral; the cohort's defining act is revolt. Gen-3-4 collapses far below baseline
- **intergen_sign**: FLIPS hardest - whatever raw gen-1 forcing survives δ → deeply REFUTED by gen-3-4; the model would show the largest sign reversal in the batch
- **Verdict-LEAN**: **REFUTED** - the theoretical ceiling of the coercion-backfire law; the higher the stake, the harder the defection, the faster the legitimacy collapse, and the more violent the cross-generational reversal

### H331 - Sacralise motherhood as norm (no penalty)
- **Mechanism**: elevate motherhood as a high-status sacred vocation through culture and ritual WITHOUT any penalty on the childless - the transferable core extracted from the Georgia case; pure norm channel
- **f** = { fN: -0.15, fPb: +0.08 }
- **δ** = 0.08 (voluntary; nothing to evade, nothing coerced)
- **Side-effect cost**: { women's autonomy/rights: -0.1 (mild expectation pressure), pluralism: -0.1 }
- **Analogue**: Georgia (H318) generalised; Norris-Inglehart - religion re-expresses norm+community and raises fertility where it retains meaning; the norm, not the establishment, is the active ingredient
- **cross_gen**: compounds through the norm channel. Because it works by elevating a freely-held norm, the next cohort inherits a pronatal fN directly, with no scarring and (via valued, intact parenting) mild fF+; the norm is self-transmitting, so the effect persists without renewed forcing. Gen-4 ≥ gen-1 - the devotion-compounds side of the batch thesis in its most transferable form
- **intergen_sign**: no flip, positive persistence - SUPPORTED now, SUPPORTED later; the norm inheritance is what makes it durable where cash decays
- **Verdict-LEAN**: **SUPPORTED** - re-pricing a norm people may freely decline is the mode that works and self-propagates forward; this is the un-buyable-devotion lesson without the Orthodox-marriage gate

### H332 - Apocalyptic / martyrdom-reward high fertility (Quiverfull)
- **Mechanism**: eschatological framing (children as arrows, afterlife reward, spiritual warfare) drives voluntary very-high fertility inside a committed subpopulation
- **f** = { fN: -0.30, fPb: +0.25, fRV: -0.15 } (WITHIN the subpopulation only)
- **δ** = 0.05 internally, but non-transferable to the population
- **Side-effect cost**: { women's autonomy/rights: -0.4 (submission theology), pluralism: -0.1 }
- **Analogue**: Quiverfull movement, ~10+ children per couple, but only "thousands to low tens of thousands" of families ([Quiverfull, Wikipedia](https://en.wikipedia.org/wiki/Quiverfull))
- **cross_gen**: compounds WITHIN the subpopulation via norm inheritance and intact high-investment households (fN-, fF+, low fScar), so the subgroup grows geometrically across generations - PROVIDED retention holds. The forward risk is not scarring but leakage: each generation that defects breaks the compounding. Gen-4 >> gen-1 inside the group, ~0 outside it
- **intergen_sign**: no flip while retention holds (compounds positively); flips to decay only if retention collapses - the sign is retention-gated, not scarring-gated
- **Verdict-LEAN**: **PARTIAL** - a real high-fertility engine, but a compounding-subpopulation object, not a state forcing; retention (not conversion) is its lever and it is not copyable at scale

### H333 - High-demand religion retention (compounding subpopulation)
- **Mechanism**: a strict, high-demand church sustains above-replacement fertility and grows by retaining its children - fertility × retention as a compounding object, not a policy
- **f** = { fN: -0.20, fPb: +0.15 } (subpopulation)
- **δ** = n/a as forcing (this is a growth object, not a lever); retention leakage is the risk
- **Side-effect cost**: { pluralism: -0.05 (voluntary membership) }
- **Analogue**: LDS TFR ~3.4 (2015) but declining toward the national mean as practice converges; needs ~70% child retention to self-replace ([IFS, religious-secular fertility divide](https://ifstudies.org/blog/americas-growing-religious-secular-fertility-divide); [Times & Seasons](https://timesandseasons.org/index.php/2024/09/is-the-church-replacing-itself-part-ii/))
- **cross_gen**: the purest compounding-vs-leakage object in the batch. Norm + intact-household transmission (fN-, fF+) compounds geometrically, but LDS data show the norm itself CONVERGING toward the secular mean each generation - so the forward signal is a race between fertility compounding and norm erosion. Gen-4 depends entirely on whether retention × norm-strength holds
- **intergen_sign**: soft flip via convergence - compounding at gen-1, decaying toward the mean by gen-3-4 as the distinctive norm dilutes; not a scarring reversal but a dilution one
- **Verdict-LEAN**: **PARTIAL** - a genuine compounding object with a demographic future, but converging downward and non-transferable; the model should carry it as a subpopulation, not a forcing

### H334 - Ban contraception
- **Mechanism**: prohibit contraceptives to force births by removing means (the pure-means arm of H319)
- **f** = { fPb: +0.05 } raw
- **δ** = 0.6 (private supply, demand persists, clandestine channels)
- **Side-effect cost**: { women's autonomy/rights: -0.6, welfare: -0.3 }
- **Analogue**: Iran/Quiverfull-internal; wherever tried at state scale the demand routes around it (mirrors abortion-ban evasion)
- **cross_gen**: same reversal family as H319/H328 - the few forced births are unwanted/mistimed, entering the integral with elevated fScar and low fF, plus the autonomy-norm damage transmits forward. Small gen-1, negative-leaning gen-4
- **intergen_sign**: FLIPS weakly - small positive at gen-1 → negative by gen-3-4 through the unwanted-child + eroded-autonomy-norm channels
- **Verdict-LEAN**: **REFUTED** - removing means without changing demand yields high δ and large autonomy cost; a classic coercion backfire that also reverses forward

### H335 - Pronatal media / glorify large families
- **Mechanism**: state or aligned-media propaganda glorifying large families to shift the norm
- **f** = { fN: -0.05 } raw → net ≈0 or negative under credibility discount
- **δ** = 0.4 (low-credibility messaging; reactance)
- **Side-effect cost**: { pluralism: -0.2, women's autonomy/rights: -0.15 }
- **Analogue**: campaign propaganda-backfire finding; overt pronatal messaging reads as manipulation and provokes reactance rather than adoption
- **cross_gen**: transmits a discredited, manipulative norm forward - the next cohort inherits reactance against the pronatal message rather than the message, so the fN signal is weakly negative and self-defeating across generations. No scarring, but no positive inheritance either
- **intergen_sign**: no positive flip - REFUTED now, REFUTED later; if anything the cynicism toward state pronatalism compounds
- **Verdict-LEAN**: **REFUTED** - the norm channel is real but weaponised messaging backfires; credibility, not volume, moves norms (contrast the un-purchasable Georgia signal)

### H336 - Shame / honour penalty on childlessness
- **Mechanism**: social stigma and honour penalties on the childless to coerce fertility via reputational cost
- **f** = { fRV: -0.08, fN: -0.05 } raw → net eroded by resentment
- **δ** = 0.4 (evasion, resentment, exit from the community imposing it)
- **Side-effect cost**: { women's autonomy/rights: -0.5, welfare: -0.2 (targets the involuntarily childless) }
- **Analogue**: the penalty family (USSR childlessness tax, honour-shame cultures) - penalties are coercion-adjacent and backfire per the campaign's defection screen
- **cross_gen**: stigma-driven births and stigma-shadowed households transmit resentment and constrained-mother env (fScar+) forward, and the coercive-shame norm the next cohort inherits breeds exit/reactance. A weak gen-1 signal decays into a negative gen-4
- **intergen_sign**: FLIPS - marginal-positive-at-most at gen-1 → negative by gen-3-4 via transmitted resentment and the discredited shame norm
- **Verdict-LEAN**: **REFUTED** - a penalty by another name; it flips negative on the defection screen, carries a heavy autonomy cost, and reverses across generations

### H337 - Total covenant-community bundle (Amish-style)
- **Mechanism**: a closed pronatalist subculture bundling natural fertility, early universal marriage, strong communal norms, and high retention - the existence proof that modern high-income fertility can be very high
- **f** = { fN: -0.30, fC: +0.20, fPb: +0.25, fTau: -0.15 } (WITHIN the bundle)
- **δ** = 0.15 (defection ≈15%, the second engine's leak)
- **Side-effect cost**: { pluralism: -0.05 (voluntary, enclaved), women's autonomy/rights: -0.3 }
- **Analogue**: Old Order Amish, completed fertility ~6-7, population doubles ~20 yr, retention ~85% ([Greksa-Korbin 2002, in-project digest])
- **cross_gen**: compounds strongly within the enclave - intact, high-commitment, low-conflict households (fF+, low fScar) plus a directly-inherited pronatal norm feed a healthy env forward, and the population doubles ~every 20 years. The forward risk is the ~15% defection leak, not scarring. Gen-4 >> gen-1 inside the bundle, ~0 transferable outside
- **intergen_sign**: no flip while retention holds - SUPPORTED-within-group and compounding; the opposite trajectory to the coercive cases
- **Verdict-LEAN**: **PARTIAL** - an existence proof, but it is a total subculture, not a separable lever; the transferable signal (norm+retention+early universal marriage as a BUNDLE) is weak and non-legislable

### H338 - Tech-right pronatalism (IVF + embryo selection)
- **Mechanism**: an elite subculture reframing high fertility as a rational/technological imperative, using IVF and embryo screening; norm channel among a small high-agency group
- **f** = { fN: -0.10, fPb: +0.08 } (elite subgroup)
- **δ** = 0.1 internally, non-transferable to the population
- **Side-effect cost**: { pluralism: -0.2 (eugenic-selection framing), women's autonomy/rights: -0.05 }
- **Analogue**: Collins family, Natal Conference (attendance doubled 2023→2025) ([NPR](https://www.npr.org/2025/04/25/nx-s1-5371718/pronatalist-birth-rate-musk-natal-conference); [CNN](https://www.cnn.com/2025/04/10/us/pronatalism-elon-musk-birth-rates-cec))
- **cross_gen**: within the elite subculture the pronatal-rationalist norm plus high-resource intact households transmit forward positively (fN-, fF+), so it compounds inside the group; but it is tiny, and the embryo-selection framing risks transmitting a stratifying/commodifying norm that erodes broader pluralism. Gen-4 > gen-1 within-group, negligible population-wide
- **intergen_sign**: no flip within-group (compounds); population-wide it stays negligible - a scale limitation, not a sign reversal
- **Verdict-LEAN**: **PARTIAL** - a real norm-shift inside a tiny elite subculture with an embryo-selection commodification cost; unproven at population scale and small by construction

---

## Interaction note

- **zeal × coercion**: the interaction is DESTRUCTIVE, not additive. Zeal attached to a penalty or ban (Gilead, Decree 770, Iran, shame-tax) raises the stake, and the campaign law is that weaponisation and defection track the stake - so higher zeal on a coercive lever makes δ WORSE, not the fertility better. Zeal and coercion should enter the model multiplicatively on the δ term, not additively on the fertility term.
- **devotion × δ**: the entire positive signal in this round lives where devotion is UN-BUYABLE, so δ≈0 (Georgia baptism, sacralised-motherhood norm, high-demand-religion retention). A sacred act that cannot be faked, purchased, or means-tested has no evasion channel - that is precisely why it clears where cash (mirage, gameable) and bans (evadable) fail. Model devotion as a δ-suppressor conditional on non-fungibility.
- **theocracy × security**: Norris-Inglehart predicts established religion is INERT under high existential security - so a theocratic establishment adds little forcing in a rich, secure society and instead pays the full pluralism+autonomy cost. Theocracy only "works" by manufacturing insecurity (the coercive route), which reactivates the coercion-backfire law. The interaction term between establishment-religion forcing and security should be strongly negative.
- **norm × penalty (the dividing line)**: the same norm channel (fN) SUPPORTS when re-priced voluntarily (H318, H331) and REFUTES when enforced by penalty (H336) or propaganda (H335). The sign of the norm lever is conditional on whether an option is removed. This is the single most important static finding of the round.
- **coercion × time (the path integral, the round's headline)**: coercive levers force gen-1 births into SCARRED childhood environments (high fScar, low fF), and `ot.CohortMemory` carries that damage forward 27-45 years into depressed marriageability and coupling - so coercion's true signature is a gen-1 boost that REVERSES by gen-3-4 (H314 Decree 770 is the calibration case; H327, H328, H330, H334, H336 share the family). Devotion and structural levers force births into HEALTHY, freely-chosen environments and transmit a pronatal norm forward, so they HOLD or COMPOUND (H318, H322, H331, H333, H337). The interaction is: coercion and the path integral multiply to a sign flip; devotion and the path integral multiply to persistence. No static ΔTFR can see either - that is why the round needed cohort tracking.

## Verdict tally (25)

- **SUPPORTED (3)**: H318 sacred third-child baptism, H322 Demeny/proxy voting, H331 sacralised-motherhood norm
- **PARTIAL (11)**: H315 Mutterkreuz medal, H316 childlessness-tax+medals, H320 Hungary tax-exemption, H323 child-linked pension, H324 state matchmaking, H328 abortion ban, H329 conscription exemption, H332 apocalyptic/Quiverfull, H333 high-demand-religion retention, H337 covenant-community bundle, H338 tech-right pronatalism
- **REFUTED (11)**: H314 Decree 770, H317 eugenic Graduate Mothers, H319 contraception rollback, H321 covenant marriage/no-fault ban, H325 bride-price revival, H326 polygamy, H327 lower marriage age, H330 Gilead, H334 contraception ban, H335 pronatal media, H336 shame/honour penalty

**Cross-generational (intergen_sign) reading**:

- **Reverse across generations (SUPPORTED/small-now → REFUTED-later, via fScar+/fF- into the path integral)**: H314 Decree 770 (the calibration case), H319, H327, H328, H330 Gilead (deepest), H334, H336 - and H316 weakly. Coercion wins gen-1 and loses gen-3-4
- **Compound or hold forward (SUPPORTED-now → SUPPORTED/stronger-later, via inherited pronatal norm + healthy fF/low fScar)**: H318 Georgia baptism, H322 Demeny voting, H323 child-linked pension (back-loaded), H331 sacralised-motherhood norm, H333 high-demand religion (retention-gated), H337 covenant-community (retention-gated), H338 within-group
- **Tempo/dilution decay (not a scarring reversal)**: H320 Hungary (tempo pull-forward reverses), H333 also carries norm dilution
- **No material flip (weak-and-stable)**: H315, H324, H329, H317/H325/H326/H335 stay REFUTED with worsening norm tails

**Net reading**: coercion and penalty REFUTE 11/11 of their pure cases statically, and a majority of them REVERSE cross-generationally - the forced cohort is scarred and transmits collapse forward. The only SUPPORTED levers are un-buyable, voluntary, and either sacred-norm or structural-commitment in kind, and these are precisely the ones that COMPOUND across generations. Zeal buys fertility only in the norm mode, never in the coercion mode; and the path integral sharpens the verdict from "coercion doesn't work" to "coercion can win the first generation and lose the third." That sign-flip - invisible to any static ΔTFR, now measurable via `ot.CohortMemory` - is the payoff of the round.
