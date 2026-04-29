# Team Ops — Second Brain (Work)

A manager's second brain for running a Value Consulting team. This is your operating system for **direct reports + cross-functional partners**: the people, the work in flight, the decisions, and the actions.

> **Privacy:** All content folders (people, meetings, engagements, etc.) are gitignored. Only the *structure* and *templates* are committed. Nothing personal leaks into PRs.

---

## The Model — PARA, adapted for managers

Standard PARA is Projects/Areas/Resources/Archives. For a manager, the missing axis is **People** — most of your signal is *about* people doing work, not the work itself. So this brain has:

| Folder | What lives here | Lifecycle |
|---|---|---|
| `people/` | One page per direct report + key cross-functional partner. Running record of context, growth, signals, 1:1 history. | Permanent — updated continuously |
| `engagements/` | Active projects/deals/initiatives with a definite end-state. | Active until closed → `archive/` |
| `areas/` | Ongoing responsibilities (team health, hiring, ops cadence, capability building). | Permanent — reviewed periodically |
| `meetings/` | Processed meeting notes (after Inbox routing). Filed by date or by topic. | Reference |
| `decisions/` | Decision log — *what* was decided, *why*, *who*, *when*. | Permanent |
| `actions/` | Open action items (yours, assigned, awaiting). | Active until done → archive |
| `archive/` | Closed engagements, old meetings, dormant areas. | Reference only |
| `inbox/` | **Drop zone** for raw Plaud transcripts and other captured inputs. Processed → routed → emptied. | Transient |
| `templates/` | Capture templates. Use these. | Permanent (tracked in git) |

---

## The Flow — Capture → Process → Route → Surface

```
   Plaud / notes / Slack screenshots
              │
              ▼
        ┌──────────┐
        │  inbox/  │   raw, unprocessed
        └────┬─────┘
             │  process via templates/meeting-capture.md
             ▼
   ┌────────────────────────┐
   │  Structured meeting    │
   │  - decisions extracted │
   │  - actions extracted   │
   │  - people signals      │
   └────┬───┬───┬───┬───────┘
        │   │   │   │
        ▼   ▼   ▼   ▼
   meetings/  decisions/  actions/  people/<name>.md (signals appended)
                                    engagements/<name>.md (status updated)
```

### 1. Capture
Drop everything into `inbox/` — raw is fine. Plaud transcripts, hand-scribbled notes, forwarded emails, screenshots-converted-to-text. Don't process at capture time.

### 2. Process (this is where Claude helps)
Run the meeting-capture template against any inbox item. Output:
- A clean summary
- Decisions made (with context)
- Actions (owner, what, when)
- Signals about people (growth, friction, mood, capability)
- Cross-references (which engagement, which area)

### 3. Route
Each piece of the processed output goes to its home:
- **Decisions** → append to `decisions/YYYY-Q.md`
- **Actions** → add to `actions/open.md` (or assign to someone's page)
- **People signals** → append dated entries to `people/<name>.md`
- **Engagement updates** → update `engagements/<name>.md`
- **Full processed transcript** → `meetings/YYYY/MM-DD-<topic>.md`
- **Inbox file** → delete (it's now routed)

### 4. Surface
The system pays you back through:
- **`/team-ops weekly-review`** — what happened this week, what's stuck, who needs attention
- **`/team-ops 1on1-prep <name>`** — pull last 4 weeks of signals + open actions for a person
- **`/team-ops engagement-status <name>`** — current state of an engagement with provenance
- **`/team-ops decision-log Q2`** — what we decided and why

(These skills don't exist yet — see `ROADMAP.md` once we get past v1.)

---

## Getting Started (5-min version)

1. Read `PLAUD-INTAKE.md` — set up the export path so transcripts land in `inbox/` automatically.
2. Create one `people/<name>.md` per direct report using `templates/person-page.md`. Put 1-2 sentences of context. Don't try to be complete.
3. Create one `engagements/<name>.md` per active engagement using `templates/engagement-page.md`. Same — minimal.
4. Have your next meeting. Drop the Plaud transcript in `inbox/`. Ask Claude to "process inbox" — verify the routing makes sense.
5. Do this for two weeks before adding any sophistication. Capture habits beat clever architecture.

---

## What this is NOT

- **Not a task tracker.** Use whatever you already use (Linear, Asana, Notion, etc.) for assigned work. `actions/` is a personal queue + manager follow-up list.
- **Not a CRM.** Engagement IP belongs in `engagements/` at the top of the repo. `team-ops/engagements/` here is your *manager view* of those engagements (status, risks, who's on it, what you owe).
- **Not a journal.** Personal reflections, life stuff → that's the **third brain** (separate repo, see immortal.ai work).

---

## Conventions

- **Filenames:** kebab-case. Dates in `YYYY-MM-DD` form.
- **People pages:** `people/firstname-lastname.md` (or `firstname-l.md` if uniqueness allows). Use a consistent identifier — Claude will index by filename.
- **Engagement pages:** `engagements/<client-or-codename>.md`.
- **Tags:** Inline `#tag` in markdown — useful for cross-cutting (`#hiring`, `#escalation`, `#growth-conversation`).
- **Front-matter:** Every page starts with YAML front-matter (see templates) so Claude can parse status, last-updated, owner, etc.

---

## Trust & Safety

- Content here may include performance observations, sensitive 1:1 notes, candid signals. Treat accordingly.
- `team-ops/inbox/`, `team-ops/people/`, `team-ops/meetings/`, `team-ops/decisions/`, `team-ops/actions/`, `team-ops/engagements/`, `team-ops/areas/`, `team-ops/archive/` are **gitignored**. Only READMEs and templates are tracked.
- If you ever need to reset: `git status` will only show structural changes. Personal content stays local.
