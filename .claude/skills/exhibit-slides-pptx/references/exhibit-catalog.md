# Exhibit catalog — pick the exhibit that matches the content

One exhibit per slide, 2–3 callouts max. Choose from this validated set; do not invent a new
visual grammar mid-deck. All were production-tested on client decks (BACB close 16 Jul 2026,
SNB Capital 21 Jul 2026). Build with `ExhibitDeck` primitives (`rect/txt/oval/hline/dashed_conn`).

## Core patterns (T02–T14)

| # | Pattern | Use when | Build notes |
|---|---------|----------|-------------|
| T02 | **Sorted bars** | Ranked magnitudes | Lead bar `BLUE`, the client's own bar `NAVY` bold (when the client has the metric — if not, carry them in the under-bar line instead), rest `BLUE3/BLUE4` tinted. Right-aligned value labels. See `example_build.py` S3. |
| T03 | **Segmented to-scale bar** | One total split into parts | Widths strictly proportional; label each segment; total at the right |
| T04 | **Wave/gantt timeline** | Plans in waves | `d.diamond()` gates: blue = platform release, coral = decision the CLIENT owns |
| T05 | **Quadrant bubble** | Two measures + size | Light zone fills (tint), dashed boundary lines, uppercase zone captions at zone tops, uniform dots + labels; dashed blue arrow = the move |
| T06 | **Dotted region map** | Geography by intensity | One dot = one land unit; navy label chips; shade-legend row above |
| T07 | **Cohort cascade** | Funnel over time | Bottom-aligned stacks growing left→right; carried-in cohorts in tint; gates as dashed verticals |
| T08 | **Milestone strip** | 3–4 big numbers on a journey | Oversized numerals on a milestone line, gate diamonds, dark ramp band beneath |
| T09 | **Unit dot-grid** | "x of y" messages | One dot = one unit, filled `BLUE` vs dim `TINT`; hero band "= x of y". See S4 |
| T10 | **Concern → answer stack** | Objection handling | Dark glow card per concern, answer in white |
| T11 | **Chips + hero split** | Few facts + one key message | Dashed chips left, dark hero card right, at most one coral callout |
| T12 | **Cadence tiles + step flow** | Rhythms and sequences | Big W/M/Q letterforms; numbered chips with arrows |
| T13 | **Plain table** | The ONE intentional table per deck | Condition · owner · date. Header row in blue caps, hairline row rules. See S6 |
| T14 | **Chapter divider** | Section breaks | `d.divider(number, title, subtitle)` — dark, big light-weight number |

Also approved (compose from primitives): stacked bars, phase grids, strategy pyramid,
plan-curve + upside fan, stat grid (S2), persona profile/solve pair, lifecycle map.

## SNB Capital vocabulary (T17-class — the 37-slide VC-track deck Shyam ratified as the look)

Reference build: `Engagement/SNB Capital/Output/build_snbc_vc_pptx.py` (+ the dossier deck
`SNBC_persona_dossiers_22Jul.pptx`). Copy the slide function, swap the content.

- **Meet-slide / persona dossier** — full-page persona: name + age header, bio line,
  context chips, ONE navy hero-stat card, needs, "WHAT HE DOES NOT KNOW TO ASK FOR"
  (unconsidered needs), where-he-goes-today row, verbatim quote, watch-fors, hand-off line.
- **Impact close (stat-card row) — THE default value/impact visual** (Shyam, 28 Jul 2026:
  "I use this one more — a lot cleaner"; supersedes the 3-hero-tile close, now retired to
  only-when-the-room-needs-exactly-one-number): blue subtitle (bold lead + regular rest,
  13pt) · "WHAT IT MOVES" micro-label · FOUR `d.stat_card()`s across the content width
  (muted "from →" line, 30pt `BLUE2` landing value, muted label) · navy hero-claim card
  (~5.6 × 0.82, 15pt bold white — the ONE headline range) with 2–3 receipt lines beside
  it (11.5pt) · `d.proven_band()` naming where it runs live · source footnote.
  Copy-source: `example_build.py` S5.
