# Deal Notes — meeting transcript → deal-state record + live deal journal

Turn a raw meeting transcript or messy notes into a structured **deal-state record**
(action items, strategic reads, stakeholder map, next steps) and **append it to a
persistent per-deal journal**, so deal context compounds across meetings instead of
scattering across files.

This is the commercial/close counterpart to the `discovery-transcript-interpreter`
agent. Discovery extracts an *Evidence Register* for a value assessment. Deal Notes
captures *deal state* for a negotiation: who said what, what moved, what's blocked,
what's next, and what it means. Run it after **every** commercial / POC / legal touchpoint.

## When to Use

- After any client meeting, procurement session, POC playback, legal call, or internal deal-strategy call
- Triggers: "summarise this transcript", "deal notes from today", "update the deal journal"

## Usage

```
/deal-notes <path-to-transcript>   (and the engagement folder, if not obvious)
```

### Step 1 — Archive the source first (folder discipline)
Copy the raw transcript into the engagement's `Input/` subfolder **before** processing
(meeting transcripts → `Input/1. Client meetings & presentation/`). Never work from
Downloads only.

### Step 2 — Resolve speakers
Map speaker labels to named Backbase vs client roles. Where a label is ambiguous,
**flag it as low-confidence — do not guess.** If the consultant gives an attribution
hint ("unnamed speakers are client-side"), apply it but still mark inferred names.

### Step 3 — Checkpoint 1 (pre-write)
Show the consultant the structured note + the one-line journal append you intend to
write. Confirm before writing anything.

### Step 4 — Extract into the fixed schema (below) and write the strategic read
The strategic read is the judgement layer — 3–6 "so-what" bullets — that makes this
worth more than minutes.

### Step 5 — Append to the deal journal
Append (never overwrite) to `Output/DEAL_JOURNAL.md` (create if absent) in reverse-
chronological order, and — if a deal-status agent memory exists — append a dated
state-delta block there too.

### Step 6 — Checkpoint 2 (post-write)
Confirm the note + journal append with the consultant.

## Output schema (one block per meeting)

```markdown
# <Deal> · <Meeting type> — <date>
**Attendees:** <Backbase / client, named, with roles>   ·   **Source:** <archived path>

## Headline state of play
<2–4 sentences: where the deal is now>

## What was covered / demonstrated

## Key exchanges & tensions
<issue → position(s) → resolution or open item>

## Action items
| Owner | Action | When |
|---|---|---|

## Strategic reads
<3–6 so-what bullets: leverage, risk, who to protect, what it means for the close>

## Next milestones

<!-- TELEMETRY_START -->
agent: deal-notes
date: <YYYY-MM-DD>
source: <archived transcript path>
attendees_resolved: <n named / n total>
low_confidence_attributions: <n>
journal_appended: true
<!-- TELEMETRY_END -->
```

## Guardrails

- Every attribution and claim traces to the transcript; low-confidence ones are flagged, never asserted as fact.
- Strategic reads are clearly separated from what was actually said.
- Anonymise before any harvest to `knowledge/learnings/` (no client or stakeholder names).

## Governance (mandatory — per CLAUDE.md)

- Journal entry + telemetry block on completion · dual checkpoint (pre-write + post-write).
- Recurring stakeholder-archetype / objection patterns may feed `knowledge/learnings/` (anonymised).

## Reference quality bar

Output should match or exceed the hand-built examples this skill was distilled from:
`POC_PLAYBACK_NOTES_20260602.md`, `COMMERCIAL_NOTES_20260529_Peter_onsite.md`,
`COMMERCIAL_TRACK_NOTES_20260511.md`.

## Origin

`knowledge/learnings/pipeline_gaps/deal_desk_commercial_track.md` ·
`knowledge/learnings/pipeline_gaps/SPEC_deal-notes.md`
