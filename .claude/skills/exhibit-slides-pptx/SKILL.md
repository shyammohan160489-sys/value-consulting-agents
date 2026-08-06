---
name: exhibit-slides-pptx
description: THE DEFAULT skill for ALL PowerPoint/PPTX decks (ratified by Shyam, 28 Jul 2026). Build a Backbase exhibit-style PPTX deck (white slides, hairline chrome v3.1 with right rail, action-sentence titles, one exhibit per slide, navy #071224 / blue #4066F5, source footnotes) using the locked python-pptx engine bundled with this skill. Use for EVERY deck/slides/PPT request — "exhibit deck", "McKinsey style", "VC-track", "the SNB/BACB style", or just "make me a deck" — unless the user EXPLICITLY asks for Frontline 2026 branded layouts (/frontline-slides-pptx, on request only).
---

# Exhibit Slides PPTX — the locked exhibit-style deck builder

Produce a client-ready PPTX in the Backbase exhibit style: white slides, full-bleed hairlines,
the step glyph, a blue kicker + full-sentence action title, ONE exhibit per slide, a navy
one-line takeaway band, and a source footnote on every numeric slide. Google Slides-safe.

The style is **LOCKED**. It was validated live on client decks (BACB close, SNB Capital) and
survived partner-level review and Google Slides round-trips. Your job is to pour new content
into it — never to restyle it. If you find yourself picking a new hex value, font, coordinate,
or decorative idea, stop: that is the one thing this skill exists to prevent.

## Evidence pre-flight (mandatory — Shyam, 6 Aug 2026)

Before drafting content (this step is about substance, not style — the visual lock below is untouched):
read `knowledge/domains/ai-value-evidence/` plus the relevant `knowledge/domains/<domain>/`, and embed the
verified market evidence that supports this deck's story — cited to the primary source (bank disclosure,
named analyst report), never to an aggregator. Where a value proposition has NO external validation, do not
stretch research to cover it: carry it with demonstration instead (prototype, design, journey exhibit) and
keep the claim honest. Unverified (⚠️) items never enter client assets.

## Which lane — exhibit or Frontline?

**This skill is the DEFAULT for every PPTX** (Shyam, 28 Jul 2026 — supersedes the
CLAUDE.md Frontline-default for PPTX on this fork). Two design lanes exist and they
never blend:

| | **Exhibit lane (this skill) — DEFAULT** | **Frontline 2026 lane — on explicit request** |
|---|---|---|
| Look | White, hairlines, McKinsey exhibits | Branded Frontline layouts |
| Palette | `#071224` navy / `#4066F5` blue | `#041326` navy / `#3367FF` blue |
| Use for | Every PPTX deck unless told otherwise | Only when the user names Frontline/branded |
| Skill | this one | `/frontline-slides-pptx` |

Never mix tokens between lanes. Do not ask which lane — build exhibit unless the user
explicitly asked for Frontline.

## Workflow

1. **Read the content input** (transcript, notes, bullets, upstream outputs). Draft the
   storyline first as a list of action titles — each a full sentence a person would say out
   loud. If the titles don't tell the story on their own, fix the storyline before building.
2. **Pick one exhibit per slide** from `references/exhibit-catalog.md`. Match the exhibit to
   the content shape (ranked magnitudes → sorted bars; "x of y" → dot grid; plan → waves).
   Never invent a new visual grammar mid-deck. The richest exemplars are the SNB Capital
   builds (`Engagement/SNB Capital/Output/build_snbc_vc_pptx.py` and
   `build_snbc_journey_maps_pptx.py`) — the look Shyam ratified as default; lift slide
   functions from there before composing from scratch.