- **Cascade surfaces** — N persona-labelled app-surface cards on a ONE-PLATFORM navy band
  ("two demoed · five served · one platform"). The scale-without-rebuild close.
- **Node-chain engine** — entry points → prescription → channel node chains; the
  intelligence-engine grammar (5 entry points, never a single pipe).
- **Wave roadmap with coral gates** — T04 waves where every coral diamond is a decision
  the CLIENT owns, labelled with the risk it retires (hosting, data, segment split).
- **Divergence matrix** — personas × domains grid showing where propositions diverge;
  converges into the packages ladder.
- **Packages ladder** — land / grow / compound package columns with value-pool tags.
- **Lifecycle map** — stage columns × platform components + a metric per stage.
- **Use-case catalog grid** — dense tile grid (e.g. 24 conversational use cases),
  "live in prototype" flags in blue, the rest tinted.

## Journey & workshop patterns (T16-class — validated SNB Capital journey maps, 27–28 Jul 2026)

Reference build: `Engagement/SNB Capital/Output/build_snbc_journey_maps_pptx.py`.

- **Swim-lane process map** — an end-to-end journey as actor lanes (CLIENT / SYSTEM /
  EMPLOYEE) × navy stage chips across the top; each step a `d.chip()`; hairline rules
  BETWEEN lanes only (never under the last lane — it collides with the bottom band);
  a navy deltas band closes the slide (cyan before→after pairs, e.g. "35% → 5%").
- **Today vs target case-flow** — left column: coral dashed pain chips ("today");
  right column: the target flow as stacked tint chips, first step `BLUE`/white, small
  blue ↓ between steps. Balance the two columns' bottoms.
- **Rules table (signal → prescription → channel)** — navy signal chips · plain
  prescription text · tint channel chips, one row per rule. The exhibit that says
  "rule-based first, AI later"; doubles as a live workshop exercise.
- **Hero delta tiles** — 2–3 big before→after tiles: gray "from" line, 38pt bold BLUE2
  number, one-line label, on a TINT card. Workshop-steer slides only (velocity in the
  room); for impact/value closes use the stat-card row above — the ratified default.
- **STEER chip** — `d.chip(fill=None, line=CORAL, dash='dash', bold=True, tc=CORAL)`
  carrying the question you hand the room ("STEER: …"). One per workshop-steer slide,
  bottom of slide, >=0.06in above the footnote hairline.

## BACB/SNB-validated additions (T15-class)

- **Receipts row** — a claim with its sourced stats lined up underneath it, each stat
  numbered to the footnote. Use when a bold claim needs instant evidence.
- **Dashed = yours** — half-built grammar: solid shapes are what Backbase ships, dashed
  (`DASHC` or coral) outlines are what the client owns/decides. Keep the legend on-slide.
- **Scenario board** — phases across the top × A/B bands down the side; one recommended
  band tinted. For "two shapes of the same program" conversations.
- **Engagement plan** — session / outcome / attendees rows, navy finale row with the ask.
- **Story page** — who → problem → what we did → what it proved, one client story per slide,
  anonymised ("a UK wealth manager we are implementing now").

## Data exhibits (T17-class — the v3.2 chart layer, mined from the TD 1Mn-calls deck, Sep 2026)

**Form follows message (rule, same weight as the type scale):** if the slide's claim is a
magnitude, trend, ranking, share or distribution, the exhibit MUST be a drawn chart from this
section — never boxes. Boxes are for structure, sequence and quality comparisons. Charts are
DRAWN (flat shapes + freeform polylines via the engine) — never native PowerPoint chart parts.
Runnable reference: `example_data_build.py` (all seven, neutral content).

