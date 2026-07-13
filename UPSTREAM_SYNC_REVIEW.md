# Upstream Sync Review — `value-consulting-agents`

**Generated:** 2026-06-24
**Your local / origin:** `shyammohan160489-sys/...` @ `c1b9bd4` (+ 49 uncommitted changes)
**Upstream:** `mayur294-lgtm/...` @ `27e2b1f`
**Split point (merge-base):** `385f280` — 2026-02-26 (~4 months ago)
**Decision baseline:** your *full* local state (committed + uncommitted) = `backup/20260623-local-snapshot` (`de0c5aa`)

> **Standing decision:** Your Frontline 2026 design system **wins**. Do not merge upstream's design-system rebuild (PR #71/#53). This review flags those files as KEEP-YOURS and surfaces only the *non-design* additions worth considering.

---

## TL;DR

- **305 files differ** between your local and upstream — but that number is misleading. Most are your unique work (safe) or already identical.
- **Only 47 files** were changed by *both* sides **and** still differ → these are the only real "keep vs adopt" decisions.
- Of those 47, **~33 are your Frontline 2026 design system + palette-driven drift** → KEEP YOURS, no thought needed.
- That leaves **~14 files** needing actual judgement (CLAUDE.md, settings, ROI cluster, orchestrate.py) — mostly small.
- **5 genuine upstream additions** are worth grabbing (auditability hooks, official Banking OS v4.0 narrative, a Pictet QBR deck, a sales ROI calculator, a question bank).
- **Recommendation:** keep your design system; cherry-pick the 5 additions onto a test branch; manually reconcile `CLAUDE.md` + your Banking OS canon. **Do not merge upstream wholesale.**

### The whole landscape at a glance

