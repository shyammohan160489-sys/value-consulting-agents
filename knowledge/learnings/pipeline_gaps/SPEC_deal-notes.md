# Skill Spec — `/deal-notes`  (Phase 1 · lead)

> **Status:** Proposed skill spec for Architect-tier implementation. Not yet built.
> **Tier:** Architect implements (`.claude/commands/deal-notes.md` + any helper in `tools/`).
> **Origin:** `knowledge/learnings/pipeline_gaps/deal_desk_commercial_track.md` (archetype #6).

## One-liner
Turn a raw meeting transcript or notes into a structured **deal-state record** — action items, strategic reads, stakeholder map, next steps — and **append it to a persistent per-deal journal**, so deal context compounds across meetings instead of living in scattered files.

## Why this is distinct from `discovery-transcript-interpreter`
The Discovery agent extracts an **Evidence Register** (E-IDs, pain points, metrics) to feed a *value assessment*. `/deal-notes` produces **deal state** to feed a *negotiation / close*: who said what, what moved, what's blocked, what's next, what it means strategically. Different output, different consumer, different cadence (after *every* commercial/POC/legal touchpoint, not once at discovery).

## When to use
- After any client meeting, procurement session, POC playback, legal call, or internal deal-strategy call.
- Triggered by: "summarise this transcript", "deal notes from today", "update the deal journal".

## Inputs
| Input | Required | Notes |
|---|---|---|
| Transcript / notes (txt, docx, paste) | Yes | Raw, messy, speaker-labelled or not. |
| Deal/engagement path | Yes | To locate the journal + Input archive. |
| Meeting metadata (date, attendees, type) | Optional | Inferred from transcript if absent. |
| Speaker-attribution hints | Optional | "Unnamed speakers are client-side" style guidance. |

## Processing
1. **Archive the source first** — copy the raw transcript into the engagement `Input/` subfolder (per folder-discipline rule) before processing.
2. **Resolve speakers** — map labels to named Backbase vs client roles; flag low-confidence attributions explicitly rather than guessing.
3. **Extract into a fixed schema** (see Output).
4. **Strategic read** — 3–6 "so-what" bullets: what this means for the close, risks, leverage, who to protect. This is the judgement layer that makes the notes worth more than minutes.
5. **Append to the deal journal** — a persistent, reverse-chronological per-deal markdown (and optionally the agent memory) so state compounds. Never overwrite prior entries.
6. **Checkpoint** — show the consultant the structured note + proposed journal append before writing (pre-write checkpoint); confirm after (post-write checkpoint).

## Output schema (per meeting)
```
# <Deal> · <Meeting type> — <date>
**Attendees:** <Backbase / client, named, with roles>  · **Source:** <archived path>
## Headline state of play        (2-4 sentences: where the deal is now)
## What was covered / demonstrated
## Key exchanges & tensions       (issue → position → resolution/open)
## Action items                   (table: owner · action · when)
## Strategic reads                (3-6 so-what bullets)
## Next milestones
<!-- TELEMETRY_START ... TELEMETRY_END -->
```
Plus a one-line append to `Output/DEAL_JOURNAL.md` (or the deal-status memory) summarising the state delta.

## Governance (mandatory, per CLAUDE.md)
- Journal entry on completion · telemetry block in every note · dual checkpoint (pre-write + post-write).
- Every attribution traces to the transcript; low-confidence ones flagged, not asserted.
- Anonymised harvest hook: recurring stakeholder-archetype / objection patterns can feed `knowledge/learnings/`.

## Dependencies
- `docx` / text ingestion · engagement-folder discipline · agent memory write.
- Reuses nothing new structurally — low build risk. **This is why it leads Phase 1.**

## Definition of done
Given a transcript + deal path, produces the structured note, archives the source, appends the journal, passes both checkpoints, and emits a telemetry block. Validated against the existing hand-built examples (`POC_PLAYBACK_NOTES`, `COMMERCIAL_NOTES`, `COMMERCIAL_TRACK_NOTES`) — output should match or exceed those.
