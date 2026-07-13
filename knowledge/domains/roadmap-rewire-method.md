# Roadmap Reverse-Engineering & Banking OS Rewire — Reusable Method

**Status:** Reusable across **any** engagement where a client hands us a **roadmap, target solution, or strategy artifact** (their own deck, an EA paper, a transformation backlog, a phase-1/2/3 plan). Apply it whenever a client says some version of *"here's what we're planning — follow our roadmap, don't re-discover it."*
**Origin:** AIB Ignite, Jun 2026 — worked example in `Engagement/AIB/output/00_source_of_truth/AIB_Battle_Plan.html` §6 ("Their roadmap, rewired"). The steer that forced the method: Aiden (AIB) — *"they've already built a roadmap; don't come in greenfield as if they hadn't."*
**Pairs with:** [`banking-os.md`](../product/banking-os.md) (control-plane canon — what we rewire onto) · [`narrative-spine.md`](../design-system/narrative-spine.md) (From→To voice) · [`apa-matrix/README.md`](apa-matrix/README.md) (per-process agentic mapping) · the relevant LOB `product_directory_*.md`.

---

## 0. The thesis (advisory, never contrarian)

A client roadmap is the **visible tip** of a strategy chain. Don't take it at face value, and don't re-discover it from scratch — **trace each item back to the business outcome it serves, then rewire it onto Banking OS.** You keep *their* priorities and sequence; you add the AI layer for free and surface what they can't see.

> One-line: **"Same roadmap. Their priorities. Delivered on our OS — with the layer they'd otherwise hand-build, already in the box."**

Why this beats greenfield discovery: it respects that they've done the thinking (no "garage-load of consultants going over old ground"), it uses *their own words* as the business case, and it positions us as *"we play in all these places on your roadmap you may not be aware of"* — not as outsiders questioning their plan.

---

## 1. The strategy chain — reverse-engineer bottom-up

Most banks separate **corporate strategy** (board / CEO — *what the bank wants to become*) from **digital strategy** (CDO — *how digital serves that*), which cascades into **business priorities** (LOB / tribe leads) and finally the **roadmap** (product owners / squads). The split exists because each layer has a different owner and altitude.

Reverse-engineer **upward** from any roadmap item:

```
Roadmap item  →  Business priority / outcome  →  Digital-strategy pillar  →  Corporate-strategy ambition
 (the WHAT)         (the WHY)                      (the owner: CDO)            (the owner: board/CEO)
```

This gives you three things at once:
1. **The WHY** behind each item (the outcome the business actually wants).
2. **The DMU map** — who owns the rationale at each altitude (so you know who to ask the "why," and who actually decides).
3. **The ladder to the C-suite** — you can tie any feature back to a board-level ambition, so your value speaks the language of the person who signs.

> Probe the *why*, never question the *what*. You're tracing their rationale, not challenging their roadmap.

---

## 2. The method — seven steps

1. **Trace up.** For each item: item → why (priority/outcome) → digital pillar → corporate ambition. Note where the chain is *clear* vs *vague* — vagueness is where they need help (de-vague it *with* them, don't invent it).
2. **Extract the outcome in their words.** Use the rationale they wrote — *"FX leakage to competitors," "key customer frustration," "committed FTE benefit," "mitigate resource leakage."* Their words are your evidence; you quantify them, you don't manufacture pain.
3. **Map to Banking OS — neutrally.** For each outcome, the solution/layer that delivers it (Digital Banking, Conversational, Relationship Intelligence, Customer Ops, Nexus/Sentinel/Orchestration). Map to the *outcome*, not to a product you want to sell.
4. **Classify on two axes** (keep them separate — see §3):
   - **Strategic move** — the ambition ladder (e.g. *Foundation → Differentiate → Lead*): where this sits in their journey.
   - **Delivery** — *Adopt / Configure / Custom*: how much is OOTB. (The eval/assessment proves this.)
5. **Rewire, don't reprioritise.** Keep their sequence and priorities; overlay an *actionable* roadmap (timelines, feasibility) on top of theirs. Never tell them their roadmap is wrong.
6. **Surface what they can't see.** Two kinds of value beyond their roadmap: (a) the **leapfrog** items they'd never reach by hand (AI, conversational, intelligence) — for *them* a leap of appetite, for *us* OOTB; (b) the **now-native** capabilities added since their last version, which make their old custom redundant.
7. **Cede what's owned or better elsewhere.** If a roadmap item is already solved or owned (e.g. AIB credit = nCino), *don't pitch it* — cede the engine, keep only the honest adjacent play (signals, journey, experience). This is the anti-confirmation-bias guard: not everything maps to us, and a sharp client sees it instantly if you pretend otherwise.

---

## 3. Two axes — don't conflate them

| Axis | Question | Values | Proven by |
|---|---|---|---|
| **Strategic move** | What are they reaching for, and when? | Foundation · Differentiate · Lead *(or your set)* | the roadmap + the why |
| **Delivery** | How much is out of the box? | Adopt · Configure · Custom | the eval / capability assessment |

They're orthogonal — and the payoff line falls out of keeping them separate: *"even the boldest move is mostly **Adopt** — the leap is your decision, not our build."* (Note: "Adopt" here is the Backbase OOTB sense; if your strategic ladder also uses a word like "Adopt," **rename the ladder** to avoid the collision.)

---

## 4. The output artifact

A **"roadmap rewired"** table — one row per item:

| Their item | Priority (their words) | Business outcome | Rewired to Banking OS | Move | Delivery |
|---|---|---|---|---|---|

…plus an **actionable overlay**: our execution-friendly version with timelines and feasibility, presented as *"here's how we'd deliver your roadmap on the platform,"* not a replacement plan. (AIB §6 is the live template.)

---

## 5. Principles

- **Roadmap-led, not greenfield.** Anchor on their roadmap; don't re-run discovery they've already done.
- **Understand the why; don't question the what.** Trace rationale; never imply the roadmap is wrong.
- **Their words are the business case.** Quantify the pain they've already named.
- **Don't reprioritise — rewire.** Piggyback on their sequence and priorities.
- **Map to the outcome, then cede honestly.** Not everything is ours; ceding what's owned buys credibility for what is.

---

## 6. Limits — when reverse-engineering misleads (apply the critical lens)

- **Aspirational ≠ funded.** A roadmap item may be a wish, not a committed, resourced plan. Validate *real vs aspirational vs already-solved* before you build a case on it.
- **Political roadmaps.** Some roadmaps reflect internal negotiation, not true priorities. The *why* you reverse-engineer is a hypothesis — confirm it with the actual owners (the strategy chain tells you who).
- **The confirmation-bias trap.** The method's gravity pulls everything toward "Banking OS is the answer." Resist it: trace to the outcome *neutrally* first; cede where another system owns it or does it better.
- **Vague by design.** If items are deliberately fuzzy, de-vague them *with* the client — don't fill the gaps with your own assumptions and present them back as theirs.
- **A rewire is not a validation.** Mapping their roadmap onto our platform proves *fit*, not *appetite* or *commercial viability* — those are separate items to validate.

---

## 7. Worked example

**AIB Battle Plan §6** ("Their roadmap, rewired") — Phase 1/2/3 reverse-engineered to business priorities, rewired to Banking OS, classified on both axes. See also the same engagement for the *cede* discipline (credit → nCino) and the *validate* discipline (squad numbers, market figures) — both live applications of §6's limits.
