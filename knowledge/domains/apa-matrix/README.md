# APA Domain Matrix V3 — Agentic Process Automation Catalog

> **The default lens for prescribing AI / agentic use cases across any banking opportunity — all four lines of business, one operating model.**
> Local copy of Shobhit's APA Simulation Catalog (V3) so engagements tap a source we own — not the Netlify build.

**Source:** Reproduced from Shobhit's *APA Domain Matrix V3 — Two-Loop Operating Model* (`domainmatrixtoolkitv2.netlify.app`, Backbase internal, password-gated). Credit to Shobhit for the framework and simulations.
**Reproduced:** 13 Jul 2026, for Shyam.
**Supersedes:** v1.1 (29 Mar 2026), which used a 4-super-domain / 9-domain taxonomy. That version is preserved under `_archive_v1.1/`.
**Files:** `apa_v3.json` (machine-readable backbone — 65 processes, 283 steps, full 6-layer detail, canon-labelled) · `apa_domain_matrix_v3.html` (self-contained interactive copy, 9.2 MB) · this guide.

---

## ⭐ Terminology — canon first, verbs second

V3 organises everything into **two loops**. These map **1:1 to the Backbase go-to-market canon** (mid-year leadership deck, slide 259). **Always lead with the canon labels; the V3 verbs are a secondary skin.**

| Present this (Backbase canon — official GTM) | V3's own label (secondary skin) | What it is |
|---|---|---|
| **Customer Operations** | "Customer Resolution Loops" | Customer-**initiated** journeys closed end-to-end. High customer touch. SLA = customer patience (hours/days). Value bleed weighted to **Growth + Efficiency**. |
| **Bank Operations** | "Banking Operations" | Bank-**initiated** cadence work the customer never sees. Low customer touch. SLA = regulator / risk (regulatory cycles). Value bleed weighted to **Efficiency + Control**. |

> In any client-facing material use **Customer Operations / Bank Operations** — that is the sanctioned company story (`knowledge/product/banking-os.md`, where Customer Operations is also one of the four monetizable solutions). "Resolution Loops" is the mechanic *inside* Customer Operations, not a third domain name. The V3 verbs (Acquire, Maintain, …) are a useful shorthand for facilitation but are not the front-and-centre vocabulary.

---

## When to use this (standing instruction)

**Any time a task involves identifying, prescribing, prioritising, or sizing AI / agentic use cases for a bank — tap this module first.** Default lens for: agentic strategy notes, POC scoping, use-case portfolios, opportunity shaping, ROI hypothesis on automation, and "where can AI help?" conversations. Flex to the LOB(s) in play — Retail / SME / Commercial / Wealth & Private, or a blend.

Workflow:
1. **Identify the LOB(s)** in play (e.g. a building society = Retail + SME).
2. **Read the L1 matrix** (below) → which domains carry the highest automation potential for those LOBs.
3. **Pull the processes** in those HIGH cells from `apa_v3.json` → these are your candidate use cases.
4. **Apply the per-process method** (Value Bleed → Banking OS Simulation → Elastic Ops Business Case) to prove desirability → feasibility → viability.
5. **Re-base every $/% figure on the client's data** before anything client-facing. The toolkit numbers are illustrative reference values.

---

## The framework

**Thesis — Elastic Operations:** scale operations *without* linear headcount growth; elastic capacity delivered through **humans + agents + workflows**. Three pillars: **Growth** (acquire · retain · expand) · **Efficiency** (higher throughput · lower cost-to-serve) · **Control** (authority · policy · proof).

### The 12 domains (Two-Loop Operating Model)

**Customer Operations** (8 domains — customer-initiated, high touch):

| Canon domain | V3 verb |
|---|---|
| Onboarding & Activation | Acquire |
| Account & Profile Servicing | Maintain |
| Payments & Money Movement | Move |
| Disputes & Resolution | Resolve |
| Loan / Credit Origination | Borrow |
| Credit Servicing & Restructuring | Service credit |
| Specialist & Advisory | High-touch |
| KYC Periodic Review | Refresh |

