---
name: exhibit-slides-pptx
description: THE DEFAULT skill for ALL PowerPoint/PPTX decks, now the APEX design system (Apex ratified by Shyam 24 Sep 2026; exhibit style ratified 28 Jul 2026). Build a Backbase PPTX in the Apex look, the Claude Design look measured from production decks (white slides, three-rule hairline frame, 9pt navy kicker, 28pt regular titles, no bold, tinted cards, hero numbers, navy #091C35 / blue #3366FF, client logo on client decks only, source footnotes, human voice) with the locked exhibit engine. v3 chrome (#071224 / #4066F5) only for continuity with an account's existing deck series; Frontline only when explicitly named. Trigger on deck, slides, presentation, PPTX, PowerPoint, Apex, board deck, readout, "the Claude Design look".
---

# Apex — the default PPTX design system (engine: exhibit-slides-pptx)

Apex is the look of a Claude Design deck, measured and rebuilt as engine recipes so every deck
gets it without a Claude Design round-trip: white slides, a three-rule hairline frame with the
step glyph, a 9pt navy kicker, a 28pt regular title without a period, ONE exhibit per slide,
tinted cards and dark hero numbers carrying the weight (no bold anywhere), a statement line for
the so-what, a source footnote on every numeric slide, the Backbase wordmark and a grey page
number in the footer, and the client's logo top right on client decks. Google Slides-safe.

Lineage: the exhibit style (BACB close, SNB Capital) was ratified as the default on 28 Jul 2026
and locked as chrome v3. On 18 Sep 2026 the Claude Design look was measured from the Nedbank
ENBI Voice VC report (68 slides, XML-read) and implemented as `look='v4'`; on 24 Sep 2026 Shyam
named it **Apex** and made it the default for every new deck. The engine keeps v3 as its own
default so older build scripts render unchanged; the SKILL builds new decks on Apex.

The look is **LOCKED**. Your job is to pour new content into it, never to restyle it. If you
find yourself picking a new hex value, font, coordinate or decorative idea, stop: that is the
one thing this skill exists to prevent.

## Evidence pre-flight (mandatory — Shyam, 6 Aug 2026)

Before drafting content (this step is about substance, not style; the visual lock is untouched):
read `knowledge/domains/ai-value-evidence/` plus the relevant `knowledge/domains/<domain>/`, and
embed the verified market evidence that supports this deck's story, cited to the primary source
(bank disclosure, named analyst report), never to an aggregator. Where a value proposition has NO
external validation, do not stretch research to cover it: carry it with demonstration instead
(prototype, design, journey exhibit) and keep the claim honest. Unverified (⚠️) items never enter
client assets.

## Which look

| | **Apex (this skill) — DEFAULT** | **v3 exhibit chrome — continuity only** | **Frontline 2026 — on explicit request** |
|---|---|---|---|
| Call | `ExhibitDeck(look='apex')` | `ExhibitDeck()` | `/frontline-slides-pptx` |
| Palette | `#091C35` navy / `#3366FF` blue / tints `#E5EBFF` `#F3F6F9` | `#071224` / `#4066F5` / cyan `#93FBFE` | `#041326` / `#3367FF` |
| Frame | three rules, no right rail, grey page number | four rules incl. right rail, bold page number | branded layouts |
| Weight | none: size and colour carry it | bold titles, leads, values | Frontline type |
| Use for | every new deck | a deck added to an account series already on v3, mid-cycle (SNB Capital, BACB) | only when the user names Frontline |

Never mix tokens between looks. Do not ask which look: build Apex unless the deck extends an
existing v3 series or the user names Frontline. Nedbank's own decks moved to the Claude Design
look in September 2026, so new Nedbank decks are Apex.

## The Apex look, measured (`references/visual-grammar-v4.md` has every number)

| Element | Apex |
|---|---|
| Frame | rules `D2D4D8` at y 0.573, x 0.573, y 7.042; step glyph at (0.406, 0.406) in blue |
| Kicker | 9pt navy, uppercase, tracked, at (1.00, 0.86): `01 · WHAT WE FOUND` |
| Title | 28pt regular navy at (1.00, 1.10), one line, no trailing period |
| Footer | black wordmark at 11.35 + 9pt grey page number at 12.55; no divider |
| Footnote | 8.5pt `6E7B91` at y 6.55, no hairline above it |
| Cards | `F3F6F9` faint · `E5EBFF` light · `7D9DFF` mid · `091C35` dark; 9pt titles, 7.5pt sub-lines, count badges |
| Numbers | 33pt blue on tint, cyan `69FEFF` on dark; 13.5pt mini-stats with 8.25pt suffixes |
| So-what | a hero number or a 12pt statement line (navy lead, blue rest); a takeaway band is rare |
| Client logo | top right of every content slide at (12.60, -0.08, 0.60 × 0.69); cover at (1.19, 1.76) |
| Pages | `cover_page` (navy, offset frame, accent word), `divider_band` (blue), `vision_band` (tint band with notches) |

## Client logo rule (Shyam, 24 Sep 2026)

- **Client deck** (anything an account will see): the client's logo on the cover and top right
  of every content slide, via `ExhibitDeck(look='apex', client_logo=X.client_logo("<Client>"))`.
  The one place it lives (Shyam, 25 Sep 2026): **`Engagement/<Client>/Input/brand-assets/`**, a
  PNG or JPG with "logo" in its name. `X.client_logo()` returns None when nothing is there: then
  **ask for the logo before building**; never draw a placeholder into a client deck and never
  use another organisation's mark. When the bank's own deck carries the mark, extract it into
  brand-assets first (python-pptx `shape.image.blob`).
- **Internal deck** (enablement, team, QBR, events, POVs for our own teams): no client logo.
  Mark it `d.tag_chip(s, "Internal · <what>", kind="quiet")` top right instead.
- The engine fits the logo inside the box and keeps its aspect; the Claude Design export
  stretched it, and the fitted version is the one to ship.

## The chart standard (Apex v4.2, 25 Sep 2026)

The report's charts are the standard: clean, drawn from flat shapes, the value beside or above
the bar, no axes, no gridlines, no native chart objects, regular weight. Every form below is a
measured recipe (`references/exhibit-catalog.md` T56–T67); `scripts/example_apex_charts_build.py`
rebuilds the reference pages line for line.

| Claim shape | Recipe | Engine |
|---|---|---|
| Ranked magnitudes | horizontal bars, value after the bar, legend row | `d.hbar_rows` + `d.legend` |
| Composition per row (minutes, cost) | stacked horizontal rows with a volume column | `d.hstack_rows` |
| Today against released, per row | paired horizontal rows (tint reference, blue result) | `d.paired_hrows` |
| A funnel, today against with-us | thin paired bars per step with a change column | `d.funnel_rows` |
| A trend or a walk across states | columns, values above, muted deltas, dashed estimates | `d.bars` (Apex weight) |
| A cost walk with the lever beside each step | column pairs on one baseline | `d.column_walk` |
| Pay against get, by year | grouped stacked columns with totals and a legend | `d.stacked_columns` |
| One share of one whole, one row | share bar, values inside, total under the right end | `d.share_bar` |
| One share of one whole, a circle | donut with the total in the hole; thickness 1.0 = pie | `d.donut` |
| A population split | proportional block with labels beside each part | `d.area_block` |
| The KPIs beside a chart | rule, uppercase label, 24pt value, 9pt body, repeated | `d.kpi_stack` |
| Production proof | a ledger with a resolution bar per deployment and the hero number beside it | `d.proof_ledger` + `d.hero_column` |
| Where the work sits on the loop | value-pool chips on the autonomy rows, the hero count beside them | `d.loop_matrix` + `d.hero_column` |
| The team, the close | photo column with names; the navy close with the glow | `d.team_page`, `d.closing_page` |

Colour semantics on every chart: BLUE = the lead or our state, NAVY = the second series or a
committed figure, BLUE3 and BLUE4 = the next states, TINT = a reference or a fee, GREY = today's
reference, dashed outline = an estimate or a state not yet certified, CORAL only as a warning.
Never green, never a gradient, never a 3D or shadowed shape.

## Workflow

1. **Read the content input** (transcript, notes, bullets, upstream outputs). Then draft the
   storyline BEFORE any slide: pick the archetype and write the title chain per
   `references/storyline-patterns.md` (six archetypes + title grammar), and run its **flip
   test**: the titles read alone, in order, must argue the whole case. Each title is a claim a
   person would say out loud. If the titles do not tell the story on their own, fix the chain
   before building.
2. **Pick one exhibit per slide** from `references/exhibit-catalog.md`: the Apex recipes
   (T40–T55) first, then the data layer (T17–T23), comparison layer (T24–T29) and evidence
   layer (T30–T39). Match the exhibit to the content shape (eight numbers → stat grid; "built
   once, reused" → lane grid with count badges; options → option cards; a plan → timeline lanes
   + who signs; ranked magnitudes → bars). **Form follows message:** a magnitude, trend, ranking,
   share or distribution is a drawn chart, never boxes; boxes carry structure, sequence and
   quality comparisons. Never invent a new visual grammar mid-deck. The richest exemplars are
   `scripts/example_v4_build.py` (four Nedbank pages rebuilt line for line) and the first live
   Apex deck, `Engagement/_enablement/conversational-banking-gtm/company-view/build_cb_company_view_apex_pptx.py`
   (14 slides, every recipe in use); lift slide functions from there before composing from scratch.
3. **Write the build script.** Copy `scripts/example_v4_build.py` next to your output as
   `build_<deck>_pptx.py`, open with `d = X.ExhibitDeck(look='apex', client_logo=...)` (or no
   logo for internal decks) and compose slide by slide. Point the `sys.path.insert` at this
   skill's `scripts/` directory when the copy lives outside the skill folder, or the import
   fails. All chrome comes from `d.chrome() / d.footnote() / d.statement_line() /
   d.cover_page() / d.divider_band() / d.vision_band()`; never hand-draw chrome. Read colours
   from `d.pal` (`d.pal.NAVY`, `d.pal.BLUE`, ...), never from hard-coded hex. Icons for stat
   blocks and cards come from `X.icon('phone')` (the pack in `assets/icons/`).
4. **Run it** (`python3 build_<deck>_pptx.py out.pptx`; needs `python-pptx`). Fix overflow by
   cutting words or switching to a denser exhibit, never by shrinking type below the scale.
5. **Render and look** (mandatory since 24 Sep 2026): `soffice --headless --convert-to pdf`,
   then `pdftoppm -r 80 -png`, then a contact sheet, and read it. Check the cover title stays
   left of the inner rule, captions are not squeezed, nothing crosses the footnote.
6. **QA against the checklist** below, then deliver the `.pptx` plus the build script (the
   script IS the editable source; keep it next to the output).

Only read `references/chrome-spec.md` (v3) or `references/visual-grammar-v4.md` (Apex) when you
need to verify a detail or extend the engine; the engine already implements both.

## Content and voice rules (same weight as the geometry)

- **Titles are claims**, short and human, 28pt regular, ONE line, about 60 characters at most,
  **no trailing period** (Apex). The test: say it aloud; if you would not say the sentence to
  the room, it does not go on the slide. Numbers go into the title when the claim is numeric.
- **Kickers count the chapter**: `01 · The shift`, `02 · What we sell`; serial kickers count
  the series ("3 of 9").
- **Footnotes**: 8.5pt at y 6.55, at most two lines (about 230 characters), numbered sources.
- **Statement lines** carry the so-what: a navy lead of a few words, a blue remainder, one
  sentence, one line. Use a hero number when the so-what is a figure.
- Short sentences. Periods, not semicolon chains. No stacked triads. No consultant
  abstractions. No emoji. No em dashes. "X, not Y" contrasts: avoid.
- Sentence case everywhere; only labels uppercase. Halve the first draft's word count.
- Ranges shown as ranges (15 to 20): honest forecasting. USD first, local currency in brackets,
  unless the deck is natively in one currency.
- Every numeric slide ends with a numbered source footnote. Assumed or outside-in numbers are
  drawn dashed (bars) or badged coral with an owner, never presented as verified.
- Key message on the slide; detail goes to speaker notes, including DEFENSE lines (what to say
  when a number is challenged, and the reconciliation if the client's figure differs).
- The client's own name stays clean text; third-party logos only on landscape and evaluation
  exhibits with supplied assets. Per-person data never on slides.

## QA checklist (run before delivering)

- [ ] Every content slide: Apex chrome (three rules, glyph, kicker, 28pt regular title, wordmark, page number)
- [ ] Client deck: client logo on the cover and every content slide; internal deck: none, `Internal` tag instead
- [ ] Titles ONE line each, no trailing period; footnotes at most two lines
- [ ] No bold anywhere; weight comes from size and colour
- [ ] One exhibit per slide, at most 2 or 3 callouts, nothing crossing y 6.55
- [ ] Every numeric slide has a source footnote; estimates dashed or badged coral with an owner
- [ ] At most ONE plain table in the whole deck
- [ ] Speaker notes on every content slide, DEFENSE lines on number slides
- [ ] Rendered to PNG and read (step 5), cover title left of the inner rule
- [ ] Saved via `d.save()` (runs the flatness/strip pass that keeps Google Slides clean)

## Files in this skill

- `scripts/exhibit_pptx.py`: the engine. v3 chrome, the data/comparison/evidence layers, and the
  Apex (v4) layer: palette, `_chrome_v4`, cards, stat grid, hero numbers, panels, cover, divider,
  vision band, film frame, option and numbered cards, step flow, compare rows, wave track,
  timeline lanes, who signs. Locked; do not modify per deck.
- `scripts/example_v4_build.py`: the Apex example, four Nedbank report pages rebuilt line for
  line for a side-by-side check. Copy it as your starting point.
- `scripts/example_apex_charts_build.py`: the chart sampler, fifteen pages: every chart recipe
  rebuilt from its reference page, the donut and pie, the two summit pages, the team page and the close.
- `scripts/example_build.py`, `example_data_build.py`, `example_charts_build.py`,
  `example_bcg_build.py`: the v3-era examples for the data, comparison and evidence layers;
  every helper in them draws in Apex tokens under `look='apex'`.
- `references/visual-grammar-v4.md`: the Apex spec, every number read from the source XML.
- `references/exhibit-catalog.md`: the exhibit patterns and when to use each (T02–T55).
- `references/storyline-patterns.md`: six deck archetypes and the title grammar.
- `references/chrome-spec.md`: the v3 chrome numbers (verification only).
- `assets/backbase_logo_black.png`, `assets/backbase_wordmark_white.png`: the wordmarks; `assets/close_bg.jpg`: the navy page with the glow for `closing_page`.
- `assets/icons/*.png`: the twelve line icons (brightness, users, headset, sparkle, person,
  route, shield_check, document, database, check, phone, phone_incoming) via `X.icon(name)`.

If the engine genuinely cannot express a needed exhibit, compose it from the primitives in the
same grammar (hairlines, tint fills, blue accents, flat shapes, regular weight) and keep the
chrome untouched. Log the gap in `knowledge/design-system/claude-design-exhibit-kit/BACKLOG.md`
so it becomes a recipe in the next mining round.
