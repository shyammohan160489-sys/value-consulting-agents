# Backbase AI Pricing Playbook

**Internal — Confidential**
**Version:** 1.0 | **Last Updated:** March 2026

---

## 1. Pillar Selection Guide

The Backbase AI pricing framework has three pillars. Most deals involve 1-2 pillars; large platform deals may involve all three.

### Decision Tree

```
What is the primary AI use case?

├─ AI features in the banking app (recommendations, alerts, search)
│  → Pillar 1: Embedded AI — Signature Tier + token pass-through
│  → Buyer: CDO / CTO
│
├─ Chat-based employee assist or customer self-service
│  → Pillar 2: Conversational Engine — Base fee + per-interaction
│  → Buyer: CDO / COO
│
├─ Automating manual processes (onboarding, KYC, disputes, FinCrime)
│  → Pillar 3: Process Automation — Per-execution / per-outcome
│  → Buyer: COO / CTO
│
└─ Bank wants to build custom AI agents
   → BYO Platform — Platform fee + deployment + tokens
   → Buyer: CTO
```

### When to Combine Pillars

- **Wealth management:** Pillar 1 (Embedded) + Pillar 3 (Process Automation) — advisors get AI in their workspace, compliance processes get automated. This is the Schroders pattern.
- **Retail banking:** Pillar 1 (Embedded) + Pillar 2 (Conversational) — app gets smart features, customers get a chatbot, employees get an assistant.
- **Commercial banking:** Pillar 2 (Conversational) + Pillar 3 (Process Automation) — RMs get an assistant, trade finance and KYB get automated.

---

## 2. Deal Size Reference Pricing

All pricing below uses the **BIC model (Intelligence Fabric)** and assumes the full domain agent catalog is activated. Actual deals may activate a subset.

### Small Bank (50 users)

| Domain | Platform ($) | Per User/Mo | Compute ($) | BIY ($) | Ratio |
|--------|-------------|-------------|-------------|---------|-------|
| Retail | ~$290K | ~$480 | ~$660 | ~$3.0M | 440x |
| Wealth | ~$408K | ~$680 | ~$940 | ~$3.4M | 434x |
| Commercial | ~$298K | ~$497 | ~$630 | ~$3.0M | 473x |

**Guidance:** At 50 users, per-user cost is high due to fixed domain base. Recommend Entry tier ($250K base). AI adoption is a strategic bet — position as "platform for growth" not "cost per user."

### Mid-Market (500 users)

| Domain | Platform ($) | Per User/Mo | Compute ($) | BIY ($) | Ratio |
|--------|-------------|-------------|-------------|---------|-------|
| Retail | ~$310K | ~$52 | ~$6.5K | ~$3.0M | 48x |
| Wealth | ~$570K | ~$95 | ~$9.4K | ~$3.4M | 61x |
| Commercial | ~$420K | ~$70 | ~$7.0K | ~$3.0M | 60x |

**Guidance:** Sweet spot for BIC model. Per-user cost is competitive with Microsoft Copilot ($30/mo) to ServiceNow ($75-125/mo). Emphasise domain specialisation vs generic copilots.

### Tier 1 Bank (5,000 users)

| Domain | Platform ($) | Per User/Mo | Compute ($) | BIY ($) | Ratio |
|--------|-------------|-------------|-------------|---------|-------|
| Retail | ~$557K | ~$9 | ~$18K | ~$3.0M | 30x |
| Wealth | ~$1.9M | ~$32 | ~$94K | ~$3.4M | 20x |
| Commercial | ~$1.1M | ~$19 | ~$63K | ~$3.0M | 16x |

**Guidance:** At scale, BIC block costs dominate. Apply volume discounts (10-20% on BIC blocks for >1M BICs). Platform:Compute ratio drops to 16-30x — still healthy, but the BIY comparison narrows. Lead with **time-to-value** narrative, not cost arbitrage.

---

## 3. Domain Positioning

### Retail Banking
- **Agent profile:** High volume, low complexity (BIC weights 0.2-2.5)
- **Typical mix:** 8-10 agents — smart recommendations, proactive alerts, conversational banking, onboarding automation, dispute triage
- **Value narrative:** Call deflection savings, digital adoption increase, onboarding speed
- **Pricing sweet spot:** $250-550K/yr platform | $9-50/user/month

