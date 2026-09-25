---
name: proposal-longform
description: Build a client-facing interactive proposal document (single self-contained HTML, Backbase Frontline 2026 look) with a multilingual toggle (incl. RTL Arabic), live pricing-transparency sliders, and a one-click executive readout PDF. Use this whenever the user asks for a "proposal", "commercial proposal", "pricing proposal", "bilingual/Arabic proposal", "interactive pricing", "proposal with sliders", or an "executive readout" — even if they only mention one of those features. Not for negotiation strategy, concession ladders, or Deal Desk packs (that is the internal /proposal-builder cockpit).
---

# Proposal Long-Form — interactive client proposal builder

Produce a single self-contained HTML proposal a client can open anywhere: Frontline 2026
branded, sidebar-navigated, with three interactive modules baked in:

1. **Language toggle** — the whole document flips between languages (LTR/RTL aware,
   localized number/currency/date formatting). Default pair: English + Arabic.
2. **Pricing transparency sliders** — the client moves the volume/term drivers and the
   projected pricing recomputes live, with every calculation line and the published volume
   tiers visible. "The math, in the open" is the persuasion mechanic: nothing hidden.
3. **Executive readout (PDF)** — one button prints a one-page executive summary that
   snapshots the current language and slider configuration, via the browser's print-to-PDF.

Start from `assets/proposal_longform_template.html` — it is a complete working example
("Meridian Bank", fictional) with all three modules wired and tested. Copy it to the
engagement folder, then replace content. Never rebuild the mechanics from scratch.

## Evidence pre-flight (mandatory — Shyam, 6 Aug 2026)

Before drafting content, read `knowledge/domains/ai-value-evidence/` plus the relevant
`knowledge/domains/<domain>/`, and embed the verified market evidence that supports the proposal's value
story — cited to the primary source (bank disclosure, named analyst report), never to an aggregator.
Where a value proposition has NO external validation, do not stretch research to cover it: carry it with
demonstration instead (prototype, design, journey) and keep the claim honest. Unverified (⚠️) items never
enter client assets.

## Scope guardrail (important)

This skill produces the **client-facing proposal document**. It deliberately contains no
negotiation planning: no concession ladders, no floors, no walk-away numbers, no internal
discount targets, no approval tiers. If the user wants deal strategy, route them to the
internal `/proposal-builder` cockpit and keep its outputs out of this document. In the
document itself, all pricing is **projected, list/published basis, explicitly non-binding**
(the template's disclaimer block carries this — keep it in both languages).

Never put in a client document: internal floors or minimum prices, discount percentages
off rack, competitor pricing intel, internal steers, or "prepared for [person]" covers.

## Workflow

1. **Intake.** Gather: client name, deal shape (LOB, pricing basis, drivers), the published
   tier structure to show, scenario presets (conservative/base/upside), language pair,
   currency, and the narrative facts (value levers, phases, assumptions, next steps).
   Missing numbers: mark as assumptions in the assumptions table — never invent silently.
2. **Copy the template** into the engagement folder as `<client>_proposal_v1.html`.
3. **Replace content section by section.** Every text block exists twice — `<span lang="en">`
   and `<span lang="ar">` (or your second language). Keep BOTH in sync; if you change one,
   change the other. Read `references/authoring-guide.md` for the content contract,
   the `PRICING` config schema, language/RTL notes, and the readout hooks.
4. **Wire the pricing.** Edit the `PRICING` object (base fee, tiers, presets) and the driver
   sliders' min/max/step. Keep the math panel lines honest — each line must state its own
   formula with live numbers. If the deal's math needs a different shape (e.g. AUM-based),
   adjust `recompute()` but keep every displayed line self-explanatory.
5. **Verify in a browser** (checklist below), then deliver the single HTML file.

## QA checklist

- [ ] Toggle both languages: no untranslated strings, layout mirrors correctly in RTL,
      money/dates format per locale (Western digits for money in Arabic by default)
- [ ] Move every slider end to end: no NaN, tier highlight follows, totals reconcile
      (hand-check one configuration: base + users×rate, ×term, +services)
- [ ] Preset buttons snap all drivers and re-highlight correctly
- [ ] Executive readout button prints ONE clean page in the current language with the
      current slider state (also test `?readout=1` and `?readout=1&lang=ar` URL modes)
- [ ] Disclaimer ("projected, not a quote") present in every language, on page and readout
- [ ] No internal-only content anywhere (floors, discounts, steers, personal names)
- [ ] Assumptions table lists every assumed number with its validation owner

## Governance (per Cortex CLAUDE.md)

Two checkpoints (echo the intake back before building; walk the QA result after), a journal
entry with telemetry block in the engagement `ENGAGEMENT_JOURNAL.md`, and every number
traced to a source or listed as an assumption. In non-interactive runs, record both
checkpoints in the journal instead of pausing.

## Files in this skill

- `assets/proposal_longform_template.html` — the working template + demo content. The source of truth for the mechanics.
- `references/authoring-guide.md` — content contract, PRICING schema, i18n/RTL detail, readout hooks, headless PDF generation.

## Roadmap note

The target state adds guided commercial strategy on top (scenario framing fed by the
internal deal engine). Until that lands, this skill stays purely client-safe output.
