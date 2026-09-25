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

## Apex recipes (T40–T55 — the Claude Design look measured from the Nedbank report, 18 Sep 2026;
## named Apex and made the default 24 Sep 2026; every helper reads the active palette)

| # | Exhibit | Use when | Engine |
|---|---|---|---|
| T40 | **Stat grid** | "The floor, in eight numbers": 4 to 8 bank-stated figures, tension numbers on dark blocks | `d.stat_grid(s, x, y, cells, cols=4)` — cells `{number, caption, dark, icon}`; icons via `X.icon()` |
| T41 | **Lane grid + weight legend** | "Built once, used by all N": components in labelled lanes, a count badge per box, fill weight = reuse | `d.lane_grid(s, x, y, lanes)` + `d.weight_legend()`; span=2 for double cards; `d.card_row()` for one lane |
| T42 | **State panels** | Today / next / beyond: 3 tinted panels, each with a drawn bar, a big price and mini-stats | `d.panel()` + `d.mini_stat()` + `d.rect()` bar (see example_v4_build P3) |
| T43 | **Option cards** | Two or three commercial or design options, one recommended (dark, cyan badge), comparison-only dashed | `d.option_card(s, x, y, w, h, tag, name, body, stats, kind='dark'|'faint'|'dashed', badge=)` |
| T44 | **Numbered cards** | "Your seven questions", roles on Monday, a question bank: number, title, body, page chip | `d.numbered_card(s, x, y, w, h, n, title, body, tag=)`; `kind='dark'` for the how-to-read card |
| T45 | **Step flow** | How a call runs, how a deal runs: N step cards with arrows, one blue, one dark | `d.step_flow(s, x, y, items)` — items `(num, title, body, weight)` |
| T46 | **Compare rows** | Moment by moment, today against with-us, an effort column | `d.compare_rows(s, x, y, headers, rows)` |
| T47 | **Stacked hbars** | Cost by intent, do-nothing against with-us per row | `d.stacked_hbars(s, x, y, w, rows)` |
| T48 | **Wave track** | Four waves, four gates the client owns | `d.wave_track(s, x, y, w, waves, progress=, marker=)` |
| T49 | **Timeline lanes + who signs** | The mutual plan: dated nodes, an owner lane per side, the signing chips | `d.timeline_lanes(s, x, y, w, nodes, lanes, committed=)` then `d.who_signs()` |
| T50 | **From → To columns + pillar row** | The shift page: muted today, navy tomorrow, an arrow between; three pillars under a rule | `d.from_to_columns(s, y, ...)`; `d.pillar_row(s, x, y, w, items, label=)` |
| T51 | **Share bar** | Where the volume goes: one bar split to scale with values inside | `d.share_bar(s, x, y, w, segments)` |
| T52 | **Hero number · mini stat · statement line** | The so-what as a figure (dark block, cyan number) or as one sentence (navy lead, blue rest) | `d.hero_number(dark=, layout='side'|'stack')`, `d.mini_stat()`, `d.statement_line()` |
| T53 | **Pages** | Cover (navy, offset frame, accent word), chapter divider (blue band), vision band, film frame | `d.cover_page(kicker, runs, date_line=, client_logo=, title_w=)`, `d.divider_band()`, `d.vision_band()`, `d.film_frame()` |
| T54 | **Icons** | A line icon top left of a stat block or card, the twelve from the Nedbank export | `X.icon('phone')` → `stat_block(icon=...)`; never emoji, never a fabricated glyph |
| T55 | **Apex bars** | Column or row bars without bold: 19pt value, 8.5pt status, dashed outline for estimates | compose from `d.rect()` + `d.txt()` as in the company-view build (`vbars`, `hrows`) until the engine variant lands |

| T56 | **Ranked horizontal bars** | Ranked magnitudes, one series, two colours by category (report p25) | `d.hbar_rows(s, x, y, w, items)` + `d.legend()`; items `(label, value, display[, fill])`, codes before " · " draw BLUE |
| T57 | **Stacked horizontal rows** | Composition per row with a volume column: minutes, cost per intent (p12) | `d.hstack_rows(s, x, y, w, rows, scale=)` — rows `{label, sub, vol, vol_sub, segments, end, right}` |
| T58 | **Paired horizontal rows** | Today against released per story (p24) | `d.paired_hrows(s, x, y, w, rows)` — `(label, sub, ref_value, ref_display, value, display)` |
| T59 | **Funnel rows** | A funnel today against with-us, a change column (p37) | `d.funnel_rows(s, x, y, w, rows, headers=)` + two `hero_number` blocks right |
| T60 | **Columns, Apex weight** | A value across states or years; estimates dashed (p33) | `d.bars(..., dashed=(i,), badge=(i, text))` — 15pt values, 10.5pt deltas, per-item fills |
| T61 | **Column walk** | A cost walk with the lever removed beside each step (p55) | `d.column_walk(s, x, y, w, h, steps)` — dicts `{label, value, display, delta, delta_display, fill, delta_fill, dashed, delta_dashed}` |
| T62 | **Stacked columns** | Pay against get by year; the bill by year and state (p28, p47, p46) | `d.stacked_columns(s, x, y, w, h, groups, col_w=, gap=)` — segments `(value, fill)` or `(value, ('dashed', line[, fill]))` |
| T63 | **KPI stack** | The three figures beside a chart (p28, p47) | `d.kpi_stack(s, x, y, w, items, val_size=, pitch=)` |
| T64 | **Share bar, Apex** | One row split to scale, values inside, the total under the right end (p46) | `d.share_bar(..., val_size=9, total=(display, unit), total_pos='below', label=)` |
| T65 | **Area block** | A population split as a proportional block (p8) | `d.area_block(s, x, y, w, h, parts, top_label=)` |
| T66 | **Donut / pie** | One share of one whole as a circle (no reference page; built to order) | `d.donut(s, x, y, d, segments, thickness=0.28, center=, legend=True)`; `thickness=1.0` = pie |
| T67 | **Team page · close** | The people in the room; the last page (summit deck p10, p11) | `d.team_page(kicker, title_runs, people)`; `d.closing_page("Thank you")` |

