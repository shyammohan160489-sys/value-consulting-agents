# The cost anatomy of an agent across the autonomy spectrum — and how to package & price it

**Status:** Internal / 1:1. The synthesis layer: takes the [autonomy framework](../agent-autonomy-framework.md), [Mayur's cost model](mayur-conversational-cost-model.md), the **APA agent catalog** (`../apa-matrix/`), the productized **agent catalogs** (`deal-pricing-system/knowledge_base/ai_agents/`), and the **Intelligence Credits / pillar** reference, and answers: *what actually drives agent cost, does it scale with autonomy, and how do we package & price agents across the whole product?*
**Pricing & figures internal-only. Compute-pricing layer is provisional pending Mayur's latest Intelligence Credits / compute doc (§8).**

---

## 0. The headline (the finding that reshapes the model)

**Compute is orthogonal to autonomy.** Across **28 real productized agents** (retail + wealth + commercial catalogs), the correlation between autonomy level and per-action compute cost is **−0.02 — i.e. none.** What drives compute is **tokens / data-intensity** (corr with cost **+0.99**). An **A1** "Credit Memo Drafter" costs **$0.050**/action; an **A4** "Compliance Screening" agent costs **$0.0006** — **80× cheaper at higher autonomy.**

So the intuitive pitch — *"lower autonomy ⇒ fewer tokens ⇒ cheaper"* — is **false**, and pitching it gets refuted by our own catalog. The **stronger, true** model:

> **Autonomy is the VALUE axis, the RUNTIME axis, and the ASSURANCE axis — *not* the compute axis. Compute is a separate, orthogonal meter driven by data-intensity. Price autonomy; meter compute.**

This is a *better* answer than a clean correlation would have been: it cleanly separates the flat/tiered parts (which you package by autonomy) from the variable part (which you meter), and it makes the "BYO-LLM vs our-LLM" question fall out naturally (§6).

---

## 1. The cost variables — and how each scales with autonomy

Every agent's cost decomposes into these variables, each living in a Banking OS layer. The critical column is the last one.

| Cost variable | Banking OS layer (product) | Scales with autonomy? |
|---|---|---|
| **LLM compute (tokens)** | Intelligence Fabric (the model) | **⊥ Orthogonal** — driven by *data-intensity*, not autonomy (corr ≈ 0) |
| **Orchestration steps / outcome** | Orchestration — Agent Studio | **↑ Rises** — plan→act→observe loops, multi-tool chaining |
| **Agentic runtime (always-on)** | Orchestration — hosting | **Flat base / ↑ usage** — per-agent pods ($326/agent/mo, Mayur); more replicas at high autonomy |
| **Assurance / governance** | **Sentinel** + observability (Langfuse) | **↑ Rises** — more actions to authorize, audit, eval, trace |
| **Memory / state** | **Nexus** (semantic) | **↑ Rises** — more context reads/writes per step |
| **Integration calls** | Connectivity — Grand Central | **↑ Rises** — executes across more systems |
| **Interactions / outcome** | Interaction — Unified Frontline | **↓ Falls** — agent does more per turn |
| **Human effort / outcome** | *(the bank's cost — the VALUE)* | **↓↓ Falls hard** — human moves to exceptions only |

**Read this carefully — it's the whole answer to "what does autonomy actually change?":** climbing the scale grows the **agentic platform around the model** (orchestration, runtime, assurance, memory, integration) and grows the **value** (human effort removed), while the **token bill per action stays roughly constant** and the **number of interactions per outcome falls**. The LLM is *not* where autonomy spends money. The *platform* is.

## 2. The evidence (n=28 real agents)

| | corr with compute $/action |
|---|---|
| **autonomy level** | **−0.02** (none) |
| tokens / action | **+0.99** (the driver) |
| bic_weight | +0.95 |

Per-action compute by level — note the **enormous spread within each level** (data-intensity, not autonomy, sets the cost):

| Level | n | mean $/action | min–max $ | mean tokens |
|---|---|---|---|---|
| A1 Assist | 10 | 0.0268 | 0.0006 – 0.050 (**83×**) | 2,730 |
| A2 Recommend | 4 | 0.0049 | 0.0003 – 0.018 | 825 |
| A3 Execute-on-approval | 7 | 0.0267 | 0.015 – 0.050 | 2,671 |
| A4 Execute-by-exception | 7 | 0.0229 | 0.0006 – 0.035 | 2,371 |

*The tell:* A1 spans an 83× cost range (Intelligent Search $0.0006 → Credit Memo Drafter $0.050); A4's cheapest agent (Compliance Screening, $0.0006) is cheaper than most A1s. **Autonomy and compute are independent.**

> **Caveat — the grain.** The catalog measures cost *per action*, not *per resolved outcome*. At the outcome grain, **orchestration steps per outcome** and **interactions per outcome** kick in — and those *do* move with autonomy (steps ↑, interactions ↓). The catalog can't see the multi-step loop (same blind spot as Mayur's n=2). Confirming the per-outcome curve is the open work (§8) — but the per-*action* orthogonality of compute is solid.

## 3. The reframe → the 4 commercial building blocks

Because compute is orthogonal, an agent's price is built from **four separable blocks** — three tiered by autonomy, one metered:

| # | Block | What it covers | How it's set | Maps to |
|---|---|---|---|---|
| **1** | **Agent License** (the value) | The productized agent / IP — the outcome it delivers | **Autonomy tier** (value rises with autonomy) | Factory Mission |
| **2** | **Agentic Runtime** | Always-on hosting + orchestration compute | **Flat per agent**, stepped by autonomy tier | Orchestration layer |
| **3** | **Assurance / Sentinel tier** | Governance, authority checks, audit, evals, observability | **Autonomy *ceiling*** → Entry/Critical/Enterprise | Sentinel + observability |
| **4** | **Compute** | LLM tokens | **Metered** — BYO passthrough *or* Intelligence Credits | Intelligence Fabric |

**Captured via a unit that shifts with autonomy** (the value meter): **per-seat (A1–A2) → per-interaction (A3) → per-outcome/execution (A4–A5).**

*Empirical support for the unit shift* (from the pillar reference): conversational **per-interaction** rates run **$0.40–1.80**; process-automation **per-execution** rates run **$6–15** (onboarding $8, KYC $12, fin-crime $15). **The unit AND the price both jump an order of magnitude** as you move from interaction-grain (A1–A3) to execution/outcome-grain (A3–A5) — exactly as the framework predicts.

## 4. Agentic Runtime — the new flat charge (block 2), made precise

This is the charge you flagged. It's real and it's **flat per agent, not per token:**
- **Base "to exist":** ~**$326/agent/mo** across DTAP environments (Mayur: 7 pods × $46.67) — *invariant to traffic and to autonomy at the floor.* Just hosting one agent.
- **Usage scaling:** autoscaling (~$0.006/1k requests) + observability (Langfuse, 7 units/interaction).
- **Autonomy step-up:** higher-autonomy agents run more orchestration replicas + more observability tracing → the runtime tier steps up (A1 single-pod → A4/A5 multi-replica + heavy tracing).
- **It already exists in one pillar:** the BYO platform charges **$2,500/agent/mo deployment** — that *is* an agentic-runtime charge (≈7× the raw $326 cost = healthy margin). **For productized agents, bake the equivalent runtime into the package.**

> Runtime is the cleanest autonomy-tiered, compute-independent line on the bill. It's the same whether the bank brings its own LLM or uses ours — which is the hinge for §6.

## 5. Run across the spectrum — representative agents by domain × autonomy

Pulling from the real catalogs + APA processes + NBA agents:

| Level | Conversational Banking | Relationship Intelligence (NBA) | Customer Operations / Process (APA) |
|---|---|---|---|
| **A1 Assist** | Intelligent Search · Just-Ask answer · Employee Workspace Assist | Meeting Prep · Portfolio Commentary · RM Briefing Copilot | SAR Narrative draft · Credit Memo Drafter |
| **A2 Recommend** | Smart Recommendations · Proactive Alerts | **NBA Engine** · Cash-Flow Forecasting · Risk Scoring (advise) | Covenant flag (recommend) |
| **A3 Execute-on-approval** | Customer Conversational (Transact: transfer, card) | Personalised Outreach (send on approval) | Dispute Triage · KYC Auto-Extract · Trade-Finance Checker · Loan Decision · Periodic Review *(suitability-capped)* |
| **A4 Execute-by-exception** | Resolve loops (STP + handoff) | Risk/attrition auto-monitor | Onboarding STP · KYB · Fraud/AML Triage (auto-close FPs) · Compliance Screening · Covenant Monitoring |
| **A5 Self-directed** | (multi-turn mission) | (autonomous book management — ceiling-limited) | Multi-process orchestration (Factory Mission) |

*(Autonomy assignments are the documented working mapping — validate per deployment; the same agent can sit a level higher/lower by configuration.)*

## 6. BYO-LLM vs our-LLM (Intelligence Credits) — the compute meter

Mayur's model assumed **BYO LLM + bank builds its own agents.** Reality is a 2×2. Because compute (block 4) is orthogonal and metered, the **other three blocks are invariant** — only block 4 changes:

| | **Bank brings own LLM** | **Bank uses our LLM** |
|---|---|---|
| Blocks 1–3 (License + Runtime + Assurance) | **Same — autonomy-tiered** | **Same — autonomy-tiered** |
| Block 4 (Compute) | **Passthrough** — bank pays its own tokens; we charge orchestration margin only | **Intelligence Credits** — metered IC (a normalised unit of AI work), our margin on tokens |

**Intelligence Credits already exist in the engine** as **BICs** ("a normalised unit of AI work; each agent action has a BIC weight by complexity," 0.1 deterministic → 5.0 complex orchestration). That weight scale is essentially **a compute proxy, not an autonomy proxy** (it tracks tokens at +0.95) — consistent with §0. **The IC unit is the right currency for metered compute precisely because it's data-/complexity-indexed, not autonomy-indexed.** *(Reconcile with Mayur's latest IC doc — §8.)*

