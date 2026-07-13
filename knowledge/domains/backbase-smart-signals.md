# Backbase Smart Signals & Next-Best-Action — Product Language

**Status:** Internal product vocabulary. Use this language when hypothesising/solutioning any NBA, signal, nudge or RM-copilot work. Extends [`knowledge/product/banking-os.md`](../product/banking-os.md) (control plane · Nexus · Sentinel · Relationship Intelligence · Factory/agents).
**Source:** Backbase Wealth product team — **Lennart** (Product Director, Wealth) + **Nano** (R&D) — Schroders NBA working sessions & Lennart's "SCH NBA Internal Analysis" classification, June 2026.
**Handling:** Internal / 1:1. Named agents and the decisioning roadmap are forward-looking — attribute as product direction, not shipped fact, in client materials.

> **Why this exists:** the product team classifies NBAs on a *delivery/engineering* axis (how a signal is detected, typed, surfaced, actioned). We classify on a *value* axis. Speaking their language makes our solutioning product-accurate and lets the two views merge cleanly.

---

## 1. The signal → action chain (the mental model)

Every NBA answers five questions, in order:

1. **What is the signal, and how is it created?** → *Detection mechanism*
2. **What type is it?** → *Notification / Task / Alert / Smart Signal*
3. **Where does it surface?** → *Surface (RM Workspace widget)*
4. **What's the recommended action?** → *Execution: surface-only / create task / launch agent*
5. **How is it prioritised against everything else?** → *Centralized decisioning*

---

## 2. The three signal sources (how an NBA is created) — updated Jun 2026

Lennart's refined model (supersedes the earlier "source-triggered / model-based" wording). Every signal/NBA originates one of three ways, then — unless bypassed — feeds the NBA framework, which ranks & filters per RM.

| Source | Meaning | Example |
|---|---|---|
| **Third-Party Signal** | Created by the bank or a 3rd-party system **outside** Backbase. The bank decides: **bypass triage** (highlight to the RM immediately) or **feed the NBA framework**. | A "hot prospect" flagged in Salesforce → Smart Signal to the RM Workspace, bypassing triage. A redemption model the bank builds → an Alert ingested by Backbase. |
| **Backbase Rule-Based Signal** | Deterministic rule trigger living in the Rule & NBA framework inside Backbase. | Cash balance > X% for Y days → Task for the RM. |
| **Backbase Agentic Signal** | An agentic workflow consumes data + the bank's **context** and outputs a recommended next action. | Cadence breach → Smart Signal + proposed Personalised Outreach. |

All three feed the **NBA framework**, which — configured for the org — **ranks and filters** every NBA/signal per RM (the centralized decisioning/triage, §5). The bank can override at triage or during ingestion (e.g., bypass for must-see signals).

**Read "complexity" correctly.** Lennart's Low/Medium/High = **Backbase-side implementation complexity** (assuming Salesforce + core are integrated) — *not* the bank's model-build effort. A heavy ML use case is **Low** Backbase-complexity if the bank owns the model and sends it as a Third-Party Signal (e.g., **redemption risk**), but **High** if Backbase builds the inference as an Agentic Signal (e.g., **share-of-wallet**). *Who owns the hard build is encoded in the signal source.*

> Maps to our value tiers: **Third-Party** (bank-owned, incl. their ML) · **Rule-Based** (= Rules) · **Agentic** (= Predictive/Generative). Deterministic-first still holds: prefer Rule-Based; reach for Agentic only where inference genuinely adds value.

---

## 3. Signal types — and where they surface

Two widgets in the RM dashboard:

**A. Notification · Task · Alert** — one grouped module ("needs your attention"):
- **Notification** — a **stateful event NOT tied to a condition/threshold** (e.g., birthday). Awareness; lower urgency.
- **Alert** — a **stateful event WITH a threshold/condition**; higher importance & urgency; "cannot ignore." **Compliance "gates" are alerts** — must surface every time.
- **Task** — something that must be **done**; created from a signal/alert, manually or via an agent.

