# [Paper digest] Lags and Leads in Life Satisfaction: A Test of the Baseline Hypothesis

**Authors**: Andrew E. Clark, Ed Diener, Yannis Georgellis, Richard E. Lucas<br>
**Year**: 2008  **Venue**: The Economic Journal 118(529):F222-F243 (IZA Discussion Paper 2526, Dec 2006)<br>
**Original (link)**: [https://docs.iza.org/dp2526.pdf](https://docs.iza.org/dp2526.pdf) (DOI 10.1111/j.1468-0297.2008.02150.x)<br>
**Local PDF**: `[paper] lags leads life satisfaction adaptation Clark, 2008.pdf` (open-access IZA discussion-paper version, full text)<br>
**Used in**: E42 HAPPINESS-FERTILITY core (calibrates the W adaptation timescale T_adapt - how fast life satisfaction returns to baseline after a life event)

## Summary

Twenty waves of German panel data (GSOEP), life satisfaction 0-10, tracked from five years before to five years after six life/labour events. Tests the hedonic-treadmill "baseline hypothesis": do people return to a set-point after shocks? Finding: adaptation is event-specific. It is essentially complete within a few years for divorce, widowhood, birth of first child and layoff; only partial for marriage; and absent for male unemployment. This gives the model per-event adaptation half-lives for the W dynamics.

## Parameters for the model

- **Birth of first child** (the fertility-relevant event): year-of-birth boost men +0.258, women +0.408; a one-year anticipation for men (+0.099); positive lag persists ~1 year for men, ~2 years for women (women 1-2 yr later +0.267), then decays to zero and slightly negative by 4-5 years (both ~-0.082). Adaptation to a first birth is complete within roughly 2 years -> T_adapt(birth) ~= 1-2 years
- **Marriage**: contemporaneous boost ~+0.3; recent-marriage boost decays over ~2 years (women) to 3 years (men); but the long-run "married" effect stays positive (+0.168 to +0.206) - adaptation is INCOMPLETE (a permanent set-point shift, not full return)
- **Widowhood**: sharp impact, year-of-event men -0.943, women -1.008 (the largest shock in the paper); recovers to ~baseline over ~3 years -> complete habituation, T_adapt ~= 2-3 years; strong lead (grief before death): within-next-year men -0.239, women -0.519
- **Divorce**: long-run effect not significant (complete adaptation); strongest LEAD effects - satisfaction below baseline 2 years before (women) to 3 years before (men); women divorced 4-5 years ago end up significantly happier (relief/rebound)
- **Unemployment (state)**: currently unemployed men -0.520, women -0.430; NO adaptation for men - satisfaction stays depressed for the whole spell (a permanent negative shift while unemployed)
- **Layoff (transition)**: negative for men ~2 years; women affected less
- **Set-point asymmetry**: bad states (unemployment) resist adaptation more than good/discrete events; men more affected by labour-market events, women by family events
- **Calibration takeaway**: use event-specific adaptation - discrete positive events (birth, marriage boost) decay on a ~1-2 year timescale back toward a baseline; ongoing bad states (unemployment) do NOT adapt away; a first-birth happiness bump is transient (gone within ~2 years), so a level-based W-fertility loop must not treat the birth boost as permanent

## Caveats

German-only, and small cells for widowhood/widowers weaken those estimates. "Complete adaptation" is measured over a 5-year post-event window, so very-slow residual adaptation could be missed. Coefficients are on a 0-10 life-satisfaction scale controlling for income, health, children, region and year. The key modelling input is the timescale (T_adapt ~ 1-2 yr for discrete positive events; no adaptation for chronic unemployment), not the absolute magnitudes.
