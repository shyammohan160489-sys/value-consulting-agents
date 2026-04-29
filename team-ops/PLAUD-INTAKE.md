# Plaud Intake — Getting Recordings Into the Inbox

## The honest answer on direct integration

There's **no public Plaud API** that lets Claude reach into your device or account. What Plaud does have:

- A mobile + desktop app that holds transcripts
- Cloud sync (Plaud Cloud)
- Export to: Markdown, plain text, audio (.mp3), summary
- Built-in integrations to **Notion**, **Obsidian**, and (depending on plan) **OneDrive / Google Drive / Dropbox**
- Webhook export on the AI Pro plan

So the flow we want is:

```
Plaud device → Plaud app → auto-export → team-ops/inbox/  (local folder)
                                              │
                                              ▼
                                        Claude processes
```

## Three setup paths — pick whichever works

### Option A: Plaud → Cloud Storage → local sync (easiest, no plan upgrade needed)

1. In Plaud app, set **Auto-export** to your cloud drive (Drive / OneDrive / Dropbox).
2. Sync that drive folder locally on your machine.
3. Symlink (or set Plaud's export folder) to: `team-ops/inbox/plaud/`

```bash
# Example — adjust path to your synced Plaud folder
mkdir -p team-ops/inbox/plaud
ln -s "$HOME/Google Drive/Plaud" team-ops/inbox/plaud
```

Every new recording shows up in `inbox/plaud/<date>.md` automatically.

### Option B: Plaud → Notion / Obsidian → manual copy

If you already use Notion or Obsidian as your Plaud destination, just copy the markdown export into `inbox/` when you're ready to process. Less automatic but zero new setup.

### Option C: Plaud webhooks (AI Pro plan)

If you're on AI Pro, configure a webhook that POSTs the transcript to a small ingestion endpoint. We'd need a tiny script to receive and write to `inbox/`. **Defer this — only worth doing if A and B prove insufficient.**

## What Claude expects to see in the inbox

A markdown or text file. Front-matter is nice but not required — Claude will parse what's there. Naming convention:

```
inbox/2026-04-29-1on1-mayur.md
inbox/2026-04-29-team-standup.md
inbox/2026-04-29-cust-XYZ-discovery.md
```

If Plaud names them by timestamp, that's fine — you can rename or just tell Claude what each one was during processing.

## Processing the inbox

When you're ready to process, ask:

> "Process my inbox"

Claude will, for each file:
1. Read the transcript
2. Apply `templates/meeting-capture.md`
3. Show you the structured output for review
4. On your OK: route to `meetings/`, append to `people/`, update `engagements/`, log decisions and actions, then **delete the inbox file**

Nothing routes without you confirming the first few times. Once you trust the routing, you can say "process and route automatically."

## Privacy reminders

- `team-ops/inbox/**` is gitignored. Plaud files never reach the repo's remote.
- Plaud's own privacy: review your Plaud cloud settings — by default they may use audio for model training. If recordings include sensitive client or HR content, opt out in their app settings.
- Do not export Plaud recordings of conversations where consent was not obtained for recording.
