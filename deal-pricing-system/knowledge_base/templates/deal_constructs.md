# Pricing Construct Definitions

## 0. Base Fee + Tiered Users (2025 Default Model)
**What:** Fixed annual base fee with included user tier + tiered additional user pricing.
**This is the DEFAULT construct for new deals from 2025 onwards.**
**When to use:**
- All new logos (default starting point)
- Renewals transitioning to 2025 pricing model
- Edition upsells (Essential → Premium → Signature)
- When managed hosting should be embedded (not a separate line)
**When to avoid:**
- Legacy contracts where block or per-user model is already negotiated and client resists change
- Very small deals where base fee exceeds reasonable spend
**Mechanics:**
- Fixed base fee (e.g., $494K for Essential, $607K for Premium, $787K for Signature)
- Includes first 20,000 users in base fee
- Additional users at tiered rates (rate decreases as volume increases)
- Example tiers: $6.52/user → $3.20/user → $1.02/user
- Managed hosting is embedded in the base fee
- Only the additional user rate is discountable — base fee is fixed
**Optics:** Simple, predictable. Client knows base cost + marginal cost per additional user. Natural upsell path between editions.
**Negotiation note:** The base fee is NOT discountable. Only concede on additional user tiers. This anchors the deal at a healthy floor.

## 1. Flat Block Pricing
**What:** Fixed price per block of users (e.g., $250K per 100K-user block).
**When to use:**
- Renewal with stable/growing usage
- Client wants audit simplicity (no per-user counting)
- Backbase wants ARR predictability
**When to avoid:**
- Rapidly declining user base (client overpays for unused capacity)
- Very early stage where user count is uncertain
**Mechanics:**
- Blocks are pre-purchased (e.g., 3 blocks = 300K users for $750K)
- When usage crosses a block boundary, next block kicks in automatically
- Optional: annual true-up vs. real-time block activation
**Optics:** $/user decreases as users grow within a block (good for client story).

## 2. Milestone-Based Ramp
**What:** Reduced rates in early years, full pricing at adoption maturity.
**When to use:**
- New logo or expansion where adoption is gradual
- Client has budget approval constraints (lower Y1 spend)
- Competitive pressure (low entry price to win)
**When to avoid:**
- Renewal where client is already at scale (why discount?)
- Client with history of delaying adoption to extend discounts
**Mechanics:**
- Year 1: 70% of full rate
- Year 2: 85% of full rate
- Year 3-5: 100% of full rate
- Multiplier applied to base per-user or per-block rate
**Optics:** Rising costs each year (manage narrative: "aligned to value delivery").

## 3. All-You-Can-Eat (AYCE)
**What:** Flat annual fee regardless of user count.
**When to use:**
- Client is extremely audit-averse
- Usage trajectory is uncertain
- Simple optics needed for board approval
**When to avoid:**
- High-growth client (Backbase misses upside)
- Low usage client (they're overpaying — retention risk)
**Mechanics:**
- Fixed annual license fee (e.g., $1.5M/year for 5 years)
- Optional: user cap with overage rate for extreme growth
**Optics:** Simplest possible pricing. $/user decreases as users grow (good client story).

## 4. Floor + Kicker
**What:** Guaranteed minimum ARR with per-user kicker above a threshold.
**When to use:**
- High-growth market where user ramp is expected but uncertain
- Backbase wants ARR protection while giving client growth optionality
- Transition from fixed to variable pricing
**When to avoid:**
- Stable/declining market (floor is all you'll get)
- Client resists variable components (prefers fixed certainty)
**Mechanics:**
- Floor: $1M/year minimum (paid regardless of usage)
- Threshold: 500K users
- Kicker: $1.50/user above threshold
- Revenue = max(floor, floor + (users - threshold) * kicker_rate)
**Optics:** "You only pay more when you're succeeding" — easy sell.

## 5. Dual-Track
**What:** Separate pricing tracks by segment or channel.
**When to use:**
- Multi-segment deals (retail + business + wealth)
- Different channels launching at different times
- Segments have very different unit economics
**When to avoid:**
- Single-segment deal (unnecessary complexity)
- Client wants pricing simplicity
**Mechanics:**
- Track A (Retail): $2/user, all years
- Track B (Business): $8/user, starting Year 2
- Track C (Wealth): $25/advisor, starting Year 3
- Total = sum of all track revenues
**Optics:** Transparent cost allocation by business line.

## 6. Cross-Sell Bundle
**What:** Bundled pricing for multiple modules at a discount vs. standalone.
**When to use:**
- Upsell / expansion with new modules
- Client is price-sensitive on individual line items
- Backbase wants to increase platform stickiness
**When to avoid:**
- Client only wants one module (forced bundling feels aggressive)
**Mechanics:**
- Digital Banking: $3/user
- Identity: $100K/year
- Banking Premium: $1/user uplift
- Bundle discount: 10-15% off combined standalone
**Optics:** "More for less" — client gets more value, Backbase gets higher total ARR.

## 7. Regional Structure
**What:** Entity or jurisdiction structuring for tax/optics optimization.
**When to use:**
- Multi-country deals with different tax regimes
- Client wants to optimize VAT/withholding tax impact
- Backbase has entity in favorable jurisdiction
**When to avoid:**
- Single-country deal (no benefit)
- Client's compliance team resists complex structures
**Mechanics:**
- Uses dual-track mechanics internally
- Different entity billing (Backbase EU vs SG vs US)
- Transfer pricing considerations
**Optics:** Same total cost, better tax treatment.
