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
