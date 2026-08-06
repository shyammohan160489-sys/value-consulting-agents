# Cortex Routing Map — Natural Language → Built Assets

**Purpose:** Shyam talks in natural English; Claude owns the translation to the toolkit. This is the full word-association map behind the per-turn router hook (`.claude/routing-card.md`, injected on every prompt via `UserPromptSubmit`). When his words match a row here, use the built asset — do not freeform-generate. When they match none but feel adjacent to one, **ask before executing**.

## Deliverable words → skills

| When Shyam says… | Route to | Notes |
|---|---|---|
| deck, slides, presentation, PPTX, PowerPoint, "board deck", "readout" | `/exhibit-slides-pptx` | ⭐ DEFAULT for ALL PPTX (ratified 28 Jul 2026). Frontline PPTX **only** when he names Frontline/branded layouts. |
| HTML deck, interactive deck, "self-running", walkthrough | `/frontline-slides-html` | Presenter mode, 17 layouts. |
| long-form, document, business case, value case, "something they read", email-able, PDF | `/frontline-long-form` | Sidebar-nav scrolling doc, PDF-printable. |
| proposal, commercial proposal, pricing proposal, bilingual/Arabic, sliders, executive readout | `/proposal-longform` | Client-facing interactive proposal. |
| deal strategy, CPQ, concession, negotiation prep, deal desk | `/proposal-builder` | Internal cockpit — never client-facing. |
| prototype, clickable, mockup, demo, "show it working", phone frame | `/prototype` | Backbase use-case prototypes. |
| assessment, capability heatmap, maturity dashboard | `/generate-assessment-html` | NEVER hand-roll assessment HTML. |
| ROI, business case model, value levers, benefits case | `/build-roi` (+ `roi-hypothesis-builder` → `roi-financial-modeler` agents) | Levers first, numbers second. |
| questionnaire, data request, "what to ask the client" | `/generate-roi-questionnaire` | Pre-populated from upstream. |
| journey, journey map, day-in-the-life, swim lanes | `/build-journey` | Needs discovery outputs. |
| use case, use-case doc, "10-section" | `/usecase-doc` | Product-validated use cases. |
| transcript, meeting notes, call recording, "what did we agree" | `/deal-notes` (or Plaud MCP to pull recordings) | Deal-state record + journal. |
| pricing, price this, unit pricing, interaction pricing | `/pricing-model` + `deal-pricing-system/` | LOB pricing rules: wealth=AUM, retail/SME=unit, CB=platform+interaction. |
| bank numbers, annual report, financials, cost-income | `/profile-bank` | Public financial extraction. |
| publish, "push my changes", PR | `/publish` | Git is Claude's job, not his. |

## Topic words → knowledge (read BEFORE generating)

| Topic in his words | Read first |
|---|---|
| AI/agentic use cases, agents for X, autonomy, "which processes" | `knowledge/domains/apa-matrix/` (apa_v3.json) + `knowledge/domains/agent-autonomy-framework.md` (A1–A5) |
| AI value proof, "who's doing what", market evidence, stats for a POV | `knowledge/domains/ai-value-evidence/` — embed ✅ items w/ primary citations; ⚠️ items verify first |
| wealth pitch, advisor, NBA, signals | `knowledge/domains/wealth/` (wealth-os-narrative, next-best-action-method, apa-processes) |
| conversational banking, deflection, contact center, voice | `knowledge/domains/conversational-banking/` + Mayur cost model (`agent-pricing/`) |
| building societies | `knowledge/domains/building-societies/` |
| product truth, Banking OS, Nexus/Sentinel, packaging | `knowledge/product/banking-os.md` — WINS over any diverging file |
| messaging, story arc, From→To, vocabulary | `knowledge/design-system/narrative-spine.md` |
| visual tokens, colors, layouts | `knowledge/design-system/frontline-tokens.json` (Frontline) — exhibit kit has its OWN palette, never blend |

## The evidence doctrine (locked 6 Aug 2026)

1. **Validated value prop?** Embed the external research, cited to the **primary source** (earnings call, named analyst report). Analyst frames + live bank disclosures together beat either alone.
2. **Unvalidated value prop?** Do **not** stretch or cherry-pick research to cover it. Convince by **demonstration**: prototype, design, journey map, working demo. Say openly that we're ahead of the research where we are.
3. **All third-party content is polarized** — analysts and aggregators have sponsors and agendas. Verify before client use; expect distortions (we caught 3 in 10 posts from one aggregator).
4. **Never fabricate. Never present assumed as verified.**

## The ambiguity rule

If a request could route two or more ways, or no built asset fits but one is adjacent — **ask first, one line, name the options**. A wrong silent route costs more than a question. This is the agreed contract: Shyam speaks natural language and does not track the toolkit; Claude translates and asks when the translation is unclear.

*Established 6 Aug 2026. Maintained by Claude — update this file when skills are added/retired.*
