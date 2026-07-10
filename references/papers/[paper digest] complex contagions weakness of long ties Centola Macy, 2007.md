# [Paper digest] Complex Contagions and the Weakness of Long Ties

**Author**: Damon Centola (Harvard University), Michael Macy (Cornell University)<br>
**Year**: 2007  **Venue**: American Journal of Sociology 113(3):702‒734, DOI 10.1086/521848 (2009 ASA Best Article in Mathematical Sociology)<br>
**Original (download)**: [https://ndg.asc.upenn.edu/wp-content/uploads/2016/04/Centola-Macy-2007-AJS.pdf](https://ndg.asc.upenn.edu/wp-content/uploads/2016/04/Centola-Macy-2007-AJS.pdf) (open access, author's Network Dynamics Group site)<br>
**Local PDF**: `[paper] complex contagions weakness of long ties Centola Macy, 2007.pdf` (in this folder)<br>
**Used in**: E38 (social-fabric round; H368 - complex contagion, the KEY reinforcement-threshold paper)

## Key mechanism

Centola and Macy split "contagions" into SIMPLE and COMPLEX. A simple contagion (a rumour, a virus) needs contact with a single active source, so it rides Granovetter's long weak ties and diffuses fast. A complex contagion needs social AFFIRMATION from multiple independent sources before an individual will adopt - high-risk, high-cost, or norm-violating behaviours (joining a movement, an avant-garde fashion, an unproven technology, and by extension a costly life decision like having a child). For a complex contagion a single weak tie is not enough: a node needs several of its neighbours already active. The paper's central result is that long ties are only strong for simple contagions; for complex contagions what matters is the WIDTH of a bridge - the number of parallel ties connecting one neighbourhood to another - not its length. Randomly rewiring a clustered network shortens path length (good for simple contagion) but narrows bridges to width 1, which KILLS complex contagion.

## Main findings

- Two regimes: simple contagion adopts on 1 signal (threshold effectively 1); complex contagion requires a threshold of ≥ 2 active neighbours (affirmation from multiple sources)
- A "wide bridge" of width w can transmit a contagion of threshold up to w; a width-1 long tie (the classic weak-tie bridge) transmits simple contagion but CANNOT carry a threshold-≥2 complex contagion
- Random perturbation of a regular lattice: for simple contagions the small-world rewiring speeds diffusion, but for complex contagions there is a critical amount of rewiring beyond which the behaviour fails to propagate at all
- The "strength of weak ties" therefore does NOT generalise from information to costly behaviour - long ties become a weakness, impeding diffusion, once adoption needs reinforcement
- Wide, redundant bridges are characteristic of SPATIAL/clustered networks, which explains why real social movements diffuse geographically (neighbourhood to adjacent neighbourhood) rather than jumping randomly across a network
- The result inverts standard small-world intuition: clustering (redundancy), usually treated as inefficient, is precisely what a complex contagion needs

## Method and identification

- Formal generalisation of the Watts (2002) threshold model on regular lattices with tunable neighbourhood size and random rewiring probability
- Diffusion simulated from small active seeds; outcome measured as whether/how fast the contagion reaches the whole network under varying threshold and rewiring
- Identifying comparison holds degree fixed while varying bridge WIDTH and path length, isolating width as the causal structural variable for complex spread

## Key takeaways for the model

- Childbearing is a COMPLEX contagion (costly, identity-laden, needs multiple reinforcing peers) - so a pronatal norm needs a reinforcement THRESHOLD of ≥ 2 active neighbours in the model, not single-contact exposure (H368)
- Sets a hard structural gate: norm spread depends on wide/redundant local bridges; atomised, weak-tie-only networks BLOCK the low-fertility escape rather than help it - more (weak) ties is not more diffusion for behaviour
- Parameterise a clustering/bridge-width term separate from average degree; below a critical width the seeded norm cannot cross clusters at all (sign-flip vs simple-contagion intuition)

**Tags**: `complex-contagion` `reinforcement-threshold` `wide-bridges` `long-ties` `weak-ties` `Watts-threshold-model` `clustering` `spatial-diffusion` `Centola` `Macy` `H368` `E38`
