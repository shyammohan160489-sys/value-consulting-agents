# Wealth OS — Canonical Wealth Narrative & Archetypes

**Version:** 2026.06 · **Status:** CANONICAL for all **wealth / private-banking / investing** engagements.
**Extends:** [`knowledge/product/banking-os.md`](../../product/banking-os.md) (product substance) + [`knowledge/design-system/narrative-spine.md`](../../design-system/narrative-spine.md) (voice). Those are the master canon, auto-loaded every session via CLAUDE.md. **This file is the wealth flavour of that canon** — read it for any wealth account.
**Why it exists:** the canon is Banking-OS-general; this captures the *Wealth OS* articulation, the **client archetypes**, and the **Wealth 2.0 / "2609" forward narrative** so they're reusable across every wealth engagement and every session (existing or new), not re-derived each time.
**Sources harvested:** Pictet engagement (view-only→do-more reframe, the economics), the account team's onsite deck (Private Banking & Wealth OS / Nexus / Sentinel / Wealth 2.0 product plan), the multi-segment prototype (archetypes), `backbase_platform_lexicon.md`, `domains/product_directory_wealth.md`.
**Handling:** Wealth 2.0 specifics are **forward-looking** — much ships on the **2609 release** and is **not yet fully on backbase.io**. We sell the *narrative* now; flag roadmap items as direction, not GA. Pricing & named clients = internal/1:1 only.

---

