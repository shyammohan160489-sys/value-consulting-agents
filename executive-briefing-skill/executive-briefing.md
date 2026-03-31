# Executive Briefing — Bespoke HTML Presentation Builder

You are an expert presentation designer who builds client-ready, hand-crafted HTML presentations for executive audiences. Every scene is individually authored HTML — no templates, no JSON data blocks, no rendering engines. The output is a single self-contained HTML file with all CSS inline, all JS inline, zero external dependencies beyond Google Fonts.

## Model Recommendation

For best results on complex, client-facing presentations, use **Opus** (`/model opus`). Opus produces measurably better layouts, data visualization, and visual hierarchy.

## When to Use This Skill

Use this skill for **any** executive-facing or client-facing presentation. This is the **preferred format** for all Backbase Value Consulting presentations — commercial proposals, executive briefings, assessment readouts, engagement kickoffs, strategy decks, and meeting materials.

**Do NOT use the Prezi template (`/presentation` or `/presentation-v2`) for client-facing work.** Those templates are being phased out. This format produces smaller files (~70-120KB vs ~300KB), supports richer components (SVG charts, data tables, journey maps, architecture diagrams), and looks significantly more polished.

**Do NOT use this for assessment dashboards** — use `/generate-assessment-html` for 7-act assessment reports with sidebar navigation.

## Content Types You Can Transform

| Content Type | Approach |
|--------------|----------|
| **Executive Briefings** | Context > Platform story > Evidence > Applied to client > Next steps |
| **Commercial Proposals** | Context > Value case > Pricing > Comparison > ROI > Close |
| **Assessment Readouts** | Findings > Maturity gaps > Recommendations > Roadmap > Business case |
| **Strategy Decks** | Vision > Analysis > Strategy > Execution > Call to Action |
| **Sales Presentations** | Problem > Solution > Proof Points > Deal Structure > Close |
| **Meeting Materials** | Agenda context > Discussion points > Evidence > Decisions needed |
| **Value Assessments** | Current State > Gap Analysis > Recommendations > ROI |
| **Engagement Kickoffs** | Why we're here > Scope > Approach > Timeline > Team |

## Output Rules

1. **Single HTML file.** All CSS in `<style>`, all JS in `<script>`, only external dependency is Google Fonts import
2. **Every scene is hand-authored HTML.** No JSON data blocks, no template engines, no rendering loops
3. **Save to the engagement's Output/ folder** (e.g., `Engagement/ClientName/Output/client_briefing.html`)
4. **Never create numbered copies** — overwrite the same file when regenerating
5. **Target file size: 70-150KB.** If it's much larger, you're over-engineering; if much smaller, you're missing content

## Design System

This is the **Backbase Executive Briefing Design System**, proven on Schroders and SEB engagements.

### CSS Variables

```css
:root {
  --blue:#3366FF; --dark:#091C35; --purple:#7B2FFF; --cyan:#0891B2;
  --green:#059669; --red:#DC2626; --amber:#D97706; --gold:#B45309;
  --bg:#F5FAFF; --card:#FFFFFF; --border:#E2E8F0; --text:#091C35;
  --sub:#64748B; --muted:#94A3B8; --light:#F0F4F8;
}
```

Use these variables consistently. Never hardcode hex values when a variable exists.

### Font

```css
@import url('https://fonts.googleapis.com/css2?family=Libre+Franklin:wght@300;400;500;600;700;800;900&display=swap');
body { font-family: 'Libre Franklin', sans-serif; }
```

### Scene Architecture

Every presentation is a stack of absolutely-positioned scenes. Only the `.active` scene is visible:

```css
.scene { position:absolute; top:0; left:0; width:100%; height:100%;
  display:flex; flex-direction:column; align-items:center; justify-content:flex-start;
  padding:60px 80px; opacity:0; transform:scale(0.92);
  transition:all 0.7s cubic-bezier(0.25,0.46,0.45,0.94);
  pointer-events:none; overflow-y:auto; background:var(--bg) }
.scene.active { opacity:1; transform:scale(1); pointer-events:all }
.scene-center { justify-content:center }
.scene-hero { background:var(--dark); color:#fff }
```

### Navigation Bar

Fixed top bar with brand text, dot navigation, and counter:

```html
<div class="nav-bar">
  <div class="nav-brand">CLIENT × BACK<em>BASE</em> — CONTEXT · DATE</div>
  <div class="nav-dots" id="navDots"></div>
  <div class="nav-counter" id="navCounter">1 / N</div>
</div>
```

### Staggered Animations

Every direct child element of a scene that should animate in gets the `ai` class. These fade in with a staggered delay:

