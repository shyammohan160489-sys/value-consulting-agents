"""
Nordea TxB — Strategic POV for Taru Moller
Frontline 2026 HTML presentation
Meeting: April 2, 2026 (45 min)
"""
import sys, os
sys.path.insert(0, '/Users/shyam/cortex')
from tools.frontline_2026_html import Frontline2026HTML

h = Frontline2026HTML("Nordea Transaction Banking — Strategic Conversation")

# ── 1. Cover ──
h.add_cover(
    "Backbase x Nordea",
    "Transaction Banking |A Strategic Conversation",
    "April 2, 2026"
)

# ── 2. The structural shift — our thesis ──
h.add_tiles(
    "The architecture beneath payments is being restructured",
    "Not faster rails. Not better channels. A structural migration of where value sits.",
    section_label="Our Observation",
    columns=3,
    tiles=[
        {
            "stat": "01",
            "title": "Execution",
            "body": "The rail. Speed is baseline. Instant payments, A2A, ISO 20022 — rails are becoming interchangeable. The rail executes. It no longer differentiates.",
            "accent": "red",
            "pill": "COMMODITY"
        },
        {
            "stat": "02",
            "title": "Trust",
            "body": "Identity, consent, risk interpretation. The connective tissue linking wallets, fraud management, and AI-enabled ecosystems. Not a compliance checkbox — architectural infrastructure.",
            "accent": "amber",
            "pill": "CONNECTIVE TISSUE"
        },
        {
            "stat": "03",
            "title": "Intent",
            "body": "AI-driven decisioning. Translating verified identity into executable action. Where AI doesn't just respond — it monitors state, identifies the right moment, and acts within governed boundaries.",
            "accent": "blue",
            "pill": "EMERGING FRONTIER"
        },
    ],
    footer_text="Value is migrating upward. **Whoever connects trust to real-time decisioning at scale** — anchoring identity, managing consent, interpreting risk — owns the next decade of transaction banking."
)

# ── 3. The Nordea commitment — hard numbers ──
h.add_stat_cards(
    "Nordea has made a public commitment",
    "The targets are clear. The operating model that delivers them is the open question.",
    stats=[
        {"number": "€600M", "label": "Gross cost takeout by 2030", "trend": ""},
        {"number": "1,500", "label": "Roles impacted, announced March 17", "trend": ""},
        {"number": "46→40%", "label": "Cost-to-income ratio target", "trend": ""},
        {"number": "+50K", "label": "New SME customers by 2030", "trend": ""},
        {"number": "60%", "label": "Workloads on next-gen systems", "trend": ""},
    ]
)

# ── 4. The productivity paradox ──
h.add_tiles(
    "The productivity paradox",
    "Three targets that only coexist with a fundamentally different operating model.",
    section_label="The Challenge",
    columns=3,
    tiles=[
        {
            "stat": "-1,500",
            "title": "People",
            "body": "Workforce reduction in 2026-27. Headcount is the cost line being managed — not the solution to scaling.",
            "accent": "red",
        },
        {
            "stat": "+50,000",
            "title": "SME Customers",
            "body": "Explicit growth target by 2030. Volume must grow while the workforce shrinks. Linear scaling is over.",
            "accent": "green",
        },
        {
            "stat": "46→40%",
            "title": "Cost-to-Income",
            "body": "Three points in four years. Efficiency must improve while serving more customers, across more products, in four Nordic markets.",
            "accent": "blue",
        },
    ],
    footer_text="The commitment is public. **The answer is elastic operations** — scale without linear headcount growth. AI agents execute routine work. Humans govern high-value decisions. One platform orchestrates."
)

# ── 5. Where the cost actually lives ──
h.add_tiles(
    "Where the cost actually lives",
    "Not in your systems. In the whitespace between them. 50% of banking work lives in handoffs.",
    section_label="The Real Problem",
    columns=3,
    tiles=[
        {
            "title": "Payments Operations",
            "body": [
                "ISO 20022 is live. Instant payments compliant.",
                "But every exception, dispute, chargeback, and sanctions flag is still handled **manually** — across four country systems, by hand, via email.",
                "",
                "The rail is modern. The operations around it are not."
            ],
            "accent": "red",
            "pill": "TxB"
        },
        {
            "title": "Trade Finance",
            "body": [
                "Strong operation. Top-ranked by Prospera.",
                "But document analysis, compliance checks, sanctions screening remain **multi-day processes**.",
                "",
                "Multi-agent coordination could collapse days into hours — with human escalation at defined thresholds."
            ],
            "accent": "amber",
            "pill": "TxB"
        },
        {
            "title": "Cash Management",
            "body": [
                "#1 in the Nordics. Real-time APIs. Global Cash Pool.",
                "But the system **reports**. It doesn't interpret patterns, suggest sweep optimisations, or act on treasurer intent.",
                "",
                "The data is there. The intelligence layer is not."
            ],
            "accent": "blue",
            "pill": "TxB"
        },
    ],
)