**Bank Operations** (4 domains — bank-initiated, low touch):

| Canon domain | V3 verb |
|---|---|
| Financial Crime Surveillance | Surveil |
| Credit Portfolio Surveillance | Monitor |
| Regulatory Reporting & Audit | Report |
| Operational Controls & Recon | Reconcile |

### The 6-layer Banking OS (each process simulation walks these top-to-bottom)

| Layer | Role | Product reality |
|---|---|---|
| **Interaction** | Unified Frontline — composable workspaces, branch, mobile, contact centre | Unified Frontline |
| **Orchestration** | The agents that plan & execute multi-step tasks | Agent Studio + Agent Orchestration |
| **Intelligence** | ML — intent, propensity, outcome prediction, risk scoring | Intelligence Fabric |
| **Sentinel** | Authority Layer — decides what each actor (customer/employee/AI agent) may do; every action checked against bank policy before it executes; immutable audit | **Sentinel** |
| **Semantic (NEXUS)** | Customer State Graph — one real-time customer view + Banking Ontology | NEXUS |
| **Connectivity** | Integration to systems of record | Grand Central (iPaaS) |

> Sentinel, NEXUS and the Intelligence Fabric are official Backbase product names (AI-Native Banking OS, launched at Backbase ENGAGE, 22 Apr 2026).

### Decision Token (the governance artefact) — new in V3

Every agent action emits a **Decision Token**: *policy applied · actor identity · model version · outcome · full context.* This is the concrete artefact behind the Sentinel / Control story — regulator-scrutable, board-trustable. Use it whenever you need to make "governed, auditable, compliant" tangible rather than a slogan.

### The three agentic tiers — don't call everything "agentic"

- **Assisted (copilot):** AI drafts, human decides.
- **Automated (workflow/STP):** deterministic, rules-based. No reasoning (Flow).
- **Agentic (autonomous):** agent reasons over NEXUS, plans & executes across systems inside Sentinel guardrails; human at the risk gate only. *Spend the word only where autonomy earns its keep — high-volume, context-heavy, judgment-light work.*

### Per-process method — the desirability/viability engine

| Artefact | Proves | What it is |
|---|---|---|
| **Value Bleed Analysis** | Desirability | Quantified $ bleed per process step + narrative — the pain, sized |
| **Banking OS Process Simulation** | Feasibility | 6-layer walk-through of the agentic future state |
| **Elastic Operations Business Case** | Viability | Growth Restored · Efficiency Gained · Control Enforced, with recovery math |

---

## Coverage

- **4 Lines of Business:** Retail · SME · Commercial · Wealth & Private
- **2 execution halves / 12 domains** (8 Customer Operations + 4 Bank Operations, above)
- **65 process simulations · 283 steps**, each with the full 6-layer agentic walk-through in `apa_v3.json`.

### L1 Automation-Potential Matrix

Automation potential per LOB × domain. **HIGH** = strong agentic fit · **MED** = partial · **LOW** = mostly automated / low-leverage. Columns are canon domains (V3 verb in parentheses).

| LOB | Onboard (Acquire) | Servicing (Maintain) | Payments (Move) | Disputes (Resolve) | Origination (Borrow) | Credit svc (Service) | Advisory (High-touch) | KYC review (Refresh) | Fin-crime (Surveil) | Credit port (Monitor) | Reg report (Report) | Controls (Reconcile) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **Retail** | MED | HIGH | LOW | HIGH | HIGH | HIGH | MED | MED | HIGH | MED | MED | MED |
| **SME** | HIGH | MED | MED | HIGH | HIGH | MED | HIGH | HIGH | MED | HIGH | MED | LOW |
| **Commercial** | HIGH | MED | HIGH | MED | HIGH | MED | HIGH | HIGH | HIGH | HIGH | HIGH | HIGH |
| **Wealth & Private** | HIGH | MED | MED | LOW | MED | MED | HIGH | HIGH | HIGH | MED | HIGH | MED |

**How to read it for an opportunity:** take the client's LOB row(s), pick the HIGH cells, then pull those processes from `apa_v3.json` as your priority use-case shortlist. *(First 8 columns = Customer Operations; last 4 = Bank Operations.)*

