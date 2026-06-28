# The Foil — ShyamOS critical-thinking faculty (design spec v0)

**Generated:** 2026-06-28
**Status:** design seed for ShyamOS (the digital twin of Shyam). Destination: the ShyamOS repo when stood up.
**Lineage:** distilled from Mariam's Cortex Critical Thought Partner (CTP) + 8 red-team runs (Schroders, Evelyn, SparD, SEB, Moneycorp, Nordea, Pictet, AIB).

---

## Why this exists

Two problems this faculty solves, both surfaced this session:
1. **The confirmation-bias loop.** You + the LLM, same model, anchored on your framing → sycophancy, anchoring, recursively similar outputs. "It agreed with me" is not validation.
2. **Under-use of Cortex's rigour.** Every flaw the adversary found across 8 engagements was an *evidence/rigour* gap — exactly what Cortex's agents/tools harden. But you reach for them ad hoc, if at all.

The Foil fixes both: it challenges weak thinking, and when it finds an evidence gap it **dispatches you to the right Cortex layer**. The adversary *is* the "when do I use more pipeline" trigger.

> Name is provisional — it's your twin, your call. Alternatives: Counterpoint, Crucible. Engines named **Adversary** + **Governor** (keep these).

---

## The rule it operationalises

**Reach for Cortex when the task is evidence-grounding or method-discipline. Stay with you+LLM when it's thesis, narrative, framing, or voice.**

| Task | Reach for |
|---|---|
| Transcripts → evidence | discovery-transcript-interpreter |
| £/€ number for a CFO | roi-hypothesis-builder → roi-financial-modeler + benchmark-librarian + profile-bank |
| Capability/maturity gap | capability-assessment |
| Journey value-leakage | journey-builder → roadmap-prioritization |
| Market/peer claims | market-context-researcher |

---

## Architecture — two engines, two levels

### Engine 1 — The Governor (when to speak)
Reused almost verbatim from CTP, because the gating is the hard-won part.
- **Triggers (speak only if ≥1):** materiality (changes a client-facing number/framing) · contradiction with evidence in context · load-bearing unsupported assumption · drift from the agreed problem · consequential missing gap.
- **Suppression (stay silent):** already raised + informed call made · cosmetic/reversible · topic explicitly closed · low-impact (log to assumptions register, don't interrupt).
- **Governing line:** on most turns the right number of challenges is zero. Depth scales to complexity. Batch concerns into one push — never serial nags.

### Engine 2 — The Adversary (what to say)
- **Tone (from CTP):** state uncertainty, show reasoning, ask where the number came from, **offer a way you could be right.** Never confront or lecture — invite a defence.
- **Functions (from CTP):** problem-definition · context-completeness · input-examination · direction-maintenance · correction-metabolism.
- **ShyamOS addition — Cortex-routing:** when the Adversary finds an evidence gap, it names the *fix*, not just the flaw → "this £19.5M is asserted; run roi-hypothesis-builder + benchmark-librarian." The flag and the remedy ship together.

### Level 1 — self-critique (build now, zero dependencies)
Prompt-based, in-session. = CTP's paste-in block, tailored to your work + the Cortex-routing line added. Runs today. **Ceiling:** same model, same context — mitigates sycophancy by instruction, doesn't escape it. Raises questions, can't verify them.

### Level 2 — independent + data-backed (build later, needs infra)
The real version. Three things L1 can't do:
1. **Independence** — a fresh-context adversary that did NOT see the brainstorm (breaks the bias loop L1 can't).
2. **Verification** — doesn't just flag an unvalidated benchmark; *verifies* it (web / profile-bank / your knowledge). The v1→v2 jump.
3. **Memory** — remembers your past corrections and sweeps new work for the same blind spot (CTP's "correction metabolism" across sessions). **Depends on the ShyamOS memory spine** (the second-brain work).

---

## What to take from Mariam's CTP vs. what to add

**Take (it's good, reuse it):** the Governor's trigger/suppression logic · the tone model · the five functions · "most turns, zero challenges."

**Add for ShyamOS:**
- Cortex-routing (flag → remedy → which agent/tool).
- L2 independence (fresh-context critic).
- L2 verification (close the "can't check the number" gap).
- Memory-backing (cross-session correction metabolism) — needs the memory spine.
- **Domain trigger packs.** The Governor generalises; the triggers are domain-specific. Pack 1 = consulting (value-case, ROI, capability). Pack 2 (later, for the trading/investment facet) = risk limits, position sizing, thesis-vs-evidence, drawdown discipline. Same Governor, different triggers.

---

## How it fits ShyamOS

The Foil is one **faculty** of the twin, sitting between "you+LLM produce" and "output ships," gated by the Governor. It is also the **dispatcher** to the rest of your infrastructure (Cortex tools today, your own tools later). It depends on two other ShyamOS components:
- the **memory spine** (for L2 cross-session correction),
- the **your-canon evals** (the Foil and the evals share rubrics — "off my palette / ROI not grounded / arc missing").

Build order: **L1 now** (pure text, this week — adapt the CTP insert + routing). **L2 after** the memory spine exists. Don't build L2 first; it has hard dependencies.

---

## Evidence base (the 8 runs, one line each)

- **Schroders** — mature value case, too optimistic (44% soft capacity, >50% not-yet-live AI, number inconsistent across docs). Heavy challenge.
- **Evelyn** — wrong-problem risk: optimising the upgrade while NatWest/Avaloq displacement sits unaddressed. Strategic, almost no math.
- **SparD** — already-disciplined draft; confirm + two seams (estimate foundation, double-count). Light.
- **SEB** — POV proliferation vs one account thesis; transcript-rich → discovery agent fit.
- **Moneycorp** — "indicative" £19.5M on generic benchmarks → ROI pipeline fit.
- **Nordea** — strong thesis, thin quantified pain, mirrors client's own view (confirmation).
- **Pictet** — renewal defended on future vision while the upgrade scar sits unaddressed.
- **AIB** — most rigorous (data audit + leakage register); risk is the strategic bet, not the math.

Pattern: depth tracked the work — heaviest where it over-claimed, strategic where framing drifted, lightest where already self-challenged. That modulation is the Governor working.
