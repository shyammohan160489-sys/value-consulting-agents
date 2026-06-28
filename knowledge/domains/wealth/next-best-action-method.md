# Next-Best-Action for Wealth — Reusable Method

**Status:** Reusable across **all** wealth NBA / smart-signal / RM-copilot pitches (Pictet, Evelyn, and any other wealth manager). Apply this method to any client's "nudges & signals" wish list.
**Origin:** Schroders NBA engagement, Jun 2026 (working artifacts at `Engagement/Schroders Group/Output/nba-analysis/` — fork the builders/decks as templates).
**Pairs with:** [`backbase-smart-signals.md`](../backbase-smart-signals.md) (Backbase product language) · [`wealth-os-narrative.md`](wealth-os-narrative.md) (wealth narrative/voice) · [`banking-os.md`](../../product/banking-os.md) (control-plane canon).

---

## 0. The thesis to lead with (advisory, not contrarian)

NBA is mostly a **control-plane problem, not an AI problem**. On a typical ~60-item wish list, only ~1 in 6 genuinely needs bespoke AI; the rest is **shared truth + governance + orchestration + productised agents**. Lead with *"where AI earns its place"* (guidance), never *"this isn't AI"* (negation) — wealth boards want direction, delivered consultatively.

> One-line: **"Start with the foundations, not the algorithm. Buy the control plane; bring your own intelligence and context."**

---

## 1. The four lenses — run every NBA list through all four

**A. AI tier (does it actually need AI?)** — *Rules · AI-Enriched · Predictive · Generative.*
AI ≠ tokens: predictive ML is high-value and runs quietly/cheap; **generative is the only token-heavy tier** — apply sparingly. Putting an LLM on a date/threshold trigger is the costly, governance-risky anti-pattern. Typical split on a wealth list: ~60% Rules, ~20% Enriched, ~15% Predictive, ~5% Generative.

**B. Backbase product classification** (speak their language — see product module):
- **Signal source:** Third-Party · Backbase Rule-Based · Backbase Agentic.
- **Type:** Notification · Task · Alert · Smart Signal (compliance = mandatory Alert "gates").
- **Action:** Surface-only · Create Task · launch a productised **Agent** (Personalised Outreach · Market Move Explainer · Meeting Prep).

**C. OOTB readiness** (the "what can we do today, no prompt engineering?" question):
- **OOTB — data only:** deterministic / ingested, no LLM. Do today with the right data.
- **OOTB agent — context only:** uses a productised agent; context/template config, not bespoke prompts.
- **Prompt engineering — bespoke:** agentic detection reasoning over the client's data + rule-book.
Rule of thumb: bespoke prompt engineering concentrates in the ~10 *agentic growth/retention inference* use cases (share-of-wallet, life events, engagement-lag, at-risk, campaign targeting, note extraction, vulnerability-from-free-text).

**D. Value × complexity** (the prioritisation that drives the roadmap):
- **Value-at-stake** = tied to the *client's own* firmographics / baseline metrics (§3), not generic.
- **Complexity** = **Backbase-side implementation effort (Low/Med/High), NOT the model build.**
- Verdicts: **★ Do-first** (high value × low complexity) · Quick win · Sequence (flag high-value Mediums) · Flagship build (high-complexity agentic).

---

## 2. Hard-won principles & gotchas

- **Complexity is Backbase-side, not build-side.** A heavy ML use case can be **Low** Backbase-complexity if the *client owns the model* and sends it as a Third-Party Signal (e.g., redemption risk), or **High** if Backbase builds the inference (e.g., share-of-wallet). **Who owns the hard build = the signal source.** Don't let "Low" read as "free end-to-end" — the model build still sits on someone's side.
- **"Third-party / source-triggered" assumes the source system emits events** — core/PMS/OMS/AML usually deliver *batch files*, not events. The control plane (Nexus) is what turns batch into real-time, event-able truth. Validate per item ("does T24 emit events or batch?").
- **Centralized decisioning is the make-or-break.** ~200 clients × ~100 signals ≈ **~2,000 signals/RM/month** — prioritisation *is* the ROI. No self-serve GUI for it yet (Backbase productising). Your value-at-stake ranking is the business-rule layer that feeds it.
- **Deterministic-first.** Prefer Rule-Based; reach for Agentic only where inference genuinely adds value.
- **The at-risk / redemption bridge** (resolves "client wants ML pattern-led" vs "we want rule-steered to avoid hallucination"): **rule-based proxy now → accumulate labels via the feedback loop → graduate to the model.** Ships value day one; ML when the data earns it. Also solves cold-start (no labelled outflow history).
- **Governance = licence to operate.** Compliance items are mandatory Alert "gates." Under **FCA Consumer Duty + SM&CR** the regulator wrote *no* new AI rules — human-in-the-loop + overridable + auditable maps 1:1. This is a *positive* (the architecture the regulator already rewards), not a warning.

