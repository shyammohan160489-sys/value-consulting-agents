# Visual grammar v4: the Claude Design look, measured

Source: `Engagement/Nedbank/Input/vc-report-18sept/Nedbank_ENBI_Voice_VC Report_18Sep26.pptx`
(68 slides, Google Slides export of a Claude Design deck, 13.333 x 7.5 in). Every number below
was read from the slide XML with python-pptx on 18 Sep 2026 (mining round 6). Inches on the
13.333 x 7.5 canvas unless stated. Colours are hex. The engine implements this as the `v4` look:
`ExhibitDeck(look='v4')`. The v3 look (locked 28 Jul 2026) is untouched and stays the default.

The deck was assembled from two sources. 63 slides are the Claude Design export; slide 61 (the
mutual plan) was built with our engine and inserted. Where the two differ, the export wins.

## 1. Frame (63 of 68 slides carry it)

| Element | Geometry | Style |
|---|---|---|
| Top rule | (0, 0.573) to (13.333, 0.573) | `D2D4D8`, 0.01 in tall rect (a 0.75pt line renders the same) |
| Left rail | (0.573, 0) to (0.573, 7.042) | same |
| Bottom rule | (0, 7.042) to (13.333, 7.042) | same |
| Right rail | none | the v3 right rail at 12.760 is absent in v4 |
| Corner mark | box (0.406, 0.406, 0.167 x 0.166) | the step glyph in `3366FF` (a square with its top-left quadrant removed), inner corner at the rule crossing. The export carries it as a PNG; the engine draws the custGeom glyph |
| Backbase wordmark | (11.35, 7.185, 1.067 x 0.173) | `assets/backbase_logo_black.png` (481 x 78 px, the same asset as v3) |
| Page number | (12.55, 7.16, 0.58 x 0.21) | 9pt `6E7B91`, left-aligned, no divider hairline |
| Client logo | (12.60, -0.08, 0.60 x 0.69) | PNG top right, on 64 of 68 slides (every content slide, the cover carries it at (1.19, 1.76) instead). The export stretches a square logo into the 0.60 x 0.69 box; the engine fits it inside the box and keeps its aspect |
| Kicker | (1.00, 0.86, 8.0 x 0.20) | 9pt `091C35` uppercase, tracked (+60) |
| Title | (1.00, 1.10, 12.26 x 0.45) | 28pt (27.75 to 27.98 in the XML) `091C35`, REGULAR weight, one line, no trailing period |
| Footnote | (1.00, 6.55, 11.95 x 0.42) | 8.5pt `6E7B91` (some pages 7.5pt `091C35` at 6.50), no hairline above it |

Every text run in the export is regular weight (`b="0"`). The v4 look has no bold anywhere on a
content slide. Weight is carried by size and colour instead.

## 2. Type scale (pt, Libre Franklin, all regular)

| Role | Size | Colour | Notes |
|---|---|---|---|
| Title | 28 | `091C35` | one line, 12.26 in wide box |
| Cover title | 54 | `FFFFFF` + accent word | one line |
| Divider title | 40 | `FFFFFF` | on the blue band |
| Big number, tinted card | 33 | `3366FF` | 25.5 when the string is long ("98% → 20%") |
| Big number, dark card | 33 or 25.5 | `69FEFF` | |
| Stat trio number | 34 | `091C35`, highlighted column `3366FF` | |
| Statement (vision band) | 30 | `091C35` + accent runs | |
| Companion number (tinted hero row) | 22.5 | `3366FF` | |
| Question number | 25.5 | `3366FF` | |
| Option value | 19.5 | `FFFFFF` on dark, `091C35` on light | |
| Chart value / effort value | 15 | `091C35` or `3366FF` | |
| Option name / wave name | 16.5 / 15 | | |
| Mini-stat value | 13.5 | `091C35` | 8.25pt suffix in `3366FF` for deltas |
| Statement line under an exhibit | 12 | `091C35` + `3366FF` runs | |
| Pillar name / row label | 11 / 11.5 | `3366FF` / `091C35` | |
| Card title | 9 | `091C35` on light, `FFFFFF` on mid and dark | 8 on the 0.50 in system tile |
| Body in cells | 9 | `091C35` | |
| Kicker | 9 | `091C35` | uppercase, tracked |
| Count badge | 8.5 | as the card title | right-aligned, box 0.44 wide |
| Section label | 8.5 (7.9 on dense pages) | `55647E` uppercase | the label above an exhibit |
| Footnote / legend / page number | 8.5 | `6E7B91` (legend `55647E`) | |
| Lane label | 8 | `3366FF` uppercase, sub 8 `55647E` | |
| Card sub-line | 7.5 | `55647E` on light, `DDE5FF` on mid and dark | |
| Mini-stat label | 7.5 | `091C35` uppercase | |
| Who-signs status | 7 | `3366FF` | |

