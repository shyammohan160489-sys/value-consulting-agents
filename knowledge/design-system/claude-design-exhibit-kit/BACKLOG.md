# Exhibit style — path to default (backlog)

*Opened 2026-07-15 (Shyam) after the BACB close deck. Maturity per the harvest ladder (example → method → template → skill → default) and Shyam's G-scale.*

**Current maturity: DEFAULT — RATIFIED 2026-07-28 (Shyam, verbal, during SNBC workshop week).** "Make this the default skill going forward — all future PowerPoint slides with this skill." The ladder is climbed: example (BACB) → template → registered skill (`.claude/skills/exhibit-slides-pptx/`) → **default for ALL PPTX on this fork** (Frontline `/frontline-slides-pptx` only on explicit request; supersedes the CLAUDE.md PPTX default here). Backlog item #5 (palette decision) resolved-for-fork the same way: exhibit palette is the default PPTX lane, no blending. Engine now v3.1: right rail standard (mirrors left, x=12.760), title law ONE line <=63 chars @25pt, `chip()` primitive, journey/workshop patterns (T16-class) in the catalog. Validated production decks: BACB close (18), SNBC VC track (37), SNBC dossiers (3), SNBC journey maps (4).

**Impact-close pattern — RATIFIED 2026-07-28 (2nd ruling of the day):** Shyam prefers the 4-up stat-card row (muted "from →" + 30pt landing value + label) with ONE navy hero-claim card, receipt lines beside it, and a "Proven here" band — over the 3-hero-tile close ("I use this one more — a lot cleaner"). Reverses the 22-Jul "too busy → simplify to hero tiles" call after a week of live room use. Codified: `d.stat_card()` + `d.proven_band()` in the engine, catalog entry replaces the proof strip (3-tile close retired to one-number-only moments), copy-source = `example_build.py` S5.

**Page numbers — LANDED 2026-07-28:** the parallel thread's mechanism (Product Factory deck, Mayur PDP session) is `<a:fld type="slidenum">` — live fields that auto-renumber on insert/reorder. Ported into the engine as `ExhibitDeck.page_field()`, styled to the existing footer spec (12.75pt bold black on the divider). Source deck archived at `Engagement/internal/vc-monetization-pdp/Input/Product_Factory_Execution_Plan_Exhibit.pptx`. Ends the hardcoded-"NN" renumbering passes of the SNBC builds.

*(Pre-default history below, kept for the record.)* One full production deck (BACB close, 18 slides, PPTX-native, Google Slides-safe) built in this language, QA'd, client-ready. Reference implementation: `Engagement/BACB/Output/build_scripts/bacb_close_exhibit_pptx.py`.

**Ratified into SKILL.md (permanent):**
- One-sentence punchline strips, one line, bold lead + regular remainder (2026-07-15).

## Edits required before "default" (the upgrade list)

