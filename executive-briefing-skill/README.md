# Executive Briefing Skill — Installation Guide

## What's Included

| File | Purpose |
|------|---------|
| `executive-briefing.md` | The skill definition (install this) |
| `schroders_commercial_v7.html` | Design system reference — CSS, components, SVG charts |
| `SEB_AI_Native_Front_Office_v5.html` | Latest example — 26 scenes, custom components |

## Installation

1. Copy `executive-briefing.md` into your project's `.claude/commands/` directory:

```bash
cp executive-briefing.md /path/to/your/project/.claude/commands/
```

2. Place the two reference HTML files somewhere in your project (e.g., `references/` or `examples/`). Then update the two reference paths at the bottom of `executive-briefing.md` to point to wherever you placed them.

3. In Claude Code, invoke the skill:

```
/executive-briefing
```

Then provide your content (transcript, data, bullet points, or upstream agent outputs).

## Output

Produces a single self-contained HTML file (~70-120KB) with:
- Keyboard navigation (arrow keys, Space, Home/End)
- 20+ component types (stat cards, SVG charts, journey maps, timelines, etc.)
- Libre Franklin typography, Backbase color system
- Smooth scale+opacity transitions
- Zero external dependencies
