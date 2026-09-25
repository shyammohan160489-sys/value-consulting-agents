---
name: apex
description: Build a PowerPoint in the Apex design system, the default look for every PPTX since 24 Sep 2026 (the Claude Design look, rebuilt as engine recipes). Runs the exhibit-slides-pptx skill with ExhibitDeck(look='apex'). Trigger on "Apex", "Apex deck", "in the Apex look".
---

# /apex — a PPTX in the Apex design system

Load and follow `.claude/skills/exhibit-slides-pptx/SKILL.md` end to end. Apex is that skill's
default look; this command exists so the name works as a front door.

Non-negotiables, restated:

1. `d = X.ExhibitDeck(look='apex', client_logo=<png>)` for a client deck; `look='apex'` with no
   logo for an internal deck, tagged `Internal · <what>` top right.
2. If the deck is for a client you know and no logo file exists in the account's Input or assets
   folder, ask for the logo before building. Never a placeholder in a client deck.
3. Storyline first (`references/storyline-patterns.md`, flip test), one exhibit per slide from
   the Apex recipes (`references/exhibit-catalog.md` T40–T55), titles 28pt regular without a
   period, no bold anywhere, statement line or hero number for the so-what, footnote on every
   numeric slide.
4. Render to PNG and read every page before delivering; ship the `.pptx` with its build script
   next to it.
5. Use `look='v3'` only when the deck extends an account series that is still on v3 mid-cycle.
