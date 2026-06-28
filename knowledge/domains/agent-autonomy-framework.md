# AI Agent Autonomy — Classification & Pricing Framework

**Status:** Internal IP / 1:1. Reusable across **all** agentic engagements (Conversational Banking, Relationship Intelligence, Customer Operations, wealth NBA). This is the developed framework; its seed was [`agent-autonomy-pricing-brief.md`](agent-autonomy-pricing-brief.md).
**Extends:** [`banking-os.md`](../product/banking-os.md) (control plane · Nexus · **Sentinel authority spectrum** · 4 solutions) · [`backbase-smart-signals.md`](backbase-smart-signals.md) (execution ladder, named agents) · [`wealth/next-best-action-method.md`](wealth/next-best-action-method.md) (4-lens NBA method) · the BIC pricing engine in `deal-pricing-system/`.
**Handling:** Pricing figures and named customers are **internal-only**. Forward-looking agents are **product direction, not shipped fact** — attribute accordingly in client materials. "Palantir of banking" is an analyst quote — attribute, don't claim.

---

## 0. The one idea

A **single autonomy spectrum** that, as you climb it, *simultaneously* means: more autonomy · higher maturity (crawl→walk→run) · greater agent complexity (one tool call → multi-step, multi-agent, self-correcting) · richer multimodality (text→voice→docs→actions) · **less human effort per outcome**. Because all of these co-vary, one level number is usable as **both a classification scheme** (bucket every agent) **and a pricing basis** (higher level ⇒ more compute + orchestration + value + assurance).

**The key finding from grounding this against the product canon:** *we are not inventing a scale.* Backbase already ships three partial autonomy ladders —

- **Sentinel's authority spectrum:** *recommend → approve → execute* (banking-os.md §2)
- **Conversational Banking's four verbs:** *Assist → Transact → Resolve → Grow* (banking-os.md §4)
- **Smart-signals' execution ladder:** *surface-only → create task → launch agent* (backbase-smart-signals.md §4)

The framework's job is to **fuse these into one named scale** and make it the spine that the existing three-layer BIC pricing already implies (`bic_weight` is the complexity-and-therefore-autonomy proxy the engine prices on today). This makes the scale *product-true*, not a consulting overlay.

---

## 1. The scale — A0 → A5 (the **Frontline Autonomy Scale**)

> **Branding decision (recommend → confirm):** brand it the **Frontline Autonomy Scale (FAS)**, levels **A1–A5**, with **A0** as the manual baseline (the From-state). It ties to the "Unified Frontline" brand, works as both classification and pricing tiers, and is CEO-sayable. *Alternative:* keep it generic ("autonomy levels L1–L5"). Flagged for sign-off in §8.

**A0 — Manual.** No agent. Today's fragmented frontline; the **FROM** in From→To. The pricing floor (€0 AI). Included only because it anchors the narrative and the value delta.

| Level | Name | What the AI does | Human's role | Citi loop | Human effort |
|---|---|---|---|---|---|
| **A1** | **Assist** (Co-pilot) | Answers, drafts, retrieves — **on request** | Does the work; AI assists when asked | **In** | High |
| **A2** | **Recommend** (Augmented) | **Proactively** recommends the next action, ranks, pre-fills | Reviews & **approves each** action | **In** | Med–High |
| **A3** | **Execute-on-approval** (Supervised) | Executes a task **end-to-end within bounds**, pauses for sign-off before commit | Approves before commit / can intervene | **On** | Med |
| **A4** | **Execute-by-exception** (High) | Acts autonomously within policy; **escalates only edge cases** | Supervises; handles exceptions | **On → Out** | Low |
| **A5** | **Self-directed** (Full) | Sets sub-goals, acts, **self-corrects** across multi-step / multi-agent | Sets **intent & guardrails only** | **Out** | Minimal |

**Citi-loop collapse:** in-loop ≈ A1–A2 (approve each) · on-loop ≈ A3–A4 (supervise / exception-only) · out-of-loop ≈ A5. The 3-loop framing is the executive shorthand; A1–A5 is the working resolution.

