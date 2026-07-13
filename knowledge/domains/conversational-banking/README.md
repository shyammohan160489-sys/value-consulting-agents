# Conversational Banking Domain Matrix — Use Cases, Dependencies, Value Density

> **A reusable module for scoping, qualifying, and proving value for Conversational Banking pursuits — especially standalone new-logo deals.**
> Sibling of [`../apa-matrix/`](../apa-matrix/README.md) (which covers back-office agentic processes). This module covers the **conversational front door** across the customer lifecycle.

**Sources:** 2026 Mid-Year Leadership deck (July 2026, slide refs `s###` — extract in `Engagement/internal/2026-mid-year-leadership/Input/`) · `knowledge/product/banking-os.md` (canon) · Eurobank pricing model (`Engagement/Eurobank/Output/MODEL_NOTES.md`, NFCU-parity) · Mayur conversational cost model · live-deployment research (web-verified 2026-07-13, evidence register §8).
**Built:** 13 Jul 2026 for Shyam. Status: internal working canon — re-base all figures on client data before anything client-facing.

> **🖥️ Client-ready interactive version:** [`cb_domain_matrix_toolkit.html`](cb_domain_matrix_toolkit.html) — single-file, Frontline 2026 brand, built as a **consultant's working tool**, not a reference dump. Five views: **The Matrix** (28 cases, filter by role/level/depth, "how we decide" 4-test strip) · **Value Ladder** (L1 first-proof / L2 act-&-enrich / L3 resolve-&-grow, each with its unlock + dependency state, plus the standalone-thesis panel: "Yes — here is the honest boundary") · **Value & Economics** (intent-cost chart + editable break-even calculator) · **Proof Library** (31 deployments, source-flagged) · **First 3 Conversations** (per-meeting questions + leave-withs + the 4 engagement plays + guardrails). **Every use-case card opens a HANDOUT** — why it pays, how to size it, business/architecture/economics questions, what we need from the bank, the engagement play, the falsifier, proof — with **Copy-for-slides / Download .html / Print-to-PDF** so it drops straight into a deck or a meeting. **Client-safe by construction:** internal price books, pipeline names, bot census, and buying-signal research stay in THIS readme only; the toolkit anonymizes the card-issuer sample and uses illustrative editable fees. Open it directly in any browser (fully self-contained, no server needed) — or Netlify it for team/client sharing.

---

## 0. When to use this (standing instruction)

Any pursuit where **Conversational Banking is the opportunity space** — standalone new logo, trade-in displacement, or platform attach. Use it to: qualify the account (§7 signals), pick anchor use cases (§3 matrix), test standalone feasibility (§4 dependency tiers), build the value case (§5–6), and run the Ignite (§7 runbook). Per the mid-year mandate (s277): **all Ignite motions make Conversational Banking the default introduction.**

---

## 1. What Backbase Conversational Banking IS (mid-year canon, July 2026)

**Definition (s227):** *"The conversational front door of Banking OS: turning customer or employee intent into governed banking actions, resolutions, and relationship moments."*

- **Wedge role (s224):** the **Entry Wedge** of Agentic Banking — "the visible front door, the easiest thing for executives to understand and demo." €4M starting ARR (the only agentic solution with revenue today). Customer Operations = high-impact wedge (operational ROI); Relationship/Customer Intelligence = expansion wedge (growth ROI). CB is **SELL NOW / regular motion**; RI and CustOps are Early Access (s266).
- **Modalities:** **Chat** (s228) + **Voice** (s229 — speech-to-speech, "instant responses, no awkward pauses"; financial-services guardrails run **on every turn**: no false promises, no tipping-off, vulnerable-customer handling) + **Agents that take Action** (s230 — "From Intent to Resolution", the bridge into CustOps and RI).
- **Capability ladder (banking-os.md §4):** **Assist** (answer, find, navigate) → **Transact** (authenticated routine actions) → **Resolve** (governed resolution loops → Customer Operations) → **Grow** (financial-progress moments / NBA, *not formal advice* → Relationship Intelligence).
- **Interaction-evolution axis (s192):** *navigate* (web/mobile) → *ask, it answers* (conversational) → *knows before you ask* (proactive) → *plans & acts on your behalf* (agentic). This is the maturity spine of the matrix below.
- **Architecture (s227):** five layers — Interaction (natural-language front door) · Orchestration (event-driven + agentic workflows, skills) · Authority (**Sentinel**: decision authority, policy evaluation, autonomy governance) · Memory (**Nexus**: ontology + customer state graph) · Connectivity (**Grand Central**: connectors, event streams, marketplace). Engine flow: Understand → Orchestrate → Assure → Resolved.
- **Kasisto = the product core** (acquisition completed H1 2026; s193/s234): integration with Digital Banking is top product priority; managed hosting Aug 2026; "KCB→BB CB migration" = migrating Kasisto's **KAI Consumer Banking** clients onto Backbase Conversational Banking; H2 goal "Win First 10 Customers". Marketing (s49): *"Banking OS launch missing proof until the Kasisto acquisition"* — CB is the proof-carrier.
- **Commercial shape:** leadership model (s265): **€350K committed base fee per domain + ~€350K expected consumption after ~4-month ramp = €700K mature ARR per domain**; 50% take a second domain within 12 months. Deal-desk mechanics (banking-os.md §10 + Eurobank model): platform tier by **autonomy ceiling** (Entry €350K = Assist · Critical €700K = Transact · Enterprise €1.5M = group AI platform/BYOA) + LOB fee €350K (1 included) + **€0.07/interaction** (declining) + LLM compute pass-through at cost (≈€0.034/interaction pre-PTU; PTU cuts ~55%). Session convention: **1 conversation ≈ 3 interactions**.

