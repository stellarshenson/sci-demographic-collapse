"""Single source-of-truth intervention catalogue for the demographic-collapse campaign.

Every hypothesis lever harvested from the E14-E18 catalogue tables (as re-judged dynamically in
E19/nb14) and the E25-E33 batches (nb19-nb27), expressed on the one extensible interface of the
coupled emergent model: a 9-channel forcing over
(fS, fC, fPb, fTau, fRV, fN, fq, fF, fScar).

Conventions
- each entry: {"id", "name", "batch", "f", "recorded_verdict"}
- "f" holds EFFECTIVE channel amplitudes at full ramp: the source batches' per-lever magnitude
  `mag` and defection leakage `(1 - delta)` are folded in, so `force_of(entry["f"])` reproduces
  the batch forcing under the standard 10-year ramp
- durability/erosion envelopes (`durable=False` levers) and custom ramp durations are NOT
  carried; every lever is rendered durable here - consult the source batch for fade behaviour
- E14-E18 rows use the E19 channel-class mapping at full push (coupling fS=1.2e, fC=0.5e;
  quantum/cash fPb=3e; tempo fTau=-15e; backfire fS=-e-0.6b, fRV=+0.5b); migration levers act
  through the Leslie migration multiplier, not a channel forcing, so their "f" is empty
- "recorded_verdict" is the batch's recorded verdict: SUPPORTED/PARTIAL/REFUTED for E25-E33,
  the E19 dynamical class (e.g. "coupling escape", "tempo mirage") for E14-E18
- calibrated constants recovered from executed notebooks: polygyny parity arm mag=0.666 (nb21),
  unit-parity magnitude K=0.366 (nb22), durable-therapy magnitude fq=0.084 (nb24)

Not reconstructable as static channel vectors (verdicts live in reports/*_verdicts.json):
E28 H219/H222-H226 (sweep and interaction syntheses), E29 H227-H246 (population-framework
mechanism batch), E30 H249/H251/H255-H258/H260 (core-property claims), E32 H285 (interaction
finding), E33 H300-H302/H306 (compounding sub-populations).
"""

CHANNELS = ("fS", "fC", "fPb", "fTau", "fRV", "fN", "fq", "fF", "fScar")