| # | Edit | Why | Tier |
|---|------|-----|------|
| 1 | Extract the BACB build helpers into a reusable builder (`chrome`, `kicker_title`, `footnote`, `rich/para_block`, `oval/gate`, `strip_theme_styles`) — an `ExhibitPresenter` class beside `frontline_slides_pptx.py` | Today the language exists only as a per-deck script | **Architect** (`tools/`) |
| 2 | `strip_theme_styles` (remove `<p:style>` from every shape) as a mandatory save step | Kills theme drop-shadows in LibreOffice/Google Slides — found the hard way | with #1 |
| 3 | Codify the new patterns as T15–T19: **receipts row** (sourced stats under a claim) · **dashed = yours** half-built grammar · **scenario board** (phases × A/B bands) · **engagement plan** (session/outcome/attendees, navy finale row) · **story page** (who → problem → what we did → what it proved) | All validated on BACB; currently undocumented | knowledge (consultant OK) |
| 4 | Conventions: coral dashed badge = ILLUSTRATIVE/OUTSIDE-IN · DEFENSE lines in speaker notes on number slides · "the math, in the open" formula-table appendix | Credibility architecture that made the deck defensible | knowledge |
| 5 | **The palette decision (the real blocker).** Exhibit palette (#071224/#4066F5) ≠ Frontline tokens (#041326/#3367FF). Default status needs either (a) exhibit chrome re-skinned in Frontline tokens (hybrid), or (b) brand ratifies the kit palette for a named lane (strategy/exec decks). Decide, don't blend. | CLAUDE.md canon says Frontline is the client-facing default | **Architect + brand** |
| 6 | Standing task (pre-existing): wire adopted P1+P2 exhibits into `backbase-slides-app/engine.js` + `frontline_slides_pptx.py` | HTML/Frontline parity | Architect |

**Promotion test:** after 2–3 more decks in this language (different accounts), package #1–#4 as a registered skill and take #5 to Mayur/Shobhit as the frontline-pptx-builder-promotion playbook did.

## Round-3 upgrade — the data-exhibit layer (opened 2026-09-03, TD 1Mn-calls mining)

The TD takeout deck (36 slides, colleague-built, exact exhibit palette/chrome/fonts — XML-verified) proved the system carries full chart vocabulary; our engine just can't draw it. Root cause: `exhibit_pptx.py` has zero chart primitives, so T02/T05/T07/T09 exist on paper only and every message regresses to boxes. Full mining + specs: `EXHIBIT_MINING_ROUND3_TD.md`.

| # | Edit | Tier | Status |
|---|------|------|--------|
| 7 | Chart primitives into `exhibit_pptx.py`: `bars`, `hbars`, `line_panel`, `sparkline`, `dot_grid`, `hero_stat`, `implication_card`, `so_what_rail`, `pulse_panel`, `panel_grid`, `lane_row`, `stage_column`, `frame_band`, `ramp` (all flat shapes, Slides-safe) | Architect (fork: Shyam) | ✅ SHIPPED 2026-09-04 — engine v3.2, additive; validated 6-slide render QA'd (`scripts/example_data_build.py`) |
| 8 | Catalog T17–T23: data+so-what rail · column chart · line panels · pulse grid · double-click board · wave roadmap · dot grid codified | knowledge | ✅ SHIPPED 2026-09-04 (`references/exhibit-catalog.md`) |
| 9 | Skill rule — **form follows message**: magnitude/trend/ranking/share/distribution ⇒ drawn chart, never boxes; data slides carry the so-what rail | knowledge | ✅ SHIPPED 2026-09-04 (SKILL.md workflow §2 + catalog) |
| 10 | DECIDE: title presence — one-line @25pt vs TD-style 2-line @32–34pt | **Shyam** | ✅ DECIDED 2026-09-04: **one line always** (Shyam, verbatim: "title presence should be one line always"). The v3.1 law stands for every deck incl. data-led; the kit SKILL.md §1 two-line spec is superseded on this fork. |
| 11 | Later candidates from round 3 (not yet built): dark content SCENE slide (P5) · lever cascade (P6) · VP architecture matrix (P7) — compose from primitives today, promote to primitives after first live use | knowledge | OPEN |

**Promotion test — first live deck on v3.2 (2026-09-04):** SEB 9-Sept workshop deck (`Engagement/SEB/Output/build_seb_sept9_pptx.py`, 47 slides) now uses the data layer live: priority stack rebuilt as `hbars` + `so_what_rail` (client_idx top bar, coral tension stat, THE ASK card), market-evidence slide rebuilt as `hero_stat` 2x2 + `implication_card`. Form-follows-message audit run across the deck: remaining box slides are structure/sequence (legitimate); Everest ladder kept custom (per-band item lines hbars can't carry); ratified impact-close stat-card rows untouched. Item #10 (title law) still OPEN — deck stays on one-line @25pt pending Shyam's call.

*Promotion test for v3.2: first live data-led deck (SEB pre-read or Nedbank renewal) built on the layer, then ratify per the harvest ladder.*

## Feeding registry (opened 2026-09-04 — Shyam: "keep feeding you stuff so you can embellish yourself")

Standing sources for new exhibit vocabulary, worked in mining rounds. Status per source:

| # | Source | Yield → engine | Status |
|---|--------|----------------|--------|
| 1 | Colleague decks (TD-style drops) | Round 3 → v3.2 data layer (14 primitives) | ✅ round 3 done · STANDING — every dropped .pptx gets a mining round |
| 2 | FT Visual Vocabulary (chart-doctor taxonomy) | message-type → chart-form map; candidate source for slope, range, and distribution forms | OPEN — next round |
| 3 | MGI/BCG exhibit grammar (via round-2 mid-year mining) | `waterfall` (target walk), `paired_bars` (From→To as data) | ✅ EXECUTED 2026-09-04, v3.3 |
| 4 | IBCS attainment discipline | `bullet_bars` (per-row plan ticks, mixed units), waterfall step rigor | ✅ EXECUTED 2026-09-04, v3.3 |
| 5 | Bank investor-day grammar (JPM et al.) | KPI walk (waterfall) + `growth_arrow` (CAGR annotation) | ✅ grammar absorbed 2026-09-04; slide-level mining awaits a dropped investor-day PDF (item-1 flow) |
| 6 | Own HTML engine parity (8 data layouts from round 1) | `segbar` (bar-segmented), `quadrant`, `milestone_strip`, `hbars` (bars-sorted, v3.2), `dot_grid` (v3.2) | ✅ EXECUTED 2026-09-04 — remaining HTML-only: cohort cascade, receipts-row/scenario composites (already composable) |

| 7 | Shyam's BCG archive (1,622 screenshots, ~/Documents/BCG — images stay OUT of the repo, grammar only) | Round 4 → v3.4 evidence layer: harvey/eval_matrix, logo_chip/wall, fact_rail, leader_note, tiles, agenda_rail, ring_stat, rag_matrix, tag_chip (T30-T39) + serial-template law + 10 composable recipes | ✅ EXECUTED 2026-09-07 — every image reviewed; `EXHIBIT_MINING_ROUND4_BCG.md` |
| 8 | Same archive, STORYLINE layer (chronology = slide order = deck spines; ~15 decks reconstructed) | Round 5 → 6 storyline archetypes (Ambition Walk · Model-Bank Mirror · Landscape Read · Selection Funnel · Dossier Tour · Workshop Arc) + title grammar (flip test, quantified titles, dare-hypothesis, question-title budget) + band-beat map + question-bank shapes; operative in skill `references/storyline-patterns.md`, wired into workflow step 1. Content intel NOT mined verbatim (see row 9); §5b voice law confirmed superior, untouched | ✅ EXECUTED 2026-09-07 — `EXHIBIT_MINING_ROUND5_STORYLINE.md` |
| 9 | Same archive, INTEL layer — Shyam's ruling 2026-09-07: "I don't mind stealing proprietary intel... uplift the vintage data, form an opinion yourself" | Round 6 → **consulting-priors domain** (`knowledge/domains/consulting-priors/`): durable structures extracted as PRIORS and uplifted to 2026 house views (prior → what moved → house view → use). Tranche 1: KPI tree (+autonomy branch), per-LOB question bank (GenAI shock card), maturity scale (5th stage: AI-native), onboarding read (time-to-first-value), model-bank value drivers (client-telemetry model bank). Doctrine holds: priors never cited/named in client assets, expression rebuilt, numbers current-or-client-or-badged — tradecraft, not morality. Archive is PRE-GenAI: on CB/agentic topics our own assets already lead | ✅ TRANCHE 1 EXECUTED 2026-09-07 — tranche-2 list in the domain README |

Round-2 patterns still unbuilt as primitives (compose from primitives meanwhile): stacked-ramp+step-line pair · layer ziggurat with verb leaders · health-tier drift board · zone matrix with numbered path. Round-4 composables not yet primitives: architecture coverage shading · architecture navigator · phase matrix · funnel strip · exercise card — promote after first live use.

## Chrome exact-spec (XML-verified against BACB_Close_16Jul_ExhibitStyle.pptx, 2026-07-15)
When generating PPTX in this style, replicate these EMU-exact values (inches, 13.333x7.5):
- Hairlines: straight connectors, #D2D4D8, 0.75pt, FULL-BLEED — top (0,0.573)→(13.333,0.573); left rail (0.573,0)→(0.573,7.042); footer (0,7.042)→(13.333,7.042). Inner footnote hairline x=1.0→12.708.
- Notch: two BLUE (#4066F5) rects stepping UP into the line crossing: tall (0.490, 0.406, 0.083×0.167) + square (0.406, 0.490, 0.083×0.083). Never inverse/white-cutout.
- Footer: WHITE. Backbase logo PNG (navy wordmark) at (11.750, 7.193, 0.659×0.156) + page number 12.75pt BOLD navy at x≈12.83. No navy band.
- Kicker: 13.5pt REGULAR #4066F5 at (1.0, 0.812). Title: 28.5pt bold navy at (1.0, 1.104), full sentence WITH trailing period.
- Body scale: lane headers 21pt bold (lane colors 1F3799/4066F5/5F7DF7); labels 14.25 bold navy; body 12.75 #6A717C; "PROVEN HERE"-style micro-labels 12.75 #777D87; footnotes 12.75 #8F949C.
- Takeaway band: navy #071224 roundRect, ~11.708×0.479 at content width, text 14.25 (cyan #93FBFE bold lead-in + white regular).
- Bullets: #1F3799 ellipses 0.104. All shapes FLAT (explicit empty a:effectLst — LibreOffice adds shadows otherwise).
Lesson: build from the template/reference deck's XML, never re-derive chrome from SKILL.md prose. Reference logo asset copied to Engagement/SNB Capital/Output/backbase_logo_navy.png.

### Chrome refinements v2 (June-29 SNBC deck, Shyam-directed, 2026-07-16) — SUPERSEDES notch + footer above
- Step: ONE blue square FLUSH to the left slide edge at title level — x=0, ~0.156×0.156 in (scaled from 0.234 on the 20in canvas), vertically aligned with the title's first line. Replaces the two-piece stair at the hairline crossing.
- Footer: LARGE BLACK Backbase wordmark (~1.067×0.173 in, asset: Engagement/SNB Capital/Output/backbase_logo_black.png, cropped @300dpi from the June deck) + thin vertical divider (#9A9EA6, ~0.25 in tall) + page number 10pt bold black right of the divider. This is the "Backbase │ N" pattern.
- Keep: full-bleed #D2D4D8 hairlines, white footer, kicker/title scale, flat shapes. Optional per deck: top-right session marker.

### Chrome refinements v3 — FINAL (16 Jul, verified against BACB + June decks + Shyam round-trip test) — SUPERSEDES v2 step note
- The step is the AUTHENTIC Backbase glyph, not a plain square and not two rects: custGeom path (units w=9168 h=9096): M(19,4762) L(4567,4762) L(4566,0) L(9168,0) L(9168,9096) L(0,9096) Z — i.e. a square with its top-left quadrant removed. Draw as freeform (python-pptx build_freeform w/ scale=(w*914400/9168, h*914400/9096)); HTML: clip-path polygon(0 52.4%,49.8% 52.4%,49.8% 0,100% 0,100% 100%,0 100%).
- Position: hugging the hairline crossing — box (0.406, 0.406, 0.167 x 0.166) in, glyph corner ends exactly at (0.573, 0.573). Blue #4066F5 on white; cyan #93FBFE on dark slides.
- Page number: 12.75pt BOLD black, textbox anchored MIDDLE on the footer divider (divider: vertical hairline #9A9EA6 at x=12.802, y=7.118–7.367); number at x≈12.87. Wordmark 1.067x0.173 ends at 12.700.
- Connectors: strip the <p:style> element AND append empty <a:effectLst> — otherwise the theme effectRef re-adds a line shadow in LibreOffice/Google renders.
- Survives Google Slides round-trip (tested: geometry, freeform, PNG logo all preserved).