## 2. Kasisto heritage — installed-base evidence (verified 2026-07-13)

Acquisition **announced 23 Jun 2026** (terms undisclosed; American Banker + Backbase press). Founded 2013, SRI/Siri-lab spin-out; ~$90M raised; investors include FIS, Westpac, NCR, BankSouth, DBS. The "~50 customers" count is internal/vendor — not publicly stated; ~20 are publicly verifiable.

**The white-label pattern (Shyam's hunch — confirmed):** nearly every deployment runs under the *bank's* assistant brand; "powered by Kasisto" appears only in launch PR. Verified inventory:

| Bank | Assistant | Live | Published results |
|---|---|---|---|
| DBS digibank India | (DBS brand) | 2016 | **82% containment** (vendor); DBS took equity |
| DBS/POSB SG, DBS Indonesia | POSB digibank VA | 2017 | Messenger + in-app |
| Standard Chartered HK | **"Stacy"** | 2019 | Cantonese+English; payments, spend analysis |
| J.P. Morgan Treasury | unnamed | 2018 | Corporate treasurers: wires, balances, portal nav; KBB design partner |
| TD Canada | **"Clari"** | 2019 | In-app servicing |
| Westpac Group | internal orchestration + KAI-GPT pilot | 2020→ | Consolidated org-wide bots; employee copilot (mortgage ops) |
| Emirates NBD Liv. | **"Olivia"** | 2019 | Digital-bank servicing + spend insights |
| Nedbank | **"Enbi"** | 2021 | **>70% live-chat volume reduction** (vendor) |
| Manulife Bank | All-In VA | ~2019 | PFM-style insights |
| First Financial Bank | **"Gabby"** | 2023 | **90% containment · +27% new CDs · +10% new accounts · Gabby users log in 46% more · 40% of traffic off-hours** (vendor/BusinessWire) |
| BankSouth | **"Rita"** | ~2022 | **96% containment · ~30% call-volume cut in 6 months · $1M new deposits** (American Banker) |
| Meriwest CU | **"Scout"** | 2023 | Users 30% more profitable; 65% off-hours (vendor) |
| + Absa Regional Ops (2020, pan-Africa), Fairwinds/Excite/Valley Isle/Indiana Univ CUs, VeraBank | | | |

**Product taxonomy:** KAI Platform (orchestration, omnichannel) · **KAI Consumer Banking — "200+ intents OOTB"** (the intent library behind our Banking Intent Library story) · KAI Business Banking (2019, built with J.P. Morgan — SMB/corporate: balances, payment activity, cash exposures, approvals) · **KAI-GPT** (first banking-specific LLM, May 2023, employee-facing first) · KAI Answers (gen-AI long-tail Q&A) · KAI Express (community-FI SKU) · KAIgentic (Aug 2025) + KAIops (Oct 2025). Channels: in-app, web, messaging, email; live-chat handoff via Glia/LinkLive. **Voice is claimed but has no marquee public deployment — the s229 voice pitch is a Backbase-era build, sell it as roadmap-fresh, not decade-proven.**

**What the installed base PROVES for new logos:** (a) the conversational layer lands **standalone on any stack** — JPM, TD, StanChart, DBS cores, zero Backbase — the single most important standalone-fit proof; (b) containment at 82–96% is achievable on well-scoped intent sets; (c) it *sells* — FFB/BankSouth show V3 revenue effects, not just deflection; (d) community-FI economics work (KAI Express).

**What it NEVER solved end-to-end** (verified by absence + architectural handoff design): full onboarding/KYC execution (assistants *originate* applications; fulfilment stays in bank systems) · dispute **resolution** (intake/card-block only) · collections · regulated advice · true proactive outbound (alerts only). Every flagship deployment escalates to live chat — **KAI = containment layer, not resolution layer. That gap is precisely what Backbase adds** (CustOps resolution loops, RI proactive plays, Sentinel-governed execution) — the "From Answering to Acting" acquisition logic, and the literal expand path after every CB land.

**NFCU clarification:** Navy Federal is NOT a legacy Kasisto client (their stack: Verint agent-assist + an unnamed member VA; ~35 AI use cases). The NFCU deal (s268/s276) is a **displacement/trade-in + BYOA** play — consistent with the approved BYOA commercial construct (bank brings its own agents onto our governed runtime).

## 3. THE MATRIX — lifecycle × use case × dependency × value

**Columns:** A/T/R/G = Assist/Transact/Resolve/Grow · **Dep** = dependency tier (§4) · **Value pool** = primary lever (§5) · **Verdict** = business-case role: **P1 anchor** (carries the ROI headline) / **P2 supporting** (real but secondary) / **P3 coverage** (ship it, never price the case on it).

### Acquire & Onboard

| Use case — what the customer does | ATRG | Dep | Value pool | Verdict | Live proof |
|---|---|---|---|---|---|
| Prospect product Q&A, "which account fits me", rates/fees (unauthenticated) | A | D0 | V3 lead-gen + V1 (branch/call pre-sales queries) | **P2** | Universal; KAI unauthenticated mode |
| Application help: "what documents do I need", application status | A/R | D0→D4 | V2 abandonment rescue + V1 status-call deflection | **P2** | Onboarding starter pack (s195) |
| Full conversational account opening (KYC in-chat) | R | D4 | V3 + V1 | **P3 today** in tier-1 retail (whitespace); P1 only in inclusion/WhatsApp-first markets | AU Small Finance Bank (<5 min WhatsApp), Absa ChatWallet; Lemonade Maya = the cross-industry benchmark (98% of policies sold by bot) |
| Activation nudges: card activation, first payment, direct-deposit switch | T/G | D1/D3 | V3 primacy + V5 | **P2** | CBA Ceba card activation; Erica onboarding insights |

### Service (everyday servicing — the deflection engine)

| Use case | ATRG | Dep | Value pool | Verdict | Live proof |
|---|---|---|---|---|---|
| Balance, transaction search, "did X go out", account info | A | D1 | **V1 + V2** | **P1** — *if* the call log shows volume (TD sample: "Account info" = $2.1M phone cost) | Erica, Fargo, Cora, everyone |
| "What's this charge?" — unrecognised-transaction triage | A | D1→**D2** (merchant enrichment sharply raises resolve rate) | V1 + **V4** (pre-dispute deflection — many "disputes" die when the merchant name is clarified) | **P1** | Erica; Eno; Ethoca/enrichment data |
| Card controls: freeze/unfreeze, lost/stolen + replacement, PIN, activation, declines | T | D3 | **V1 high** (TD: card replacement $1.9M) | **P1** | Erica, Ceba (200 tasks), Fargo |
| Digital access: password/login reset, device re-registration | T | D3-light (IAM) | **V1 high** — top-3 call driver in most banks, chronically under-scoped | **P1** | Standard in KAI/Truist scopes |
| Payment issues: failed/late payment, status, beneficiary management | A/T | D1/D3 | **V1 high** (TD: "Make a payment" = $3.0M) | **P1** | Fargo, Nubank |
| Profile changes: address, phone, email | T | D3 | V1 **only if call-heavy today**; ≈0 if app-native | **P3 coverage** ← the canonical "hygiene" case — see §5 verdict | Everywhere; never headline it |
| Statements, documents, tax forms, interest certificates | A | D1 | V1 seasonal | **P2** | Standard scope |
| Fees/branch/ATM/opening-hours/product info (authenticated FAQ) | A | D0 | V1 low-med + containment breadth | **P3 coverage** — breadth drives adoption & containment %, not € | All bots |
| Travel notice, limit changes, standing orders | T | D3 | V1 med | **P2** | Standard KAI/Erica scope |

### Transact (money movement by conversation)

| Use case | ATRG | Dep | Value pool | Verdict | Live proof |
|---|---|---|---|---|---|
| P2P / transfers by chat or voice ("send €50 to João") | T | D3 | V2/V5 (self-serve shift; deflection only where phone-banking heavy); voice = accessibility + phone-channel replacement | **P2** digital-native markets · **P1** where IVR/phone-banking volume is big | Nubank Pix-on-WhatsApp (<10s), T-Bank Oleg (voice-biometric), Fargo Zelle |
| Bill pay, top-ups | T | D3 | as above | **P2** | Erica, Fargo |
| Balance transfer / card-to-card offers | T/G | D3+D5 | **V3** (revenue-adjacent; TD: $1.7M intent) | **P1 for Cards LOB** | TD Cards deal shape (Conversational + RI) |

### Engage & Grow (proactive — conversation flips outbound)

| Use case | ATRG | Dep | Value pool | Verdict | Live proof |
|---|---|---|---|---|---|
| Duplicate-charge, refund-tracking, subscription-price-rise alerts → act in-thread | G | **D2 required** | V5 engagement flywheel + V4 | **P1 as engagement anchor** (Erica: ~60% of all interactions start from a proactive insight) | Erica (1.7B insights), Eno, Personetics (150M users) |
| Spend/budget Q&A: "how much on groceries last 2 months" | A/G | **D2 required** | V5 + V3 primacy | **P2** (Eurobank launch scope = exactly this + KB) | Erica, Cleo (7M users, ~$280M ARR) |
| Financial-health nudge → product suggestion (save-rate, payroll switch, rate watch, deposit maturity) | G | D5 (RI) | **V3 measurable** (deposit growth, primacy) | **P1 revenue play** when decisioning exists; else the RI-attach hook | RI plays catalog (Mutual Value Model); First Financial +27% CDs |
| Low-balance / cashflow-ahead warnings | G | D2 | V5 + V4 (OD/NSF fairness, CFPB-sensitive) | **P2** | Erica, Personetics |

### Sell & Deepen

| Use case | ATRG | Dep | Value pool | Verdict | Live proof |
|---|---|---|---|---|---|
| Product discovery & comparison Q&A → warm lead | A | D0 | V3 | **P2** | KAI lead-gen |
| Pre-qualified offer surfaced in-thread, accept conversationally | G/T | **D5** (eligibility/decisioning) | **V3 high** | **P1** where bank has decisioning APIs; otherwise sell as CB+RI | Capital One Chat Concierge (55% better lead→buy, live 2025); First Financial |
| Conversational application assist / abandonment rescue (loan, card) | R | D4 | V3 | **P2** | Onboarding/lending starter packs |
| SME: cashflow & invoice Q&A, payment chasing | A/G | D2-SME | V3 retention | **P2 emerging** — differentiator vs retail-only bots | DBS Joy (corporate, 120k chats since Feb 2025); Erica for Business (>40% of CashPro chat) |

### Protect (fraud, disputes — trust moments)

| Use case | ATRG | Dep | Value pool | Verdict | Live proof |
|---|---|---|---|---|---|
| Two-way fraud-alert confirmation ("was this you?") | T/R | D3/D4 | **V4 + V1** (fraud-line deflection, faster confirm = lower loss) | **P1** | Universal (Eno, Ceba) |
| Scam check-in-the-moment ("am I being scammed?", payment friction on suspicious payees) | G | D5-light | **V4 large** in APP-scam markets (UK PSR liability!) | **P1 UK/AU/NL** | CBA: scam losses −50%, proactive alerts 20k→35k/day |
| Dispute intake → status → resolution | R | **D4** (CustOps bridge) | **V1 high** (TD: top intent, $3.0M) + V4 recovery + NPS at the worst moment | **P1 — AND the expand wedge**: the Disputes Starter Pack demo is CB→CustOps in one flow (s259–261: Kasisto deflects → Flow orchestrates → Case Manager → Nexus → Ethoca via GC) | Starter Pack (live demo asset) |

### Collect & Retain (hardship, churn — the underrated edge)

| Use case | ATRG | Dep | Value pool | Verdict | Live proof |
|---|---|---|---|---|---|
| Pre-delinquency outreach → self-serve payment plan in-chat | G/R | D4+D5 | **V4 high** (roll-rate, recovery, cost per collection contact) | **P1 for lenders/cards** — usually absent from bank bots = differentiation | TrueAccord (96–98% resolve no-human), InDebted (+33% AI-written conversion), spocto/India (Central Bank of India SMA 8%→3%) |
| Hardship conversations (shame-free, 24/7) | R | D4 | V4 + V5 + conduct/regulatory | **P2** | Collections-tech evidence: debtors prefer bots |
| Churn-save: exit signal → retention conversation/offer | G | D5 | V3 | **P2 emerging** (live in telco, thin in banking) | Vodafone-class retention bots |
| Product cancellations, mandate switches handled gracefully | T/R | D3/D4 | V5 + V2 | **P3 coverage** | — |

### Employee side (same platform — count it in the case)

Agent-assist / RM copilot (answers from SOPs while on a call, wrap-up automation, case summarisation): **D0/D1, P1 supporting lever** — reduces AHT on the contacts that *don't* contain. Proof: DBS CSO Assistant (−20% call handling, 500+ agents), Morgan Stanley (98% advisor adoption), Santander (>40% of contact-centre interactions copilot-supported, €200M+ savings claim 2024). In deflection-shy cultures this is the risk-free P1.

## 4. Dependency tiers — what "standalone" actually needs

Shyam's core question: *which use cases depend on underlying domain services?* Answer: classify every use case D0–D5. **CB is interface + orchestration; it consumes whatever APIs exist.** Kasisto's decade on non-Backbase stacks proves D0–D3 land anywhere; D4–D5 is where the expand story (CustOps/RI) begins.

| Tier | Needs from the bank | Time-to-live | Examples | Standalone fit (new logo, non-Backbase stack) |
|---|---|---|---|---|
| **D0 Knowledge-only** | Content: product sheets, fees, policies, SOPs (RAG) | **Weeks** | FAQ, product discovery, how-to | ✅ Trivial — works on ANY stack, zero core integration |
| **D1 Identity + read** | SSO/session + read APIs (accounts, transactions, status) | Weeks–2 mo | Balance, tx search, statements | ✅ Every bank with a mobile app has these APIs — reuse them |
| **D2 Enriched read** | **Categorisation/enrichment service** (merchant cleansing, spend categories, subscription detection) — SaltEdge / Visa-MC enrichment / bank's own PFM engine | +1 dependency decision | Spend Q&A, "what's this charge", subscription & duplicate insights | ⚠️ The ONE genuine new dependency for PFM-class use cases. Treatment (Eurobank precedent, assumption A13): **bank-side dependency or 3rd-party pass-through — never inside the Backbase fee line.** If the bank has no enrichment: scope it as a named prerequisite with 2 options (bank licenses provider / uses existing PFM vendor's API) |
| **D3 Execute** | Write APIs + step-up auth (card controls, transfers, profile updates) + Sentinel-tier assurance | 2–4 mo | Card freeze, payments, address change | ✅ APIs exist (the app uses them); the *real* asks are auth delegation + risk sign-off → this is the **Entry→Critical tier trigger** (autonomy ceiling A3) |
| **D4 Workflow/case** | Case management + process orchestration (ours via CustOps starter packs, or bank's BPM) | 3–6 mo (starter pack compresses) | Disputes, complaints, onboarding docs, hardship plans | ◑ Standalone-ISH: CB does intake/status standalone; **resolution** needs the workflow layer → the natural second-domain sale |
| **D5 Decisioning** | Eligibility/propensity/pricing engines (RI, or bank's own decisioning APIs) | 3–6 mo | Pre-approved offers, NBA, collections treatments, churn-save | ◑ If the bank exposes decisioning APIs, CB consumes them; otherwise this is the RI attach |

**Standalone new-logo scoping rule:** Land = D0+D1 (+D3 for 3–5 named transactions). Prove in 90 days (the "pilot to governed production" executive offer, s-canon). Expand = D2 (enrichment decision), more D3, then D4 (CustOps) and D5 (RI). **Never let a D2 dependency (no enrichment vendor) or D4 ambition (dispute resolution) block the land** — scope around it, name it on the roadmap.

## 5. Value density — the five pools + the hypothesis verdict

**Value pools (every use case is priced on exactly one primary pool):**
- **V1 Deflection** — human contact avoided. *Only counts where the current state is a human channel.* Value = human-handled volume × containment × (cost/contact − bot variable cost).
- **V2 Completion/containment uplift** — failed-self-serve rescued (customer tried the app, gave up, called). Real but smaller; evidence: a large share of inbound calls concern tasks already available digitally.
- **V3 Revenue** — conversion, leads, deepening, retention offers, primacy (deposit growth).
- **V4 Risk/loss** — scam interdiction, fraud-confirm speed, dispute recovery, collections roll-rate.
- **V5 Experience** — CSAT/NPS/accessibility. Strategic, not bankable — unless contractually tied to churn or regulatory (vulnerable customers, accessibility).

**The Shyam hypothesis** — *"making already-easy self-serve tasks (address change) conversational adds little"* — **verdict: SUPPORTED, with one critical refinement.**

- Supported: for an app-native customer, address change via chat vs via profile tab creates **zero V1** (nothing was deflected), zero V3/V4, small V5. Worse — every bot conversation costs the bank ~€0.31 variable (§6) where the app tap cost ~nothing. **Never anchor a business case on conversationalising working self-serve.** These are P3 coverage rows: ship them (breadth drives adoption and containment), price the case elsewhere.
- The refinement: **the unit of value is not the task — it's the task's current channel mix.** The same "account info" intent that is worthless-to-conversationalise in an app-native segment showed up in TD's two-week call sample as **$2.1M of phone-answering cost** (s273). People still call about things the app already does (navigation failure, trust, habit, vulnerable segments) — and the independent evidence says this failed demand is enormous: **73% of customers attempt self-service, but only 14% of issues fully resolve there — and even "very simple" issues resolve only 36% of the time** (Gartner, Aug 2024, n=5,700); 45% abandon because "the company didn't understand what I was trying to do" — which is *exactly* the failure mode a conversational front door fixes (intent understanding vs menu navigation). Banking-specific: ~48% of inbound bank calls concern tasks already re-routable to digital (McKinsey/Finalta). So the address-change genre is re-framed, not dismissed: **the value is capturing failed self-serve demand (V2), never channel preference (V5)** — and it's only bankable where the call log proves the failure volume. So:

> **Price the call log, not the feature list.** A use case earns P1 by appearing in the bank's contact-intent distribution with volume × unit cost — not by sounding impressive in a demo. The TD signal slide is the canonical shape: 51,000 human-answered calls in two weeks → Dispute $3.0M · Make-a-payment $3.0M · Account info $2.1M · Card replacement $1.9M · Balance transfer $1.7M · ten more at $0.6–1.6M each.

- Second refinement: **if the bank is already highly digital, don't force a deflection case.** Anchor shifts to V3 (Grow plays, TD-Cards-style Conversational+RI), V4 (scam/fraud/collections), and **voice** (replacing the IVR/phone channel itself — where the human cost still lives). This is also what the bot census implies: the 53% greenfield pool takes the deflection play; the 34% aging-bot pool takes the trade-in play ("your bot answers, ours acts" — containment delta + action coverage); the 2% modern-gen-AI-bot pool gets sold RI/CustOps instead (s271).

## 6. Break-even economics — when does standalone CB become meaningful?

**Benchmark parameters (verified 2026-07-13 — full register §8):**

| Parameter | Value | Source / vintage |
|---|---|---|
| Cost per inbound call | **£4.18 median / £5.58 mean** (UK, fresh) · $8.01 live-channel (Gartner 2019, stale-but-cited) · use **€4–9 band**, conservative low | ContactBabel DMG 2024 [IND] |
| Live web chat | ~£2.00–3.05 (~45% below voice) | ContactBabel 2024 [IND] |
| Calls per retail customer/yr | **2–4, heavily skewed** (millennials ~5–6/yr; top 4% of customers = 41% of calls) | Bain 2017–18 ⚠️ · McKinsey [IND] |
| Share of calls routine/avoidable | >50% routine; ~70% digitally addressable (Bain 2018 ⚠️); **48% re-routable** (McKinsey/Finalta 2020) | [IND] |
| Safely automatable WITHOUT process rewiring | **only ~20%** — but **25–40% call reduction when properly integrated** | **McKinsey, Apr 2026** [IND] — freshest banking number; see note below |
| Containment norms | typical 20–40% · average 40–55% · best-in-class 70–90% (vendor genre); per-intent (Glia 2026, 400 FIs): balance **94.8%**, direct-deposit setup **91.3%**, transfer troubles **45.2%**, account closures 41% | [VEN, large-n] |
| Gen-AI ceiling | human-serviced contact volume cut **up to 50%**; care productivity worth 30–45% of function cost | McKinsey 2023 [IND] |

> **The McKinsey Apr-2026 pair is the pitch, not a problem:** "only ~20% of calls are safely automatable without rewiring" explains why the 34% aging-bot pool plateaued (bolt-on bots answer, they don't act) — and "25–40% reduction when integrated" is the *integrated* claim only an execution-layer platform can make. Quote both; position Transact/Resolve as the rewiring.

**Unit mechanics (canon + Eurobank model, pre-PTU conservative):**
- Bot variable cost ≈ 3 interactions/conversation × (€0.07 fee + ~€0.034 LLM) ≈ **€0.31 per conversation** (PTU cuts LLM ~55% at scale → ~€0.26).
- Net value per **deflected** human contact = cost per human contact − €0.31. At €5/call → **€4.7**; at €8/call → **€7.7**.
- Conversations that merely shift self-serve (would have been an app tap) contribute **−€0.31** each. Deflected share of bot volume matters.

**Break-even on deflection alone (fixed fees ÷ net value/deflected contact):**

| Landing shape | Annual fixed | Deflected human contacts/yr to break even (at €5/call · €8/call) |
|---|---|---|
| Entry (Assist scope: D0–D2) €350K | €350K | ~75K · ~45K |
| Critical (Transact: +D3) €700K | €700K | ~150K · ~91K |
| Critical + 2nd LOB €1.05M | €1.05M | ~225K · ~136K |

**Worked bands (retail, calls/customer/yr ≈ 0.8–1.5, ~60% of intents addressable, 40–60% containment on addressable, all conservative):**

| Bank size (active retail) | Annual human contacts | Realistic deflected/yr | Deflection value @€5–8 | Verdict for standalone CB |
|---|---|---|---|---|
| ~150–250K customers | ~150–300K | 35–90K | €0.2–0.7M | ⚠️ Deflection alone struggles to clear Critical. **Land Entry/Assist (€350K)**, anchor on V2+V3+voice, or attach to a platform deal. Per-outcome pricing helps here. |
| ~400–600K customers | ~400–800K | 100–250K | €0.5–2.0M | ✅ Clears Critical on deflection alone at the mid-band; V3/V4 stack on top. **This is the floor of the comfortable standalone zone.** |
| ~1–2M customers | ~1–3M | 300K–1M | €1.5–8M | ✅✅ Deflection alone is 2–5× the fee line; the conversation moves to speed & containment proof. TD-class evidence (1.3M calls/yr in ONE card portfolio). |
| Phone/IVR-heavy or voice-first scope (any size) | multiply by voice share | — | — | Voice replaces the most expensive channel — pulls the threshold DOWN a size class. |

**Rule-of-thumb qualification line:** standalone Conversational Banking pays for itself on cost alone at roughly **≥100–150K deflectable human contacts/year in the scoped LOB** (≈ a call-heavy bank of ~400K+ active customers, or a smaller one with a big phone/IVR share). Below that line the deal is still winnable — but the case must be anchored on V3 revenue plays, V4 risk, employee-assist, or ride attached to a platform deal. **This is why the wedge model prices land at €350K committed + consumption:** the fee scales with realised usage, so the bank's break-even is protected at land and the upside is shared at ramp (€700K mature = the consumption model working, not a leap of faith).

Sanity anchors against the fee line: NatWest Cora runs ~11.2M conversations/yr with 49% no-human resolution; TD's single card portfolio burns >$20M/yr answering 15 intents by phone; CBA's messaging absorbs 50K enquiries/day. Against pools like that, €0.7–1.5M/yr is a rounding error — **the qualification job is proving the client HAS such a pool, not defending the price.**

## 7. Running Ignite when Conversational Banking is the topic

**Qualify (before the room):**
1. **Bot census on the account** (the 3 plays, s271): what assistant runs today, bought when, renewal when → *greenfield* (53% of market: deflection-with-containment-proof play) / *aging or channel-only bot* (34%: trade-in displacement — "answers vs acts") / *modern gen-AI bot* (2%: don't pitch CB; pitch RI/CustOps).
2. **The money signal (s272):** 56% of assistant buyers had a live **cost-income/efficiency target** — but 45 of 61 announced it as an "experience program." Screen the annual report for the cost target; listen for the contact-centre pressure (IVR contract ending, volume growth, headcount strain — public only 17% of the time).
3. **The buyers (s274):** Door 1 Head of Digital (gift: "the assistant is the next thing your channel does: answer, resolve, sell"). Door 2 Head of Service/Contact Centre (gift: the deflection number and its headcount plan). Side door: business-line P&L owner (Cards!). COO + data office co-sponsor.

**The ONE data ask that changes everything:** a 2-week contact-intent sample (call log or transcripts, top 25 intents × volume × AHT) + cost per contact + current digital/IVR containment. From it, build the client's own TD-style **intent-cost table** — that table *is* the current-state assessment, the use-case shortlist, and the ROI baseline in one artifact. If the client can't produce it, run transcript classification on a sample (that's exactly what we did for TD) — it's a week of work and it makes the case unfalsifiable. Secondary asks: complaints/disputes volumes, fraud-alert volumes, collections queue size, app adoption %.

**Workshop flow (maps to the standard Ignite arc):**
1. Current state = the intent-cost table on the wall. Circle the top 10 by cost.
2. Overlay the matrix (§3): each circled intent gets A/T/R/G + dependency tier + value pool. The client sees that ~70% of their cost pool is D0–D3 (landable in one quarter) — that kills the "18-month AI program" objection in the room.
3. Pick anchors: **3–5 P1 deflection intents** (D1/D3, high human volume) + **1 revenue play** (V3, usually the Cards or deposit-maturity moment) + **1 resolve loop** (D4 — disputes; demo the Starter Pack; plant the CustOps expand). Explicitly park the P3 hygiene rows as "included, not priced."
4. Value model per §6, conservative: client volumes × benchmark containment (start at NatWest's 49%, not Truist's 80%) × client cost/contact. Session=3-interactions convention. Tier by autonomy ceiling (Assist-only scope → Entry; any Transact → Critical from day one if in-year, per Eurobank §2 lesson).
5. Roadmap = the dependency ladder, not a feature list: **Land** D0–D1(+3 transactions) in 90 days → **Prove** containment weekly → **Expand** D2 enrichment + full D3 → D4 CustOps (2nd domain, the 50%-rule) → D5 RI. Falsifier per thesis (pursuit-loop discipline): "if the intent sample shows <X human-handled contacts on addressable intents, the deflection case fails and we pivot to V3/V4 anchors."

**Positioning language:** never sell "a chatbot" (848 banks already have one — that's the *trade-in* pool). Sell the wedge: *"the front door of the Banking OS — it answers today, acts this quarter, resolves by year-end, and grows from there."* From→To, operating-model thesis, per narrative spine.

## 8. Evidence register (verified 2026-07-13; vendor-claimed flagged)

**Scale proofs (servicing):** BofA Erica 3B+ interactions, ~58M/mo, ~60% proactive-initiated (BofA newsroom Aug 2025) · Wells Fargo "Fargo" 21M ('23)→245M ('24)→1B+ cumulative (Mar 2026) · NatWest Cora 11.2M convs/yr, 49% no-human (IBM 2025); Cora+ gen-AI +150% satisfaction (NatWest Jun 2024) · Truist Assist 5.5M convs, >80% in-bot (FY2025 AR) · CBA 50K enquiries/day, wait −40%, scam losses −50% (Nov 2024) · Bradesco BIA ~74M customers, >2M req/day (Microsoft 2025) · WeBank ~98% AI-handled (dated ~2021).
**Transacting:** Nubank Pix-by-chat/voice/photo <10s (rollout Q1 2025, OpenAI/Nu) · BBVA "Blue" GPT-powered, executes account/card transactions, live Spain+Mexico Feb 2025 · T-Bank Oleg voice-biometric transfers · Erica/Fargo/Ceba execute at scale on deterministic NLU (governance-first design choice).
**Grow/revenue:** First Financial Bank +27% new CDs (Kasisto, vendor) · Capital One Chat Concierge agentic, 55% lead-conversion lift (Fortune Dec 2025) · Personetics 150M MAU / 1.2B insights/mo / 130+ banks (Oct 2024) · Cleo 7M users ~$280M ARR (Sacra Jul 2025).
**Protect/collect:** CBA scam −50% · TrueAccord 96–98% no-human resolution, 20M+ consumers (vendor) · InDebted 80% resolution, AI-written +33% (vendor) · spocto: Central Bank of India SMA 8%→3% Feb 2025 (vendor/ANI) · Klarna: 2.3M convs month-1 = ~700 FTE, then May-2025 partial reversal (rehired humans for disputes/empathy) — **the quality-guardrail citation; use it FOR our Sentinel/human-handoff story**.
**Adjacent (borrow where banking is thin):** Lemonade Maya 98% of policies sold by bot, ~90s quote-to-bind (SEC filings) · Octopus Energy gen-AI answers ~45% of emails, CSAT 80% vs 65% human (2023–24) · Vodafone SuperTOBi ~60M interactions/mo, FTR 15%→60% (2024–25) · Morgan Stanley 98% advisor adoption (advisor-facing only — client-facing regulated advice remains whitespace).
**Deal/GTM proofs (internal, s268–277):** 28 agentic opportunities in pipe, ~€6M pure agentic · standalone CB deals: Navy Federal (Q3), Eurobank (Q4), TD Bank Cards (Conversational+RI, Q4) · 737 verified new-logo CB targets from the 848-prospect bot census · 63/107 base accounts pitchable today, 100% introduced by Q4.

**Contact-economics benchmarks (register):** ContactBabel UK DMG 2024 — inbound call £5.58 mean/£4.18 median, chat £3.05, ID&V £0.58/call (76% of calls) · Gartner 2019 — $8.01 live vs $0.10 self-service (stale, cited) · Gartner Aug 2024 (n=5,700) — 73% attempt self-service / 14% fully resolve / 36% on simple issues / 45% "didn't understand me" · Bain 2017–18 — 2–4 calls/customer/yr skewed; >50% routine; ~70% avoidable · McKinsey/Finalta 2020 — 48% re-routable · **McKinsey Apr 2026 — ~20% automatable without rewiring; 25–40% reduction when integrated** · McKinsey 2023 — gen-AI cuts human-serviced volume ≤50%, 30–45% of care cost · Glia Mar 2026 (400 FIs) — per-intent containment: balance 94.8% / direct-deposit 91.3% / transfer troubles 45.2% / closures 41%, escalation <10% · Juniper 2019 — $0.50–0.70 saved/inquiry (stale genre) · McKinsey collections — digital-first cuts cost ≥15%, +12% payments. **Kasisto installed-base results:** DBS 82% containment · FFB 90% + 27% CDs · BankSouth 96% + 30% call cut · Nedbank >70% chat-volume cut (all §2). **Gaps to fill ONLY with client data:** the intent-share table, calls/1,000 customers, app task-abandonment.

## 9. Maintenance & links

- **Canon guard:** where this file and `knowledge/product/banking-os.md` diverge, banking-os.md wins on product substance; this module owns the *pursuit method* (matrix, dependencies, economics, runbook). Mid-year deltas already flagged in `Engagement/internal/2026-mid-year-leadership/CANON_DIGEST.md` §9.
- **Pricing:** never touch tier prices / interaction curve without deal desk — reuse `Engagement/internal/conversational-banking-pricing/template/` + `tools/pricing_model.py` (Eurobank MODEL_NOTES §7 recipe).
- **Siblings:** [`../apa-matrix/`](../apa-matrix/README.md) (ops processes; use for D4/D5 depth) · [`../agent-autonomy-framework.md`](../agent-autonomy-framework.md) (A1–A5 → tier floor) · [`../agent-pricing/`](../agent-pricing/) (Mayur cost model).
- Re-verify the §8 register quarterly; every client-facing use re-bases on client data (README root rule).
