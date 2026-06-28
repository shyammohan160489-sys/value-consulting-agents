"""
SEB April 14 — Extended Content Master (21-slide deck)
Frontline 2026 PPTX for Google Slides import.
"""
import sys
sys.path.insert(0, '/Users/shyam/cortex')
from tools.frontline_2026_presenter import Frontline2026Presenter

p = Frontline2026Presenter(output_path="/Users/shyam/cortex/Engagement/SEB/Output/SEB_Service_to_Sale_Extended.pptx")

# ═══ 1. COVER ═══
p.add_cover_slide("Backbase x SEB", "From Service to Sale\nThe Connected Advisor", "Stockholm  ·  April 14, 2026")

# ═══ 2. AGENDA ═══
p.add_agenda_slide("AI-Native Banking OS", "Agenda", "Backbase x SEB", [
    "Unified Frontline & Banking OS", "The Service-to-Sale Challenge",
    "The AI-Native Future State", "The Episode: Service Call to Sale",
    "Banking OS & Architecture", "Next Steps — Ignite"
])

# ═══ 3. BACKBASE INTRO ═══
p.add_stat_cards_slide("150+ banks. One platform.", subtitle="Backbase builds the AI-native Banking OS.", stats=[
    {"number": "150+", "label": "Financial institutions"},
    {"number": "€200M+", "label": "Annual revenue"},
    {"number": "2,500+", "label": "People globally"},
])

# ═══ 4. LIFECYCLE ═══
p.add_tiles_slide("Four stages. Today we double-click on two.", section_label="The Customer Lifecycle", columns=4, tiles=[
    {"stat": "", "title": "Acquire", "body": "Onboarding, origination, KYC", "accent": "blue", "pill": "ACQUIRE"},
    {"stat": "", "title": "Activate", "body": "Daily banking, payments, adoption", "accent": "blue", "pill": "ACTIVATE"},
    {"stat": "", "title": "Engage", "body": "Cross-sell, NBA, RM advisory", "accent": "blue", "pill": "ENGAGE  ←  TODAY"},
    {"stat": "", "title": "Retain", "body": "Servicing, human assist, churn", "accent": "blue", "pill": "RETAIN  ←  TODAY"},
])

# ═══ 5. DIVIDER ═══
p.add_section_divider("Let's Double-Click", "Service to Sale\nThe episode that matters.", "What happens next determines whether you retain, engage — or lose.")

# ═══ 6. THREE GAPS ═══
p.add_tiles_slide("The service-to-sales thread is broken", subtitle="Three gaps that bleed value.", section_label="The Problem", columns=3, tiles=[
    {"stat": "1", "title": "The Context Gap", "body": "Agent sees problem but not opportunity. Different system, data.", "accent": "red", "pill": "SILOED DATA"},
    {"stat": "2", "title": "The Handoff Gap", "body": "RM gets calendar invite with no backstory.", "accent": "amber", "pill": "LOST CONTEXT"},
    {"stat": "3", "title": "The Follow-Through Gap", "body": "Activation in yet another system. No thread.", "accent": "red", "pill": "BROKEN ACTIVATION"},
])

# ═══ 7. VALUE LEAKAGE ═══
p.add_process_rows_slide("Where value bleeds across the episode", section_label="Value Leakage", rows=[
    {"label": "Service Call — 5-8 systems", "before": "70-80%", "after": "cross-sell missed", "saving": ""},
    {"label": "Handoff — Manual CRM, email", "before": "40-60%", "after": "leads go cold", "saving": ""},
    {"label": "RM Meeting — 2-4 hrs prep", "before": "40-60%", "after": "RM day on admin", "saving": ""},
    {"label": "Origination — Separate system", "before": "15-30%", "after": "app abandonment", "saving": ""},
    {"label": "Activation — No journey", "before": "0", "after": "pipeline continuity", "saving": ""},
], footer_text="Discovery: Where does the thread break for SEB?")

# ═══ 8. AI MATURITY ═══
p.add_tiles_slide("The path to an AI-native service-to-sale", section_label="Our Point of View", columns=3, tiles=[
    {"stat": "L1", "title": "AI-Assisted", "body": "Human-in-the-loop. AI surfaces insights. Humans decide. Where most banks are heading today.", "accent": "blue", "pill": "LEVEL 1"},
    {"stat": "L2", "title": "AI-Augmented", "body": "Human-on-the-loop. AI acts by default. Humans monitor. 12-18 months on the Banking OS.", "accent": "purple", "pill": "LEVEL 2"},
    {"stat": "L3", "title": "AI-Native", "body": "Human-out-of-the-loop (routine). AI handles routine. Humans focus on advisory. Target state.", "accent": "green", "pill": "LEVEL 3"},
])