---

## 2. The unifying read — the scale *is* the product (not an overlay)

This is the table to lead with internally — it proves the scale is the single read of constructs we already have. Every column is an existing Backbase primitive.

| Level | **Sentinel** authority | **Conversational Banking** verb | **Smart-signal** execution | What's governed |
|---|---|---|---|---|
| **A1** Assist | *(read / draft — no execution authority)* | **Assist** (answer, find, navigate) | **Surface-only** | Output quality (no action taken) |
| **A2** Recommend | **recommend** | **Grow** (NBA / financial-progress nudge) | **Surface / Create task** | Recommendation + ranking; compliance gates surface |
| **A3** Execute-on-approval | **approve** (gate before commit) | **Transact** (authenticated routine action) · **Resolve** (gated loop) | **Launch agent (with approval)** | The action, at the approval gate; full audit |
| **A4** Execute-by-exception | **execute** (within policy) | **Resolve** at scale — *STP where possible, human handoff where needed* | **Launch agent (auto, gated on exceptions)** | Continuous monitoring + immutable audit + policy engine |
| **A5** Self-directed | **execute** (delegated authority within guardrails) | *(multi-mission orchestration)* | **Multi-agent orchestration** | The whole mission; maximal assurance burden |

Read across A4: *"STP where possible, human handoff where needed"* is **verbatim Customer Operations** (banking-os.md §4). The product already describes execute-by-exception — we are naming the level, not adding a capability.

**Why this matters commercially:** the differentiator is *being in the execution path* (banking-os.md §5). Autonomy level **is** depth-in-the-execution-path. A1 sits beside the path (advice); A5 runs it. The further along, the more of the "messy middle" (~60% of bank work in the whitespace between systems) the agent absorbs — which is exactly where the value and the price are.

---

## 3. Mapping Backbase's agents onto A1–A5

Representative agents from the product canon and the engine's domain catalogs. *(Forward-looking items = product direction, not shipped fact.)*

| Agent (source) | Default level | Notes |
|---|---|---|
| **Meeting Prep / Meeting Preparation** (smart-signals) | **A1** | Consolidates client context; human runs the meeting. Read-only. *The copilot beachhead everyone ships first* (NBA method §4). |
| **Market Move Explainer** (smart-signals) | **A1 → A2** | A1 when it drafts a brief on request; A2 when it *proactively* pushes to affected portfolios. |
| Portfolio commentary · review prep · credit-memo draft | **A1** | Drafting; human owns the output. |
| Conversational **Assist** (Just-Ask answer) | **A1** | Answer / navigate. |
| **Smart Signal NBA / Next-Best-Action** | **A2** | Proactively recommends + ranks; RM approves. The Relationship-Intelligence "Grow" surface. |
| **Personalised Outreach** (smart-signals) | **A2 → A3** | A2: drafts, RM approves send. A3: sends on approval / within rules. **The canonical "same agent, two levels" example** (see below). |
| Covenant monitoring · dispute triage (commercial/retail) | **A2 → A4** | A2 alert → A4 auto-action within thresholds, exception handoff. |
| Conversational **Transact** (freeze card, update details, status) | **A3** | Executes an authenticated routine action on confirmation. |
| **Customer Operations Resolution Loops** (dispute / payment / KYC / fraud) | **A3 → A4** | Gated at A3; A4 once STP thresholds + exception handoff are trusted. |
| Onboarding doc collection · KYC/KYB automation | **A3 → A4** | Servicing class; high autonomy ceiling. |
| **Factory multi-agent Mission orchestration** | **A5** | The platform ceiling. Rare in production for regulated work (see §4). |

**The pricing hook — "same agent, configurable level."** Personalised Outreach licensed at A2 (draft-and-approve) and at A3 (send-on-rules) are *different products commercially*: A3 does more compute, touches more systems, carries more assurance, and replaces more human effort. **You license an agent up to a maximum autonomy level**, and compute + value + assurance all scale with that ceiling. This is consistent with smart-signals' own point that signal *type* and *execution* are bank-configurable (surface-only / task / agent) — autonomy is the dial.

