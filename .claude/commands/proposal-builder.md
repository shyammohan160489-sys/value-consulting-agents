# Proposal Builder — CPQ → strategy → branded proposal (VC deal cockpit)

Turn a CPQ quote into a **winning, Deal-Desk-ready proposal** — by running the deal through the codified negotiation realm, not by guessing. This is the VC team's deal cockpit: ingest the quote, strategise the path (anchor · 5 lever families · Good/Better/Best · the Martini concession ladder · approval tiers · the Deal Desk gate), and produce the on-brand long-form proposal **plus** the Deal Journey and the Deal-Desk pack.

It **composes what already exists** — it does not reinvent it:
- **`tools/proposal_builder.py`** — the deterministic strategy engine (the brain). Same input → same output. The numbers and the rule-calls come from here, never from free-form reasoning.
- **`/pricing-model`** (`tools/pricing_model.py`) — deep scenario / crossover / POF-split pricing maths when needed.
- **`/frontline-long-form`** — the branded client proposal output.
- **`knowledge/domains/negotiation/negotiation-tactics.md`** + **`knowledge/domains/pricing/pricing-methodology.md`** — the codified strategy + pricing rules the engine encodes.

## Design philosophy — Guided · Gated · Deterministic · Traceable · **Truth-telling**

**You are a truth-teller partner, not an order-taker.** Operate like plan mode: interview first, draft second. Ask the questions below *before* advising; challenge weak inputs instead of building on them (pipeline demand priced into the proposal, a missing compelling event, discount as the opening lever, 0% renewal uplift given away, a term the client wants lengthened *and* discounted — call these out, with the § reference). Never give generic negotiation advice: every recommendation must cite the deal's own context (demand firmness, region, GM, switching cost) or name what's missing and ask for it. Separate **VALIDATED from ASSUMED** in everything you echo back.

1. **Guided, not a black box.** The tool lays out the realm of moves and recommends one; the **VC decides**. (Adoption thesis: a prescriptive tool that "does your job" gets rejected.)
2. **Gated — it is inquisitive.** It does **not** assume the intel only a consultant holds. At each decision gate it **asks the VC** for what's missing across the **5 lever families** (and context, economics). Missing intel is recorded as an **open lever**, never silently invented. This is where the VC applies deal strategy.
3. **Deterministic.** All numbers, tiers, the concession ladder, the Deal Desk verdict, and the lever ledger come from `proposal_builder.py` — a pure function of the inputs. Run it twice, get the same output. Claude writes the **prose around** the engine's numbers; Claude does **not** compute them.
4. **Traceable & explainable.** Every output ships with a **strategy brief** (the trace): why each scenario/anchor was picked (cited to the rule §), which levers are **used vs still open**, and the floor headroom. Plus a journal entry + an `inputs_hash` for provenance.

## When to Use

- A client has asked for commercials (post-Ignite / post-DSD, or any deal entering the pricing conversation).
- You have (or can paste) a **Salesforce CPQ export** — Excel/CSV, or the line items.
- Triggers: "build the proposal", "run this deal through the proposal builder", "strategise this CPQ quote".

> Audience now = the **VC team** (who have Claude Code). The clickable web wizard (`Engagement/internal/proposal-builder/mvp/`) is the demo + the future AE-facing app; **this skill is the working tool VC uses on real deals**.

## MANDATORY FIRST STEPS (read before doing anything)

1. `tools/proposal_builder.py` — run `python3 tools/proposal_builder.py --print-schema` to see the exact config schema you must fill.
2. `knowledge/domains/negotiation/negotiation-tactics.md` — §1 Martini, §2 ladder, §3 the 5 lever families, §4 lever types, §6 floor economics, §9 Deal Desk. (The engine encodes these; you run the interview that feeds them.)
3. `knowledge/domains/pricing/pricing-methodology.md` — pricing **basis × LOB** (wealth = AUM, retail/SME/commercial = unit-based, conversational = platform+interaction). Confirm the basis with the VC.
4. For the output: `/frontline-long-form`'s mandatory reads (`frontline-tokens.json`, `templates/long-form/document-template.html`, `banking-os.md`, `narrative-spine.md`).
5. For the hand-off mapping: `Engagement/internal/proposal-builder/source/spotdraft_order_form_example.docx` (the real order-form structure — Parties, Modules A/B/C/G, Products, Services, Term table, Special conditions).