CATALOGUE = [
    {
        "id": "IV1",
        "name": "Universal subsidized childcare",
        "batch": "E14",
        "f": {"fS": 0.3, "fC": 0.125},
        "recorded_verdict": "coupling escape",
    },
    {
        "id": "IV2",
        "name": "Child allowance / cash transfers",
        "batch": "E14",
        "f": {"fPb": 0.51},
        "recorded_verdict": "tempo mirage",
    },
    {
        "id": "IV3",
        "name": "Baby bonus / birth grant (one-off)",
        "batch": "E14",
        "f": {"fPb": 0.24},
        "recorded_verdict": "weak / stall",
    },
    {
        "id": "IV4",
        "name": "Paid parental leave (incl. paternity)",
        "batch": "E14",
        "f": {"fS": 0.12, "fC": 0.05},
        "recorded_verdict": "durable bend",
    },
    {
        "id": "IV5",
        "name": "Family housing support / affordability",
        "batch": "E14",
        "f": {"fS": 0.18, "fC": 0.075},
        "recorded_verdict": "durable bend",
    },
    {
        "id": "IV6",
        "name": "Subsidized assisted reproduction (IVF)",
        "batch": "E14",
        "f": {"fTau": -0.75},
        "recorded_verdict": "weak / stall",
    },
    {
        "id": "IV7",
        "name": "Work-family reconciliation (flexible hrs)",
        "batch": "E14",
        "f": {"fS": 0.12, "fC": 0.05},
        "recorded_verdict": "durable bend",
    },
    {
        "id": "IV8",
        "name": "Pro-natal / replacement migration",
        "batch": "E14",
        "f": {},
        "recorded_verdict": "one-time bridge",
    },
    {
        "id": "IV9",
        "name": "Gender-equity (domestic-labour equalize)",
        "batch": "E14",
        "f": {"fS": 0.24, "fC": 0.1},
        "recorded_verdict": "durable bend",
    },
    {
        "id": "IV10",
        "name": "Earlier union formation / relationship support",
        "batch": "E14",
        "f": {"fS": 0.12, "fC": 0.05},
        "recorded_verdict": "durable bend",
    },
    {
        "id": "IV11",
        "name": "De-stigmatize non-marital births",
        "batch": "E14",
        "f": {"fS": 0.12, "fC": 0.05},
        "recorded_verdict": "durable bend",
    },
    {
        "id": "IV12",
        "name": "Reduce intensive-parenting / child-cost norm",
        "batch": "E14",
        "f": {"fPb": 0.36},
        "recorded_verdict": "weak / stall",
    },
    {
        "id": "IV13",
        "name": "Attention-economy / dating-app regulation",
        "batch": "E14",
        "f": {"fS": 0.096, "fC": 0.04},
        "recorded_verdict": "durable bend",
    },
    {
        "id": "IV14",
        "name": "Economic security / youth-precarity reduction",
        "batch": "E14",
        "f": {"fS": 0.18, "fC": 0.075},
        "recorded_verdict": "durable bend",
    },
    {
        "id": "IV1",
        "name": "Universal childcare",
        "batch": "E15",
        "f": {"fS": 0.3, "fC": 0.125},
        "recorded_verdict": "coupling escape",
    },
    {
        "id": "IV9",
        "name": "Gender-equity (domestic)",
        "batch": "E15",
        "f": {"fS": 0.24, "fC": 0.1},
        "recorded_verdict": "durable bend",
    },
    {
        "id": "IV5",
        "name": "Family housing support",
        "batch": "E15",
        "f": {"fS": 0.18, "fC": 0.075},
        "recorded_verdict": "durable bend",
    },
    {
        "id": "IV14",
        "name": "Youth-precarity / job guar.",
        "batch": "E15",
        "f": {"fS": 0.18, "fC": 0.075},
        "recorded_verdict": "durable bend",
    },
    {
        "id": "IV4",
        "name": "Paid parental leave (long)",
        "batch": "E15",
        "f": {"fS": 0.12, "fC": 0.05},
        "recorded_verdict": "durable bend",
    },
    {
        "id": "IV7",
        "name": "Work-family flexibility",
        "batch": "E15",
        "f": {"fS": 0.12, "fC": 0.05},
        "recorded_verdict": "durable bend",
    },
    {
        "id": "IV2",
        "name": "Child allowance (cash)",
        "batch": "E15",
        "f": {"fPb": 0.3},
        "recorded_verdict": "weak / stall",
    },
    {
        "id": "IV12",
        "name": "Reduce child-cost norm",
        "batch": "E15",
        "f": {"fPb": 0.36},
        "recorded_verdict": "durable bend",
    },
    {
        "id": "IV6",
        "name": "Baby bonus (one-off)",
        "batch": "E15",
        "f": {"fPb": 0.18},
        "recorded_verdict": "weak / stall",
    },
    {
        "id": "IV3",
        "name": "IVF / ART subsidy",
        "batch": "E15",
        "f": {"fTau": -0.75},
        "recorded_verdict": "weak / stall",
    },
    {
        "id": "IV10",
        "name": "Earlier union formation",
        "batch": "E15",
        "f": {"fS": 0.18, "fC": 0.075},
        "recorded_verdict": "durable bend",
    },
    {
        "id": "IV11",
        "name": "Longer / stable unions",
        "batch": "E15",
        "f": {"fS": 0.18, "fC": 0.075},
        "recorded_verdict": "durable bend",
    },
    {
        "id": "IV13",
        "name": "State partner-market (camp)",
        "batch": "E15",
        "f": {"fS": 0.24, "fC": 0.1},
        "recorded_verdict": "durable bend",
    },
    {
        "id": "IV8",
        "name": "Replacement migration",
        "batch": "E15",
        "f": {},
        "recorded_verdict": "one-time bridge",
    },
    {
        "id": "H101",
        "name": "Tutoring ban",
        "batch": "E16",
        "f": {"fS": -0.3105, "fRV": 0.2},
        "recorded_verdict": "backfire",
    },
    {
        "id": "H102",
        "name": "Lottery-band admission",
        "batch": "E16",
        "f": {"fPb": 0.4657},
        "recorded_verdict": "weak / stall",
    },
    {
        "id": "H103",
        "name": "Multi-dim un-gameable admission",
        "batch": "E16",
        "f": {"fPb": 0.1188},
        "recorded_verdict": "weak / stall",
    },
    {
        "id": "H104",
        "name": "Positional cap (Frank)",
        "batch": "E16",
        "f": {"fPb": 0.4239},
        "recorded_verdict": "durable bend",
    },
    {
        "id": "H105",
        "name": "Inequality compression",
        "batch": "E16",
        "f": {"fS": 0.2881, "fC": 0.12},
        "recorded_verdict": "coupling escape",
    },
    {
        "id": "H106",
        "name": "Estate / inheritance tax",
        "batch": "E16",
        "f": {"fPb": 0.118},
        "recorded_verdict": "weak / stall",
    },
    {
        "id": "H107",
        "name": "Progressive wealth cap",
        "batch": "E16",
        "f": {"fS": -0.2447, "fRV": 0.2},
        "recorded_verdict": "backfire",
    },
    {
        "id": "H108",
        "name": "Tax childlessness",
        "batch": "E16",
        "f": {"fPb": 0.1575},
        "recorded_verdict": "weak / stall",
    },
    {
        "id": "H109",
        "name": "Remove DINK tax advantage",
        "batch": "E16",
        "f": {"fPb": 0.2601},
        "recorded_verdict": "weak / stall",
    },
    {
        "id": "H110",
        "name": "Universal motherhood-penalty removal",
        "batch": "E16",
        "f": {"fS": 0.2166, "fC": 0.0902},
        "recorded_verdict": "durable bend",
    },
    {
        "id": "H111",
        "name": "Israel default + universal IVF",
        "batch": "E16",
        "f": {"fS": 0.1355, "fC": 0.0565},
        "recorded_verdict": "durable bend",
    },
    {
        "id": "H112",
        "name": "High-fertility subculture",
        "batch": "E16",
        "f": {"fS": 0.0216, "fC": 0.009},
        "recorded_verdict": "weak / stall",
    },
    {
        "id": "H113",
        "name": "Hungary cash package",
        "batch": "E16",
        "f": {"fPb": 0.1215},
        "recorded_verdict": "weak / stall",
    },
    {
        "id": "H114",
        "name": "Housing supply / zoning",
        "batch": "E16",
        "f": {"fS": 0.13, "fC": 0.0541},
        "recorded_verdict": "durable bend",
    },
    {
        "id": "H115",
        "name": "Student-debt relief / free tertiary",
        "batch": "E16",
        "f": {"fS": 0.1016, "fC": 0.0423},
        "recorded_verdict": "durable bend",
    },
    {
        "id": "H116",
        "name": "Peer-led parent archetype",
        "batch": "E16",
        "f": {"fPb": 0.0607},
        "recorded_verdict": "weak / stall",
    },
    {
        "id": "H117",
        "name": "Top-down pronatal propaganda",
        "batch": "E16",
        "f": {"fS": -0.3112, "fRV": 0.2},
        "recorded_verdict": "backfire",
    },
    {
        "id": "H118",
        "name": "Remove the parenthood happiness penalty",
        "batch": "E16",
        "f": {"fS": 0.0972, "fC": 0.0405},
        "recorded_verdict": "durable bend",
    },
    {
        "id": "H119",
        "name": "Decouple status from job-title/hours",
        "batch": "E16",
        "f": {"fS": 0.0706, "fC": 0.0294},
        "recorded_verdict": "durable bend",
    },
    {
        "id": "H120",
        "name": "Marriage-first exhortation",
        "batch": "E16",
        "f": {"fS": -0.2452, "fRV": 0.2},
        "recorded_verdict": "backfire",
    },
    {
        "id": "H121",
        "name": "Use-it-or-lose-it default",
        "batch": "E16",
        "f": {"fS": 0.1355, "fC": 0.0565},
        "recorded_verdict": "durable bend",
    },
    {
        "id": "H123",
        "name": "Recycle the defection",
        "batch": "E16",
        "f": {"fPb": 0.0153},
        "recorded_verdict": "weak / stall",
    },
    {
        "id": "E17-H126",
        "name": "coupling economies-of-scale (financial channel)",
        "batch": "E17",
        "f": {"fS": 0.0427, "fC": 0.0178},
        "recorded_verdict": "durable bend",
    },
    {
        "id": "E17-H127",
        "name": "single-parent precarity",
        "batch": "E17",
        "f": {},
        "recorded_verdict": "weak / stall",
    },
    {
        "id": "E17-H128",
        "name": "solo-parent support (benefit-cliff)",
        "batch": "E17",
        "f": {"fPb": 0.2052},
        "recorded_verdict": "weak / stall",
    },
    {
        "id": "E17-H129",
        "name": "reward union duration (de-risk vs lock-in)",
        "batch": "E17",
        "f": {"fS": 0.0441, "fC": 0.0184},
        "recorded_verdict": "durable bend",
    },
    {
        "id": "E17-H130",
        "name": "duration bonuses / anniversary holiday / longevity medals",
        "batch": "E17",
        "f": {},
        "recorded_verdict": "weak / stall",
    },
    {
        "id": "E17-H131",
        "name": "lock-in / covenant marriage / adultery penalty",
        "batch": "E17",
        "f": {"fS": -0.2767, "fRV": 0.2},
        "recorded_verdict": "backfire",
    },
    {
        "id": "E17-H132",
        "name": "school finance + communication education",
        "batch": "E17",
        "f": {"fPb": 0.243},
        "recorded_verdict": "weak / stall",
    },
    {
        "id": "E17-H133",
        "name": "infidelity norm / stigma (soft, non-legal)",
        "batch": "E17",
        "f": {"fPb": 0.0074},
        "recorded_verdict": "weak / stall",
    },
    {
        "id": "E17-H134",
        "name": "pornography ban as a fertility lever",
        "batch": "E17",
        "f": {"fS": -0.248, "fRV": 0.2},
        "recorded_verdict": "backfire",
    },
    {
        "id": "E17-H135",
        "name": "Amish / enclosed-community fertility",
        "batch": "E17",
        "f": {},
        "recorded_verdict": "weak / stall",
    },
    {
        "id": "E17-H136",
        "name": "universal vs means-tested",
        "batch": "E17",
        "f": {"fPb": 0.2925},
        "recorded_verdict": "weak / stall",
    },
    {
        "id": "E17-H137",
        "name": "benefit form (cash/in-kind/time)",
        "batch": "E17",
        "f": {"fS": 0.27, "fC": 0.1125},
        "recorded_verdict": "durable bend",
    },
    {
        "id": "E17-H138",
        "name": "credible permanence",
        "batch": "E17",
        "f": {"fPb": 0.5577},
        "recorded_verdict": "tempo mirage",
    },
    {
        "id": "E17-H139",
        "name": "geographic scale",
        "batch": "E17",
        "f": {"fPb": 0.108},
        "recorded_verdict": "weak / stall",
    },
    {
        "id": "E17-H140",
        "name": "who pays (state vs employer mandate)",
        "batch": "E17",
        "f": {"fPb": 0.45},
        "recorded_verdict": "weak / stall",
    },
    {
        "id": "E17-H141",
        "name": "surrogate-carrier market (conditioned class)",
        "batch": "E17",
        "f": {"fPb": 0.0252},
        "recorded_verdict": "weak / stall",
    },
    {
        "id": "E17-H142",
        "name": "optimum-type taxonomy",
        "batch": "E17",
        "f": {},
        "recorded_verdict": "weak / stall",
    },
    {
        "id": "E17-H143",
        "name": "robust vs fragile bundle (Seldon manifold)",
        "batch": "E17",
        "f": {"fPb": 1.4127},
        "recorded_verdict": "tempo mirage",
    },
    {
        "id": "E18-H144",
        "name": "compress x lottery-band",
        "batch": "E18",
        "f": {"fS": 0.3281, "fC": 0.1367},
        "recorded_verdict": "coupling escape",
    },
    {
        "id": "E18-H145",
        "name": "in-kind x permanence",
        "batch": "E18",
        "f": {"fS": 0.3901, "fC": 0.1626},
        "recorded_verdict": "coupling escape",
    },
    {
        "id": "E18-H146",
        "name": "universal+statefund x de-risk",
        "batch": "E18",
        "f": {"fS": 0.36, "fC": 0.15},
        "recorded_verdict": "coupling escape",
    },
    {
        "id": "E18-H147",
        "name": "coupling-afford x housing-supply",
        "batch": "E18",
        "f": {"fS": 0.1741, "fC": 0.0726},
        "recorded_verdict": "durable bend",
    },
    {
        "id": "E18-H148",
        "name": "de-risk x school-ed x peer",
        "batch": "E18",
        "f": {"fS": 0.168, "fC": 0.07},
        "recorded_verdict": "durable bend",
    },
    {
        "id": "E18-H149",
        "name": "IVF-default x egg-banking x permanence",
        "batch": "E18",
        "f": {"fS": 0.18, "fC": 0.075},
        "recorded_verdict": "durable bend",
    },
    {
        "id": "E18-H150",
        "name": "gender-eq x father-quota x short-hrs",
        "batch": "E18",
        "f": {"fS": 0.18, "fC": 0.075},
        "recorded_verdict": "durable bend",
    },
    {
        "id": "E18-H151",
        "name": "inequality-compression x fertility-linked-pension",
        "batch": "E18",
        "f": {"fS": 0.3, "fC": 0.125},
        "recorded_verdict": "coupling escape",
    },
    {
        "id": "E18-H152",
        "name": "pension-fertility externality",
        "batch": "E18",
        "f": {"fPb": 0.0942},
        "recorded_verdict": "weak / stall",
    },
    {
        "id": "E18-H160",
        "name": "UBI vs child-conditional transfer",
        "batch": "E18",
        "f": {"fPb": 0.39},
        "recorded_verdict": "weak / stall",
    },
    {
        "id": "E18-H163",
        "name": "employment-precarity formation-brake",
        "batch": "E18",
        "f": {"fS": 0.1157, "fC": 0.0482},
        "recorded_verdict": "durable bend",
    },
    {
        "id": "E18-H153",
        "name": "egg-freezing option-value trap",
        "batch": "E18",
        "f": {"fS": -0.3028, "fRV": 0.2},
        "recorded_verdict": "backfire",
    },
    {
        "id": "E18-H154",
        "name": "fecundity floor (sub-fecundity)",
        "batch": "E18",
        "f": {"fPb": 0.4131},
        "recorded_verdict": "weak / stall",
    },
    {
        "id": "E18-H155",
        "name": "hypergamy marriage-squeeze",
        "batch": "E18",
        "f": {"fS": 0.1357, "fC": 0.0566},
        "recorded_verdict": "durable bend",
    },
    {
        "id": "E18-H156",
        "name": "one-child-policy hysteresis",
        "batch": "E18",
        "f": {"fPb": 0.0519},
        "recorded_verdict": "weak / stall",
    },
    {
        "id": "E18-H157",
        "name": "grandmother hypothesis (kin proximity)",
        "batch": "E18",
        "f": {"fS": 0.1157, "fC": 0.0482},
        "recorded_verdict": "durable bend",
    },
    {
        "id": "E18-H158",
        "name": "climate/expectations birth-strike",
        "batch": "E18",
        "f": {"fS": -0.2799, "fRV": 0.2},
        "recorded_verdict": "backfire",
    },
    {
        "id": "E18-H159",
        "name": "migrant-fertility assimilation convergence",
        "batch": "E18",
        "f": {},
        "recorded_verdict": "one-time bridge",
    },
    {
        "id": "E18-H161",
        "name": "urban-density fertility penalty",
        "batch": "E18",
        "f": {"fS": 0.144, "fC": 0.06},
        "recorded_verdict": "durable bend",
    },
    {
        "id": "E18-H162",
        "name": "status-of-parenthood reversal",
        "batch": "E18",
        "f": {"fS": 0.096, "fC": 0.04},
        "recorded_verdict": "durable bend",
    },
    {
        "id": "H182",
        "name": "abortion restrictiveness (graded to total ban)",
        "batch": "E25",
        "f": {"fPb": 0.0135},
        "recorded_verdict": "REFUTED",
    },
    {
        "id": "H183",
        "name": "penalise family/friends who help with an abortion",
        "batch": "E25",
        "f": {"fPb": 0.021, "fS": -0.0025, "fC": -0.0017},
        "recorded_verdict": "REFUTED",
    },
    {
        "id": "H184",
        "name": "kin / grandparental support",
        "batch": "E25",
        "f": {"fPb": 0.051, "fS": 0.0127},
        "recorded_verdict": "PARTIAL",
    },
    {
        "id": "H185",
        "name": "in-kind childcare services (not cash)",
        "batch": "E25",
        "f": {"fPb": 0.0864, "fS": 0.0216},
        "recorded_verdict": "SUPPORTED",
    },
    {
        "id": "H186",
        "name": "reverse social atomisation (community / third places)",
        "batch": "E25",
        "f": {"fC": 0.035, "fS": 0.007},
        "recorded_verdict": "PARTIAL",
    },
    {
        "id": "H187",
        "name": "bistable social norm - pronatal media push",
        "batch": "E25",
        "f": {"fN": -0.024},
        "recorded_verdict": "PARTIAL",
    },
    {
        "id": "H188",
        "name": "polyamory raises the partnership count -> coupling",
        "batch": "E26",
        "f": {"fC": 0.0105, "fRV": 0.0021},
        "recorded_verdict": "REFUTED",
    },
    {
        "id": "H189",
        "name": "polyamorous alloparenting shares child cost -> parity",
        "batch": "E26",
        "f": {"fPb": 0.0192},
        "recorded_verdict": "PARTIAL",
    },
    {
        "id": "H190",
        "name": "CNM concentrates mating on high-status men -> excluded-male externality",
        "batch": "E26",
        "f": {"fC": -0.0135},
        "recorded_verdict": "REFUTED",
    },
    {
        "id": "H191",
        "name": "matrilineal descent raises fertility",
        "batch": "E26",
        "f": {"fRV": -0.0024, "fPb": -0.004},
        "recorded_verdict": "REFUTED",
    },
    {
        "id": "H192",
        "name": "matrilocal residence -> grandmaternal childcare",
        "batch": "E26",
        "f": {"fPb": 0.028, "fTau": -0.032},
        "recorded_verdict": "PARTIAL",
    },
    {
        "id": "H193",
        "name": "stacking co-resident female kin pools childcare",
        "batch": "E26",
        "f": {"fPb": -0.0064},
        "recorded_verdict": "REFUTED",
    },
    {
        "id": "H194",
        "name": "kibbutz-style full cost-socialisation of a child",
        "batch": "E26",
        "f": {"fPb": 0.0756, "fS": 0.0162},
        "recorded_verdict": "SUPPORTED",
    },
    {
        "id": "H195",
        "name": "generic cooperative breeding raises fertility",
        "batch": "E26",
        "f": {"fPb": 0.0175},
        "recorded_verdict": "PARTIAL",
    },
    {
        "id": "H196",
        "name": "state-funded universal in-kind childcare",
        "batch": "E26",
        "f": {"fPb": 0.0594, "fS": 0.0198},
        "recorded_verdict": "SUPPORTED",
    },
    {
        "id": "H197",
        "name": "the communal FORM without cost-socialisation raises fertility",
        "batch": "E26",
        "f": {"fPb": -0.0032},
        "recorded_verdict": "REFUTED",
    },
    {
        "id": "H198",
        "name": "media is a causal fertility channel (antinatal direction)",
        "batch": "E26",
        "f": {"fN": 0.016},
        "recorded_verdict": "SUPPORTED",
    },
    {
        "id": "H199",
        "name": "deliberate pronatal media raises fertility",
        "batch": "E26",
        "f": {"fN": -0.0105},
        "recorded_verdict": "PARTIAL",
    },
    {
        "id": "H201",
        "name": "maternal grandmother proximity raises fertility",
        "batch": "E26",
        "f": {"fPb": 0.034, "fTau": -0.0255},
        "recorded_verdict": "PARTIAL",
    },
    {
        "id": "H202",
        "name": "paying grandparents to provide care recreates the effect",
        "batch": "E26",
        "f": {"fPb": 0.006},
        "recorded_verdict": "REFUTED",
    },
    {
        "id": "H203",
        "name": "kin buffers the late-tempo fecundability loss",
        "batch": "E26",
        "f": {"fPb": 0.0144, "fTau": -0.0144},
        "recorded_verdict": "PARTIAL",
    },
    {
        "id": "H204",
        "name": "legal recognition of plural parents raises fertility",
        "batch": "E26",
        "f": {"fPb": 0.0018},
        "recorded_verdict": "REFUTED",
    },
    {
        "id": "H207",
        "name": "autonomy-lowering pronatal traditionalism raises fertility net",
        "batch": "E26",
        "f": {"fPb": 0.016, "fRV": -0.004},
        "recorded_verdict": "REFUTED",
    },
    {
        "id": "H200",
        "name": "a pronatal norm multiplies structural levers",
        "batch": "E26",
        "f": {"fN": -0.012},
        "recorded_verdict": "PARTIAL",
    },
    {
        "id": "H205",
        "name": "the complementary stack childcare + kin + pronatal-N is super-additive",
        "batch": "E26",
        "f": {"fPb": 0.0934, "fS": 0.0198, "fTau": -0.0255, "fN": -0.012},
        "recorded_verdict": "PARTIAL",
    },
    {
        "id": "H206",
        "name": ("state childcare and grandmother care are substitutes that crowd each other out"),
        "batch": "E26",
        "f": {"fPb": 0.0934, "fS": 0.0198, "fTau": -0.0255},
        "recorded_verdict": "REFUTED",
    },
    {
        "id": "H208",
        "name": "polygyny (one male, many females)",
        "batch": "E27",
        "f": {"fPb": -0.3663, "fC": -0.2331, "fRV": -0.0266, "fS": -0.0533},
        "recorded_verdict": "REFUTED",
    },
    {
        "id": "H209",
        "name": "polyandry (one female, many males)",
        "batch": "E27",
        "f": {"fRV": 0.024, "fC": -0.0036},
        "recorded_verdict": "PARTIAL",
    },
    {
        "id": "H210",
        "name": "extreme hypergamy / mating-market skew",
        "batch": "E27",
        "f": {"fC": -0.015, "fTau": 0.06},
        "recorded_verdict": "PARTIAL",
    },
    {
        "id": "H211",
        "name": "state-sanctioned polygyny (legitimacy + subsidy)",
        "batch": "E27",
        "f": {"fPb": -0.3663, "fC": -0.2331, "fRV": -0.0266, "fS": 0.0133, "fN": 0.0067},
        "recorded_verdict": "REFUTED",
    },
    {
        "id": "H212",
        "name": "media normalisation of the structure (N forcing)",
        "batch": "E27",
        "f": {"fN": 0.015, "fC": -0.08},
        "recorded_verdict": "REFUTED",
    },
    {
        "id": "H213",
        "name": (
            "state suppression of polygyny (enforced monogamy) is the fertility-fav"
            "ouring institution in the developed regime"
        ),
        "batch": "E28",
        "f": {"fC": 1.0614, "fS": 0.2562},
        "recorded_verdict": "SUPPORTED",
    },
    {
        "id": "H214",
        "name": "cultural / society endorsement of polygyny raises fertility",
        "batch": "E28",
        "f": {"fPb": -0.2928, "fC": -0.5307, "fS": -0.1281, "fRV": -0.0549, "fN": 0.022},
        "recorded_verdict": "REFUTED",
    },
    {
        "id": "H215",
        "name": "state endorsement + subsidy of polygyny manufactures the missing quantum",
        "batch": "E28",
        "f": {"fPb": -0.5856, "fC": -1.0614, "fS": 0.183, "fRV": -0.1098, "fN": 0.0439},
        "recorded_verdict": "REFUTED",
    },
    {
        "id": "H216",
        "name": (
            "the development regime flips the sign of polygyny (Tertilt +40% only i"
            "n low-development)"
        ),
        "batch": "E28",
        "f": {"fPb": 0.5856, "fRV": -0.5124, "fC": -0.1098, "fN": 0.0439},
        "recorded_verdict": "SUPPORTED",
    },
    {
        "id": "H217",
        "name": "polyandry endorsement suppresses fertility regardless of endorsement level",
        "batch": "E28",
        "f": {"fRV": 0.6222, "fC": -0.0915, "fN": 0.0366},
        "recorded_verdict": "SUPPORTED",
    },
    {
        "id": "H218",
        "name": (
            "state suppression of polyandry raises fertility by un-rationing women's reproduction"
        ),
        "batch": "E28",
        "f": {"fRV": -0.2928},
        "recorded_verdict": "PARTIAL",
    },
    {
        "id": "H220",
        "name": "endorsement shifts the bistable norm N enough to matter on its own",
        "batch": "E28",
        "f": {"fN": 0.0366},
        "recorded_verdict": "PARTIAL",
    },
    {
        "id": "H221",
        "name": "a state subsidy offsets the polygyny externality",
        "batch": "E28",
        "f": {"fS": 0.3294},
        "recorded_verdict": "PARTIAL",
    },
    {
        "id": "H247",
        "name": (
            "durable population-scale therapy/health raises marriageability and cle"
            "ars the E21 null"
        ),
        "batch": "E30",
        "f": {"fq": 0.084},
        "recorded_verdict": "SUPPORTED",
    },
    {
        "id": "H248",
        "name": "voluntary one-off couples therapy stays null",
        "batch": "E30",
        "f": {"fq": 0.084},
        "recorded_verdict": "REFUTED",
    },
    {
        "id": "H250",
        "name": (
            "father-access loss has no contemporary effect but a delayed intergenerational cost"
        ),
        "batch": "E30",
        "f": {"fF": -0.4},
        "recorded_verdict": "SUPPORTED",
    },
    {
        "id": "H252",
        "name": "relationship scars impose a delayed next-generation coupling cost",
        "batch": "E30",
        "f": {"fScar": 0.4},
        "recorded_verdict": "SUPPORTED",
    },
    {
        "id": "H253",
        "name": "a shared-custody presumption pays a delayed intergenerational dividend",
        "batch": "E30",
        "f": {"fC": 0.1, "fF": 0.25},
        "recorded_verdict": "SUPPORTED",
    },
    {
        "id": "H254",
        "name": (
            "paternity certainty raises father investment and pays an intergenerational dividend"
        ),
        "batch": "E30",
        "f": {"fF": 0.4},
        "recorded_verdict": "SUPPORTED",
    },
    {
        "id": "H259",
        "name": "cash can buy marriageability",
        "batch": "E30",
        "f": {"fS": 0.2},
        "recorded_verdict": "REFUTED",
    },
    {
        "id": "H261",
        "name": "rebuttable shared-custody presumption (the causal winner)",
        "batch": "E31",
        "f": {"fC": 0.15, "fF": 0.1, "fRV": -0.05},
        "recorded_verdict": "SUPPORTED",
    },
    {
        "id": "H262",
        "name": "rigid mandatory 50/50 vs rebuttable",
        "batch": "E31",
        "f": {"fC": 0.1, "fF": 0.06, "fScar": 0.08},
        "recorded_verdict": "PARTIAL",
    },
    {
        "id": "H263",
        "name": "fines / sanctions / contempt for access denial",
        "batch": "E31",
        "f": {"fF": 0.03, "fScar": 0.1},
        "recorded_verdict": "REFUTED",
    },
    {
        "id": "H264",
        "name": "criminalisation of alienation (Brazil Lei 12.318/2010)",
        "batch": "E31",
        "f": {"fScar": 0.15, "fF": -0.05},
        "recorded_verdict": "REFUTED",
    },
    {
        "id": "H265",
        "name": "mandated reunification therapy / camps",
        "batch": "E31",
        "f": {"fF": 0.02, "fScar": 0.1},
        "recorded_verdict": "REFUTED",
    },
    {
        "id": "H266",
        "name": "mandatory co-parenting / divorce education",
        "batch": "E31",
        "f": {"fq": 0.05, "fF": 0.03},
        "recorded_verdict": "PARTIAL",
    },
    {
        "id": "H267",
        "name": "early mediation (divert from litigation)",
        "batch": "E31",
        "f": {"fF": 0.12, "fScar": -0.08, "fq": 0.03},
        "recorded_verdict": "SUPPORTED",
    },
    {
        "id": "H268",
        "name": "DV carve-out design (safety-gated shared custody)",
        "batch": "E31",
        "f": {"fC": 0.15, "fF": 0.1},
        "recorded_verdict": "SUPPORTED",
    },
    {
        "id": "H269",
        "name": "weaponisation screen (the Meier correction)",
        "batch": "E31",
        "f": {"fScar": -0.1},
        "recorded_verdict": "PARTIAL",
    },
    {
        "id": "H270",
        "name": "prevention-over-punishment synthesis",
        "batch": "E31",
        "f": {"fC": 0.15, "fF": 0.15, "fq": 0.05, "fScar": -0.15, "fRV": -0.05},
        "recorded_verdict": "SUPPORTED",
    },
    {
        "id": "H271",
        "name": "social-work supervision",
        "batch": "E32",
        "f": {"fC": 0.05, "fF": 0.08, "fScar": 0.02},
        "recorded_verdict": "PARTIAL",
    },
    {
        "id": "H272",
        "name": "stepped therapy (escalate on failure, abuse-gated)",
        "batch": "E32",
        "f": {"fC": 0.1, "fq": 0.05, "fF": 0.22, "fScar": 0.06},
        "recorded_verdict": "PARTIAL",
    },
    {
        "id": "H273",
        "name": "monitored sanction (certainty supplied)",
        "batch": "E32",
        "f": {"fF": 0.05, "fScar": 0.18},
        "recorded_verdict": "PARTIAL",
    },
    {
        "id": "H274",
        "name": "raw criminalisation, no monitoring (severity)",
        "batch": "E32",
        "f": {"fF": -0.2, "fScar": 0.25},
        "recorded_verdict": "REFUTED",
    },
    {
        "id": "H275",
        "name": "coercion sign-heterogeneity",
        "batch": "E32",
        "f": {"fF": -0.03, "fScar": 0.1},
        "recorded_verdict": "PARTIAL",
    },
    {
        "id": "H276",
        "name": "foster/removal-until-reconciliation",
        "batch": "E32",
        "f": {"fq": -0.1, "fF": -0.45, "fScar": 0.4},
        "recorded_verdict": "REFUTED",
    },
    {
        "id": "H277",
        "name": "refund + clawback bond (the seed)",
        "batch": "E32",
        "f": {"fS": 0.05, "fC": 0.1, "fF": 0.2, "fScar": -0.12},
        "recorded_verdict": "SUPPORTED",
    },
    {
        "id": "H278",
        "name": "contingency-management milestone rewards",
        "batch": "E32",
        "f": {"fC": 0.15, "fF": 0.28, "fScar": -0.15},
        "recorded_verdict": "SUPPORTED",
    },
    {
        "id": "H279",
        "name": "conditional cash / tax credit",
        "batch": "E32",
        "f": {"fS": 0.2, "fC": 0.05, "fF": 0.1, "fScar": -0.05},
        "recorded_verdict": "PARTIAL",
    },
    {
        "id": "H280",
        "name": "symmetric two-sided bond (un-weaponizable)",
        "batch": "E32",
        "f": {"fC": 0.12, "fF": 0.18, "fScar": -0.15},
        "recorded_verdict": "SUPPORTED",
    },
    {
        "id": "H281",
        "name": "loss-frame (lose-it) vs gain-frame",
        "batch": "E32",
        "f": {"fS": 0.08, "fC": 0.15, "fF": 0.32, "fScar": -0.2},
        "recorded_verdict": "SUPPORTED",
    },
    {
        "id": "H282",
        "name": "child-outcome-contingent reward",
        "batch": "E32",
        "f": {"fC": 0.1, "fF": 0.24, "fScar": -0.14},
        "recorded_verdict": "PARTIAL",
    },
    {
        "id": "H283",
        "name": "objective clawback trigger (detection design)",
        "batch": "E32",
        "f": {"fF": 0.1, "fScar": -0.1},
        "recorded_verdict": "PARTIAL",
    },
    {
        "id": "H284",
        "name": "reward x shared-custody x mediation (the stack)",
        "batch": "E32",
        "f": {"fS": 0.05, "fC": 0.2, "fq": 0.05, "fF": 0.42, "fScar": -0.28},
        "recorded_verdict": "SUPPORTED",
    },
    {
        "id": "H286",
        "name": "escalating per-diem contact-denial ticket",
        "batch": "E32",
        "f": {"fF": 0.04, "fScar": 0.02},
        "recorded_verdict": "PARTIAL",
    },
    {
        "id": "H287",
        "name": "income-scaled day-fine",
        "batch": "E32",
        "f": {"fF": 0.05, "fScar": 0.02},
        "recorded_verdict": "SUPPORTED",
    },
    {
        "id": "H288",
        "name": "on-the-spot police issuance (certainty)",
        "batch": "E32",
        "f": {"fF": 0.05, "fScar": 0.03},
        "recorded_verdict": "PARTIAL",
    },
    {
        "id": "H289",
        "name": "civil (no custody consequence) vs criminal",
        "batch": "E32",
        "f": {"fF": 0.05, "fScar": 0.03},
        "recorded_verdict": "SUPPORTED",
    },
    {
        "id": "H290",
        "name": "revenue to the wronged parent (make-whole)",
        "batch": "E32",
        "f": {"fS": 0.02, "fF": 0.03, "fScar": 0.01},
        "recorded_verdict": "PARTIAL",
    },
    {
        "id": "H291",
        "name": "supervised exchange / neutral drop-off",
        "batch": "E32",
        "f": {"fF": 0.06, "fScar": -0.05},
        "recorded_verdict": "SUPPORTED",
    },
    {
        "id": "H292",
        "name": "parenting coordinator / special master",
        "batch": "E32",
        "f": {"fF": 0.04, "fScar": -0.03},
        "recorded_verdict": "PARTIAL",
    },
    {
        "id": "H293",
        "name": "family-support social work (corrective)",
        "batch": "E32",
        "f": {"fF": 0.02},
        "recorded_verdict": "PARTIAL",
    },
    {
        "id": "H294",
        "name": "criminal fine, custody-decoupled",
        "batch": "E32",
        "f": {"fF": 0.05, "fScar": 0.05},
        "recorded_verdict": "PARTIAL",
    },
    {
        "id": "H295",
        "name": "community service / public works",
        "batch": "E32",
        "f": {"fF": 0.06, "fScar": 0.06},
        "recorded_verdict": "PARTIAL",
    },
    {
        "id": "H296",
        "name": "suspended jail sentence (threat, decoupled)",
        "batch": "E32",
        "f": {"fF": 0.08, "fScar": 0.1},
        "recorded_verdict": "PARTIAL",
    },
    {
        "id": "H297",
        "name": "actual jail time (custody-decoupled)",
        "batch": "E32",
        "f": {"fq": -0.05, "fF": -0.15, "fScar": 0.3},
        "recorded_verdict": "REFUTED",
    },
    {
        "id": "H298",
        "name": "religious PRACTICE (weekly attendance) vs nominal affiliation",
        "batch": "E33",
        "f": {"fN": -0.06, "fC": 0.03},
        "recorded_verdict": "PARTIAL",
    },
    {
        "id": "H299",
        "name": "cross-denomination TFR gradient",
        "batch": "E33",
        "f": {"fN": -0.04, "fS": 0.04},
        "recorded_verdict": "PARTIAL",
    },
    {
        "id": "H303",
        "name": "pronatal theology (Quiverfull/LDS) via realised practice",
        "batch": "E33",
        "f": {"fN": -0.05, "fPb": 0.06},
        "recorded_verdict": "PARTIAL",
    },
    {
        "id": "H304",
        "name": "state-established church / religious schooling as a fertility lever",
        "batch": "E33",
        "f": {"fN": -0.006},
        "recorded_verdict": "REFUTED",
    },
    {
        "id": "H305",
        "name": "Israel nationalism as a SECULAR norm-carrier",
        "batch": "E33",
        "f": {"fN": -0.12, "fS": 0.08, "fC": 0.06, "fRV": -0.05},
        "recorded_verdict": "SUPPORTED",
    },
    {
        "id": "H308",
        "name": "religious marriage + lower divorce (compositional)",
        "batch": "E33",
        "f": {"fC": 0.1, "fScar": -0.08},
        "recorded_verdict": "PARTIAL",
    },
    {
        "id": "H309",
        "name": "non-stopping / higher parity (contraception rejection)",
        "batch": "E33",
        "f": {"fPb": 0.03},
        "recorded_verdict": "PARTIAL",
    },
    {
        "id": "H310",
        "name": "earlier tempo (younger marriage / first birth)",
        "batch": "E33",
        "f": {"fTau": -0.1},
        "recorded_verdict": "PARTIAL",
    },
    {
        "id": "H311",
        "name": "lower permanent childlessness (rho->0) - the strongest quantum channel",
        "batch": "E33",
        "f": {"fRV": -0.1},
        "recorded_verdict": "SUPPORTED",
    },
    {
        "id": "H312",
        "name": "congregation as community / alloparenting (fS)",
        "batch": "E33",
        "f": {"fS": 0.08},
        "recorded_verdict": "SUPPORTED",
    },
    {
        "id": "H313",
        "name": "traditional GENDER ROLES as the mechanism",
        "batch": "E33",
        "f": {"fScar": 0.05, "fC": 0.02},
        "recorded_verdict": "REFUTED",
    },
    {
        "id": "H307",
        "name": "is religion predominantly the norm channel N?",
        "batch": "E33",
        "f": {"fN": -0.06, "fC": 0.03, "fS": 0.08},
        "recorded_verdict": "PARTIAL",
    },
]

