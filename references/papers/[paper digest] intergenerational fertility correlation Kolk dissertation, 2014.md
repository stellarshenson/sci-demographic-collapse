# [Paper digest] Correlations in fertility across generations: can low fertility persist?

**Authors**: Martin Kolk, Daniel Cownden, Magnus Enquist (Centre for the Study of Cultural Evolution, Stockholm)<br>
**Year**: 2014  **Venue**: Proceedings of the Royal Society B 281(1779):20132561 (article paywalled; model reproduced in Kolk's PhD dissertation, this copy)<br>
**Original (article)**: [https://doi.org/10.1098/rspb.2013.2561](https://doi.org/10.1098/rspb.2013.2561) (Royal Society, Cloudflare-blocked to bots)<br>
**Open source (download)**: [http://www.diva-portal.org/smash/get/diva2:742300/FULLTEXT02.pdf](http://www.diva-portal.org/smash/get/diva2:742300/FULLTEXT02.pdf) (DiVA, Stockholm University - dissertation containing Study 3)<br>
**Local PDF**: `[paper] intergenerational fertility correlation Kolk dissertation, 2014.pdf` (dissertation kappa)<br>
**Model class**: deterministic cultural-evolutionary recursion (two-type, parental + social influence)<br>
**Downloaded**: yes (dissertation; the RSPB article itself is ABSTRACT/paywalled)

## The transmission model

A deterministic cultural-transmission model (structurally like population genetics, but the "inheritance" is cultural) of how a parent-child fertility correlation evolves the population fertility distribution over generations. Family-size "lifestyle" is acquired from a mix of **parental influence** (vertical) and **social influence** (oblique/horizontal). Because higher-fertility parents transmit a higher-fertility lifestyle to more children, differential fertility makes the high-fertility lifestyle compound in frequency.

- **Differential fertility**: high-fertility types leave more offspring, so their trait is over-represented in the next generation's pool of learners - the same fertility-weighting that Arenberg (2021) later fused into a matrix `A = P∘F`
- **Central result**: with any positive intergenerational transmission, the twentieth-century decline **reverses** and fertility rises over the long run - population is not self-stabilising at low fertility
- **The condition for low fertility to persist (our leak term)**: sustained low fertility requires that **new low-fertility lifestyles keep being introduced into the population at a rapid pace** - a continual oblique influx of novelty at the edge that outruns the pronatal compounding. Absent that influx, transmission drags fertility back up
- Arenberg et al. (2021) is the explicit successor that adds imperfect fidelity `p` and shows `p·F > 1` can fail

## How differential fertility enters

Via the fertility-weighted composition of each new generation's learning pool: parents transmit in proportion to how many children they have. This is the deterministic precedent for our fertility-weighted vertical mixing.

## Portability to our ensemble

Kolk supplies the mechanism (fertility-weighted vertical + social transmission of a family-size lifestyle) and, crucially, the **edge-leak intuition**: our modular bearer needs a leak/novelty-influx term or it will manufacture an unrealistic pronatal rebound. Arenberg's matrix is the discretised, Leslie-ready form of this same process.

## Tags

`intergenerational-transmission` `cultural-evolution` `two-type` `fertility-weighted` `low-fertility-persistence` `edge-leak` `rebound` `deterministic-recursion` `precursor-to-Arenberg`
