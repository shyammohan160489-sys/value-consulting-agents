# Pipeline Gap — the Commercial / Deal-Desk track

- **Surfaced by:** Enterprise wealth deal, EMEA, usage/AUM-based pricing, competitive late-stage negotiation (BAFO). 2026-Q2.
- **Also applies to:** Any enterprise deal with usage-, AUM-, seat-, or tier-based pricing and a live negotiation. Confirmed relevant to at least one other concurrent EMEA wealth/banking deal. Effectively every large commercial close.
- **Last seen:** 2026-06-04
- **Severity:** HIGH — this was ~70% of the engagement's deliverable volume and carries the highest commercial sensitivity, yet has zero pipeline support and zero governance coverage.

## The gap in one line

Cortex's agent pipeline is a **value-assessment** engine (`discovery → capability → roi-business-case → roadmap → narrative`). It can prove *value*. It **cannot structure, model, or defend *price***. Real enterprise deals turn on the second.

## What happened

The engagement's value case (multi-£M, multi-phase lifecycle benefit model) was classic pipeline territory — `roi-business-case-builder` + `generate-roi-excel` + `frontline-long-form` covered it.

Everything *commercial* was built bespoke, re-deriving its own logic each time, with no agent, no template, and **outside the journal / telemetry / auditability governance** the rest of the pipeline enforces:

- usage-based pricing model (bands, uplift curves, smoothing, crossover, scenario tabs, margin head-to-head, software-vs-3rd-party "price of failure" split)
- multi-scenario negotiation deck (where-we-are → scenarios side-by-side → projection table → schedule → held terms)
- a "negotiation travel" anchoring 1-pager (ghost "standard ramp" vs "presented", round-by-round)
- a negotiation playbook (anchors, concession ladder, decoys, BATNA, walk-aways)
- procurement / deal-desk support packs
- deal-state meeting notes + a persistent live deal journal (transcript → action items + strategic reads + stakeholder map + next steps → append to deal memory)

## Classification (🟢 in-pipeline · 🟡 rendering in-pipeline, logic bespoke · 🔴 fully bespoke)

| Archetype | Status | Proposed codification |
|---|---|---|
| Usage-based pricing model | 🔴 | `/pricing-model` skill (+ optional deal-structuring agent) |
| Multi-scenario negotiation deck | 🟡 | negotiation-deck layout kit (consumes pricing model) |
| Negotiation "travel" anchoring 1-pager | 🔴 | layout in the negotiation kit — novel, high reuse |
| Negotiation playbook / strategy | 🔴 | internal-only negotiation-strategy agent |
| Procurement / deal-desk pack | 🟡 | procurement-briefing template |
| Deal-state notes + live deal journal | 🔴 | `/deal-notes` skill — highest day-to-day reuse |
| CFO / decision paper | 🟡 | `frontline-long-form` variant |
| POC vision-playback planning kit | 🟡 | playback planning template |
| Client brand re-theme of any Frontline output | 🔴 | `--theme <client>` param on Frontline skills |

## What the foundation made possible

The bespoke work was *fast* only because the rendering + context substrate already existed: the Frontline 2026 engine + tokens, `frontline-long-form`, `executive-briefing`, the xlsx/pptx skills, and the engagement-folder + deal-state-memory discipline. The substrate was in-pipeline; the commercial **logic and archetypes** were not.

## Why codify (the productization case)

1. **Universal reuse** — pricing model, negotiation deck, travel slide, deal-notes apply to every usage-priced enterprise deal, any domain.
2. **Methodology was re-derived every time** — codifying captures it once, makes it consistent, and lets *any* consultant produce it (not just the one who reasoned it out).
3. **Closes the structural gap** — Cortex gains the ability to defend price, not just prove value.
4. **Pulls the most sensitive outputs under governance** — pricing + negotiation artifacts currently carry no journal, telemetry, or evidence-tracing.

## Recommended sequence

- **Phase 1:** `/deal-notes` (fastest, everyone uses it, low risk) → `/pricing-model` (biggest structural value). Specs drafted alongside this entry.
- **Phase 2:** negotiation-deck kit + `--theme`.
- **Phase 3:** negotiation-strategy agent, decision-paper / procurement templates, POC kit.

## Governance / contribution path

Building skills is Architect-tier. Path: (1) this learning + specs land in `knowledge/learnings/` (consultant-tier, done); (2) Architects implement Phase 1; (3) each new skill ships journal + telemetry + dual-checkpoint compliant from day one — unlike the bespoke originals.

> Full (client-named) working brief retained in the engagement folder:
> `Engagement/<client>/Output/CORTEX_DELTA_dealdesk_productization_20260604.md`
