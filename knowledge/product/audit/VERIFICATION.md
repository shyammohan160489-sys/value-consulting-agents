# Banking OS Cascade — Verification Pass

**Date:** 2026-06-09 · **Type:** Verification (confirm fixes landed; flag residual misalignment)
**Standard:** `knowledge/product/banking-os.md` (substance) + `knowledge/design-system/narrative-spine.md` (voice)
**Inputs verified against:** `01_skills.md` · `02_agents.md` · `03_knowledge.md` · `04_templates.md` · `REPO_ALIGNMENT_AUDIT.md`

---

## 1. HIGH-findings pass/partial/fail table

### Skills (`01_skills.md` — 4 HIGH)

| Finding | Verdict | Evidence |
|---|---|---|
| `executive-briefing.md` — no spine/banking-os pointer; no From→To anchor | **PASS** | "Canon — read first" block at L5 names banking-os.md + narrative-spine.md, 4 solutions, retires "engagement banking / better channels". |
| `executive-briefing-slides.md` — off-brand example cover ("Transforming / Client Experience / digital strategy") + missing spine | **PASS** | Canon block at L7. Example cover (L352-353) now reads "From frontline fragmentation / to a Unified Frontline." |
| `prototype.md` — legacy tokens (`#0052CC`, Inter), no spine | **PASS** | Canon block L7. Tokens re-based: `--navy:#041326`, `--primary:#3367FF`, Libre Franklin, cites `frontline-tokens.json` (L41-56). |
| `usecase-doc.md` — module enum names "Digital Assist / Digital Engage" | **PASS** | Canon block L7. §1 + §8 "Backbase Solution" = Digital Banking / Conversational Banking / Relationship Intelligence / Customer Operations (L23, L131). No "Digital Assist/Engage". |

### Agents (`02_agents.md` — 5 HIGH)

| Finding | Verdict | Evidence |
|---|---|---|
| `narrative-assembler.md` — 3-fabric/13-product as authoritative; NEXUS=HELIX; no Sentinel/4-solutions/From→To | **PASS** | Canon block L10. banking-os.md flagged CANONICAL (L72); lexicon flagged LEGACY (L73). Nexus + Sentinel as distinct layers (L112, L150-164). BIAN table 3rd col → Banking OS model (L82-93). Acquire/Activate/Expand/Retain marked legacy (L99, L118). See deep-fix §2b. |
| `discovery-transcript-interpreter.md` — no spine; no value-leakage lens | **PASS** | Canon block L10 adds value-leakage / whitespace-between-systems FROM lens. |
| `capability-assessment.md` — maturity not framed as distance-from-Unified-Frontline; no spine | **PASS** | Canon block L10 reframes maturity as distance from "running as one"; assess Conversational Banking + Resolution-Loop readiness. |
| `journey-builder.md` — cites stale lexicon; no spine/Resolution Loops | **PASS** | Canon block L10. banking-os.md added as CANONICAL ref #7 (L30); lexicon explicitly marked **legacy**. |
| `usecase-designer.md` — old 10-layer architecture + "Backbase Module: Digital Assist"; channel-era value themes | **PARTIAL** | Canon block L10 instructs mapping to 4 Solutions. **But** the body's "Backbase Architecture Layers" section (L144-153) still teaches the legacy 10-layer model incl. "Integration Services (Grand Central)" and is **not** marked legacy. Pointer landed; hard-coded stale body content not reframed. |

### Knowledge (`03_knowledge.md` — 5 named HIGH rows; headline tally says 6)

> Note: the slice headline says "HIGH 6" but the findings table lists **5** HIGH rows. Verified the 5 named files. The 6-count appears to be a tally rounding/miscount in the source report.

| Finding | Verdict | Evidence |
|---|---|---|
| `backbase_platform_lexicon.md` — keystone stale "authoritative" file | **PASS** | Canonical banner at L5 routes to banking-os.md; explicitly states "Where this lexicon describes an older model … banking-os.md supersedes it." Old model retained as background. |
| `Ignite Inspire/agent-6-presentation.md` — "6-product suite / 3-plane / omnichannel / Grand Central" deck model | **PASS** | Canonical banner L7; control-plane / 4-solutions rebuild at L509-520; "6-product suite" grid marked superseded. |
| `Ignite Inspire/agent-1-strategy.md` — "Backbase is an Engagement Banking Platform" | **PASS** | Canonical banner L7; platform primer rewritten to "AI-Native Banking OS … control plane … Nexus + Sentinel" (L235). |
| `Ignite Inspire/agent-4-architecture.md` — "EBP as Integration Hub (Grand Central)"; omnichannel | **PASS** | Canonical banner L7 re-anchors on control-plane layer model; Grand Central reframed as the INTEGRATE primitive. |
| `competitor_intelligence.md` — "digital banking platform market / customer-experience orchestration" wedge | **PASS** | Canonical positioning banner L3; "the wedge" (L9) re-led on control plane + governed agentic execution ("AI won't fix fragmentation — it amplifies it"). |

