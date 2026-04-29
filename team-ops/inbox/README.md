# Inbox

**Drop zone for raw, unprocessed inputs.**

Anything goes here:
- Plaud transcripts (markdown / text exports)
- Hand-typed notes
- Forwarded emails (paste body into a `.md` file)
- Slack thread screenshots → OCR → text
- Voice memos transcribed elsewhere

## Rules

1. **No processing at capture time.** Just dump. Friction kills capture.
2. **One thought per file is fine.** Don't try to batch.
3. **Filename hints help:** `2026-04-29-1on1-mayur.md` is better than `recording_4729.md` — but rename later if needed.
4. **This folder gets emptied** as items are processed and routed.

## Processing

Ask Claude: **"Process my inbox"** or **"Process inbox/<filename>"**

Claude applies `templates/meeting-capture.md`, shows you the structured output, and on confirmation routes pieces to `meetings/`, `people/`, `engagements/`, `decisions/`, `actions/`.

The raw inbox file is deleted only after routing is confirmed.

## Privacy

Contents of this folder are **gitignored**. Never committed to the repo.