Nothing below 7pt anywhere in the deck.

## 3. Colour ramp actually used

Solid fills, counted over 68 slides: `3366FF` 228 · `D2D4D8` 220 (frame and inner rules) ·
`091C35` 183 · `F3F6F9` 150 · `E5EBFF` 146 · `7D9DFF` 96 · `E3E8EF` 90 · `C9D1DC` 69 ·
`FFFFFF` 66 · `D6DBE6` 38 · `E4E8F0` 18 · `26BC71` 8 · `C4D2FF` 7 · `69FEFF` 6 · `2E4A7A` 5.

Text colours: `091C35` 1538 · `3366FF` 340 · `55647E` 330 · `FFFFFF` 174 · `6E7B91` 58 ·
`69FEFF` 18 · `DDE5FF` 14 · `7D9DFF` 7 · `FF503C` 5.

Lines: `D6DBE6` 0.75pt (faint card borders, 72) · `3366FF` 0.75pt (outline chips, 46) ·
`9AA6B8` 0.75pt dashed (comparison-only cards, 23) · `7D9DFF` 0.75pt dashed (future nodes, 19) ·
`E3E8EF` 0.75pt (question and option card borders, 18) · `C9D1DC` dashed 15 · `091C35` dashed 9.

The v4 palette in the engine:

| Token | Hex | Used for |
|---|---|---|
| NAVY | `091C35` | ink, dark cards, committed bars |
| BLUE | `3366FF` | accent, big numbers, active cards, chart lead bars, divider band |
| BLUE2 | `3366FF` | same as BLUE (v4 has no deep blue) |
| BLUE3 | `7D9DFF` | the mid weight, "next" bars |
| BLUE4 | `C4D2FF` | light bars, future nodes and the future stretch of a timeline |
| TINT | `E5EBFF` | light cards, "with" cells, highlight panels |
| TINT2 | `F3F6F9` | faint cards and panels, who-signs chips |
| GREY | `C9D1DC` | "today" reference bars, done nodes |
| CYAN | `69FEFF` | numbers and labels on dark, the recommended badge |
| SUB_D | `DDE5FF` | sub-lines on dark and mid cards |
| MUT | `55647E` | muted body, labels, legends |
| FN | `6E7B91` | footnotes, page number |
| HAIR | `D2D4D8` | frame rules, chart baselines drawn light |
| CARD_LINE | `D6DBE6` | faint card border, vertical separators |
| LINE_SOFT | `E3E8EF` | question and option card border |
| HAIR_ROW | `E4E8F0` | row rules in lane tables |
| DASHC | `9AA6B8` | dashed comparison-only outlines |
| CORAL | `FF503C` | the one warning colour (5 runs in 68 slides) |
| COVER_LINE | `6B7786` | the cover frame lines |

Greens (`26BC71`, `1B6B4F`, `008533`, `D9EAD3`) are the client's brand accent on this deck (the
vision band, the cover's accent word, the "revenue on top" bars). They are not part of the
palette. A client accent is passed per call (`accent=`), never added to the engine.

## 4. The fill-weight rule (slide 15 and its legend "Reused by")

Weight is a count, and the count picks the fill. Four steps on slide 15, one more for "active":

| Weight | Fill | Border | Title and badge | Sub-line | Slide 15 meaning |
|---|---|---|---|---|---|
| faint | `F3F6F9` | `D6DBE6` 0.75 | `091C35` | `55647E` | 1 or 2 intents |
| light | `E5EBFF` | none | `091C35` | `55647E` | 3 to 8 |
| mid | `7D9DFF` | none | `FFFFFF` | `DDE5FF` | 9 to 16 |
| dark | `091C35` | none | `FFFFFF` | `DDE5FF` | 17 to 22, all of them |
| blue | `3366FF` | none | `FFFFFF` | `FFFFFF` | the active step (slide 14 "Enbi decides") |
| outline | `FFFFFF` | `D6DBE6` 0.75 | `091C35` | `55647E` | someone else's stack (slide 14) |
| dashed | `FFFFFF` | `9AA6B8` 0.75 dashed | `091C35` | `55647E` | comparison only, not offered |

Rule: the heaviest items go navy, the middle band goes blue (`7D9DFF` here), the rest stays in
tints. Never more than one dark weight per band of meaning. The legend sits under the exhibit at
y=6.40: "Reused by" 8.5pt `55647E`, 0.16 in swatches, labels 8.5pt, a right-aligned note in
`6E7B91` ending at x=12.60 ("Number = how many of the 22 intents use the box").

