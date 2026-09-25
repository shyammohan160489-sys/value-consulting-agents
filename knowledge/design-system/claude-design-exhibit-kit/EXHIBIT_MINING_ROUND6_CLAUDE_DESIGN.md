# Exhibit mining round 6 and 7 — the Claude Design look, measured and named Apex

*Round 6 opened 18 Sep 2026 (Nedbank ENBI Voice VC report). Round 7 added 24 Sep 2026 (McKinsey Africa AI Summit tech talk). Named **Apex** by Shyam on 24 Sep 2026 and made the default look for every new PPTX.*

## Round 6 · the Nedbank report (18 Sep 2026)

**Source.** `Engagement/Nedbank/Input/vc-report-18sept/Nedbank_ENBI_Voice_VC Report_18Sep26.pptx`, 68 slides, a Google Slides export of a Claude Design deck on the 13.333 × 7.5 canvas. Sixty-three slides are the export; slide 61 (the mutual plan) was built with our engine and inserted.

**Method.** Every number read from the slide XML with python-pptx: shape geometry, fills, line colours, run sizes, weights and colours, counted over the whole deck. The spec is `.claude/skills/exhibit-slides-pptx/references/visual-grammar-v4.md`.

**What the look is.** A three-rule frame (top, left, bottom, no right rail) with the step glyph in blue; a 9pt navy tracked kicker; a 28pt regular title with no trailing period; regular weight everywhere (not one bold run in 68 slides); a palette of navy `091C35`, blue `3366FF`, mid `7D9DFF`, light `C4D2FF`, tints `E5EBFF` and `F3F6F9`, grey `C9D1DC`, cyan `69FEFF` on dark, coral `FF503C` as the one warning colour; cards whose fill weight encodes a count; the so-what in a hero number or a 12pt statement line; footnotes at 8.5pt with no hairline; the client logo top right of every content slide.

**What went into the engine (v4.0).** `ExhibitDeck(look='v4')` and 26 helpers: card, card_row, lane_grid, weight_legend, stat_block, stat_grid, hero_number, mini_stat, stat_column, panel, statement_line, cover_page, divider_band, vision_band, film_frame, numbered_rows, from_to_columns, pillar_row, share_bar, step_flow, compare_rows, stacked_hbars, wave_track, option_card, numbered_card, timeline_lanes, who_signs. `scripts/example_v4_build.py` rebuilds four report pages (6, 15, 31, 61) for a side-by-side check.

**Side-by-side result (24 Sep 2026).** Pages 6 and 15 rendered next to the export: the frame, kicker, title, card fills, badges, numbers, footnote and footer match. The one visible gap was the line icons top left of the stat blocks; closed in round 7 (below).

## Round 7 · the McKinsey summit tech talk (24 Sep 2026)

**Source.** `Engagement/events/mckinsey-africa-ai-summit-2026/Input/Backbase_McKinsey_Africa_AI_Summit_TechTalk_v3.pptx`, 11 slides: a Claude Design export (slides 2, 3, 4, 8, 9 on the light frame; 1, 7, 10, 11 as cover, film, team and close) that Shyam then spruced up with the v3 exhibit engine (slides 5 and 6, dark scenes in `071224` / `4066F5` / cyan `93FBFE`).

**What it adds to the grammar.**
- Light pages carry the same frame, kicker and regular title as the Nedbank report (32pt where the title is short). Hero numbers go bigger on a stage deck: 36pt in a two-row stat grid, 55pt ("4 of 4") and 75pt ("76%") as the page's single number.
- An era timeline of navy cards climbing left to right (2010s → 2020s → 2026), a loop matrix of chips on four rows (out of the loop → person only), a "where the needle moved" ledger of bars with a big number at the right.
- Dark scenes for the stage: a navy cover with a blue mosaic image and a bold second line; a dark From → To three-column page; a dark four-solution architecture page with a Banking OS band; a full-bleed film poster; a team page with three photos; a "Thank you" close.

**Closed in the engine (v4.1, 24 Sep 2026).** The icon pack: twelve 300 px line icons lifted from the Nedbank export into `assets/icons/` (brightness, users, headset, sparkle, person, route, shield_check, document, database, check, phone, phone_incoming), reachable as `X.icon(name)` for `stat_block(icon=)`. `cover_page(title_w=)` so a long cover title wraps left of the inner rule. `tag_chip` regular weight under Apex. The `apex` alias.

