# Negotiation & Commercial Strategy — Tactics Library

**Status:** CANONICAL for commercial negotiation. Reusable across any deal. Feeds the proposal builder and the (Phase-3) negotiation-strategy agent.
**Source:** Aniket's **Negotiation Planner** (`negotiation_planner.html`, Jun 2026) — negotiation IP carried from his Salesforce CPQ days, formalised into a structured planner. Connects to `deal-pricing-system/knowledge_base/templates/negotiation_best_practices.md` and `ai_pricing_playbook.md`, and to the Schroders "travel" anchoring artefact.
**Maintainer note:** Treat this as a *living* library — **always watch for more negotiation / commercial-strategy intel** (from Aniket, Anton, live deals) and fold it in here.

---

## 1. The one rule — concessions must SHRINK (the Martini)

The *shape* of your concessions across rounds **is a message**. The buyer reads it. Five patterns, ranked:

| Pattern | Rank | Shape (cumulative across 4 rounds) | What it signals |
|---|---|---|---|
| **Martini** | ✅ Best | `0 → 0.60 → 0.90 → 1.0` (strong anchor, then shrinking) | "I'm serious about my first offer, but can concede some." |
| **Ice Cream** | Good | `0.50 → 0.80 → 0.95 → 1.0` (concede at open, largest first, shrinking) | "I'm willing to negotiate, but approaching my floor." |
| **Avalanche** | ❌ Bad | `0.05 → 0.20 → 0.50 → 1.0` (bigger each round) | "If you keep pushing, I'll concede more." — trains the buyer to push. |
| **Wrecking Ball** | ❌ Worst | `0 → 0 → 0 → 1.0` (nothing, then one big drop) | "I'm inflexible / negotiating in bad faith." |
| **Lollipop / Sucker** | ❌ Worst | `1.0 → 1.0 → 1.0 → 1.0` (everything in round 1) | "Take it or leave it." — gives away all leverage instantly. |

**Rule:** make each move **visibly smaller than the last**. Aim for the **Martini**. Never let concessions grow round-on-round.

**Diagnose the counterparty's shape** (and yours) from their offer sequence:
- A *later* offer priced higher than an earlier one → **Inconsistent** → resist.
- Sum ≈ 0 → **No concessions yet** → hold posture.
- All up front → **Lollipop**; nothing-then-one-drop → **Wrecking Ball**; growing each round → **Avalanche** → these are weak/manipulable shapes, respond firmly.
- Shrinking after a real first move → **Martini/Ice Cream** → disciplined counterpart.

---

## 2. The 4-stage concession ladder

| Stage | Posture | Next-best-action | What you ask in return |
|---|---|---|---|
| **1 · Anchor** | Firm. Zero upfront. | Present the **full-scope value case**, state **no discount**, secure agreement in principle as a **reference**. | Set the value baseline; secure willingness to serve as a reference. *(Full scope · 5-yr term · list-anchored value · std renewal cap · reference rights.)* |
| **2 · Counter 1** | **Biggest move, cheap-weighted.** | Make your **largest** concession now, weighted to **cheap** levers (Net 60, sandbox, training), paired to a **signed 5-yr term + reference rights**. | Concede only against a 5-yr term and signed reference rights. |
| **3 · Counter 2** | **Smaller** move, structure + price. | A visibly **smaller** move than Counter 1. Trade the **volume discount only** against **year-one prepay + a written expansion commitment**. | Price only for prepay + written expansion commit. |
| **4 · Best & Final** | **Smallest** move, floor + closer. | Smallest move, **dated and final**. Send the **price-hold addendum to deal desk** (gated). State the **signature deadline once, then stop talking**. | Final & dated. Price-hold addendum needs deal-desk sign-off, not rep authority. |

The ladder *is* a Martini: Anchor (0) → big → smaller → smallest.

---

## 3. The lever families — exhaust 1→4 BEFORE you touch price (5)

Trade in this order. **Never open with price.** Spend the cheap, margin-friendly families first.

| # | Family | Margin cost | Trade rule | Levers |
|---|---|---|---|---|
| 1 | **Solution optionality** | **Zero margin cost** | **Anchor here.** Reframes the deal from a *price* decision to a *configuration* choice. | Good/Better/Best · Bundle/unbundle · Phasing · Scope ramp |
| 2 | **Commitment terms** | Often **margin-accretive** | You *gain* commitment in return for value. Trade these **before any price move**. | 3/5/10-yr term · Volume tier · Year-one prepay · Expansion commit |
| 3 | **Non-price value** | Capacity cost | Cheap in cash, real in delivery hours — **price the bench, don't treat as free**. | Sandbox · Training credits · Premium support/SLA · Program architect · Dedicated CS · Advisory seat |
| 4 | **Timing & cash flow** | Cost of capital only | Eases the buyer's budget, barely touches margin. | Payment terms · Stub bill · Staggered activation · Billing cadence |
| 5 | **Price** | **1:1 margin hit** | **Last resort.** Every point erodes margin **and sets the renewal reference**. | Volume discount · VPA / price hold · Renewal cap |

---

## 4. Lever types — classify every concession before you give it

| Type | Meaning | Examples |
|---|---|---|
| **Cheap** — *give first* | Low margin cost, give early to show movement | Net 60, stub bill, staggered licenses, sandbox + training, swap language, growth tiers, SLA |
| **Costly** — *trade hard* | Real margin cost, only against something | Volume discount, VPA / price hold, discount-to-floor, program architect, dedicated CS |
| **Resist** | Hold the line; gate it | Price-hold addendum (deal-desk gated), flat renewal |
| **Extract** — *what you GET* | Always take something back | Reference rights, case study, press/speaking, expansion commitment |
| **Posture** | Frame, not a giveaway | Full scope, 5-yr term, list-anchored value, signature deadline |