### Wealth Management
- **Agent profile:** Low volume, high complexity (BIC weights 0.7-5.2)
- **Typical mix:** 8-10 agents — review prep, NBA, meeting summarisation, portfolio commentary, compliance
- **Value narrative:** Advisor productivity (hours recovered), AUM retention (attrition reduction), compliance automation
- **Pricing sweet spot:** $400K-1.9M/yr platform | $32-175/user/month
- **Reference deal:** Schroders — 225 advisors, 10 agents, ~£373K/yr (standard tier)

### Commercial Banking
- **Agent profile:** Medium volume, medium-high complexity (BIC weights 1.5-4.5)
- **Typical mix:** 6-8 agents — RM briefing, credit memo drafting, KYB, trade finance, covenant monitoring
- **Value narrative:** RM prep time reduction, KYB processing speed, trade finance automation
- **Pricing sweet spot:** $300K-1.1M/yr platform | $19-125/user/month

---

## 4. BIC vs Per-Interaction vs Per-Execution

### When to Use BIC Model (Recommended Default)

- Deals with Embedded AI (Pillar 1) + Process Automation (Pillar 3)
- Wealth and commercial deals where agents are complex and varied
- When the client wants budget predictability (pre-purchased blocks)
- When you need the three-layer transparency story (raw compute → platform → BIY)

### When to Use Per-Interaction (Pillar 2 Only)

- Conversational Banking or Employee Workspace as standalone products
- When the buyer thinks in "cost per contact" or "cost per conversation"
- Retail deals with high-volume, low-complexity conversational use cases
- When the client explicitly prefers usage-aligned pricing

### When to Use Per-Execution (Pillar 3 Standalone)

- Process automation sold separately from the platform
- When the buyer has clear FTE replacement targets (onboarding, KYC)
- When the value case is "this agent replaces X FTEs at Y% of the cost"
- Start per-execution, slide into per-outcome as baselines are established

### Hybrid Approaches

For large deals combining multiple pillars:
- **Embedded + Process:** BIC model covers both (one IF Domain + BIC blocks)
- **Embedded + Conversational:** BIC for embedded, per-interaction for conversational engine (separate line items)
- **All three:** BIC for embedded + process, per-interaction for conversational, BYO platform fee if applicable

---

## 5. Negotiation Levers

### Concession Levers (ordered by preference — give the cheapest first)

| Lever | Impact | When to Use |
|-------|--------|-------------|
| **BIC block size** | Offer larger blocks at lower per-BIC rate | Client pushes on variable cost |
| **Compute markup** | Reduce from 15% to 10% or even cost pass-through | Client has procurement doing LLM cost benchmarking |
| **Agent phasing** | Start with 3-5 agents, add more over time | Client nervous about commitment size |
| **Volume commitment** | 10-20% discount for 2+ year BIC commitment | Client wants multi-year predictability |
| **Sandbox allowance** | Increase included sandbox tokens | Client wants to experiment first |
| **Domain tier** | Entry instead of Standard (saves $100K/yr) | Small deals where enterprise SLA not needed |
| **AI activation year** | Push AI to Year 2 (ramp the license) | Client wants lower Year 1 cost |

### Red Lines (Never Concede)

- **Three-layer transparency** — Always show raw compute vs platform vs BIY. This is our value justification.
- **Model-agnostic positioning** — Never lock the client to a specific LLM. The orchestration layer is the value.
- **Minimum IF Domain Base** — Do not go below Entry tier ($250K). The domain base covers Agent Factory, gateway, orchestration, guardrails.
- **Compute markup below 10%** — Below this, we lose money on infrastructure.

### Discount Framework

| Component | Max Discount | Approval Level |
|-----------|-------------|----------------|
| IF Domain Base | 15% | VP Sales |
| BIC Blocks | 20% | VP Sales |
| Compute Markup | Reduce to 10% | Deal Desk |
| Conversational Base Fee | 15% | VP Sales |
| Per-Interaction Rate | 25% | Deal Desk |
| BYO Platform Fee | 10% | VP Sales |

---

## 6. Competitive Positioning

### vs "We'll just use Azure OpenAI / AWS Bedrock directly"