| # | Pattern | Use when | Build with |
|---|---------|----------|------------|
| T17 | **Data slide + so-what rail** | Any chart slide needing its argument beside it | exhibit at x=1.0..9.6 + `d.so_what_rail()` (2-3 `hero_stat`s over an `implication_card`; coral stat = the tension). See S1/S2 |
| T18 | **Column chart** | A magnitude over time or categories | `d.bars()` — value labels above bars ARE the data (no y-axis, no gridlines), muted deltas under them, intensity ramp `mode='time'` (light→BLUE) or `'rank'`; `hi` bar + label in full BLUE |
| T19 | **Line panel(s)** | A trend, an inflection, a divergence | `d.line_panel()` — series label ON the panel, annotated peaks/troughs (dot + bold value + muted phrase), ticks under the LAST panel only; stack two thin panels over one dual-axis chart |
| T20 | **Pulse-panel grid** | "We see live telemetry" operational credibility | `d.panel_grid()` of `pulse_panel`s — themed top bars (blue = day job, coral = friction, deep navy = growth), sparkline + observed range per card; takeaway callouts with tick bars beneath. See S3 |
| T21 | **Double-click stage board** | One lever/use-case suite, end to end | `d.frame_band("OPPORTUNITY", …)` top → `d.stage_column()`s (numbered plays, bold lead + muted body) → navy solution rail → `d.frame_band("VALUE", …)` bottom. See S4 |
| T22 | **Swimlane wave roadmap** | Capability roadmap gated by evidence, not dates | `d.lane_row()` headers left × wave columns; `d.chip()` use-cases (fill intensity = commitment), per-wave value notes in blue text, coral `d.diamond()` gates ON a bottom axis, labels under it. See S5 |
| T23 | **Dot grid, codified** | "x of y" share messages (T09 now has an engine call) | `d.dot_grid()` — filled from the bottom row up + tick-bar hero line "= x of y". See S6 |

Rail geometry (T17): rail x=9.98, w=2.70 (ends 12.68, clear of the right hairline at 12.760);
exhibit keeps to x=1.0..9.6. Hero stats: number + tick in the SAME color, 30pt regular (never
bold); the implication card fills down to y=6.30 and never crosses the footnote hairline.

### Comparison exhibits (T24-T29 — the v3.3 layer; sources: MGI/BCG grammar via the round-2
### mid-year mining, IBCS attainment discipline, JPM investor-day walk, HTML-engine parity)

Runnable reference: `example_charts_build.py` (all six, neutral content).

| # | Pattern | Use when | Build with |
|---|---------|----------|------------|
| T24 | **Waterfall (target walk)** | A number walks to another via named moves | `d.waterfall()` — totals NAVY; pass `positive=` the GOOD direction (BLUE), the honest counterweight goes CORAL (on a cost walk `positive='down'`); dashed step lines carry the levels |
| T25 | **Bullet bars (attainment)** | Actuals vs plan/target, mixed units welcome | `d.bullet_bars()` — IBCS-style: light track, BLUE actual, NAVY plan tick at a fixed fraction so each row scales to ITS OWN plan and over-plan rows visibly cross the tick; deltas colored by direction |
| T26 | **Paired From-To bars** | Current vs with-Backbase as data, not prose | `d.paired_bars()` — From = BLUE4 muted, To = BLUE bold, legend top-right; add `d.growth_arrow()` across the To-bars for the average lift (JPM CAGR style) |
| T03 | **Segmented to-scale bar** — now engine-backed | One total split into parts | `d.segbar()` — widths strictly proportional, display inside segments, names below, total right; label only segments above ~8% share (group the tail) |
| T05 | **Quadrant bubble** — now engine-backed | Two measures pick the priority order | `d.quadrant()` — target zone tinted, dashed midlines, uppercase zone captions, uniform BLUE dots, `move=` draws the dashed sequencing arrow |
| T08 | **Milestone strip** — now engine-backed | 3-4 big numbers on a journey | `d.milestone_strip()` — oversized numerals over gate diamonds on one line, optional navy band beneath |

Annotation helper: `d.growth_arrow(x1,y1,x2,y2, label)` — arrowed connector with a bold
label above the midpoint; `dash='dash'` for the quadrant move arrow.