Bars follow the same ramp: `C4D2FF` for today or the reference, `93AEFF` / `7D9DFF` for the
middle state, `3366FF` for the target, `091C35` for the committed total. Grey `C9D1DC` marks
"today, as is" when it must not read as a Backbase state (slides 31, 37, 40).

## 5. Card geometry

**The 0.62 card (slide 15).** Box w x 0.62. Unit width 1.62, gap 0.11, a double card is 3.35
(2 x 1.62 + 0.11). Title 9pt at (x+0.10, y+0.07, w-0.37 x 0.21). Count badge 8.5pt right-aligned
in a 0.44 box at (x+w-0.50, y+0.05). Sub-line 7.5pt at (x+0.10, y+0.29, w-0.16 x 0.22), two lines
allowed (0.39 tall). Lane pitch 0.75 (0.62 + 0.13).

**The 0.50 system tile (slide 15, last lane).** 1.20 x 0.50, gap 0.10 (pitch 1.30), eight across.
Title 8pt at (x+0.10, y+0.07, 0.83 x 0.21, two lines 0.38). Badge as above. No sub-line. Row
pitch 0.56.

**Lane label column.** Label 8pt `3366FF` uppercase at (1.00, y+0.06); sub 8pt `55647E` at
(1.00, y+0.25). Cards start at x=2.55 (label column 1.55 wide).

**Stat block (slide 6).** 2.73 x 2.22, four across at pitch 2.875 (gap 0.145), two rows at pitch
2.36 (gap 0.14). Fill `F3F6F9` (no border) or `091C35`. Icon 0.25 x 0.25 at (x+0.21, y+0.21).
Number 33pt at (x+0.21, caption_y-0.56, 2.54 x 0.50), `3366FF` on tint, `69FEFF` on dark. Caption
9pt `091C35` / `FFFFFF`, 2.40 wide, bottom-anchored so that its last line ends 0.17 above the card
bottom (two lines: caption at y+1.66, number at y+1.10; three lines: y+1.48 and y+0.92; one line:
y+1.84 and y+1.28).

**Hero number (slides 27, 37, 45).** Side layout: `091C35` block 5.83 x 0.83; number 33pt
`69FEFF` at (x+0.21, y+0.19, 2.63 x 0.50); caption 9pt `FFFFFF` at (x+2.77, y+0.24, 2.94 x 0.39).
Tinted companions under it: `F3F6F9` 5.83 x 0.72, number 22.5pt `3366FF`, caption 9pt `091C35`.
Stack layout: `091C35` 3.65 x 1.28; number at (x+0.21, y+0.21); caption 9.4pt at (x+0.21, y+0.71).

**Mini stat (slides 31, 44).** Label 7.5pt uppercase `091C35` (0.17 tall), value 13.5pt at
y+0.12 (0.26 tall), optional 8.25pt suffix (`3366FF` for a delta, `091C35` for a unit). Two mini
stats side by side at pitch 1.66.

**Three-state panel (slide 31).** `F3F6F9` 3.63 x 4.38, three at pitch 3.86 (gap 0.23), inset
0.21. Label 7.9pt uppercase (`091C35` today, `3366FF` for the next states) at y+0.19; sub 8.25pt at
y+0.35; body 9pt at y+0.63. A bar 0.94 wide whose height is proportional to the price (4.66 in per
dollar) stands on a `D2D4D8` rule; the number (33pt) sits at rule_y-0.83 to the right of the bar
(bar_x+1.08), its caption 7.9pt at rule_y-0.33. Then two mini stats, a rule, one more mini stat.
Bars: `C9D1DC` today, `7D9DFF` next, `3366FF` beyond.

**Film frame (slide 22).** 16:9 image 2.20 x 1.24, five across at pitch 2.35 (gap 0.15). Tag:
`091C35` box 0.95 x 0.30 at the image's bottom-left, "film" 8.5pt `FFFFFF` at (x+0.08, y+h-0.27).
Caption 9pt `091C35` at (x, y+h+0.10); sub 8pt `55647E` at (x, y+h+0.56, w x 0.41).

**Option card (slide 44).** 3.65 x 4.17, three at pitch 3.855. Recommended = `091C35` with a
`69FEFF` badge chip (0.92 x 0.20, 7.9pt `091C35` text) top right; plain = `F3F6F9` + `E3E8EF`
border; comparison only = `FFFFFF` + `9AA6B8` dashed with an outlined badge. Inset 0.23. Tag
8.25pt uppercase at y+0.25; name 16.5pt at y+0.57; body 9pt at y+0.99; two mini stats (7.9 / 19.5)
at y+1.55; rule at y+2.16; "per resolved conversation" 7.9pt at y+2.29; two 0.15 tall bars at
y+2.50 and y+2.73 with 9.75pt labels after them; note 9.4pt at y+3.57.

