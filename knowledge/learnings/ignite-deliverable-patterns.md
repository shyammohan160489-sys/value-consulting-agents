# Ignite deliverable patterns + the output-harvest method

*How good outputs (yours or teammates') become repeatable assets — and the first worked application: the Ignite deliverable family. Sources: Glacier (business case), MyState (playback), SchoolsFirst (roadmap workshop).*

---

## Part A — the harvest method (how a "plonked-in" output gets absorbed)

When a strong output lands, run **dissect → triage → converge → promote**:

1. **Dissect** — pull it into: purpose/context · story arc (beat sequence) · value/logic engine (levers, math, scoring) · proof approach · visual pattern. Save the raw text extract + a digest.
2. **Triage** — tag it as one or more of: **Reference example** (show-me-how) · **Method** (reusable logic → knowledge) · **Template** (fillable structure) · **Skill candidate** (mechanizable, repeats ≥2–3×).
3. **Converge** — when 2+ examples share a pattern, distil the COMMON structure. One example = a note; three = codify.
4. **Promote** — example → method/template → skill, as the pattern proves itself.

**Where it lives:** raw extract + digest in `Engagement/[client]/`; converged patterns + methods here in `knowledge/learnings/` — the team's shared-memory layer, and **consultant-tier contributable upstream**, so this literally builds the shared team memory you don't have yet; skills in `.claude/commands/` once a pattern earns automation.

**The loop:** every output you plonk in → dissect + digest → check convergence with existing patterns → promote. The library compounds; it doesn't pile up.

---

## Part B — first application: the Ignite deliverable family

Three real customer outputs = three points in the Ignite lifecycle:

| Deliverable | Example | Signature structure |
|---|---|---|
| **Roadmap Workshop** | SchoolsFirst (US CU, 188 slides) | Exec brief & align → **Day 1** use-case prioritization (strategic/value lens) → **Day 2** feasibility deep-dive (what it takes from BB + from the client) → outside-in **multi-year roadmap** (Early Value → Growth → Scale, phased by quarter) → "what done looks like = a written proposal" |
| **Playback** | MyState (AUS, post-sell, 42 slides) | Strategy **"in your words"** (validated across 3 sessions) → **"where value leaks"** (THEIR numbers = the headroom) → opportunity cards: *what we heard → the move → **how others did it** (sourced peer proof)* → staged path |
| **Business Case** | Glacier (US, detailed) | Value levers × (**today → with Backbase → annual → 7-yr**) → **maturity uplift** (1.31→2.74 / 59 caps) → 7-yr economics (inv / net / NPV) → phased ask |

### The common DNA (the repeatable engine across all three)
1. **"Your strategy is our blueprint / in your words"** — anchor on the client's *own* strategy, mirrored back, validated across sessions. Not vendor-push.
2. **From→To, quantified with THEIR numbers** — the gap between today and ambition is the headroom.
3. **Discrete value levers** — each: today → with Backbase → benefit.
4. **"How others did it" — sourced peer proof** (BMO 81%, US Bank 26%, Canadian 81% containment…). Honour the v4.0 rule: sourced + attributed, never invented; directional ranges as framing only.
5. **Phased roadmap / staged path** — Early Value → Growth → Scale.
6. **Customer-lifecycle spine** — Acquire / Activate / Expand / Retain.

### Skill candidates (promote when ready)
- **Ignite Roadmap Workshop kit** — themes → use-case prioritization grid (value × feasibility) → 2-day flow → multi-year roadmap. *(SchoolsFirst = template.)*
- **Ignite Playback** — strategy-in-your-words → value-leak map → opportunity cards (heard → move → how-others-did-it) → staged path. *(MyState = template.)*
- **Ignite Business Case** — lever build (today→future→annual→7yr) → maturity uplift → 7-yr economics → phased ask. *(Glacier = template.)*

These map onto the team's existing Ignite agents (`workshop-preparation`, `ignite-workshop-synthesizer`, `usecase-designer`, ROI, `narrative-assembler`) — so these three decks are the **worked proof + signature-move library** for those agents, not net-new.

### Imbibe, don't build — the pipeline already does these
**Ignite Inspire** (workshop-driven: agent-0→7, prep + synthesizer + usecase + presentation + roi) and **Ignite Assess** (evidence-based: discovery→capability→roi→roadmap→assembly) already produce all three deliverable types. So do NOT build new skills — these decks are the *client-ready, polished* version; the pipeline produces the *scaffold*. The gap = the signature moves. Fold each into the named existing agent:

| Best practice (from the real decks) | Fold into |
|---|---|
| "In your words" — open by mirroring the client's strategy, validated across sessions | ignite-workshop-synthesizer · narrative-assembler |
| "How others did it" — pair every value claim with a sourced, attributed peer proof | benchmark-librarian · narrative-assembler |
| Headroom — frame the gap using the CLIENT's own numbers | roi-hypothesis/modeler · capability-assessment |
| Opportunity-card format (heard → move → how-others-did-it → staged) | agent-6-presentation / playback |
| 2-day flow + value×feasibility prioritization grid | workshop-preparation · usecase-designer |
| Maturity uplift as headline (1.31→2.74) + per-lever today→future→annual→7yr | capability-assessment · ROI output |

The 3 decks become the **few-shot exemplars** those agents reference. (A precise per-agent output-vs-deck gap audit is the deeper next pass.)

### Audit result (2026-06-30) — coverage of the 6 moves across the Ignite corpus
Grepped 30 agent/prompt files. **Verdict: the pipeline is strong on the *quantitative scaffold*, weak on the three *narrative/trust* moves that make these decks land.**

| Move | Where it's specified | Gap? |
|---|---|---|
| 1 In-your-words strategy mirror | only `ignite-workshop-synthesizer` (weak) | **GAP** |
| 2 Sourced peer proof in the narrative | only `roi-financial-modeler` (numbers, not the story) | **GAP** |
| 3 Headroom from the client's own numbers | **nowhere** | **BIGGEST GAP** |
| 4 Opportunity-card discipline (heard→move→proof→stage) | partial (`agent-1..4`, `capability-assessment`) | tighten |
| 5 2-day flow + value×feasibility grid | covered (`agent-0/3/6` + templates) | ok |
| 6 Maturity uplift + per-lever 7-yr economics | covered (`capability-assessment`, `agent-7-roi`, `narrative-assembler`, `roi-financial-modeler`) | ok |

**Priority fix:** fold moves **3 → 1 → 2** into `narrative-assembler` + `agent-6-presentation` + `ignite-workshop-synthesizer` (sourcing peer proof via `benchmark-librarian`). The quant agents (`capability-assessment`, `roi-*`) need no change — they already do the hard maths; they just don't *tell the story* the way these decks do.

**Fix applied (2026-07-01):** all three agents now carry a named **"Signature Moves"** section (headroom / in-your-words / peer-proof), each adapted to that agent's role, plus concrete reinforcements:
- `ignite-workshop-synthesizer` — Signature Moves block + Step 3 pain-point register reworked to **headroom columns** (client baseline → client target → gap), with a `(benchmark)` labelling rule.
- `agent-6-presentation` — Signature Moves block (opportunity-card discipline: heard → move → how-others-did-it → staged) + S15/S19 use-case card rules now require *what we heard* / headroom framing / *how others did it* peer proof.
- `narrative-assembler` — Signature Moves block naming the three moves and wiring them to existing machinery (value-leakage funnels + benefits case = headroom; transformation arc + vocabulary mirror = in-your-words; Act 4 "what good looks like" = peer proof), with the sourcing discipline made explicit.

Raw extracts: `Engagement/{Glacier,SchoolsFirst,MyState}/*_text_extract.txt`.
