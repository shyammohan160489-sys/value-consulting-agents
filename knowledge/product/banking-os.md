# Backbase Banking OS — Canonical Product Reference

**Version:** 2026.06 · **Status:** CENTRAL / AUTHORITATIVE. This is Backbase's latest product direction. **Every deliverable for every account must align to this** — it is the product substance behind the [narrative spine](../design-system/narrative-spine.md).
**Source:** `source/Banking_OS_Unified_Frontline_May2026.pptx` (architecture) + `source/Banking_OS_Conversational_Banking_June2026.pptx` (solution + pricing). Raw extract: `EXTRACT_raw.txt`.
**Handling:** Pricing and named customer cases are **internal / 1:1 only** — never in public or client-shared assets without approval. "Palantir of Banking" is an analyst quote — attribute, don't claim.

---

## 1. The thesis — operating models, not channels

> "The next decade will not be defined by better channels, but by better operating models."

- **FROM — Frontline Fragmentation** (a losing formula): no shared truth, no shared outcomes. The hidden tax — **6–12 systems per journey · 30–60% manual work · high cost-to-serve · slow cycle times · AI stuck in pilots.**
- **The messy middle:** **~60% of bank work lives in the whitespace *between* systems** — handoffs, exceptions, manual coordination. The highest-value work happens there.
- **TO — the Unified Frontline Operating Model:** humans **and** agents collaborating on one **shared truth** and one operating model.

## 2. Banking OS = the Control Plane

**Banking OS is the control plane of the unified frontline — the system to coordinate and govern the work across your frontline**, between customers, employees, agents and hundreds of downstream systems. Add-on-top, **no rip-and-replace**.

**The layers (primitives) — verb per layer:**
| Layer | Verb | What it is |
|---|---|---|
| **Semantic layer — Nexus** | UNDERSTAND | Shared **source of customer truth**; banking ontology (Palantir-inspired). The system of **truth**, *not* the system of record or a data lake. Links scattered data (core, LMS, CRM, credit) into one real-time truth so customers, employees & agents share context. |
| **Authority layer — Sentinel** | AUTHORIZE | **Governed execution.** Authority (who may decide) · Policies (under which rules) · Entitlements (multi-entity access). Authority spectrum: recommend → approve → execute. Observability + immutable **Auditability**. Humans *and* agents stay within guardrails. |
| **Orchestration layer** | ORCHESTRATE | Coordinates the work across systems and actors. |
| **Connectivity / Integration layer** | INTEGRATE | Connects internal + fintech systems & data. |
| **Intelligence layer** | OPTIMIZE | Reasoning, simulation, continuous improvement. |

## 3. Two execution domains

- **Customer Engagement** — coordinate customer **lifecycle** execution.
- **Banking Operations** (a.k.a. Employee Productivity) — coordinate **front-to-back work** execution.

## 4. The four pre-built Solutions (easy to adopt, easy to customize)

1. **Digital Banking** — modernize the digital foundation → move toward a Unified Frontline. Spans **Retail · SME · Commercial · Wealth**. Empower front-office, delight clients, streamline middle & back office.
2. **Conversational Banking** — a natural-language interface for customers **and** employees. *"From Answering to Acting."* Powered by the **Kasisto** acquisition. **"Just Ask"** embedded in app (chat + voice). Capabilities:
   - **Assist** — answer questions, find info, navigate.
   - **Transact** — complete authenticated routine actions (freeze card, update details, check status).
   - **Resolve** — turn needs into governed resolution loops (disputes, missing payments, complaints, onboarding docs) — links to Customer Operations.
   - **Grow** — surface timely financial-progress moments / next-best-action (not formal advice) — links to Relationship Intelligence.
3. **Relationship Intelligence** — bank-owned AI for financial progress & growth. **Financial Wellness (Grow)** + **Share of Wallet**. Proactive nudges, monitor → guide to next milestone. Delivered as pre-built **Plays** (e.g., Home Ownership Roadmap).
4. **Customer Operations** — close the loop from trigger to resolved outcome. **Resolution Loops:** capture customer intent → coordinate fulfilment across the unified frontline → return the outcome. Card / dispute / payment / KYC / fraud resolution; STP where possible, human handoff where needed.

## 5. Agentic execution model