### Templates (`04_templates.md` — 3 HIGH)

| Finding | Verdict | Evidence |
|---|---|---|
| `assessment_report.md` — 7-section skeleton sells "Unified Banking Platform / progressive modernization"; no From→To / 4-solutions | **PASS** | TOC guidance (L28-33) opens on From→To; Section 2 (L173-188) = control plane / Nexus / Sentinel / 2-domains→4-solutions / Resolution Loops / three value pools. |
| `assessment_report.md` — lifecycle value model names deprecated products (Grand Central, Digital Engage/Assist, Data Foundations) | **PASS** | L32 explicitly: "Do NOT use the deprecated names Grand Central, Digital Engage, Digital Assist, Data Foundations." Value model (L251-260) mapped to the 4 solutions + Resolution Loops + value pools. (Minor: L234 still cross-refs lexicon for product names — but lexicon is now re-based with a canonical banner; lifecycle stages L257-260 retained as a flagged "narrative aid".) |
| `capability_assessment.md` — glossary defines "HELIX / Customer Brain / Grand Central / Flow Foundation" | **PASS** | Glossary (L499-501) rewritten to Banking OS / Nexus / Sentinel. HELIX, Customer Brain, Grand Central, Flow Foundation removed from glossary. |

**HIGH tally:** 16 verified findings (4 skills + 5 agents + 5 knowledge + 3 templates — the 6th knowledge HIGH is a source-report miscount). **15 PASS · 1 PARTIAL · 0 FAIL.**

---

## 2. Deep-fix checks

### 2a. `tools/pricing_model.py` + `.claude/commands/pricing-model.md`

- **Selftest:** `python3 tools/pricing_model.py --selftest` → exit 0.
  **Result line:** `SELFTEST: PASS ✓`
- **CONVERSATIONAL section present:** YES — selftest output includes `— CONVERSATIONAL (platform + LOB + per-interaction) —` with 7 regression points (e.g. `Critical · 3 domains @ 250,000/mo = €1,610,000 [ok]` … `Enterprise · all dom @ 2,000,000/mo = €3,054,000 [ok]`).
- **Native `conversational` basis (not a tiered_per_unit workaround):**
  - `.py`: `price_conversational()` defined (L100); dispatched as a first-class basis (`if basis == "conversational": return price_conversational(...)`, L60). Banner cites banking-os.md §10.
  - `.md`: documents **three** bases; **#3 `conversational`** (L63) — "platform fee (Entry €350K · Critical €700K · Enterprise €1.5M) + LOB fee €350K/domain + per-interaction from €0.07 + LLM compute pass-through … activated per domain, not per customer/channel." Explicitly the canonical Banking OS deal shape, **not** a tiered_per_unit mapping.

  **Verdict: PASS.**

### 2b. `.claude/agents/narrative-assembler.md`

- **Nexus AND Sentinel both present as distinct layers:** YES. L112 lists "Nexus (shared source of customer truth … system of *truth*, not of record) · Sentinel (governed, auditable execution)" as separate primitives; L150-164 give each its own subsection; L151 explicitly: "two distinct primitives — Nexus and Sentinel (do not collapse them into one)."
- **BIAN table third column no longer says "Flow Foundation / Digital Assist / Data Foundations / Agentic AI":** CONFIRMED. The BIAN table (L82-93) third column now maps to the Banking OS model — Digital Banking, Customer Engagement (domain), Sentinel (governed execution), Nexus (shared source of truth), Relationship Intelligence / Intelligence layer, Customer Operations (Resolution Loops). The old product-name mapping is gone from the table. (Flow Foundation / Digital Assist / Data Foundations still appear in the repo, but only inside the explicitly **LEGACY**-bannered product-line tables at L118-180, as historical reference + a translation map to the 4 solutions — not as the BIAN column.)
- **Acquire/Activate/Expand/Retain marked legacy:** YES. L99 — "The older Acquire → Activate → Expand → Retain flywheel is a *legacy lens* … do not present it as the product story." L118 banner lists it among LEGACY tables.

  **Verdict: PASS.**

---

## 3. Residual retired positioning (live tree only)

**Scope/exclusions applied:** excluded `knowledge/product/**`, the audit reports, `**/deprecated/**`, `**/worktrees/**`, `banking-os-alignment-checker.md` (legitimately names the phrases as detection anti-patterns), and any line already labelled LEGACY/superseded/retired.

### Genuine residuals (product positioning that should have been caught)