| T68 | **Proof ledger** | The production runs: a resolution bar per deployment, what moved it (summit deck p8) | `d.proof_ledger(s, x, y, w, rows)` — `(name, sub, value, display, what[, fill])`, bars scaled to 100 |
| T69 | **Loop matrix** | The value pools as chips on the autonomy rows: out of / on / in the loop / person only (summit deck p9) | `d.loop_matrix(s, x, y, w, pools, rows)` — pools `(key, label, blue|navy|tint|outline)`, chips sized from the font metrics |
| T70 | **Hero column** | The big number, caption and implication beside a ledger or matrix, behind a navy rule | `d.hero_column(s, x, y, number, caption, implication, num_size=75|55)` |

## Framework layer (T71–T83 — engine v5.0, 25 Sep 2026; Shyam: "stop boxing yourself in with tiles; use the
## frameworks from the BCG archive; use icons"). Structure without boxes. Sampler: `example_apex_frameworks_build.py`.

| # | Exhibit | Use when | Engine |
|---|---|---|---|
| T71 | **Vector icon** | One icon per concept, in a row, a card, a node; never decorative | `d.icon_glyph(s, name, x, y, size, color)`; `X.lucide_search("word")` picks the name from 2,118 Lucide icons |
| T72 | **Flywheel** | A loop where each step feeds the next: the operating model, a reinforcing cycle | `d.flywheel(s, cx, cy, r, steps, center=, start=)` — steps `(label, sub, icon)`; start=-60 for six steps keeps labels off the title and footnote |
| T73 | **Cascade** | Where a total comes from: root → branches → leaves, left to right | `d.cascade(s, x, y, w, h, root, branches)` — the value tree, the driver tree, the lever cascade |
| T74 | **Funnel** | Stages that narrow: leads to booked, applicants to accounts | `d.funnel(s, x, y, w, h, stages, orientation='down'|'right')` — `(label, value, display, conversion)` |
| T75 | **Zoom** | One row of a map opened up: the overview at left, the detail at right behind a lens | `d.zoom(s, x, y, w, h, items, focus, title=)` returns the detail box; fill it with icon rows, a chart, cards |
| T76 | **Value map** | The three pools with their levers and values, icons on the pools | `d.value_map(s, x, y, w, pools, total=)` |
| T77 | **Chevron flow** | A process with a direction: how a deal runs, how a call runs | `d.chevron_flow(s, x, y, w, steps, h=)` — `(label, sub, icon)` |
| T78 | **Rings** | Layers from a core outward: where the assistant sits, maturity levels | `d.rings(s, cx, cy, r, levels, label_x=, label_w=)` |
| T79 | **Stack / ziggurat** | An architecture or a moat, top to bottom, one verb per layer, a thesis each | `d.stack(s, x, y, w, layers, shape='bands'|'ziggurat', band_h=)` |
| T80 | **Hub and spoke** | One centre, many surfaces or parties | `d.hub_spoke(s, cx, cy, hub, spokes, r=, start=)` |
| T81 | **Icon rows** | Points with an icon each and no box: the antidote to tiles | `d.icon_rows(s, x, y, w, items, cols=, pitch=)` — `(icon, title, body)` |
| T82 | **Venn** | What each side brings and where the value overlaps | `d.venn(s, cx, cy, r, left, right, overlap)` |
| T83 | **Pillars** | Programmes on a foundation under one roof: a strategy frame | `d.pillars(s, x, y, w, roof, columns, base)` |

Framework laws: the claim decides the form (a loop → flywheel, a total → cascade, a narrowing → funnel, one part opened → zoom, a process → chevrons, layers → rings or stack, one centre → hub, sides and an overlap → venn, programmes on a base → pillars). Tiles and card rows carry structure only when none of these fit, and never twice in a row. One icon per concept, blue on light, white on dark, from the Lucide set by name; never an emoji, never a fabricated glyph.

Apex composition laws (from 68 measured slides): one exhibit per page and the so-what in a hero
number or a statement line; captions bottom-anchored in cards; status words drawn, not asserted
(dashed = estimate or indicative, solid = measured or committed); the client's own figures on
the page, ours in the notes; the same template repeated N times for N comparable things.

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