---

## 4. Governance ceiling per use-case class

**The principle: the ceiling is set by *accountability and harm*, not by capability.** Capping below A5 for advice is a **feature** — it is the architecture regulators already reward (FCA Consumer Duty + SM&CR wrote *no* new AI rules; human-in/on-the-loop + overridable + auditable maps to them 1:1 — NBA method §2). Sell it as licence-to-operate, never as a limitation.

| Use-case class | Ceiling | Rationale |
|---|---|---|
| **Regulated advice** (suitability-bearing: investment advice, lending decisions) | **A3** | A named human must stay accountable (SM&CR). Execute-on-approval is the ceiling; never autonomous. |
| **Customer-facing financial actions** (payments, transfers, card actions) | **A4** within strict limits | Sentinel limits + step-up auth; high-value / novel → drops to A3. |
| **Servicing & operations** (KYC docs, dispute triage, status, data updates) | **A4** routine; **A5** for low-risk, high-volume STP with exception handoff | The Customer Operations sweet spot. |
| **Internal productivity** (meeting prep, summarisation, commentary, retrieval) | **A5** possible | No external action / no customer commitment — but usually A1 by nature. |
| **Financial crime / fraud / risk** | **mandatory gate at every level** | Compliance events are must-surface Alert "gates"; auto-block can be A4 but always with a human review trail. |

In the engine this becomes a **hard check**: a deal may not license an agent above its use-case-class ceiling, and licensing A4/A5 forces the assurance/platform tier up (§5–6).

---

## 5. The autonomy → pricing model

The brief asked for pricing across four co-variates — **compute · interaction/orchestration · value · assurance**. The finding: **each maps onto a lever the engine already has.** Autonomy level is not a new pillar; it is the *organising spine* that bands and triggers the existing levers.

### 5.1 The four co-variates → existing levers

| Co-variate | Existing lever | How autonomy drives it |
|---|---|---|
| **Compute** | `bic_weight` × volume + compute pass-through | Autonomy level sets the **BIC-weight band** (5.2). The engine already prices on `bic_weight`; autonomy is the *client-legible* way to set it. |
| **Interaction / orchestration** | step count / system touches per run (folded into `bic_weight`; per-interaction count for conversational) | Higher level = more steps, more system touches → naturally heavier weight. |
| **Value** | unit of price (per-seat / per-interaction / per-outcome) | **The unit itself is a function of the level** (5.3). This is the elegant answer to "what's the unit of price?" — there isn't one; it shifts as autonomy rises. |
| **Assurance / governance** | Domain Base / platform tier (Entry/Critical/Enterprise = Sentinel) | The **max autonomy level licensed sets the platform-tier floor** (5.4). Folded into the platform fee — *not* a separate punitive line. |

### 5.2 BIC-weight bands by level (aligns to the engine's existing simple/medium/complex thresholds)

The engine derives complexity from `bic_weight` (simple ≤1.0, medium ≤3.0, complex >3.0). Autonomy standardises the bands within that:

| Level | `bic_weight` band | Engine complexity |
|---|---|---|
| A1 Assist | 0.2 – 1.0 | simple |
| A2 Recommend | 1.0 – 2.0 | medium (low) |
| A3 Execute-on-approval | 2.0 – 3.0 | medium |
| A4 Execute-by-exception | 3.0 – 5.0 | complex |
| A5 Self-directed | 5.0+ | complex+ |

*(Bands are the proposed mapping — validate against live catalog weights before committing.)*

### 5.3 Unit of price shifts with the level (the core mechanic)

| Level | Primary unit | Why |
|---|---|---|
| A1–A2 | **per-seat** (per-user/mo) | The agent augments a *named human*; value = productivity per user. Matches the playbook's per-user metric. |
| A2–A3 | **per-interaction / per-action** | Conversational base + per-interaction (€0.07 model, banking-os.md §10). Value = work done, not seats. |
| A4–A5 | **per-resolution / per-outcome** | The human is out of the loop; price the *outcome*. Matches the playbook's "start per-execution, slide into per-outcome." |

