# Frontline 2026 — Slide Composition Rules (canonical)

These rules exist so the recurring spacing problems **cannot regress**. They are
enforced in BOTH renderers — the PPTX builder (`tools/frontline_slides_pptx.py`)
and the HTML slide engine (`presentations/backbase-slides-app/`) — and must be
honoured by any new layout and by `tools/frontline_2026_presenter.py`.

**Where each rule lives in the HTML engine** (`deck-template.html` + `engine.js`):
- Rule 1 (fixed gap): content anchored at `top:34%` (label 10% · title 15% ·
  subtitle 24%).
- Rule 2 (no float): `.content-body{justify-content:flex-start}` — content sits
  under the headline, never centred-and-floating. (`.body-only`, i.e. no header,
  stays centred by design.)
- Rule 3 (timeline): the `timeline` layout (`renderTimeline` + `.layout-timeline`
  CSS) — same milestone component as the PPTX `add_timeline`.

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
