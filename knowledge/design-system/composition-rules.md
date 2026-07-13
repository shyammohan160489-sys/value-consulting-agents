# Frontline 2026 — Slide Composition Rules (canonical)

> **Layouts catalog:** [master-template-2026-catalog.md](master-template-2026-catalog.md) maps the
> official Backbase 2026 master template (`Backbase Master Template _ 2026.pptx`) → engine layouts, with
> the content→layout decision guide and the 4-level type system. Pick the layout there FIRST; these
> composition rules govern how a chosen layout's body is filled.


These rules exist so the recurring spacing problems **cannot regress**. They are
enforced in BOTH renderers — the PPTX builder (`tools/frontline_slides_pptx.py`)
and the HTML slide engine (`presentations/backbase-slides-app/`) — and must be
honoured by any new layout and by `tools/frontline_2026_presenter.py`.

**Where each rule lives in the HTML engine** (`deck-template.html` + `engine.js`):
- Rule 1 (fixed gap): content anchored at `top:33%` (label 10% · title 15% ·
  subtitle 24%); `top:30%` when there is no subtitle.
- Rule 2 (top-anchored, NOT centred): a header `.content-body` is **top-anchored
  and content-height** — it flows downward from the body line and has **no fixed
  height and no vertical centering**. A sparse slide keeps a clean bottom margin;
  that is correct. (`.body-only`, i.e. no header, is the ONLY centred case.)
  ⚠️ Do not re-add `bottom:…` + `justify-content:center` to header bodies — that
  marooned content in the middle of a tall box and forced fonts smaller (the
  29-Jun-2026 regression). "Balanced" means *text centred inside each card*, never
  the whole body block centred in the band.
- Rule 3 (timeline): the `timeline` layout (`renderTimeline` + `.layout-timeline`
  CSS) — same milestone component as the PPTX `add_timeline`.
- Rule 4 (type sizing, HTML): `structured:true` on `content-standard`
  (`content-body--structured` — resets body to `font-size:1em`); size body in em via
  `em(px)=px/21.376`. See Rule 4 below.
- Rule 5 (subtitle & strap line are flex levers): omit `subtitle` to rebase the body
  higher (`top:30%` vs `33%`); drop redundant/on-the-nose copy. See Rule 5 below.

## The problem they solve
Two failure modes kept recurring on content slides:
1. **Stretched tiles** — a card sized to the full slide band, so short content was
   marooned at the top of a tall empty box.
2. **Floating / void** — after content-sizing, compact cards pinned at a drifted
   top anchor (~40%), leaving a *big gap under the headline* and a *void below*.

Both are symptoms of one missing thing: **composing the vertical space**, not just
sizing/placing one box. Nudging individual boxes per deck is whack-a-mole; these
rules fix it at the system level.

## Rule 1 — Fixed headline→content gap
Content starts on the engine's body line: **`BODY_TOP_FRAC = 0.33`** of slide
height (label 10% · title 15% · subtitle 24% · body ~32%). It must **not** drift to
0.34–0.40. The gap under the headline is constant on every slide.

## Rule 2 — Cards are content-proportionate, never stretched, never floating
- Card height = **content height + comfortable padding** (`CARD_COMFORT_IN ≈ 0.85"`),
  floored at `CARD_MIN_IN ≈ 1.5"`, capped at the content band (to `BAND_BOTTOM_FRAC
  = 0.90`). A row of cards shares the tallest card's height (equal heights).
- Never size a card to *fill* the band (that marooned text). Never leave a thin
  strip floating (that looked unfinished).
- **Text is vertically centred inside the card** (`valign='middle'`) so a card that
  is taller than its content reads balanced, not top-marooned.
- Elements that follow the cards (chip rows, callout strips, led-by footers)
  **follow the actual card height** — they never sit at a fixed low anchor.
- A genuinely sparse slide will have a clean bottom margin. That is correct — the
  fix is a *tight headline gap + well-proportioned cards*, not inflating content.