3. **Write the build script.** Copy `scripts/example_build.py` next to your output as
   `build_<deck>_pptx.py` and compose slide by slide. The example imports the engine with
   `sys.path.insert(0, <dir of the script>)` — when your copy lives outside the skill
   folder, point that insert at this skill's `scripts/` directory instead, or the import
   fails. All chrome comes from `d.chrome() / d.footnote() / d.takeaway_band() /
   d.divider() / d.open_badge() / d.chip()` — never hand-draw chrome. Chrome v3.1
   draws the right rail automatically. Title sizing: `chrome()` defaults to 25pt
   (the standard); 28.5 only for short punch titles (<=48 chars).
4. **Run it** (`python3 build_<deck>_pptx.py out.pptx`; needs `python-pptx`). Fix overflow by
   cutting words or switching to a denser exhibit — never by shrinking type below the scale.
5. **QA against the checklist** below, then deliver the `.pptx` plus the build script (the
   script IS the editable source; keep it next to the output).

Only read `references/chrome-spec.md` when you need to verify a detail or extend the engine —
the engine already implements it.

## Content and voice rules (same weight as the geometry)

- **Action titles are full sentences**, short and human, with a trailing period. The test:
  say it aloud — if you wouldn't say the sentence to the room, it doesn't go on the slide.
- **Titles: ONE line, <=63 chars at 25pt** (SNB law, ratified). Never let a title wrap —
  shorten the sentence, never shrink the type.
- **Footnotes: ONE line** (~<=175 chars at 9.5pt), two sentences max.
- Short sentences. Periods, not semicolon chains. No stacked triads. No consultant
  abstractions. No emoji. Em dashes and "X, not Y" contrasts: avoid by default — at most
  ONE deliberate beat per slide, and only when it passes the say-it-aloud test
  (SNB Capital practice, ratified 28 Jul 2026).
- Sentence case everywhere; only labels uppercase. Halve the first draft's word count.
- **Takeaway bands: exactly ONE sentence fitting ONE line.** If it wraps, cut words.
  Use a band when the slide needs its punchline stated; a full slide with a clear
  message can go without (the example omits it on the sorted-bars slide).
- Ranges shown as ranges (15-20): honest forecasting. Currency in euros unless natively other.
- Every numeric slide ends with a numbered source footnote. Assumed/outside-in numbers get
  the coral dashed badge and an owner — never presented as verified.
- Key message on the slide; detail goes to speaker notes, including DEFENSE lines (what to
  say when a number is challenged, and the reconciliation if the client's figure differs).
- Account names as clean text, never logos. Per-person data never on slides.

## QA checklist (run before delivering)

- [ ] Every slide: chrome present (incl. right rail), action title is a full sentence with a period
- [ ] Titles ONE line each; footnotes ONE line each
- [ ] One exhibit per slide, max 2-3 callouts, nothing overflowing the footnote hairline
- [ ] No shape's bottom edge touches the footnote hairline (keep >=0.06in clearance)
- [ ] Takeaway bands one line each; no em dashes anywhere in the deck
- [ ] Every numeric slide has a source footnote; assumptions badged coral with an owner
- [ ] At most ONE plain table in the whole deck (T13)
- [ ] Speaker notes on every content slide, DEFENSE lines on number slides
- [ ] Rendered once and eyeballed (open the file, or convert a slide to PNG if headless)
- [ ] Saved via `d.save()` (runs the flatness/strip pass that keeps Google Slides clean)

## Files in this skill

- `scripts/exhibit_pptx.py` — the engine: palette, chrome v3, primitives, save pass. Locked.
- `scripts/example_build.py` — runnable 6-slide neutral example; copy as your starting point.
- `references/exhibit-catalog.md` — the validated exhibit patterns and when to use each.
- `references/chrome-spec.md` — the XML-verified chrome numbers (verification only).
- `assets/backbase_logo_black.png` — footer wordmark (light slides).
- `assets/backbase_wordmark_white.png` — wordmark for dark covers/dividers if an image is preferred over text.

If the engine genuinely cannot express a needed exhibit, compose it from the primitives in
the same grammar (hairlines, tint fills, blue accents, flat shapes) — and keep the chrome
untouched. Do not modify `exhibit_pptx.py` per deck.