### Evidence exhibits (T30-T39 — the v3.4 layer; grammar mined from the BCG archive,
### re-expressed in exhibit tokens: good/covered = BLUE family, gap = CORAL, never green)

Runnable reference: `example_bcg_build.py` (all of them, neutral content). Full mining:
`knowledge/design-system/claude-design-exhibit-kit/EXHIBIT_MINING_ROUND4_BCG.md`.

**Serial-template law:** when a deck profiles N comparable things (players, vendors,
journeys, pillars), build ONE template slide and repeat it N times — never redesign per
item. Kicker carries the series position ("player profile 3 of 9").

| # | Pattern | Use when | Build with |
|---|---------|----------|------------|
| T30 | **Harvey ball** | One verdict per cell in ledgers | `d.harvey(x,y,d,frac)` — quarter steps, BLUE on TINT2 |
| T31 | **Evaluation matrix** | Vendors/options x gating criteria | `d.eval_matrix()` — logo or clean-text columns, monogram criteria rows, harvey cells, legend on. See S2 |
| T32 | **Logo chip / wall** | Market maps, "works with" rails, credential walls | `d.logo_chip()` (image, or clean-text fallback — never fabricate a logo), `d.logo_wall()`; group with header chips + count ovals. See S3 |
| T33 | **Fact rail** | Dossier spine: the who/what/where of a profiled thing | `d.fact_rail()` — monogram square + bold label + muted value |
| T34 | **Leader note** | Annotating a product shot, screen, or diagram | `d.leader_note()` — dashed line to a bold-lead floating note |
| T35 | **Tile grid** | N parallel moves/themes/features, uniform weight | `d.tiles()` — accent top bars carry meaning (coral = the dependency/risk); never stretch tiles. See S4 |
| T36 | **Agenda tracker rail** | Section navigation; re-shown each chapter, light moved | `d.agenda_rail()`. See S5 |
| T37 | **Ring stat** | 1-5 proof numbers without a chart | `d.ring_stat()` — open circle, bold value, caption below |
| T38 | **RAG coverage matrix** | OOTB vs configuration vs custom vs gap boards | `d.rag_matrix()` — BLUE covered / BLUE4 partial / CORAL gap / TINT2 n-a, legend mandatory. See S6 |
| T39 | **Status tag** | Honesty labels top-right | `d.tag_chip()` — ILLUSTRATIVE / PRELIMINARY / NOT EXHAUSTIVE (coral dashed), BACKUP (tint) |

Composable recipes (no primitive needed — see the round-4 mining doc): player dossier
one-pager (S1) · vendor profile 4-up · architecture coverage shading (chip the blocks of a
diagram BLUE/BLUE4/CORAL by OOTB fit) · architecture navigator breadcrumb · phase x
activity matrix with ramped headers · funnel strip with ring counts · press/credential
wall · journey teardown kit · workshop exercise card (Objective band + Exercise/Hints/
Output columns) · From→To icon ledger.

Logo rule: market/vendor/ecosystem logos are allowed on landscape and evaluation
exhibits (image assets supplied per deck); the CLIENT's own account name stays clean
text in client decks. Never fabricate a logo — text chips until assets exist.

## Credibility architecture (what made these decks defensible)

- **Coral dashed badge** = ILLUSTRATIVE / OUTSIDE-IN / still-open. Never present an assumed
  number as verified — badge it coral, name the owner of the open item (`d.open_badge`).
- **DEFENSE lines in speaker notes** on every number slide: what to say if the number is
  challenged, the source to attribute, the reconciliation if the client's own figure differs.
  Write them at build time while the sourcing is fresh — this is where the deck wins the room.
- **"The math, in the open"** — a formula-table appendix slide showing each headline number's
  calculation chain. Offer it, don't force it into the main flow.
- **Source footnote on every numeric slide** (`d.footnote`), numbered references, honest
  caveats ("definitions differ; comparison directional").