**Response:** "You absolutely can. Raw LLM inference will cost you ~$5-15K/year. What it won't give you is:
- Banking-specific prompt engineering and guardrails
- Model routing that optimises cost vs quality per request
- Agent orchestration with your core banking, CRM, and data warehouse
- PII filtering, audit logging, and compliance controls
- Pre-built agents that work out of the box
- Agent Factory to build your own agents with guardrails baked in

Building that layer yourself costs ~$2-3M/year in engineering. We charge $300-500K. That's 80-85% cheaper than DIY, with a 6-month head start."

### vs Microsoft Copilot ($30/user/month)

**Response:** "Copilot is a horizontal productivity tool — great for emails and documents. We're a vertical banking AI platform:
- Our agents understand KYC, suitability, regulatory compliance
- We integrate with core banking systems, not just Office 365
- Our pricing scales with banking value delivered, not seats purchased
- At 500+ users, our per-user cost is competitive ($30-50/mo) with far deeper capability"

### vs "Your margin over raw compute is too high"

**Response:** "You're right — our platform costs 20-100x more than raw tokens. Here's what that covers:
1. **Agent Factory** — build, test, deploy agents without ML engineers
2. **Model routing** — automatically picks the cheapest model that's good enough per request
3. **Banking guardrails** — PII filtering, compliance logging, regulatory controls
4. **Orchestration** — connects AI to your T24/Temenos/Finastra, CRM, data warehouse
5. **Pre-built agents** — 8-10 banking-specific agents ready to deploy

The alternative is building this yourself at ~$2-3M/year. Our margin is the arbitrage between your build cost and our platform cost."

---

## 7. Objection Handling

### "What if we want to switch AI models?"

"The platform is model-agnostic. Today it routes to GPT-4o, Claude Sonnet, and Gemini Pro — picking the best model per request. If a new model launches tomorrow that's cheaper or better, we add it to the routing layer. You don't need to change anything. Your agents keep running, your costs go down. That's the whole point of the orchestration layer."

### "Why can't we just buy BIC blocks without the Domain Base?"

"The Domain Base covers the infrastructure that makes BICs valuable: Agent Factory (build agents), AI Gateway (route and secure requests), orchestration (connect to your systems), guardrails (compliance, PII), and telemetry (monitor and audit). Without it, BIC blocks are just tokens — you'd need to build the platform yourself. The Domain Base IS the product; BICs are the fuel."

### "We have our own data science team — we don't need pre-built agents"

"That's great — and exactly why we offer Agent Factory. Your team can build custom agents using our platform, with banking guardrails, model routing, and deployment infrastructure already handled. The pre-built agents are a head start; Agent Factory is the long game. Most clients start with 3-5 pre-built agents to prove value, then use Agent Factory to build domain-specific agents their team designs."

### "The per-user cost is too high for a small deployment"

"You're right — at 50 users, the per-user cost is $400-700/month. That's because the platform has a fixed cost floor (Domain Base + minimum BIC block). The economics flip at 200+ users: per-user cost drops to $50-100/month, competitive with generic copilots but with domain-specific value. Two options: (1) start with Entry tier and fewer agents to reduce the floor, or (2) commit to a growth trajectory that gets you to the sweet spot."

---

## 8. Quick Reference Card

### The Three-Layer Pitch (30 seconds)

> "Every AI pricing conversation has three numbers:
> 1. **Raw compute** — what the AI models cost to run. For you, that's about $X/year.
> 2. **Our platform** — that same AI, wrapped in banking guardrails, agent orchestration, and pre-built agents. That's $Y/year.
> 3. **Build-it-yourself** — what it would cost you to build the same thing internally. That's $Z/year.
>
> We're 80% cheaper than building it yourself, and you're live in months, not years."

### Key Metrics to Quote

| Metric | Range |
|--------|-------|
| Per-user/month (500 users) | $30-95 depending on domain |
| Platform:Compute ratio | 15-100x (higher at small scale) |
| Time to first agent | 4-6 weeks (productised) |
| Time to custom agent | 8-12 weeks (Agent Factory) |
| BIY cost comparison | 80-90% cheaper via platform |
| LLM cost trend | Declining 30-50% annually |