# ── 6. What peers are executing ──
h.add_tiles(
    "European peers are not piloting. They are executing.",
    "The pattern: ISO 20022 + workforce restructuring + AI in back-office ops = the same inflection Nordea is navigating.",
    section_label="The Race Is On",
    columns=3,
    tiles=[
        {
            "title": "ING",
            "body": [
                "Agentic AI in production across KYC, AML operations, and wholesale banking CDD.",
                "",
                "COO confirmed **25% productivity gain** when AI enters an ops process.",
                "Next: deploying more powerful models."
            ],
            "accent": "blue",
            "pill": "IN PRODUCTION"
        },
        {
            "title": "ABN AMRO",
            "body": [
                "Full 'ISO native' strategy — all payment applications ISO 20022 end-to-end.",
                "",
                "Simultaneously announced **5,200 job cuts** by 2028.",
                "Explicitly citing AI automation of back-office ops and AML as the enabler."
            ],
            "accent": "blue",
            "pill": "IN PRODUCTION"
        },
        {
            "title": "Danske Bank",
            "body": [
                "DanskeGPT adopted by **74% of employees**.",
                "GenAI applied to reconciliations, data automation, and post-trade processing.",
                "",
                "AWS hyperautomation halved their migration timeline.",
                "Backbase as enterprise-wide platform."
            ],
            "accent": "blue",
            "pill": "IN PRODUCTION"
        },
    ],
    footer_text="Sources: Computer Weekly (ING COO, Jul 2025) · SWIFT ISO native case study · Brussels Signal (Nov 2025) · Danske Bank Annual Report 2024 · AWS case study"
)

# ── 7. Three acceleration areas for TxB ──
h.add_pillar_rows(
    "Three acceleration areas for Transaction Banking",
    "Specific to your domain. Where AI and platform architecture intersect with Nordea's TxB priorities.",
    section_label="Where We See Opportunity",
    columns=["TxB Domain", "The Shift Required", "What Acceleration Looks Like"],
    rows=[
        {
            "left": "Payments Operations",
            "left_detail": "Exceptions, disputes, sanctions flags — manual, multi-country",
            "mid": "From manual exception handling to governed automation",
            "mid_detail": "AI agents handle routing, screening, and resolution. Humans govern thresholds and escalations.",
            "right": "Agentic Process Automation",
            "right_detail": "Multi-agent coordination. Same governance as human operators. Collapse multi-day processes.",
            "left_accent": "red",
            "right_accent": "blue",
        },
        {
            "left": "Cash Management",
            "left_detail": "Real-time data exists but only reports — no interpretation, no action",
            "mid": "From reactive reporting to proactive liquidity intelligence",
            "mid_detail": "Detect patterns across Nordic accounts. Suggest sweeps, investment windows, funding needs.",
            "right": "Intent Orchestration",
            "right_detail": "The system interprets treasurer intent and acts within governed parameters. AI that recommends and executes.",
            "left_accent": "amber",
            "right_accent": "blue",
        },
        {
            "left": "Embedded Distribution",
            "left_detail": "API Market is mature — but primarily compliance-driven, not strategic",
            "mid": "From compliance distribution to strategic embedded finance",
            "mid_detail": "Expose TxB services inside ERPs, billing systems, corporate treasury platforms.",
            "right": "Platform-as-Distribution",
            "right_detail": "Integration layer makes it trivial to surface Nordea TxB services in third-party platforms at scale.",
            "left_accent": "amber",
            "right_accent": "blue",
        },
    ]
)