## Rule 3 — Timelines: milestone line, not a Gantt, for "journey" stories
For a sequence/journey narrative, use the **horizontal milestone timeline**
(`add_timeline`): one connector line, coloured nodes with labels above, a card under
each (title · body · coloured footer), optional callout. It is far cleaner and more
scannable than a Gantt grid. Reserve the Gantt (`add_roadmap`) for genuine
multi-track schedules.

## Rule 4 — Type sizing: use em, never fixed px (HTML engine)
Fixed px do not scale with the frame — the em-based title balloons while px body stays
tiny and the **title:body ratio breaks** (reads as "the font doesn't match the title").
Size every body element in em off the slide root: **`em(px) = px / 21.376`** (root is
`1.67vw` ⇒ `1em ≈ 1.67%` of frame width; `1.67%·1280 = 21.376`), reusing the hand-authored
reference deck's own px so proportions hold at any frame size. Reference values: body /
bullets `em(14)`, tile heading `em(17)`, pyramid name / big head `em(20)`, callout heading
`em(15)`, badge `em(10)`, uppercase mini-label `em(11)`, table cell `em(14)` / header
`em(11)`, arch item `em(13)`; container padding via `em()` too (card `em(24) em(26)`).
- For custom **structured** bodies (card grid, layer stack, pyramid, table) set
  `structured:true` — it resets the body to `font-size:1em` so `em()` reads off the root.
  Put font-size on **leaf text only** (a container that also has children compounds em).
- Structured bodies flow at **natural height, top-anchored, and FLEX** — bottom margin
  varies with content volume (measured 72–93% across the HSBC deck; do NOT force them all
  to one line). This is Rule 2 applied to custom HTML: never `flex:1` / `grid-auto-rows:1fr`
  / `height:100%` to fill.
- The engine header zone starts the body lower (30–33%) than a bespoke deck (~24%), so
  content-HEAVY stacks (5-layer arch, 4-bar pyramid) take slightly tighter internal padding
  (arch layer `em(11)`, pyramid bar `em(13)`) to still leave a bottom margin.
- (PPTX builder sizes in pt via the 4-level type system — this em law is HTML-only; the
  *flex / natural-height* principle applies to both.)

## Rule 5 — Subtitle and strap line are flex levers, not fixed slots
The **eyebrow (label)** and **title** are the constants on every slide. The blue
**subtitle** and the **callout / strap line** are OPTIONAL — spend them only when they earn
their place. Decide per slide:
- Content-DENSE slide → **drop the subtitle** (rebases the body higher: `top:30%` vs `33%`,
  buying room) and let the title carry it — **sharpen the title to stand alone**.
- LIGHT slide → keep the subtitle.
- Always drop a subtitle that merely **narrates what the eyebrow + title + tiles already
  say** — redundant prose reads as filler, and in client decks as on-the-nose sell.
- Client copy is **directional and impact-led**, never the pitch spelled out (e.g. not
  "the fastest, lowest-risk *way in*"). If a good line won't come, **drop it — don't force
  it**. Applies to both renderers.

## Builder constants (single source of truth)
`tools/frontline_slides_pptx.py`:
```
BODY_TOP_FRAC    = 0.33   # headline→content gap
BAND_BOTTOM_FRAC = 0.90   # bottom of the content band
CARD_COMFORT_IN  = 0.85   # padding added to content (proportionate, not fill)
CARD_MIN_IN      = 1.5    # a card is never a thin strip
```
Helpers: `_band()`, `_content_h()`, `_row_card_h()`, `_card(valign='middle')`,
`add_timeline()`. Change the look by changing these constants — not per deck.

## Proof
Pictet QBR slides 5, 9, 20, 25, 26 (cards/comparison/options — tight gap, balanced,
no stretch/float) and slide 21 (the milestone timeline). Rebuild:
`python3 Engagement/Pictet/Output/build_deck_pptx.py`.