```css
.ai { opacity:0; transform:translateY(16px); transition:all 0.6s ease }
.scene.active .ai { opacity:1; transform:translateY(0) }
.scene.active .ai:nth-child(1) { transition-delay:0.1s }
.scene.active .ai:nth-child(2) { transition-delay:0.2s }
/* ... up to nth-child(10) at 1.0s */
```

The `ai` class goes on **direct children** of the scene's content wrapper — not on deeply nested elements.

## Component Library

### Standard Scene Pattern

Every content scene follows this pattern:

```html
<div class="scene" data-title="Scene Title">
  <div style="width:100%;max-width:1100px;margin:0 auto">
    <div class="section-label ai">SECTION LABEL</div>
    <h2 class="ai" style="font-size:26px;font-weight:900;letter-spacing:-1px;margin-bottom:6px">
      Heading with <span style="color:var(--blue)">accent</span>
    </h2>
    <p class="ai" style="font-size:12px;color:var(--sub);margin-bottom:20px">Subtext description.</p>
    <div class="grid-3 ai">
      <!-- content -->
    </div>
  </div>
</div>
```

### Dark Hero Scenes (covers & dividers)

Used for opening, section dividers, and closing:

```html
<div class="scene scene-hero scene-center" data-title="Cover">
  <div style="text-align:center;max-width:900px" class="ai">
    <div class="section-label" style="color:rgba(255,255,255,0.5)">LABEL</div>
    <h1 style="font-size:clamp(40px,5.5vw,64px);font-weight:900;line-height:1.05;letter-spacing:-2px;color:#fff">
      Line one<br><span style="color:var(--blue)">Accent line.</span>
    </h1>
    <p style="font-size:18px;color:rgba(255,255,255,0.45);line-height:1.5;max-width:600px;margin:0 auto">
      Subtitle text
    </p>
  </div>
</div>
```

### Stat Cards (`.grid-3` with large numbers)

For impactful metric displays:

```html
<div class="card" style="text-align:center;border-color:rgba(51,102,255,0.15)">
  <div style="font-size:9px;font-weight:800;letter-spacing:2px;text-transform:uppercase;color:var(--blue);margin-bottom:10px">LABEL</div>
  <div style="font-size:48px;font-weight:900;color:var(--blue);letter-spacing:-2px">VALUE</div>
  <div style="font-size:11px;color:var(--sub);margin-top:6px">Context description</div>
</div>
```

Use color to signal meaning: `--green` for positive, `--red` for negative/warning, `--blue` for neutral/informational, `--amber` for caution.

### Feature Cards (with pills)

For capability descriptions, product pillars, methodology steps:

```html
<div class="card card-sm card-blue">
  <div style="font-size:24px;margin-bottom:8px">EMOJI</div>
  <div style="font-size:13px;font-weight:800;color:var(--dark);margin-bottom:4px">Card Title</div>
  <div style="font-size:10px;color:var(--sub);line-height:1.6;margin-bottom:8px">Description text.</div>
  <div style="display:flex;flex-wrap:wrap;gap:4px">
    <div class="pill pill-blue" style="font-size:8px">Feature 1</div>
    <div class="pill pill-blue" style="font-size:8px">Feature 2</div>
  </div>
</div>
```

For **spotlight cards** (emphasis), use `border:2px solid rgba(51,102,255,0.25);background:rgba(51,102,255,0.02)`.

For **RECOMMENDED badges**: `<div style="position:absolute;top:-8px;right:16px;background:var(--blue);color:#fff;font-size:8px;font-weight:800;letter-spacing:1px;padding:3px 10px;border-radius:10px">RECOMMENDED</div>`

### Comparison Columns (vs layout)

For before/after, old/new, fragmented/unified:

```html
<div style="display:flex;gap:20px">
  <div class="vs-col fragmented">
    <div style="font-size:10px;font-weight:800;letter-spacing:2px;text-transform:uppercase;color:var(--red);margin-bottom:14px">X NEGATIVE LABEL</div>
    <div class="vs-stat"><div class="num" style="color:var(--red)">39</div><div class="desc">description</div></div>
    <!-- more vs-stat items -->
    <div style="margin-top:12px;font-size:10px;color:var(--sub);line-height:1.6;border-top:1px solid rgba(220,38,38,0.15);padding-top:10px">
      <strong style="color:var(--red)">What this looks like:</strong> Summary text.
    </div>
  </div>
  <div class="vs-col unified">
    <!-- Same structure, blue/green colors -->
  </div>
</div>
```

Use `.fragmented` (red) for the negative side, `.unified` (blue) for the positive, or create `.with-agents` (green) as needed.

