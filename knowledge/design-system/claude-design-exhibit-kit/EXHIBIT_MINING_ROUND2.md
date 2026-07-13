# Exhibit Mining · Round 2 — the Mid-Year Leadership deck

**Source:** `Engagement/internal/2026-mid-year-leadership/Input/2026-mid-year-leadership.pptx` (306-slide final; rendered candidates in `Input/exhibit-mining/`). Mined 2026-07-09, after the kit's T00–T14 were adopted (see DIGEST.md). The deck confirms the kit's provenance — the hidden Land·Expand·Consume backup section IS the kit's source material — and yields **ten patterns the kit did not template**, including three the kit's own SKILL.md listed as "approved but not templated" (stacked bars, plan-curve, strategy pyramid).

**Token validation:** the deck's chart semantics map 1:1 onto frontline-tokens roles — green = actuals/success, blue = forecast/lead, gray = budget/neutral, amber = warning, red = current/"from" state, cyan = hero total on dark. Nothing about these adoptions requires a new color.

## The ten patterns

| # | Pattern | Seen at | Adopt | Priority |
|---|---------|---------|-------|----------|
| R1 | **Target-walk waterfall** — quarter blocks stepping to a total column, dual numbers per block (actual/budget), dashed target line, boxed period summaries, **pipeline mini-table aligned under the axis** (amber warning cells) | s39 Road to Target | ✅ | **P1** — every QBR and account/region review |
| R2 | **Attainment bullet-bars** — progress bar + half-year target tick, semantic state color (behind=amber/orange, ahead=green), value+% inline; with **KPI split-header** (3 stat groups, hairline dividers) | s105 New bookings vs target | ✅ | **P1** — GTM OS, region reviews (Mihaljek) |
| R3 | **Health-tier drift board** — tier rows (full semantic ramp navy→blue→light→amber→red), rounded bars sized to value, **delta column** (↓€16M red / ↑€18M amber), summary "drift" band with hero callouts + status chips | s112 Value is Sliding | ✅ | **P1** — portfolio health, migration states (SBSA), base reviews |
| R4 | **Layer ziggurat with verb leaders** — stacked trapezoids, intensity ramp top→bottom, one verb per layer with dotted leaders, thesis text right | s190/s296 Moat Stack | ✅ | **P1** — THE canonical Banking OS visual; render in Frontline for client decks |
| R5 | **Current-vs-future paired bars** — red "current" bar over blue "with Backbase" bar per capability, legend chips, hero-value left rail + endorsement band | s129 Schroders spotlight | ✅ | **P1** — From→To as data; assessments, business cases |
| R6 | **Stacked ramp + step-line pair** — same series two encodings: staircase line (dots + value labels) beside stacked bars (base + upside, 2-color legend) | s182 Consumption Ramp | ✅ | P2 — ROI ramps, consumption models (stacked-ramp alone is the workhorse) |
| R7 | **Analogue evidence card** — company kicker + takeaway subtitle, quarterly ramp bars with **milestone-only emphasis** (3 dark bars among tints), value-prop/who-owns-it rail, 5-stat strip | s177 Sierra | ✅ | P2 — competitor/analogue proof slides (verify claims per feedback rule) |
| R8 | **Execution-system cascade** — outcome box (dark, cyan number) → motion boxes (blue) → enabler tiles (light), row labels left | s268 Three motions on six enablers | ✅ | P2 — program-on-a-page, account plans |
| R9 | **Zone matrix with numbered path** — 2×2 category matrix (filled quadrants, axis captions) + numbered move-arrows + step rail with highlighted step | s17/21/186/295 Execution Zones | ✅ | P2 — strategy frames (highlight chip → blue_light, never yellow) |
| R10 | **Split trend panels** — paired line charts, H1/H2 dashed divider, bracket annotations per half, 3-card takeaway row | s9 Financials outlook | ✅ | P3 — internal finance reviews |

**Not taken from this deck:** the yellow highlight chip (s21 → use `blue_light`), Aptos-era body fonts (n/a in our engine), the one-off AgentOps mega-architecture (s66) and product working-example diagrams (s196/s258) — bespoke content, not reusable patterns.

**Not yet mined:** s23 (time-to-scale zone variant), s66 (AgentOps), s106 (installed base), s249/s255 (resolution-loop / factory diagrams — candidates for a future "system diagram" recipe rather than a layout).

## Combined backlog (kit round 1 + deck round 2)

Implementation order when we productionize into `engine.js` + `frontline_slides_pptx.py` + composition-rules:

1. **Tranche 1 (approved, sampled):** sorted-bars · segmented-bar · quadrant-bubble · unit-dot-grid · source-footnote slot · chart color grammar — *sample deck built (`frontline-exhibit-adoption-sample.html`)*
2. **Tranche 2 (approved):** cohort-cascade · milestone-strip · dotted-region-map · roadmap gates · concern-answer
3. **Tranche 3 (round 2, pending Shyam's cut):** R1 target-walk · R2 attainment bullets · R3 drift board · R4 ziggurat · R5 paired bars, then R6–R10
