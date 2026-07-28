# Engagement Journal — VC Monetization PDP (internal)

**Engagement:** VC function monetization · Product Factory (Engine A) + AI-Native Services (Engine B)
**Type:** Internal — PDP track (Mayur) + talent programme (Tim Ruttner). Not client-facing.
**Folder:** `Engagement/Internal/vc-monetization-pdp/` · deliverables in `Output/`
**Related sources:** `PDP_BACKLOG.md` (repo root) · `knowledge/product/banking-os.md` · `knowledge/domains/apa-matrix/` · `.claude/skills/exhibit-slides-pptx/`

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

## 2026-07-27 — Product Factory deck v3: full execution content + critique (41 slides)

**Change:** Extended from 20 to 41 slides on consultant direction. Added: ladder↔lifecycle bridge slide (resolves the rung-to-stage mapping); artifact chain with 4 account-level decision gates; "one wedge, four lenses" (answer to "why would a bank buy one layer"); Engine A + Engine B two-engines slide with the sequencing rule (Engine B never sells cold — runs on Engine A evidence); per-product deep-dives (activities/entails/outcomes/adds-up) and illustrative sample-output exhibits for all four products (leakage heatmap, integration landscape map, Mission card, ontology coverage map, truth-gap report, Nexus blueprint, authority map, guardrail rule card, Sentinel readiness score, cost-per-outcome tiles, waste register, ROI re-proof); Engine B block (AI Maturity, Workforce Optimization, AI-Native Org Design flagship — deep-dive, pyramid→inverted-T exhibit, new-roles card, plan); buying-criteria slide; Early Access Program as the pre-RFP vehicle; pre-RFP mechanics (product SKU, sponsor's pen, credit-forward, specimen pack, ownership + value floor); honest-critique chapter (capacity math revision: year one = proof year of 3-4 installs; five open decisions with owners).

**Assumptions added:** EAP eligibility (new logos vs existing customers) UNCONFIRMED — flagged on 3 slides for validation with program owner; Engine B ticket €80-150K to validate; all sample-output figures marked as illustrative specimens.

<!-- TELEMETRY_START
agent: frontline-slides-pptx (bespoke exhibit renderer v3)
engagement: internal-pdp-product-factory
deliverable: Product_Factory_Execution_Plan_Exhibit.pptx (v3, 41 slides)
slides: 41
checkpoints: 2
assumptions_documented: 8
modification_source: consultant feedback (ladder-lifecycle confusion, content depth, buying criteria, EAP, Engine B)
generated: 2026-07-27
TELEMETRY_END -->

## 2026-07-28 — Product Factory deck v4: rebuilt on the exhibit-slides-pptx engine + playbook expansion (57 slides)

**Change 1 — engine migration:** Installed the `exhibit-slides-pptx` skill drop (consultant-supplied zip) at `.claude/skills/exhibit-slides-pptx/` — the locked v3.1 engine extracted from the SNB Capital and BACB production builders, ratified as THE DEFAULT for all PPTX (Shyam, 28 Jul 2026). Rebuilt the deck on it verbatim: exhibit palette (#071224/#4066F5), chrome v3.1 with right rail, one-line ≤63-char action titles, one-line footnotes, takeaway bands, coral open badges, live slidenum page fields (mechanism the engine itself credits to this deck). Retired the bespoke master-template builder (`build_exhibit_deck.py`); new source: `build_product_factory_pptx.py`.

**Change 2 — playbook expansion (41 → 57 slides), per consultant direction:**
- **Chapter 00 "The short version"** — 6 exec slides for the Tim meeting (play on a page, line-up, numbers via the ratified stat-card row, route to yes, must-have quadrant, three asks).
- **Chapter 03 "The AI-native operating model"** — Engine B expanded to 8 slides: loop postures (in/on/above the loop + not-delegated zone; Citi three-case reference footnoted), permission map (possible now / preconditioned / not permitted), maturity path (Early A1-A3 / Mid A4 / Late A5), workforce shift (augmented / autonomous / new roles + skills to build), six-workshop execution anatomy, plus the existing deep-dive, sample outputs and plan.
- **Chapter 04 "The business connection"** — ambition → objective → value pool → Mission POC → measured proof bridge; must-have vs good-to-have account archetypes with 5-year-strategy signals to read.

**Verification:** Libre Franklin installed in the render container; all 57 slides rendered and eyeballed; QA checklist run (titles one line, footnotes one line, one table, coral badges on open items, DEFENSE notes on number slides).

<!-- TELEMETRY_START
agent: exhibit-slides-pptx (locked engine v3.1)
engagement: internal-pdp-product-factory
deliverable: Product_Factory_Execution_Plan_Exhibit.pptx (v4, 57 slides, playbook + exec version)
slides: 57
checkpoints: 2
assumptions_documented: 8
modification_source: consultant direction (skill drop as default; operating-model depth; business connection; exec version for Tim)
generated: 2026-07-28
TELEMETRY_END -->

## 2026-07-28 — Exec slides rework: horizontal ladder + what/why/outcome/feasibility grid

**Change:** Consultant feedback on the short version. E1 (the play) rebuilt as a left-to-right rung journey — four rung cards with propose·sign arrows between, each carrying what happens plus a "you leave with" exit artifact, closing with the read-left-to-right explainer line. E2 (the line-up) rebuilt as a five-offer grid with columns WHAT IT SELLS / WHY ONLY US / WHAT THE BANK GETS / FEASIBILITY, mirroring the consultant's reference table. Feasibility rated honestly per offer: X-Ray HIGH (assets exist, lite mode), Telemetry HIGH·GATED (live deployment + keystone), Guardrail HIGH (documents only), Cartographer MEDIUM (R&D alignment), Org Design MEDIUM (sequencing rule).

<!-- TELEMETRY_START
agent: exhibit-slides-pptx (locked engine v3.1)
engagement: internal-pdp-vc-monetization
deliverable: Product_Factory_Execution_Plan_Exhibit.pptx (v4.1, 57 slides)
slides: 57
checkpoints: 2
modification_source: consultant feedback (rungs horizontal, what/why/outcome + feasibility in short version)
generated: 2026-07-28
TELEMETRY_END -->

## 2026-07-28 — Tim package: the leadership case behind the playbook (5 slides)

**New deliverable:** `Output/Shyam_Talent_Programme_Tim.pptx` — a separate 5-slide personal package for the one-hour talent-programme session with Tim Ruttner. Cover + four slides: (1) the three-altitude record — accounts & pursuits (SNB Capital, BACB, ABSA ×5, HSBC, Schroders, SEB, NFIS cohort), market & category (Nordic FinTech Forum 2026 POV, Advisor Cockpit POV, exhibit design language ratified), the machine (Cortex AgenticOS, the Flywheel, the Pursuit Loop, peer enablement); (2) the philosophy the 57-slide playbook is written in (ship installations, codify everything, evidence over enthusiasm, diverge-then-converge); (3) three future theses with a named move each (cost per outcome, orgs follow the autonomy curve, vendors win by installing); (4) the ask ladder (P&L ownership path, ExCo sponsorship, €5K as seed) closing on "judge me on January."

**Evidence basis:** every claim traces to a repo artifact (engagement outputs, learnings/pursuit-loop-method.md, FLYWHEEL.md, docs/cortex-launch-presentation.html, exhibit-kit ratification records). Session-transcript history outside this repo was not available; the record used is the repo itself, stated as such to the consultant.

<!-- TELEMETRY_START
agent: exhibit-slides-pptx (locked engine v3.1)
engagement: internal-pdp-vc-monetization
deliverable: Shyam_Talent_Programme_Tim.pptx (5 slides)
slides: 5
checkpoints: 2
modification_source: consultant request (personal leadership package for Tim hour)
generated: 2026-07-28
TELEMETRY_END -->

## 2026-07-28 — Tim package v2: visual / infographic edition (9 slides)

**Change:** Rebuilt the Tim package as one exhibit per question, per consultant direction ("proper McKinsey style, more infographic"): strategy house (ambition roof, two-engine pillars, wedge-ladder beam, Cortex foundation, success-metrics rail) · why-now convergence (three pentagon currents → the join) · the arsenal (65 processes / 24h loop / 10 accounts, three big-number columns) · the ammunition belt (five feasibility-shaded chevrons firing at the POC + propellant row: EAP slots, specimen packs, credit-forward) · the Backbase leverage stack (six given tiles below, four added tiles above) · the skills from→to ladder (five rows, today-dot vs target-dot; category building flagged as the CMO-mentorship row) · the flywheel (six-node cycle around a compounding hub + revenue payout rail with an unsized licence-pull badge) · the ask ladder unchanged. 5 → 9 slides.

<!-- TELEMETRY_START
agent: exhibit-slides-pptx (locked engine v3.1 + flat autoshape composition)
engagement: internal-pdp-vc-monetization
deliverable: Shyam_Talent_Programme_Tim.pptx (v2, 9 slides, infographic)
slides: 9
checkpoints: 2
modification_source: consultant feedback (more visual, seven-question structure, flywheel)
generated: 2026-07-28
TELEMETRY_END -->