**B. Smart Signals** — a **separate widget**: agentic-driven, strategic, proactive NBA. The growth/retention nudges.

> Type is Backbase's *proposition* but **mappable by the bank** — a Notification can be re-mapped to a mandatory Alert. Signals/Alerts can spawn **Tasks**.

---

## 4. Execution on action (the "next best action")

- **Surface only** — show it; the RM decides.
- **Create Task** — generate a task in the RM portal, optionally linked to a workflow (payments, approval).
- **Launch an Agent** — an agentic workflow performs the action. Named Backbase Wealth agents:
  - **Personalized Outreach** — drafts/sends a personalised client message to open a conversation (retention/growth nudges; hot-lead follow-up).
  - **Market Move Explainer** — generates a client-ready brief around a macro/market event for relevant portfolios.
  - **Meeting Prep / Meeting Preparation** — consolidates client context (allocation, cash, risk, open actions, recent comms) when a meeting is scheduled.

Agents run inside the **RM Portal / RM Workspace**.

---

## 5. Centralized decisioning & prioritisation — the make-or-break

- **The volume problem:** ~200 clients/RM × ~100 signals/client ≈ **~2,000 signals/RM/month.** Without prioritisation it's noise; the entire ROI hinges on signal-to-noise.
- A **centralized decisioning engine inside Backbase** ranks which signals surface. It **must** sit inside Backbase — Backbase emits its own signals too, so routing everything out to an external engine and back floods/defeats the purpose.
- **Today (gap):** limited — you can **override the agentic decisioning** via rules, but there is **no GUI** to define prioritisation yourself (code-based). Lennart's intent: **productise** this (it's a common problem across banks).
- **Prioritisation inputs (Nano):** *ranking dimensions* + *gates* (e.g., compliance events that must always surface).
- **Context management** = the bank-owned **"rule book" / steering context** fed to agentic models (e.g., the definition of an *at-risk* client). Steering with rules/examples reduces hallucination vs a pure "find me at-risk clients" prompt (which "tries to please" and over-flags).

---

## 6. Surfaces & data foundation

- **RM Workspace / RM Portal** — where signals & agents surface to the advisor. *(Phasing is engagement-specific; at Schroders the RM Workspace is Phase 3.)*
- **Nexus schema** — the data foundation / mandatory-field model signals depend on (data-quality blockers reference it). Our **shared client truth (Nexus)**.
- **GenTech fabric** — Backbase's underlying gen-AI infrastructure (~50 R&D FTE building it). The thing a bank would have to **replicate to build this in-house** — the core of the build-vs-buy case.

---

## 7. How this maps to the Banking OS canon

| Smart-Signals term | Banking OS canon |
|---|---|
| Smart Signal (proactive NBA) | **Relationship Intelligence** — Grow / financial progress, surfaced in the unified frontline |
| Personalized Outreach · Market Move Explainer · Meeting Prep | **Factory Missions** — agentic workflows |
| Centralized decisioning + context management | **Orchestration** + **Nexus** (shared truth) + **Sentinel** (governed, gated execution; compliance = mandatory alerts) |
| Detection + fallback (deterministic-first) | Our value tiers: Rules → Enriched → Predictive → Generative |
| GenTech fabric | The control plane you'd otherwise rebuild — the "buy vs build" crux |

---

## 8. Cheat-sheet — solutioning an NBA in product language

For each signal, specify:

**Detection (+ fallback) · Type (Notification / Task / Alert / Smart Signal) · Surface (RM Workspace widget) · Execution (surface-only / create task / agent: ___) · Systems involved · Decisioning/prioritisation need · Governance gate (if compliance).**

Lead with plain English; these are the product-accurate terms to reach for. Pair them with our value-at-stake lens to get the full picture (what to build *and* what it's worth).