# ═══ 9. MATURITY MAPPED ═══
p.add_pillar_rows_slide("The episode at each maturity level", subtitle="Same steps. Different human involvement.", section_label="Maturity Path",
    columns=["L1: AI-Assisted", "L2: AI-Augmented", "L3: AI-Native"],
    rows=[
        {"left": "Service Call", "left_detail": "CSR sees AI flag, decides", "mid": "Agent drafts pitch, CSR confirms", "mid_detail": "", "right": "Conv AI resolves autonomously", "right_detail": ""},
        {"left": "Handoff", "left_detail": "CSR books RM manually", "mid": "System suggests slot, confirms", "mid_detail": "", "right": "Auto-booked, RM notified", "right_detail": ""},
        {"left": "RM Meeting", "left_detail": "AI brief, RM adjusts", "mid": "Brief auto-sent, exceptions", "mid_detail": "", "right": "AI pre-qualifies; RM complex only", "right_detail": ""},
        {"left": "Origination", "left_detail": "Pre-filled, RM validates", "mid": "Auto-initiated, RM approves", "mid_detail": "", "right": "Straight-through processing", "right_detail": ""},
        {"left": "Follow-Up", "left_detail": "AI suggests, RM schedules", "mid": "Auto-scheduled, RM monitors", "mid_detail": "", "right": "Full lifecycle by agents", "right_detail": ""},
    ]
)

# ═══ 10. AI-NATIVE TARGET STATE ═══
p.add_split_comparison("What the RM of 2028 looks like", section_label="The AI-Native Target State",
    left_title="WHAT AI HANDLES",
    left_items=["Opportunity detection — auto-flagging", "Meeting scheduling — auto-booked", "Pre-meeting intelligence — AI briefs", "Pre-approved origination — STP", "Post-sale lifecycle — activation + follow-up", "Compliance — autonomous suitability"],
    right_title="WHAT HUMANS OWN",
    right_items=["Strategic advisory — growth, financing", "Relationship moments — life events", "Exception handling — edge cases", "Trust building — empathy, recovery", "Portfolio oversight — tuning agents"]
)

# ═══ 11. AI vs HUMAN BARS ═══
p.add_process_rows_slide("Where AI takes over and where humans remain essential", section_label="AI vs Human — Target State", rows=[
    {"label": "Service — Resolve + detect", "before": "60% AI", "after": "40% Human", "saving": "Empathetic recovery"},
    {"label": "Handoff — Route + brief", "before": "85% AI", "after": "15% Human", "saving": "VIP preferences"},
    {"label": "Advisory — Advise + recommend", "before": "35% AI", "after": "65% Human", "saving": "Strategic advisory"},
    {"label": "Origination — Apply + decide", "before": "75% AI", "after": "25% Human", "saving": "Complex structuring"},
    {"label": "Activation — Onboard + retain", "before": "90% AI", "after": "10% Human", "saving": "Churn intervention"},
], footer_text="AI highest at edges, lowest at center. Danske at L1-L2. Not replacing — redirecting.")

# ═══ 12. EPISODE DIVIDER ═══
p.add_section_divider("The Episode", "A service call\nbecomes a sale.", "Anna, SME business owner. Five AI agents make the difference.")

# ═══ 13. EPISODE STEPS 1-2 ═══
p.add_split_comparison("Service call → Warm handoff", section_label="The Episode — Steps 1 & 2",
    left_title="STEP 1: SERVICE CALL",
    left_items=["Anna calls about failed payment", "Customer 360: profile, accounts, history", "AI Copilot: business grew 40%", "Resolution: fixed in 2 min", "Service-to-Sales Agent flags opportunity"],
    right_title="STEP 2: WARM HANDOFF",
    right_items=["Anna says yes to RM meeting", "CSR clicks 'Book Advisory Meeting'", "One click, in context — no CRM", "Meeting Prep Agent auto-generates brief", "Context transferred: profile, offer, summary"]
)

# ═══ 14. EPISODE STEPS 3-4 ═══
p.add_split_comparison("RM meeting → Sale & activation", section_label="The Episode — Steps 3 & 4",
    left_title="STEP 3: RM MEETING",
    left_items=["RM opens Advisor Workspace", "AI brief: cash flow, credit line, history", "Knows Anna's story — no 'tell me'", "Sales Intelligence recommends products", "Creates opportunity in pipeline"],
    right_title="STEP 4: SALE & ACTIVATION",
    right_items=["Data pre-filled, auto-decisioning", "Pre-approved — funds same day", "Welcome journey activated", "NBA shifts to merchant services", "Follow-Up Agent: 3-month review"]
)

# ═══ 15. FIVE AGENTS ═══
p.add_tiles_slide("Five agents powering the episode", subtitle="Each reads from Nexus, governed by Sentinel.", section_label="The Agents", columns=5, tiles=[
    {"stat": "", "title": "Sales Intelligence", "body": "Monitors behavior, flags opportunities", "accent": "green", "pill": "ORCHESTRATION"},
    {"stat": "", "title": "Meeting Prep", "body": "Auto-generates RM briefings", "accent": "purple", "pill": "ORCHESTRATION"},
    {"stat": "", "title": "Service-to-Sales", "body": "Cross-sell in live service", "accent": "amber", "pill": "ORCHESTRATION"},
    {"stat": "", "title": "Follow-Up", "body": "Tracks actions, pipeline, reviews", "accent": "blue", "pill": "ORCHESTRATION"},
    {"stat": "", "title": "Compliance", "body": "Suitability checks on every offer", "accent": "cyan", "pill": "AUTHORITY"},
])

