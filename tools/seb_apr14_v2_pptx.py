"""
SEB April 14 Meeting — v2 (13-slide meeting deck)
Frontline 2026 PPTX for Google Slides import.
"""
import sys
sys.path.insert(0, '/Users/shyam/cortex')
from tools.frontline_2026_presenter import Frontline2026Presenter

p = Frontline2026Presenter(output_path="/Users/shyam/cortex/Engagement/SEB/Output/SEB_Service_to_Sale_Apr14_v2.pptx")

# ═══ 1. COVER ═══
p.add_cover_slide("Backbase x SEB", "From Service to Sale\nThe Connected Advisor", "Stockholm  ·  April 14, 2026")

# ═══ 2. AGENDA ═══
p.add_agenda_slide("AI-Native Banking OS", "Agenda", "Backbase x SEB", [
    "Unified Frontline & Banking OS",
    "The Service-to-Sale Challenge",
    "Live Platform Demo",
    "Banking OS & Architecture",
    "Next Steps — Ignite"
])

# ═══ 3. BACKBASE / BANKING OS (Noora) ═══
p.add_stat_cards_slide(
    title="150+ banks. One platform.",
    subtitle="Backbase builds the AI-native Banking OS — the system that orchestrates every customer, employee, and AI agent interaction across a bank's entire frontline.",
    stats=[
        {"number": "150+", "label": "Financial institutions"},
        {"number": "€200M+", "label": "Annual revenue"},
        {"number": "2,500+", "label": "People globally"},
    ]
)

# ═══ 4. LIFECYCLE ═══
p.add_tiles_slide(
    title="Four stages. Today we double-click on two.",
    subtitle="The Banking OS orchestrates the entire customer lifecycle.",
    section_label="The Customer Lifecycle",
    columns=4,
    tiles=[
        {"stat": "", "title": "Acquire", "body": "Onboarding, origination, lead management, KYC", "accent": "blue", "pill": "ACQUIRE"},
        {"stat": "", "title": "Activate", "body": "Daily banking, payments, first transaction, digital adoption", "accent": "blue", "pill": "ACTIVATE"},
        {"stat": "", "title": "Engage", "body": "Cross-sell, next-best-action, RM advisory, sales pipeline", "accent": "blue", "pill": "ENGAGE  ←  TODAY"},
        {"stat": "", "title": "Retain", "body": "Servicing, human assist, case management, churn prediction", "accent": "blue", "pill": "RETAIN  ←  TODAY"},
    ]
)

# ═══ 5. DIVIDER ═══
p.add_section_divider("Let's Double-Click", "Service to Sale\nThe episode that matters.", "A customer calls the service center. What happens next determines whether you retain, engage — or lose.")

# ═══ 6. HYPOTHESIS — CRM GAP ═══
p.add_split_comparison(
    title="CRM knows who the customer is. It doesn't power the interaction.",
    section_label="Our Hypothesis",
    left_title="WHERE THE THREAD BREAKS",
    left_items=[
        "Service Call — CSR has no cross-sell visibility. CRM doesn't surface NBA or propensity. (70-80% missed)",
        "Handoff — CRM captures the lead but not the interaction context. RM gets a name, not a story. (40-60% go cold)",
        "RM Meeting — CRM doesn't generate briefs or AI prep. RM pulls data from 5+ sources. (40-60% day on admin)",
        "Activation — CRM marks deal as 'won' but doesn't orchestrate onboarding or follow-up. (0 pipeline continuity)",
    ],
    right_title="WHY CRM ALONE CAN'T CLOSE IT",
    right_items=[
        "CRM = system of record — tracks contacts and deals, not live interactions",
        "No unified workspace — CSR/RM still toggles between CRM, core banking, email",
        "No AI-native engagement — no real-time NBA, meeting briefs, or opportunity flagging",
        "No activation layer — when the deal closes, CRM's job is done, but the customer's journey begins",
        "Nordic benchmark: CRM + engagement layer = 2-4x cross-sell, 40-60% RM admin freed",
    ]
)

# ═══ 7. AI MATURITY MODEL ═══
p.add_tiles_slide(
    title="The path to an AI-native service-to-sale",
    subtitle="Three maturity levels. Each changes the role of the human.",
    section_label="Our Point of View",
    columns=3,
    tiles=[
        {"stat": "L1", "title": "AI-Assisted", "body": "Human-in-the-loop. AI surfaces insights. Humans decide and act on every step. Where most banks are heading today.", "accent": "blue", "pill": "LEVEL 1"},
        {"stat": "L2", "title": "AI-Augmented", "body": "Human-on-the-loop. AI acts by default. Humans monitor and override. Achievable within 12-18 months on the Banking OS.", "accent": "purple", "pill": "LEVEL 2"},
        {"stat": "L3", "title": "AI-Native", "body": "Human-out-of-the-loop (routine). AI handles routine end-to-end. Humans focus on complex advisory. The target state.", "accent": "green", "pill": "LEVEL 3"},
    ]
)

