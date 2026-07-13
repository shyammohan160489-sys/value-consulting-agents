"""
Nordea TxB — Strategic POV for Taru Moller
Frontline 2026 PPTX (Google Slides compatible)
Meeting: April 2, 2026 (45 min)
"""
import sys, os
sys.path.insert(0, '/Users/shyam/cortex')
from tools.frontline_2026_presenter import Frontline2026Presenter

out_path = "/Users/shyam/cortex/Engagement/Nordea/Output/nordea_txb_frontline.pptx"
p = Frontline2026Presenter(output_path=out_path)

# ── 1. Cover ──
p.add_cover_slide(
    "Backbase x Nordea",
    "Transaction Banking\nA Strategic Conversation",
    "April 2, 2026"
)

# ── 2. The structural shift — our thesis ──
p.add_tiles_slide(
    "The architecture beneath payments is being restructured",
    subtitle="Not faster rails. Not better channels. A structural migration of where value sits.",
    section_label="Our Observation",
    columns=3,
    tiles=[
        {
            "stat": "01",
            "title": "Execution",
            "body": "The rail. Speed is baseline. Instant payments, A2A, ISO 20022 \u2014 rails are becoming interchangeable. The rail executes. It no longer differentiates.",
            "accent": "red",
            "pill": "COMMODITY"
        },
        {
            "stat": "02",
            "title": "Trust",
            "body": "Identity, consent, risk interpretation. The connective tissue linking wallets, fraud management, and AI-enabled ecosystems. Not a compliance checkbox \u2014 architectural infrastructure.",
            "accent": "amber",
            "pill": "CONNECTIVE TISSUE"
        },
        {
            "stat": "03",
            "title": "Intent",
            "body": "AI-driven decisioning. Translating verified identity into executable action. Where AI monitors state, identifies the right moment, and acts within governed boundaries.",
            "accent": "blue",
            "pill": "EMERGING FRONTIER"
        },
    ],
)

# ── 3. The Nordea commitment — hard numbers ──
p.add_stat_cards_slide(
    "Nordea has made a public commitment",
    "The targets are clear. The operating model that delivers them is the open question.",
    stats=[
        {"number": "\u20ac600M", "label": "Gross cost takeout by 2030"},
        {"number": "1,500", "label": "Roles impacted, announced March 17"},
        {"number": "46\u219240%", "label": "Cost-to-income ratio target"},
        {"number": "+50K", "label": "New SME customers by 2030"},
        {"number": "60%", "label": "Workloads on next-gen systems"},
    ]
)

# ── 4. The productivity paradox ──
p.add_tiles_slide(
    "The productivity paradox",
    subtitle="Three targets that only coexist with a fundamentally different operating model.",
    section_label="The Challenge",
    columns=3,
    tiles=[
        {
            "stat": "-1,500",
            "title": "People",
            "body": "Workforce reduction in 2026-27. Headcount is the cost line being managed \u2014 not the solution to scaling.",
            "accent": "red",
        },
        {
            "stat": "+50,000",
            "title": "SME Customers",
            "body": "Explicit growth target by 2030. Volume must grow while the workforce shrinks. Linear scaling is over.",
            "accent": "green",
        },
        {
            "stat": "46\u219240%",
            "title": "Cost-to-Income",
            "body": "Three points in four years. Efficiency must improve while serving more customers, across more products, in four Nordic markets.",
            "accent": "blue",
        },
    ],
)

# ── 5. Where the cost actually lives ──
p.add_tiles_slide(
    "Where the cost actually lives",
    subtitle="Not in your systems. In the whitespace between them. 50% of banking work lives in handoffs.",
    section_label="The Real Problem",
    columns=3,
    tiles=[
        {
            "title": "Payments Operations",
            "body": "ISO 20022 is live. Instant payments compliant. But every exception, dispute, chargeback, and sanctions flag is still handled manually \u2014 across four country systems, by hand, via email.",
            "accent": "red",
            "pill": "TxB"
        },
        {
            "title": "Trade Finance",
            "body": "Strong operation. Top-ranked by Prospera. But document analysis, compliance checks, sanctions screening remain multi-day processes. Multi-agent coordination could collapse days into hours.",
            "accent": "amber",
            "pill": "TxB"
        },
        {
            "title": "Cash Management",
            "body": "#1 in the Nordics. Real-time APIs. Global Cash Pool. But the system reports. It doesn't interpret patterns, suggest sweep optimisations, or act on treasurer intent.",
            "accent": "blue",
            "pill": "TxB"
        },
    ],
)

