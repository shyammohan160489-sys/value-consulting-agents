# Digest: Claude Design "McKinsey exhibit" deck kit

**What this is.** A self-contained skill package for **Claude Design** (claude.ai's design canvas, `.dc.html` format) that teaches Claude to build Backbase decks in a validated **McKinsey exhibit style** — action-title sentences, one exhibit per slide, white slides with navy/blue accents. Arrived 2026-07-08 as `Agentic Banking Rollout Deck.zip` (files dated 2026-07-06); distilled from deck reviews run June–July 2026. Contents preserved verbatim in this folder.

**What it is NOT.** Not an animation tool (`support.js` is just the dc-runtime viewer: parse `<x-dc>`, render sections, pan/zoom, PPTX export hooks). And not part of the Frontline 2026 family — see "Relationship to Frontline" below.

## Contents

| File | Role |
|------|------|
| `SKILL.md` | The skill: type scale, slide anatomy, palette, 15-pattern exhibit catalog, content rules, PPTX export mechanics |
| `Backbase Exhibit Templates.dc.html` | 15 ready-to-copy template slides (T00–T14), one per validated pattern |
| `support.js` | dc-runtime the `.dc.html` needs (generated from TypeScript; viewer, not animation) |
| `assets/logo/` | Backbase wordmarks (dark + white) |
| `README.md` | Install instructions: upload zip to a Claude Design project, bind SKILL.md + templates as the design system |

## The exhibit catalog (T00–T14)

Cover · slide anatomy · sorted bars · segmented to-scale bar · wave/gantt timeline · quadrant bubble · dotted region map · **cohort cascade (funnel-over-time)** · milestone strip · unit dot-grid · concern→answer stack · chips+hero split · cadence tiles+step flow · plain table (the ONE table per deck) · chapter divider.

## Hard rules that survived review (worth stealing)

- Type scale on 1280×720: action title 38–40px (full sentence, max 2 lines) · body 18–21px · footnotes 17px · **nothing below 17px**. (The original 45pt/24pt brief overflowed and was replaced after review.)
- One exhibit per slide, 2–3 callouts max; detail goes to speaker notes, never on-slide.
- Sentence case; no emoji; **no em dashes**; no negative/contrastive framings ("X, not Y") — state the positive claim.
- Ranges as ranges (15–20) = honest forecasting. Every numeric slide ends with a 17px source footnote.
- Account names as clean text, never logos; per-person data never on slides.
- Placeholder slides: coral dashed badge "Placeholder/Open · owner".

## Palette (⚠️ different from Frontline tokens)

Navy `#071224` · primary blue `#4066F5` · secondary `#1F3799 #5F7DF7 #B5C1F1` · tints `#E6EBFE #F5F6FA` · cyan `#93FBFE` (highlight only) · coral `#EC5E48` (gates/risks/placeholders only). Frontline 2026 is navy `#041326` / blue `#3367FF` (see `../frontline-tokens.json`). Same Libre Franklin typography.

## Provenance signals

- Slide anatomy includes an **L·E·C position marker** (Land · Expand · Consume — the Backbase GTM motion model), and the catalog is GTM-shaped (cohort cascade for pipeline, wave timelines, milestone strips, concern→answer for objections). Zip name = "Agentic Banking Rollout Deck".
- Reads as distilled from internal **agentic-banking GTM rollout deck work** (the mid-year agentic motion), packaged for team distribution in Claude Design projects.

## Relationship to Frontline 2026 (decision needed before mixing)

This kit and Frontline 2026 are **parallel design languages targeting different environments**:

| | Frontline 2026 (this repo) | Exhibit kit (this folder) |
|---|---|---|
| Environment | Cortex skills → self-contained HTML / PPTX | Claude Design projects (claude.ai), `.dc.html` + gen_pptx |
| Blue / Navy | `#3367FF` / `#041326` | `#4066F5` / `#071224` |
| Philosophy | 17 layouts, brand-template-derived | McKinsey exhibits, action titles, one-exhibit-per-slide |
| Likely lane | Client-facing deliverables (canonical per CLAUDE.md) | Internal strategy / GTM / leadership decks |

**Do not blend the palettes.** If a Cortex deliverable should use this style, that's a deliberate choice, not a default. The *content rules* (action titles, one exhibit per slide, ≥17px floor, source footnotes, ranges-as-ranges) are style-agnostic and worth absorbing into Frontline composition rules — candidates flagged in `../composition-rules.md` review.

## Adoption status (2026-07-08)

Shyam approved adopting **P1** (sorted bars, segmented bar, quadrant bubble, unit dot-grid + source-footnote slot + chart color grammar) and **P2** (cohort cascade, milestone strip, dotted region map, roadmap gates, concern-answer), and agreed the not-taken list (kit palette, kit chrome, L·E·C marker, fixed px, 17px hard floor, Claude Design runtime).

**Proof deck:** [`frontline-exhibit-adoption-sample.html`](frontline-exhibit-adoption-sample.html) — a 15-slide Frontline-engine deck rendering every adopted exhibit in frontline-tokens.json colors, with an on-slide adopted/left-behind tag ledger per exhibit and a closing "deliberately left behind" slide. Intensity ramp = alpha steps of token blue (validated as a sequential scale with the dataviz six-checks; light steps always carry direct labels). Preview: launch config `exhibit-kit` (port 8817).

**Next step (not yet done):** wire the adopted exhibits into `presentations/backbase-slides-app/engine.js` + `tools/frontline_slides_pptx.py` as real layouts, add a charts section to `../composition-rules.md`, extend `../master-template-2026-catalog.md`'s content→layout guide, and document the derived ramp in `../frontline-tokens.json`.
