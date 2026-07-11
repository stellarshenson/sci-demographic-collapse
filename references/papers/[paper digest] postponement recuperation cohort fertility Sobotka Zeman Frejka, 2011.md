# [Paper digest] Postponement and Recuperation in Cohort Fertility

**Authors**: Tomáš Sobotka, Kryštof Zeman, Ron Lesthaeghe, Tomáš Frejka<br>
**Year**: 2011  **Venue**: European Demographic Research Paper 2011-2, Vienna Institute of Demography (VID), OA<br>
**Original (link)**: [https://www.oeaw.ac.at/fileadmin/subsites/Institute/VID/PDF/Publications/EDRP/edrp_2011_02.pdf](https://www.oeaw.ac.at/fileadmin/subsites/Institute/VID/PDF/Publications/EDRP/edrp_2011_02.pdf)<br>
**Local PDF**: `[paper] postponement recuperation cohort fertility Sobotka Zeman Frejka, 2011.pdf` (OA, 86 pp)<br>
**Used in**: E46 second-order tempo anchor (mass/damping of the tau damped-oscillator - recuperation fraction and recovery timescale)

## Summary

Defines and measures the two halves of the fertility postponement transition in a cohort frame: **postponement** (fertility decline at young ages, before a trough age m) and **recuperation** (the partial recovery of those births after the trough, up to the end of reproductive life). The central quantitative device is the **Recuperation Index (RI)** - the share of the young-age deficit that is later made up. The paper is the empirical spine for a second-order tempo channel because it supplies both the recuperation FRACTION (how much comes back) and the within-cohort TIMESCALE (over how many years of a woman's life it comes back).

## Parameters for the model

- **Definitions** (their Figure 1): `P_c` = cumulative fertility decline until the trough age `m` (postponement); `R_c` = absolute recuperation between trough age and end of reproduction; final difference `FD_c = P_c + R_c` (the permanent, non-recovered loss). **Recuperation Index** `RI_c = R_c / (-P_c)`, expressed 0 (no recovery) to 100% (full) or above 100% ('overcompensation'). Equivalently `FD_c = P_c·(1 - RI_c)`
- **Worked example (their schematic)**: trough at age `m = 25`; `P_c = -0.59`, `R_c = +0.52`, so `FD_c = -0.07` and `RI = 0.52/0.59 = 0.88` (88% recovered)
- **Timescale (within cohort)**: postponement accumulates below age ~25-27; recuperation is measured cumulatively by **age 36** (partial 'preview') and **age 40-42** (near-complete). So the trough-to-recovery span is roughly **age 25 -> age 40, i.e. ~15 years** of a cohort's reproductive life
- **Total-order recuperation, 1960s cohorts**: a 'healthy' recuperation is **~70%**; **Spain ~37%**, East Germany and Austria below one half; the **United States overcompensates (RI > 1)** for cohorts born after 1962
- **By birth order (1960s cohorts)**: first births recuperate **>67% in every country studied**; second births **~65%** in Austria, Czech Republic, Netherlands, Switzerland (low in Spain); third-and-higher births show **no measurable recovery in Austria and Spain**, ~30% in Switzerland, and US overcompensation with **RI > 2** in the 1965 cohort
- **Benchmark cohort CTFR (first births, all near 0.88-0.92)**: Netherlands BC1945 CTFR1 = 0.883; benchmark total CTFR ~1.8-1.95 (Austria 1.84, Germany 1.78, Czech 1.90, Netherlands 1.98, Spain 1.87, Sweden 1.95)
- **Projected completed cohort fertility, early-1980s cohorts**: wide spread from **1.3 (lowest scenario, Spain)** to **1.9 (highest, Czech Republic)** - recuperation strength, not the depth of postponement, drives the cross-country gap
- **RI stability caveat**: RI is only informative alongside the absolute trough decline `P_c`; when `P_c` is small (e.g. Switzerland) the index fluctuates wildly and can be unstable

## Caveats

The index is a cohort accounting identity, not a fitted dynamical law - it says how much came back and by what age, but not the trajectory shape (single swing vs damped oscillation), which the aggregate data rarely resolve. RI values above 1 (US) are genuine over-recovery and cannot arise from a passive damping process - they require a real quantum/period push. Order-specific results depend heavily on birth-order data quality. For the model: read `RI ~ 0.65-0.70` as the central recuperation fraction (bracket 0.37 Spain to >1 US), and the trough-to-recovery span as **~15 years** in the cohort frame, to be reconciled with the shorter ~10-year period-level recovery episode documented in Bongaarts & Sobotka (2012).
