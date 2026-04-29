# Actions

**Open action items — your manager queue.**

This is **not** a replacement for whatever task tracker your team uses (Linear, Asana, Notion, etc.). This is your *personal* manager-actions queue:

- Things you owe people
- Things people owe you (that you're tracking)
- Things you've delegated and need to follow up on
- Cross-cutting actions that don't sit naturally in any one engagement

## Files

- `open.md` — current open actions
- `done.md` — completed actions (recent — older ones flow to `archive/`)
- `waiting.md` — actions blocked on someone else (with chase dates)

## Format

```markdown
- [ ] **<owner>** — <action> — due YYYY-MM-DD — source: meetings/2026/04-29-*.md
```

## Daily / weekly hygiene

- **Daily:** scan `open.md`, mark anything done, flag overdue
- **Weekly review:** scan `waiting.md`, decide if it's time to escalate / re-ask

## Privacy

Contents of this folder are **gitignored**. Never committed.
