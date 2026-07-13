# Agent Packaging & Pricing — working thread

**Status:** Internal / 1:1. Active thread on **how to classify, package, and price AI agents.** Pricing & named-source figures internal-only.

This folder is the home for the agent-pricing/packaging workstream and the **landing zone for fresh source content** Shyam drops in periodically (AI / APA / pricing / packaging). Each source: copy the file into `sources/`, write a markdown digest, link it here.

## Contents

| File | What |
|---|---|
| [`../agent-autonomy-framework.md`](../agent-autonomy-framework.md) | **The spine.** Frontline Autonomy Scale (A1–A5) as classification + pricing basis. |
| [`mayur-conversational-cost-model.md`](mayur-conversational-cost-model.md) | Digest of **Mayur's bottom-up Conversational Banking cost model** (built on Deepak's agentic-platform costing). The compute/supply-side truth. |
| [`autonomy-cost-correlation.md`](autonomy-cost-correlation.md) | **Tests Shyam's hypothesis** — does autonomy correlate with cost? (Verdict: yes, but on the per-*outcome* axis, not per-interaction. Validates per-interaction pricing for A1–A3, outcome pricing for A4–A5.) |
| [`cost-anatomy-and-packaging.md`](cost-anatomy-and-packaging.md) | **The synthesis** — runs 28 real agents across the spectrum. Finding: **compute is orthogonal to autonomy** (corr −0.02; driven by data-intensity). ⇒ price autonomy (License + Runtime + Assurance, autonomy-tiered) but **meter compute** (BYO passthrough or Intelligence Credits). 4 building blocks · agentic-runtime flat charge · Factory vs productized SKUs · domain×autonomy grid. |
| `sources/` | Original source files (durable copies — never work from Downloads only). |

## Open threads
1. Extend Mayur's model with A2/A4/A5 use cases + an **interactions-per-outcome** column → turn n=2 into a real proof (see correlation note §4).
2. Build the **agent packaging SKUs** (Assist / Recommend / Transact-Resolve / Autonomous Missions) off the autonomy × assurance-tier grid.
3. Reconcile with the engine in `deal-pricing-system/` (framework §6) and deal-desk pricing figures (banking-os.md §10).

## Related
- Product cost/pricing canon: [`../../product/banking-os.md`](../../product/banking-os.md) §10
- NBA / smart-signals method: [`../wealth/next-best-action-method.md`](../wealth/next-best-action-method.md), [`../backbase-smart-signals.md`](../backbase-smart-signals.md)
- Engine: `deal-pricing-system/` (BIC three-layer model)
