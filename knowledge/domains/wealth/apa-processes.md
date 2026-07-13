# Wealth & Private — APA Process Catalog (V3, canon-aligned)

> The Wealth & Private cut of the **APA Domain Matrix V3**, mapped to the Backbase go-to-market canon (**Customer Operations / Bank Operations**, mid-year slide 259). Wealth is **integrated into** the master matrix, not siloed — this file is the wealth lens onto it.
>
> **Master module:** [`knowledge/domains/apa-matrix/`](../apa-matrix/README.md) — `apa_v3.json` (full 6-layer step detail, all 4 LOBs) · `apa_domain_matrix_v3.html` (interactive).
> **Terminology rule:** lead with **Customer Operations / Bank Operations** (canon). V3's verbs (Acquire, Maintain, …) are a secondary facilitation skin. See [[reference_apa_domain_matrix_v3]].
> **Source:** Shobhit's APA Domain Matrix V3 (Backbase internal). Reproduced 13 Jul 2026. Numbers are illustrative reference values — **re-base on the client's data before anything client-facing.**

---

## Why wealth is different (read before pitching)

In wealth, the value bleed sits in **Customer Operations onboarding/advisory** and **Bank Operations compliance** — *not* in payments or disputes. The L1 row proves it: **Resolve/Disputes = LOW** (advisor-mediated), **Payments/Move = MED** (custody, not retail rails). Lead a wealth story with the **HIGH** cells:

- **Acquire (Onboarding & Activation) = HIGH** — suitability, source-of-wealth, 30–60 day cycles.
- **High-touch (Specialist & Advisory) = HIGH** — proposals, rebalancing.
- **Refresh (KYC Periodic Review) = HIGH** — UHNW source-of-wealth re-verification.
- **Surveil (Financial Crime Surveillance) = HIGH** — cross-border layering.
- **Report (Regulatory Reporting & Audit) = HIGH** — suitability evidence, FATCA/CRS.

> This is the objective steer for any wealth deck (SEB, Pictet, Schroders, Evelyn) — and the correction to the Jules "APA for Wealth" draft, which led with disputes/payments (LOW/MED for wealth).

---

## Wealth L1 row (automation potential)

| Domain (canon) | Verb | Level | Where the bleed is |
|---|---|---|---|
| Onboarding & Activation | Acquire | **HIGH** | Suitability · 30-60 days |
| Account & Profile Servicing | Maintain | MED | 3rd party · ACATs |
| Payments & Money Movement | Move | MED | Custody · settlement |
| Disputes & Resolution | Resolve | LOW | Advisor-mediated |
| Loan / Credit Origination | Borrow | MED | SBL / Lombard · mortgage |
| Credit Servicing & Restructuring | Service credit | MED | Margin calls · collateral |
| Specialist & Advisory | High-touch | **HIGH** | Proposals · rebalance |
| KYC Periodic Review | Refresh | **HIGH** | UHNW source-of-wealth |
| Financial Crime Surveillance | Surveil | **HIGH** | Cross-border layering |
| Credit Portfolio Surveillance | Monitor | MED | Collateral re-valuation |
| Regulatory Reporting & Audit | Report | **HIGH** | Suitability evidence |
| Operational Controls & Recon | Reconcile | MED | Corp actions ops control |

*First 8 = Customer Operations · last 4 = Bank Operations.*

---

## The 20 wealth processes, by canon domain

Each process carries a full 6-layer Banking OS simulation + Value Bleed + Elastic Ops business case in `apa_v3.json`. Cycle time = the Process Health Scan headline. A process can span several domains (one simulation covers several use cases).

### Customer Operations

**Onboarding & Activation** — Acquire · L1 **HIGH**
- **Wealth Client Onboarding** — HNW Client Onboarding · cycle 30-60 days · 5 steps
- **Wealth Suitability & Risk Profiling** — cycle 10-21 days · 4 steps
- **Wealth Tax Residency & CRS Classification** — cycle 21-45 days · 4 steps
- **Wealth Intergenerational Wealth Transfer** — cycle 6-18 months · 5 steps

**Account & Profile Servicing** — Maintain · L1 MED
- **Wealth 3rd Party Access Management** — cycle 15-35 days · 4 steps
- **Wealth ACAT & Account Transfers** — cycle 6-15 business days · 4 steps
- **Wealth Beneficiary & Estate Processing** — cycle 60-180 days · 4 steps
- **Wealth Client Servicing & Lifecycle** (RM support ops) — cycle 30-75 days · 5 steps

**Payments & Money Movement** — Move · L1 MED
- **Wealth Payments & Cash Management** (custody movements, settlement, cash sweeps) — cycle 2-5 days · 4 steps

**Disputes & Resolution** — Resolve · L1 **LOW** _(advisor-mediated — low leverage; don't lead here)_
- **Wealth Disputes & Chargebacks** — cycle 30-75 days · 4 steps

**Loan / Credit Origination** — Borrow · L1 MED
- **Wealth Lending & Credit** (Lombard lending, jumbo mortgage, facility structuring) — cycle 30-75 days · 5 steps
- **Wealth Corporate Actions Processing** — cycle 5-15 days · 4 steps

**Credit Servicing & Restructuring** — Service credit · L1 MED
- **Wealth Margin Call Processing** — cycle 1-3 days · 4 steps

**Specialist & Advisory** — High-touch · L1 **HIGH**
- **Wealth Investment Proposal Creation** — cycle 14-30 days · 4 steps
- **Wealth Client Servicing & Lifecycle** (portfolio rebalancing & execution) — cycle 30-75 days · 5 steps

**KYC Periodic Review** — Refresh · L1 **HIGH**
- **Wealth KYC & Due Diligence** (annual client review, source-of-funds re-verification, enhanced-DD triggers) — cycle 30-75 days · 4 steps

### Bank Operations

**Financial Crime Surveillance** — Surveil · L1 **HIGH**
- **Wealth Financial Crime & Fraud** (cross-border transaction monitoring, SAR/STR, sanctions screening) — cycle 21-45 days · 4 steps
- **Wealth PEP / Sanctions / Adverse Media Monitoring** — 40% stall rate · 4 steps

**Credit Portfolio Surveillance** — Monitor · L1 MED
- **Wealth Credit Risk & Decisioning** (collateral re-valuation, LTV monitoring) — cycle 21-45 days · 4 steps

**Regulatory Reporting & Audit** — Report · L1 **HIGH**
- **Wealth FATCA / CRS Reporting** — cycle 60-120 days · 4 steps
- **Wealth Regulatory & Compliance** (reg-change impact, audit trail & evidence) — cycle 30-75 days · 4 steps

**Operational Controls & Recon** — Reconcile · L1 MED
- **Wealth Regulatory & Compliance** (audit trail & evidence mgmt) · **Wealth Client Servicing & Lifecycle** (fee calc & billing, performance recon)

---

## Governance hook for wealth pitches

Use the **Decision Token** to make "governed advice" tangible: every agent action (a rebalance proposal, an EDD escalation, a margin call) emits *policy applied · actor identity · model version · outcome · full context* — regulator-scrutable, board-trustable. This is the wealth answer to "can we trust AI near a UHNW mandate?"

Pairs with the wealth NBA method ([`next-best-action-method.md`](next-best-action-method.md)) and the Wealth OS narrative ([`wealth-os-narrative.md`](wealth-os-narrative.md)).