| Bucket | Count | Action |
|---|---:|---|
| 1. Keep yours — Frontline 2026 + your rewrites | ~33 | Do nothing |
| 2. Review & decide — real differences | ~14 | Eyeball, mostly keep yours; merge a few |
| 3. Upstream-only additions worth adopting | 5 groups | Cherry-pick to a test branch |
| 4. Upstream-only palette/template sweeps | ~25 | Ignore (tied to design system you're rejecting) |
| 5. Already identical (both changed, now same) | 53 | No action — upstream work already in your branch |
| 6. Your unique work (upstream never touched) | 218 | Safe — your engagements, domains, tools |

---

## What upstream shipped since the split (25 commits, themed)

| Theme | Commits | Verdict |
|---|---|---|
| **Frontline 2026 design-system rebuild** | #53, #71, palette sweep (`c9beae4`, `f650dad`, `e29edcc`) | **Reject** — yours wins. (Note: their palette converges to *your* tokens `#041326`/`#3367FF`.) |
| **Auditability enforcement hooks** | #72 (`27e2b1f`) | **Adopt-worthy** — enforces journal/telemetry/checkpoint governance |
| **Banking OS v4.0 canonical narrative** | #70, #66, #67 (`e868f63`, `b389588`) | **Reconcile** — official PMM source (Yashita Arora / Jouk Pleiter) vs your canon |
| **ROI pipeline v2** (two-agent + calibrator) | #36, #37, mariam/roi (`370c81d`, `305983e`) | **Mostly already absorbed** — verify no bugfix drift |
| **Security hardening + PII anonymization** | #37 (`fccb8c3`) | **Already identical** in your branch |
| **Knowledge-harvest zero-setup** | #24 (`efb40af`) | Already identical |

---

## Bucket 1 — KEEP YOURS (do nothing)

Your Frontline 2026 design system and your own rewrites. Upstream's competing versions should **not** be adopted.

| File | What upstream did | Why keep yours |
|---|---|---|
| `presentations/backbase-slides-app/engine.js` | Rebuilt on their palette (+659) | Your engine is the live one (+689) |
| `presentations/backbase-slides-app/deck-template.html` | Palette rebuild | Yours wins |
| `presentations/frontline-2026/{design-tokens.json, html-components.md, slide-layouts.md, google-slides-rules.md}` | Their token/component set | Your tokens are canonical |
| `tools/frontline_2026_presenter.py`, `frontline_2026_html.py`, `frontline_slides_pptx.py` | Their builders | Yours are the ones you maintain |
| `knowledge/design-system.md` | +267 lines (palette doc) | Yours wins — glance only if curious |
| `.claude/commands/frontline*.md`, `generate-assessment-html.md` | Palette/skill-name refs | Tied to design system → yours |
| `.claude/commands/deprecated/{frontline-html,frontline-slides,presentation,presentation-v2}.md` | Palette refs | Deprecated anyway — ignore |
| `.claude/agents/narrative-assembler.md` | +3 lines | **You rewrote it** (+49/-21) — keep yours |
| `knowledge/Ignite Inspire/{README, agent-1..6}.md` | **Palette sweep only** (`#3366FF→#3367FF`, `#091C35→#041326`) | Confirmed cosmetic — keep yours |

---

## Bucket 2 — REVIEW & DECIDE (real differences, mostly small)

These genuinely differ and aren't pure design-system. Most you'll still keep; a few need a real merge.

| File | Yours | Theirs | Recommendation |
|---|---|---|---|
| **`CLAUDE.md`** | +178/-36 | +39/-42 | **Merge manually.** Both added governance. Upstream added auditability + Banking OS refs; you added far more. Diff section-by-section. |
| **`.claude/settings.json`** | +10 | +30 | **Merge.** Upstream likely registers the new auditability hooks. Smart-merge different keys. |
| `.gitignore` | +41 | +11 | **Merge** (additive — take both) |
| **`scripts/orchestrate.py`** | +321/-82 | +345/-102 | **Review.** Upstream's change is ROI-v2 + hook integration. Check if you want their pipeline wiring. |
| `CHANGELOG.md`, `VERSION` | small | small | Trivial — take latest / both |
| `tools/roi_excel_generator.py` | +75/-10 | +76/-14 | **Review** — small drift; check for upstream bugfix |
| `.claude/agents/roi-financial-modeler.md`, `roi-hypothesis-builder.md` | ~+490 | ~+490 | Review — you've absorbed ROI v2; confirm no bugfix delta |
| `.claude/agents/roi-business-case-builder.md` | +9/**-960** | +10/-73 | **Keep yours** — you deliberately gutted/deprecated this |
| `.claude/commands/build-roi.md`, `generate-roi-questionnaire.md` | small | small | Review — likely keep yours |
| `knowledge/methodologies/{capability_driven_patterns, value_lever_framework}.md` | ~+260 | ~+260 | Review — near-identical; confirm |
| `.claude/agents/{capability-assessment, discovery-transcript-interpreter, ignite-workshop-synthesizer, journey-builder, market-context-researcher, usecase-designer, workshop-preparation}.md` | small | **tiny** (palette/security-ref) | **Keep yours** — upstream adds nothing meaningful |
| `knowledge/backbase_platform_lexicon.md` | +3 | +8 | Review — small |

---

## Bucket 3 — UPSTREAM-ONLY ADDITIONS (nothing of yours at risk — adopt the good ones)

These files **don't exist in your local** (or you never touched them). Pure additions — cherry-pick what's useful.

| File | What it is | Size | Recommendation |
|---|---|---:|---|
| `.claude/hooks/enforce-journal.py` | Journal/telemetry enforcement hook (#72) | +173 | **ADOPT** — implements your governance standard |
| `.claude/hooks/require-checkpoint.py` | Pre-gen checkpoint gate (#72) | +144 | **ADOPT** (with eyes open — adds friction to every agent run) |
| `knowledge/banking_os.md` | **Official Banking OS v4.0 PMM narrative** (Yashita Arora / Jouk Pleiter sources) | +718 | **RECONCILE** vs your `knowledge/product/banking-os.md` — this is the authoritative source |
| `knowledge/conversational_banking.md` | Conversational Banking positioning | +374 | **REVIEW** — compare to your Conv. Banking pricing work |
| `knowledge/positioning_history/README.md`, `knowledge/README.md` | Canon-versioning convention | +59 | Review — adopt the convention if useful |
| `presentations/.../examples/pictet_qbr_2026_REFERENCE.html` | **"Pictet — QBR \| Backbase Wealth"** deck | +1410 | **REVIEW** — your live account. See what the team built (built on *their* engine though) |
| `presentations/.../examples/pictet_slides_data.js` | Data for the Pictet deck | +288 | Review with the above |
| `Cortex_Sales_ROI_Calculator.html` | "Backbase Self-Service ROI Calculator" | +757 | **REVIEW** — possibly useful standalone tool |
| `knowledge/discovery_question_bank.md` | Discovery question bank addition | +33 | **ADOPT** — small, additive |

---

## Bucket 4 — IGNORE (upstream-only palette/template sweeps)

Tied to the design system you're rejecting. Equal +/- counts = mechanical color find-replace.

`knowledge/Ignite Inspire/*.html` (all templates + example decks), `knowledge/Ignite Inspire/{CLAUDE.md, design-system.md, agent-0-engagement-plan.md}`, `templates/presentations/{assessment-dashboard-template, prezi-template, prezi-template-v2, example-ack2026-day2}.html`, `docs/keeping-agents-updated.html` — **~25 files, all cosmetic. Skip.**

---

## Bucket 5 — ALREADY IDENTICAL (53 files, no action)

Both you and upstream changed these, but they're **byte-identical now** — meaning upstream's work already reached your branch via your earlier merges/cherry-picks. Includes: `knowledge/standards/security_protocol.md`, `tools/roi_calibrator.py`, `knowledge/methodologies/hypothesis_tree_decomposition.md`, `templates/long-form/document-template.html`, `agents/definitions/roi.md`, `scripts/{anonymize_transcript, dev_agent, review_agent, aggregate_issues, test_agent, setup-harvest}`, and the test artifacts. **The security hardening and most ROI v2 work is already in your branch.**

---

## Bucket 6 — YOUR UNIQUE WORK (218 files, safe)

Upstream never touched these. All your engagements (`Engagement/**`, `presentations/absa-*`, `advisor-cockpit-pov`, `cortex-book-of-work`, Nordic FinTech Forum), new knowledge domains (`knowledge/domains/{wealth, agent-pricing, negotiation, ...}`, `knowledge/field-cdo`), learnings, and bespoke tools. **No conflict, no decision — keep as-is.**

---

## Recommended next steps

1. **Don't touch your branch.** It's backed up (`backup/20260623-local-snapshot` on origin) and your design system stays.
2. **Spin up a throwaway integration branch** to test upstream additions without risk:
   ```bash
   git switch -c spike/upstream-adopt c1b9bd4
   ```
3. **Cherry-pick / copy the 5 worthwhile additions** (Bucket 3) onto that branch and try them:
   - auditability hooks (`.claude/hooks/*.py`)
   - `knowledge/discovery_question_bank.md`
   - the Pictet QBR deck + sales ROI calculator (just open and read — they're on upstream's engine)
4. **Reconcile two things by hand** (not a git merge):
   - `CLAUDE.md` — diff section-by-section, take upstream's auditability/governance additions, keep your structure.
   - **Banking OS canon** — compare upstream's official `knowledge/banking_os.md` (v4.0 PMM) against your `knowledge/product/banking-os.md`. Decide which is canonical or fold the official framing into yours.
5. **Ignore** Buckets 4 (palette) and 5 (already identical).
6. When happy, copy the adopted files back to your working branch and commit normally. Never `git merge upstream/main`.

### Commands to inspect any single file's actual diff
```bash
# your version vs upstream's version of one file:
git diff backup/20260623-local-snapshot upstream/main -- <path>

# just upstream's change since the split:
git diff 385f280 upstream/main -- <path>
```


---

## 13 Jul 2026 — full upstream comparison (post one-brain reconcile)

**State:** fork main 39 ahead / 41 behind upstream/main. Verdict: **missing nothing of substance.** The 41 upstream commits decode as:
- **Your own work round-tripped** — Mariam's PR#71 "verified Frontline 2026 (Shyam_2)" imported YOUR design system + Pictet QBR as upstream's reference; their engine/template additions are snapshots of your source (yours is newer).
- **Already absorbed** — Banking OS v4.0 narrative (knowledge/reference/banking-os-v4-UPSTREAM.md + DELTA), question bank, worktree hygiene.
- **Deliberately not merged (blueprint stance)** — bb-* dev harness + 24 eval commits (Langfuse judges, tracing, CI). Mining candidate for ShyamOS Foil: the 11 per-agent judge prompts (6852a61).
- **Declined as regression** — upstream's roi_excel_generator change removed _validate_and_cap_impacts() and made the scenario fallback silent 1.0 (was flagged 30%) — violates conservative-bias doctrine. Keep ours.
- **Taken (1 char × 2)** — #3366FF → #3367FF hex fix in roi-financial-modeler.md, aligning to canonical frontline-tokens blue.

Stance unchanged: never merge upstream/main; cherry-pick additive bits only.
