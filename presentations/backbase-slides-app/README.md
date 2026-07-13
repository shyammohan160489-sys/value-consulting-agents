# Backbase Slide Template Engine

A self-contained HTML presentation engine with 17 Backbase-branded layouts, presenter mode, and overview grid.

## Quick Start

### Create a new deck

```bash
cd backbase-slides-app
./create-deck.sh my-deck "Backbase — My Presentation"
```

This creates a new folder `../my-deck/` with:
- `index.html` — loads the shared engine
- `slides.js` — your slide content (edit this file)
- `images/` — put deck-specific images here

### Preview a deck

```bash
# From the slides/ parent directory:
npx serve . -l 3000

# Then open:
# http://localhost:3000/my-deck/
# http://localhost:3000/backbase-slides-app/    (template demos)
```

### Keyboard shortcuts

| Key | Action |
|-----|--------|
| `Arrow Right` / `Space` | Next slide |
| `Arrow Left` / `Backspace` | Previous slide |
| `F` | Toggle fullscreen |
| `O` | Overview grid |
| `P` | Presenter mode (notes + timer) |
| `G` | Go to slide number |
| `Home` / `End` | First / last slide |

## Architecture

```
slides/
  backbase-slides-app/     <- Template engine (shared)
    engine.js              <- Render engine + navigation
    index.html             <- Demo deck with all layouts
    slides.js              <- Demo slide data
    deck-template.html     <- HTML skeleton for new decks
    images/                <- Shared assets (bg.jpg, covers)
  my-deck/                 <- Your presentation
    index.html             <- Loads engine.js from ../backbase-slides-app/
    slides.js              <- SLIDES array + SPEAKER_NOTES
    images/                <- Deck-specific images
```

Each deck's `slides.js` defines two globals:
- `SLIDES` — array of slide objects
- `SPEAKER_NOTES` — object keyed by 1-based slide number

The engine (`engine.js`) reads these globals and renders the presentation.

### Shared images

Decks set `window.BB_SHARED_ASSETS = '../backbase-slides-app'` in their `slides.js` so the engine can find shared assets like `bg.jpg` (used by cover and thank-you slides).

## Layout Catalog

### 1. cover-color-block
Navy background with blue glow gradient. Best for: opening slide.
```js
{ layout: 'cover-color-block', label: 'BACKBASE', title: 'Title\nLine 2', date: 'March 2026', partner: false }
```

### 2. cover-photo
Two variants: with image (photo + white panel) or without (navy + bg.jpg). Best for: visual/branded opening.
```js
{ layout: 'cover-photo', label: 'LABEL', title: 'Title\nLine 2', date: 'March 2026', image: 'images/photo.jpg' }
// Without image: navy variant with client logo placeholder
{ layout: 'cover-photo', label: 'LABEL', title: 'Title', date: 'March 2026', partner: 'images/logo.png' }
```

### 3. chapter-numbered
Large number left, title right. Best for: numbered section dividers.
```js
{ layout: 'chapter-numbered', theme: 'navy|blue', number: '01', label: 'CHAPTER', title: 'Title', subtitle: 'Description' }
```

### 4. chapter-standard
Full-width title, no number. Best for: section dividers without numbering.
```js
{ layout: 'chapter-standard', theme: 'navy|blue', label: 'SECTION', title: 'Title', subtitle: 'Description' }
```

### 5. toc
Table of contents with numbered or plain rows. Best for: agenda.
```js
{ layout: 'toc', label: 'AGENDA', title: 'Contents', numbered: true, items: ['Item 1', 'Item 2', 'Item 3'] }
```

### 6. content-standard
General-purpose content slide. Best for: text, bullets, custom HTML.
```js
{ layout: 'content-standard', theme: 'light|dark', label: 'TOPIC', title: 'Title', subtitle: 'Subtitle', body: '<ul><li>Point 1</li></ul>' }
```

**Default behavior:** plain text / bullet bodies are TOP-ANCHORED and flow downward. A
sparse text slide keeps a clean bottom margin — that is correct. Never vertically-center
or stretch a prose body (that re-creates the "marooned middle").

**Structured mode — `structured: true`** (for card grids, layer stacks, pyramids, tables).
It does NOT stretch. It only resets the body font to `1em` (root scale) so authored `em`
sizes read directly off the slide root. Content stays NATURAL height and top-anchored, and
the bottom margin FLEXES with content volume — a light slide leaves clean bottom whitespace,
a heavy one reaches near the footer. This mirrors the hand-authored reference (content ends
anywhere from ~72% to ~93% depending on volume — do NOT force them all to the same line).
```js
{ layout: 'content-standard', structured: true, label: 'TOPIC', title: 'Title', subtitle: '…',
  body: `<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:${em(20)}">
           <div>card</div><div>card</div><div>card</div></div>${calloutHtml}` }
```
Never stretch (`flex:1`, `grid-auto-rows:1fr`, `height:100%`) or vertically-centre content
to fill the slide — that reads oversized and was the exact regression the user rejected.

**The subtitle is a FLEX LEVER, not a fixed slot — decide it per slide.** Omitting `subtitle`
rebases the body higher (`no-subtitle` → `top:30%` vs `33%`), buying the content room. So on a
content-DENSE slide, drop the blue subtitle and let the black title carry it (sharpen the title
to stand alone); on a LIGHT slide, keep the subtitle. Also drop it when the subtitle just
narrates what the eyebrow + title + tiles already say (redundant prose reads as filler and,
in client decks, as on-the-nose sell). Same judgement applies to the callout/strap line — it's
optional. Decide actively: eyebrow (label) + title (sharp thesis) are the constants; subtitle
and callout are levers you spend only when they earn their place.