# ── 6. What peers are executing ──
p.add_tiles_slide(
    "European peers are not piloting. They are executing.",
    subtitle="The pattern: ISO 20022 + workforce restructuring + AI in back-office ops = the same inflection Nordea is navigating.",
    section_label="The Race Is On",
    columns=3,
    tiles=[
        {
            "title": "ING",
            "body": "Agentic AI in production across KYC, AML operations, and wholesale banking CDD. COO confirmed 25% productivity gain when AI enters an ops process.",
            "accent": "blue",
            "pill": "IN PRODUCTION"
        },
        {
            "title": "ABN AMRO",
            "body": "Full 'ISO native' strategy \u2014 all payment applications ISO 20022 end-to-end. Announced 5,200 job cuts by 2028, explicitly citing AI automation.",
            "accent": "blue",
            "pill": "IN PRODUCTION"
        },
        {
            "title": "Danske Bank",
            "body": "DanskeGPT adopted by 74% of employees. GenAI in reconciliations, data automation, and post-trade processing. Backbase as enterprise-wide platform.",
            "accent": "blue",
            "pill": "IN PRODUCTION"
        },
    ],
)

# ── 7. Three acceleration areas for TxB ──
p.add_pillar_rows_slide(
    "Three acceleration areas for Transaction Banking",
    subtitle="Specific to your domain. Where AI and platform architecture intersect with Nordea's TxB priorities.",
    section_label="Where We See Opportunity",
    columns=["TxB Domain", "The Shift Required", "What Acceleration Looks Like"],
    rows=[
        {
            "left": "Payments Operations",
            "left_detail": "Exceptions, disputes, sanctions flags \u2014 manual, multi-country",
            "mid": "From manual exception handling to governed automation",
            "mid_detail": "AI agents handle routing, screening, and resolution. Humans govern thresholds.",
            "right": "Agentic Process Automation",
            "right_detail": "Multi-agent coordination. Same governance as human operators.",
            "left_accent": "red",
            "right_accent": "blue",
        },
        {
            "left": "Cash Management",
            "left_detail": "Real-time data exists but only reports \u2014 no interpretation",
            "mid": "From reactive reporting to proactive liquidity intelligence",
            "mid_detail": "Detect patterns across Nordic accounts. Suggest sweeps, funding needs.",
            "right": "Intent Orchestration",
            "right_detail": "The system interprets treasurer intent and acts within governed parameters.",
            "left_accent": "amber",
            "right_accent": "blue",
        },
        {
            "left": "Embedded Distribution",
            "left_detail": "API Market mature but primarily compliance-driven",
            "mid": "From compliance distribution to strategic embedded finance",
            "mid_detail": "Expose TxB services inside ERPs, billing systems, treasury platforms.",
            "right": "Platform-as-Distribution",
            "right_detail": "Integration layer surfaces Nordea TxB in third-party platforms at scale.",
            "left_accent": "amber",
            "right_accent": "blue",
        },
    ]
)

# ── 8. The architecture that enables it ──
p.add_architecture_stack_slide(
    "An architecture built for this shift",
    subtitle="Not rip-and-replace. An intelligent orchestration layer on top of your existing infrastructure.",
    section_label="Banking OS",
    layers=[
        {
            "label": "Frontline",
            "sub_label": "Customers + Employees + AI Agents \u2014 unified identity and entitlements",
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
            "sub_label": "Trust infrastructure \u2014 unified customer state, consent, risk interpretation",
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
            "sub_label": "Connects to existing cores \u2014 no rip-and-replace",
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
p.add_case_study_slide(
    "Danske Bank \u2014 enterprise-wide platform, in production",
    body_lines=[
        "Enterprise-wide engagement platform across Personal, Business, and Large Corporates & Institutions",
        "500 onboarding flows consolidated into a unified digital journey",
        "12 design systems rationalised into one",
        "Go-live in under 6 months \u2014 2-year acceleration on original transformation timeline",
        "DanskeGPT adopted by 74% of employees \u2014 GenAI in reconciliations and post-trade processing",
        "Strategic platform for all segments: retail, SME, commercial, and wealth",
    ],
    legal_text="Restricted use. This case study is intended solely for use in 1:1 discussions with prospective clients."
)

# ── 10. The question ──
p.add_statement_slide(
    "You have built trust infrastructure. #1 cash management in the Nordics. Top-ranked trade finance. Among the most mature API platforms in Europe. The question is whether you connect that trust to real-time decisioning \u2014 at scale. That is the shift from products to platform.",
    highlight_words=[
        "trust infrastructure",
        "connect that trust to real-time decisioning",
        "products to platform"
    ]
)

# ── 11. Where do we go from here? ──
p.add_tiles_slide(
    "Where do we go from here?",
    subtitle="Three concrete next steps \u2014 scoped to your priorities.",
    section_label="Next Steps",
    columns=3,
    tiles=[
        {
            "stat": "01",
            "title": "Which TxB domain first?",
            "body": "Which problem is costing Nordea most today \u2014 and which one unlocks the adjacent stakeholders needed to move the full 2030 agenda?",
            "accent": "blue",
        },
        {
            "stat": "02",
            "title": "A live demonstration",
            "body": "Prioritised use cases demonstrated against Nordea's own 2030 targets. Not a generic demo \u2014 your scenarios, your data model, your operations.",
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
p.add_section_divider(
    "Product Showcase",
    "What this looks like\nin practice",
    "Principal Solutions Engineer"
)

# ── Save ──
p.save()
print(f"Saved: {out_path}")
print(f"Slides: {len(p.slides)}")
print(f"Size: {os.path.getsize(out_path)/1024:.1f} KB")
