# ShyamOS — Architecture (v3, simplified)

**Generated:** 2026-06-28
**What it is:** the digital twin of Shyam — a complementary intelligence that extends the human across every facet (work, finance, marketing, ops, ethics, leadership), creates value *for* him and *in the world*.

> **Naming is a skin, not the structure.** The structure below is stable. The names are a light identity layer you can re-skin anytime (sci-fi, fantasy, Marvel, whatever) without changing a thing. Only the **key faculties** are named; smaller functions **nest inside** them.

---

## Principles

1. **MVP-first — never break what works.** Today's setup already functions; everything is an additive layer.
2. **Six faculties, not thirteen.** Group by job. If two want the same job, merge them.
3. **The twin extends, never replaces.** Authority flows from Shyam; the twin acts within mandate.
4. **Governance is the floor** — especially for money and outward action.
5. **No silent regressions.** Every change to a faculty passes the Foil's eval-gate before it ships (see Build discipline).

---

## The six faculties (+ you)

| Faculty | What it is | Nests | Autonomy |
|---|---|---|---|
| **You — the Principal** | intent, taste, final say | — | — |
| **the Mind** | what ShyamOS knows and *is* | **Persona** (model of you) · **Memory** (what happened) · **Playbook** (your methods + design system) | A4 recall / A2 write |
| **the Studio** | where work gets made — **Cortex lives here** | design system · skills · tools · **Modeler** (ROI/value math) | A4 |
| **the Foil** | the critic + quality gate | **Adversary** (challenges) · **Governor** (gates when it's worth it) · routes to rigour | A2 |
| **the Watch** | eyes outward & forward | **Scout** (senses now) · **Forecaster** (sees ahead) | A3 |
| **the Hands** | does things in the world | **Operator** (send/deploy/publish) · **Treasurer** (moves money) | A3 (A1 for money) |
| **the Warden** | the law (cross-cutting) | mandate · the A1–A5 autonomy dial · audit | sets the others' levels |

**Infrastructure (not faculties — just how it runs):**
- **the Console** — the interface where you command and get briefed (the MVP is Claude Code; graduate to a chat/voice/morning-brief later). Must do four things: **brief · command · approve · review.**
- **the runtime** — routes a request to the right faculties. (No "character" needed; it's the OS.)

```
  You ─ the Console (interface) ─ the runtime (routing)
        │
        Mind · Studio · Foil · Watch · Hands
        │
        the Warden  (governance wraps all of it)
```

That's it. Six faculties, one of which (the Studio) is where your current Cortex craft lives — so the MVP already runs faculties 1–3 in basic form today.

---

## Life-domains × faculties (one grid, not a system per domain)

Faculties are horizontal; your life-domains are vertical. The same six serve all of them:

| Domain | Served by |
|---|---|
| Finance (personal) | Treasurer + Modeler + Watch, under the Warden's risk limits |
| Marketing | Studio (content) + Mind/Persona (voice) + Watch (trends) + Hands (publish) |
| Operations / execution | Hands + runtime + Warden |
| Ethics | Mind/Persona (values, red lines) + Warden (guardrails) + Foil |
| Leadership | Mind/Persona + Mind/Playbook (methods) + Foil (pressure-test) |

**Ethics and leadership aren't components — they're encoded in the Persona and enforced by the Warden + Foil.** That's why the Persona is the must-have: it's where your character lives.

---

## Build discipline (the dev/eval principle, adopted — not the hooks)

The team made their bb-* harness + evals *mandatory* for a real reason: a document factory has no compiler, so **the eval suite IS the compiler** — a change to an agent/skill can silently regress quality and nothing catches it. That principle is worth keeping; the *hooks* that enforce it in the team repo hamper how you work, so we don't adopt those.

- **In the team repo:** skip the gating hooks. (Reminder: *"skip all"* = none of bb-*/evals in your repo; *"files only"* = the files present but hooks off. We're doing files-off-hooks, keeping only the eval **rubrics** as reference.)
- **In ShyamOS:** adopt the *principle* as law — **no faculty change ships without passing the Foil's eval-gate.** The gate lives in the Foil; the Warden enforces it. Upstream's "final-check rubric — before any output goes out" (see `knowledge/reference/banking-os-v4-DELTA.md`) is a ready seed for that rubric.

---

## Absorb from the team's pipeline (don't run it — imbibe it)

You don't run the team's assessment pipeline or bb-* harness — but they're a **library of methods, standards, and memory-patterns** worth absorbing as ShyamOS faculties. Not used today ≠ not wanted tomorrow.

| Team asset | What it really is | Lands in | Phase |
|---|---|---|---|
| **20 eval rubrics** (assumption_discipline, conservative_bias, evidence_grounding, report_tone, design_quality, value_leakage_quantified, benchmarks_defensible…) | the codified consulting quality bar — and it *matches your own values* | the **Foil's eval-gate** (merged with your feedback memories) | 1 |
| **3 eval altitudes** (deliverable · component · pipeline) | output-level + faculty-level checks | how the Foil grades | 2 |
| **18 agents** (discovery, capability, ROI 4-link, journey, roadmap, narrative-assembler…) | a library of rigorous methods | callable by the Studio/Modeler, routed by the Foil — **on demand, not mandatory** | 2 |
| **CLIENT_PROFILE + ENGAGEMENT_CONTEXT/JOURNAL** (persists across engagements) | structured persistent client memory | the **Mind/Vault** — also unlocks the Foil's cross-session drift-catching | 1 |
| **Langfuse tracing** | observability of runs | the Console's "review" + the Warden's audit | 2 |
| **telemetry → backlog → improve** (intake-only) | a learning loop | ShyamOS's **learning loop** (corrections → Persona + Playbook) | 2–3 |

Principle: **absorb the parts as on-demand capabilities; never adopt the mandatory pipeline.** The eval rubrics are the concrete seed for the "your-canon evals" deep-mechanic — and they *converge* with your own values (conservative_bias = your conservative ROI; evidence_grounding = your verify-don't-repeat; report_tone = your humanise/less-is-more). So the harvest (#6) becomes: your feedback memories + these 20 rubrics → the Foil's standards.

## Roadmap (MVP-first, additive)

- **Phase 0 — MVP (works, don't touch):** You + the Studio (Cortex) + the Mind (basic — your knowledge + memory files).
- **Phase 0.5 — Stabilise (DONE):** repo clean + backed up, additive bits adopted, junk ignored.
- **Phase 1 — now:** Foil L1 (runnable today) · the Mind proper (Persona v0 + Memory spine) · Warden v0 · your-canon evals.
- **Phase 2 — needs the Mind:** Foil L2 (independent, verifying) · the Watch · the runtime (real routing) · the Modeler.
- **Phase 3 — new powers, under the Warden:** Forecaster · Treasurer (money, A1) · the Hands (action).

**Still open / to decide later:** the Console surface (which interface), and the learning loop (corrections flow back into Persona + Playbook — your own flywheel).
