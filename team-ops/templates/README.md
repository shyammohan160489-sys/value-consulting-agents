# Templates

The capture & processing templates that drive the second brain. **These are tracked in git** — the structure is reusable, only the content (in sibling folders) is gitignored.

## What's here

| Template | Used for | Lives where after use |
|---|---|---|
| `meeting-capture.md` | Processing any inbox item (Plaud transcript, notes) into structured output | Output routes to `meetings/`, `people/`, `engagements/`, `decisions/`, `actions/` |
| `person-page.md` | Creating a new entry under `people/` | `people/<name>.md` |
| `engagement-page.md` | Creating a new entry under `engagements/` | `engagements/<slug>.md` |
| `area-page.md` | Creating a new entry under `areas/` | `areas/<slug>.md` |
| `decision-record.md` | A single decision entry (multiple per quarterly file) | `decisions/YYYY-Q<n>.md` |
| `1on1-prep.md` | Generated before each 1:1 by pulling recent signals | Disposable — not filed |
| `weekly-review.md` | Generated each Friday/Monday by scanning the week | Disposable — not filed (or `archive/weekly-reviews/` if you want history) |

## Editing templates

Templates evolve as you learn what's missing. When you change one:
- Add the rationale as a one-line commit message
- Don't worry about retrofitting old entries — old shapes are fine

## Conventions used in templates

- **YAML front-matter** at top — Claude parses this for indexing
- **Append-only sections** marked with `<!-- comments -->` — Claude appends, doesn't rewrite
- **Cross-references** as relative markdown links — `[name](../people/<file>.md)`
- **Status colors** as `green | yellow | red` — easy to grep
