# Exhibit mining — round 4: the BCG archive (Sept 2026)

**Source:** Shyam's personal photo archive of his past BCG work — 1,622 screenshots across 28 folders (`~/Documents/BCG/`, NOT copied into this repo). Every image was reviewed (136 contact sheets + full-res deep dives). **Provenance rule:** per the standing no-McK/BCG-lineage rule, no BCG content, text, branding, or client data enters this repo or any deck; what is codified here is layout grammar only, re-expressed in exhibit tokens (navy/blue/coral, Libre Franklin). BCG green semantics map to: good/covered = BLUE family, tension/gap = CORAL, neutral = TINT/TINT2. Never green.

## What the archive teaches (the three meta-lessons)

1. **Whitespace is the chrome.** BCG slides are mostly white space with small, precise ink. Density comes from repetition of small uniform units (tiles, chips, dots), never from big filled shapes. Our engine already believes this; the archive proves it at 1,600-slide scale.
2. **Repeatable per-item templates beat bespoke slides.** The archive's power is serial templates: one dossier per player, one profile per vendor, one detail page per pillar, the same agenda rail re-shown with the active chapter lit. Decks feel "designed" because slide N+1 keeps slide N's promise.
3. **Evidence glyphs carry judgment compactly.** Harvey balls, plan ticks, RAG cells, ring stats, logo-as-data-point: one glyph = one verdict, arrayed in ledgers. This is how 10-vendor × 5-criteria judgments stay readable.

## Patterns codified into the engine (v3.4)

| # | Pattern | Anatomy (exhibit tokens) | Engine call |
|---|---------|--------------------------|-------------|
| T30 | **Harvey ball** | Quarter-step pie 0/¼/½/¾/full; BLUE on TINT2 ring; ~0.30in in ledgers | `d.harvey(x,y,d,frac)` |
| T31 | **Evaluation matrix** | Column headers = vendor logo chips (or clean-text names), rows = criteria w/ glyph+label left rail, harvey per cell, hairline row rules, legend row, ONE summary row allowed (score chips) | `d.eval_matrix()` |
| T32 | **Logo chip + logo wall** | White card, HAIR border 0.75, centered logo image (or 12pt bold navy text fallback), optional 9.5 caption; wall = grid w/ optional group headers + count chips | `d.logo_chip()`, `d.logo_wall()` |
| T33 | **Fact rail (dossier spine)** | Icon-square (TINT rounded, bold BLUE monogram) + bold navy label + regular value, 0.5-0.6in pitch; the left third of a player dossier | `d.fact_rail()` |
| T34 | **Leader note** | Dashed HAIR connector from subject to a 2-4 line note (10.5 MUT, bold navy lead); the floating-annotation grammar of dossiers and product shots | `d.leader_note()` |
| T35 | **Tile grid** | Uniform TINT2 cards, 0.035 accent top bar, bold navy title, MUT body, optional BLUE bold footer stat; 3-5 per row, equal heights, 0.12 gaps | `d.tiles()` |
| T36 | **Agenda rail / tracker** | Numbered rows; active = BLUE chip + navy bold, inactive = TINT2 chip + MUT; re-shown at each chapter with the active row moved | `d.agenda_rail()` |
| T37 | **Ring stat** | Outlined circle (BLUE 2.5pt, no fill), 20-24pt bold value inside, caption below; row of 3-5 = the proof strip | `d.ring_stat()` |
| T38 | **RAG coverage matrix** | Rows × vendor cols; cell = rounded chip: BLUE=covered, BLUE4=partial, CORAL=gap, TINT2=n/a, optional 8.5 label in cell; legend row mandatory | `d.rag_matrix()` |
| T39 | **Status tag** | Top-right uppercase chip: ILLUSTRATIVE / PRELIMINARY / NOT EXHAUSTIVE / BACKUP; coral outline (honesty) or TINT2 (backup) — extends the coral-badge credibility convention | `d.tag_chip()` |

## Patterns documented for composition (no new primitive needed)

- **Player dossier one-pager** — flag/market chip + logo top-right + `fact_rail` left + product visual center with `leader_note`s + "Partnerships"/"Works with" `logo_wall` right rail. Recipe in `example_bcg_build.py` S1. For competitive/vendor/market decks (BOV super-app RFP, CB landscape, profile-bank).
- **Vendor profile 4-up** — 2×2 of mini-profiles: name chip, 4-5 harvey-scored dimensions, 2-3 bullets each. Compose from `logo_chip` + `harvey` + `txt`.
- **Architecture coverage shading** — block diagram where each block is chipped BLUE/BLUE4/CORAL by coverage (the "color the architecture by OOTB fit" device). Compose from `rect`+`chip`; killer for Backbase OOTB vs custom conversations.
- **Architecture navigator** — mini stack map repeated top-left per slide with the in-focus zone in BLUE, rest TINT2 (breadcrumb for solution-design series). Compose from `rect`.
- **Phase × activity matrix** — phase columns with intensity-ramp headers (BLUE2→BLUE4), Key activities / Deliverables rows.
- **Funnel strip** — N stages left→right with counts in ring stats and darkening fills (`ramp('time')`).
- **Press/credential wall** — media or client `logo_wall` + quote chips; anonymise per repo rules when client-facing.
- **Journey teardown kit** — stat intro card (fields/time/days ring stats) + screen-by-screen flow pages with `leader_note`s.
- **Exercise card (workshops)** — Objective band + Exercise/Hints/Output 3-column with icon chips + timing chips; maps onto ignite-cb session decks.
- **Two-column From→To ledger** — icon rows, From (MUT) vs To (bold navy/BLUE) columns; pairs with `paired_bars` when numeric.

## Rules refined (ratified by the ask itself, note the tension resolved)

- **Logos on slides:** market/vendor/ecosystem logos ARE allowed on landscape, evaluation and dossier exhibits (that is the point of T31/T32) — supplied as image assets per deck, `logo_chip` falls back to clean text when no asset exists. The existing rule stands for the CLIENT's own account name in client decks: clean text, never their logo. Never fabricate a logo.
- **Serial-template law:** when a deck profiles N comparable things (players, vendors, journeys, pillars), use ONE template slide and repeat it N times. Do not redesign per item.
- **Whitespace law:** tiles and ledgers over filled panels; if a slide needs a big filled shape to feel done, the content is thin — cut the shape, not the whitespace.

## Deliberately NOT taken

BCG green (palette locked) · 3D/isometric blocks and metal-texture tier chips (off-idiom) · photo-heavy dividers as default (our dark dividers stay; photo optional per deck) · icon fonts as a dependency (monogram squares suffice; real icons only when a deck ships assets) · multi-hue accent headers (one accent family + coral, per palette law).

**Validation:** `scripts/example_bcg_build.py` (6 slides, render-QA'd). Feeding registry updated (BCG archive = item 7, executed).
