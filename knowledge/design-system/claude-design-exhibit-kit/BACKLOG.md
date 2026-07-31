# Exhibit style — path to default (backlog)

*Opened 2026-07-15 (Shyam) after the BACB close deck. Maturity per the harvest ladder (example → method → template → skill → default) and Shyam's G-scale.*

**Current maturity: DEFAULT — RATIFIED 2026-07-28 (Shyam, verbal, during SNBC workshop week).** "Make this the default skill going forward — all future PowerPoint slides with this skill." The ladder is climbed: example (BACB) → template → registered skill (`.claude/skills/exhibit-slides-pptx/`) → **default for ALL PPTX on this fork** (Frontline `/frontline-slides-pptx` only on explicit request; supersedes the CLAUDE.md PPTX default here). Backlog item #5 (palette decision) resolved-for-fork the same way: exhibit palette is the default PPTX lane, no blending. Engine now v3.1: right rail standard (mirrors left, x=12.760), title law ONE line <=63 chars @25pt, `chip()` primitive, journey/workshop patterns (T16-class) in the catalog. Validated production decks: BACB close (18), SNBC VC track (37), SNBC dossiers (3), SNBC journey maps (4).

**Impact-close pattern — RATIFIED 2026-07-28 (2nd ruling of the day):** Shyam prefers the 4-up stat-card row (muted "from →" + 30pt landing value + label) with ONE navy hero-claim card, receipt lines beside it, and a "Proven here" band — over the 3-hero-tile close ("I use this one more — a lot cleaner"). Reverses the 22-Jul "too busy → simplify to hero tiles" call after a week of live room use. Codified: `d.stat_card()` + `d.proven_band()` in the engine, catalog entry replaces the proof strip (3-tile close retired to one-number-only moments), copy-source = `example_build.py` S5.

**Page numbers — LANDED 2026-07-28:** the parallel thread's mechanism (Product Factory deck, Mayur PDP session) is `<a:fld type="slidenum">` — live fields that auto-renumber on insert/reorder. Ported into the engine as `ExhibitDeck.page_field()`, styled to the existing footer spec (12.75pt bold black on the divider). Source deck archived at `Engagement/internal/vc-monetization-pdp/Input/Product_Factory_Execution_Plan_Exhibit.pptx`. Ends the hardcoded-"NN" renumbering passes of the SNBC builds.

*(Pre-default history below, kept for the record.)* One full production deck (BACB close, 18 slides, PPTX-native, Google Slides-safe) built in this language, QA'd, client-ready. Reference implementation: `Engagement/BACB/Output/build_scripts/bacb_close_exhibit_pptx.py`.

**Ratified into SKILL.md (permanent):**
- One-sentence punchline strips, one line, bold lead + regular remainder (2026-07-15).

## Edits required before "default" (the upgrade list)

