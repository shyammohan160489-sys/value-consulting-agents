"""
Nordic FinTech Forum — Helsinki, May 2026
Opening POV for AI Roundtable (5-10 min)

Narrative arc:
  Act 1 — The Commodity Trap (intelligence is becoming a utility)
  Act 2 — Trust Becomes Infrastructure (the new moat)
  Act 3 — The Intent Layer (where customers go when the app disappears)
  Synthesis — Orchestration of trust and intent is the differentiator
"""

import sys
sys.path.insert(0, '/home/user/value-consulting-agents')
from tools.frontline_2026_html import Frontline2026HTML

h = Frontline2026HTML("Differentiation in the Age of AI — Nordic FinTech Forum 2026")

# ──────────────────────────────────────────
# 1. COVER
# ──────────────────────────────────────────
h.add_cover(
    section_label="Nordic FinTech Forum · Helsinki · May 2026",
    title="When Intelligence\nBecomes a Utility",
    subtitle="Orchestrating Trust and Intent as Banking's Next Differentiator",
)

# ──────────────────────────────────────────
# 2. OPENING STATEMENT — the provocation
# ──────────────────────────────────────────
h.add_statement(
    "Every bank is shipping AI. None of them are different.",
    highlight_words=["different"],
)

# ──────────────────────────────────────────
# 3. THE SHIFT — from/to
# ──────────────────────────────────────────
h.add_split_comparison(
    title="The frame has already moved",
    section_label="The Shift",
    left_title="2024 — Compete on AI features",
    left_items=[
        "Copilots, chatbots, GenAI on top of the app",
        "Time-to-launch beats time-to-trust",
        "Model quality = differentiation",
        "Assume customers come to your interface",
    ],
    right_title="2026 — Compete on trust and intent",
    right_items=[
        "Intelligence is a commodity input, not a feature",
        "Explainability and provenance are the product",
        "Orchestration of trusted action = differentiation",
        "Assume agents act on the customer's behalf",
    ],
)

# ──────────────────────────────────────────
# 4. ACT 1 DIVIDER
# ──────────────────────────────────────────
h.add_section_divider(
    section_label="Act 1",
    title="The Commodity Trap",
    tagline="Intelligence is becoming electricity. Everyone has it. Nobody wins on it.",
)

# ──────────────────────────────────────────
# 5. ACT 1 — stats on commoditization
# ──────────────────────────────────────────
h.add_stat_cards(
    title="Why the AI advantage will not hold",
    subtitle="Three signals the moat is dissolving underneath the industry",
    stats=[
        {"number": "<5%", "label": "Performance gap between frontier models on banking-relevant tasks", "trend": "closing"},
        {"number": "100%", "label": "Of global top-50 banks have shipped a GenAI assistant since 2024", "trend": "saturated"},
        {"number": "18 mo", "label": "Until feature parity — your copilot will look like theirs", "trend": "converging"},
    ],
)

# ──────────────────────────────────────────
# 6. ACT 1 — the tension (statement)
# ──────────────────────────────────────────
h.add_statement(
    "If intelligence is a utility, the moat moves up the stack.",
    highlight_words=["up the stack"],
)

# ──────────────────────────────────────────
# 7. ACT 2 DIVIDER
# ──────────────────────────────────────────
h.add_section_divider(
    section_label="Act 2",
    title="Trust Becomes Infrastructure",
    tagline="Not a brand claim. Not a policy. Plumbing.",
)

# ──────────────────────────────────────────
# 8. ACT 2 — trust tiles (the shift)
# ──────────────────────────────────────────
h.add_tiles(
    title="Trust shifts from promise to performance",
    subtitle="McKinsey, State of AI Trust 2026 — trust is now measured, audited, and proven at the decision level",
    section_label="The New Plumbing",
    columns=3,
    tiles=[
        {
            "stat": "1 in 3",
            "title": "Firms at maturity level 3+ on AI governance",
            "body": "Two-thirds of the industry cannot yet prove how their AI decides. That is the gap — and the opportunity.",
            "accent": "red",
            "pill": "GAP",
        },
        {
            "stat": "From → To",
            "title": "Promise → Performance metric",
            "body": "Explainability, provenance, and human oversight are moving from principle to KPI. Trust is being instrumented.",
            "accent": "blue",
            "pill": "SHIFT",
        },
        {
            "stat": "Nordics",
            "title": "Best-positioned region globally",
            "body": "High-trust societies, mature regulators, interoperable digital identity. Trust-as-infrastructure is an export, not a cost.",
            "accent": "green",
            "pill": "EDGE",
        },
    ],
)

