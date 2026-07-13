# Does autonomy level correlate with cost? — testing the pricing hypothesis

**Status:** Internal / 1:1. The analytical bridge between the [autonomy framework](../agent-autonomy-framework.md) (value/demand side) and [Mayur's cost model](mayur-conversational-cost-model.md) (compute/supply side).
**The question (Shyam):** *If I reclassify agents by autonomy level instead of by use case, (a) is the pricing materially the same, (b) is there a direct correlation between autonomy and token/compute/interaction consumption? If the correlation is direct, the model is validated.*

---

## Verdict in one paragraph

**The correlation is real — but not on the axis the naive version of the pitch assumes, and that distinction is the whole game.** Mayur's data shows **per-interaction cost is roughly flat (~$0.037–0.040)** and is **not monotonic in autonomy**: his higher-autonomy "Money Movement" (an *action*) uses **fewer** model calls than the lower-autonomy "Chat to my finances" (a *query*) yet costs ~7% more. So *"higher autonomy ⇒ more tokens per interaction ⇒ charge more per interaction"* is **not supported** — and pitching it that way gets shot down by this very sheet. **What IS supported:** cost rises with autonomy through (1) reasoning/tool model tier + tokens *per step*, (2) steps *per outcome*, and (3) — decisively — **interactions consumed *per resolved outcome*.** That means: **per-interaction pricing is correct and materially unchanged for A1–A3 (the autonomy relabel is free), and it structurally *under-prices* A4–A5, which is exactly where the unit must move to per-outcome.** Your model doesn't contradict Mayur's — **it extends it precisely where his runs out.**

---

## 1. The evidence (from Mayur's two use cases, n=2)

Mapping his use cases onto the Frontline Autonomy Scale:

| Use case | Autonomy level | Conv-Banking verb | Model calls | Tokens (in→out) on the costly call | **Cost / interaction** |
|---|---|---|---|---|---|
| Chat to my finances | **A1 Assist** | Assist (answer) | 5 | 5,000 → 1,000 (×1) | **$0.0370** |
| Money Movement | **A3 Execute-on-approval** | Transact (action) | 2 | 5,800 → 1,000 (×2) | **$0.0395** |

Two facts that kill the naive correlation:
1. **Fewer calls, higher cost.** A3 has 2 calls vs A1's 5, but costs more. The supporting purposes that pad A1's count (embedding, guardrails, online evals) run on **mini/nano models and are nearly free**. Cost concentrates in the **reasoning / tool-calling** call on the full model.
2. **Per-interaction cost is flat** (ratio 1.07). This is *why a single $0.07/interaction sell price works across use cases* — and why a per-interaction sell price is **blind to autonomy by construction.**

> Caveat stated plainly: **n = 2.** This is directional, not proven. The recommendation in §4 is to model 3–4 more use cases spanning A1→A5 before treating any of this as settled.

## 2. Why the correlation is real anyway — the three channels

Cost *does* climb with autonomy, but through channels a per-interaction snapshot hides:

| Channel | What rises with autonomy | Visible in Mayur's model as |
|---|---|---|
| **A. Reasoning per step** | Bigger context, more tool schemas, planning, self-correction | tokens/call + the reasoning/tool-calling purpose (already: 5.8k vs 5.0k tok, ×2 calls at A3) |
| **B. Steps per outcome** | A1 = 1 pass; A4/A5 = plan→act→observe→re-plan loops | model-calls-per-interaction (will balloon at A4/A5) |
| **C. Interactions per *outcome*** | A1 needs many human turns to resolve; A4 resolves in ~1; A5 in 0 | **NOT modelled yet** — the missing variable |
| **D. Assurance overhead** | More guardrail + eval + observability passes per autonomous action | guardrails + online evals + **Langfuse 7 LF units/interaction** |

Channel **C** is the one that flips the economics and the one Mayur's sheet doesn't yet capture. It's also the one that *helps* the value story: a higher-autonomy agent **consumes more compute per outcome but fewer human interactions per outcome** — so on a *per-interaction* meter it looks cheap-and-similar, while on a *per-outcome* basis its cost (and its value) is clearly higher.

## 3. So is the pricing "materially the same"? — answer by level

| Levels | Reclassify by autonomy → pricing impact | Why |
|---|---|---|
| **A1–A3** | **Materially identical.** The relabel is essentially free. | Per-interaction cost is flat (~$0.04), so Mayur's per-interaction model + 57–75% margins hold unchanged. Autonomy is just a cleaner *packaging label* on the same cost engine. |
| **A4–A5** | **Materially different — and that's the upside.** | Per-interaction pricing under-captures autonomous resolution (one A4 outcome = many reasoning steps + replaces several human interactions). The unit must move to **per-resolution / per-outcome**. This is net-new revenue logic Mayur's model doesn't express. |

This **empirically grounds framework §5.3** (unit shifts seat → interaction → outcome) — it's no longer just asserted; Mayur's flat per-interaction curve is the evidence that the interaction meter is the right instrument *only up to A3*.

## 4. What to do next — make n=2 into a real proof

The hypothesis is *promising and directionally validated*, not *proven*. To make the model "amazing" defensibly:

1. **Model 3–4 more use cases** spanning the scale, in Mayur's own sheet so it's apples-to-apples:
   - **A2 Recommend** — a proactive NBA/nudge (e.g. "you can save on this subscription").
   - **A4 Execute-by-exception** — a Customer-Operations resolution loop (e.g. dispute auto-resolution within thresholds) — model the **full plan→act→observe loop** (many model calls) **and** the interactions-per-outcome.
   - **A5 Self-directed** — a multi-step mission (e.g. autonomous onboarding completion).
2. **Add the missing column: interactions (and human-turns) per *resolved outcome*.** This is the variable that makes autonomy a pricing axis. Without it, the sheet can't see channel C.
3. **Plot two curves:** cost-per-interaction (expect ~flat) and **cost-per-outcome (expect rising with autonomy)**. The gap between them *is* the case for outcome pricing at the top.
4. **Test the assurance prediction:** the guardrail + eval + Langfuse-observability share of cost should **rise with autonomy** (more monitoring per autonomous action). If it does → independent validation of the framework's "assurance scales with autonomy" tier logic (§5.4).
5. **Then state the claim precisely:** *"Autonomy level is a valid pricing basis. For A1–A3 it reproduces the current per-interaction economics exactly (so adoption is zero-risk); for A4–A5 it captures value the per-interaction model leaves on the table, via an outcome meter."*

## 5. How this feeds "packaging & pricing agents" (Shyam's next thread)

The packaging unit isn't the use case (too many, bank-specific) or the raw interaction (blind to value) — it's the **agent, licensed up to a maximum autonomy level**, on the assurance tier that ceiling requires (framework §5.4). Mayur's model supplies the **cost floor** per agent (DTAP base $326.67/agent/mo + usage + observability); the autonomy level sets the **meter and the assurance tier**. Packaging SKUs then fall out naturally:
- **Assist pack (A1)** — per-seat, Entry assurance.
- **Recommend pack (A2)** — per-seat + per-signal, Entry/Critical.
- **Transact/Resolve pack (A3–A4)** — per-interaction → per-resolution, Critical/Enterprise.
- **Autonomous Missions (A4–A5)** — per-outcome (value-share), Enterprise.

That's the bridge from Mayur's compute truth to a sellable agent catalogue.