| # | Edit | Why | Tier |
|---|------|-----|------|
| 1 | Extract the BACB build helpers into a reusable builder (`chrome`, `kicker_title`, `footnote`, `rich/para_block`, `oval/gate`, `strip_theme_styles`) — an `ExhibitPresenter` class beside `frontline_slides_pptx.py` | Today the language exists only as a per-deck script | **Architect** (`tools/`) |
| 2 | `strip_theme_styles` (remove `<p:style>` from every shape) as a mandatory save step | Kills theme drop-shadows in LibreOffice/Google Slides — found the hard way | with #1 |
| 3 | Codify the new patterns as T15–T19: **receipts row** (sourced stats under a claim) · **dashed = yours** half-built grammar · **scenario board** (phases × A/B bands) · **engagement plan** (session/outcome/attendees, navy finale row) · **story page** (who → problem → what we did → what it proved) | All validated on BACB; currently undocumented | knowledge (consultant OK) |
| 4 | Conventions: coral dashed badge = ILLUSTRATIVE/OUTSIDE-IN · DEFENSE lines in speaker notes on number slides · "the math, in the open" formula-table appendix | Credibility architecture that made the deck defensible | knowledge |
| 5 | **The palette decision (the real blocker).** Exhibit palette (#071224/#4066F5) ≠ Frontline tokens (#041326/#3367FF). Default status needs either (a) exhibit chrome re-skinned in Frontline tokens (hybrid), or (b) brand ratifies the kit palette for a named lane (strategy/exec decks). Decide, don't blend. | CLAUDE.md canon says Frontline is the client-facing default | **Architect + brand** |
| 6 | Standing task (pre-existing): wire adopted P1+P2 exhibits into `backbase-slides-app/engine.js` + `frontline_slides_pptx.py` | HTML/Frontline parity | Architect |

**Promotion test:** after 2–3 more decks in this language (different accounts), package #1–#4 as a registered skill and take #5 to Mayur/Shobhit as the frontline-pptx-builder-promotion playbook did.

## Chrome exact-spec (XML-verified against BACB_Close_16Jul_ExhibitStyle.pptx, 2026-07-15)
When generating PPTX in this style, replicate these EMU-exact values (inches, 13.333x7.5):
- Hairlines: straight connectors, #D2D4D8, 0.75pt, FULL-BLEED — top (0,0.573)→(13.333,0.573); left rail (0.573,0)→(0.573,7.042); footer (0,7.042)→(13.333,7.042). Inner footnote hairline x=1.0→12.708.
- Notch: two BLUE (#4066F5) rects stepping UP into the line crossing: tall (0.490, 0.406, 0.083×0.167) + square (0.406, 0.490, 0.083×0.083). Never inverse/white-cutout.
- Footer: WHITE. Backbase logo PNG (navy wordmark) at (11.750, 7.193, 0.659×0.156) + page number 12.75pt BOLD navy at x≈12.83. No navy band.
- Kicker: 13.5pt REGULAR #4066F5 at (1.0, 0.812). Title: 28.5pt bold navy at (1.0, 1.104), full sentence WITH trailing period.
- Body scale: lane headers 21pt bold (lane colors 1F3799/4066F5/5F7DF7); labels 14.25 bold navy; body 12.75 #6A717C; "PROVEN HERE"-style micro-labels 12.75 #777D87; footnotes 12.75 #8F949C.
- Takeaway band: navy #071224 roundRect, ~11.708×0.479 at content width, text 14.25 (cyan #93FBFE bold lead-in + white regular).
- Bullets: #1F3799 ellipses 0.104. All shapes FLAT (explicit empty a:effectLst — LibreOffice adds shadows otherwise).
Lesson: build from the template/reference deck's XML, never re-derive chrome from SKILL.md prose. Reference logo asset copied to Engagement/SNB Capital/Output/backbase_logo_navy.png.

### Chrome refinements v2 (June-29 SNBC deck, Shyam-directed, 2026-07-16) — SUPERSEDES notch + footer above
- Step: ONE blue square FLUSH to the left slide edge at title level — x=0, ~0.156×0.156 in (scaled from 0.234 on the 20in canvas), vertically aligned with the title's first line. Replaces the two-piece stair at the hairline crossing.
- Footer: LARGE BLACK Backbase wordmark (~1.067×0.173 in, asset: Engagement/SNB Capital/Output/backbase_logo_black.png, cropped @300dpi from the June deck) + thin vertical divider (#9A9EA6, ~0.25 in tall) + page number 10pt bold black right of the divider. This is the "Backbase │ N" pattern.
- Keep: full-bleed #D2D4D8 hairlines, white footer, kicker/title scale, flat shapes. Optional per deck: top-right session marker.

### Chrome refinements v3 — FINAL (16 Jul, verified against BACB + June decks + Shyam round-trip test) — SUPERSEDES v2 step note
- The step is the AUTHENTIC Backbase glyph, not a plain square and not two rects: custGeom path (units w=9168 h=9096): M(19,4762) L(4567,4762) L(4566,0) L(9168,0) L(9168,9096) L(0,9096) Z — i.e. a square with its top-left quadrant removed. Draw as freeform (python-pptx build_freeform w/ scale=(w*914400/9168, h*914400/9096)); HTML: clip-path polygon(0 52.4%,49.8% 52.4%,49.8% 0,100% 0,100% 100%,0 100%).
- Position: hugging the hairline crossing — box (0.406, 0.406, 0.167 x 0.166) in, glyph corner ends exactly at (0.573, 0.573). Blue #4066F5 on white; cyan #93FBFE on dark slides.
- Page number: 12.75pt BOLD black, textbox anchored MIDDLE on the footer divider (divider: vertical hairline #9A9EA6 at x=12.802, y=7.118–7.367); number at x≈12.87. Wordmark 1.067x0.173 ends at 12.700.
- Connectors: strip the <p:style> element AND append empty <a:effectLst> — otherwise the theme effectRef re-adds a line shadow in LibreOffice/Google renders.
- Survives Google Slides round-trip (tested: geometry, freeform, PNG logo all preserved).