| # | File:line | Phrase | Why it's a residual |
|---|---|---|---|
| R1 | `.claude/commands/domain-pain-points.md:60` | "Omnichannel platform" | Worked-example **solution** column maps "Fragmented experience across channels → Omnichannel platform" — teaches retired solution language. (Audit MED, not closed.) |
| R2 | `templates/long-form/document-template.html:603` | "Grand Central iPaaS" | Architecture-diagram layer label hard-codes a deprecated product name; inconsistent with the same diagram's correct "AI-Native Banking OS" label one row up. (Audit MED, not closed.) |
| R3 | `.claude/agents/usecase-designer.md:144-153` | 10-layer architecture incl. "Integration Services (Grand Central)" | Legacy architecture list taught as the live model, not marked legacy (same as the PARTIAL above). |
| R4 | `.claude/agents/workshop-preparation.md:141,310` | "Digital Assist capability alignment" / "Digital Assist capabilities mapped" | Names a retired product as a live capability to map; not legacy-labelled. (Canon pointer present at L10, but body content stale.) |
| R5 | `.claude/agents/capability-gap-analyzer.md:75,124` | "Flow Foundation" in example capability columns | Example use-case rows cite a retired product line as the live capability vocabulary; not legacy-labelled. (The L222 MCP-query fix landed; these example rows did not.) |
| R6 | `.claude/agents/usecase-designer.md:194` (per audit) / roi-hypothesis-builder.md:101 | "Flow Foundation" / DOL.x enabler names | Enabler examples still use old product/feature codes rather than the 4 solutions. (Audit MED for ROI agent.) |

### Not residuals (correctly excluded — judged in-scope-but-defensible by the audit)

- `knowledge/standards/capability_taxonomy*.md` "Omnichannel with context continuity" — maturity-ladder **mid-rung vocabulary**, explicitly judged defensible by the audit ("can stay if reframed"). Not lead positioning.
- `knowledge/discovery_question_bank.md:225` "headless/omnichannel architecture?" — a client-context discovery probe (audit LOW), not positioning.
- `knowledge/competitor_intelligence.md:69` "Limited true omnichannel capability" — describes a **competitor's** gap, not Backbase positioning.
- `knowledge/domains/retail/personas.md:33` "Primary Channel: Omnichannel" — persona attribute, not positioning.
- `knowledge/domains/apa-matrix/apa_simulations.json:3185` "Omnichannel Auto" — a process-sim data label, not positioning.
- `knowledge/backbase_platform_lexicon.md` (timeline rows L133-134, EBP gloss L524) — historical product-evolution timeline, under the file's canonical "superseded" banner.
- `knowledge/Ignite Inspire/*` omnichannel/Grand Central/Digital Engage uses — all under the pack's new canonical banners marking the legacy framing superseded; flagged MED (pack-level reframe), not HIGH.
- `narrative-assembler.md` L122-180 retired product names — inside the explicit LEGACY-bannered tables / translation map.

**Genuine residual count: 6** (R1–R6). All are residual MED-level body content under files that now carry the correct Canon/canonical pointer — i.e. the cascade pointer landed everywhere, but a handful of hard-coded legacy examples in agent/skill/template bodies were not scrubbed.

---

## 4. Cascade-pointer coverage counts

| Surface | With pointer to banking-os.md / narrative-spine.md | Total files | In-scope target | Status |
|---|---|---|---|---|
| Skills (`.claude/commands/*.md`) | **19** | 30 | ~10 narrative/deliverable skills | All narrative skills covered. The 11 without (chunk-document, deal-notes, extract-learnings, log-modification, profile-bank, publish, reconcile, run-pipeline, scan-engagement, sync-telemetry, upgrade-analysis) are operational/non-narrative — correctly out of scope. |
| Agents (`.claude/agents/*.md`) | **14** | 22 | 12 narrative agents | All **12** flagged HIGH/MED narrative agents carry the pointer (verified individually). The 8 without are internal/system agents (coach/dev/release/review-agent, knowledge-harvester), the orchestrator (thin router, LOW), benchmark-librarian (LOW), and the roi-business-case-builder stub (LOW) — all audit "no action required / optional". |

**12/12 target narrative agents** and **all targeted narrative skills** now carry the Canon pointer. Coverage matches the audit's Tier-1 intended scope.

---

## 5. Overall verdict

**The HIGH findings are closed.** 15 of 16 verifiable HIGH findings are PASS; the one remaining (**`usecase-designer.md`**) is PARTIAL — its Canon pointer landed and directionally supersedes the stale content, but the legacy 10-layer architecture list in its body was not reframed to the 4 solutions. No HIGH finding is FAIL. Both deep fixes (pricing_model conversational basis; narrative-assembler Nexus/Sentinel + BIAN table + legacy-flagged lifecycle) fully verified.

The cascade pointer is now wired the way the visual tokens were — every target narrative skill (≈10) and all 12 narrative agents route to banking-os.md + narrative-spine.md. Residual exposure is no longer architectural (a missing authority pointer) but cosmetic: a small set of un-scrubbed legacy product names in example/body content of files that already carry the correct pointer.
