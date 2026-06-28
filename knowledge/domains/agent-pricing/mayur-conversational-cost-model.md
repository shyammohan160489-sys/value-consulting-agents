# Mayur's Conversational Banking Cost Model — digest

**Status:** Internal / 1:1. Durable digest of the source workbook (Mayur, built on Deepak's agentic-platform costing — Deepak owns the infra build). **Pricing & figures internal-only.**
**Source file:** [`sources/Conversational_Banking_Model_Costs_Per_Use_Case.xlsx`](sources/Conversational_Banking_Model_Costs_Per_Use_Case.xlsx) (ingested 2026-06-16).
**Why it matters:** it's the **bottom-up, supply-side** cost truth for agentic conversational banking. Our [autonomy framework](../agent-autonomy-framework.md) is the **demand-side / value-side** packaging. The correlation between the two is tested in [`autonomy-cost-correlation.md`](autonomy-cost-correlation.md).

---

## 1. What it is — a bottom-up cost-to-serve build

It prices a Conversational Banking deal from the **compute up**: decompose each use case into its model calls, cost each call from token prices, scale by interaction volume, discount for reserved throughput, layer platform + team + 3rd-party costs, then check margin against a per-interaction sell price. 8 sheets:

| Sheet | Role |
|---|---|
| **Use Cases** | The unit economics — each use case decomposed into model calls by *purpose* |
| **Models** | Price book — input/output $/1M tokens per model |
| **Simulations** | Scales sessions (600k → 15M) → annual model cost, ± PTU discount |
| **WIP BB Agentic Platform Costs** | Bottom-up platform compute (pods, observability, DB, team) |
| **WIP Simulations Platform** | Platform cost at volume |
| **Margins** | The commercial layer — revenue vs all-in cost → margin |
| Sheet5 / Instructions | empty / how-to |

## 2. The unit of analysis: Interaction (3 per Session)

- **Session = 3 interactions** (assumption). Modelled split: **2 "Chat to my finances" + 1 "Money Movement"** per session.
- An **interaction** = a stack of **model calls**, each tagged with a **Model Purpose**.

### The Model-Purpose taxonomy (the cost atoms)
This is the important structural idea — an interaction is decomposed into functional model calls:
**Reasoning · Embedding · Application Guardrails · Online Evals · Tool Calling · Response Generation.**
Each call: `cost = (input_tok/1M × input_price) + (output_tok/1M × output_price)`, model price looked up from the Models sheet.

## 3. The two modelled use cases (the entire empirical base — n=2)

| Use case | Nature | Model-call stack | Calls/interaction | **Cost/interaction** |
|---|---|---|---|---|
| **Chat to my finances** ("What did I spend on dining?") | Query / read | Reasoning (GPT-4.1, 5k→1k tok) · Embedding (emb-3-small) · Guardrails (4o-mini) · Online Evals (4.1-mini ×2) | **5** | **$0.0370** |
| **Money Movement** ("Transfer $5 to Tom") | Authenticated action | Tool Calling + Response Gen (GPT-4.1, 5.8k→1k tok, ×2) · Guardrails (4o-mini) | **2** | **$0.0395** |

> **The headline finding:** the *action* use case has **fewer model calls (2 vs 5)** but is **~7% more expensive** per interaction — because cost is driven by the **reasoning/tool model tier + token load**, not by the count of (cheap) supporting calls. Per-interaction cost is **roughly flat (~$0.037–0.040)**. This is the crux for the autonomy-pricing hypothesis — see the correlation note.

## 4. Models price book (selected, $/1M tokens)

GPT-4.1 $2/$8 · GPT-4.1-mini $0.4/$1.6 · GPT-4.1-nano $0.1/$0.4 · GPT-4o $2.5/$10 · GPT-4o-mini $0.15/$0.6 · GPT-5.1 $1.06/$8.48 · GPT-5.2 $1.49/$11.47 · o3 $2/$8 · o4-mini $1.1/$4.4 · Claude Sonnet 4 / 3.5 $3/$15 · text-embedding-3-small $0.025 in. (Azure AI Foundry + Anthropic.)

## 5. Scaling & the PTU lever (Simulations)

- Non-discounted model cost: **$0.1136/session** = **$0.0379/interaction**.
- **PTU (Provisioned Throughput Units) reservation → ×0.45 (~55% discount)** on model compute → **$0.0170/interaction**. This is the single biggest cost lever.
- Annual model cost scales linearly: 600k sessions → $0.82M; 5M → $6.81M; 15M → $20.4M (pre-PTU).

## 6. Platform compute (WIP BB Agentic Platform Costs) — bottom-up

- **Per-agent DTAP base = $326.67/agent/mo** — 7 pods just to "exist" (1 Dev + 2 Test/Stg + 3 Prod-AZ + 1 DR) × $46.67/pod. *Fixed per agent regardless of traffic.*
- **Usage compute** = autoscaling $0.006/1k requests (3 replicas across AZs).
- **Observability — Langfuse: 7 LF units per interaction**, usage-tiered (~$0.08/1k units). *Scales with interactions.*
- Fixed: base platform (AKS/APIM/KeyVault) $4k · Grafana $500 · Langfuse base $2,799 · Postgres HA $750 · Redis $320.
- **Platform team $10k/mo** ("~10 clients to break even"; 100% agentic team ~€800k + 30% of GC team).
- **Total ≈ $21.4k/mo ≈ $257k/yr** (at the 5M-session config).

## 7. The commercial layer (Margins)

**Revenue = Platform fee + per-interaction + per-session:**
`Rev = $1,000,000 + ($0.07 × 3 × sessions × 12) + ($0.05 × sessions × 12)`
- Note the **dual meter**: $0.07/interaction **and** $0.05/session, on top of a $1M platform fee. ($0.07 matches the canonical banking-os.md §10 per-interaction figure.)

**All-in cost** = PTU-discounted model compute + Agentic Platform Compute & Team + **Kasisto** (the conversational engine, from the acquisition) + Other Solutions.

| Scale | Revenue | Margin |
|---|---|---|
| 600k sessions / 1.8M interactions | $2.87M | **57.6%** |
| 5M sessions / 15M interactions | $16.6M | **75.5%** |

Margin expands with scale as the $1M platform + Kasisto + team costs amortise over volume.

## 8. What's WIP / to confirm with Mayur

- Only **2 use cases** modelled → thin base for any cost-by-category claim (see correlation note).
- Platform cost sheets marked **WIP**; per-agent base vs shared-MS assumption ("more microservices running fewer agents → same cost structure") is a stated *working thesis*, not settled.
- Kasisto / Other-Solutions cost lines are flat allocations, not built up.
- $0.05/session fee rationale not documented.
