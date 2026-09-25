# Chrome exact-spec — LOCKED (v3.1)

XML-verified against `BACB_Close_16Jul_ExhibitStyle.pptx` (16 Jul 2026) and the SNB Capital
21 Jul deck, both of which survived a Google Slides round-trip (geometry, freeform glyph and
PNG logo all preserved). v3.1 (28 Jul 2026, ratified default): adds the RIGHT rail, standard
on the SNB Capital 22 Jul + journey-maps decks. `scripts/exhibit_pptx.py` implements every
value below — this file exists so you can verify output, never so you can re-derive chrome
by hand.

**The prime rule: build from the engine, never re-derive chrome from prose.** Every past
attempt to eyeball these values produced drift that a partner-level reviewer caught.

Canvas: 13.333 × 7.5 in (= 1280 × 720 px at 96dpi). Font: Libre Franklin everywhere.

## Hairlines
- Straight connectors, `#D2D4D8`, 0.75pt, FULL-BLEED:
  - top: (0, 0.573) → (13.333, 0.573)
  - left rail: (0.573, 0) → (0.573, 7.042)
  - right rail (v3.1, standard): (12.760, 0) → (12.760, 7.042) — mirrors the left rail
  - footer: (0, 7.042) → (13.333, 7.042)
- Inner footnote hairline: x = 1.0 → 12.708.
- Strip the `<p:style>` element from every connector AND append an empty `<a:effectLst>` —
  otherwise the theme effectRef re-adds a line shadow in LibreOffice/Google renders.

## The step glyph (the Backbase mark on every slide)
- The AUTHENTIC glyph, not a plain square and not two stacked rects: a custGeom freeform,
  path units w=9168 h=9096: `M(19,4762) L(4567,4762) L(4566,0) L(9168,0) L(9168,9096) L(0,9096) Z`
  (a square with its top-left quadrant removed).
- Position: hugging the hairline crossing — box (0.406, 0.406, 0.167 × 0.166) in; the glyph's
  inner corner ends exactly at (0.573, 0.573).
- Blue `#4066F5` on white slides; cyan `#93FBFE` on dark slides.
- HTML twin equivalent: `clip-path: polygon(0 52.4%, 49.8% 52.4%, 49.8% 0, 100% 0, 100% 100%, 0 100%)`.

## Kicker + action title
- Kicker: 13.5pt REGULAR (not bold), `#4066F5`, at (1.0, 0.812), uppercase, tracked (+120).
- Title: 25pt bold navy at (1.0, 1.104), a full sentence WITH trailing period.
  Law (v3.1): ONE line, <=63 chars at 25pt. 28.5pt only for short punch titles (<=48 chars).
  Never let a title wrap — shorten the sentence instead.

## Footer ("Backbase │ N")
- WHITE footer — no navy band.
- Large BLACK Backbase wordmark PNG at (11.633, 7.185, 1.067 × 0.173) — asset
  `assets/backbase_logo_black.png`, cropped @300dpi from the June master deck. Wordmark ends at 12.700.
- Thin vertical divider `#9A9EA6`, x = 12.802, y = 7.118 → 7.367.
- Page number 12.75pt BOLD black, textbox anchored MIDDLE on the divider, x ≈ 12.87 —
  a LIVE `<a:fld type="slidenum">` field since v3.1 (mechanism from the Product Factory
  deck, Mayur PDP session, 28 Jul 2026): auto-renumbers on insert/reorder in PowerPoint
  and Google Slides; the literal digit inside the field is the build-time fallback.
  `ExhibitDeck.page_field()` builds it — never hardcode page numbers as plain text again.

## Type scale (pt, on the 13.333in canvas)
- Action title 28.5 (dense slides 25) · kicker 13.5 · lane headers ~15.75 bold
- Labels 14.25 bold navy · body 12.75 `#6A717C` · micro-labels 12.75 `#777D87`
- Footnotes 9.5–12.75 `#8F949C` (engine default 9.5) · cell hero numbers 17–22 · standalone hero stats up to 44+ light.

## Takeaway band (punchline strip)
- Navy `#071224` roundRect, ~11.708 × 0.479 at content width.
- Text 13.5–14.25: bold CYAN `#93FBFE` lead-in + regular WHITE remainder.
- EXACTLY one sentence fitting ONE line; if it wraps, cut words until it doesn't.

## Flatness (Google Slides safety)
- ALL shapes flat: explicit empty `<a:effectLst>` on every spPr; `shadow.inherit = False`.
- `<p:style>` stripped from every shape at save time (`ExhibitDeck.save()` does this pass).
- No gradients (the dark-slide glow is approximated with solid rects), no autofit, no theme fills.

## Palette (LOCKED — never invent or blend)
Navy `#071224` · primary blue `#4066F5` · secondary blues `#1F3799` `#5F7DF7` `#B5C1F1` ·
tints `#E6EBFE` `#F5F6FA` · cyan `#93FBFE` (dark-slide highlight only, never a gradient step) ·
coral `#EC5E48` (gates, risks, placeholders, illustrative-flags ONLY) · muted `#6A717C` ·
footnote `#8F949C` · hairline `#D2D4D8`.
Intensity ramp (deep→light): `#1F3799 → #4066F5 → #5F7DF7 → #B5C1F1 → #E6EBFE`.

⚠️ This palette is NOT Frontline 2026 (`#041326` / `#3367FF`). The two are separate lanes.
Never mix tokens between them (see SKILL.md "Which lane").
