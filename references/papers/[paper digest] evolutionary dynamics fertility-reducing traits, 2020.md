# [Paper digest] Evolutionary dynamics of culturally transmitted, fertility-reducing traits

**Authors**: Dominik Wodarz, Shaun Stipp, David Hirshleifer, Natalia L. Komarova<br>
**Year**: 2020  **Venue**: Proceedings of the Royal Society B 287:20192468 (bioRxiv preprint 10.1101/619882, this copy)<br>
**Original (download)**: [https://www.biorxiv.org/content/10.1101/619882v2.full.pdf](https://www.biorxiv.org/content/10.1101/619882v2.full.pdf) (open, CC-BY-NC-ND)<br>
**Local PDF**: `[paper] evolutionary dynamics fertility-reducing traits, 2020.pdf` (in this folder)<br>
**Model class**: deterministic ODE (non-spatial, asexual two-type), plus age-structured and continuous-trait variants<br>
**Downloaded**: yes (full text)

## The transmission operator (this is the anchor form)

Two cultural types: fast reproducers `x_f` and slow reproducers `x_s`. The core deterministic model is a pair of ODEs where a logistic growth term, a common death term, and a **frequency-dependent transmission ("infection-like") term** couple the two:

```
ẋ_f = r_f x_f W − d x_f − β x_f x_s / K
ẋ_s = r_s x_s W − d x_s + β x_f x_s / K
W = 1 − (x_f + x_s)/K        (logistic, K = carrying capacity)
```

- `r_f > r_s`: differential fertility enters directly as each type's own linear **reproduction rate** - this is the fertility weight
- `β = β_f − β_s > 0`: net **conversion (imitation) rate** from fast→slow. Switching is proportional to the abundance of the opposite type (mass-action, exactly the form of an epidemic infection term), so it is oblique/horizontal transmission, not vertical
- `d`: common mortality. The paper's central result is that **low `d` slows population turnover, which lets the transmission advantage `β` of slow reproducers out-race their reproductive disadvantage `r_s < r_f`** - mortality decline drives fertility decline via cultural selection
- Bias assumption: slow reproducers carry higher social influence (they channel resources into wealth/status), motivating `β_f > β_s`
- Extensions: (i) an **age-structured** version replacing fast/slow with age-specific reproduction; (ii) a **continuous-trait** version where the reproduction rate evolves by imitation with copying error `G` (~2%), which can push mean fertility below replacement

## How differential fertility enters

Multiplicatively and per-type: each trait grows at its own `r_i · W`. Selection is the race between the fertility gap (`r_f − r_s`, favouring fast) and the transmission gap (`β`, favouring slow), refereed by turnover rate `d`. Trait frequency is the compounding state variable.

## Portability to our ensemble

Direct: the mass-action `± β x_f x_s / K` term is a ready-made oblique-transmission operator, and differential fertility as a per-type multiplier maps onto our TFR-weighted vertical mixing; the mortality-gated turnover result argues the bearer must be coupled to the Leslie mortality schedule, not just to fertility.

## Tags

`cultural-selection` `ODE` `two-type` `differential-fertility` `oblique-transmission` `mass-action` `mortality-turnover` `continuous-trait-imitation` `demographic-transition`