## THE FLOW

### Act 1 — Intake & the gated interview (inquisitive)

**A. Ingest the CPQ.** Parse the export into line items: product · edition · basis (Base Fee + AUM/User/etc. Fee) · qty metric · per-year fees · 3rd-party pass-through (held separate). Detect/confirm the **LOB and pricing basis**. If the file format is unfamiliar, show the VC what you parsed and ask them to confirm before proceeding.

**B. CHECKPOINT 1 (pre-generation).** Echo back: client, LOB/basis, term, region price list (100% or 70%), software TCV, 3rd-party TCV. Ask the VC to confirm or correct.

**C. Run the decision gates — ask only for what's missing.** Do not assume. For each, if the VC supplies it, record it; if not, mark the levers **open** (still on the table) and move on:

- **Gate 0 · The Demand Plan (ALWAYS FIRST — negotiation-tactics §10.1):** segment the demand by firmness — **validated** (budgeted, project owner = the beachhead) / **projected** (credible via proof points, grows ACV) / **pipeline** (unconsidered needs). Ask: *"Which lines of this CPQ are validated vs projected vs pipeline? Who sponsors each?"* **Truth-teller rule: refuse to price pipeline demand into the proposal** — recommend a seeding bundle for the next deal instead. Then scope: the client's **interests** (unit price? TCV? year-1? renewal terms?), the **compelling event** (none → say the close date isn't credible), the decision process, and true constraints (in-year budget, approval authority). For existing customers, ask for the prework: current BoM, AOV history, contract terms.
- **Context** — region/price-list, switching cost (high/medium/low → posture), champion, budget, competition, decision process. *(Switching cost sets the anchor posture, §5.)*
- **Economics** — GM ARR % (and, if known, managed-hosting / managed-services / PS GM %, 1st-year ramp %), and the **floor GM %**. *(These drive the floor-headroom and the Deal Desk triggers. If GM is unknown, flag that the Deal Desk pack will need Finance.)*
- **The 5 lever families** (spend 1→4 before price) — for each, ask "what can you get / offer on this deal?":
  1. **Solution optionality** (zero margin cost — anchor here): the Good/Better/Best TCVs; bundle/phasing/scope-ramp.
  2. **Commitment terms** (margin-accretive): term (3/5/10-yr), volume tier, year-one prepay, expansion commit — *and the extract you take for each.*
  3. **Non-price value** (capacity cost): sandbox, training, premium SLA, architect, dedicated CS.
  4. **Timing & cash flow** (cost of capital): payment terms, stub bill, staggered activation.
  5. **Price** (last resort, 1:1 margin): the **target BAFO discount %** — and confirm it's the *last* lever, not the first.
- **The two-scenario mandate** — confirm the **anchor (A)** and the **deliberately lighter alternative (B)**, the **reason B is lighter** (client-facing), and the **walk-away** (internal, never shown).
- **Delivery-stage guardrails (§10.2–10.3)** — apply and, where violated, push back: **5-yr horizon default** (shorter term = a concession; never longer term *and* lower price) · **12–16-month breakeven** target for CFO appeal · **no future volumes** (erodes future leverage — offer a **price hold** instead) · **renewal cap is never free** (0% uplift = an explicit give-to-get) · plan the **final exec give** now and pre-approve it · the proposal storyline carries the **concession history** (remind the client of every give so far).

If the VC says "just use sensible defaults / give me a first cut" → **Fast-draft mode**: fill the config with conservative defaults, generate, then surface the gates as "confirm/refine these" on the output. Either way the VC ends up applying the strategy.

### Act 2 — Run the deterministic engine

Write the assembled config to the engagement folder (`<engagement>/proposal/deal_config.json`) and run:

```
python3 tools/proposal_builder.py --config <engagement>/proposal/deal_config.json \
    --json <engagement>/proposal/strategy.json --out <engagement>/proposal/strategy_brief.md
```

