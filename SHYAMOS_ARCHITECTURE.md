# ShyamOS — Architecture & Roadmap (v2)

**Generated:** 2026-06-28
**What it is:** the reference architecture + phased roadmap for ShyamOS — the digital twin of Shyam: a multi-modal, complementary intelligence that extends the human, creates value *for* him (incl. capabilities he lacks today, e.g. investing), and value *in the world* (consulting + IP).
**Naming:** contemporary, with a light thread of character. The medieval "small council" was a useful sketch; this is it in working clothes. **Adversary** and **Governor** kept — they were right.

---

## Principles

1. **MVP-first — never break what works.** The current setup (your judgement + Cortex craft + knowledge) already functions. Every layer below is *additive*. None replaces the MVP.
2. **The twin extends, never replaces.** All authority flows from Shyam (the Principal). The system advises and acts *within mandate*; he keeps taste, intent, and final say.
3. **One responsibility per component** (MECE). If two want the same job, the design is wrong.
4. **Governance is the floor, not a feature** — especially for money and outward action. Autonomy is granted per component, never assumed.
5. **Memory is the keystone.** Most of the intelligence depends on it. Build it early.

---

## The components (contemporary)

| Component | Function | Autonomy (A1–A5) | (court sketch) |
|---|---|---|---|
| **Shyam — the Principal** | intent, mandate, taste, final say | — | Sovereign |
| **Chief of Staff** | orchestration — route a request to the right components, sequence, synthesise one answer | A4 | the Hand |
| **the Vault** | memory — identity, every engagement, decision, correction, the corpus of work | A4 recall · A2 write | Chronicler |
| **the Persona** | the model of *you* — taste, voice, values, red lines, decision-style. What makes it a *twin* | reference (read by all) | (new — was a gap) |
| **the Playbook** | canon — methods, design system, narrative spine, pricing methodology, domain knowledge | A4 | Loremaster |
| **the Studio** | production — forge the artifacts (decks, docs, models, prototypes). **Cortex lives here** | A4 | Artificer |
| **the Foil** | critique — **Adversary** generates the challenge, **Governor** gates when it earns the interruption; dispatches to rigour on an evidence gap | A2 | (kept) |
| **the Scout** | intelligence — outside-in market/client/competitor signal, verification, stakeholder map | A3 | Whisperer |
| **the Forecaster** | foresight — scenarios, prediction, timing. Most bias-prone; never speaks without the Foil | A1–A2 | Oracle |
| **the Modeler** | quantification — ROI, value math, pricing | A3 | Master of Coin (deals) |
| **the Treasurer** | personal capital — investing, "make money work" (your Privy Purse) | A1 → earns up | Master of Coin (money) |
| **the Operator** | action — send, schedule, deploy, trade, within mandate | A3 | Steward |
| **the Warden** | governance — the mandate, the autonomy dial, the audit trail, hard guardrails on money & outward action | sets everyone's level | Justiciar |

---

## Layers

```
  Principal      Shyam — intent, mandate, taste, final say
      │
  Command        Chief of Staff — orchestration
      │
  Cognition      Vault · Persona · Playbook · Scout · Forecaster · Modeler · the Foil
      │
  Production     the Studio — the forge   ◄── Cortex resides here
      │
  Action         the Operator — execution into the world
      │
  ──────────────────────────────────────────────────
  Governance     the Warden — mandate · autonomy (A1–A5) · audit   (wraps Command→Action)
```

Cortex is **not** ShyamOS — it's the Studio *inside* it. You keep its craft; it sits as one layer under a twin that also remembers, knows *you*, senses, foresees, critiques, governs, and acts.

---

## The roadmap — MVP-first, additive, phased

**Phase 0 — the MVP (already works · DO NOT TOUCH).**
= the Principal + the Studio (Cortex) + the Playbook (your knowledge) + a basic Vault (your memory files & engagement folders). This is how you work today, and it functions. Everything below is an additive layer.

**Phase 0.5 — Stabilise the base (the backlog · do first).**
Tidy the workshop before adding wings — and this does **not** change how output is produced: repo clean-up (commit the working tree, keep Frontline 2026, adopt the additive upstream bits — question bank, Pictet ref deck, Banking OS v4.0 as *reference*), skip the dev/eval layer. This is the decided-but-unexecuted backlog. Foundation, not enhancement.

**Phase 1 — Judgement + memory + self (now, low barrier).**
- the **Foil L1** (Adversary + Governor, pure text, runnable this week)
- the **Vault** proper (memory spine / second-brain — the keystone)
- the **Persona** v0 (start capturing your taste/voice/red-lines — build it *with* the Vault)
- the **Warden** v0 (write the mandate + autonomy dial before anything can act)
- **your-canon evals** (the deep-mechanic backlog item — the Studio's quality bar + the Foil's standards)

**Phase 2 — Sensing + orchestration (needs the Vault).**
- the **Foil L2** (independent, verifying, memory-backed)
- the **Scout** (wire in research/profile tools)
- the **Chief of Staff** (real routing across components)
- the **Modeler** (deliberately adopt Cortex's ROI/pricing tools)

**Phase 3 — The new powers (highest value + governance, born under the Warden).**
- the **Forecaster** (foresight)
- the **Treasurer** (personal investing — the "make my money work" ambition; starts A1)
- the **Operator** (action/execution; outward actions gated A3)

Trust is earned **per component, over time** — graduate A2→A3 on track record, never by default. Exactly how you'd advise a bank to roll out agents, applied to yourself.

---

## What you're missing (the architect's gap pass)

1. **The Console — where you actually command the council.** Lots of faculties, no defined *interface*. Today it's Claude Code in a terminal; that's fine as MVP, but ShyamOS needs one consistent surface (chat / voice / a morning dashboard) — the throne room. Biggest practical gap; decide the surface before you scale the components.
2. **The Persona — the model of *you*** (now added above). The Vault stores *what happened*; nothing yet encodes *how you think* — your taste, voice, values, red lines. Without it, it's a sharp assistant, not a twin. This is the defining piece; build it alongside the Vault in Phase 1.
3. **The learning loop.** How does it get *better at being you*? Corrections must flow back into the Persona + Playbook — your own flywheel (the thing Cortex's evals do for the team). Otherwise it plateaus.
4. **Security & privacy boundary.** It will hold your life, clients' confidential data, and your money. The Warden owns this — flag now: data isolation, and the impersonation line (it *amplifies* you; it never *poses* as you outward without approval).

---

## A day in the twin's service

> Morning: the **Scout** has read overnight — a competitor move at Pictet, an org change at AIB, two market shifts touching your Privy Purse. The **Forecaster** flags one deal trending to slip and one position drifting past its risk band. The **Chief of Staff** convenes: the **Playbook** supplies the method, the **Persona** keeps it sounding like *you*, the **Studio** drafts the response on-brand, the **Foil** red-teams it before coffee and routes one number to the **Modeler** because it was asserted, not evidenced. The **Treasurer** proposes a rebalance; the **Warden** holds it at "recommend" — it's money — so it waits for your nod. You glance, approve two, kill one. The **Operator** sends and schedules. The **Vault** logs all of it — so tomorrow the twin is sharper, and in six months the Foil catches the mistake you were about to repeat.

Not a faster typist — a council that lets one person operate like ten, without losing the one thing that's yours: your judgement.