**Cost-plus vs value-share (avoiding "penalising the customer for the platform doing more"):** keep A1–A3 **cost-plus** (per-seat / per-interaction — predictable, defensible). Reach for **value-share** (per-outcome with a floor) only at **A4–A5**, where the agent replaces whole processes/FTEs and the outcome is measurable. *Autonomy level tells you when you've earned the right to price the outcome.*

> **Empirically grounded (2026-06).** Mayur's bottom-up Conversational Banking cost model shows **per-interaction cost is roughly flat (~$0.037–0.040) and not monotonic in autonomy** — confirming the interaction meter is the right instrument for A1–A3 (the autonomy relabel is economically free) but **structurally under-prices A4–A5**, where the unit must shift to per-outcome. Full test: [`agent-pricing/autonomy-cost-correlation.md`](agent-pricing/autonomy-cost-correlation.md); model digest: [`agent-pricing/mayur-conversational-cost-model.md`](agent-pricing/mayur-conversational-cost-model.md).

### 5.4 Assurance tier triggered by the autonomy ceiling

The platform/Domain-Base fee **is** the assurance layer (Sentinel: continuous monitoring, immutable audit, policy engine, eval, guardrails). Reuse the canonical tiers (banking-os.md §10) with a *principled trigger*:

| Max autonomy licensed | Platform-tier floor |
|---|---|
| A1–A2 | **Entry** |
| A3 | **Critical** |
| A4–A5 | **Enterprise** |

You cannot buy A4 ops autonomy on the Entry assurance tier — the governance burden (real-time monitoring, immutable audit at scale, exception routing) genuinely costs more, and the regulator expects it. This makes the tier step-up *defensible*, not arbitrary.

> **Pricing-figure note (do not silently reconcile):** use **banking-os.md §10** as the canonical pricing *shape* (Entry €350K · Critical €700K · Enterprise €1.5M + LOB €350K/domain + per-interaction from €0.07 + compute pass-through at cost). The `deal-pricing-system` engine's defaults ($250K entry, BIC blocks) **predate** the June 2026 Conversational pricing and should be **reconciled with deal-desk** — flag, don't merge. (Per the "separate commercial tracks" discipline.)

### 5.5 The composite formula

```
Price(deal) =
    Assurance/Platform tier        ← set by MAX autonomy level licensed (5.4)
  + LOB fee × domains              ← per domain activated (banking-os.md §10)
  + Σ agent [ autonomy-banded bic_weight × volume ]   ← compute/orchestration (5.2)
  + compute pass-through (at cost) ← transparent; voice STT/TTS lives here, not in margin
  + unit charge, BASIS set per agent by its level     ← seat → interaction → outcome (5.3)
```

The **three-layer transparency** (raw compute → platform price → build-it-yourself) is untouched — autonomy *organises* it, it doesn't replace it. Three-layer is a red line in the playbook; keep it.

### 5.6 Two open questions, answered

- **Multimodality multiplier?** **No — bake it into the level.** Multimodality co-varies with autonomy by definition (text→voice→docs→actions); a voice+action agent already carries a heavier `bic_weight`. A separate multiplier would double-count and muddy "pay for outcomes, not infrastructure." *Exception:* voice has a real extra compute cost (STT/TTS) — recover it in **compute pass-through at cost**, never as a margin multiplier.
- **Band compute to level?** **Yes** — via 5.2. Already engine-compatible.

### 5.7 Two axes, not one — autonomy × production mode

Autonomy (*what the agent does*) is orthogonal to **production mode** (*who builds the intelligence* — the smart-signals **signal source**: Third-Party / Rule-Based / Agentic, a.k.a. Connect / Configure / Compose). Pricing keys off **both**:

- **Production mode → who owns the hard build** → affects `bic_weight` and Domain Base. (A heavy ML use case is *Low* Backbase-complexity if the bank owns the model and sends a Third-Party Signal; *High* if Backbase builds the inference — NBA method §2.)
- **Autonomy → the unit of price + the assurance tier.**

