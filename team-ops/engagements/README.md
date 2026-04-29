# Engagements

**Active project / deal / initiative pages — the manager's view, not the delivery view.**

## What's an engagement here vs. at the repo top

The repo's top-level `engagements/` (or `Engagement/`) folder holds **client deliverables and engagement IP** — the actual outputs.

This folder (`team-ops/engagements/`) holds **your manager view** of those engagements:
- Status + risks from your perspective
- Who's on it and how they're doing
- What you owe (decisions, removals of blockers, exec coverage)
- What's at stake commercially / strategically

Two different lenses, same engagement.

## File naming

`<client-or-codename>.md` — kebab-case.

## Lifecycle

- **Active** — lives here, status updated as things change
- **Closed / paused** — moves to `archive/engagements/`

## What triggers an update

- A meeting touching the engagement → status delta logged
- A decision affecting it → cross-referenced from `decisions/`
- A risk surfacing → added to the risks section
- A team change → reflected in the team list

## Privacy

Contents of this folder are **gitignored**. Never committed.