**Question card (slide 48).** 2.75 x 2.38, four across at pitch 2.87, two rows at pitch 2.51.
`F3F6F9` + `E3E8EF` border; one dashed (`9AA6B8`), one dark for "how to read". Number 25.5pt
`3366FF` at (x+0.18, y+0.18); outlined page chip (`3366FF` 0.75, 7.5pt) top right at y+0.34; title
10.5pt at y+0.61; body 8.6pt at y+0.88.

**Who-signs chip (slide 61).** `F3F6F9` rounded 1.50 x 0.64, six at pitch 1.585 from x=3.10.
Role 8pt `091C35` at (x+0.10, y+0.06); status 7pt `3366FF` at (x+0.10, y+0.41).

## 6. Recipes, one per slide type

Kicker and title come from `d.chrome()` in every recipe. "Section label" means 8.5pt `55647E`
uppercase above the exhibit.

1. **Cover (slide 1).** Full navy page (the export uses a dark image; the engine uses solid
   `091C35`). Frame lines `6B7786` 0.5pt: top (0.55, 1.62) to (12.79, 1.62); inner vertical
   x=8.64 full height; inner horizontal (0.55, 5.20) to (8.64, 5.20); left x=0.55; right x=12.78.
   White glyph at (8.47, 1.62). Wordmark top left at (0.60, 0.42). Client logo (1.19, 1.76, 0.60
   x 0.69). Kicker 9.5pt white tracked at (1.09, 2.45). Title 54pt white at (1.06, 3.00), one
   accent word (client colour, default cyan). Date line 12pt white at (1.00, 5.71).
   Engine: `d.cover_page(kicker, runs, date_line)`.
2. **Vision band (slide 2).** No kicker or title. Band (0.57, 1.85, 12.20 x 3.70) in a tint
   (client tint on the reference; default `E5EBFF`), with two white notches cut out of it: top
   left (0.58, 1.85, 3.69 x 0.55) and bottom right (10.00, 5.10, 2.77 x 0.45). Kicker 9pt inside
   the top notch at (1.00, 2.03). Statement 30pt `091C35` at (1.00, 2.85, 11.12 x 1.47) with the
   claim's core in the accent colour. Engine: `d.vision_band(s, kicker, runs)`.
3. **From-to shift (slide 3).** Two columns of bullet lines at x=1.00 and 7.40, 5.10 wide, pitch
   0.66: left in `55647E` (from), right in `091C35` with `3366FF` bullets (to). Column labels
   8.5pt uppercase at y=2.17. A `D6DBE6` vertical rule at x=6.60 with a 22pt `3366FF` arrow on it.
   Under a rule at y=5.15: a pillar row of four names 11pt `3366FF` + 8.5pt `55647E` bodies with
   vertical separators. Engine: `d.from_to_columns()` + `d.pillar_row()`.
4. **Eight-number floor (slide 6).** 4 x 2 stat blocks (section 5), two of them dark for the
   tension numbers. Footnote 7.5pt at 6.50. Engine: `d.stat_grid()` or eight `d.stat_block()`.
5. **Stacked-bar intents (slides 7, 34).** Slide 7: one full-width share bar 0.85 tall at y=2.30
   with segments `3366FF` / `091C35` / `C9D3E6` / `E5EBFF`, value 15pt and label 8.5pt inside
   each, three note columns under it (12.5pt lead + 10pt body) separated by vertical rules.
   Slide 34: per intent, a faint reference track ("do nothing") over a stacked bar
   (`091C35` / `3366FF` / `7D9DFF`) 0.20 tall, row pitch 0.50, labels after each bar, legend
   under. Engine: `d.share_bar()` and `d.stacked_hbars()`.
6. **Architecture grid (slide 15).** Five lanes, label column left, cards right; count badge on
   every card; weight from the count; the system lane in 0.50 tiles, eight across, two rows;
   weight legend at y=6.40. Engine: `d.lane_grid()` + `d.weight_legend()`.
7. **Moment-by-moment table (slide 18).** Header row 7.9pt uppercase at y=1.82 (the "with"
   header in `3366FF`); rows at pitch 0.80: moment label 9.4pt, a `F3F6F9` today cell 3.44 x
   0.73, a `3366FF` arrow, an `E5EBFF` with-cell, then a 15pt `3366FF` effort value with an 8.6pt
   caption. Engine: `d.compare_rows()`.
