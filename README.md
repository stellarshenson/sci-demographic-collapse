# sci-demographic-collapse

**Psychohistory for the one thing that kills civilizations quietly: a people that stops replacing itself.**

[![Python 3.13](https://img.shields.io/badge/Python-3.13-3776AB.svg?logo=python&logoColor=white)](https://www.python.org/)
[![GPU](https://img.shields.io/badge/runs%20on-torch%20%2F%20CUDA-EE4C2C.svg?logo=pytorch&logoColor=white)](https://pytorch.org/)
[![Hypotheses](https://img.shields.io/badge/hypotheses-188-2ea44f.svg)](docs/experiments/demographic-collapse-experiments.md)
[![Rounds](https://img.shields.io/badge/rounds-E1--E19-f0883e.svg)](docs/experiments/demographic-collapse-experiments.md)
[![Notebooks](https://img.shields.io/badge/notebooks-14-8957e5.svg)](notebooks/)
[![Seldon manifold](https://img.shields.io/badge/Seldon%20manifold-TFR%201.5-critical.svg)](docs/story.md)
[![psychohistory](https://img.shields.io/badge/psychohistory-descriptive%2C%20not%20prophetic-lightgrey.svg)](docs/story.md)

Asimov's Hari Seldon couldn't predict one person. He could predict a billion. Read the aggregate and the fall is already written - generations before anyone feels it.

That's the trick, pointed at fertility instead of a galaxy. Ignore the individual, read the flow, find the line that splits the peoples who recover from the peoples who don't. One rule the fiction skipped and this keeps: **it is descriptive, not prophetic.** It sizes the forces and puts each country on the map. It does not hand you a date of death.

## Two valleys, one ridge

Every nation is a ball on a landscape. One valley recovers. The other is a pit - absorbing, and the model means the word: get deep enough and every path points down. The ridge between them is the **Seldon manifold** - a watershed. A hand's breadth to one side runs to the sea; the other side runs to the desert.

> [!WARNING]
> Falling is the default. Two of every three configurations drain to collapse. You don't have to be unlucky - the floor is tilted. Recovery is the thing you have to *hold*.

Fit to nothing, the ridge lands at **TFR ≈ 1.5** - the exact low-fertility trap Lutz, Skirbekk and Testa argued from data years earlier. A landscape invented from first principles put its watershed on someone else's measured cliff. Replacement is 2.1. The ridge is 1.5. **Six tenths of a child is the whole margin.**

- **US - 1.66** - safe side, barely, on a single strut
- **Europe - 1.47** - standing on the knife
- **China - 1.20** - over it, top-heavy, no one big enough to backfill from
- **Korea - 0.72** - off the map, in country no modern society has ever walked

## 188 hypotheses. Here is what survived.

- **Coupling is the keystone.** Kids come from couples, not people. Pull that stone and the arch drops - it does not sag, it drops.
- **Tempo steals quietly.** Push first birth from 21 to 31 and the window shuts on some children for good. A delay is not a no. Arithmetic does not care about intent.
- **The bust was quantum, not momentum.** People wanted fewer - not a mechanical echo you can wait out.
- **Age structure is a standing tree** - cut at the base, still upright on its own mass. Korea's 2050 was cast in the 1990s. Not up for debate.
- **Migration is the only fast hand on the wheel.** A migrant lands grown, straight into the hollow middle of the pyramid. It is the entire US strut.
- **Cash is a mirage. Coercion backfires.** The durable levers are coupling and structure, delivered to everyone. Run it four generations and you can hear which trees have begun to lean.

## The build (the fun part)

- **Leslie cohort-component core** - single-year ages, births / deaths / Rogers-Castro migration, momentum and eigenstructure. `src/sci_demographic_collapse/coremodel.py`, torch on GPU.
- **Bongaarts-Feeney** tempo-quantum split - *when* births happen vs *how many* complete. Get these confused and every signal is a mirage.
- **Free-energy calibration** in Pyro. The ELBO collapsed the posterior (it ignored the latent and drew a straight line). Swapped in an **exact-1D-Wasserstein** objective and the gap went 0.26 → 0.018, mutual-information usage 0.07 → 0.96, forecast coverage 50% → 100%.
- **The nine-state Seldon ODE** - bistable coupling × childlessness. The separatrix put *itself* on TFR-1.5; nobody placed it there.
- **Coupled behavioural-ODE × Leslie simulator** (round E19) - the model becomes the judge. Every intervention run four generations. Tempo levers turn out to be mirages that revert. Quantum levers are gated by coupling. Only the strongest coupling levers escape the trap. Timing decides.

## The trail

- **14 notebooks** (`notebooks/01…14`) - the stylized ODE, age-structured calibration, crisis stress-tests, the intervention campaign, the dynamical simulator
- **The evidence log** - all 188 hypotheses, E1-E19, in [`docs/experiments/demographic-collapse-experiments.md`](docs/experiments/demographic-collapse-experiments.md)
- **The distilled design** - [`docs/demographic-collapse-sota.md`](docs/demographic-collapse-sota.md)
- **The star-ranked intervention guide** - [`docs/interventions.md`](docs/interventions.md)
- **The plain-language story** - [`docs/story.md`](docs/story.md)
- **30+ open-access papers** with structured digests in `references/papers/`

> [!NOTE]
> Learning project. The behavioural models are stylized and qualitatively calibrated - they rank mechanisms and place peoples on a landscape. They forecast nobody's future, and they are honest about it.

## Run it

```bash
make install     # uv environment + package
make test        # tests
```

## Makefile targets

- `make install` - create environment and install package
- `make test` - run tests
- `make lint` / `make format` - check / fix style with ruff
- `make build` - build the wheel
- `make clean` - remove caches and build artifacts
- `make .env` / `make .env.enc` - decrypt / encrypt secrets
- `make help` - all targets

## Project organization

```
├── Makefile                          <- install / test / lint / format
├── pyproject.toml                    <- config and dependencies (uv)
├── data/raw/unwpp                    <- UN WPP 2024 schedules (immutable) + World Bank / Eurostat / OWID
├── notebooks                         <- 01…14, the campaign end to end
├── src/sci_demographic_collapse
│   └── coremodel.py                  <- the Leslie core (imported by notebooks 4-14)
├── docs
│   ├── story.md                      <- the Seldon-Region narrative
│   ├── demographic-collapse-sota.md  <- the distilled design
│   ├── interventions.md              <- star-ranked intervention guide
│   └── experiments/…                 <- the 188-hypothesis experiments log
├── reports/figures                   <- every executed figure (nb1…nb14)
└── references/papers                 <- the research library ([paper] + [paper digest] pairs)
```

---

*Low fertility alone does not decide the fall. The age structure decides the timing and the depth, and migration is the only fast hand on the wheel. The peoples who hold the ridge are not the ones with the most children this year - they are the ones whose pyramid still has a base to buy time, and who keep drawing the young inward while that time lasts.*