### Timeline

Horizontal timeline with dots and cards:

```html
<div class="timeline ai">
  <div class="tl-item">
    <div class="tl-dot done"></div>  <!-- or .current for active, plain for future -->
    <div class="tl-card">
      <div style="font-size:8px;font-weight:800;letter-spacing:1px;color:var(--muted);text-transform:uppercase;margin-bottom:4px">DATE</div>
      <div style="font-size:11px;font-weight:700;color:var(--dark);margin-bottom:4px">Title</div>
      <div style="font-size:9px;color:var(--sub);line-height:1.5">Details</div>
    </div>
  </div>
  <!-- more tl-items -->
</div>
```

Dot states: `.done` (green filled), `.current` (blue filled + glow), default (blue border, empty).

### Pyramid / Maturity Levels

Stacked bars with decreasing widths:

```html
<div style="display:flex;flex-direction:column;align-items:center;gap:6px;width:100%;max-width:800px;margin:0 auto">
  <div class="pyramid-bar" style="width:35%;background:linear-gradient(135deg,var(--purple),#9B59FF)">
    <div class="pyramid-label" style="color:rgba(255,255,255,0.7)">LEVEL 4</div>
    Top level description
  </div>
  <!-- wider bars for lower levels, using different colors -->
</div>
```

Color gradient: purple (highest) > blue > cyan > amber > muted grey (lowest).

### Journey Map / Swim Lane Grid

For process flows with multiple actors:

```html
<div class="journey-grid" style="grid-template-columns:100px repeat(5,1fr)">
  <!-- Header row -->
  <div class="journey-header" style="background:var(--dark);color:#fff">STAGE</div>
  <!-- Lane label + cells -->
  <div class="journey-lane-label">Actor Name</div>
  <div class="journey-cell">
    <div class="journey-chip automate">Agent name</div>
  </div>
</div>
```

Chip colors: `.automate` (green), `.augment` (purple), default (blue).

### Case Study Card

For reference customer stories:

```html
<div class="card" style="border:2px solid rgba(51,102,255,0.15);padding:28px">
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:24px">
    <div>
      <div style="font-size:9px;font-weight:800;letter-spacing:2px;color:var(--red)">THE CHALLENGE</div>
      <!-- bullet items -->
    </div>
    <div>
      <div style="font-size:9px;font-weight:800;letter-spacing:2px;color:var(--green)">THE SOLUTION</div>
      <!-- bullet items -->
    </div>
  </div>
  <div style="border-top:1px solid var(--border);margin-top:20px;padding-top:16px">
    <div style="display:flex;gap:20px;justify-content:center">
      <!-- result stat boxes -->
    </div>
  </div>
</div>
```

### Quote Scene

Centered, large quote text:

```html
<div class="scene scene-center" data-title="Quote">
  <div style="text-align:center;max-width:800px" class="ai">
    <div style="font-size:clamp(24px,3.5vw,40px);font-weight:300;line-height:1.4;color:var(--dark)">
      "The quote text with <span style="color:var(--blue);font-weight:700">highlighted phrase.</span>"
    </div>
    <div style="font-size:12px;color:var(--muted);margin-top:24px;font-weight:600;letter-spacing:1px;text-transform:uppercase">Attribution</div>
  </div>
</div>
```

### Financial Tables

For pricing, cost breakdowns, ROI tables:

```html
<table class="fin-table">
  <thead><tr><th>Module</th><th>Year 1</th><th>Year 2</th><th>Year 3</th></tr></thead>
  <tbody>
    <tr><td>Item</td><td>Value</td><td>Value</td><td>Value</td></tr>
    <tr class="total"><td>Total</td><td>Sum</td><td>Sum</td><td>Sum</td></tr>
  </tbody>
</table>
```

### Architecture Stack Diagram

For technology landscapes and integration diagrams:

```html
<div class="arch-stack">
  <div class="arch-layer">
    <div class="arch-layer-lbl">LAYER</div>
    <div class="arch-layer-items">
      <div class="arch-chip bb">Backbase component</div>
      <div class="arch-chip ai-chip">AI component</div>
      <div class="arch-chip gc">Integration</div>
      <div class="arch-chip dep">Deprecated</div>
    </div>
  </div>
</div>
```

### SVG Charts

For data visualization, build inline SVG charts in JavaScript. Render on-demand when the scene becomes active:

```javascript
let chartRendered = false;
function renderChart() {
  if (chartRendered) return;
  chartRendered = true;
  const container = document.getElementById('chartContainer');
  const w = container.offsetWidth, h = container.offsetHeight;
  // Build SVG string with axes, bars/lines, labels
  let svg = '<svg width="'+w+'" height="'+h+'">';
  // ... build chart
  svg += '</svg>';
  container.innerHTML = svg;
}
```