# ──────────────────────────────────────────
# 9. ACT 3 DIVIDER
# ──────────────────────────────────────────
h.add_section_divider(
    section_label="Act 3",
    title="The Intent Layer",
    tagline="When your customer stops using your app — but still needs your bank.",
)

# ──────────────────────────────────────────
# 10. ACT 3 — the intent economy
# ──────────────────────────────────────────
h.add_stat_cards(
    title="The interface is disappearing. The balance sheet is not.",
    subtitle="Agentic commerce is the next platform shift — and it routes around banks that cannot be trusted to act",
    stats=[
        {"number": "$3–5T", "label": "Agentic commerce revenue by 2030 (McKinsey)", "trend": "↑"},
        {"number": "57%", "label": "Of banking execs expect AI agents embedded in core ops within 3 years", "trend": "↑"},
        {"number": "24 mo", "label": "Until agents transact on customers' behalf at scale", "trend": "↑"},
    ],
)

# ──────────────────────────────────────────
# 11. SYNTHESIS — the three-layer stack
# ──────────────────────────────────────────
h.add_architecture_stack(
    title="Differentiation is the orchestration layer",
    subtitle="Three layers. The bottom commoditises. The top two are the competition.",
    section_label="The Thesis",
    layers=[
        {
            "label": "Intent Layer",
            "sub_label": "Where customers and their agents act",
            "bg": "#001C3D",
            "dark": True,
            "accent": "#1A5AFF",
            "items": [
                {"name": "Agent-to-bank APIs"},
                {"name": "Intent routing"},
                {"name": "Delegated authority"},
                {"name": "Outcome contracts"},
            ],
        },
        {
            "label": "Trust Layer",
            "sub_label": "The moat — instrumented, audited, provable",
            "bg": "#EBF0FF",
            "accent": "#1A5AFF",
            "items": [
                {"name": "Explainability", "border": "#1A5AFF", "color": "#001C3D"},
                {"name": "Provenance", "border": "#1A5AFF", "color": "#001C3D"},
                {"name": "Human oversight", "border": "#1A5AFF", "color": "#001C3D"},
                {"name": "Consent & identity", "border": "#1A5AFF", "color": "#001C3D"},
                {"name": "Audit trail", "border": "#1A5AFF", "color": "#001C3D"},
            ],
        },
        {
            "label": "Intelligence Layer",
            "sub_label": "The commodity — assume parity in 18 months",
            "bg": "#F5F7F9",
            "accent": "#5C6E84",
            "items": [
                {"name": "Foundation models", "border": "#C4CDD9", "color": "#5C6E84"},
                {"name": "Retrieval", "border": "#C4CDD9", "color": "#5C6E84"},
                {"name": "Agents & tool use", "border": "#C4CDD9", "color": "#5C6E84"},
                {"name": "Fine-tuning", "border": "#C4CDD9", "color": "#5C6E84"},
            ],
        },
    ],
)

# ──────────────────────────────────────────
# 12. CLOSE — three questions for the room
# ──────────────────────────────────────────
h.add_pillar_rows(
    title="Three questions to open the room",
    subtitle="Chatham House. 20 minutes each. The answers become the Helsinki Principles.",
    section_label="Discussion",
    columns=["Act 1 — Commodity Trap", "Act 2 — Trust as Infrastructure", "Act 3 — Intent Layer"],
    rows=[
        {
            "left": "If your AI looks like theirs in 18 months, what is left to compete on?",
            "left_detail": "Name one capability your bank owns that a competitor cannot buy.",
            "left_accent": "red",
            "mid": "Is trust a marketing claim, a compliance cost, or a product?",
            "mid_detail": "If it is a product — who owns the roadmap?",
            "right": "When an agent shops for a mortgage on behalf of a customer, does it pick your bank — or route around you?",
            "right_detail": "What would make you the default choice of a machine?",
            "right_accent": "blue",
        },
    ],
)

# ──────────────────────────────────────────
# 13. CLOSING STATEMENT
# ──────────────────────────────────────────
h.add_statement(
    "The next decade of banking is not won on intelligence. It is won on the orchestration of trust and intent.",
    highlight_words=["orchestration of trust and intent"],
)

out = "/home/user/value-consulting-agents/presentations/nordic-fintech-forum-2026/nordic_fintech_forum_opening_pov.html"
h.save(out)
print(f"Wrote: {out}")
