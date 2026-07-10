# [Paper digest] The Spread of Behavior in an Online Social Network Experiment

**Author**: Damon Centola (MIT / Harvard)<br>
**Year**: 2010  **Venue**: Science 329(5996):1194‒1197, DOI 10.1126/science.1185231<br>
**Original (download)**: [https://faculty.cs.byu.edu/~mike/mikeg/papers/SpreadofBehaviorinSocialNetworkExperimentScience.pdf](https://faculty.cs.byu.edu/~mike/mikeg/papers/SpreadofBehaviorinSocialNetworkExperimentScience.pdf) (open-access university mirror)<br>
**Local PDF**: `[paper] spread of behavior online network experiment Centola, 2010.pdf` (in this folder)<br>
**Used in**: E38 (social-fabric round; H368 / H369 - experimental confirmation that clustering beats reach for behaviour)

## Key mechanism

Centola built the missing experiment for the complex-contagion theory: he constructed the social network itself and randomised its topology, so tie structure is exogenous rather than confounded with homophily. Participants in an online health community were embedded either in a CLUSTERED-LATTICE network (redundant ties - your neighbours share neighbours, so an adopter's activity reaches you through multiple reinforcing paths) or in a RANDOM network with the same number of neighbours per node (same degree, but ties rewired to reach distant, non-overlapping parts of the graph). A health behaviour (registering for and using a health forum) then spread as participants received "health-buddy" signals. Because degree is held identical across conditions, any difference in spread is caused purely by clustering/redundancy - the direct test of whether reinforcement (clustered) or reach (random) wins for a costly behaviour.

## Main findings

- The behaviour reached 53.77% of nodes in the CLUSTERED-lattice networks versus only 38.26% in the RANDOM networks - clustering raised adoption by ~15 percentage points (a ~40% relative gain)
- Diffusion was also FASTER in the clustered condition: spread rate ~0.0643 x 10⁻³ nodes/s in the random condition, higher in the clustered one; both success and rate differences were statistically significant
- Adoption is threshold-like: individuals were significantly more likely to adopt after receiving reinforcing signals from MULTIPLE distinct neighbours, not just one
- A second signal sharply raised the adoption hazard and a THIRD signal raised it further; additional signals beyond the third had no significant effect (reinforcement saturates at ~3)
- Engagement echoed the threshold: <15% of adopters who received one signal returned to the forum, >30% of those receiving two signals returned, and 40% of those receiving three signals made a return visit
- Confirms Centola & Macy (2007) empirically: for a costly/effortful behaviour, redundant local ties beat long-range reach - the opposite of the simple-contagion result

## Method and identification

- Randomised controlled network experiment: N ≈ 1,500 participants recruited to structured online communities, randomly assigned to clustered vs random network conditions with identical degree
- The experimenter engineered the network, so topology is exogenous - this removes the homophily/selection confound that plagues observational peer-effect studies (the paper's core identification advance)
- Outcomes: fraction of network adopting (success of diffusion) and hazard of adoption per number of reinforcing signals (Cox proportional-hazards model)

## Key takeaways for the model

- Hard calibration numbers for a clustering premium: clustered topology lifts final adoption 38.3% → 53.8% at equal degree - use as the effect size for the reinforcement/clustering term (H368/H369)
- Reinforcement saturates: adoption probability rises through the 2nd and 3rd reinforcing neighbour then flattens - set the complex-contagion threshold near 2‒3 active neighbours, with diminishing returns above 3
- Behaviour ≠ information: since childbearing is behaviour, seed a pronatal norm into DENSE, redundant local clusters, not into maximally-reaching weak-tie hubs; reach without redundancy under-delivers by ~15 points

**Tags**: `complex-contagion` `network-experiment` `clustered-vs-random` `reinforcement` `adoption-threshold` `53.8-vs-38.3` `Cox-hazard` `homophily-control` `Centola` `H368` `H369` `E38`
