# Frontline PPTX — promoting the "good" builder (Schroders decision paper)

**Date:** 2026-06-09
**Author:** Shyam Mohan (Value Consulting)
**Status:** Local working-tree changes only — NOT pushed. Builder edits are architect-tier; this note is the consultant-safe record + handoff.
**Companion to:** [frontline-builder-reassessment-2026-06.md](frontline-builder-reassessment-2026-06.md) (the Pictet reassessment). Same theme — PPTX component-vocabulary fidelity — now with the answer.

---

## The discovery

The Schroders "Project Nova" decision paper is the best HTML→PPTX translation the team has produced. Reverse-engineering it revealed why: it was built by **`tools/frontline_2026_presenter.py` (`Frontline2026Presenter`)** — a mature, rich builder on the larger 20×11.25 canvas with purpose-built layout methods (`add_tiles_slide`, `add_pillar_rows_slide`, `add_process_rows_slide`, `add_financial_table_slide`, `add_bar_chart_slide`, `add_split_comparison`, `add_architecture_*`).

**The catch:** that builder powers the **deprecated** `/frontline-slides` skill (`.claude/commands/deprecated/frontline-slides.md`). The *registered* `/frontline-slides-pptx` uses the weaker `BackbaseSlidesPresenter` (the one behind the poor Pictet output). The rich vocabulary already exists — it was orphaned in the deprecated builder when the skills were "modernized."

## What the consultant fixed by hand (= the builder gaps, now closed)

Comparing the as-generated baseline against the hand-edited delivery isolated five gaps. All five are now fixed in `frontline_2026_presenter.py`:

| Hand fix | Root cause | Builder change |
|---|---|---|
| Photo cover w/ frosted-glass panel | Only a plain navy cover existed | New `add_cover_photo_slide()` + `_set_fill_transparency()` |
| Two-tone titles (key words red/blue) | Titles were single-colour | `_add_rich_title()` — `**word**` → `highlight='red'|'blue'`; wired into tiles, pillar, process, financial + cover |
| White-column stat strips (dividers, big stat) | Only grey cards + accent-bar + pill existed | `add_tiles_slide(..., style='column')` |
| Footer "N / Total" deleted | `save()` force-rewrote the number and it wrapped | `save()` no longer rewrites; footer = plain "N" |
| (invisible) off-canon colours | `#001C3D / #1A5AFF / #E02020` | Reconciled to canonical `#041326 / #3367FF / #FF503C` |

Also fixed: footer logo/number overlap (fixed-width logo); stray slide-number placeholders stripped from master + layouts at init.

**Token note to ratify:** the Schroders HTML used crimson `#DC2626` for "red"; canonical token red is coral `#FF503C`. The builder now uses canonical `#FF503C` (visibly more orange). One-line flip in `frontline_2026_presenter.py` (`SEMANTIC_RED`) if we want to pin to the HTML crimson.

## Proof

- Improved deck: `Engagement/Schroders Group/Output/decision-paper/schroders_nova_frontline_2026_v2_improved.pptx`
- Build script: `build_schroders_pptx_v2.py` (uses photo cover, two-tone titles, `style='column'` stat strips)
- Before/after PDFs: `schroders_AS-GENERATED-baseline_no-images.pdf` vs `schroders_v2-IMPROVED-builder.pdf`

The v2 deck reads very close to the hand-edited delivery without manual touch-ups (cover, stat strips, two-tone titles, pillar flow, process rows, financial table all render faithfully).

## Recommendation — how to imbibe into the skill

1. **Promote** `Frontline2026Presenter` (with these upgrades) to be the canonical PPTX builder, or repoint `/frontline-slides-pptx` at it. The richer vocabulary is what makes decks render faithfully.
2. **Ratify** the red token (`#FF503C` vs `#DC2626`).
3. **Update the skill prompt** to steer authors to the structured methods (tiles/columns/pillar/process/financial + photo cover + `**` two-tone titles) and away from raw-HTML bodies.

## Architect handoff

`tools/**` and `.claude/**` are architect-tier (CI blocks consultant PRs). All builder changes are in the working tree, proven, **not pushed** (per instruction). For Mayur / Shobhit / Mariam to review and land. The skill-registration question (which builder is canonical) is a real architectural decision and should be ratified before promotion.

<!-- TELEMETRY_START
agent: claude
task: frontline-pptx-builder-promotion
outputs:
  - knowledge/learnings/frontline-pptx-builder-promotion-2026-06.md
  - tools/frontline_2026_presenter.py (PROPOSED — architect-tier; tokens, photo cover, two-tone titles, column tiles, footer fixes)
  - Engagement/Schroders Group/Output/decision-paper/build_schroders_pptx_v2.py
  - Engagement/Schroders Group/Output/decision-paper/schroders_nova_frontline_2026_v2_improved.pptx
  - Engagement/Schroders Group/Output/decision-paper/schroders_v2-IMPROVED-builder.pdf
checkpoints: 2 (gap analysis vs hand-edited deck; visual verification across slides 1-5,10-12)
pushed: false
TELEMETRY_END -->