# ═══ 16. PRODUCT ACTIVATION ═══
p.add_tiles_slide("Sales → Product Activation & Expansion", section_label="The Dependent Step", columns=4, tiles=[
    {"stat": "", "title": "Digital Lending", "body": "Loan apps, credit lines, mortgages", "accent": "blue", "pill": "ORIGINATION"},
    {"stat": "", "title": "Digital Onboarding", "body": "Account opening, product setup, KYC", "accent": "blue", "pill": "SETUP"},
    {"stat": "", "title": "Digital Engage", "body": "Welcome journeys, feature discovery", "accent": "green", "pill": "ACTIVATION"},
    {"stat": "", "title": "Cross-Lending (CLO)", "body": "Pre-filled, pre-approved, shorter", "accent": "purple", "pill": "EXPANSION"},
])

# ═══ 17. 5-LAYER CONTROL PLANE ═══
p.add_architecture_stack_slide("Where each agent lives in the Banking OS", subtitle="Five layers. Each serves a specific function.", section_label="The Control Plane", layers=[
    {"label": "Interaction — Customers + Employees", "items": [{"name": "Customer Assist (CSR)"}, {"name": "RM/Advisor Workspace"}, {"name": "Customer Apps"}, {"name": "Conversational AI"}], "bg_hex": "#EBF0FF", "accent_hex": "#1A5AFF"},
    {"label": "Orchestration — Executing the Work", "items": [{"name": "Sales Intelligence"}, {"name": "Meeting Prep"}, {"name": "Service-to-Sales"}, {"name": "Follow-Up Agent"}], "bg_hex": "#F5F3FF", "accent_hex": "#7C3AED"},
    {"label": "Authority — Sentinel", "items": [{"name": "Compliance + Policy"}, {"name": "Decision Kernel"}], "dark": True, "accent_hex": "#F59E0B"},
    {"label": "Semantic — Nexus", "items": [{"name": "Customer State Graph"}, {"name": "Actions + Context"}], "dark": True, "accent_hex": "#16A34A"},
    {"label": "Connectivity — Grand Central", "items": [{"name": "Core Banking"}, {"name": "Dynamics 365 / CRM"}, {"name": "Payments"}, {"name": "KYC / AML"}, {"name": "Cards"}], "bg_hex": "#F5F7F9", "accent_hex": "#5C6E84"},
])

# ═══ 18. BANKING OS SYSTEM DIAGRAM ═══
p.add_architecture_slide(
    title="The Banking OS — understands, runs + governs the Unified Frontline.",
    customer_channels=["Mobile", "Web", "Conversational AI"],
    employee_workspaces=["Customer Assist (CSR)", "RM / Advisor", "Branch", "Operations"],
    platform_label="AI-native Banking OS — Understand · Run · Govern",
    enablement_systems=["Dynamics 365 / CRM", "Agent Studio", "Nexus", "Flow Foundation", "Intelligence Fabric"],
    core_systems=["Core Banking", "Cards", "Payments", "KYC", "Fraud"]
)

# ═══ 19. BOOKEND ═══
p.add_tiles_slide("150+ banks. One platform.", subtitle="Everything you saw today runs on the same Banking OS.", section_label="The Platform", columns=4, tiles=[
    {"stat": "", "title": "Digital Assist", "body": "CSR & RM workspaces, Customer 360", "accent": "blue", "pill": "ASSIST"},
    {"stat": "", "title": "Digital Engage", "body": "NBA engine, campaigns, activation", "accent": "green", "pill": "ENGAGE"},
    {"stat": "", "title": "Agentic AI", "body": "Agent Studio, Nexus, Sentinel", "accent": "purple", "pill": "AI"},
    {"stat": "", "title": "Digital Lending", "body": "Origination, CLO, decisioning", "accent": "cyan", "pill": "LENDING"},
])

# ═══ 20. IGNITE ═══
p.add_tiles_slide("Ignite — from conversation to conviction", subtitle="Structured engagement → roadmap + value case. We cooperate with Microsoft — Backbase complements Dynamics.", section_label="The Method", columns=2, tiles=[
    {"stat": "", "title": "Phase 1: Pre-Ignite", "body": "4-6 hours across 2 days.\n\n• Strategic Alignment\n• Customer Experience\n• Employee Experience\n• IT Architecture", "accent": "blue", "pill": "PRE-IGNITE"},
    {"stat": "", "title": "Phase 2: Innovation Day", "body": "1.5 days onsite.\n\n• Art of the Possible\n• Use Case Workshops\n• Build/Buy Decisions\n• Gamified Roadmap", "accent": "green", "pill": "INNOVATION DAY"},
])

# ═══ 21. CLOSE ═══
p.add_section_divider("Over to You", "Where does the\nthread break?", "SEB x Backbase — April 2026")

p.save()
print(f"Saved: {p.output_path}")
print(f"Slides: {len(p.slides)}")
