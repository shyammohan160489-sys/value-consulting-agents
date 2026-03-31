# Intelligence Fabric AI Pricing — Client Rationale Template

**Instructions:** This template produces the AI pricing appendix for client proposals. Fill in the `{{placeholders}}` with engagement-specific data. The three-layer pricing transparency section is mandatory. Use the AI pricing engine (`compute_ai_pricing()`) to generate the numbers, then populate this template.

---

## Appendix: Intelligence Fabric — AI Pricing

### How Intelligence Fabric Is Priced

Intelligence Fabric uses **Backbase Intelligence Credits (BICs)** — a normalised unit of AI work. Each agent action has a defined BIC weight based on its complexity:

| BIC Weight | Action Type | Example |
|------------|-------------|---------|
| 0.1 | Deterministic workflow step | Rule-based routing, status update |
| 0.5 | Agent reasoning + tool call | NBA calculation, compliance check |
| 1.0 | Standard agent action | Document processing, summarisation |
| 2.0-3.0 | Multi-step agent reasoning | Credit assessment, review briefing |
| 5.0 | Complex orchestrated workflow | Meeting summarisation, periodic review |

### Your Agent Portfolio

| # | Agent | What It Does | BIC Weight | Monthly Actions | Annual BICs | Phase |
|---|-------|-------------|------------|-----------------|-------------|-------|
| 1 | {{agent_1_name}} | {{agent_1_description}} | {{agent_1_bic}} | {{agent_1_volume}} | {{agent_1_annual_bics}} | {{phase}} |
| 2 | {{agent_2_name}} | {{agent_2_description}} | {{agent_2_bic}} | {{agent_2_volume}} | {{agent_2_annual_bics}} | {{phase}} |
| 3 | {{agent_3_name}} | {{agent_3_description}} | {{agent_3_bic}} | {{agent_3_volume}} | {{agent_3_annual_bics}} | {{phase}} |
| ... | ... | ... | ... | ... | ... | ... |
| | **Total** | | | | **{{total_annual_bics}}** | |

*Volume estimates based on {{user_count}} {{user_type}} × average monthly usage per user.*

### Intelligence Fabric Pricing Composition

| Component | {{phase_2_label}} | {{phase_3_label}} |
|-----------|-------------------|-------------------|
| IF Domain Base (Agent Factory, AI gateway, orchestration, guardrails) | {{domain_base}} | {{domain_base}} |
| BIC Blocks (productised agents) | {{bic_blocks_p2}} ({{blocks_count_p2}} blocks) | {{bic_blocks_p3}} ({{blocks_count_p3}} blocks) |
| Compute pass-through (LLM at cost + 15%) | {{compute_p2}} | {{compute_p3}} |
| Custom agent BIC allocation | — | {{custom_bic_p3}} |
| **Total Intelligence Fabric** | **{{total_if_p2}}** | **{{total_if_p3}}** |

### Three-Layer Pricing Transparency

Every AI investment has three numbers. This is what yours looks like:

| Layer | What It Represents | Annual Cost |
|-------|-------------------|-------------|
| **Raw LLM Compute** | What the AI models actually cost to run | {{raw_compute}}/yr |
| **Backbase Intelligence Fabric** | Domain base + BIC blocks + compute pass-through (what Backbase charges) | {{platform_price}}/yr |
| **Build-It-Yourself** | What it would cost {{client_name}} to build {{agent_count}} agents internally | {{biy_cost}}/yr |

**What the gap covers:**
- **Agent Factory** — low-code/pro-code builder for custom agents
- **AI Gateway** — model routing, prompt management, safety guardrails
- **Banking Orchestration** — pre-built connectors to {{core_system}}, {{crm}}, and your data warehouse
- **Compliance Controls** — PII filtering, audit logging, regulatory guardrails
- **Observability** — real-time usage dashboard, cost attribution, performance monitoring

### Model Lock-In Protection

{{client_stakeholder}} raised an important concern: the risk of AI vendor lock-in. The BIC model addresses this directly:

- **No per-query charges** — consumption trap avoided
- **No hidden overage fees** — transparent rate card (cost + 15%)
- **No single vendor lock-in** — orchestration layer connects to GPT, Claude, Gemini, or {{client_name}}'s own models
- **Model switching** — configuration change, not procurement event
- **Cost trajectory** — as LLM costs decline (30-50% annually), {{client_name}} benefits automatically — the same BIC allocation buys more compute each year
- **Full visibility** — real-time dashboard shows queries, tokens, model distribution, and cost per agent

### Phased Agent Activation

Agents activate when their dependent modules go live:

| Phase | Agents | Dependent Module | BICs/yr |
|-------|--------|-----------------|---------|
| {{phase_2_label}} | {{phase_2_agents}} | {{phase_2_modules}} | {{phase_2_bics}} |
| {{phase_3_label}} | {{phase_3_agents}} | {{phase_3_modules}} | {{phase_3_bics}} |

### Custom Agent Economics ({{custom_phase_label}})

| Component | What's Included | Pricing |
|-----------|----------------|---------|
| Agent Factory | Low-code/pro-code builder, AI gateway, sandbox | Included in IF domain base |
| Sandbox BICs | {{sandbox_bics}}/month for development and testing | Included in IF |
| Production agents | Custom agents consume BICs from allocated blocks | Existing block allocation |
| Additional BIC blocks | When total consumption exceeds allocation | {{additional_block_price}} per 250K block |

### The Risk of Fragmented AI

| Risk | Data Point | Source |
|------|-----------|--------|
| AI budget waste | 31% of AI budgets wasted on redundant subscriptions | Zapier 2025 |
| POC failure rate | 88% of AI proofs-of-concept never reach production | IDC 2025 |
| Governance gap | 3.4x higher AI effectiveness with unified governance | Gartner 2025 |
| Shadow AI liability | $670K additional cost per data breach involving shadow AI | IBM 2025 |

---

*Template version 1.0 — March 2026. Generate numbers using `compute_ai_pricing()` from the deal-pricing-system.*