| | A1–A2 (low autonomy) | A3 (approval) | A4–A5 (high autonomy) |
|---|---|---|---|
| **Rule-Based** (Configure) | cheap quick-win, Entry | per-action, Critical | rare — rules don't self-direct |
| **Agentic** (Compose) | NBA surface, Entry | gated agent, Critical | per-outcome, Enterprise — the flagship |
| **Third-Party** (Connect) | bank's model surfaced, Entry | bank's model → action | bank's model drives autonomous loop |

This also reconciles the **pillars**: Pillar 1 Embedded ≈ A1–A2 · Pillar 2 Conversational ≈ A1(Assist)→A3(Transact)→A4(Resolve) · Pillar 3 Process Automation ≈ A3–A5. The pillars are the coarse *packaging* cut; autonomy is the fine axis that explains *why* a Pillar-3 agent costs more than a Pillar-1 one.

---

## 6. Engine integration spec (`deal-pricing-system/`)

Additive, non-breaking. *(Spec only — engine code is architect-tier; this is the handoff.)*

1. **Add `autonomy_level: A1–A5`** to `AIAgent` and `AIAgentSelection` (`models/ai_pricing.py`).
2. **Validate `bic_weight` against the level band** (5.2) — warn if an agent's weight is outside its level's band; autonomy becomes the legible way to *set* the weight (keep `bic_weight` as the computed driver — no breakage).
3. **Add `use_case_class` + `governance_ceiling`** per agent; the engine **rejects** any selection above its class ceiling (§4) and surfaces the reason.
4. **Set the Domain-Base / platform-tier floor from `max(autonomy_level)`** across selected agents (5.4) — automatic, defensible assurance step-up.
5. **Add `value_basis` (seat / interaction / outcome)** derived from level (5.3) → routes each agent to per-user vs conversational-per-interaction vs per-execution/outcome pricing.
6. **Keep the three-layer output** (raw compute / platform / BIY) exactly as-is.

---

## 7. How this cascades into deliverables

- **Discovery / NBA classification:** add autonomy level as a 5th lens alongside the NBA method's four (§1 of that method). Each wish-list item gets an A-level → drives both the roadmap *and* the price.
- **Roadmap / phasing:** sequence A1–A2 quick wins (prove the platform) → A3 gated execution → A4 exception-based ops → A5 selectively. Mirrors the NBA "phasing waves."
- **Commercial / pricing deck:** the autonomy ladder *is* the pricing tier ladder — one visual carries classification, maturity, and price. Use it in `/pricing-model` and the negotiation narrative.
- **Governance story:** lead with the ceiling table (§4) as licence-to-operate — the regulator-rewarded architecture, not a constraint.
- **Voice:** From (A0 manual / fragmented) → To (the right autonomy level per use case, governed by Sentinel). Outcomes-first, per the narrative spine.

---

## 8. Open decisions / fold-in next

1. **Branding sign-off** — adopt **Frontline Autonomy Scale (A1–A5)**, or keep generic L1–L5? (§1)
2. **Source content** — Mayur's bottom-up Conversational Banking cost model has been ingested (see [`agent-pricing/`](agent-pricing/)). Its compute truth now anchors the pricing logic. More source drops expected; land them in `agent-pricing/`.
3. **BIC-weight bands (5.2)** — validate against the live domain catalogs *and* Mayur's per-purpose token data (Reasoning / Tool-Calling vs the near-free Embedding / Guardrails / Evals) before committing the bands.
6. **Prove the correlation (n=2 → n≥5)** — model A2/A4/A5 use cases in Mayur's sheet with an *interactions-per-outcome* column to turn the directional finding into a defensible one (correlation note §4).
4. **Pricing-figure reconciliation** — align the engine defaults to banking-os.md §10 with deal-desk (5.4 note). Flag, don't silently merge.
5. **Engine build** — §6 is the architect handoff; decide whether to implement now or keep as spec.