# ── 8. The architecture that enables it ──
h.add_architecture_stack(
    "An architecture built for this shift",
    "Not rip-and-replace. An intelligent orchestration layer that sits on top of your existing infrastructure.",
    section_label="Banking OS",
    layers=[
        {
            "label": "Frontline",
            "sub_label": "Customers + Employees + AI Agents — unified identity and entitlements",
            "items": [
                {"name": "Corporate Portal", "border": "#1A5AFF", "color": "#1A5AFF"},
                {"name": "RM Workspace", "border": "#1A5AFF", "color": "#1A5AFF"},
                {"name": "Operations Workspace", "border": "#1A5AFF", "color": "#1A5AFF"},
                {"name": "Conversational AI", "border": "#1A5AFF", "color": "#1A5AFF"},
            ],
            "accent": "#1A5AFF",
        },
        {
            "label": "Intelligence + Orchestration",
            "sub_label": "Trust infrastructure — unified customer state, consent, risk interpretation",
            "items": [
                {"name": "Customer State Graph", "border": "#7C3AED", "color": "#7C3AED"},
                {"name": "Banking Ontology", "border": "#7C3AED", "color": "#7C3AED"},
                {"name": "Agentic Runtime", "border": "#7C3AED", "color": "#7C3AED"},
                {"name": "Human-in-the-Loop Governance", "border": "#7C3AED", "color": "#7C3AED"},
            ],
            "accent": "#7C3AED",
        },
        {
            "label": "AI-native Banking OS",
            "dark": True,
            "items": [
                {"name": "Process Orchestration"},
                {"name": "Case Management"},
                {"name": "Multi-Model AI"},
                {"name": "Audit Trail"},
                {"name": "Control Plane"},
            ],
            "accent": "#1A5AFF",
        },
        {
            "label": "Integration Layer",
            "sub_label": "Connects to existing cores — no rip-and-replace",
            "items": [
                {"name": "Core Banking", "border": "#D1D5DB"},
                {"name": "Payments", "border": "#D1D5DB"},
                {"name": "Cards", "border": "#D1D5DB"},
                {"name": "KYC / AML", "border": "#D1D5DB"},
                {"name": "ERP Systems", "border": "#D1D5DB"},
                {"name": "50+ Connectors", "border": "#D1D5DB"},
            ],
            "accent": "#5C6E84",
        },
    ]
)

# ── 9. Danske Bank — in production ──
h.add_case_study(
    "Danske Bank — enterprise-wide platform, in production",
    body_lines=[
        "Enterprise-wide engagement platform across Personal, Business, and Large Corporates & Institutions",
        "500 onboarding flows consolidated into a unified digital journey",
        "12 design systems rationalised into one",
        "Go-live in under 6 months — 2-year acceleration on original transformation timeline",
        "DanskeGPT adopted by 74% of employees — GenAI in reconciliations and post-trade processing",
        "Strategic platform for all segments: retail, SME, commercial, and wealth",
    ],
    legal_text="Restricted use. This case study is intended solely for use in 1:1 discussions with prospective clients."
)

# ── 10. The question ──
h.add_statement(
    "You have built trust infrastructure. #1 cash management in the Nordics. Top-ranked trade finance. Among the most mature API platforms in Europe. The question is whether you connect that trust to real-time decisioning — at scale. That is the shift from products to platform.",
    highlight_words=[
        "trust infrastructure",
        "connect that trust to real-time decisioning",
        "products to platform"
    ]
)

# ── 11. Where do we go from here? ──
h.add_tiles(
    "Where do we go from here?",
    "Three concrete next steps — scoped to your priorities.",
    section_label="Next Steps",
    columns=3,
    tiles=[
        {
            "stat": "01",
            "title": "Which TxB domain first?",
            "body": "Which problem is costing Nordea most today — and which one unlocks the adjacent stakeholders needed to move the full 2030 agenda?",
            "accent": "blue",
        },
        {
            "stat": "02",
            "title": "A live demonstration",
            "body": "Prioritised use cases demonstrated against Nordea's own 2030 targets. Not a generic demo — your scenarios, your data model, your operations.",
            "accent": "blue",
        },
        {
            "stat": "03",
            "title": "A value case",
            "body": "A quantified business case modelled directly against Nordea's cost-to-income, FTE, and volume metrics. Conservative. Defensible. Decision-ready.",
            "accent": "blue",
        },
    ]
)

# ── 12. Handoff to live demo ──
h.add_section_divider(
    "Product Showcase",
    "What this looks like |in practice",
    "Principal Solutions Engineer"
)

# ── Save ──
out_path = "/Users/shyam/cortex/Engagement/Nordea/Output/nordea_txb_frontline.html"
out = h.save(out_path)
print(f"Saved: {out}")
print(f"Scenes: {len(h.scenes)}")
print(f"Size: {os.path.getsize(out)/1024:.1f} KB")