**Still to build (backlog).** A dark content scene under Apex (the engine's `slide(dark=True)` is the v3 glow); an image-led cover with the mosaic; a team page with photos; a "Thank you" close; the chip loop-matrix as a recipe; no-bold engine variants of `bars`, `hbars`, `milestone_strip` and `takeaway_band` (the company-view build carries local `vbars` / `hrows` meanwhile); HTML-engine parity for the Apex recipes.

## Promotion test (the harvest ladder: example → method → template → skill → default)

First live deck on Apex: the CB enablement kit's company view, `Engagement/_enablement/conversational-banking-gtm/company-view/build_cb_company_view_apex_pptx.py`, 14 slides, built 24 Sep 2026 from the same content as the v3 build of the same day, rendered and read page by page against the v3 version and the Nedbank reference. Every page uses engine recipes (from → to columns, pillar row, state table, hero numbers, option cards, dashed cards, panels, mini-stats, numbered rows, drawn bars, step flow, card row, ladder, numbered cards, cover, divider band). Two fixes came out of the render check and went into the engine (cover title width) and the build (stacked hero captions).

**Ruling (Shyam, 24 Sep 2026):** Apex is the default for every new PPTX. v3 stays the engine default so the SNB Capital, BACB and September Nedbank build scripts render unchanged; a deck added to a series still on v3 stays v3 until the account's next cycle.

## Round 8 · the report's charts (25 Sep 2026, the chart standard)

**Source.** The 22 Sep 2026 IGNITE report (80 slides). Every chart in it is drawn from flat rectangles: no native chart objects, no pies, no line charts. Twelve chart pages measured from the XML (pages 8, 12, 24, 25, 28, 33, 37, 46, 47, 55, plus the McKinsey team page and close).

**What went into the engine (v4.2).** `legend`, `hbar_rows`, `hstack_rows`, `paired_hrows`, `funnel_rows`, `bars` in Apex weight with dashed estimates, `column_walk`, `stacked_columns`, `share_bar` with values inside and the total below, `kpi_stack`, `area_block`, `donut` (block arcs; thickness 1.0 = pie), `team_page`, `closing_page` with `assets/close_bg.jpg`, `client_logo()` reading `Engagement/<Client>/Input/brand-assets/`, and the no-bold law in `txt()` so every older helper draws regular under Apex. Catalog T56–T67. Sampler: `scripts/example_apex_charts_build.py`.

**QA (25 Sep).** Each sampler page rendered next to its reference page. First pass found five gaps and closed them: the blue code prefix on row labels, share-bar values inside with the total under the right end, doubled year labels under small stacked columns, a wrapped section label, the close's wordmark size. What still differs from the export, on purpose: the client's green brand accent (never in the engine palette), the eighth "in the contract" row on page 55, and the frame offset of the summit deck's team page (0.38 in the export, the Apex 0.573 in the engine).

## Round 9 · the two summit pages Shyam meant (25 Sep 2026)

Correction: "the second-last page and the last page" referred to pages 8 and 9 of the eleven-page file as presented, the production-runs ledger and the value-pool loop matrix, not the team page and the close. Both measured from the XML and shipped (engine v4.4): `proof_ledger` (12pt uppercase headers, navy 0.01 rules, a 2.00 × 0.11 TINT2 track with the BLUE bar scaled to 100, the 18pt value in the row's colour, the NAVY row as the one to notice), `loop_matrix` (the value-pool legend with a dashed swatch for the outline pool, 13pt row labels with 12pt muted descriptions, 0.30 chips coloured by pool that flow and wrap at 0.37, rules at 0.905 pitch) and `hero_column` (a navy vertical rule, the 75pt or 55pt BLUE number, 13pt caption, rule, IMPLICATION, 13pt body). Chip widths come from the real Libre Franklin metrics (`text_w()`, PIL over the repo TTFs; within 3% of the export's boxes). QA: sampler pages 12 and 13 next to the summit pages, two passes (values took the row colour; chip padding 0.18 as measured).

## Round 10 · the stage scale (25 Sep 2026)

Shyam, looking at the summit pages next to the engine's: "why is the font size on the new Apex much smaller... I want the Claude Design original as it's cleaner, easier to read." Measured answer: the body copy was the same 12 and 13pt on both; the difference was the chrome and the colour. The summit deck runs a larger scale than the report the engine was built from: title 32pt at 1.36 (report 28pt at 1.10), kicker 12pt at 0.97 (report 9pt), footnote 12pt (report 8.5pt), secondary text navy (report muted grey), a navy rule at 6.98 above the footer (report: the grey hairline at 7.04). The summit's type sizes: 12pt ×19 runs, 13pt ×8, 18pt values, 15pt statement, 36pt stat numbers, 55 and 75pt heroes.

Shipped as engine v4.5: `ExhibitDeck(look='apex', scale='stage'|'report')`, stage the default. Chrome, footnote and statement line switch by scale; the measured recipes multiply their type and row pitches by the deck's factor (4/3 at stage), so the same content needs more pages at stage. The summit-native recipes are stage-measured and shrink to 0.75 at report. `example_apex_stage_build.py` builds five pages at both scales for the comparison. Today's dense builds were pinned to report so nothing moved under them.
