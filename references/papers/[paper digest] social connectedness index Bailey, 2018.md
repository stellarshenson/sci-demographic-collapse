# [Paper digest] Social Connectedness: Measurement, Determinants, and Effects

**Author**: Michael Bailey, Rachel Cao, Theresa Kuchler, Johannes Stroebel, Arlene Wong (Facebook / NYU Stern / Princeton)<br>
**Year**: 2018  **Venue**: Journal of Economic Perspectives 32(3):259‒280, DOI 10.1257/jep.32.3.259<br>
**Original (download)**: [https://www.aeaweb.org/articles/pdf/doi/10.1257/jep.32.3.259](https://www.aeaweb.org/articles/pdf/doi/10.1257/jep.32.3.259) (fully open access, JEP)<br>
**Local PDF**: `[paper] social connectedness index Bailey, 2018.pdf` (in this folder)<br>
**Used in**: E38 (social-fabric round; H370 - the Social Connectedness Index as the region-to-region tie matrix)

## Key mechanism

The paper introduces the Social Connectedness Index (SCI), the first large-scale representative map of who is socially tied to whom across geographies, built from the universe of Facebook friendship links. For every pair of regions the SCI is the normalised count of friendship links between people in region i and region j, turning a private friendship graph into a public region-by-region connectedness matrix. The mechanism it exposes is that social ties are steeply LOCAL - friendship probability falls off sharply with distance and is cut by political and historical boundaries - yet a minority of ties reach far, and those predict real economic outcomes (trade, migration, patenting, mobility). For a fertility model the SCI supplies the empirical weights on the inter-region influence channel: how strongly a norm in one region reaches residents of another.

## Main findings

- The SCI is built between all 3,136 US counties (and between every US county and every foreign country) as the normalised count of friendship links, rescaled so the highest observed value = 1,000,000 (a relative, capped index, not an absolute count)
- Distance decay is steep: the elasticity of friendship-link intensity to geographic distance is about −2.0 for distances under 200 miles, weakening to about −1.2 beyond 200 miles (i.e. doubling distance under 200 mi roughly quarters the tie count)
- Ties are overwhelmingly local: for the median (population-weighted) US county, 55.4% of friends live within 50 miles; the great majority live within ~100 miles, though this share varies widely across counties
- Political and historical boundaries matter beyond distance: state lines, historical divisions and past migration episodes all shape who is connected, so connectedness is not a pure function of physical proximity
- SCI is positively correlated with cross-region economic activity - migration, trade, spread of innovation and social mobility - validating friendship structure as an economic force
- The authors define a "relative probability of friendship" = SCI(i,j) divided by the product of the two regions' user counts, to compare connectedness net of population size

## Method and identification

- Data: a snapshot of the universe of Facebook friendship links (aggregated, anonymised); active users only, so coverage skews to the online-active population - the main measurement caveat
- Construction: raw pairwise link counts → normalised and capped at 1,000,000; the index is inherently RELATIVE (rankings and elasticities interpretable, absolute magnitudes not)
- Determinants from regressing log SCI on distance and boundary variables; effects are descriptive/correlational - a measurement piece, not a causal design

## Key takeaways for the model

- Use SCI as the empirical inter-region coupling weight in the social-fabric layer (H370): connectedness between regions is far from uniform and decays with a distance elasticity near −2 short-range, −1.2 long-range - plug these as the off-diagonal norm-transmission strengths
- Ties are ~55% within 50 miles, so norm diffusion is dominated by WITHIN-region and near-neighbour coupling; long-range cross-region influence exists but is an order of magnitude thinner - do not model regions as equally coupled
- Caveats to carry: the index is normalised/capped (relative only), reflects the Facebook-active population, and within-region self-loops dominate the raw matrix - guard against double-counting a region's own density as external influence

**Tags**: `social-connectedness-index` `SCI` `Facebook-friendship-graph` `distance-decay` `elasticity-minus-2` `inter-region-coupling` `55-percent-within-50mi` `measurement` `Bailey` `H370` `E38`