---

## 3. Where the value is (wealth value levers — tie each to a client baseline)

1. **Retention / attrition** — usually the biggest lever. Each 1pt of attrition on the AUM book ≈ large AUM retained × revenue yield. (Schroders: 4%→2-3% on ~£85bn ≈ ~£850m AUM/pt.)
2. **Share of wallet / held-away assets** — low plan penetration = upside (NNA).
3. **RM productivity** — review-prep hours, % admin time; frees capacity → indirect revenue + hard savings.
4. **Conversion** — lead conversion gap vs benchmark (prospecting NBAs; mostly cheap rules).
5. **Risk / compliance loss-avoidance** — weight up for sensitive books (e.g., charity, UHNW): AML, fraud, vulnerability, suitability.

Use `profile-bank` + `domain-benchmarks` to source the client's baseline; rank for "maximum business value" off these.

---

## 4. Outside-in market proof (validates the approach — cite, don't claim)

- **Morgan Stanley** — ML **"Next Best Action"** for advisors since ~2018 (human-in-the-loop, override) **+** GenAI copilots on OpenAI: **Assistant** (retrieval) & **Debrief** (meeting notes/follow-ups). The cleanest proof of the *two-track* split.
- **Commonwealth Bank** — **Customer Engagement Engine**: ~1,000 ML models, ~55m next-best-conversation decisions/day. NBA at scale; moat = central decisioning + single customer view.
- **DBS** — hyper-personalised nudges off a 15,000-data-point client view. **RBC NOMI** — consumer predictive nudges.
- **Recurring lesson:** (1) separate *predictive NBA* from *generative copilots*; (2) value & risk live in the **single client view + governance/supervision**, not the model; (3) human-in-the-loop for advice; (4) **the copilot beachhead everyone chose first = meeting admin (prep / consented notes / follow-ups), not advice.**

---

## 5. Strategic plays (reuse in any wealth pitch)

- **Build-vs-buy:** replicating the agentic "GenTech fabric" in-house is a multi-year, ~50-R&D-FTE platform programme. **Buy the control plane; bring your own intelligence + context/rule-book.** The edge is the client's *data and rule-book*, not the plumbing.
- **Interim value (when the RM Workspace surface lands late):** the data foundation must be built anyway → build now, surface simply (Teams/email/Snowflake/Salesforce), migrate to the RM Workspace later. The value clock starts now; the surface *amplifies*, it doesn't *start*, value.
- **Phasing waves:** rule-based quick wins + meeting copilot first (prove the platform) → predictive value engines (retention, SoW) → governance/ops + generative scale.

---

## 6. Recipe — applying this to a new pitch

1. Get the client's signal/nudge wish list (NBAs + workflow signals).
2. Classify every item on the **four lenses** (§1) — reuse the Schroders workbook builder (`build_nba_analysis.py`) as the template.
3. Tie value to **that client's** firmographics/baseline (§3).
4. Produce: the **four-tier split** (headline "~X of N genuinely need AI"), the **value × complexity do-first shortlist**, the **OOTB readiness** answer, and the **build-vs-buy + phasing** story.
5. **Tone:** advisory; mark any product-capability specifics as *to-validate with Backbase product* (don't assert product roadmap as fact).
6. **Reusable assets:** workbook builder + workshop deck + value/investment deck at `Engagement/Schroders Group/Output/nba-analysis/`; product language in `backbase-smart-signals.md`.

**Applying to live accounts:**
- **Pictet (Big Day / Ignite):** UHNW, CHF, family-owned/multi-gen; fork the "Full-Circle" Advisor-desk prototype as a live Smart-Signals demo. *Never name other clients to Pictet.*
- **Evelyn / other UK wealth:** same method; lead with FCA Consumer Duty governance and the retention lever.