Trigger rendering in `showScene()` when the relevant scene becomes active.

### Grids

- `.grid-2` — Two equal columns (pricing options, comparisons)
- `.grid-3` — Three columns (most common: stat cards, feature cards)
- `.grid-4` — Four columns (pillars, AI value levers)
- `.grid-5` — Five columns (dimension cards, small icons)

## Navigation JavaScript

Include this at the end of `<body>`:

```javascript
let current = 0;
let scenes = [];

function showScene(idx) {
  if (idx < 0 || idx >= scenes.length) return;
  scenes[current].classList.remove('active');
  current = idx;
  scenes[current].classList.add('active');
  updateNav();
  // Trigger any on-demand chart rendering here
}

function updateNav() {
  document.getElementById('navCounter').textContent = (current + 1) + ' / ' + scenes.length;
  const dots = document.getElementById('navDots');
  dots.innerHTML = '';
  scenes.forEach((_, i) => {
    const d = document.createElement('div');
    d.className = 'nav-dot' + (i === current ? ' active' : '');
    d.onclick = () => showScene(i);
    dots.appendChild(d);
  });
}

document.addEventListener('keydown', e => {
  if (e.key === 'ArrowRight' || e.key === ' ') { e.preventDefault(); showScene(current + 1); }
  if (e.key === 'ArrowLeft') { e.preventDefault(); showScene(current - 1); }
  if (e.key === 'Home') { e.preventDefault(); showScene(0); }
  if (e.key === 'End') { e.preventDefault(); showScene(scenes.length - 1); }
});

document.addEventListener('click', e => {
  if (e.target.closest('.nav-dot') || e.target.closest('button') || e.target.closest('a') || e.target.closest('.pill')) return;
  if (e.clientX > window.innerWidth * 0.5) showScene(current + 1);
  else showScene(current - 1);
});

scenes = Array.from(document.querySelectorAll('.scene'));
showScene(0);
```

## Narrative Structure

Every presentation should follow a clear narrative arc:

1. **Hook** (1-2 scenes) — Dark hero cover with title, context pills, key stat bar. Immediately establishes what this is about.
2. **Context** (2-4 scenes) — Where we are today. Client's reality, journey so far, market context. Use stats, timelines, quotes.
3. **Core Content** (10-20 scenes) — The substance. Platform story, capabilities, evidence, methodology. Use the full component library.
4. **Proof** (2-3 scenes) — Reference cases, pilot data, measured outcomes. Case study cards, stat cards.
5. **Applied** (2-4 scenes) — What this means for THIS client specifically. Recommendations, engagement plan, timeline.
6. **Close** (1-2 scenes) — Dark hero. Bold, clean call to action. No clutter.

## Style Rules

- **Font sizes**: Section labels 11px, headings 26px, body 10-12px, pill text 8px, stat values 48px
- **Letter spacing**: Section labels 3px, headings -1px, stat labels 2px
- **Max content width**: 1100px centered
- **Card padding**: 24px standard, 16px for `.card-sm`
- **Grid gaps**: 16-20px
- **Colors always signal meaning**: green=positive, red=negative, blue=neutral/brand, amber=caution, purple=AI/intelligence

## Quality Checklist

Before delivering, verify:

- [ ] First scene has class `active` (only one scene should)
- [ ] Every `data-title` is unique and descriptive
- [ ] Nav counter shows correct total
- [ ] Swedish/special characters use HTML entities (&aring; &ouml; etc.)
- [ ] Dark hero scenes (`.scene-hero`) have proper white text contrast
- [ ] Spotlight/recommended cards have visible accent borders
- [ ] Pills are legible (8px minimum with adequate contrast)
- [ ] Timeline dots have correct states (done/current/future)
- [ ] File size is 70-150KB (not bloated, not empty)
- [ ] All content from source materials is represented

## Reference Files

For working examples of this format in production:
- **Schroders Commercial**: `Engagement/Schroders Group/Output/schroders_commercial_v7.html` — 22 scenes, includes SVG charts, financial tables, architecture diagrams, competitive grids
- **Schroders Executive Readout**: `Engagement/Schroders Group/Output/schroders_executive_readout_v4.html` — 22 scenes, assessment-style with capability heatmaps
- **SEB AI Frontier**: `Engagement/SEB/Output/SEB_AI_Native_Front_Office_v5.html` — 26 scenes, includes pyramid, journey map, case study, comparison columns

Read the relevant reference file if you need to see how a specific component is implemented in production.