**Intent → trigger workflows → governed execution → faster resolution & growth.**
Conversational engine flow: **Understand** (identity & verification, intent & entities) → **Orchestrate** (Knowledge & RAG = your SOPs + Banking Intent Library; AI agents & skills; Integration & APIs) → **Assure** (quality, relevance, safety — no hallucinations) → **Resolved** (a governed answer or action). **Generative guardrails** — Security · Risk · Fraud · Compliance = **Sentinel governance at every step, fully auditable.**

> The differentiator: being **in the execution path** captures what no CRM does — the policy exception, the reasoning trace, the monitoring condition, the relationship history.

## 6. Factory & Missions (delivery model)

**Factory** — design → build → deploy a working AI solution in **6–12 weeks**. Tools: Process & Workspace Designer · Semantic Modeler · Agent Builder · Decision & Policy · Connector Studio · Simulation & Testing · Deployment & Ops Control.
- **Mission** = the organization object inside Factory. **Mission Contract** = a declarative, machine-readable definition. **Nexus binding + Sentinel binding.** Agentic SDLC (code/test generation, CI/CD).
- Ethos: **Land fast. Prove value. Expand.** — one use case live in weeks, then light up the next solution line on the same Banking OS.

## 7. GTM Formula

**Ignite (light)** — VC + senior bankers identify high-ROI, risk-free use cases and prioritise one for a **Mission Sprint** → **Proof/Outcome** — SE + FDE specify & prototype (6–12 weeks) → **Land & Expand** on the same platform. Operated by a small Backbase AI Consultants team (~2 FTE).

## 8. Value (three pools)

**$150M–$300M+ annual value unlock** (bank-size dependent):
- **Cost-to-serve ↓ 20–40%** (seamless front-to-back resolution loops)
- **Conversion / cross-sell / retention ↑ 10–25%**
- **AI approval-to-production 3–5× faster**

## 9. Value-Leakage / Customer-Resolution-Loop method (assessment)

Find broken **customer-intent loops** where **time · contact · evidence · ownership** leak across the bank →
1. Capture customer intent → 2. Map resolution leakage → 3. Prioritise the mission (pain × economics × feasibility) → 4. Launch the Customer Resolution Mission (governed by Banking OS) → 5. Prove ROI & scale into a repeatable mission pattern.
Whitespace heatmap by **LOB** (Retail / SME / Commercial / Wealth / Payments) × **ops area** (Onboarding · Servicing · Payments & Disputes · Lending · Loan Origination · Credit · KYC · Financial Crime · Regulatory). *(Close cousin of the internal APA Domain Matrix value-bleed method.)*

## 10. Pricing shape (Conversational Banking reference — INTERNAL)

Simple & predictable: **Platform fee** (Entry €350K · Critical €700K · Enterprise €1.5M) **+ LOB fee** €350K/domain (Retail/SME/Commercial/Wealth; one included; waived on Enterprise) **+ per-interaction** from €0.07 (drops with volume) **+ LLM compute** as transparent pass-through at cost. *"Pay for outcomes, not infrastructure."* — activated **per domain, not per customer/channel**.

## 11. Proof points

120+ customers live · $350M+ revenue · 2,000+ FTEs (700+ R&D / 900 FDE) · 28+ partnerships. Gartner: *"the Palantir of Banking"*, *"light years ahead of traditional banking vendors."* Analyst "customer's favourite" — high trust, flexibility, foundational layers.

## 12. How this MUST cascade into every deliverable

1. **Open on the operating-model thesis + From→To** — fragmented frontline → unified frontline. (Retire "engagement banking" and "better channels" framing.)
2. **Anchor on Banking OS = the control plane**; name **Nexus** (shared truth) and **Sentinel** (governance) where credible.
3. **Map opportunities to the 2 domains + 4 solutions**; Conversational Banking = **Assist / Transact / Resolve / Grow**.
4. **Quantify with the three value pools** and the **value-leakage / resolution-loop** method.
5. **Position delivery as Factory Missions** — land fast (6–12 weeks), prove value, expand.
6. **Shape commercials** on the platform + LOB + per-interaction + compute-pass-through model (usable directly in `/pricing-model`).
7. **Lead with governed, auditable agentic execution** — "AI won't fix fragmentation; without shared truth and guardrails it amplifies it."
