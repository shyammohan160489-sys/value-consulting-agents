---
name: frontline
description: Frontline 2026 design-system launcher. Start here for ANY client-facing visual deliverable (deck, document, presentation). Probes the user for the output format first, explains the options, then routes to the right skill.
---

# /frontline — Design System Launcher

The user wants a client-facing visual deliverable in the **Frontline 2026** design
system. **Do NOT assume the format. Probe first.**

## STEP 0 — Probe for format (only the FIRST time)

**Ask only if no format is established yet.** If the user is already working in a
format (chosen earlier this session, in progress, or named this turn), skip STEP 0
entirely and just proceed in that format. Otherwise — on the first output request —
open with a short, friendly question — *"I can produce this in the Frontline 2026
design system. What output format would you prefer — HTML deck, long-form HTML,
PDF, or PPT?"* — then present the options with their one-line explanations:

| # | Format | Skill / how | What it is | Best when… |
|---|--------|-------------|-----------|-----------|
| **1** | **HTML slide deck** ⭐ | `/frontline-slides-html` | Self-running `.html`, 17 layouts, presenter mode. The **Pictet QBR look** — cards, chips, two-tone panels, option cards w/ RECOMMENDED badge, Gantt. Highest fidelity. | Presented/demoed; richest look; no editing needed. |
| **2** | **Long-form HTML** | `/frontline-long-form` | Scrolling business/value case w/ sidebar nav, hero stats, lever/scenario cards. | Read async (emailed) — business case, ROI summary, exec briefing. |
| **3** | **PDF** | build then export | A flat, final, **non-editable** file. Built as long-form (for documents) or as a deck (for slides), then exported to PDF — Chrome headless for HTML, `soffice` for PPTX. | Sending a locked file for review/sign-off/printing; recipient won't edit it. |
| **4** | **PPT** | `/frontline-slides-pptx` | Editable Google Slides / PowerPoint, same brand (~90% of the HTML look). | Team must edit numbers/scope/pricing first, or it lives in Drive. |

(Need bespoke pixel-perfect scenes the 17 layouts can't carry? Use
`/executive-briefing` / `-slides` — rare.)

If the format isn't obvious, ask **two clarifiers**:
- **Presented live, or read async?** → presented ⇒ 1 / 4; async ⇒ 2 / 3.
- **Will anyone edit it before delivery, or is it final?** → edit ⇒ 4 (PPT); final/locked ⇒ 3 (PDF); rich & self-running ⇒ 1 (HTML).

If the user already named a format, skip the menu — confirm in one line and proceed.

## STEP 1 — Route
Invoke the matching skill above and follow its prompt.

## Non-negotiables (every format)
- Read tokens from `knowledge/design-system/frontline-tokens.json` — never invent
  hex/font/geometry (navy `#041326`, blue `#3367FF`, red `#FF503C`, Libre Franklin).
- Apply `knowledge/design-system/narrative-spine.md` (operating-model thesis,
  From→To, outcomes-not-features).
- Reference look-and-feel: the Pictet QBR HTML
  (`Engagement/Pictet/Output/pictet_qbr_2026.html`).
- **PPTX note:** two builders exist — `tools/frontline_2026_presenter.py`
  (`Frontline2026Presenter`: tiles/columns/pillar/process/financial, photo cover,
  two-tone titles — the Schroders look; **default**) and
  `tools/frontline_slides_pptx.py` (`BackbaseSlidesPresenter`: cards, before→after
  with chips, RECOMMENDED option card, statement band — the Pictet components).
  Pick by which components the deck needs.