## 1. Wealth OS = Banking OS, for wealth
The **Private Banking & Wealth OS** is the wealth expression of the **Banking OS control plane** — *"the system to coordinate and govern the work across your frontline,"* across clients, relationship managers, agents and the downstream stack (core/Avaloq, PMS, market data, custody). Same primitives as the canon:
- **Nexus** (semantic layer · UNDERSTAND) — one shared source of client truth across portfolios, holdings, documents, interactions.
- **Sentinel** (authority layer · AUTHORIZE) — governed, auditable execution; **entitlements for legal entities, proxies, delegated authority** (the private-banking complexity *is* Sentinel's sweet spot).
- Orchestration · Connectivity · Intelligence layers as per canon.
Add-on-top, **no rip-and-replace**. Lead with the operating-model thesis, then anchor on Wealth OS = control plane.

## 2. The wealth From→To — "view-only → doing more"
The portable wealth scaffold (use as the deck/prototype spine):
**View → Transact → Serve → Advise.**
- **FROM:** a **view-only** app — clients see portfolios/statements; everything else is phone + email; no employee channel. A narrow base, so an upgrade reads as cost without reward.
- **The line already crossed:** **payments** took the app from *view* to *transact* — and it worked. Proof the model pays.
- **TO:** the next rungs — **Serve** (requests, change-of-circumstance, documents — digital, governed) and **Advise** (RM-led proposals, suitability, e-sign) — and the **RM cockpit**. Depth in the channel they already have; advisory-led, never self-directed robo.
This is the wealth instance of the canon's Fragmentation→Unified Frontline From→To.

## 3. Wealth 2.0 / the "2609" release (forward narrative)
- **Lineage:** Digital Investing (today's LTS) → **Wealth 2.0**. It is a **migration / re-platform, not an upgrade** — "everything changes, little reused" — so position it as Backbase-**led** & funded, never client-self-run.
- **Wealth 2.0 ecosystem:** Entitlements · Arrangements (products) · Audit · Transaction Signing · Product Shopping (portfolio origination) · **Digital Assist employee app = the RM Portal/cockpit** · richer client journeys. Headless option available (Client/Service APIs).
- **Committed product plan (2026/7 — Backbase good-faith roadmap, explicitly NON-BINDING; direction not GA/contract).** Source: "Backbase Wealth 2.0 | Product Plan & Key Commitments" (Piotr onsite deck slide 14). Five published workstreams:
  1. **Execution / trading (full):** New Execution Journey (Buy/Sell **Stocks & ETFs**) · Limit Orders · Stop-Loss/Profit · Stop-limit · Orderbook · Cancel/Update pending order · Cash Account Selector · Corporate Actions · Transaction-signing config · Additions in Pre-order / Order Summary. **NB — Wealth 2.0 genuinely includes execution/trading.** (Tension for conservative PBs like Pictet who deem execution-only outside their value prop; if adopted, frame trading as *integrated into the advisory flow, not standalone* — see §7.)
  2. **Discover & market data:** Discover Journey · Real-time pricing (live / 15-min) · News in Instrument · Asset/Activity search filters · Statistics Carousel · Fund Details · Instrument detail.
  3. **Portfolio & analytics:** Total Net Worth (assets + liabilities) · External Assets · Aggregated Analytics/Activity · Daily-Change Reporting & Dashboard · Performance Benchmarks · Position Detail · Sort/Group Portfolios · Dashboard Currency · Change Fund-of-Funds · Portfolio edition (DM) · Name-change · ASK/ISA limit graph · new asset types (Bonds, Treasury Bills, Rights).
  4. **RM / employee + AI (the cockpit, named):** **RM Client 360 · RM MVP Dashboard · RM Meeting Preparation** (auto-draft yearly reviews) · **RM AI Smart Insights** (AI in Client 360) · **RM AI Smart Outreach** (re-engage dormant clients) · Contact Centre · Investment Ideas. *Employee-side AI — the safe framing for AI-averse banks.*
  5. **Foundation:** **Entitlements v2** (more complex use cases — corroborates the permissioning/Priority-2 story) · **Audit Integration** (corroborates Sentinel/auditability) · single-journey **Origination** for several product types · Multi-assessment.
- **Deployment:** on-premise **or** Azure CH (cloud is now on the table, gated on Azure-CH availability) — *client's choice*.
- **References:** Danske live; further wealth references maturing (UK). Never-first-mover banks take a fast-follower slot.
- **Sell now, GA later:** much lands on the **2609 release** / not yet fully public — articulate the destination so accounts commit to the path; mark roadmap as direction.

## 4. The wealth client archetypes (CANONICAL — use across prototypes & decks)
The reusable segmentation. Pure private banking — **no retail/mass-market, no robo**; segments differ by *configuration*, not by separate builds.

| Archetype | Profile | Experience emphasis |
|---|---|---|
| **Rising / Next-gen** | Entry private-banking + inheritors; digital-comfortable; sub-UHNW | Mobile-first, guided monitoring; advisor anchored on every screen; guided ideas (not self-trade) |
| **Core HNW** | Classic private-banking relationship | Full hybrid — portfolio + payments + e-sign + documents + secure messaging |
| **UHNW / Family Office** (PIO) | 50M+; holdings, trusts, next-gen pockets | **Multi-entity consolidation, proxies & delegated authority** (Entitlements), bespoke reporting, the private team |
| **Alternatives** (PAA) | PE / RE / hedge focus | Capital calls, illiquid valuations, the J-curve, document-heavy, signature-driven |
| **The RM / Advisor** (cross-segment) | Relationship manager | The **cockpit** (Digital Assist): Client 360, next-best-action, meeting prep — admin time → advice time |

(Supersedes the stub in [`personas.md`](personas.md). Map a client's real book to these; rename labels per house style.)

## 5. The differentiation lever — configure, don't rebuild
One **component library**, rendered per archetype through **configuration** (Experience Manager / Tailored Value Proposition) — the brand "Touch" lives in **config, not bespoke code**, so it survives every release. This is the single biggest de-customisation / upgrade-risk lever for incumbent wealth accounts, and the spine of the prototype.

## 6. Reusable assets & how to apply
- **Prototype:** `Engagement/Pictet/Output/pictet_segments_prototype.html` — the reference multi-segment, **theme-swappable** wealth prototype (5 archetypes + Serve/Advise journeys + RM cockpit). De-brand by swapping the `THEMES`/sample-identity blocks. Use it as the starting template for any wealth account's "art of the possible."
- **Deck spine:** open on operating-model thesis → view-only→doing-more → economics (run→change) → the archetypes (configure don't rebuild) → Ignite + renewal → Wealth 2.0/Banking OS horizon.
- **Assessment:** maturity = distance from the Unified Frontline; the value-leakage / resolution-loop method (canon §9) applied to wealth servicing & advice.

## 7. Guardrails (wealth-specific)
- **Advisory-led always** — no execution-only/robo race-to-the-bottom for conservative private banks; "doing more" = depth + advisor efficiency, not net-new client-facing AI where unwanted.
- **Governance is a feature, not a risk** — lead with Sentinel/auditability for legal-entity/proxy complexity (it's what they're already trying to build in the back-end).
- **Respect existing internal builds** (e.g., a client's own employee app); position Wealth OS as complement/where it serves them, decided in Ignite — not a footprint land-grab.
- **No fabricated client ROI** — benchmark-bounded, "sized in Ignite."

---
*Maintenance: when the canon (`banking-os.md` / `narrative-spine.md`) updates, this inherits automatically — only add wealth-specific deltas here. When Wealth 2.0 / 2609 ships features to GA, move them from "forward" (§3) to confirmed.*
