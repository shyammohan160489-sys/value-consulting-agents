# Skill: Backbase McKinsey-exhibit decks

Invoke this skill whenever building or editing a Backbase slide deck in the McKinsey exhibit style (action titles, one exhibit per slide, white slides with navy/blue accents). It captures everything validated during deck reviews (June-July 2026). The companion file **`Backbase Exhibit Templates.dc.html`** holds one ready-to-copy slide per pattern (T00-T14) — copy the `<section>` you need and replace the placeholder content.

## 1. Type scale (px on a 1280×720 slide) — validated, do not enlarge
The original "45pt headline / 24pt body" brief overflowed at 1280×720; this scale replaced it after review:
- Action title (full-sentence takeaway): 38-40px, max 2 lines, max-width ~900px
- Kicker/label (uppercase): 18px, letter-spacing .1em
- Body, callouts, table cells: 18-21px
- Cell hero numbers: 24-26px; standalone hero stats: up to 74px (weight 300)
- Legends, sub-labels, footnotes: 17px. Nothing below 17px anywhere.

## 2. Slide anatomy (template T01)
1. Hairlines: top at 55px, left rail at 55px (light: rgba(7,18,36,.18); dark: rgba(255,255,255,.22)). Notch mark at 39,39.
2. Kicker (uppercase, #4066F5) + action-title sentence.
3. L·E·C position marker top-right (40×26px cells; active cell filled #4066F5; enabler slides fill a 9px bar under the cells instead).
4. One exhibit, 2-3 callouts max.
5. Hairline-topped footnote, 17px, rgba(7,18,36,.45): assumptions + source where numeric.
6. Footer: 44px band, hairline, wordmark right + page number.
7. Content container: `position:absolute;left:96px;right:60px;top:76px;bottom:60px;display:flex;flex-direction:column`. Absolutely position only chrome; content lives in one flow container. Grids use `minmax(0,1fr)` rows and `overflow:hidden` cells.

## 3. Palette
Navy #071224 · primary blue #4066F5 · secondary blues #1F3799 #5F7DF7 #B5C1F1 · tints #E6EBFE #F5F6FA · cyan #93FBFE (overlay/highlight, never a gradient step) · coral #EC5E48 (gates, risks, placeholders only). Dark cards: navy + radial blue glow `radial-gradient(620px 320px at 88% -10%, rgba(42,80,220,.6), transparent)`. Intensity gradients (deep→light): #1F3799 → #4066F5 → #5F7DF7 → #B5C1F1 → #E6EBFE. Max 1-2 background colors per deck.

## 4. Exhibit catalog (template slide → when to use)
- **T02 sorted bars** — ranked magnitudes; lead bar blue, rest tinted.
- **T03 segmented to-scale bar** — one total split into parts; widths proportional.
- **T04 wave/gantt timeline** — plans in waves; diamond gates (blue = GA, coral = decision).
- **T05 quadrant bubble chart** — two measures + size; light zone fills, dashed boundary lines, uppercase zone captions at zone tops.
- **T06 dotted region map** — geography shaded by intensity; one dot = land unit; navy label chips; shade legend row above.
- **T07 cohort cascade** — funnel-over-time; bottom-aligned stacks growing left→right, carried-in cohorts in tint, gates as dashed verticals, wins row under the axis.
- **T08 milestone strip** — 3-4 oversized numerals on a milestone line, gate diamonds, dark ramp band beneath.
- **T09 unit dot-grid** — "x of y" messages; one dot = one unit, filled vs dim, hero band `= x of y`.
- **T10 concern → answer stack** — objections; dark glow card per concern, answer in white.
- **T11 chips + hero split** — few facts + one key message; dashed chips left, dark hero card right, one coral callout.
- **T12 cadence tiles + step flow** — rhythms (big W/M/Q letterforms) and sequences (numbered chips with arrows).
- **T13 plain table** — the ONE intentional table per deck (conditions/register: condition · owner · date).
- **T14 chapter divider** — dark, big light-weight number + title.
Approved but not templated separately: stacked bars, phase grids, strategy pyramid, plan-curve + upside fan.

## 5. Content rules
- Action titles are full sentences, short and human. Kickers name section · role.
- Sentence case everywhere; only labels uppercase. No emoji. **No em dashes.** Currency in euros unless natively USD.
- No negative/contrastive framings ("X, not Y"); state the positive claim.
- Ranges shown as ranges (15-20, 4-10): honest forecasting.
- Key message per slide; detail goes to `data-speaker-notes` on the section, never crammed on-slide.
- Account names as clean text, never logos. Per-person data never on slides.
- Placeholder slides: coral dashed outline badge "Placeholder/Open · owner".
- Every numeric slide ends with a 17px source footnote.

## 6. Build mechanics
- One `.dc.html`, inline styles only, `<section data-screen-label>` per slide, Libre Franklin (via the bound design system's `tokens/fonts.css`, or Google Fonts when unbound).
- Keep an embedded `<script type="application/json" id="speaker-notes">` array aligned to section order for PPTX export; regenerate it whenever slides are added/removed/reordered.
- Export: `gen_pptx` at 1280×720, one entry per section.