# ═══ 8. AI vs HUMAN + PEER BENCHMARKS ═══
p.add_process_rows_slide(
    title="Where AI takes over and where humans remain essential",
    subtitle="AI/human split at L3 target. Nordic peers at L0-L1 — the gap is the opportunity.",
    section_label="AI vs Human — Target State",
    rows=[
        {"label": "Service — Resolve + detect", "before": "60% AI", "after": "40% Human", "saving": "Empathetic recovery"},
        {"label": "Handoff — Route + brief", "before": "85% AI", "after": "15% Human", "saving": "VIP preferences"},
        {"label": "Advisory — Advise + recommend", "before": "35% AI", "after": "65% Human", "saving": "Strategic advisory, trust"},
        {"label": "Origination — Apply + decide", "before": "75% AI", "after": "25% Human", "saving": "Complex structuring"},
        {"label": "Activation — Onboard + retain", "before": "90% AI", "after": "10% Human", "saving": "Churn intervention"},
    ],
    footer_text="AI highest at edges (service + activation), lowest at center (advisory). Danske Bank furthest at L1-L2. Not replacing people — redirecting them."
)

# ═══ 9. DEMO HANDOFF ═══
p.add_section_divider("Live Platform Demo", "Let's see it\nin action.", "The Unified Frontline — customer + employee on one platform. Micha Kroes, Principal Solutions Engineer.")

# ═══ 10. 5-LAYER CONTROL PLANE ═══
p.add_architecture_stack_slide(
    title="Where each capability lives in the Banking OS",
    subtitle="Five layers. What Micha just showed you operates across them.",
    section_label="The Control Plane",
    layers=[
        {"label": "Interaction — Customers + Employees", "items": [{"name": "Customer Assist (CSR)"}, {"name": "RM/Advisor Workspace"}, {"name": "Customer Apps"}, {"name": "Conversational AI"}], "bg_hex": "#EBF0FF", "accent_hex": "#1A5AFF"},
        {"label": "Orchestration — Executing the Work", "items": [{"name": "Sales Intelligence Agent"}, {"name": "Meeting Prep Agent"}, {"name": "Service-to-Sales Agent"}, {"name": "Follow-Up Agent"}], "bg_hex": "#F5F3FF", "accent_hex": "#7C3AED"},
        {"label": "Authority — Sentinel", "items": [{"name": "Compliance Agent + Policy"}, {"name": "Decision Kernel + Governance"}], "dark": True, "accent_hex": "#F59E0B"},
        {"label": "Semantic — Nexus", "items": [{"name": "Customer State Graph"}, {"name": "Actions + Context Graph"}], "dark": True, "accent_hex": "#16A34A"},
        {"label": "Connectivity — Grand Central", "items": [{"name": "Core Banking"}, {"name": "Dynamics 365 / CRM"}, {"name": "ERP"}, {"name": "Payments"}, {"name": "KYC / AML"}], "bg_hex": "#F5F7F9", "accent_hex": "#5C6E84"},
    ]
)

# ═══ 11. BANKING OS SYSTEM DIAGRAM ═══
p.add_architecture_slide(
    title="The Banking OS — The system that understands, runs + governs the Unified Frontline.",
    subtitle="Customers, employees, and AI agents — orchestrated by a single platform.",
    customer_channels=["Mobile", "Web", "Conversational AI"],
    employee_workspaces=["Customer Assist (CSR)", "RM / Advisor", "Branch", "Operations"],
    platform_label="AI-native Banking OS — Understand · Run · Govern",
    enablement_systems=["Dynamics 365 / CRM", "Agent Studio", "Nexus", "Flow Foundation", "Intelligence Fabric"],
    core_systems=["Core Banking", "Cards", "Payments", "KYC", "Fraud"]
)

# ═══ 12. IGNITE — SCOPED ═══
p.add_tiles_slide(
    title="Ignite — Connected Advisor Assessment for SEB",
    subtitle="A scoped 2-day engagement to quantify the service-to-sale opportunity and build the case for investment. Backbase cooperates with Microsoft — the architecture blueprint addresses Dynamics complementarity.",
    section_label="Next Step",
    columns=2,
    tiles=[
        {"stat": "", "title": "Day 1: Discovery & Validation", "body": "Validate the gaps with SEB's own data.\n\n• Map the current service-to-sale flow\n• Assess maturity (L1 → L2 → L3) per step\n• Identify the engagement platform gap\n• Validate use cases: SME & Privates", "accent": "blue", "pill": "DAY 1"},
        {"stat": "", "title": "Day 2: Architecture & Value Case", "body": "Build the case for investment.\n\n• Design target architecture (Banking OS + Dynamics)\n• Quantify the business case (cross-sell, RM productivity)\n• Build phased roadmap (quick wins → target)\n• Live demo deep-dive: RM workspace", "accent": "green", "pill": "DAY 2"},
    ]
)

# ═══ 13. CLOSE ═══
p.add_section_divider("Over to You", "Where does the\nthread break?", "SEB x Backbase — April 2026")

p.save()
print(f"Saved: {p.output_path}")
print(f"Slides: {len(p.slides)}")
