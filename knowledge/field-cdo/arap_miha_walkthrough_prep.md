# Prep Questions for Miha Mura Walkthrough — April 14, 2026

> Context: Product walkthrough of the acquired AR/AP/Expense Management codebase. Answers feed directly into the three "bill of material" deliverables (competitive landscape, why-backbase one-pager, ROI calculator).

---

## 1. Product Capabilities & Differentiation (feeds BOM #1 & #2)

### What's Live vs. Roadmap
- Which of the three modules (Invoicing/AR, Bill Pay/AP, Expense Management) are **production-ready today**?
- Are there capabilities listed in the announcement (e.g., e-invoicing compliance, AI-approval workflows, AI-receipt matching) that are still in development?
- What's the current state of the **micro-frontend / embeddable** option vs. headless API-only?

### White-Label Depth
- How deep does white-labeling go? (just branding/colors, or full UX customization?)
- Can banks configure workflows (e.g., approval chains) without engineering effort?
- Multi-language / multi-currency support — which regions are ready today?

### AI Capabilities
- What specifically does the AI do in each module? (OCR accuracy rates, reconciliation logic, categorization quality)
- Is the AI model proprietary or built on foundation models?
- What training data / calibration is needed per bank deployment?

### Integration Architecture
- What accounting systems are integrated today? (Xero, QuickBooks, Exact, local players?)
- Payment rails — which payment methods/gateways are supported?
- How does a bank connect their core banking / payment infrastructure?
- What's the integration effort for a typical bank deployment?

---

## 2. Competitive Positioning (feeds BOM #1)

- Who did Monite lose deals to most often? Why?
- Which competitors came up in sales cycles? (Autobooks, WeFact, country-specific players?)
- What was the #1 reason customers chose Monite over alternatives?
- Are there published case studies or reference clients we can use?
- Did they have a competitive battle card or positioning doc?

---

## 3. Pricing & Revenue Model (feeds BOM #3 — ROI Calculator)

### Pricing Structure
- Confirm: flat platform fee + variable per-transaction fee. What are typical ranges?
- How is "transaction" defined? (per invoice sent? per payment processed? per bill paid?)
- Is there a per-SME-user fee or is it unlimited users per bank?
- What's the revenue share model — how much goes to Backbase vs. the bank?

### Unit Economics
- What's the average revenue per SME client per month? (at different usage levels)
- What's the typical bank deployment cost (implementation + run)?
- Time to go live for a typical deployment?
- What does the **revenue calculator** that Jarno mentioned look like? Can I get a copy?

### The Data Loop / Credit Angle (Slide 13)
- Is there an existing API or data export that banks can use for credit decisioning?
- Has any client actually used AR/AP data for invoice factoring or credit products?
- What data points are captured that would be useful for lending? (invoice amounts, payment terms, days outstanding, counterparty info)

---

## 4. Go-to-Market & Sales (general context)

- What was Monite's typical sales cycle length?
- What personas were involved in the buying decision? (Head of SME, IT, Compliance?)
- What were the top 3 objections they heard from banks?
- Are there **demo environments** ready for us to show prospects?
- What compliance/regulatory considerations per region? (e-invoicing mandates, data residency)

---

## 5. Rabobank-Specific (if appropriate to discuss)

- Any insights from the Rabobank pitch last Thursday?
- What specific modules were they most interested in?
- What would a "starter package" look like for a bank in experimentation mode?

---

## Key Outputs Needed from This Walkthrough

| Output | What I Need | Priority |
|--------|------------|----------|
| Feature matrix | Confirmed list of what's live vs. roadmap per module | High |
| Pricing model | Transaction fee ranges, platform fee, revenue share | High |
| Competitive intel | Who they lost to, why customers chose them | High |
| Integration effort | Typical deployment timeline and cost | Medium |
| Data/credit loop | What data is available for lending use cases | Medium |
| Demo readiness | Can we demo this week to SEs? | Medium |