### Process index by LOB

A process can span more than one domain cell (one simulation covers several use cases). The label below is its **highest-leverage** placement; full placements are in each process's `placements[]` in the JSON.

**Retail (16)** — Retail Account Opening · Document Upload & Validation · Account Servicing · Payments & Cash Management · Consumer Loan Origination · Appraisal & Collateral Valuation · Loan Servicing & Restructuring · Limit Changes & Overrides · Fee Adjustments & Waivers · Disputes & Chargebacks · KYC & Due Diligence · Financial Crime & Fraud · Mule Account Detection · Credit Risk & Decisioning · Regulatory & Compliance · Audit Trail & Evidence Management

**SME (15)** — Document Collection & Review · KYC & Due Diligence · KYC Risk Assessment & Scoring · Multi-Signatory Setup & Mandates · Account Setup & Product Bundling · Day-to-Day Servicing · Payments & Cash Management · AP/AR & Expense Management · Lending & Credit · Credit Risk & Decisioning · Collections & Recovery · Transaction Disputes · Financial Crime & Fraud · Regulatory & Compliance · Audit Prep & Evidence Management

**Commercial (14)** — Entity Onboarding · Multi-Product Onboarding · Compliance & Enhanced Due Diligence · KYC & Due Diligence · Account Config & Fulfillment · Account Servicing · Treasury & Cash Management · Lending & Credit · Syndication & Participation Management · Trade Finance · Disputes & Chargebacks · Credit Risk & Decisioning · Financial Crime & Fraud · Regulatory & Compliance

**Wealth & Private (20)** — Client Onboarding · Suitability & Risk Profiling · Tax Residency & CRS Classification · Intergenerational Wealth Transfer · Client Servicing & Lifecycle · 3rd Party Access Management · Beneficiary & Estate Processing · ACAT & Account Transfers · Payments & Cash Management · Investment Proposal Creation · Corporate Actions Processing · Lending & Credit · Margin Call Processing · KYC & Due Diligence · PEP / Sanctions / Adverse Media Monitoring · Financial Crime & Fraud · Credit Risk & Decisioning · FATCA / CRS Reporting · Regulatory & Compliance

> Wealth is **integrated here, not siloed.** For the wealth-specific cut (mapped to these same canon domains, with client-play notes), see `knowledge/domains/wealth/apa-processes.md`.

---

## Using the data

`apa_v3.json` structure:
```
meta            — source, attribution, canon alignment, supersedes note
framework       — thesis, pillars, operating_model (Customer Ops / Bank Ops),
                  domains12, layers6, method3, tiers3, decision_token
lines_of_business
l1_matrix       — loops, labels, matrix{LOB → [{level, note}]}
processes{slug} — title, lob, primary_half, primary_verb, primary_domain,
                  placements[] (every domain cell this process fills),
                  num_steps, steps[]
   steps[]      — name, timeline, timeNote, customer, customerLabel,
                  agent/agentDesc, intel/intelDesc, sentinel/sentinelDesc
                  (bulleted authority policy + $ thresholds + audit token),
                  nexus/nexusShort/nexusAttrs, metric, recoveryLabel
```
Each `steps[]` entry is one stage of the agentic process, mapped to the 6 layers. Richer than v1.1: adds `customerLabel`, `timeNote`, bulleted `sentinelDesc` policy detail with dollar thresholds and audit tokens, `nexusShort`, `nexusAttrs`, `recoveryLabel`.

For visual / interactive browsing (Value Bleed slides, UI prototypes, animated business case), open `apa_domain_matrix_v3.html` locally.

---

## Maintenance

Point-in-time copy of V3 (13 Jul 2026). If Shobhit ships updates, **re-pull and diff — don't silently overwrite.** The prior v1.1 lives in `_archive_v1.1/`. To formalise as an auto-triggered skill/hook (so it fires on every AI-use-case task without relying on memory), an Architect (Mayur / Shobhit / Mariam) needs to add it under `.claude/`.
