# How I actually use Cortex — and what to build next

**Generated:** 2026-06-28
**Question:** Of my real output, how much runs on Cortex *infrastructure* (pipeline, agents, skills, tools, knowledge, design system) vs. how much is me + the LLM + creativity?
**Method:** classified 13 marquee deliverables by build signature + scanned the repo for pipeline fingerprints (`roi_config.json`, `evidence_register.md`, `journey_maps.json`, `ENGAGEMENT_JOURNAL.md`) + reviewed ~40 past sessions.

---

## The finding

**For me, Cortex is a design system + a rendering skill-set — not an autonomous consulting engine.** I supply the entire consulting brain (what to say, the evidence, the commercial logic, the narrative arc). Cortex makes it fast, consistent, and on-brand. The multi-agent *pipeline* the core team is most invested in (and is now wrapping evals around) is the part I essentially never touch.

### Layer usage (estimated, across marquee work)

| Layer | Usage | Read |
|---|---|---|
| You + the LLM (strategy, narrative, judgment) | ~100% | the engine |
| Knowledge + design system (Frontline 2026, domains) | ~100% | every output carries it |
| Skills (frontline-slides, long-form, exec-brief) | ~90% | the workhorse |
| Tools (python builders, behind skills) | ~mid | indirect |
| Agents (discovery, ROI, journey, assembler) | ~0% | bypassed |
| Orchestrated pipeline (autonomous Act 1–7) | ~0% | bypassed |

## The evidence

| Client / output | Built with | Cortex layer | Pipeline? |
|---|---|---|---|
| Pictet QBR | frontline-slides engine | skill + DS | No |
| Barclays — Banking OS path POV | frontline-slides engine | skill + DS | No |
| SEB — Baltic / Aija | frontline-slides engine | skill + DS | No |
| SparD — commercial pricing proposal | frontline-slides engine | skill + DS | No |
| Evelyn — business case for change | frontline-slides engine | skill + DS | No |
| Coventry BS — agentic banking | frontline-slides engine | skill + DS | No |
| Advisor cockpit POV | frontline-slides engine | skill + DS | No |
| St. James's Place POV | frontline-slides engine | skill + DS | No |
| Absa — strategic alignment | frontline-slides engine | skill + DS | No |
| HSBC — CIB POV | long-form skill | skill + DS | No |
| Schroders — Nova (latest) | frontline-slides-pptx | skill + DS | No |
| AIB — Battle Plan | hand-built HTML | design system only | No |
| Nordic FinTech — opening POV | hand-built HTML | design system only | No |

Pipeline fingerprints appear **only** in `tests/` (NFIS, BECU, WSFS, SeABank validation). Closest real exception: `engagements/bbva_spain` used the engagement scaffolding + some discovery extraction, but not the full ROI/journey/assembly chain. Even ROI work (SparD pricing, Evelyn case) was skills + my pricing methodology, not the ROI agent pipeline.

---

## What to build next (a "Shyam OS")

### Already owned (the hard parts)
1. A design system — Frontline 2026.
2. A rendering engine + skills — the output factory.
3. A knowledge corpus — domains, narrative spine, pricing methodology, A1–A5 autonomy framework.
4. **Output history** — 13+ marquee decks = worked examples of how I think/structure/argue/price. The few-shot substrate for a digital twin. Most valuable, most underused.

### To add for robustness / determinism (the part I don't have yet)
1. **Memory/knowledge spine** — consolidate corpus + output patterns into a queryable brain (the twin's long-term memory).
2. **Determinism where it repeats** — POV arc, value case, pricing model, assessment layout → typed templates/contracts, not re-improvised each time.
3. **Quality gates (evals) against my canon** — flag "off my palette / ROI not grounded / arc missing," graded on my design tokens + conservative-ROI rules. (The `evals/` idea, pointed at my standards.)
4. **Build discipline (bb-* style)** — evolve engine/skills via spec → build → eval-gate, so nothing regresses. In my own repo, those hooks *help* (I'm the deliberate builder, not a user trying to move fast).
5. **Selective orchestration only** — automate genuinely repeatable flows (e.g. bank public data → first-draft POV); keep bespoke creative work manual. Don't rebuild the heavy autonomous pipeline I've proven I don't need.

### Repo strategy
A new clean repo = "my infrastructure" (design system + engine + skills + knowledge brain + my eval gates), seeded from the good parts of my fork, governed by the discipline I choose. Kept separate from the team's shared Cortex so my robustness isn't entangled with their pipeline.

### The reframe on bb-*/evals (part-1/part-2 decision)
In the team's repo that machinery hampers me because I'm a *user* there → keep it out (skip or files-only). In my *own* infrastructure that same machinery is exactly what converts "me + LLM + creativity" into a system I own and trust → study the eval system as the blueprint.
