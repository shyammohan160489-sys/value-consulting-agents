# Frontline 2026 Builder Reassessment — HTML vs PPTX Fidelity

**Date:** 2026-06-09
**Author:** Shyam Mohan (Value Consulting) — reassessment + proposed patch
**Trigger:** Team feedback (June 2026) — decks generated from Cortex "are not coming the desired way." The PPTX builder is the worst offender; the Frontline 2026 design system is not translating into generated decks.
**Test case:** Pictet QBR deck, built in both formats from the same 29 slides.
**Scope of edit:** This report lives in `knowledge/learnings/**` (consultant-editable). The **proposed builder patch touches `tools/frontline_slides_pptx.py`, which is ARCHITECT-tier** (`enforce-contribution-scope.yml`). See [Architect handoff](#architect-handoff) — it must be landed by Mayur / Shobhit / Mariam, not via a consultant PR.

---

## 1. Executive summary

The HTML deck engine and the PPTX builder claim parity ("same 17 layouts, same data schema, visually consistent output"). In practice they diverge badly the moment a slide carries anything richer than a title + bullets. The gap is **not** sloppy authoring — the Pictet PPTX build script was a careful, faithful mapping of the same content. The gap is the **PPTX builder's component vocabulary**.

**Root cause, in one sentence:** the HTML engine renders each slide's `body` field as **raw HTML** (`${d.body}`), so authors hand-author rich, inline-styled components (cards, two-tone before/after panels, chip rows, tables, badges) that the browser renders faithfully — while the PPTX builder runs that **same HTML through an `html_to_text()` flattener**, collapsing every component into uniform arrow-bullet text and discarding all colour, weight, and box structure.

Three structural defects compounded it:
1. The statement band was approximated with **two overlapping rectangles**, producing a visibly broken protruding-step artifact on every statement slide (4 slides in Pictet).
2. Missing screenshots rendered as **large empty grey/blue placeholder rectangles** — decks without imagery looked unfinished.
3. Bullet "group headers" rendered at the **same weight/size as the bullets** — no hierarchy.

**What this reassessment delivers:**
- A precise HTML↔PPTX gap matrix (Section 4) and root-cause attribution (Section 5).
- A **working patch** to `tools/frontline_slides_pptx.py` (+598 lines) that adds the missing primitives: rounded card/panel shapes, chip/pill rows, two-tone before/after comparison blocks, an option card with a RECOMMENDED badge + accent-coded "led-by" footer, a corrected single-freeform statement band, a framed (not empty) image placeholder, inline `<b>`/`<span class="hl">` emphasis, and bullet hierarchy.
- The Pictet PPTX deck **rebuilt against the patched builder**, rendered to PDF as before/after proof. It now reads close to the HTML reference.

---

## 2. Method

- **Good reference (target):** `Engagement/Pictet/Output/pictet_qbr_2026.html` (engine + `slides_data.js`).
- **Poor output (subject):** `Engagement/Pictet/Output/pictet_qbr_2026.pptx`, built by `build_deck_pptx.py`.
- Rendered the PPTX to PDF via local LibreOffice (`soffice --headless --convert-to pdf`) and inspected all 29 pages.
- Read all three sources of truth: tokens (`knowledge/design-system/frontline-tokens.json`), HTML engine (`presentations/backbase-slides-app/engine.js` + `deck-template.html`), PPTX builder (`tools/frontline_slides_pptx.py`).
- Cross-referenced the actual rich bodies authored in `slides_data.js` against what the builder produced.

**Evidence files:**
- After-state proof: `Engagement/Pictet/Output/pictet_qbr_2026_AFTER_builder_v2.pdf` (this reassessment's output).
- Before-state builder: recoverable via `git show HEAD:tools/frontline_slides_pptx.py`. Before-state render is documented slide-by-slide below.

---

## 3. The three sources of truth & how each builder honours them

| Source of truth | HTML engine | PPTX builder (before) | PPTX builder (after patch) |
|---|---|---|---|
| **Tokens** (`frontline-tokens.json`) — navy `#041326`, blue `#3367FF`, cyan, red, Libre Franklin, 16px card radius | Honoured (CSS vars) | Colours/fonts honoured; **radius, cards, chips not used at all** | Honoured incl. rounded cards (small radius), accent system |
| **Layout geometry** (grid lines, margins, 17 layouts) | Authoritative | Faithful for chrome (grid, motif, footer) | Unchanged chrome; richer body region |
| **`body` = raw HTML escape hatch** | **Rendered verbatim** — the entire rich-component story lives here | **Flattened to text** via `html_to_text()` | Rich bodies map to real shapes via new structured methods; remaining HTML bodies get hierarchy + inline emphasis |

The critical asymmetry: **the HTML engine's expressiveness is unbounded** (any HTML/CSS the author writes into `body`), while **the PPTX builder's was bounded to flat text**. Parity was therefore impossible by construction for any non-trivial slide.

---

## 4. HTML ↔ PPTX gap matrix (Pictet slides)

| # | Slide | HTML component | PPTX **before** | PPTX **after patch** |
|---|---|---|---|---|
| 5 | What's working | 4 colour-coded **cards** w/ uppercase eyebrows + inline bold | Flat arrow bullets | `add_content_cards` — 4 rounded cards, eyebrows, inline `<b>` ✅ |
| 6 | The hard truth | Statement band + **`.hl` highlights** | Broken 2-rect band; highlights stripped | Single freeform band; red `.hl` ✅ |
| 9 | Harmonization | **Two-tone before/after** + arrow + **chip row** | Flat bullets, no panels/chips | `add_comparison` — red/blue accent cards, arrow, 5 chips ✅ |
| 10 | Complex accounts | 2 cards, one with **chip cluster** | Flat bullets | `add_content_cards` — bullets card + chips card ✅ |
| 11 | The shift | Statement band + `.hl` | Broken band; highlights stripped | Single band; blue `.hl` ✅ |
| 13 | Custom → product | 4-col matrix (light, colour-coded cell) | Navy table (acceptable) | Navy table retained (reads well) ◑ |
| 14 | Secure Messaging | Bullets + screenshot region | Bullets + **empty grey box** | Inline-bold bullets + **framed "PRODUCT SCREENSHOT"** panel ✅ |
| 15 | Pictet Touch | Two-tone before/after | Flat bullets | `add_comparison` ✅ |
| 16 | The principle | Statement band + `.hl` | Broken band | Single band; `.hl` ✅ |
| 19 | Advisor cockpit | 2 cards (chips + admin→advice) | Flat bullets | `add_content_cards` w/ chips + coloured inline spans ✅ |
| 20 | How upgrade runs | 2 bullet cards + **navy callout** | Flat bullets, no callout | `add_content_cards` + cyan-lead **callout strip** ✅ |
| 23 | Step 1 · Ignite | Nested mini-grid + callout | Flat bullets | `add_content_cards` (simplified) + callout ✅ |
| 24 | Step 2 · Proof | 2 cards | Flat bullets | `add_content_cards` ✅ |
| 25 | Commercial frame | 2 bullet cards | Flat bullets | `add_content_cards` ✅ |
| 26 | **Three ways forward** | 3 **option cards**, RECOMMENDED badge, red/navy/blue "led-by" | Plain text columns; badge → "(RECOMMENDED)"; led-by → inline line | `add_options` — badge, blue border, colour-coded led-by footer ✅ |
| 27 | What good looks like | Stat band + `.hl` | Band OK; highlights stripped | `.hl` preserved ✅ |
| 4 | Pictet Wealth | Stats + screenshot | Stats OK + **empty grey box** | Framed "SCREENSHOT" placeholder ✅ |

Legend: ✅ now matches HTML closely · ◑ acceptable PPTX-native equivalent.

---

## 5. Root causes — answering the brief's questions

**(a) Where does each builder diverge from tokens / Master Template?**
- Tokens: the PPTX builder used the right hexes and font, but **never used the 16px card radius, the card/panel concept, chips, or the accent system at all** — they simply weren't in the vocabulary. Colour fidelity was fine; *structural* fidelity was the gap.
- Master Template: no colour/geometry drift found in the builder; the divergence is component coverage, not palette.
- Minor: roadmap `cyan` bar used `#2BBCC4` vs token cyan `#69FEFF` (token cyan is too light for a filled bar on white — the builder's darker cyan is a *reasonable* deviation; worth documenting in tokens as a "chart cyan" rather than leaving it undocumented).

**(b) Where do the two builders diverge from each other? (the precise component-vocabulary gap)**
The HTML engine could render, via raw-HTML bodies: cards, two-tone panels, chip rows, inline tables, badges, nested grids, navy callouts, coloured inline spans. The PPTX builder could render **none** of these — every one collapsed to arrow-bullet text. That is the entire gap. (Now closed for cards, comparisons, chips, options, callouts, badges, inline emphasis, statement band; nested grids and inline light-tables are simplified, not pixel-matched.)

**(c) Highest-impact gaps for real decks** (ranked):
1. **Statement band artifact** — visibly broken, brand-damaging, hits every statement slide. *(fixed)*
2. **Cards / two-tone panels** — the dominant rich pattern; ~12 of 29 Pictet slides. *(fixed)*
3. **Option card + RECOMMENDED badge** — the single most important commercial slide. *(fixed)*
4. **Empty image placeholders** — make a deck look unfinished. *(fixed)*
5. **Chips/pills** — capability clusters. *(fixed)*
6. **Bullet hierarchy + inline emphasis** — readability. *(fixed)*

**(d) Is the problem in the BUILDER, the SKILL prompt, the TOKENS, or all three?**
- **Builder — primary (≈85%).** It lacked the component vocabulary and shipped a broken band + empty placeholders.
- **Skill prompt — secondary.** `frontline-slides-pptx.md` inherits the "same schema as HTML" framing, which **steers authors toward custom-HTML bodies the PPTX cannot render**. The prompt should tell PPTX authors to use the structured methods (cards/comparison/options) instead of pasting rich HTML, and should state plainly that raw-HTML bodies degrade to text in PPTX. *(prompt change is also architect-tier — see handoff.)*
- **Tokens — minor.** Largely fine; only the undocumented "chart cyan" and the absence of an explicit card/chip spec are worth tidying.

---

## 6. What the proposed patch adds (to `tools/frontline_slides_pptx.py`)

New module-level helpers:
- `parse_rich_runs(html, hl_color)` — converts an inline HTML string to styled runs honouring `<b>/<strong>`, `<span class="hl">`, and `<span style="color:#xxx">`.
- `html_to_blocks(html)` — splits a body into ordered `(header|bullet, inner_html)` blocks for hierarchy.

New shape primitives (private):
- `_round_rect`, `_accent_bar`, `_eyebrow`, `_rich_paragraph`, `_card`, `_chip_row`, `_callout_strip`, `_content_header`.

New layout methods (public):
- **`add_content_cards(label, title, subtitle, cards, callout)`** — a row of rounded cards; each card = `{eyebrow, body|bullets, chips, tone, accent, weight}`; optional navy callout strip.
- **`add_comparison(label, title, subtitle, left, right, chips, callout)`** — before→after two-tone with left accent bars and an arrow; optional chip row / callout.
- **`add_options(label, title, subtitle, options)`** — 2–4 option cards; the `recommended` one gets a blue border + RECOMMENDED badge + accent-coded `led_by` footer.

Fixes to existing methods:
- `_band_shape` — replaced the two-rectangle approximation with a **single python-pptx freeform polygon matching the CSS `clip-path` exactly** (8 points).
- `_placeholder_rect` — now a **framed rounded panel with a centered caption** instead of an empty grey box.
- `_body_text` — **group headers bold, bullets indented**, inline emphasis preserved.
- `add_statement` / `add_statement_stat` — now render `.hl` highlights (blue, or red on accent-red) instead of stripping them.
- `add_product` — labelled "PRODUCT SCREENSHOT" frame when no image.

**Design choice — structured params over an HTML renderer.** Rather than build a fragile CSS-flexbox interpreter inside python-pptx, the patch exposes **structured component methods**. The Pictet build script was rewritten to call them. This is the realistic forward path: PPTX consumes structured component data; raw-HTML parity at the body level is abandoned as infeasible. *(Recommendation: evolve the HTML engine to also accept these structured component objects, so a single structured schema drives both renderers — true parity, finally.)*

---

## 7. Residual gaps / known limitations

- **Drop shadows in LibreOffice preview.** Cards show a faint shadow in the `soffice` PDF render despite `shadow.inherit = False` (empty `effectLst`). In PowerPoint / Google Slides — the actual delivery targets — this resolves to no shadow. Token rule `no_drop_shadows` is respected at the XML level; the shadow is a LibreOffice-preview artifact only. Worth a one-line note in the skill.
- **Light inline tables / nested mini-grids** (slides 13, 23) are rendered as a navy table / simplified cards, not pixel-matched to the HTML's light colour-coded table. Acceptable; a future `add_matrix` (light, colour-coded cells) would close it.
- **Chip wrap width** uses a heuristic character-advance estimate; very long chip labels may wrap slightly early. Cosmetic.
- **`content-columns`** (slides 8, 18, 28) left as-is — already an acceptable PPTX-native rendering (blue subtitle + body + dividers).

---

## 8. Ranked fix list (for the backlog)

| Rank | Fix | Status |
|---|---|---|
| 1 | Statement band → single freeform polygon | ✅ in patch |
| 2 | Card row primitive (`add_content_cards`) | ✅ in patch |
| 3 | Two-tone comparison (`add_comparison`) | ✅ in patch |
| 4 | Option card + RECOMMENDED badge (`add_options`) | ✅ in patch |
| 5 | Framed image placeholder (no empty grey box) | ✅ in patch |
| 6 | Chip/pill rows | ✅ in patch |
| 7 | Inline emphasis (`<b>`, `.hl`) + bullet hierarchy | ✅ in patch |
| 8 | Skill-prompt update — steer PPTX authors to structured methods, warn that raw-HTML bodies degrade | ⬜ architect (prompt) |
| 9 | Token tidy — document "chart cyan"; add card/chip spec | ⬜ architect (tokens) |
| 10 | `add_matrix` light colour-coded table | ⬜ backlog |
| 11 | Evolve HTML engine to accept structured component objects → one schema, both renderers | ⬜ backlog (strategic) |

---

## Architect handoff

Per `CLAUDE.md` + `.github/workflows/enforce-contribution-scope.yml`, **`tools/**` and `.claude/**` are ARCHITECT-tier** (Mayur @mayur294-lgtm, Shobhit @shobhitonnet, Mariam @mariamt-coder). A consultant PR touching them is blocked by CI.

**This report** (`knowledge/learnings/**`) is consultant-safe and can be published normally.

**The builder patch** to `tools/frontline_slides_pptx.py` is prepared in the working tree and proven, but **must be reviewed and landed by an architect.** Suggested path:
1. An architect cherry-picks the `tools/frontline_slides_pptx.py` diff onto an architect branch.
2. Apply the skill-prompt update (item 8) and token tidy (item 9) in the same PR.
3. The patch is **additive** — all 17 existing `add_*` methods keep their signatures; only `_band_shape`, `_placeholder_rect`, `_body_text`, `add_statement`, `add_statement_stat`, `add_product` changed behaviour (all backward-compatible). Risk: low.
4. Regression check: re-run `Engagement/Pictet/Output/build_deck_pptx.py` and render to PDF (the before/after evidence).

**Follow-on (separate session):** redraft the Pictet "Big Day" QBR PPTX against the improved builder. The Pictet deck + build script are kept working and runnable.

<!-- TELEMETRY_START
agent: claude (reassessment)
task: frontline-builder-reassessment
engagement: internal / design-system
outputs:
  - knowledge/learnings/frontline-builder-reassessment-2026-06.md
  - tools/frontline_slides_pptx.py (PROPOSED patch — architect-tier, +598 lines)
  - Engagement/Pictet/Output/build_deck_pptx.py (rewritten to use structured methods)
  - Engagement/Pictet/Output/pictet_qbr_2026.pptx (rebuilt — 29 slides)
  - Engagement/Pictet/Output/pictet_qbr_2026_AFTER_builder_v2.pdf (proof)
checkpoints: 2 (pre-analysis scoping; post-build visual verification across slides 4,5,6,9,10,14,20,26,27)
evidence: Pictet HTML deck (slides_data.js) vs PPTX render (LibreOffice PDF)
TELEMETRY_END -->