**Golden rule:** every concession is **traded, never gifted** — pair each give with an *extract*.

---

## 5. Read your leverage (switching cost → posture)

| Switching cost | Posture |
|---|---|
| **High** | Anchor firm. The incumbent **lock-in is your leverage**, not a reason to discount. |
| **Medium** | Standard anchor. **Protect price, trade structure.** |
| **Low** | The buyer has real alternatives. **Lead with non-price value, hold the floor tightly.** |

---

## 6. The economics — never cross the floor

Discipline = a **floor gross margin** you do not breach. `maxDiscountToFloor` computes the *maximum* discount before the floor is hit, from: in-scope module list × years-active × (1 − GM) recurring cost, plus services one-time × (1 − GM) less any services credit, plus delivery adds, all grossed up by `1/(1 − floorGM)`. Headroom to that floor sets how much room you actually have.

- **Deal-size bands:** large ≥ **$10M** TCV · mid ≥ **$3M**.
- **Discount headroom bands:** ample ≥ **18%** · moderate ≥ **8%** to the floor. Below moderate → almost no room; lead on value, not price.

---

## 7. Solution optionality — the anchor lever (zero margin cost)

Reframe from "what's your discount?" to "which configuration?". Worked example structure:
- **Good / Better / Best** — Good (Digital Foundation) · Better (Engagement Platform) · **Best = anchor** (Full Engagement + Wealth, dedicated CS, architect, price hold). Anchor on Best.
- **Bundle / unbundle** — full bundle (anchor, simplest to sign) · core + add-ons · à la carte (most flexible, higher unit price).
- **Phasing** — big bang · **two waves (anchor)** · three waves.
- **Scope ramp** — flat · **expanding (anchor)** · pilot-to-platform.

*(Map "Good/Better/Best" tiers onto the current Banking OS 4-solutions where relevant — see `knowledge/product/banking-os.md`.)*

---

## 8. Deploy by scenario (brainstorm aid)

| Scenario | Play |
|---|---|
| Buyer opens with "what's your best price?" | Don't answer price. Anchor on **Solution optionality** (Good/Better/Best); reframe to configuration. |
| Incumbent, high switching cost | Anchor **firm**; lock-in is leverage; trade structure not price. |
| Competitive, low switching cost | Lead **non-price value**; hold floor tightly; smallest viable moves. |
| Buyer keeps pushing each round | You're drifting to **Avalanche** — stop; reset to shrinking moves; make next move smaller + dated. |
| Need to show goodwill early | Give a **cheap** lever (Net 60, sandbox, training) — never price — and **extract** a reference. |
| Approaching the deadline | **Best & Final**: smallest move, dated, signature deadline stated once, price-hold gated to deal desk. |
| Asked for a discount with nothing back | Convert to a **trade** — discount only vs prepay + expansion commit + multi-year term. |

---

## 9. Deal-desk approval governance (Backbase · Salesforce CPQ)

Discounting is **role-gated** — an AE cannot self-discount. Know which tier a move triggers *before* you make it.

| Role | Discount authority |
|---|---|
| **AE** | Up to **0%** |
| **RVP** | Up to **20%** |
| **SVP** | Up to **40%** |
| **CCO / Deal Desk** | **Over 40%** |

(Applies across all editions + embedded hosting pricing.)

**Mandatory Deal-Desk triggers** (regardless of discount %): selling **outside ICP** · a deal **without managed hosting** · a **new-logo deal under €600K** · a **contract term over 5 years** → early qualification, in or out.

**Approval flows:** *Happy* (within model → straight to order form) · *Approval* (threshold crossed → approvals workflow) · *Validation* (discount on an existing run-rate → added Finance check). Cadence: Wed review → Thu Finance prep → Fri Executive Deal Desk (deal economics + concessions).

**Packaging context (the real Good/Better/Best, §7):** three editions — **Essential / Premium / Signature** (use-case packaged; Premium ≈ 100% baseline, Essential ≈ 70–80%, Signature ≈ 130–180%), with **localized geo pricing** (Tier-1 markets 100%, others ~70%). License model = **Base Fee + User/AUM Fee**; cloud-default; **€600K minimum deal size**.

**Deploy:** plan concessions *within* the AE's authority; when a move crosses a tier, route it deliberately with the deal-economics pack. This is Anton's "internal approval gate" trigger and the gated levers in §4, made concrete. *Source: Elevate Rookie Basecamp Day 1 (slides 57–80) + Schroders CPQ Q-06367.*

## 10. Provenance & related

- **Source:** Aniket's Negotiation Planner (Jun 2026). The planner also computes a live offer table, detects the concession shape, and meters discount headroom to floor.
- **Related:** Schroders negotiation playbook + "travel" anchoring 1-pager; `deal-pricing-system/knowledge_base/templates/`; the deal-desk codification (`knowledge/learnings/pipeline_gaps/deal_desk_commercial_track.md`); the **proposal builder** (`presentations/gtm-os-proposal-builder/`).
- **Anton's Sparekassen retro** — the real-world sequence of a fellowship commercial — slots alongside this as the *worked example* of these tactics in motion. *(Absorb when accessible.)*
