# Skill Spec — `/pricing-model`  (Phase 1 · structural)

> **Status:** Proposed skill spec for Architect-tier implementation. Not yet built.
> **Tier:** Architect implements (`.claude/commands/pricing-model.md` + `tools/pricing_model.py`).
> **Origin:** `knowledge/learnings/pipeline_gaps/deal_desk_commercial_track.md` (archetype #1).

## One-liner
A parameterised **usage-based pricing engine**: given a baseline fee schedule and a band/uplift structure, generate a defensible multi-scenario pricing model — projections across the growth metric, scenario comparison, crossover analysis, margin/head-to-head, and the software-vs-3rd-party split needed for a Price-of-Failure (POF) / BAFO submission.

## Why this is distinct from `generate-roi-excel`
`generate-roi-excel` models the **benefit** side — value levers, savings, ROI for the *client's* business case. `/pricing-model` models the **price** side — what *Backbase charges* and how it scales with the client's growth. Opposite side of the table. No overlap.

## When to use
- Structuring or re-structuring a commercial offer with usage/AUM/seat/tier-based pricing.
- Negotiation rounds: "what if we drop the baseline but raise the top band", "where does scenario B beat A", "re-price to a £X total", "split software from 3rd-party fees for the POF".
- Feeds the negotiation-deck kit (Phase 2) directly.

## Inputs
| Input | Required | Notes |
|---|---|---|
| Baseline fee schedule (per-line, per-year) | Yes | e.g. product lines × Yr1–5. |
| Growth metric + bands | Yes | AUM / seats / volume; band thresholds + uplift % per band. |
| Scenario definitions | Yes | Each = baseline point + band overrides (e.g. smoothed top band). |
| 3rd-party / pass-through fees | Optional | Held flat, excluded from uplift (POF requirement). |
| Target total (for back-solve) | Optional | e.g. "re-price all software to hit £X over 5yr" → solve the proportional discount. |
| Growth trajectory assumptions | Optional | Organic % / acquisition steps for in-term realism. |

## Processing / core capabilities (the methodology to encode)
0. **Two pricing bases (deal-type-general)** — `band_multiplier` for wealth/AUM (baseline × per-band uplift) and `tiered_per_unit` for retail/banking/lending (flat fee + per-customer/account/loan volume tiers). Both are regression-tested; crossover, margin H2H, and the POF split work on either. Metric is generic (£bn AUM, customer counts, loan volumes) with metric-aware axis labels + a display divisor.
1. **Band engine** — apply multiplicative or additive uplift per band across the growth metric; support *reducing-uplift* curves (rate falls as you scale) and **smoothing** (cap the top band below the standard rate).
2. **Projection table** — fee at each growth milestone, per scenario, side by side.
3. **Crossover analysis** — the growth point where one scenario overtakes another; flag where it sits vs the client's stated ambition and vs realistic in-term growth.
4. **Margin / head-to-head** — for two structures hitting a similar headline, show which yields more to Backbase across the realistic growth range (not just at one point).
5. **Software vs 3rd-party split (POF / BAFO)** — apply uplift to software only; hold pass-through fees flat; **back-solve a proportional discount** so the grand total (software + uplift + 3rd-party) equals a target. (This is exactly the Phase-A maths the deal-desk asked for — encode it once.)
6. **Scenario tabs** — emit a clean multi-tab xlsx: Current, each What-if, Head-to-head, POF split.

## Output
- Multi-tab `.xlsx` (openpyxl), brand-formatted, each tab self-explaining with assumptions stated.
- A compact JSON/return summary (baselines, crossovers, totals) that the Phase-2 negotiation-deck kit consumes to render scenario cards + projection table + travel slide without re-deriving the maths.

## Guardrails (conservative-by-default, per CLAUDE.md)
- Every number traces to an input or a stated assumption; assumptions listed on each tab.
- No optimistic rounding; show the downside / crossover honestly.
- Never silently change an approved band schedule — scenario overrides are explicit and labelled.
- Pricing is commercially sensitive: outputs are internal/deal-desk by default, not client-facing until a consultant promotes them.

## Governance (mandatory)
- Journal entry on completion · telemetry block · dual checkpoint (assumptions confirmed pre-build; model reviewed post-build).
- Anonymised methodology patterns (band shapes, smoothing tactics, crossover framing) can harvest to `knowledge/learnings/` — **never** client prices.

## Dependencies
- `xlsx` skill / openpyxl · Frontline tokens for formatting · feeds Phase-2 negotiation-deck kit.
- Higher build care than `/deal-notes` — the band/smoothing/back-solve logic must be pinned precisely and unit-tested against the existing hand-built models (`scenario_pricing_020626.xlsx`, `BAFO_POF_software_3rdparty_split.xlsx`, `AUM_Growth_Model`). **This is why it follows `/deal-notes`, not leads.**

## Definition of done
Reproduces the existing hand-built Schroders models to the penny from parameters alone (regression test), and can re-run any negotiation what-if (re-price to target, smooth a band, compare two structures) in one call with a defensible, assumption-stated xlsx out.