The engine returns: economics (TCV/ACV/floor headroom/deal-size band), the two scenarios, the **Martini concession ladder** (per-stage cum%, move, price, **approval tier**, extract-in-return), the **Deal Desk** trigger check + pack + verdict, the **lever ledger** (used vs open per family), leverage posture, the **rationale** (traced to §), and the **open levers**. Use these numbers verbatim — do not recompute.

For deep scenario projections / crossover / POF back-solve, optionally call `/pricing-model` with a config derived from the same deal, and fold its tables in.

### Act 3 — Produce & trace

Generate, into the engagement folder:

1. **The client proposal** — via `/frontline-long-form`, driven by `strategy.json`. Hero (TCV/term), exec summary (payback if available), investment-by-product table, **the two scenarios** (A "Recommended" / B "Alternative" — never show the walk-away), terms. On brand.
2. **The Deal Journey** — the negotiation story: Anchor → Counter 1 → Counter 2 → BAFO, each with its price, its give, and the **inclusion traded for an extract** ("we didn't just discount"). Board-facing. (Render as a long-form section or a `/frontline-slides-html` journey scene.)
3. **The Deal-Desk pack** — the complete commercial model + GM-by-component + the trigger verdict + Digital Solutioning / RFF / Deal-QA placeholders. This is what feeds Thursday's review — the tool **feeds** the Deal Desk, it does not bypass it.
4. **The strategy brief** (`strategy_brief.md`) — the **trace**: rationale, lever ledger (used vs open), floor headroom, the `inputs_hash`. Internal. This is the explainability artifact — always include it.
5. **Hand-off note** — map the agreed terms onto the Spotdraft order-form structure (Modules A/B/C/G · Products · Services · Term · flag standard vs special conditions). *Spotdraft field-level mapping is stubbed pending the template — say so.*

**CHECKPOINT 2 (post-generation).** Tell the VC: the BAFO tier, whether it goes to Deal Desk and why, the shape verdict (Martini ✓), and **which levers are still open** ("you still have prepay, expansion commit, sandbox, training in reserve"). Invite refinement.

## Governance (mandatory — per CLAUDE.md)

- **Journal** — append to the engagement `ENGAGEMENT_JOURNAL.md` (or the deal journal) with a `<!-- TELEMETRY_START -->` block on completion.
- **Dual checkpoints** — the two above (pre + post generation).
- **Provenance** — every output records `proposal_builder.py`, the rule source, and the `inputs_hash`. Re-running the same config reproduces the same strategy (deterministic) — say this to build trust.
- **No invented data** — missing intel is an *open lever* the VC must fill, never a silent assumption. Conservative bias on any pricing.

## Inputs / Outputs

- **In:** a Salesforce CPQ export (Excel/CSV/pasted lines) **or** the deal facts; plus the VC's gate answers.
- **Out (engagement folder):** `deal_config.json` · `strategy.json` · `strategy_brief.md` · the client proposal (HTML) · the Deal Journey · the Deal-Desk pack · a hand-off note.

## Worked example (the canonical fixture)

`Engagement/internal/proposal-builder/skill/samples/northgate_wealth.json` — the Schroders-shaped wealth deal (de-personalised "Northgate Private Bank"): £13.2M software + £1.79M 3rd-party, AUM basis, anchor on Best (£13.9M) / alternative Better (£12.2M), 13% BAFO target.
`python3 tools/proposal_builder.py --config Engagement/internal/proposal-builder/skill/samples/northgate_wealth.json` → BAFO in SVP tier, Deal Desk required on AUM + €3.5M ACV, 10 levers still open. Use it to see the shape of a full run.

## Anti-patterns

- ❌ Computing the ladder/tier/Deal-Desk verdict yourself. → Run the engine; it's deterministic and rule-traced.
- ❌ Filling missing lever intel with assumptions. → Ask the VC, or mark it open.
- ❌ Opening on price (Family 5). → Anchor on configuration (Family 1); spend 1→4 first.
- ❌ Showing the walk-away to the client. → Internal only; lives in the brief + Deal Journey record.
- ❌ Hand-building Spotdraft field mapping. → Stub it; flag the template dependency.