# E14 and E15 both record the shared 14-lever intervention menu IV1-IV14. Most pairs share the
# E14 channel map (re-listings of the same physical lever across two batches); a few differ
# (e.g. E14 IV3 = baby bonus `fPb` vs E15 IV3 = IVF subsidy `fTau`). Either way the ids collide,
# so batch-prefix any repeat - E14 keeps the canonical bare id, the E15 entry becomes `E15-IVn` -
# to keep id-keyed lookups from silently dropping a lever.
_seen_ids = set()
for _e in CATALOGUE:
    if _e["id"] in _seen_ids:
        _e["id"] = f"{_e['batch']}-{_e['id']}"
    _seen_ids.add(_e["id"])
assert len(_seen_ids) == len(CATALOGUE), "catalogue ids must be unique"


def force_of(f, start=0):
    """Build a 9-channel forcing function `fy(yr)` from a channel-amplitude dict.

    Applies the campaign's standard linear policy ramp (0 until start+2, full at start+12),
    matching `emergent.ramp` without importing the heavy model stack.
    """
    idx = {k: i for i, k in enumerate(CHANNELS)}

    def fy(yr):
        y = yr - start
        s = min(max((y - 2) / 10, 0.0), 1.0) if y >= 0 else 0.0
        out = [0.0] * len(CHANNELS)
        for k, v in f.items():
            out[idx[k]] += v * s
        return out

    return fy


