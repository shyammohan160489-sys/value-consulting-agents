# Frontline 2026 — Phase 2 Backlog

New layout types to add to the Frontline 2026 Slide Engine. Each one needs implementation in:
- `presentations/backbase-slides-app/engine.js` (HTML renderer)
- `presentations/backbase-slides-app/deck-template.html` (CSS for the layout)
- `tools/frontline_slides_pptx.py` (PPTX builder method)
- `.claude/commands/frontline-slides-html.md` and `frontline-slides-pptx.md` (layout catalog docs)

Goal of Phase 2: bring HTML and PPTX outputs to visual parity, and absorb the useful components from the long-form skill so they're available to deck authors too.

## From DSD long-form integration (original Phase 2 scope)

These exist as classes in `templates/long-form/document-template.html` and need to be ported as slide layouts.

| Layout | Purpose | Source class |
|--------|---------|--------------|
| **lever-grid** | Value-driver cards for ROI / business case decks | `.lever-grid + .lever-card.sme/.blue` |
| **scenario-3up** | Conservative / Base / Upside ROI scenario columns with metric stack | `.scenario-grid + .scenario-card.conservative/.base/.upside` |
| **value-table** | Navy-header value summary table with striped rows and `.total` row | `.val-table` |
| **assumption-table** | Assumption register with confidence badges | `.assumption-row + .assumption-id + .conf` |

## From AIB v3.1 PPTX gap (added 2026-04-29)

The HTML version of AIB v3.1 used custom inline HTML bodies on several content-standard slides because no native layout existed. PPTX export collapsed them to text. These deserve to be first-class layouts:

| Layout | Reference slide | What it is |
|--------|-----------------|------------|
| **comparison-card-pair** | AIB v3.1 slide 8 (Two paths forward) | Two large cards side-by-side, each with header colour band, optional "RECOMMENDED" pill, table of attributes inside, footer outcome callout. |
| **calendar-timeline** | AIB v3.1 slide 12 (What happens next) | Vertical list of date-anchored rows (date pill left, copy right), with one row highlighted (e.g. blue background) for the current/today milestone. |
| **layered-stack** *(maybe)* | AIB v3.1 slide 5 (Banking OS layers) | 4–6 stacked horizontal bars in graduated navy → blue, each with a label tag and a description. Useful for architecture stacks and capability hierarchies. May be over-scoped — could keep as inline HTML in `content-standard`. Decide when implementing. |

## Effort sketch

- Original 4 (lever, scenario, value-table, assumption-table): ~half a day total. CSS already exists in long-form template — port logic, not visuals.
- New 3 (comparison-pair, calendar, layered-stack): ~half a day. Need fresh CSS but all are simple compositions of existing primitives.

Total Phase 2: ~1 day for both HTML and PPTX builder updates, plus skill doc updates.

## Decision rule for adding more layouts

A new layout type earns its place only if it would otherwise be hand-built ≥3 times across decks. One-off custom HTML stays as a `content-standard` body — don't bloat the engine.
