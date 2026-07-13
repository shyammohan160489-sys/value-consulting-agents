# Backbase Master Template 2026 — Layout Catalog (canonical source)

> **Source of truth for slide layouts.** File: `knowledge/design-system/Backbase Master Template _ 2026.pptx`
> (the official Backbase 2026 deck template, 20×11.25in / 16:9, 74 master layouts + 55 example slides
> incl. a built-in GUIDELINES section). The Frontline engine
> (`presentations/backbase-slides-app/`) and tokens (`frontline-tokens.json`) are derived from this.
> When in doubt about a layout's purpose, geometry, or the type system, this template wins.

## The governing principle (from the template's own Guidelines)

**"Every slide uses a pre-built layout designed for a specific purpose… always use the layout that
matches the content you're creating."** And on type: **"avoid manually resizing text — the levels are
already sized and spaced to work together."**

This is the rule: **map content → the right layout, then leave the type alone.** Fighting a layout with
manual font resizing or vertical centering is the anti-pattern (it caused the 29-Jun-2026 regression —
see [composition-rules.md](composition-rules.md)). If content won't fit at the layout's built-in sizes,
the slide has too much on it → split it or pick a different layout.

## Four-level text system (Level → use → size)

| Level | Use | Size | Engine field |
|---|---|---|---|
| **1 — Label** | caption / tag / eyebrow above the title | 18pt **UPPERCASE** | `label` |
| **2 — Title** | the largest, most prominent text | 45pt | `title` |
| **3 — Subtitle** | supporting heading / key phrase | 24pt | `subtitle` |
| **4 — Body** | descriptions, details, general content | 20pt | `body` |

Titles + body appear on every slide; labels + subtitles only where the layout calls for them.

## Layout families → engine layout (content → layout decision guide)

| Master family | Use it for | Engine `layout` | Notes |
|---|---|---|---|
| **Cover — Photo** | branded/segment opening with imagery | `cover-photo` | segment + HR/employee photo variants |
| **Cover — Color Block** | dark-gradient opening, no photo | `cover-color-block` | standard + **partner** variant (set `partner`) |
| **Chapter — Numbered** | numbered section divider | `chapter-numbered` | navy + primary-blue (`theme`) |
| **Chapter — Standard** | section divider, title only | `chapter-standard` | navy + primary-blue |
| **TOC** | agenda / contents | `toc` | 5/4/3 rows, numbered or not (`numbered`) |
| **Overview — About** | introduce Backbase or a customer | `overview-about` | photo + stats/icons row |
| **Overview — Stats** | a few headline figures | `overview-stats` | big legible numbers |
| **Content — Standard** | general content / dashboard (LAST resort) | `content-standard` | navy + primary-blue; **author top-anchored** |
| **Content — Columns** | **2–6 parallel things** (pillars/options) | `content-columns` | ⭐ DEFAULT for 3 pillars; optional icons |
| **Product** | feature + product screen | `product` | with/without background (`imageBg`) |
| **Team** | people grid | `team` | 16/12/8/5/3/2 members (auto-layout) |
| **Testimonial** | customer quote | `testimonial` | always include author photo |
| **Statement** | key statement / question / standout | `statement` | positive/negative = blue/red; highlight words |
| **Statement — Stat** | one big number + line | `statement-stat` | blue/red accent |
| **Roadmap** | genuine multi-track schedule | `roadmap` | Gantt — reserve for real schedules |
| **(Journey/sequence)** | phases / steps / journey | `timeline` | engine addition; cleaner than Gantt |
| **Agenda** | event schedule table | `agenda-table` | navy table |
| **Thank you** | closing | `thank-you` | — |

## Coverage vs the engine (what we have / minor gaps)

**Covered:** all 18 families above map 1:1 to engine layouts. Columns scale 2–6; covers have partner
variant; chapters + content have navy/blue; statement has blue/red + dark. Good parity.

**Minor gaps (optional future additions, not blocking):**
- **Primary-blue `content-standard`** — master offers a blue-background variant; engine currently does
  light + navy. Add a `blue` theme if a deck needs it.
- **Speaker layout** (`Speaker 1`) — a presenter intro layout in the master; no engine equivalent yet.
- **Icon library** — the master ships a recurring-icon set (example slides 50–54); the engine uses inline
  SVGs instead. Pull from the master if a specific brand icon is needed.

## Theme colours (verified against `theme1.xml`)

| Role | Master `theme1` | Engine / tokens | Note |
|---|---|---|---|
| Primary dark | `#091C35` | `#041326` (navy) | engine standardizes on #041326; #091C35 = tokens' `navy_secondary` ("Theme 2") |
| Primary blue | `#3366FF` | `#3367FF` | 1-digit difference, imperceptible |
| Cyan | `#69FEFF` | `#69FEFF` | ✓ |
| Red | `#FF503C` | `#FF503C` | ✓ |
| Light blue | `#E5EBFF` | `#E5EBFF` | ✓ |
| Off-white | `#F3F6F9` | `#F3F6F9` | ✓ |

The master ships **two slide masters** (Theme 1 + Theme 2); the dark surface differs between them. The
engine uses one navy (`#041326`) for consistency across all decks. No action needed — flagged for
transparency, not a defect.

## How to use this

1. Before authoring any deck, pick the layout per the decision guide above — **do not default to
   `content-standard`.** Three pillars → `content-columns`. Numbers → stats. Sequence → `timeline`.
2. Use the engine's `label`/`title`/`subtitle`/`body` to match the 4-level type system; **don't resize.**
3. For a brand-new layout the engine lacks, open the .pptx, find the matching example slide, read its
   geometry, and add a renderer to `engine.js` + CSS to `deck-template.html` (Architect-tier change).

Related: [composition-rules.md](composition-rules.md) · [frontline-tokens.json](frontline-tokens.json) ·
[narrative-spine.md](narrative-spine.md) · skill `frontline-slides-html` guideline 9.