## 7. Agent Factory vs productized agents — the packaging split

| | **Productized agents** | **Agent Factory (build-your-own)** |
|---|---|---|
| What | Pre-built agents sold as **packages chosen by autonomy level** | Platform to build custom agents |
| Price | Blocks 1–4: License (autonomy-tiered) + Runtime + Assurance + Compute (IC/BYO) | Platform fee + per-agent **runtime** ($2,500/agent/mo) + Compute + (no License — they build the value) |
| Buyer | COO / business (buys outcomes) | CTO (buys capability) |
| Sell motion | **Catalogue / SKU** — "pick agents at the autonomy you're ready for" | Land platform, expand agents |

**Packaging recommendation — SKUs by autonomy:**
- **Assist Pack (A1)** — per-seat · Entry assurance · light runtime
- **Recommend Pack (A2)** — per-seat + per-signal · Entry/Critical
- **Transact/Resolve Pack (A3–A4)** — per-interaction → per-resolution · Critical/Enterprise · multi-replica runtime
- **Autonomous Missions (A4–A5)** — per-outcome (value-share) · Enterprise
- **Compute** is a **separate metered line on every SKU** (IC or BYO) — never bundled into the autonomy tier, because two agents at the same level can differ 80× in tokens.

## 8. Open variables / what unlocks the rest

1. **Mayur's latest Intelligence Credits / compute doc** — needed to lock block 4 (IC unit economics, our-LLM margin, how IC relates to the engine's BIC scale). **Requested.**
2. **The agentic-runtime tariff** — turn $326/agent/mo + autoscaling into an autonomy-tiered runtime price (A1 → A5 steps). Needs the orchestration-replica assumptions per level.
3. **Per-outcome curve** — model orchestration-steps-per-outcome and interactions-per-outcome (the catalog's blind spot) to prove the value-side rise. This is the simulation: take ~8 agents spanning A1–A5, add steps-per-outcome + interactions-per-outcome columns, compute cost-per-outcome vs cost-per-action.
4. **Validate autonomy assignments** (§5) and the within-level token spread against live deployments.

**Next build (once #1 lands):** the spectrum simulation — one sheet, ~8 agents × A1–A5, four cost blocks separated, BYO vs IC toggle, per-action vs per-outcome curves. That's the artifact that turns this into a pricing tool.
