# Backbase McKinsey-exhibit deck kit

A self-contained package for building Backbase decks in the validated McKinsey exhibit style. Hand this zip to anyone on the team; nothing else is required.

## What is inside

- `SKILL.md` — the skill: type scale, slide anatomy, palette, exhibit catalog, content rules, PPTX export mechanics. This is the file Claude reads and follows.
- `Backbase Exhibit Templates.dc.html` — 15 ready-to-copy template slides (T00-T14), one per validated exhibit pattern, with placeholder content. Opens directly in the preview.
- `assets/logo/` — Backbase wordmarks (dark for light slides, white for dark slides).
- `support.js` — runtime the template file needs; keep it next to the .dc.html.

## How to install (per person, ~2 minutes)

1. Create a new project in Claude Design.
2. Upload this zip (or drag the unzipped folder in).
3. Say: **"Use SKILL.md and Backbase Exhibit Templates.dc.html as the design system and skill for every deck in this project. Follow them exactly."**
4. Optional but recommended: also bind the official Backbase Design System (Backbase Design Systemvfinal) to the project for fonts, brand photography, and the wider token set. This kit falls back to Google Fonts Libre Franklin when the design system is not bound.

## How to use

- Ask for a deck the normal way ("build a QBR deck from this doc"). Claude picks the right template per slide from the catalog in SKILL.md.
- Or point at a pattern directly: "use T07 (cohort cascade) for the pipeline slide."
- The hard rules that make decks survive review: titles 38-40px full-sentence takeaways, body 18-21px, nothing under 17px; one exhibit per slide, 2-3 callouts; detail goes to speaker notes; slide 23-style plain tables are the one intentional table per deck; no em dashes.

## Keeping it current

When a new exhibit pattern is validated in a deck review, add it as a new T-slide in the template file and one line in the SKILL.md catalog, then re-share the zip.
