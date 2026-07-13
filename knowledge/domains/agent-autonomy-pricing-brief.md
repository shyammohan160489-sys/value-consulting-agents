# AI Agent Autonomy — Classification & Pricing Framework
### Working brief / session seed — feed this into a fresh session to continue

> **✅ DEVELOPED — see [`agent-autonomy-framework.md`](agent-autonomy-framework.md).** This brief is the original seed; the agenda below (5-level scale, agent mapping, autonomy→pricing model, governance ceiling, engine reconciliation) has been worked through in that module. Keep this file for provenance; **work from the framework**.

> **Purpose.** Spin-off from the Schroders NBA-signals work. There, we used a collapsed 3-step autonomy axis (Assist → Recommend → Act). This brief captures the fuller **5-level** idea and the **pricing** thesis so a dedicated session can develop it. Keep NBA-signals work separate; this is the new thread.

---

## 1. The core idea (one spectrum, several names)

A single autonomy spectrum that — as you climb it — *simultaneously* means:
- **more autonomy** (the agent decides/acts more on its own)
- **higher maturity** (crawl → walk → run)
- **greater agent complexity** (single-step tool call → multi-step, multi-agent, self-correcting)
- **richer multimodality** (text → voice → documents → actions across systems)
- **the human's role reduces** — AI does more of the heavy lifting (human skill/intent still varies, but net human effort per outcome falls)

Because all of these co-vary, the level is usable as **both a classification scheme** (bucket every agent on it) **and a pricing basis** (higher level ⇒ more compute + interaction + value + assurance).

---

## 2. The 5-level scale — and how it maps to Citi's 3 loops

(SAE-driving-levels–inspired; the Citi framing you had — **human in / on / out of the loop** — is the 3-tier collapse of this.)

| Level | Name | What the AI does | Human's role | Citi loop | Compute / interaction |
|---|---|---|---|---|---|
| **L1** | Assistive / Co-pilot | Answers, drafts, suggests *when asked* | Does the work; AI assists on request | **In the loop** | Low |
| **L2** | Augmented / Recommend | *Proactively* recommends the next action, pre-fills | Reviews & **approves each** action | **In the loop** | Low–Med |
| **L3** | Conditional / Supervised | Executes a task **end-to-end within defined bounds** | Approves before commit / can intervene | **On the loop** | Med–High |
| **L4** | High / Exception-based | Acts autonomously; **escalates only edge cases** | Supervises; handles exceptions | **On the loop → out** | High |
| **L5** | Full autonomy | Sets sub-goals, acts, self-corrects across multi-step / multi-agent | Sets **intent & guardrails only** | **Out of the loop** | Very High |

**Mapping:** in-loop ≈ L1–L2 (approve each) · on-loop ≈ L3–L4 (supervise / exception-only) · out-of-loop ≈ L5.
**Regulated-advice ceiling:** for suitability-bearing advice we deliberately cap below L5 — human-in/on-the-loop is a *governance feature* under FCA Consumer Duty + SM&CR, not a limitation.

---

## 3. The pricing thesis (to develop)

Tie **autonomy level → commercial tier**. Each level up adds, roughly proportionally:
- **Compute** — more model calls, tool use, multi-step reasoning, memory.
- **Interaction / orchestration** — more system touches, longer-running workflows, multi-agent coordination.
- **Value created** — the agent replaces more human effort / drives more outcome.
- **Assurance / governance overhead** — eval, audit, guardrails, monitoring rise with autonomy.

Open pricing questions for the session:
- **Unit of price** — per agent (licensed to a max autonomy level)? per action/run (metered by compute)? per outcome (high levels)? per seat? a hybrid?
- How does **compute** map to level (can we band it)?
- How to **price the assurance/governance** layer (flat platform fee vs per-level premium)?
- How to avoid *penalising the customer* for the platform doing more (value-share vs cost-plus)?
- Does **multimodality** get its own multiplier, or is it baked into the level?

---

## 4. Connections to existing assets (for context in the new session)

- **NBA signal map** (`Engagement/Schroders Group/Output/nba-analysis/Schroders_NBA_Signal_Map.html`) — uses the collapsed Assist/Recommend/Act axis; the 5-level is the fuller scale. Bubbles can be re-plotted on L1–L5.
- **Backbase product language** — `knowledge/domains/backbase-smart-signals.md` (agents: Personalised Outreach, Market Move Explainer, Meeting Prep — place each on the scale).
- **Production-mode reframe** — Connect / Configure / Compose (how a signal is produced) is the *complementary* axis to autonomy (what it does). Pricing may key off **both**.
- **Wealth NBA method** — `knowledge/domains/wealth/next-best-action-method.md`.
- **Pricing tooling in repo** — the `pricing-model` skill / `deal-pricing-system/` (usage-based pricing engine) — candidate home for an autonomy-tiered model.
- **External anchors** — SAE-inspired autonomy levels ([arXiv 2506.12469](https://arxiv.org/pdf/2506.12469)); Anthropic *Building Effective Agents* (workflows vs agents — autonomy of control) ([anthropic.com](https://www.anthropic.com/research/building-effective-agents)); Citi's human in/on/out-of-the-loop.

---

## 5. Agenda for the new session
1. Lock the **5-level definitions + names** (and decide whether to brand the scale).
2. Map **Backbase's current + planned agents** onto L1–L5.
3. Build the **autonomy → pricing model** (compute + interaction + value + assurance).
4. Decide the **governance ceiling** per use-case class (regulated advice vs ops).
5. Fold in the **file you'll attach** + reconcile with `deal-pricing-system`.

---

## 6. Kickoff prompt (paste to start the new session)

> *"New thread on **AI agent autonomy as a classification & pricing framework** — separate from the NBA-signals work. Start from `knowledge/domains/agent-autonomy-pricing-brief.md`. I want to (1) finalise a 5-level autonomy scale (mapped to Citi's human in/on/out-of-the-loop), usable as both an agent-classification and a pricing basis where level co-varies with autonomy/maturity/complexity/multimodality and inversely with human effort; (2) map Backbase's agents onto it; and (3) build an autonomy-tiered pricing model (compute + interaction + value + assurance). I'll attach a file to work from."*