8. **Stat trio (slide 26).** Three columns at pitch 3.95: label 8.5pt uppercase, number 34pt,
   sub 11.5pt, body 9.5pt `55647E`. The middle column highlighted by an `E5EBFF` panel (x-0.20,
   y-0.22, 3.85 x 3.90) and a `3366FF` number. Engine: `d.stat_column()` x 3.
9. **Three states (slide 31).** Three panels (section 5). Engine: `d.panel()` + `d.txt()` +
   `d.rect()` bar + `d.mini_stat()`; see `example_v4_build.py` page 3.
10. **Waterfall glide path (slide 33).** Four bars 0.88 wide at pitch 1.60 whose height falls
    with the price (`C4D2FF`, `93AEFF`, `3366FF`, `3366FF`), 15pt values above, 10.5pt deltas
    under the values, a `091C35` baseline, 9pt categories; a dashed `3366FF` box marks the
    conditional state. Levers listed to the right (9.5pt lead + `55647E` body). Engine:
    `d.bars(mode='time')` with deltas, plus `d.rect(dash='dash')` for the conditional box.
11. **Roadmap timeline (slide 40).** A `D2D4D8` track 0.02 tall at y=1.97 with the committed
    stretch in `3366FF`; 0.25 square nodes at y=1.85 (`C9D1DC` done, `3366FF` go-live, `7D9DFF`
    next, dashed `7D9DFF` future); columns at pitch 2.88: tag 8.25pt `3366FF`, name 15pt, date
    8.25pt, body 8.6pt, a gate card 2.71 x 1.00 (`F3F6F9`, dark for the go-live wave) with "gate
    you own" 7.5pt. Engine: `d.wave_track()`.
12. **Options cards (slide 44).** Three option cards (section 5), the recommended one dark.
    Engine: `d.option_card()` x 3.
13. **Questions grid (slide 48).** Seven numbered cards plus one dark "how to read" card in a
    4 x 2 grid (section 5). Engine: `d.numbered_card()` x 8.
14. **Mutual-plan timeline (slide 61).** Seven nodes on a line at y=2.45 (`091C35` 1.2pt to the
    last committed node, `C4D2FF` after it); dates 8.5pt `55647E` uppercase at y=2.00; node
    titles 9.5pt at y=2.62; two owner lanes with `E4E8F0` rules at y=3.08 and 4.36 (lane names
    10pt + 7.5pt sub at x=1.00; texts 7.5pt `55647E` in 1.33 wide columns); a `D6DBE6` rule at
    y=5.56; a who-signs row at y=5.66 with six chips; footnote at 6.48. Engine:
    `d.timeline_lanes()` + `d.who_signs()`.
15. **Appendix divider band (slide 62).** Full `3366FF` page. White 0.5pt rules: y=1.62 from
    x=0 to 12.79; y=4.86 from 0.55 to 12.79; x=0.55 and x=12.78 full height. White glyph at
    (0.38, 1.45). Title 40pt white at (1.11, 3.0). Engine: `d.divider_band(title)`.
16. **Film frame (slide 22).** Five film frames (section 5) at y=2.25; a 10pt statement line at
    y=5.15 (`091C35` lead + `55647E` rest); footnote at 6.55. Engine: `d.film_frame()` x 5.

Also measured, no recipe needed: agenda rows (slide 5: 15pt `3366FF` numbers, 11.5pt lines,
`D6DBE6` rules at pitch 0.78, `d.numbered_rows()`); six-step flow (slide 14: 1.72 x 2.10 cards at
gap 0.26 with 12pt arrows between them, `d.step_flow()`); minute-by-minute block bars (slide 63:
0.32 tall blocks, one block one minute, 8.5pt numbers inside).

## 7. What v4 changes against v3, in one table

| | v3 (locked, default) | v4 (Claude Design look) |
|---|---|---|
| Palette | `071224` / `4066F5` | `091C35` / `3366FF` (section 3) |
| Frame | four rules incl. the right rail | three rules, no right rail |
| Kicker | 13.5pt blue | 9pt navy, tracked |
| Title | 25pt bold, trailing period | 28pt regular, no period |
| Footer | wordmark + divider + 12.75pt bold page number | wordmark + 9pt grey page number |
| Client logo | never | top right on every content slide, cover at (1.19, 1.76) |
| Footnote | hairline + 9.5pt | no hairline, 8.5pt at 6.55 |
| Bold | titles, leads, values | none |
| Takeaway band | navy band with cyan lead | rare; the so-what sits in a hero number or a statement line |
