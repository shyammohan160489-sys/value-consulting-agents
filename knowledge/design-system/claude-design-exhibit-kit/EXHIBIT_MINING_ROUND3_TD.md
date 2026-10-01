# Exhibit mining — round 3: the TD 1Mn-calls deck (Sept 2026)

**Source:** `knowledge/domains/conversational-banking/inputs/TD-1mn-calls-takeout-2026.pptx` (36 slides, colleague-built, Aug 2026). Content digest lives at `knowledge/domains/conversational-banking/td-1mn-calls-takeout-aug2026.md` 🔒 — this file mines the **design language only**.

## Verdict first

This deck IS the exhibit system — XML-verified: palette exact (#071224 navy, #4066F5 blue, #5F7DF7/#B5C1F1 tints, #93FBFE cyan on dark, coral for tension), Libre Franklin, hairline chrome with the step glyph at the crossing, `Backbase │ N` footer, kickers with section numbering, action-sentence titles with periods, source footnote on every numeric slide, one exhibit per slide. Zero native PowerPoint charts: **every bar, line and sparkline is drawn shapes** — rects, freeform polylines, textbox labels. Nothing in it is outside our engine's reach; the gap is vocabulary, not system.

**Why our decks come out boxy:** `exhibit_pptx.py` has 18 primitives and not one of them draws data (`rect, oval, diamond, chip, stat_card, takeaway_band, …`). The catalog names chart patterns (T02 sorted bars, T05 bubbles, T07 cascade, T09 dot grid) but the engine can't produce them without per-deck EMU arithmetic, so under deadline every message regresses to chips and boxes. The TD builders paid that arithmetic by hand; we pay it once, into the engine.

## The portable patterns (build order)

### P1 · Data slide with a so-what rail — the workhorse (slides 5, 6, 7)
Exhibit left ~62% of content width. Right rail: 2–3 **hero stats** (number 48–72px light, a short vertical tick bar in the stat's color at its left, 2-line caption below) stacked over an **IMPLICATION card** (navy, cyan uppercase label, 3–5 lines white, ~radial glow). The rail is why every data slide lands: chart = evidence, rail = so-what. Coral tick + coral number when the stat is the tension (290K calls still arrive).

### P2 · Shape-drawn column chart (slides 5, 6)
Bars as flat rects on an axis hairline. Value labels ABOVE bars (24–28px bold navy), secondary delta labels under them (+0.67M, 18px muted), category labels under the axis. No y-axis, no gridlines — labels carry the values. Fill logic: **intensity ramp** (#B5C1F1 → #4066F5) left-to-right for time series ("the base solidifies"), or saturated-first for ranked magnitude (= T02's law). Highlight bar = full #3355F5/#4066F5 with blue value label.

### P3 · Line panel (slide 7)
Freeform polyline on a baseline, month ticks only. Series label sits ON the panel top-left (bold, series color). Peaks/troughs annotated: dot + bold value + a *phrase* ("63.8K · record clicks on fewer impressions…"). Two stacked panels for two series beats one cluttered dual-axis chart.

### P4 · Sparkline pulse grid (slide 11)
Grid of micro-cards (18 on the reference): label + 4-point sparkline + range caption ("69.8K – 109.4K a day"). Card top-bar color codes the theme (blue = day job, coral = friction, dark navy = growth). Below: 3–4 takeaway callouts with left tick bars; then a full-width navy IMPLICATION band. The "we have live telemetry" slide — instant operational credibility.

### P5 · Dark scene slide (slide 13)
Full navy + radial blue glow for the ONE conceptual pivot mid-deck (today→tomorrow operating model). Boxes hairline-outlined, active steps solid #4066F5, coral outline for the pain box, cyan kicker. We have dark dividers (T14); this is a dark *content* scene — use at most once or twice per deck.

### P6 · Numbered lever cascade (slide 15)
Dark model band on top (name + mode chips top-right, uppercase scope line), thin connectors dropping to 4 cards: oversized numeral (60px+ blue), lever name, one-sentence promise, hairline, "drains · X" tag. Card top-bars ramp in intensity 1→4. The "how the machine works" slide.

### P7 · Value-prop architecture matrix (slide 17)
Left row-header rail (JOURNEY · CUSTOMER PROMISE · PERSONAS · USE-CASE STRATEGIES · ATTRIBUTION), 4 lever columns. Quote row in bold ("Get me in without making it a project."), persona chips (outlined pills), strategy blocks (blue bold lead + 18px explainer), bottom navy band with cyan ≈ranges per column. The one-pager architecture — dense, but reads top-to-bottom like a sentence per column.

### P8 · Double-click stage board (slides 19, 21)
Dashed OPPORTUNITY band top → 4–5 stage columns (tint cards, numbered plays, product codes bold-coded inline: **RI** senses · **CB** delivers) → dark Solution rail right (product blocks + cyan chain arrows: Sense → rank → trigger → learn) → dashed VALUE band bottom. One board per lever; the suite structure for use-case sections.

### P9 · Swimlane wave roadmap (slide 24)
Dark lane headers left (product + one-line role), wave columns with headers ("after the pilot proves the lift"), use-case chips carrying lever tags, per-wave value callouts in blue, coral gate diamonds ON the bottom axis with gate names. Beats T04's plain gantt for capability roadmaps.

### P10 · Appendix step-table + date chip (slide 30)
Numbered rows: bold name + uppercase stage sublabel left; right cell an inline chain — **Moment** … → **RI** … → **CB** … → **Outcome** … (bold key terms only). Yellow "NEW · AUG 25" corner chip = versioning device for living decks.

## Two deltas that are philosophy, not vocabulary (decide, don't drift)

1. **Title presence.** TD runs ~34–38px titles wrapping to 2 lines. **DECIDED 2026-09-04 (Shyam): one line always** — the v3.1 law (ONE line ≤63 chars @25pt) stands for every deck; the kit §1 two-line spec is superseded on this fork.
2. **Where the so-what lives.** Our decks put it in the takeaway band (bottom, full width, one line). TD puts it in the rail card (right, 3–5 lines) AND sometimes a band. Rail card carries more reasoning per slide without breaking the one-exhibit law. Recommend: rail card default on data slides, band reserved for the punchline moments.

## What we keep (our discipline is ahead in places)

- One-line takeaway-band law: two TD slides break at render (title collides with band on 15; implication text clips on 9). Our overflow laws exist because of exactly this.
- Speaker-notes DEFENSE lines, "math in the open" appendix, coral ILLUSTRATIVE badges — TD has none of that credibility architecture.
- Voice rules (§5b): TD copy is strong but occasionally em-dashed and triadic; ours stays.

## Engine upgrade list (Phase 1 — pays the whole debt)

Add to `exhibit_pptx.py`, all flat shapes, Google-Slides-safe like existing primitives:

| Primitive | Draws | Feeds patterns |
|---|---|---|
| `bars(cats, vals, deltas=None, ramp='time'\|'rank', hi=None)` | P2 column chart on axis hairline | T02, P1 |
| `line_panel(points, label, annotations=[])` | P3 polyline + peak notes | P1 |
| `sparkline(points, w, h, color)` | micro trend line | P4 |
| `hero_stat(num, caption, color)` | number + tick bar + caption | P1 rail |
| `implication_card(text, w, h)` | navy so-what card, cyan label | P1, P4 |
| `panel_grid(cells, cols)` | micro-card grid w/ themed top-bars | P4 |
| `lane_row(header, chips)` | dark lane header + chip row | P9 |
| `stage_column(n, title, plays)` | numbered tint column | P8 |

Then catalog entries T17–T23 (P1→P9 above), and one composition rule into SKILL.md §4:

> **Form follows message:** if the slide's claim is a magnitude, trend, ranking, share or distribution, the exhibit MUST be a drawn chart (T02/T17/T18-class) — never boxes. Boxes are for structure, sequence and quality comparisons. Every chart slide carries the so-what rail unless it ends in a punchline band.

**Promotion test:** build the next live data-led deck (SEB pre-read or Nedbank renewal) with the new layer; ratify per the harvest ladder.