**Type sizing — use em, never fixed px.** Fixed px don't scale with the frame, so the
(em-based) title balloons while px body stays tiny and the title:body ratio breaks. Size
body content in em off the slide root: `em(px) = px / 21.376` reproduces a hand-authored
measurement (its 1280-frame px) at the same proportion here (root is `1.67vw`; 1em ≈ 1.67%
of frame width; 1.67%·1280 = 21.376). Proven values matching the reference hand-authored
deck: body/bullets `em(14)`, tile heading `em(17)`, pyramid name / big tile head `em(20)`,
callout heading `em(15)`, badge `em(10)`, uppercase mini-label `em(11)`, table cell `em(14)` /
header `em(11)`, arch item `em(13)`; container paddings via `em()` too (card `em(24) em(26)`,
callout `em(16) em(20)`). Put `em()` font-sizes on LEAF text only (avoid compounding). Because
the engine's header zone starts the body lower (30–33%) than a hand-authored deck (~24%),
content-HEAVY structured slides (5-layer arch, 4-bar pyramid) need slightly tighter internal
vertical padding (e.g. arch layer `em(11)`, pyramid bar `em(13)`) so they still leave a bottom
margin. Keep the title to ONE line (a 2-line title collides with the subtitle).

### 7. content-columns
2-5 equal columns below a title. Best for: comparisons, pillars.
```js
{ layout: 'content-columns', label: 'LABEL', title: 'Title', columns: [
  { subtitle: 'Column 1', body: 'Description', icon: '<svg>...</svg>' },
  { subtitle: 'Column 2', body: 'Description' }
]}
```

### 8. overview-about
Content left, image right, stats row bottom (5 stats). Best for: company overview.
```js
{ layout: 'overview-about', label: 'ABOUT', title: 'Company Name', subtitle: 'Description', image: 'images/photo.jpg',
  stats: [{ value: '+150', label: 'Customers' }, { value: '50%', label: 'R&D Staff' }] }
```

### 9. overview-stats
Similar to overview-about but for 4 stats with different grid proportions.
```js
{ layout: 'overview-stats', label: 'CASE', title: 'Client Name', subtitle: 'Description',
  stats: [{ value: '$530B', label: 'Total Assets' }, { value: '20,000', label: 'Workforce' }] }
```

### 10. product
Title + bullets left, screenshot right. Best for: product showcase.
```js
{ layout: 'product', label: 'PRODUCT', title: 'Feature Name', subtitle: 'Subtitle',
  body: '<ul><li>Feature 1</li></ul>', image: 'images/screenshot.png', imageBg: true }
```

### 11. statement
Large text on a colored polygon band with highlighted words. Best for: impactful quotes.
```js
{ layout: 'statement', accent: 'blue|red', label: 'VISION',
  text: 'Text with <span class="hl">highlighted words</span>' }
// Dark variant (navy background):
{ layout: 'statement', variant: 'dark', label: 'INSIGHT', text: '...' }
```

### 12. statement-stat
Big number + description on a colored polygon band. Best for: data-driven statements.
```js
{ layout: 'statement-stat', accent: 'blue|red', label: 'IMPACT', stat: '70%',
  text: 'Description with <span class="hl">highlights</span>', source: 'Source Name 2025' }
```

### 13. testimonial
Customer photo left, quote right. Best for: customer quotes.
```js
{ layout: 'testimonial', logo: 'COMPANY', quote: 'Quote text', name: 'Person Name',
  role: 'Title, Company', image: 'images/person.jpg' }
```

### 14. team
Auto-layout grid based on member count. Best for: team introductions.
```js
{ layout: 'team', label: 'TEAM', title: 'Team Name', members: [
  { name: 'Name', role: 'Role', image: 'images/person.jpg' }
]}
```
Layouts: 1-3 members (feature), 5 (photo-dominant), 4+ (grid with max 4 rows).

### 15. agenda-table
Navy table with highlighted rows. Best for: event schedules.
```js
{ layout: 'agenda-table', label: 'SCHEDULE', title: 'Day 1',
  headers: ['Session', 'Time', 'Location', 'Speaker'],
  rows: [{ cells: ['Welcome', '09:00', 'Main Hall', 'Speaker'], highlight: true }] }
```

### 16. roadmap
Gantt-style timeline. Best for: project timelines.
```js
{ layout: 'roadmap', label: 'ROADMAP', title: '2026 Roadmap', months: ['Q1','Q2','Q3','Q4'],
  rows: [{ label: 'Workstream', bars: [{ start: 0, duration: 2, color: 'blue|navy|cyan|red', label: 'Phase 1' }] }] }
```

### 17. thank-you
Navy background with Backbase logo. No configuration needed.
```js
{ layout: 'thank-you' }
```

## Speaker Notes

Add notes keyed by 1-based slide number:
```js
const SPEAKER_NOTES = {
  1: 'Welcome everyone...',
  5: 'Key point to emphasize...'
};
```
Press `P` during presentation to see notes and a timer.

## Recommended Deck Structure

1. **Cover** (cover-color-block or cover-photo) — 1 slide
2. **Agenda** (toc) — 1 slide
3. **Chapter divider** (chapter-numbered) — per section
4. **Content slides** (content-standard, content-columns, product) — 2-4 per section
5. **Data / quotes** (statement, statement-stat, testimonial) — as needed
6. **Team / Roadmap** — as needed
7. **Thank you** — 1 slide
