---
# Use this template to process any raw inbox item (Plaud transcript, notes, etc.)
# Claude reads the raw input + this template and produces a structured output.
date: YYYY-MM-DD
type: 1on1 | team | cross-functional | client | leadership | interview | other
title: <short descriptive title>
participants:
  - <name> (<role>)
duration_min: <int>
source: plaud | notes | manual
inbox_file: <filename of raw input, if any>
---

# <Title>

## TL;DR
<2-3 sentences. What happened, what changed, what to watch.>

## Context
<Why this meeting happened. What was the prior state. Skip if obvious.>

## Decisions
<!-- Each decision: what, who decided, why, when effective -->
- **<decision>** — Decided by <name>, effective <date>. Rationale: <one sentence>. _(routes to decisions/)_

## Actions
<!-- Owner, action, due date. If no owner, mark UNASSIGNED. -->
- [ ] **<owner>** — <action> — due <YYYY-MM-DD>
- [ ] **UNASSIGNED** — <action> — due <YYYY-MM-DD>  ⚠ needs owner

## People Signals
<!-- Per-person observations. These append to people/<name>.md -->
### <Person Name>
- **Signal:** <observation — strength, struggle, growth, blocker, mood, capability gap>
- **Evidence:** <what they said/did that triggered this>
- **Follow-up:** <what to do about it, if anything>

## Engagement / Project Updates
<!-- Cross-references to engagements/ pages -->
- **<engagement>:** <status delta — what changed since last touch>

## Risks / Watch
- <risk> — likelihood: low/med/high — impact: low/med/high — owner: <name>

## Open Questions
- <question> — to resolve by <when> via <how>

## Quotes Worth Keeping
> "<verbatim quote that captures something important>" — <speaker>

## Routing Plan (Claude fills this when processing)
- Decisions → `decisions/<quarter>.md`
- Actions → `actions/open.md`  + assigned to person pages
- People signals → append to `people/<name>.md` under today's date
- Engagement updates → patch `engagements/<name>.md` status section
- This file → save to `meetings/YYYY/MM-DD-<slug>.md`
- Inbox source → delete after confirmed routing