def catalogue_by_batch():
    """The catalogue grouped by batch label (E14..E18, E25..E33)."""
    out = {}
    for e in CATALOGUE:
        out.setdefault(e["batch"], []).append(e)
    return out


if __name__ == "__main__":
    import os

    os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"
    os.environ["CUDA_VISIBLE_DEVICES"] = "GPU-58ae1f45-295c-681b-60ad-843265f52997"
    from pathlib import Path

    from sci_demographic_collapse.emergent import EmergentModel

    assert len(CATALOGUE) > 0, "catalogue is empty"
    for e in CATALOGUE:
        bad = set(e["f"]) - set(CHANNELS)
        assert not bad, f"{e['id']}: invalid channel keys {bad}"
        assert e["recorded_verdict"], f"{e['id']}: missing verdict"
    by = catalogue_by_batch()
    print(
        f"catalogue OK: {len(CATALOGUE)} levers across {len(by)} batches "
        f"{ {b: len(v) for b, v in sorted(by.items())} }"
    )

    root = Path(__file__).resolve().parents[2]
    m = EmergentModel(data_dir=str(root / "data" / "raw" / "unwpp"))
    base = m.run_cal("Korea")
    samples = [e for e in CATALOGUE if e["id"] in ("H185", "H261", "H305")]
    assert len(samples) == 3
    for e in samples:
        t = m.run_cal("Korea", force_of(e["f"]))
        print(
            f"{e['id']} {e['name'][:44]:<44} [{e['recorded_verdict']}] "
            f"Korea dTFR2125 {t['tfr'] - base['tfr']:+.3f}"
        )
    print("self-test passed")
