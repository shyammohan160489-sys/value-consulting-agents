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
