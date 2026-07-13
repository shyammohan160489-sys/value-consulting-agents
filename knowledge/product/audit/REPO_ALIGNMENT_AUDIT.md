# Repo Alignment Audit — Banking OS Cascade

**Date:** June 2026 · **Run by:** banking-os-alignment-checker (4 parallel slices)
**Standard:** `knowledge/product/banking-os.md` (substance) + `knowledge/design-system/narrative-spine.md` (voice)
**Slice reports:** `01_skills.md` · `02_agents.md` · `03_knowledge.md` · `04_templates.md`

## The root cause (unanimous)

The **visual** brand is a wired single source of truth (`frontline-tokens.json`, read by every Frontline skill). The **verbal + substance** brand was **orphaned** — *no skill and no agent* instructed reading `narrative-spine.md` or `banking-os.md`. Meanwhile the files agents *do* read (`backbase_platform_lexicon.md`, the Ignite Inspire pack, several output templates) still teach the **previous generation**: "Engagement Banking Platform", 3-fabric / 3-plane architecture, 13 product lines, Acquire/Activate/Expand/Retain flywheel, **Sentinel absent entirely**, no 4 Solutions, no Conversational Banking, no Resolution Loops. Net: deliverables inherit the stale story by default.

The newest modules (APA Domain Matrix, Field CDO job description, and the new spine/banking-os.md) are already on-model — but **siloed**, with nothing routing the agents to them.

## Severity tally (across all slices)

| Slice | HIGH | MED | LOW | Notes |
|---|---|---|---|---|
| Skills (`.claude/commands`) | 4 | 7 | 5 | rendering assets clean; stale framing lives in canned examples |
| Agents (`.claude/agents`) | 5 | 7 | 6 | 12 narrative agents need the pointer; run on superseded lexicon |
| Knowledge (`knowledge/**`) | 6 | 7 | 5 | lexicon + Ignite pack are the stale foundation |
| Templates (`templates/**`) | 3 | 3 | 4 | no literal stale phrases left; exposure is structure + retired product names |

## Fix plan — by leverage

### Tier 0 — central anchors (fix once, cascades everywhere)
1. **CLAUDE.md governance rule** — make `banking-os.md` (substance) + `narrative-spine.md` (voice) a mandatory "read first / align to" standard for every deliverable. *(One edit, governs all generation.)* ✅ applied
2. **Re-base `backbase_platform_lexicon.md`** on `banking-os.md` — it self-declares "authoritative" and is cited by discovery, narrative-assembler, journey-builder, capability, usecase, upgrade. Add a canonical banner + the current Banking OS model; mark the old 13-product model as legacy reference. ✅ applied

### Tier 1 — the cascade pointer (belt-and-suspenders)
3. Add a standard **"READ FIRST: banking-os.md + narrative-spine.md"** preamble to every narrative/deliverable-producing **agent** (12) and **skill** (~10): narrative-assembler, discovery, capability-assessment, journey-builder, usecase-designer, market-context, workshop-prep, ignite-synthesizer, roi-hypothesis/financial/business-case, roadmap; executive-briefing(+slides), frontline-slides-html/pptx, frontline-long-form, generate-assessment-html, prototype, usecase-doc, pricing-model.

### Tier 2 — hard-coded stale content (named, client-facing)
4. `templates/outputs/assessment_report.md` (HIGH×2) — 7-section skeleton sells "Unified Banking Platform / progressive modernization"; names deprecated products (Grand Central, Digital Engage/Assist). Reframe to From→To + Banking OS + 4 solutions + value-leakage/resolution-loops + three value pools.
5. `templates/outputs/capability_assessment.md` (HIGH) — glossary defines "HELIX / Customer Brain", "Grand Central", "Flow Foundation". Rewrite to Banking OS / Nexus / Sentinel.
6. `.claude/agents/capability-gap-analyzer.md` (L220) — hard-coded MCP query contains "engagement banking architecture" → biases Infobank retrieval to legacy. Reframe.
7. Skills canned examples: `executive-briefing-slides.md` cover ("Transforming Client Experience"…), `prototype.md` legacy tokens (`#0052CC`+Inter → Frontline navy/blue + Libre Franklin), `usecase-doc.md` module enum ("Digital Assist/Engage" → 4 solutions).
8. Ignite Inspire pack (`knowledge/Ignite Inspire/*`) — canonical banner + Banking OS preamble across agent-1..6.

### Tier 3 — value-method unification
9. Add the **three value pools** + **resolution-loop / value-leakage** method to `value_lever_framework.md` and `capability_driven_patterns.md`; cross-link to the **APA Domain Matrix** (`domains/apa-matrix/`). The APA matrix and banking-os.md §9 are the **same method under two names** — APA is the data-backed instantiation (65 process sims; Value-Bleed → Simulation → Business-Case). Map APA's Growth/Efficiency/Control outputs onto the three value pools.
5. `pricing-model.md` — add the Conversational Banking pricing basis (platform + LOB + per-interaction + LLM pass-through) so CLAUDE.md's claim that this model is "usable directly in /pricing-model" is true.

### Tier 4 — operational (non-brand, found in passing)
- `value-consulting-orchestrator.md` (L46/51/56) hard-codes another user's absolute path `/Users/mayur@backbase.com/...` — should be repo-relative.

## Status
Tier 0 applied by the lead. Tiers 1–3 executed via parallel fixer agents (see commit history). Tier 4 noted for follow-up.
