# Engagement Journal

## 2026-07-27 — Product Factory execution plan deck (internal, PDP)

**Agent/skill:** frontline-slides-pptx session, hand-authored exhibit-style builder (per user request mid-session)
**Output:** `presentations/product-factory/Product_Factory_Execution_Plan_Exhibit.pptx` (20 slides, 109 KB) + generator `presentations/product-factory/build_exhibit_deck.py`
**Audience:** Internal — Shyam's PDP track (Mayur) + talent programme (Tim Ruttner, CMO). Not client-facing.
**Style decision:** McKinsey-exhibit patterns from `knowledge/design-system/claude-design-exhibit-kit/` rendered in Frontline 2026 tokens (`#041326` / `#3367FF`), per the 2026-07-08 adoption decision (patterns adopted; kit palette, L·E·C marker and kit chrome deliberately not). Exhibit content rules applied: action-title sentences, one exhibit per slide, source footnotes, ranges as ranges, no em dashes, one intentional table.

**Content basis:** `PDP_BACKLOG.md` (29 Jun 2026 PDP session), `knowledge/product/banking-os.md` (canon), `knowledge/design-system/narrative-spine.md`, `knowledge/domains/apa-matrix/README.md` (APA V3).

**Consultant checkpoints:**
1. Pre-generation — format confirmed with consultant (PowerPoint), style corrected mid-turn to exhibit style on consultant instruction.
2. Post-generation — all 20 slides visually verified via LibreOffice render; two layout defects found and fixed (milestone-strip edge clipping, roadmap bar-label overflow).

**Assumptions (all explicit, on slide 19 of the deck):** team cost ~€1.2M/yr (LOW — validate Mayur/finance) · effort estimates ±30% (MEDIUM — recalibrate on first build) · SE 0.5 FTE available (LOW — validate SE leadership) · tickets €15–100K clear the market (MEDIUM — first 3 deals) · wedge→Mission attach ≥50% in 6 months (LOW — pilot cohort).

**Evidence tracing:** AIB ~€80K ADS reference, gain-share benchmarks (ProsperOps/nOps/Vantage), SAP/ServiceNow success-plan anchors, cost-model n=2 — all from PDP session record in `PDP_BACKLOG.md`. Factory toolchain and value pools from `banking-os.md`.

<!-- TELEMETRY_START
agent: frontline-slides-pptx (bespoke exhibit renderer)
engagement: internal-pdp-product-factory
deliverable: Product_Factory_Execution_Plan_Exhibit.pptx
slides: 20
checkpoints: 2
assumptions_documented: 5
evidence_sources: PDP_BACKLOG.md, banking-os.md, narrative-spine.md, apa-matrix/README.md, claude-design-exhibit-kit/SKILL.md
generated: 2026-07-27
TELEMETRY_END -->

## 2026-07-27 — Product Factory deck v2: Master Template chrome (SNB-format redo)

**Change:** Rebuilt the deck chrome to match the Backbase Master Template 2026 (the format of the latest SNB deck): stepped-square brand mark at hairline crossings (geometry extracted from the master's layout XML — custGeom, 0.25in, `#3367FF` light / white dark), full-height rails at master positions (0.58"/19.42" content, 0.83"/19.17" cover), master margins (content x=54px vs 96px before), cover/chapter grid with crossing lines. Logo size unchanged (validated by consultant). Page numbers converted from hardcoded text to real `slidenum` fields — auto-renumber in PowerPoint and Google Slides on insert/reorder, making the deck co-creation safe.

<!-- TELEMETRY_START
agent: frontline-slides-pptx (bespoke exhibit renderer v2)
engagement: internal-pdp-product-factory
deliverable: Product_Factory_Execution_Plan_Exhibit.pptx (v2, master chrome)
slides: 20
checkpoints: 2
modification_source: consultant feedback (stepped squares missing, margins off, hardcoded page numbers)
generated: 2026-07-27
TELEMETRY_END -->
