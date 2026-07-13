"""
Nordea TxB — Strategic POV for Taru Moller (v2)
Restructured consultative flow with speaker notes.
Frontline 2026 HTML + PPTX
Meeting: April 2, 2026 (45 min)
"""
import sys, os, re
sys.path.insert(0, '/Users/shyam/cortex')
from tools.frontline_2026_html import Frontline2026HTML

h = Frontline2026HTML("Nordea Transaction Banking — A Strategic Conversation")

# Speaker notes keyed by slide index (0-based)
NOTES = {}

# ── 1. Cover ──
h.add_cover(
    "Backbase x Nordea",
    "Transaction Banking |A Strategic Conversation",
    "April 2, 2026"
)
NOTES[0] = (
    "SLIDE 1: COVER — 90 seconds max.\n\n"
    "OBJECTIVE: Set the tone. You are not here to sell. You are here to share a "
    "point of view and test it against Taru's reality.\n\n"
    "OPENING: 'Taru, thank you for making time. I know 45 minutes is tight, so "
    "let me be direct about what we want to accomplish today.\n\n"
    "We\'ve spent time studying Nordea\'s 2030 strategy, your March restructuring "
    "announcement, and the publicly stated priorities for transaction banking. "
    "We\'ve also looked at how your peers — ING, ABN AMRO, Danske — are navigating "
    "the same inflection point.\n\n"
    "Rather than a product pitch, I want to share a point of view on where we see "
    "the architecture of transaction banking heading — and test whether it resonates "
    "with what you\'re seeing inside Nordea. We\'d love to hear your priorities and "
    "where the biggest pressure points are. If there\'s a fit, we\'ll talk about "
    "next steps. If not, you\'ll at least have a different lens on the problem.'\n\n"
    "TONE: Confident but not arrogant. You are a peer — a consultant who has seen "
    "this pattern across multiple banks, not a vendor reading a script.\n\n"
    "BODY LANGUAGE: Lean forward. Make eye contact. Don\'t look at slides."
)

# ── 2. The structural shift — Products → Trust → Intent (animated) ──
h.scenes.append('''
    <section class="slide slide--light">
      <style>
        .pti-card { opacity:0; transform:translateX(-30px); }
        .pti-arrow { opacity:0; transform:scale(0.5); }
        .slide.active .pti-card-1 { animation: ptiIn 0.6s 0.3s forwards; }
        .slide.active .pti-arrow-1 { animation: ptiArrow 0.4s 0.8s forwards; }
        .slide.active .pti-card-2 { animation: ptiIn 0.6s 1.1s forwards; }
        .slide.active .pti-arrow-2 { animation: ptiArrow 0.4s 1.6s forwards; }
        .slide.active .pti-card-3 { animation: ptiIn 0.6s 1.9s forwards; }
        .slide.active .pti-footer { animation: ptiFade 0.5s 2.4s forwards; }
        .pti-footer { opacity:0; }
        @keyframes ptiIn { to { opacity:1; transform:translateX(0); } }
        @keyframes ptiArrow { to { opacity:1; transform:scale(1); } }
        @keyframes ptiFade { to { opacity:1; } }
      </style>
      <div class="slide__inner slide__inner--content">
        <span class="label label--dark">OUR OBSERVATION</span>
        <h2 class="slide-title">The architecture of transaction banking is shifting</h2>
        <p class="slide-subtitle">Most banks have built strong products. The question is what connects them &mdash; and what acts on that connection.</p>

        <div style="display:flex; align-items:stretch; gap:0; margin-top:20px; justify-content:center;">

          <!-- Products -->
          <div class="pti-card pti-card-1" style="flex:1; max-width:300px; background:white; border:1.5px solid #FCA5A5; border-top:3px solid #DC2626; border-radius:10px; padding:20px;">
            <span style="display:inline-block; background:#FFF5F5; color:#DC2626; font-size:9px; font-weight:800; letter-spacing:1.5px; padding:3px 10px; border-radius:4px; margin-bottom:10px;">STRONG BUT ISOLATED</span>
            <div style="font-size:36px; font-weight:900; color:#DC2626; margin-bottom:4px;">Products</div>
            <div style="font-size:12px; color:#5C6E84; line-height:1.6;">Banks have built strong products &mdash; vertically, in silos.<br><br>An LC lives in one system. A payment investigation in another. Cash management in a third.<br><br><strong style="color:#001C3D;">The products work. The connections between them are manual.</strong></div>
          </div>

          <!-- Arrow 1 -->
          <div class="pti-arrow pti-arrow-1" style="display:flex; align-items:center; padding:0 16px;">
            <svg width="48" height="24" viewBox="0 0 48 24"><path d="M0 12h40M34 4l8 8-8 8" fill="none" stroke="#D97706" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/></svg>
          </div>

          <!-- Trust -->
          <div class="pti-card pti-card-2" style="flex:1; max-width:300px; background:white; border:1.5px solid #FCD34D; border-top:3px solid #D97706; border-radius:10px; padding:20px;">
            <span style="display:inline-block; background:#FFFBEB; color:#D97706; font-size:9px; font-weight:800; letter-spacing:1.5px; padding:3px 10px; border-radius:4px; margin-bottom:10px;">CONNECTIVE TISSUE</span>
            <div style="font-size:36px; font-weight:900; color:#D97706; margin-bottom:4px;">Trust</div>
            <div style="font-size:12px; color:#5C6E84; line-height:1.6;">Identity, consent, risk, compliance &mdash; not as checkboxes, but as <strong style="color:#001C3D;">shared infrastructure</strong> that connects everything.<br><br>Reusable across products, markets, and channels. The same compliance framework governing an LC, a payment, and an API call.</div>
          </div>

          <!-- Arrow 2 -->
          <div class="pti-arrow pti-arrow-2" style="display:flex; align-items:center; padding:0 16px;">
            <svg width="48" height="24" viewBox="0 0 48 24"><path d="M0 12h40M34 4l8 8-8 8" fill="none" stroke="#1A5AFF" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/></svg>
          </div>

          <!-- Intent -->
          <div class="pti-card pti-card-3" style="flex:1; max-width:300px; background:white; border:1.5px solid #93B5FF; border-top:3px solid #1A5AFF; border-radius:10px; padding:20px;">
            <span style="display:inline-block; background:#EBF0FF; color:#1A5AFF; font-size:9px; font-weight:800; letter-spacing:1.5px; padding:3px 10px; border-radius:4px; margin-bottom:10px;">EMERGING FRONTIER</span>
            <div style="font-size:36px; font-weight:900; color:#1A5AFF; margin-bottom:4px;">Intent</div>
            <div style="font-size:12px; color:#5C6E84; line-height:1.6;">AI that doesn&rsquo;t just report or respond &mdash; it <strong style="color:#001C3D;">acts</strong>.<br><br>An agent that drafts an LC when the facility is ready. An agent that screens sanctions in parallel. An agent that settles when compliance clears &mdash; automatically, within governed boundaries.</div>
          </div>

        </div>

        <div class="pti-footer" style="background:#F0F4FF; border-radius:8px; padding:10px 16px; margin-top:20px; font-size:11px; color:#001C3D; text-align:center; line-height:1.5;">Value is migrating from the product to the trust layer, and from trust to intent. <strong>The banks that connect trust to real-time decisioning at scale</strong> will define the next decade of transaction banking.</div>
      </div>
    </section>''')
NOTES[1] = (
    "SLIDE 2: PRODUCTS → TRUST → INTENT — 3 minutes. This is your intellectual "
    "credibility moment.\n\n"
    "CONTEXT: Taru published a Mobey Forum article making exactly this argument. "
    "You are expressing the same thesis independently, using TxB-specific examples. "
    "If she recognises the parallel, it\'s a trust-building moment.\n\n"
    "OPENING — click to slide, let the animation play (Products appears first):\n\n"
    "'We see the architecture of transaction banking shifting. Not incrementally — "
    "structurally. And it\'s not about faster payments or better channels. It\'s about "
    "where value actually sits.'\n\n"
    "AS PRODUCTS CARD APPEARS:\n"
    "'Most banks — Nordea included — have built genuinely strong products. Your cash "
    "management is ranked number one in the Nordics by Prospera. Your trade finance "
    "operation handles LCs, guarantees, and documentary collections across four "
    "Nordic markets plus international corridors. Your API Market has 14+ aggregator "
    "integrations — one of the most mature open banking platforms in Europe.\n\n"
    "The products work. But they\'re isolated. An LC issuance lives in Trade Finance "
    "Global. A payment investigation lives in a separate ops system. Sanctions "
    "screening sits in a third. Cash management reports liquidity but doesn\'t "
    "connect to trade finance exposure or lending limits. Each product is strong "
    "on its own — the connections between them are manual, email-based, and "
    "fragmented across your four country operations.'\n\n"
    "AS TRUST CARD APPEARS (arrow animates):\n"
    "'The next layer is trust. And I don\'t mean compliance — I mean trust as "
    "shared infrastructure. Identity, consent, risk interpretation — not as "
    "checkboxes you bolt on at the end of each process, but as a connected "
    "framework that works the same way whether you\'re issuing an LC in Stockholm, "
    "screening a sanctions hit in Helsinki, or processing a payment dispute in "
    "Copenhagen. The same compliance framework, the same customer state, the same "
    "governance — reusable across products, across markets, across channels.'\n\n"
    "AS INTENT CARD APPEARS (arrow animates):\n"
    "'And the layer after that — this is what\'s emerging — is intent. AI that "
    "doesn\'t just report or respond to questions, but that acts. An agent that "
    "reads the facility terms from the system and drafts an LC automatically "
    "when the credit approval clears. An agent that screens all counterparties "
    "and vessels against EU and UN sanctions lists in parallel — not one by one, "
    "sequentially, taking 45 minutes each. An agent that triggers SWIFT settlement "
    "the moment compliance status clears — automatically, within governed boundaries, "
    "with a full audit trail.\n\n"
    "That shift — from strong but isolated products, to connected trust "
    "infrastructure, to AI-driven intent orchestration — is what we\'re here to "
    "talk about.'\n\n"
    "PAUSE. Let it land. Watch Taru\'s reaction.\n\n"
    "IF SHE NODS or says 'this is interesting': you\'ve earned credibility. Move on.\n"
    "IF SHE SAYS 'I wrote about this': respond with 'Yes, I read your Mobey Forum "
    "piece. The framing was precise. We see the same shift from an architecture "
    "perspective — and we\'ve built a platform around it.'\n"
    "IF SHE PUSHES BACK: listen. Her objection tells you what she cares about most."
)

# ── 3. The Nordea commitment — hard numbers ──
h.add_stat_cards(
    "Nordea has made a public commitment",
    "The targets are clear. The operating model that delivers them is the open question.",
    stats=[
        {"number": "\u20ac600M", "label": "Gross cost takeout by 2030"},
        {"number": "1,500", "label": "Roles impacted, announced March 17"},
        {"number": "46\u219240%", "label": "Cost-to-income ratio target"},
        {"number": "+50K", "label": "New SME customers by 2030"},
        {"number": "60%", "label": "Workloads on next-gen systems by 2030"},
    ]
)
NOTES[2] = (
    "SLIDE 3: NORDEA COMMITMENT — 90 seconds. Factual, respectful, not critical.\n\n"
    "TRANSITION: 'Let me ground this in your specific context. These are all "
    "public commitments Nordea has made.'\n\n"
    "WALK THROUGH EACH STAT — don\'t just read them, add context:\n\n"
    "€600M: 'Six hundred million in gross cost takeout by 2030. That\'s not a "
    "stretch target — it\'s been communicated to the equity market. Your investors "
    "are pricing it in.'\n\n"
    "1,500: 'Fifteen hundred roles impacted — announced just two weeks ago, on "
    "March 17th. With the €190 million restructuring charge already booked in Q1. "
    "This is not a future plan. It\'s in motion.'\n\n"
    "46→40%: 'Cost-to-income from 46 to 40-42 percent. Three to six points in "
    "four years. For context, most Nordic banks have been stuck in the 42-48 range "
    "for a decade. Moving three points requires structural change, not incremental "
    "optimisation.'\n\n"
    "+50K: 'Fifty thousand new SME customers by 2030. This is the growth mandate — "
    "particularly in Sweden, where Nordea has publicly acknowledged below-natural "
    "market share in small business.'\n\n"
    "60%: 'Sixty percent of workloads on next-gen systems by 2030. That\'s the "
    "technology commitment — modernise the infrastructure while simultaneously "
    "cutting costs and growing volume.'\n\n"
    "CLOSE: 'These targets are clear. The question we keep coming back to is: "
    "what operating model delivers all of them simultaneously?'\n\n"
    "TONE: You are demonstrating that you\'ve done your homework. You know "
    "Nordea\'s strategy as well as an internal stakeholder would. This builds trust."
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
            "stat": "46\u219240%",
            "title": "Cost-to-Income",
            "body": "Three points in four years. Efficiency must improve while serving more customers, across more products, in four Nordic markets.",
            "accent": "blue",
        },
    ],
    footer_text="The commitment is public. **The answer is elastic operations** — scale without linear headcount growth. AI agents execute routine work. Humans govern high-value decisions. One platform orchestrates."
)
NOTES[3] = (
    "SLIDE 4: THE PRODUCTIVITY PARADOX — 2 minutes. This is the core provocation.\n\n"
    "TRANSITION: 'Here\'s what we find interesting — and slightly paradoxical.'\n\n"
    "POINT TO THE THREE TILES AS YOU SPEAK:\n\n"
    "'-1,500 people: The direction is set. Headcount is the cost line being "
    "managed. Nordea\'s restructuring is explicitly about moving from local "
    "processes to Nordic-wide value chains — which means fewer people doing "
    "country-specific work, not more people doing the same work faster.'\n\n"
    "'+50,000 SME customers: But simultaneously, the growth mandate is volume. "
    "More customers means more onboarding, more KYC reviews, more payment "
    "exceptions, more trade finance documentation, more disputes to handle. "
    "Every new customer generates operational load.'\n\n"
    "'46→40% cost-to-income: And the efficiency bar keeps rising. Three points "
    "in four years while serving more customers with fewer people. That\'s not "
    "a linear equation. You can\'t solve it by asking existing teams to work "
    "harder or by adding headcount — you\'ve just committed to cutting headcount.'\n\n"
    "THE PARADOX: 'These three targets only coexist with a fundamentally different "
    "operating model. Not a better version of the current one — a structurally "
    "different one. Where AI handles the routine work at scale. Where humans focus "
    "on high-value advisory and complex decisions. Where one platform orchestrates "
    "across all four Nordic markets instead of four separate country operations.'\n\n"
    "PAUSE HERE. This is the moment Taru either validates or pushes back.\n\n"
    "IF SHE AGREES: 'That\'s exactly the pattern we see. Let me show you what "
    "the answer looks like.'\n"
    "IF SHE SAYS 'we\'re already working on this': 'Tell me more. What\'s the "
    "approach? Where are you furthest along?' (This is discovery.)\n"
    "IF SHE PUSHES BACK: 'Help me understand — which of these three do you "
    "see as most solvable within the current model?' (Redirect to domain map.)"
)

# ── 5. Elastic Operations — full-bleed triangle (replicates company deck slide 24) ──
h.scenes.append('''
    <section class="slide" style="background:#F5F7F9;">
      <div style="position:absolute; inset:0; display:flex; flex-direction:column; align-items:center; justify-content:flex-start; padding:4% 5%;">

        <!-- Title — matches standard Frontline heading -->
        <div style="width:100%; margin-bottom:clamp(8px, 1.5vw, 16px);">
          <span class="label label--dark">BUSINESS OUTCOME</span>
          <h2 class="slide-title">Elastic Operations</h2>
          <p class="slide-subtitle">AI-native operating model &rarr; scale operations + growth, without losing control.</p>
        </div>

        <!-- Triangle — structured as flex column: Growth pill, triangle with Banking OS, bottom row with Efficiency + Control -->
        <div style="display:flex; flex-direction:column; align-items:center; width:80%; max-width:900px; gap:8px;">

          <!-- GROWTH pill — above triangle -->
          <div style="text-align:center;">
            <div style="background:#16A34A; color:white; font-size:13px; font-weight:800; letter-spacing:2.5px; padding:8px 32px; border-radius:8px; display:inline-block;">GROWTH</div>
            <div style="font-size:11px; color:#5C6E84; margin-top:6px; font-weight:600;">Acquire &bull; Retain &bull; Expand</div>
          </div>

          <!-- Triangle SVG with Banking OS text overlaid -->
          <div style="position:relative; width:100%; aspect-ratio:2.4/1;">
            <svg viewBox="0 0 1200 500" preserveAspectRatio="xMidYMid meet" style="width:100%; height:100%;" xmlns="http://www.w3.org/2000/svg">
              <polygon points="600,0 40,500 1160,500" fill="#001C3D" />
            </svg>
            <div style="position:absolute; top:45%; left:50%; transform:translate(-50%,-50%); text-align:center; color:white;">
              <div style="font-size:10px; font-weight:800; letter-spacing:3px; opacity:0.5; margin-bottom:6px;">AI-NATIVE</div>
              <div style="font-size:clamp(22px,2.5vw,38px); font-weight:900;">Banking OS</div>
              <div style="font-size:clamp(10px,0.9vw,13px); font-weight:400; opacity:0.7; margin-top:8px; line-height:1.6;">
                scale without linear headcount growth<br>
                elastic capacity delivered through<br>
                <strong style="opacity:1;">humans + agents + workflows</strong>
              </div>
            </div>
          </div>

          <!-- Bottom row: Efficiency left corner, Control right corner — wider than triangle to sit at edges -->
          <div style="display:flex; justify-content:space-between; width:110%; margin-left:-5%;">
            <div style="text-align:center;">
              <div style="background:#1A5AFF; color:white; font-size:13px; font-weight:800; letter-spacing:2.5px; padding:8px 28px; border-radius:8px; display:inline-block;">EFFICIENCY</div>
              <div style="font-size:11px; color:#5C6E84; margin-top:6px; font-weight:600; line-height:1.5;">Higher throughput &bull; Lower cost-to-serve<br>Agentic Process Automation</div>
            </div>
            <div style="text-align:center;">
              <div style="background:#7C3AED; color:white; font-size:13px; font-weight:800; letter-spacing:2.5px; padding:8px 28px; border-radius:8px; display:inline-block;">CONTROL</div>
              <div style="font-size:11px; color:#5C6E84; margin-top:6px; font-weight:600; line-height:1.5;">Authority &bull; Policy &bull; Proof<br>Decision Authority</div>
            </div>
          </div>

        </div>
      </div>
    </section>''')
NOTES[4] = (
    "SLIDE 5: ELASTIC OPERATIONS — 90 seconds. The answer to the paradox.\n\n"
    "TRANSITION: 'So how do these three targets coexist? Through what we call "
    "elastic operations.'\n\n"
    "POINT TO THE TRIANGLE:\n"
    "'Three levers, all running on the same platform.\n\n"
    "Growth — acquire, retain, expand — without proportional headcount. In trade "
    "finance, this means same-day LC issuance instead of 10-day manual cycles. "
    "In cash management, proactive liquidity alerts instead of reactive reporting. "
    "Your RMs spend time on advisory, not on chasing ops for status updates.\n\n"
    "Efficiency — higher throughput, lower cost-to-serve. This is where agentic "
    "process automation lives. AI agents handling payment exceptions, document "
    "examination, sanctions screening — not as pilots, but as core operations. "
    "ING\'s COO publicly confirmed 25% productivity gain when AI enters an ops "
    "process. ABN AMRO cited AI automation as the explicit enabler of their 5,200 "
    "job cut programme.\n\n"
    "Control — and this is critical for a Nordic systemically important bank — "
    "authority, policy, and proof must apply equally to AI agents and human "
    "operators. You cannot trade governance for speed. Every action, whether "
    "taken by a human or an agent, needs the same identity validation, the same "
    "policy evaluation, the same audit trail. This is not optional in a bank "
    "supervised by Finansinspektionen and the ECB.\n\n"
    "At the centre — the Banking OS. The system that delivers elastic capacity "
    "through humans, agents, and workflows. Scale without linear headcount growth.'\n\n"
    "TRANSITION TO DOMAIN MAP: 'Now — your remit covers several TxB domains. "
    "Let me show you where we see the pressure points.'"
)

# ── 6. TxB Domain Map — THE PIVOT (enhanced with value bleed) ──
h.add_tiles(
    "Your transaction banking remit",
    "Four domains, each with its own pressure points and measurable value at risk.",
    section_label="Where to Focus",
    columns=4,
    tiles=[
        {
            "title": "Payments & Cash Mgmt",
            "body": [
                "ISO 20022 live. Instant payments compliant.",
                "#1 cash management in Nordics.",
                "",
                "**Gap:** exceptions, disputes, sanctions still manual across 4 countries. System reports but doesn't act.",
            ],
            "accent": "red",
            "pill": "HIGH FRICTION",
            "summary": "VALUE AT RISK|$8.9\u201320.5M/yr",
            "summary_accent": "red",
        },
        {
            "title": "Trade Finance",
            "body": [
                "Top-ranked by Prospera.",
                "Trade Finance Global platform.",
                "",
                "**Gap:** document analysis, compliance, sanctions screening remain multi-day processes.",
            ],
            "accent": "amber",
            "pill": "PROCESS GAP",
            "summary": "VALUE AT RISK|$9.5\u201320M/yr",
            "summary_accent": "amber",
        },
        {
            "title": "Entity Onboarding",
            "body": [
                "Complex entity & UBO verification.",
                "Multi-jurisdiction, holding cos.",
                "",
                "**Gap:** 8\u201312 docs, 15\u201325 min review each. Paper-based, 3\u20136 systems, no STP.",
            ],
            "accent": "amber",
            "pill": "ONBOARDING GAP",
            "summary": "VALUE AT RISK|$9.3\u201322M/yr",
            "summary_accent": "amber",
        },
        {
            "title": "Open Banking & APIs",
            "body": [
                "Mature API Market.",
                "14+ aggregator integrations.",
                "",
                "**Gap:** primarily compliance-driven distribution, not strategic embedded finance.",
            ],
            "accent": "blue",
            "pill": "STRATEGIC GAP",
            "summary": "DISTRIBUTION UPSIDE|Untapped",
            "summary_accent": "blue",
        },
    ],
)

# ── 7. Value Bleed — Full Trade Finance Lifecycle (6 steps, Nordic-adapted) ──
h.scenes.append('''
    <section class="slide" style="background:#F5F7F9;">
      <div style="position:absolute; inset:0; padding:4% 5%; display:flex; flex-direction:column; justify-content:flex-start;">

        <!-- Header -->
        <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:10px;">
          <div>
            <span class="label label--dark">PROCESS HEALTH SCAN</span>
            <h2 class="slide-title" style="margin-bottom:4px;">Value Bleed &mdash; Commercial Trade Finance</h2>
          </div>
          <div style="display:flex; gap:14px; align-items:center;">
            <div style="text-align:center;"><div style="font-size:16px; font-weight:900; color:#001C3D;">14&ndash;45 days</div><div style="font-size:8px; color:#5C6E84; font-weight:700;">CYCLE TIME</div></div>
            <div style="text-align:center;"><div style="font-size:16px; font-weight:900; color:#001C3D;">40%</div><div style="font-size:8px; color:#5C6E84; font-weight:700;">STALL RATE</div></div>
            <div style="text-align:center;"><div style="font-size:16px; font-weight:900; color:#001C3D;">6&ndash;12 FTEs</div><div style="font-size:8px; color:#5C6E84; font-weight:700;">PER DEAL</div></div>
            <div style="text-align:center;"><div style="font-size:16px; font-weight:900; color:#001C3D;">12&ndash;20%</div><div style="font-size:8px; color:#5C6E84; font-weight:700;">ERROR RATE</div></div>
            <div style="background:#DC2626; color:white; font-size:10px; font-weight:800; padding:5px 14px; border-radius:20px; letter-spacing:1px;">CRITICAL</div>
          </div>
        </div>

        <!-- Process grid: 6 columns -->
        <div style="display:grid; grid-template-columns:90px repeat(6, 1fr); gap:8px; font-size:9px;">

          <!-- Step headers -->
          <div style="font-weight:700; color:#5C6E84; padding:6px 4px; font-size:8px; letter-spacing:1px;">PROCESS &gt;</div>
          <div style="background:#1A5AFF; color:white; border-radius:6px; padding:8px; text-align:center;"><div style="font-weight:800; font-size:10px;">Facility Setup &amp; Limit Loading</div><div style="opacity:0.7; font-size:8px; margin-top:2px;">Day 0&ndash;5</div></div>
          <div style="background:#1A5AFF; color:white; border-radius:6px; padding:8px; text-align:center;"><div style="font-weight:800; font-size:10px;">LC Issuance &amp; Amendment</div><div style="opacity:0.7; font-size:8px; margin-top:2px;">Day 5&ndash;15</div></div>
          <div style="background:#1A5AFF; color:white; border-radius:6px; padding:8px; text-align:center;"><div style="font-weight:800; font-size:10px;">Doc Examination &amp; Discrepancy</div><div style="opacity:0.7; font-size:8px; margin-top:2px;">Day 10&ndash;30</div></div>
          <div style="background:#1A5AFF; color:white; border-radius:6px; padding:8px; text-align:center;"><div style="font-weight:800; font-size:10px;">Compliance &amp; Sanctions</div><div style="opacity:0.7; font-size:8px; margin-top:2px;">Day 10&ndash;25</div></div>
          <div style="background:#1A5AFF; color:white; border-radius:6px; padding:8px; text-align:center;"><div style="font-weight:800; font-size:10px;">Settlement, Payment &amp; Recon</div><div style="opacity:0.7; font-size:8px; margin-top:2px;">Day 25&ndash;45</div></div>
          <div style="background:#1A5AFF; color:white; border-radius:6px; padding:8px; text-align:center;"><div style="font-weight:800; font-size:10px;">Reporting &amp; Audit Trail</div><div style="opacity:0.7; font-size:8px; margin-top:2px;">Day 35&ndash;45</div></div>

          <!-- CLIENT & RM EXPERIENCE row -->
          <div style="padding:6px 4px; font-weight:700; color:#DC2626; font-size:8px; text-transform:uppercase; letter-spacing:0.5px;">Client &amp; RM Experience</div>
          <div style="background:white; border-radius:4px; padding:6px 8px; border-left:2px solid #FCA5A5;"><strong style="color:#DC2626;">Manual facility forms, no status</strong><br>Paper facility agreement &bull; no digital intake &bull; RM chases ops daily</div>
          <div style="background:white; border-radius:4px; padding:6px 8px; border-left:2px solid #FCA5A5;"><strong style="color:#DC2626;">10-day LC issuance, no tracker</strong><br>Client blind on status &bull; amendments take 3&ndash;5 days &bull; urgency ignored</div>
          <div style="background:white; border-radius:4px; padding:6px 8px; border-left:2px solid #FCA5A5;"><strong style="color:#DC2626;">Discrepancies kill deal timing</strong><br>Silent 5&ndash;7 day review &bull; discrepancy notice delayed &bull; beneficiary misses shipment window</div>
          <div style="background:white; border-radius:4px; padding:6px 8px; border-left:2px solid #FCA5A5;"><strong style="color:#DC2626;">Invisible holds, no ETA</strong><br>Deals frozen silently &bull; 5&ndash;10 day queue &bull; client threatens to cancel</div>
          <div style="background:white; border-radius:4px; padding:6px 8px; border-left:2px solid #FCA5A5;"><strong style="color:#DC2626;">Payment delays destroy trust</strong><br>Settlement T+3 or worse &bull; SWIFT confirmations manual &bull; FX rate disputes common</div>
          <div style="background:white; border-radius:4px; padding:6px 8px; border-left:2px solid #DC2626;"><strong style="color:#DC2626;">No self-serve reporting</strong><br>RM emails ops for utilisation data &bull; audit requests take days &bull; client frustrated</div>

          <!-- OPERATIONS & RISK row -->
          <div style="padding:6px 4px; font-weight:700; color:#DC2626; font-size:8px; text-transform:uppercase; letter-spacing:0.5px;">Operations &amp; Risk</div>
          <div style="background:#FFF5F5; border-radius:4px; padding:6px 8px;"><strong>Manually keys limits into core</strong><br>Re-keys credit approval into core &bull; 2&ndash;3 hrs/deal &bull; no API to credit system</div>
          <div style="background:#FFF5F5; border-radius:4px; padding:6px 8px;"><strong>Manual SWIFT MT700 construction</strong><br>MT700/MT707 typed manually &bull; UCP 600 compliance checked manually &bull; 45&ndash;90 min per LC</div>
          <div style="background:#FFF5F5; border-radius:4px; padding:6px 8px;"><strong>Manual UCP 600 doc check: 8&ndash;12 docs</strong><br>Trade examiner manually checks 8&ndash;12 docs &bull; 3&ndash;4 hrs each &bull; 60&ndash;70% discrepancy rate</div>
          <div style="background:#FFF5F5; border-radius:4px; padding:6px 8px;"><strong>Sequential EU/UN sanctions screening</strong><br>Each party screened separately &bull; false positive rate 8&ndash;12% &bull; manual disposition 45&ndash;60 min each</div>
          <div style="background:#FFF5F5; border-radius:4px; padding:6px 8px;"><strong>Manual SWIFT MT202/MT910 payment</strong><br>Payment instructions re-keyed &bull; FX matched manually &bull; recon takes 2&ndash;3 hrs per deal</div>
          <div style="background:#FFF5F5; border-radius:4px; padding:6px 8px;"><strong>Manual regulatory &amp; client reporting</strong><br>Trade reports built manually in Excel &bull; audit package assembled per request &bull; 4&ndash;6 hrs each</div>
        </div>

        <!-- VALUE BLEED cards -->
        <div style="display:grid; grid-template-columns:90px repeat(6, 1fr); gap:8px; margin-top:16px;">
          <div style="padding:6px 4px; font-weight:700; color:#DC2626; font-size:8px; text-transform:uppercase; letter-spacing:0.5px;">Value<br>Bleed</div>
          <div style="background:white; border:1.5px solid #FCA5A5; border-radius:8px; padding:8px;">
            <div style="font-weight:800; font-size:10px; color:#001C3D;">Facility Setup &amp; Limit Loading</div>
            <div style="font-size:8px; color:#5C6E84; margin-top:4px;">Manual limit re-keying causes 12% error rate and 2&ndash;3 hrs per deal.</div>
            <div style="display:flex; gap:3px; margin-top:4px;"><span style="font-size:7px; background:#DBEAFE; color:#1A5AFF; padding:1px 5px; border-radius:3px; font-weight:700;">Efficiency</span><span style="font-size:7px; background:#F5F3FF; color:#7C3AED; padding:1px 5px; border-radius:3px; font-weight:700;">Control</span></div>
            <div style="font-size:16px; font-weight:900; color:#DC2626; margin-top:4px;">&euro;0.8&ndash;2M</div>
          </div>
          <div style="background:white; border:1.5px solid #FCA5A5; border-radius:8px; padding:8px;">
            <div style="font-weight:800; font-size:10px; color:#001C3D;">LC Issuance &amp; Amendment</div>
            <div style="font-size:8px; color:#5C6E84; margin-top:4px;">45&ndash;90 min per LC with 15% amendment rate. 40% of deals stall awaiting issuance.</div>
            <div style="display:flex; gap:3px; margin-top:4px;"><span style="font-size:7px; background:#DBEAFE; color:#1A5AFF; padding:1px 5px; border-radius:3px; font-weight:700;">Efficiency</span><span style="font-size:7px; background:#F0FDF4; color:#16A34A; padding:1px 5px; border-radius:3px; font-weight:700;">Growth</span><span style="font-size:7px; background:#F5F3FF; color:#7C3AED; padding:1px 5px; border-radius:3px; font-weight:700;">Control</span></div>
            <div style="font-size:16px; font-weight:900; color:#DC2626; margin-top:4px;">&euro;2.5&ndash;6M</div>
          </div>
          <div style="background:white; border:1.5px solid #FCA5A5; border-radius:8px; padding:8px;">
            <div style="font-weight:800; font-size:10px; color:#001C3D;">Doc Examination &amp; Discrepancy</div>
            <div style="font-size:8px; color:#5C6E84; margin-top:4px;">UCP 600 examination of 8&ndash;12 docs takes 3&ndash;4 hrs with 60&ndash;70% discrepancy rate.</div>
            <div style="display:flex; gap:3px; margin-top:4px;"><span style="font-size:7px; background:#DBEAFE; color:#1A5AFF; padding:1px 5px; border-radius:3px; font-weight:700;">Efficiency</span><span style="font-size:7px; background:#F5F3FF; color:#7C3AED; padding:1px 5px; border-radius:3px; font-weight:700;">Control</span><span style="font-size:7px; background:#F0FDF4; color:#16A34A; padding:1px 5px; border-radius:3px; font-weight:700;">Growth</span></div>
            <div style="font-size:16px; font-weight:900; color:#DC2626; margin-top:4px;">&euro;3&ndash;8M</div>
          </div>
          <div style="background:white; border:1.5px solid #FCA5A5; border-radius:8px; padding:8px;">
            <div style="font-weight:800; font-size:10px; color:#001C3D;">Compliance &amp; Sanctions Check</div>
            <div style="font-size:8px; color:#5C6E84; margin-top:4px;">Sequential EU/UN screening with 8&ndash;12% false positive. Deals frozen, 20% client churn risk.</div>
            <div style="display:flex; gap:3px; margin-top:4px;"><span style="font-size:7px; background:#F5F3FF; color:#7C3AED; padding:1px 5px; border-radius:3px; font-weight:700;">Control</span><span style="font-size:7px; background:#DBEAFE; color:#1A5AFF; padding:1px 5px; border-radius:3px; font-weight:700;">Efficiency</span><span style="font-size:7px; background:#F0FDF4; color:#16A34A; padding:1px 5px; border-radius:3px; font-weight:700;">Growth</span></div>
            <div style="font-size:16px; font-weight:900; color:#DC2626; margin-top:4px;">&euro;2&ndash;5M</div>
          </div>
          <div style="background:white; border:1.5px solid #FCA5A5; border-radius:8px; padding:8px;">
            <div style="font-weight:800; font-size:10px; color:#001C3D;">Settlement, Payment &amp; Recon</div>
            <div style="font-size:8px; color:#5C6E84; margin-top:4px;">Manual SWIFT MT202 re-keying and FX recon add T+3 delays with 14% error rate.</div>
            <div style="display:flex; gap:3px; margin-top:4px;"><span style="font-size:7px; background:#DBEAFE; color:#1A5AFF; padding:1px 5px; border-radius:3px; font-weight:700;">Efficiency</span><span style="font-size:7px; background:#F5F3FF; color:#7C3AED; padding:1px 5px; border-radius:3px; font-weight:700;">Control</span></div>
            <div style="font-size:16px; font-weight:900; color:#DC2626; margin-top:4px;">&euro;1.5&ndash;4M</div>
          </div>
          <div style="background:white; border:1.5px solid #DC2626; border-radius:8px; padding:8px;">
            <div style="font-weight:800; font-size:10px; color:#001C3D;">Reporting &amp; Audit Trail</div>
            <div style="font-size:8px; color:#5C6E84; margin-top:4px;">Trade reports built manually. 5% CTR error rate creates regulatory penalty exposure.</div>
            <div style="display:flex; gap:3px; margin-top:4px;"><span style="font-size:7px; background:#F5F3FF; color:#7C3AED; padding:1px 5px; border-radius:3px; font-weight:700;">Control</span><span style="font-size:7px; background:#DBEAFE; color:#1A5AFF; padding:1px 5px; border-radius:3px; font-weight:700;">Efficiency</span></div>
            <div style="font-size:16px; font-weight:900; color:#DC2626; margin-top:4px;">&euro;0.6&ndash;1.5M</div>
          </div>
        </div>

        <!-- Timeline bar -->
        <div style="display:grid; grid-template-columns:90px repeat(6, 1fr); gap:8px; margin-top:16px;">
          <div style="font-size:8px; font-weight:700; color:#5C6E84; padding:4px;">TIMELINE</div>
          <div style="text-align:center;"><div style="background:linear-gradient(90deg, #DC2626, #F87171); height:4px; border-radius:2px; margin-bottom:4px;"></div><div style="font-size:10px; font-weight:800; color:#001C3D;">Day 0&ndash;5</div><div style="font-size:8px; color:#16A34A; font-weight:700;">Benchmark: 1 day</div></div>
          <div style="text-align:center;"><div style="background:linear-gradient(90deg, #DC2626, #F87171); height:4px; border-radius:2px; margin-bottom:4px;"></div><div style="font-size:10px; font-weight:800; color:#001C3D;">Day 5&ndash;15</div><div style="font-size:8px; color:#16A34A; font-weight:700;">Benchmark: same day</div></div>
          <div style="text-align:center;"><div style="background:linear-gradient(90deg, #DC2626, #F87171); height:4px; border-radius:2px; margin-bottom:4px;"></div><div style="font-size:10px; font-weight:800; color:#001C3D;">Day 10&ndash;30</div><div style="font-size:8px; color:#16A34A; font-weight:700;">Benchmark: hours</div></div>
          <div style="text-align:center;"><div style="background:linear-gradient(90deg, #DC2626, #F87171); height:4px; border-radius:2px; margin-bottom:4px;"></div><div style="font-size:10px; font-weight:800; color:#001C3D;">Day 10&ndash;25</div><div style="font-size:8px; color:#16A34A; font-weight:700;">Benchmark: minutes</div></div>
          <div style="text-align:center;"><div style="background:linear-gradient(90deg, #DC2626, #F87171); height:4px; border-radius:2px; margin-bottom:4px;"></div><div style="font-size:10px; font-weight:800; color:#001C3D;">Day 25&ndash;45</div><div style="font-size:8px; color:#16A34A; font-weight:700;">Benchmark: same day</div></div>
          <div style="text-align:center;"><div style="background:linear-gradient(90deg, #DC2626, #F87171); height:4px; border-radius:2px; margin-bottom:4px;"></div><div style="font-size:10px; font-weight:800; color:#001C3D;">Day 35&ndash;45</div><div style="font-size:8px; color:#16A34A; font-weight:700;">Benchmark: automated</div></div>
        </div>
      </div>
    </section>''')
NOTES[6] = (
    "SLIDE 7: VALUE BLEED — TRADE FINANCE LIFECYCLE — 3 minutes.\n\n"
    "This is where you demonstrate deep domain knowledge. Walk the lifecycle.\n\n"
    "OPENING: 'This is a process health scan of the full trade finance lifecycle. "
    "Six steps, from facility setup through post-transaction reporting. Let me "
    "walk you through where the cost leaks — and more importantly, where clients "
    "feel it.'\n\n"
    "STEP 1 — Facility Setup (Day 0-5):\n"
    "'It starts before the first LC. Facility limits are manually re-keyed from "
    "the credit approval into core banking. No API between the credit system and "
    "the trade platform. 12% error rate on limit loading. Every error triggers a "
    "facility fee dispute downstream — and your RM is chasing ops instead of "
    "advising clients.'\n\n"
    "STEP 2 — LC Issuance (Day 5-15):\n"
    "'Your trade ops teams are still constructing SWIFT MT700 messages by hand. "
    "That\'s 45 to 90 minutes per LC. UCP 600 compliance — all 39 articles — "
    "checked manually against the facility terms. Amendments via MT707 take 3 to "
    "5 additional days. Meanwhile, 40% of deals stall at issuance. The client "
    "can\'t see status. The RM can\'t see status. Urgency is ignored because "
    "there\'s no tracker. That\'s over €2 million in fee income at risk annually "
    "from deals that stall or go to competitors who can issue faster.'\n\n"
    "STEP 3 — Document Examination (Day 10-30):\n"
    "'This is the biggest single cost driver. The trade examiner manually checks "
    "8 to 12 documents per LC against UCP 600 and ISBP 745. Bill of lading, "
    "commercial invoice, packing list, certificate of origin, insurance certificate "
    "— each one cross-referenced against the LC terms. 3 to 4 hours per examination. "
    "And the industry discrepancy rate is 60 to 70% — that\'s an ICC-documented "
    "statistic, not our estimate. Every discrepancy triggers a re-submission cycle. "
    "No OCR, no auto-check — paper documents still scanned manually. This is where "
    "clients abandon at the highest-value deal stage. €3 to 8 million in bleed.'\n\n"
    "STEP 4 — Compliance & Sanctions (Day 10-25):\n"
    "'Sequential screening against EU Council sanctions, UN sanctions, and national "
    "lists — Sweden via ISP, Finland via their FIU. Each party — applicant, "
    "beneficiary, vessel, port of loading — screened one at a time. False positive "
    "rate of 8 to 12%. Each false positive takes 45 to 60 minutes to disposition "
    "manually. Deals frozen silently — the client sees no status, gets no ETA, and "
    "threatens to move the relationship. In the current EU sanctions environment "
    "— particularly with Russia-related trade restrictions — this is also €10 million "
    "or more in regulatory penalty exposure.'\n\n"
    "STEP 5 — Settlement (Day 25-45):\n"
    "'Manual SWIFT MT202 and MT910 payment messaging. Payment instructions re-keyed "
    "into FIS. FX matched manually. Recon takes 2 to 3 hours per deal. Settlement "
    "delays of T+3 or worse — and every day of delay is a day the client\'s cash "
    "is trapped. FX rate disputes are common because the rate at booking doesn\'t "
    "match the rate at settlement.'\n\n"
    "STEP 6 — Reporting & Audit (Day 35-45):\n"
    "'Trade reports built manually in Excel. No self-serve reporting for clients or "
    "RMs. Audit packages assembled per request — 4 to 6 hours each. Regulatory "
    "filings for CTR and FFIIEC done manually with a 5% error rate that creates "
    "direct regulatory penalty exposure.'\n\n"
    "CLOSE: 'Total value bleed across this lifecycle: €9 to 23 million per year. "
    "14 to 45 day cycle time. 40% deal stall rate. And for Nordea, operating at "
    "your scale across four Nordic markets plus international corridors, the actual "
    "numbers are likely significantly higher.\n\n"
    "Now let me show you what happens when you run this same lifecycle through "
    "the Banking OS.'"
)
NOTES[5] = (
    "SLIDE 6: TxB DOMAIN MAP — THIS IS THE PIVOT. 2 minutes.\n\n"
    "Stop presenting. Start a conversation.\n\n"
    "PITCH: 'Taru, your remit cuts across all of these domains. Each one has "
    "its own pressure points — and each one has a measurable value bleed that "
    "we can quantify.'\n\n"
    "WALK THROUGH BRIEFLY — don\'t deep-dive, just signal expertise:\n\n"
    "'Payments and cash management — your infrastructure is modern. ISO 20022 "
    "is live, instant payments compliant, Global Cash Pool is market-leading. "
    "But the operations around it — exceptions, disputes, reconciliation — are "
    "still manual across four country systems. We see $8.9 to 20.5 million in "
    "annual value leakage in comparable operations.\n\n"
    "Trade finance — top-ranked by Prospera, strong LC and guarantee capability. "
    "But SWIFT MT700 messages constructed by hand, UCP 600 compliance checked "
    "manually, sequential sanctions screening. 14 to 45 day lifecycle for what "
    "should take 1 to 3 days.\n\n"
    "Entity onboarding — complex multi-jurisdiction structures, UBO verification "
    "across Nordic and international holding companies. 8 to 12 documents per "
    "entity, 15 to 25 minutes per document review. No straight-through processing.\n\n"
    "Open banking and APIs — mature API Market, but primarily compliance-driven "
    "distribution. The strategic opportunity is embedded finance — exposing TxB "
    "services inside corporate ERPs, treasury management systems, billing "
    "platforms.'\n\n"
    "THE ASK: 'I have depth on all four. But to make the next 15 minutes as "
    "useful as possible for you — which of these is the immediate priority? "
    "Where would you like to double-click?'\n\n"
    "WAIT. Let her choose.\n\n"
    "MOST LIKELY: Trade finance or payments. If she says \'all of them\': "
    "'Let me take you through trade finance as an example — it\'s the most "
    "complex lifecycle and connects to the others.'"
)

# ── 8. Banking OS Simulation — Trade Finance future state ──
# Custom HTML: simplified matrix showing 6 process steps with agents at each layer
h.scenes.append('''
    <section class="slide" style="background:#F5F7F9;">
      <div style="position:absolute; inset:0; padding:4% 5%; display:flex; flex-direction:column; justify-content:flex-start;">
        <!-- Header -->
        <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:14px;">
          <div>
            <span class="label label--dark">FUTURE STATE</span>
            <h2 class="slide-title" style="margin-bottom:4px;">Banking OS in action &mdash; Trade Finance</h2>
            <p class="slide-subtitle" style="margin-bottom:8px;">How six agents orchestrate the LC lifecycle through five Banking OS layers. 14&ndash;45 days &rarr; 1&ndash;3 days.</p>
          </div>
          <div style="display:flex; gap:16px; align-items:center;">
            <div style="text-align:center;"><div style="font-size:18px; font-weight:900; color:#16A34A;">1&ndash;3 days</div><div style="font-size:9px; color:#5C6E84; font-weight:700;">CYCLE TIME</div></div>
            <div style="text-align:center;"><div style="font-size:18px; font-weight:900; color:#16A34A;">&lt;5%</div><div style="font-size:9px; color:#5C6E84; font-weight:700;">STALL RATE</div></div>
            <div style="text-align:center;"><div style="font-size:18px; font-weight:900; color:#16A34A;">&lt;2%</div><div style="font-size:9px; color:#5C6E84; font-weight:700;">ERROR RATE</div></div>
            <div style="background:#16A34A; color:white; font-size:11px; font-weight:800; padding:6px 16px; border-radius:20px; letter-spacing:1px;">HEALTHY</div>
          </div>
        </div>

        <!-- Simulation Grid — light theme -->
        <div style="background:white; border:1.5px solid #E2E8F0; border-radius:12px; padding:18px; overflow:hidden;">
          <!-- Column headers -->
          <div style="display:grid; grid-template-columns:120px repeat(6, 1fr); gap:8px; margin-bottom:10px;">
            <div style="font-size:9px; font-weight:700; color:#5C6E84; letter-spacing:1px; padding:4px;">PROCESS &gt;</div>
            <div style="background:#1A5AFF; border-radius:6px; padding:8px 10px; text-align:center;"><div style="font-size:10px; font-weight:800; color:white; letter-spacing:0.5px;">Facility Setup</div><div style="font-size:8px; color:rgba(255,255,255,0.7); margin-top:2px;">Hours</div></div>
            <div style="background:#1A5AFF; border-radius:6px; padding:8px 10px; text-align:center;"><div style="font-size:10px; font-weight:800; color:white; letter-spacing:0.5px;">LC Issuance</div><div style="font-size:8px; color:rgba(255,255,255,0.7); margin-top:2px;">Same Day</div></div>
            <div style="background:#1A5AFF; border-radius:6px; padding:8px 10px; text-align:center;"><div style="font-size:10px; font-weight:800; color:white; letter-spacing:0.5px;">Doc Examination</div><div style="font-size:8px; color:rgba(255,255,255,0.7); margin-top:2px;">Hours</div></div>
            <div style="background:#1A5AFF; border-radius:6px; padding:8px 10px; text-align:center;"><div style="font-size:10px; font-weight:800; color:white; letter-spacing:0.5px;">Sanctions Check</div><div style="font-size:8px; color:rgba(255,255,255,0.7); margin-top:2px;">Minutes</div></div>
            <div style="background:#1A5AFF; border-radius:6px; padding:8px 10px; text-align:center;"><div style="font-size:10px; font-weight:800; color:white; letter-spacing:0.5px;">Settlement</div><div style="font-size:8px; color:rgba(255,255,255,0.7); margin-top:2px;">Same Day</div></div>
            <div style="background:#1A5AFF; border-radius:6px; padding:8px 10px; text-align:center;"><div style="font-size:10px; font-weight:800; color:white; letter-spacing:0.5px;">Reporting</div><div style="font-size:8px; color:rgba(255,255,255,0.7); margin-top:2px;">Automated</div></div>
          </div>

          <!-- Layer rows -->
          <div style="display:grid; grid-template-columns:120px repeat(6, 1fr); gap:8px; font-size:9px; color:#001C3D;">
            <!-- Interaction -->
            <div style="padding:6px 8px; font-weight:700; color:#1A5AFF; font-size:9px; border-left:2px solid #1A5AFF;">Interaction<br>Layer</div>
            <div style="background:#F0F4FF; border-radius:4px; padding:6px 8px;"><strong>RM Workspace</strong><br>Limits, collateral loaded from NEXUS</div>
            <div style="background:#F0F4FF; border-radius:4px; padding:6px 8px;"><strong>RM + Client Portal</strong><br>LC auto-drafted, one-click approve</div>
            <div style="background:#F0F4FF; border-radius:4px; padding:6px 8px;"><strong>Case Manager</strong><br>Auto-examined doc set, discrepancies highlighted</div>
            <div style="background:#F0F4FF; border-radius:4px; padding:6px 8px;"><strong>Case Manager</strong><br>Live screening dashboard, no manual lookups</div>
            <div style="background:#F0F4FF; border-radius:4px; padding:6px 8px;"><strong>RM Workspace</strong><br>Payment confirmation, recon status live</div>
            <div style="background:#F0F4FF; border-radius:4px; padding:6px 8px;"><strong>RM + Case Manager</strong><br>Full audit bundle auto-assembled</div>

            <!-- Orchestration -->
            <div style="padding:6px 8px; font-weight:700; color:#7C3AED; font-size:9px; border-left:2px solid #7C3AED;">Orchestration<br>Layer</div>
            <div style="background:#F5F3FF; border-radius:4px; padding:6px 8px;"><strong>Facility Setup Agent</strong><br>Auto-loads sublimits, enforces limit authority</div>
            <div style="background:#F5F3FF; border-radius:4px; padding:6px 8px;"><strong>LC Drafting Agent</strong><br>Auto-generates LC, NLP validates UCP 600</div>
            <div style="background:#F5F3FF; border-radius:4px; padding:6px 8px;"><strong>Doc Examination Agent</strong><br>IDP extracts 50+ fields, checks against UCP 600</div>
            <div style="background:#F5F3FF; border-radius:4px; padding:6px 8px;"><strong>Trade Sanctions Agent</strong><br>All parties screened in parallel, SENTINEL gates</div>
            <div style="background:#F5F3FF; border-radius:4px; padding:6px 8px;"><strong>Settlement Agent</strong><br>Auto-matches nostro, triggers payment release</div>
            <div style="background:#F5F3FF; border-radius:4px; padding:6px 8px;"><strong>Reporting Agent</strong><br>Complete transaction chain from NEXUS state</div>

            <!-- Control / Sentinel -->
            <div style="padding:6px 8px; font-weight:700; color:#D97706; font-size:9px; border-left:2px solid #D97706;">Control<br>(Sentinel)</div>
            <div style="background:#FFFBEB; border-radius:4px; padding:6px 8px; color:#5C6E84;">Sublimit parameters validated. Exceptions trigger RM + credit co-approval.</div>
            <div style="background:#FFFBEB; border-radius:4px; padding:6px 8px; color:#5C6E84;">LC value &le; facility sublimit = agent autonomy. UCP 600 violations auto-blocked.</div>
            <div style="background:#FFFBEB; border-radius:4px; padding:6px 8px; color:#5C6E84;">Discrepancy severity from ML gates auto-accept vs. human review.</div>
            <div style="background:#FFFBEB; border-radius:4px; padding:6px 8px; color:#5C6E84;">EU, UN sanctions. Vessel + port of loading risk. Dual-use HS code check.</div>
            <div style="background:#FFFBEB; border-radius:4px; padding:6px 8px; color:#5C6E84;">Payment only released if NEXUS state: Compliance Cleared confirmed.</div>
            <div style="background:#FFFBEB; border-radius:4px; padding:6px 8px; color:#5C6E84;">Audit trail completeness validated. Regulatory auto-filed per jurisdiction.</div>

            <!-- Semantic / Nexus -->
            <div style="padding:6px 8px; font-weight:700; color:#16A34A; font-size:9px; border-left:2px solid #16A34A;">Semantic<br>(Nexus)</div>
            <div style="background:#F0FDF4; border-radius:4px; padding:6px 8px; font-style:italic; color:#5C6E84;">State: Facility Active</div>
            <div style="background:#F0FDF4; border-radius:4px; padding:6px 8px; font-style:italic; color:#5C6E84;">State: LC Issued</div>
            <div style="background:#F0FDF4; border-radius:4px; padding:6px 8px; font-style:italic; color:#5C6E84;">State: Docs Under Review</div>
            <div style="background:#F0FDF4; border-radius:4px; padding:6px 8px; font-style:italic; color:#5C6E84;">State: Compliance Cleared</div>
            <div style="background:#F0FDF4; border-radius:4px; padding:6px 8px; font-style:italic; color:#5C6E84;">State: Settled</div>
            <div style="background:#F0FDF4; border-radius:4px; padding:6px 8px; font-style:italic; color:#5C6E84;">State: Lifecycle Persisted</div>

            <!-- Connectivity -->
            <div style="padding:6px 8px; font-weight:700; color:#5C6E84; font-size:9px; border-left:2px solid #5C6E84;">Connectivity<br>(Grand Central)</div>
            <div style="background:#F5F7F9; border-radius:4px; padding:6px 8px; color:#5C6E84;">Core Banking &bull; Limits Engine &bull; Credit Risk</div>
            <div style="background:#F5F7F9; border-radius:4px; padding:6px 8px; color:#5C6E84;">SWIFT Network &bull; Correspondent Bank API</div>
            <div style="background:#F5F7F9; border-radius:4px; padding:6px 8px; color:#5C6E84;">IDP Engine &bull; Doc Mgmt &bull; Trade Ops Portal</div>
            <div style="background:#F5F7F9; border-radius:4px; padding:6px 8px; color:#5C6E84;">EU Sanctions DB &bull; Compliance Screening</div>
            <div style="background:#F5F7F9; border-radius:4px; padding:6px 8px; color:#5C6E84;">Core Banking &bull; Nostro Mgmt &bull; FX</div>
            <div style="background:#F5F7F9; border-radius:4px; padding:6px 8px; color:#5C6E84;">Reg Reporting &bull; Audit Ledger &bull; Archive</div>
          </div>
        </div>

        <!-- Agent outcomes bar -->
        <div style="display:grid; grid-template-columns:120px repeat(6, 1fr); gap:8px; margin-top:14px;">
          <div style="font-size:9px; font-weight:700; color:#16A34A; padding:4px; letter-spacing:1px;">VALUE<br>RECOVERED</div>
          <div style="background:#F0FDF4; border:1px solid #86EFAC; border-radius:8px; padding:8px 10px; text-align:center;"><div style="font-size:10px; font-weight:800; color:#16A34A;">&check; Facility Setup Agent</div><div style="font-size:9px; color:#5C6E84; margin-top:2px;">Same Day vs 3&ndash;5 Days</div><div style="display:flex; gap:4px; justify-content:center; margin-top:4px;"><span style="font-size:8px; background:#DBEAFE; color:#1A5AFF; padding:1px 6px; border-radius:4px; font-weight:700;">Efficiency</span><span style="font-size:8px; background:#F5F3FF; color:#7C3AED; padding:1px 6px; border-radius:4px; font-weight:700;">Control</span></div></div>
          <div style="background:#F0FDF4; border:1px solid #86EFAC; border-radius:8px; padding:8px 10px; text-align:center;"><div style="font-size:10px; font-weight:800; color:#16A34A;">&check; LC Drafting Agent</div><div style="font-size:9px; color:#5C6E84; margin-top:2px;">85% effort saved</div><div style="display:flex; gap:4px; justify-content:center; margin-top:4px;"><span style="font-size:8px; background:#DBEAFE; color:#1A5AFF; padding:1px 6px; border-radius:4px; font-weight:700;">Efficiency</span><span style="font-size:8px; background:#F0FDF4; color:#16A34A; padding:1px 6px; border-radius:4px; font-weight:700;">Growth</span></div></div>
          <div style="background:#F0FDF4; border:1px solid #86EFAC; border-radius:8px; padding:8px 10px; text-align:center;"><div style="font-size:10px; font-weight:800; color:#16A34A;">&check; Doc Exam Agent</div><div style="font-size:9px; color:#5C6E84; margin-top:2px;">90% faster</div><div style="display:flex; gap:4px; justify-content:center; margin-top:4px;"><span style="font-size:8px; background:#DBEAFE; color:#1A5AFF; padding:1px 6px; border-radius:4px; font-weight:700;">Efficiency</span><span style="font-size:8px; background:#F5F3FF; color:#7C3AED; padding:1px 6px; border-radius:4px; font-weight:700;">Control</span></div></div>
          <div style="background:#F0FDF4; border:1px solid #86EFAC; border-radius:8px; padding:8px 10px; text-align:center;"><div style="font-size:10px; font-weight:800; color:#16A34A;">&check; Sanctions Agent</div><div style="font-size:9px; color:#5C6E84; margin-top:2px;">Minutes vs 2 Days</div><div style="display:flex; gap:4px; justify-content:center; margin-top:4px;"><span style="font-size:8px; background:#F5F3FF; color:#7C3AED; padding:1px 6px; border-radius:4px; font-weight:700;">Control</span></div></div>
          <div style="background:#F0FDF4; border:1px solid #86EFAC; border-radius:8px; padding:8px 10px; text-align:center;"><div style="font-size:10px; font-weight:800; color:#16A34A;">&check; Settlement Agent</div><div style="font-size:9px; color:#5C6E84; margin-top:2px;">Same Day</div><div style="display:flex; gap:4px; justify-content:center; margin-top:4px;"><span style="font-size:8px; background:#DBEAFE; color:#1A5AFF; padding:1px 6px; border-radius:4px; font-weight:700;">Efficiency</span><span style="font-size:8px; background:#F5F3FF; color:#7C3AED; padding:1px 6px; border-radius:4px; font-weight:700;">Control</span></div></div>
          <div style="background:#F0FDF4; border:1px solid #86EFAC; border-radius:8px; padding:8px 10px; text-align:center;"><div style="font-size:10px; font-weight:800; color:#16A34A;">&check; Reporting Agent</div><div style="font-size:9px; color:#5C6E84; margin-top:2px;">100% traceable</div><div style="display:flex; gap:4px; justify-content:center; margin-top:4px;"><span style="font-size:8px; background:#F5F3FF; color:#7C3AED; padding:1px 6px; border-radius:4px; font-weight:700;">Control</span></div></div>
        </div>

        <!-- Timeline bar — future state -->
        <div style="display:grid; grid-template-columns:120px repeat(6, 1fr); gap:8px; margin-top:12px;">
          <div style="font-size:8px; font-weight:700; color:#5C6E84; padding:4px; letter-spacing:1px;">TIMELINE</div>
          <div style="text-align:center;"><div style="background:linear-gradient(90deg, #16A34A, #4ADE80); height:4px; border-radius:2px; margin-bottom:4px;"></div><div style="font-size:10px; font-weight:800; color:#16A34A;">Hours</div><div style="font-size:8px; color:#5C6E84;">Auto Provisioned</div></div>
          <div style="text-align:center;"><div style="background:linear-gradient(90deg, #16A34A, #4ADE80); height:4px; border-radius:2px; margin-bottom:4px;"></div><div style="font-size:10px; font-weight:800; color:#16A34A;">Same Day</div><div style="font-size:8px; color:#5C6E84;">85% Effort Saved</div></div>
          <div style="text-align:center;"><div style="background:linear-gradient(90deg, #16A34A, #4ADE80); height:4px; border-radius:2px; margin-bottom:4px;"></div><div style="font-size:10px; font-weight:800; color:#16A34A;">Hours</div><div style="font-size:8px; color:#5C6E84;">90% Faster</div></div>
          <div style="text-align:center;"><div style="background:linear-gradient(90deg, #16A34A, #4ADE80); height:4px; border-radius:2px; margin-bottom:4px;"></div><div style="font-size:10px; font-weight:800; color:#16A34A;">Minutes</div><div style="font-size:8px; color:#5C6E84;">Real-Time Screened</div></div>
          <div style="text-align:center;"><div style="background:linear-gradient(90deg, #16A34A, #4ADE80); height:4px; border-radius:2px; margin-bottom:4px;"></div><div style="font-size:10px; font-weight:800; color:#16A34A;">Same Day</div><div style="font-size:8px; color:#5C6E84;">Straight-Through</div></div>
          <div style="text-align:center;"><div style="background:linear-gradient(90deg, #16A34A, #4ADE80); height:4px; border-radius:2px; margin-bottom:4px;"></div><div style="font-size:10px; font-weight:800; color:#16A34A;">Automated</div><div style="font-size:8px; color:#5C6E84;">100% Traceable</div></div>
        </div>
      </div>
    </section>''')
NOTES[7] = (
    "SLIDE 8: BANKING OS SIMULATION — 2-3 minutes. The future state.\n\n"
    "TRANSITION: 'Same six steps. Same lifecycle. But now each step is handled "
    "by a specialised agent operating through the Banking OS layers.'\n\n"
    "DON\'T READ EVERY CELL. Hit the highlights that contrast with the pain "
    "you just described:\n\n"
    "FACILITY SETUP: 'The Facility Setup Agent auto-loads sublimits directly from "
    "the credit approval into the trade platform. No re-keying. Sentinel — our "
    "authority layer — validates every limit parameter and triggers RM plus credit "
    "officer co-approval only for exceptions. Hours instead of days.'\n\n"
    "LC ISSUANCE: 'The LC Drafting Agent reads the facility terms from Nexus — our "
    "semantic layer — and auto-generates the MT700. The NLP model validates every "
    "clause against UCP 600. The RM sees a drafted LC in their workspace and "
    "approves with one click. Same-day issuance. That 40% stall rate drops to "
    "under 5%.'\n\n"
    "DOCUMENT EXAMINATION: 'This is the big one. The Doc Examination Agent uses "
    "intelligent document processing to extract 50+ fields from the trade documents. "
    "It cross-references every field against the LC terms and UCP 600 automatically. "
    "Discrepancy severity is scored by the ML model — Sentinel decides what\'s "
    "auto-accepted versus what requires human review. 3 to 4 hours becomes minutes. "
    "The 60-70% discrepancy rate doesn\'t go away — but the cost of handling each "
    "discrepancy drops by 90%.'\n\n"
    "SANCTIONS: 'The Trade Sanctions Agent screens all parties, all vessels, all "
    "HS codes in parallel — not sequentially. Real-time, not batch. Sentinel "
    "freezes the Nexus state on any hit. EU sanctions, UN sanctions, dual-use "
    "goods — all checked simultaneously. Minutes instead of days.'\n\n"
    "SETTLEMENT: 'The Settlement Agent auto-matches nostro entries, triggers "
    "payment messaging, and releases payment only when Nexus confirms the state "
    "is Compliance Cleared. Same-day settlement. No manual SWIFT re-keying.'\n\n"
    "REPORTING: 'The Reporting Agent reads the complete transaction state chain "
    "from Nexus — every state transition from Facility Active through to Lifecycle "
    "Persisted — and assembles the regulatory filing and audit bundle automatically. "
    "100% traceable. Zero manual assembly.'\n\n"
    "CLOSE — POINT TO THE GREEN TIMELINE:\n"
    "'Look at the timeline. Current state: 14 to 45 days. Future state: 1 to 3 days. "
    "Stall rate from 40% to under 5%. Error rate from 12-20% to under 2%. "
    "Same trade finance operation. Different operating model.'"
)

# ── 9. Elastic Operations — Trade Finance (value recovered triangle) ──
h.scenes.append('''
    <section class="slide" style="background:#F5F7F9;">
      <div style="position:absolute; inset:0; display:flex; gap:4%; padding:4% 5%; align-items:center;">

        <!-- Left: Triangle -->
        <div style="flex:0 0 38%; display:flex; flex-direction:column; align-items:center;">
          <div style="text-align:center;"><span class="label label--dark" style="display:inline-block;">VALUE RECOVERY</span></div>
          <h2 class="slide-title" style="text-align:center; margin-bottom:4px;">Elastic Operations</h2>
          <p class="slide-subtitle" style="text-align:center; margin-bottom:16px;">Commercial Trade Finance</p>

          <div style="position:relative; width:100%; max-width:380px; height:280px;">
            <svg viewBox="0 0 380 280" style="position:absolute; top:0; left:0; width:100%; height:100%;" xmlns="http://www.w3.org/2000/svg">
              <polygon points="190,20 30,260 350,260" fill="#001C3D" />
              <line x1="190" y1="90" x2="190" y2="220" stroke="rgba(255,255,255,0.15)" stroke-width="1.5" stroke-dasharray="6,4" />
            </svg>
            <div style="position:absolute; top:-4px; left:50%; transform:translateX(-50%); text-align:center; z-index:2;"><div style="background:#16A34A; color:white; font-size:10px; font-weight:800; letter-spacing:2px; padding:6px 18px; border-radius:6px;">GROWTH</div></div>
            <div style="position:absolute; top:45%; left:50%; transform:translate(-50%,-50%); text-align:center; color:white; z-index:2;"><div style="font-size:9px; font-weight:800; letter-spacing:2px; opacity:0.5;">AI-NATIVE</div><div style="font-size:18px; font-weight:900;">Banking OS</div><div style="font-size:10px; opacity:0.7; margin-top:6px; line-height:1.5;">scale without linear<br>headcount growth</div></div>
            <div style="position:absolute; bottom:-4px; left:0; text-align:center; z-index:2;"><div style="background:#1A5AFF; color:white; font-size:10px; font-weight:800; letter-spacing:2px; padding:6px 14px; border-radius:6px;">EFFICIENCY</div></div>
            <div style="position:absolute; bottom:-4px; right:0; text-align:center; z-index:2;"><div style="background:#7C3AED; color:white; font-size:10px; font-weight:800; letter-spacing:2px; padding:6px 14px; border-radius:6px;">CONTROL</div></div>
          </div>

          <!-- Total -->
          <div style="background:white; border:2px solid #16A34A30; border-radius:12px; padding:14px 24px; text-align:center; margin-top:16px; width:100%; max-width:340px;">
            <div style="font-size:10px; font-weight:800; letter-spacing:2px; color:#5C6E84;">TOTAL VALUE RECOVERED</div>
            <div style="font-size:32px; font-weight:900; color:#16A34A; margin-top:4px;">&euro;7.9&ndash;18.9M</div>
            <div style="font-size:12px; color:#5C6E84; margin-top:4px;">Recovery: <strong style="color:#16A34A;">72%</strong> &bull; 14&ndash;45 days &rarr; <strong style="color:#16A34A;">1&ndash;3 days</strong></div>
          </div>
        </div>

        <!-- Right: Three value dimensions -->
        <div style="flex:1; display:flex; flex-direction:column; gap:14px; justify-content:center;">
          <!-- Growth -->
          <div>
            <div style="font-size:14px; font-weight:800; color:#001C3D; margin-bottom:8px;">&nearr; Growth Restored</div>
            <div style="display:flex; gap:10px;">
              <div style="flex:1; background:#FFF5F5; border:1.5px solid #FCA5A5; border-radius:10px; padding:14px;"><div style="font-size:9px; font-weight:800; letter-spacing:1.5px; color:#DC2626;">CURRENT VALUE BLEED</div><div style="font-size:22px; font-weight:900; color:#DC2626; margin-top:4px;">&euro;4&ndash;10M/yr</div><div style="font-size:10px; color:#5C6E84; margin-top:6px;">40% deal stall rate &bull; 10-day LC issuance &bull; competitors win on speed &bull; fee income leakage</div></div>
              <div style="flex:1; background:#F0FDF4; border:1.5px solid #86EFAC; border-radius:10px; padding:14px;"><div style="font-size:9px; font-weight:800; letter-spacing:1.5px; color:#16A34A;">BACKBASE BANKING OS</div><div style="font-size:22px; font-weight:900; color:#16A34A; margin-top:4px;">&euro;2.9&ndash;7.3M/yr</div><div style="font-size:10px; color:#5C6E84; margin-top:6px;">&bull; Same-day LC issuance &bull; 40% stall &rarr; &lt;5% &bull; Fee leakage sealed &bull; Win on speed: 1&ndash;3 days vs competitors&rsquo; 14&ndash;45</div></div>
            </div>
          </div>
          <!-- Efficiency -->
          <div>
            <div style="font-size:14px; font-weight:800; color:#001C3D; margin-bottom:8px;">&cir; Efficiency Gained</div>
            <div style="display:flex; gap:10px;">
              <div style="flex:1; background:#FFF5F5; border:1.5px solid #FCA5A5; border-radius:10px; padding:14px;"><div style="font-size:9px; font-weight:800; letter-spacing:1.5px; color:#DC2626;">CURRENT VALUE BLEED</div><div style="font-size:22px; font-weight:900; color:#DC2626; margin-top:4px;">&euro;4.5&ndash;10M/yr</div><div style="font-size:10px; color:#5C6E84; margin-top:6px;">6&ndash;12 FTEs per deal &bull; manual SWIFT messaging &bull; 3&ndash;4 hrs doc examination &bull; sequential screening</div></div>
              <div style="flex:1; background:#F0FDF4; border:1.5px solid #86EFAC; border-radius:10px; padding:14px;"><div style="font-size:9px; font-weight:800; letter-spacing:1.5px; color:#16A34A;">VALUE RECOVERED</div><div style="font-size:22px; font-weight:900; color:#16A34A; margin-top:4px;">&euro;3.2&ndash;7.3M/yr</div><div style="font-size:10px; color:#5C6E84; margin-top:6px;">&bull; Doc exam 3&ndash;4 hrs &rarr; minutes &bull; SWIFT auto-generated &bull; 6&ndash;12 FTEs &rarr; 2&ndash;3 &bull; Parallel agents</div></div>
            </div>
          </div>
          <!-- Control -->
          <div>
            <div style="font-size:14px; font-weight:800; color:#001C3D; margin-bottom:8px;">&oplus; Control Enforced</div>
            <div style="display:flex; gap:10px;">
              <div style="flex:1; background:#FFF5F5; border:1.5px solid #FCA5A5; border-radius:10px; padding:14px;"><div style="font-size:9px; font-weight:800; letter-spacing:1.5px; color:#DC2626;">CURRENT VALUE BLEED</div><div style="font-size:22px; font-weight:900; color:#DC2626; margin-top:4px;">&euro;2.5&ndash;6M/yr</div><div style="font-size:10px; color:#5C6E84; margin-top:6px;">EU sanctions penalty exposure &bull; UCP 600 breach risk &bull; 5% CTR errors &bull; 12% limit-load errors</div></div>
              <div style="flex:1; background:#F0FDF4; border:1.5px solid #86EFAC; border-radius:10px; padding:14px;"><div style="font-size:9px; font-weight:800; letter-spacing:1.5px; color:#16A34A;">VALUE RECOVERED</div><div style="font-size:22px; font-weight:900; color:#16A34A; margin-top:4px;">&euro;1.8&ndash;4.3M/yr</div><div style="font-size:10px; color:#5C6E84; margin-top:6px;">&bull; SENTINEL screens before LC issuance &bull; UCP 600 validated by agent &bull; CTR errors &lt;0.5% &bull; Automated reporting</div></div>
            </div>
          </div>
        </div>
      </div>
    </section>''')
NOTES[8] = (
    "SLIDE 9: ELASTIC OPERATIONS — TRADE FINANCE VALUE RECOVERED — 2 minutes.\n\n"
    "TRANSITION: 'Now let me quantify what this recovers.'\n\n"
    "WALK THE THREE DIMENSIONS — connect each to specific pain points from the "
    "value bleed slide:\n\n"
    "GROWTH (point to green cards):\n"
    "'€4 to 10 million in value bleed, €2.9 to 7.3 million recoverable. "
    "The 40% deal stall rate was killing fee income. Same-day LC issuance means "
    "you stop losing deals to competitors who can issue faster. Competitors like "
    "SEB, who are investing heavily in their Swedish trade finance operations, "
    "or international banks who can offer faster digital LC platforms. When your "
    "cycle time goes from 14-45 days to 1-3, you win on speed — and speed is "
    "becoming the primary differentiator in trade finance, not relationship.'\n\n"
    "EFFICIENCY (point to blue cards):\n"
    "'€4.5 to 10 million in bleed, €3.2 to 7.3 million recoverable. The document "
    "examination alone consumed 3-4 hours per LC at 6-12 FTEs per deal. With "
    "intelligent document processing and parallel agent execution, that drops to "
    "minutes. SWIFT messages auto-generated — no manual MT700 construction. "
    "The 6-12 FTEs per deal reduces to 2-3, focused on exceptions and advisory "
    "rather than data entry. This is directly aligned with your €600M cost "
    "takeout target and the 1,500 role restructuring.'\n\n"
    "CONTROL (point to purple cards):\n"
    "'€2.5 to 6 million in bleed, €1.8 to 4.3 million recoverable. And this is "
    "the one that should concern a Head of TxB Strategy most. EU sanctions penalty "
    "exposure — in the current geopolitical environment with Russia-related trade "
    "restrictions, dual-use goods screening, and vessel tracking — is not theoretical. "
    "Nordea has already navigated sanctions-related scrutiny in the past. Having "
    "Sentinel screen every party before LC issuance — not after — and auto-file "
    "regulatory reports with under 0.5% error rate is not just efficiency. It\'s "
    "existential risk reduction.'\n\n"
    "CLOSE: 'Total: €7.9 to 18.9 million recovered. 72% recovery rate. And the "
    "cycle time compression — 14-45 days to 1-3 — is what changes the competitive "
    "position, not just the cost structure.'"
)

# ── ZOOM-OUT SEQUENCE: 3 slides from agents → layers → Banking OS ──

# ── Slide A: Trade Finance Agents + Nexus/Sentinel foundation ──
h.scenes.append('''
    <section class="slide" style="background:#F5F7F9;">
      <div style="position:absolute; inset:0; padding:4% 5%; display:flex; flex-direction:column; justify-content:flex-start;">
        <span class="label label--dark">THE AGENTS</span>
        <h2 class="slide-title">Six agents. Two foundations.</h2>
        <p class="slide-subtitle">Every agent reads from Nexus and is governed by Sentinel. That&rsquo;s the trust-to-intent connection at every step.</p>

        <!-- 6 agent cards in a row -->
        <div style="display:grid; grid-template-columns:repeat(6, 1fr); gap:10px; margin-bottom:20px;">
          <div style="background:white; border:1.5px solid #E2E8F0; border-radius:10px; padding:14px;">
            <div style="font-size:12px; font-weight:800; color:#001C3D; margin-bottom:6px;">Facility Setup</div>
            <div style="font-size:9px; color:#5C6E84; line-height:1.5;">Auto-loads sublimits from <strong style="color:#16A34A;">NEXUS</strong>. <strong style="color:#D97706;">SENTINEL</strong> enforces limit authority.</div>
          </div>
          <div style="background:white; border:1.5px solid #E2E8F0; border-radius:10px; padding:14px;">
            <div style="font-size:12px; font-weight:800; color:#001C3D; margin-bottom:6px;">LC Drafting</div>
            <div style="font-size:9px; color:#5C6E84; line-height:1.5;">Auto-generates LC from <strong style="color:#16A34A;">NEXUS</strong> facility terms. <strong style="color:#D97706;">SENTINEL</strong> validates UCP 600.</div>
          </div>
          <div style="background:white; border:1.5px solid #E2E8F0; border-radius:10px; padding:14px;">
            <div style="font-size:12px; font-weight:800; color:#001C3D; margin-bottom:6px;">Doc Examination</div>
            <div style="font-size:9px; color:#5C6E84; line-height:1.5;">Extracts 50+ fields. Validates against UCP 600. <strong style="color:#D97706;">SENTINEL</strong> governs waiver authority.</div>
          </div>
          <div style="background:white; border:1.5px solid #E2E8F0; border-radius:10px; padding:14px;">
            <div style="font-size:12px; font-weight:800; color:#001C3D; margin-bottom:6px;">Trade Sanctions</div>
            <div style="font-size:9px; color:#5C6E84; line-height:1.5;">All parties screened in parallel. <strong style="color:#D97706;">SENTINEL</strong> freezes <strong style="color:#16A34A;">NEXUS</strong> state on any hit.</div>
          </div>
          <div style="background:white; border:1.5px solid #E2E8F0; border-radius:10px; padding:14px;">
            <div style="font-size:12px; font-weight:800; color:#001C3D; margin-bottom:6px;">Settlement</div>
            <div style="font-size:9px; color:#5C6E84; line-height:1.5;">Auto-matches nostro. Payment released only when <strong style="color:#16A34A;">NEXUS</strong> confirms: Compliance Cleared.</div>
          </div>
          <div style="background:white; border:1.5px solid #E2E8F0; border-radius:10px; padding:14px;">
            <div style="font-size:12px; font-weight:800; color:#001C3D; margin-bottom:6px;">Reporting</div>
            <div style="font-size:9px; color:#5C6E84; line-height:1.5;">Full audit bundle from <strong style="color:#16A34A;">NEXUS</strong> state chain. <strong style="color:#D97706;">SENTINEL</strong> validates completeness.</div>
          </div>
        </div>

        <!-- Two foundation bars: Nexus and Sentinel -->
        <div style="display:flex; gap:12px;">
          <div style="flex:1; background:#F0FDF4; border:1.5px solid #86EFAC; border-left:4px solid #16A34A; border-radius:10px; padding:16px 20px;">
            <div style="display:flex; justify-content:space-between; align-items:center;">
              <div>
                <div style="font-size:14px; font-weight:900; color:#16A34A;">Nexus &mdash; The Interpretive Layer</div>
                <div style="font-size:11px; color:#5C6E84; margin-top:4px;">Customer State Graph &bull; Banking Ontology &bull; Actions + Context Graph</div>
              </div>
              <div style="font-size:11px; font-weight:700; color:#16A34A; text-align:right; max-width:300px;">Trust at scale requires interpretation.<br>Nexus provides that interpretive layer.</div>
            </div>
          </div>
          <div style="flex:1; background:#FFFBEB; border:1.5px solid #FCD34D; border-left:4px solid #D97706; border-radius:10px; padding:16px 20px;">
            <div style="display:flex; justify-content:space-between; align-items:center;">
              <div>
                <div style="font-size:14px; font-weight:900; color:#D97706;">Sentinel &mdash; The Governance Layer</div>
                <div style="font-size:11px; color:#5C6E84; margin-top:4px;">Decision Authority &bull; Policy Evaluation &bull; Autonomy Governance</div>
              </div>
              <div style="font-size:11px; font-weight:700; color:#D97706; text-align:right; max-width:300px;">Identity, governance, accountability.<br>Control earns trust.</div>
            </div>
          </div>
        </div>

        <p style="font-size:11px; color:#5C6E84; text-align:center; margin-top:14px;"><strong>Every agent reads from Nexus</strong> (to know what to do) <strong>and is governed by Sentinel</strong> (to ensure it&rsquo;s safe). That&rsquo;s the trust-to-intent connection &mdash; at every step.</p>
      </div>
    </section>''')
NOTES[10] = (
    "SLIDE 11: SIX AGENTS, TWO FOUNDATIONS — 2 minutes. The key conceptual slide.\n\n"
    "TRANSITION: 'Now let me show you what makes this work architecturally. "
    "It\'s not the agents themselves — it\'s what they operate on.'\n\n"
    "POINT TO THE SIX AGENT CARDS:\n"
    "'You\'ve seen what these six agents do in the trade finance lifecycle. "
    "But notice something: every single one of them — whether it\'s drafting an LC, "
    "screening sanctions, examining documents, or settling a payment — does exactly "
    "two things.\n\n"
    "It reads from Nexus — you\'ll see it highlighted in green in every card. "
    "Nexus is our semantic layer. It holds the customer state graph — the real-time "
    "position of every customer relationship, every facility, every compliance "
    "status, across all four of your Nordic markets. It\'s not a data warehouse. "
    "It\'s an interpretive model. It understands that this customer\'s facility is "
    "active, their collateral is assessed, their compliance status is cleared, "
    "their behavioural pattern is normal. That interpretation is what allows "
    "agents to form intent — to know what to do next.'\n\n"
    "POINT TO NEXUS BAR:\n"
    "'Trust at scale requires interpretation. Nexus is that interpretive layer.'\n\n"
    "POINT TO SENTINEL BAR:\n"
    "'And it\'s governed by Sentinel — you\'ll see it highlighted in amber in "
    "every card. Sentinel is our authority layer. It enforces identity, policy, "
    "and compliance on every action — whether that action is taken by a human RM "
    "in Stockholm or by an AI agent processing an LC amendment at 3am. Same rules. "
    "Same governance. Same audit trail.\n\n"
    "In trade finance specifically: Sentinel validates that the LC value is within "
    "the facility sublimit before granting agent autonomy. It checks that UCP 600 "
    "clause violations are auto-blocked. It enforces EU sanctions policy per "
    "jurisdiction. It creates an immutable audit token for every limit change, "
    "every screening decision, every payment release.\n\n"
    "Control earns trust. Data enables intent. The agents work across both.'\n\n"
    "TRANSITION: 'Let me show you where these sit in the platform.'"
)

# ── Slide B: Agents encapsulated into 5 Banking OS Layers ──
h.scenes.append('''
    <section class="slide" style="background:#F5F7F9;">
      <div style="position:absolute; inset:0; padding:4% 5%;">
        <span class="label label--dark">THE CONTROL PLANE</span>
        <h2 class="slide-title">Where each agent lives in the Banking OS</h2>
        <p class="slide-subtitle">Five layers. Each serves a specific function. The agents you just saw operate across them.</p>

        <div style="display:flex; flex-direction:column; gap:10px;">

          <!-- Interaction Layer -->
          <div style="background:#EBF0FF; border-left:4px solid #1A5AFF; border-radius:10px; padding:14px 20px; display:flex; align-items:center; gap:20px;">
            <div style="min-width:160px;"><div style="font-size:15px; font-weight:900; color:#1A5AFF;">Interaction</div><div style="font-size:10px; color:#5C6E84;">Interface to Customers + Employees</div></div>
            <div style="display:flex; gap:8px; flex-wrap:wrap;">
              <span style="background:white; border:1.5px solid #1A5AFF30; border-radius:6px; padding:6px 14px; font-size:11px; font-weight:700; color:#001C3D;">RM Workspace</span>
              <span style="background:white; border:1.5px solid #1A5AFF30; border-radius:6px; padding:6px 14px; font-size:11px; font-weight:700; color:#001C3D;">Client Portal</span>
              <span style="background:white; border:1.5px solid #1A5AFF30; border-radius:6px; padding:6px 14px; font-size:11px; font-weight:700; color:#001C3D;">Case Manager</span>
              <span style="background:white; border:1.5px solid #1A5AFF30; border-radius:6px; padding:6px 14px; font-size:11px; font-weight:700; color:#001C3D;">Conversational AI</span>
            </div>
          </div>

          <!-- Orchestration Layer -->
          <div style="background:#F5F3FF; border-left:4px solid #7C3AED; border-radius:10px; padding:14px 20px; display:flex; align-items:center; gap:20px;">
            <div style="min-width:160px;"><div style="font-size:15px; font-weight:900; color:#7C3AED;">Orchestration</div><div style="font-size:10px; color:#5C6E84;">Executing the Work</div></div>
            <div style="display:flex; gap:8px; flex-wrap:wrap;">
              <span style="background:white; border:1.5px solid #7C3AED40; border-radius:6px; padding:6px 14px; font-size:10px; font-weight:700; color:#7C3AED;">Facility Setup Agent</span>
              <span style="background:white; border:1.5px solid #7C3AED40; border-radius:6px; padding:6px 14px; font-size:10px; font-weight:700; color:#7C3AED;">LC Drafting Agent</span>
              <span style="background:white; border:1.5px solid #7C3AED40; border-radius:6px; padding:6px 14px; font-size:10px; font-weight:700; color:#7C3AED;">Doc Exam Agent</span>
              <span style="background:white; border:1.5px solid #7C3AED40; border-radius:6px; padding:6px 14px; font-size:10px; font-weight:700; color:#7C3AED;">Sanctions Agent</span>
              <span style="background:white; border:1.5px solid #7C3AED40; border-radius:6px; padding:6px 14px; font-size:10px; font-weight:700; color:#7C3AED;">Settlement Agent</span>
              <span style="background:white; border:1.5px solid #7C3AED40; border-radius:6px; padding:6px 14px; font-size:10px; font-weight:700; color:#7C3AED;">Reporting Agent</span>
            </div>
          </div>

          <!-- Authority / Sentinel -->
          <div style="background:#001C3D; border-left:4px solid #F59E0B; border-radius:10px; padding:14px 20px; display:flex; align-items:center; gap:20px;">
            <div style="min-width:160px;"><div style="font-size:15px; font-weight:900; color:#F59E0B;">Authority</div><div style="font-size:10px; color:#94A3B8;">Sentinel &mdash; Decision Authority</div><div style="font-size:9px; font-weight:700; color:#F59E0B; margin-top:4px;">Where trust lives</div></div>
            <div style="display:flex; gap:8px; flex-wrap:wrap;">
              <span style="background:rgba(255,255,255,0.1); border:1.5px solid rgba(245,158,11,0.3); border-radius:6px; padding:6px 14px; font-size:11px; font-weight:600; color:#E2E8F0;">Decision Authority + Policy Evaluation</span>
              <span style="background:rgba(255,255,255,0.1); border:1.5px solid rgba(245,158,11,0.3); border-radius:6px; padding:6px 14px; font-size:11px; font-weight:600; color:#E2E8F0;">Decision Kernel + Autonomy Governance</span>
            </div>
          </div>

          <!-- Semantic / Nexus -->
          <div style="background:#001C3D; border-left:4px solid #16A34A; border-radius:10px; padding:14px 20px; display:flex; align-items:center; gap:20px;">
            <div style="min-width:160px;"><div style="font-size:15px; font-weight:900; color:#16A34A;">Semantic</div><div style="font-size:10px; color:#94A3B8;">Nexus &mdash; Shared Customer Truth</div><div style="font-size:9px; font-weight:700; color:#16A34A; margin-top:4px;">Where intent forms</div></div>
            <div style="display:flex; gap:8px; flex-wrap:wrap;">
              <span style="background:rgba(255,255,255,0.1); border:1.5px solid rgba(22,163,74,0.3); border-radius:6px; padding:6px 14px; font-size:11px; font-weight:600; color:#E2E8F0;">Ontology + Customer State Graph</span>
              <span style="background:rgba(255,255,255,0.1); border:1.5px solid rgba(22,163,74,0.3); border-radius:6px; padding:6px 14px; font-size:11px; font-weight:600; color:#E2E8F0;">Actions + Context Graph</span>
            </div>
          </div>

          <!-- Connectivity -->
          <div style="background:#F5F7F9; border-left:4px solid #5C6E84; border-radius:10px; padding:14px 20px; display:flex; align-items:center; gap:20px; border:1px solid #E2E8F0;">
            <div style="min-width:160px;"><div style="font-size:15px; font-weight:900; color:#5C6E84;">Connectivity</div><div style="font-size:10px; color:#94A3B8;">Grand Central</div></div>
            <div style="display:flex; gap:8px; flex-wrap:wrap;">
              <span style="background:white; border:1.5px solid #D1D5DB; border-radius:6px; padding:6px 14px; font-size:11px; font-weight:600; color:#5C6E84;">SWIFT Network</span>
              <span style="background:white; border:1.5px solid #D1D5DB; border-radius:6px; padding:6px 14px; font-size:11px; font-weight:600; color:#5C6E84;">Core Banking</span>
              <span style="background:white; border:1.5px solid #D1D5DB; border-radius:6px; padding:6px 14px; font-size:11px; font-weight:600; color:#5C6E84;">Compliance DBs</span>
              <span style="background:white; border:1.5px solid #D1D5DB; border-radius:6px; padding:6px 14px; font-size:11px; font-weight:600; color:#5C6E84;">Doc Management</span>
              <span style="background:white; border:1.5px solid #D1D5DB; border-radius:6px; padding:6px 14px; font-size:11px; font-weight:600; color:#5C6E84;">Reg Reporting</span>
            </div>
          </div>

        </div>

        <p style="font-size:11px; color:#5C6E84; margin-top:12px; text-align:center;">The six trade finance agents operate in the <strong>Orchestration Layer</strong>. SENTINEL governs every decision. NEXUS holds the shared state. Grand Central connects to your existing systems.</p>
      </div>
    </section>''')
NOTES[11] = (
    "SLIDE 12: BANKING OS LAYERS — 90 seconds. Show where agents live.\n\n"
    "TRANSITION: 'Five layers. Each serves a specific function.'\n\n"
    "WALK TOP TO BOTTOM — briskly:\n\n"
    "INTERACTION (point to blue row):\n"
    "'At the top — the interaction layer. This is where your RMs, your trade "
    "finance ops teams, your corporate clients, and your AI agents all interact "
    "through the same platform. RM Workspace, Client Portal, Case Manager, "
    "Conversational AI. Built once, deployed across all four Nordic markets. "
    "No more country-specific front-ends.'\n\n"
    "ORCHESTRATION (point to purple row):\n"
    "'The orchestration layer — this is where the six agents you just saw live. "
    "Facility Setup, LC Drafting, Doc Examination, Sanctions, Settlement, "
    "Reporting. Deterministic workflows and agentic workflows side by side. "
    "Not all work should be agentic — some processes need predictable, rules-based "
    "execution. Both run here.'\n\n"
    "AUTHORITY — SENTINEL (point to dark row — \'where trust lives\'):\n"
    "'Sentinel. This is where trust lives in the architecture. Decision authority "
    "and policy evaluation on every action. The decision kernel governs how much "
    "autonomy each agent has — a Facility Setup Agent might have full autonomy "
    "for standard sublimits but require human co-approval above a threshold. "
    "That\'s configurable per bank, per jurisdiction, per product.'\n\n"
    "SEMANTIC — NEXUS (point to green-bordered row — \'where intent forms\'):\n"
    "'Nexus. This is where intent forms. The ontology — the banking concepts that "
    "ground every AI decision in domain knowledge, not just pattern matching. "
    "The customer state graph — the shared truth about every customer, every "
    "facility, every compliance status. When Nexus state says Compliance Cleared, "
    "the Settlement Agent knows it can act. That\'s intent from verified trust.'\n\n"
    "CONNECTIVITY (point to gray row):\n"
    "'And Grand Central connects to your existing systems. SWIFT network, core "
    "banking, compliance databases, document management, regulatory reporting. "
    "We don\'t replace any of them. We orchestrate across them.'\n\n"
    "TRANSITION: 'Let me zoom out one more level to show you the full picture — "
    "and then hand over to our Solutions Engineer who can show you what this looks like live.'"
)

# ── Slide C: Full Banking OS Macro View ──
h.scenes.append('''
    <section class="slide" style="background:#F5F7F9;">
      <div style="position:absolute; inset:0; padding:4% 5%;">
        <span class="label label--dark">THE SYSTEM</span>
        <h2 class="slide-title">The Banking OS</h2>
        <p class="slide-subtitle">The system that understands, runs + governs the Unified Frontline.</p>

        <div style="display:flex; flex-direction:column; align-items:center; gap:10px; max-width:1100px; margin:0 auto;">

          <!-- Three Actors -->
          <div style="display:flex; gap:16px; width:100%; justify-content:center;">
            <div style="flex:1; background:#F0F4FF; border-radius:10px; padding:16px; text-align:center;">
              <div style="font-size:16px; font-weight:900; color:#001C3D;">Customers</div>
              <div style="font-size:11px; color:#5C6E84;">Mobile &bull; Web &bull; Conversational</div>
            </div>
            <div style="flex:1; background:#F0F4FF; border-radius:10px; padding:16px; text-align:center;">
              <div style="font-size:16px; font-weight:900; color:#001C3D;">Employees</div>
              <div style="font-size:11px; color:#5C6E84;">CSR &bull; RM &bull; Branch &bull; Operations</div>
            </div>
            <div style="flex:1; background:#F0F4FF; border-radius:10px; padding:16px; text-align:center;">
              <div style="font-size:16px; font-weight:900; color:#001C3D;">AI Agents</div>
              <div style="font-size:11px; color:#5C6E84;">Servicing &bull; Sales &bull; Operations</div>
            </div>
          </div>

          <!-- Arrow down -->
          <div style="font-size:20px; color:#5C6E84;">&darr;</div>

          <!-- Unified Frontline bar -->
          <div style="width:100%; background:#E8EDFF; border-radius:10px; padding:18px; text-align:center;">
            <div style="font-size:18px; font-weight:900; color:#001C3D;">Unified Frontline</div>
            <div style="font-size:12px; color:#5C6E84;">a single operating environment &mdash; daily banking &bull; assisted servicing &bull; sales execution &bull; operations</div>
          </div>

          <!-- Arrow down -->
          <div style="font-size:20px; color:#5C6E84;">&darr;</div>

          <!-- Banking OS block -->
          <div style="width:100%; background:#001C3D; border-radius:12px; padding:20px 28px; text-align:center;">
            <div style="font-size:20px; font-weight:900; color:white;">AI-native Banking OS</div>
            <div style="font-size:12px; color:#94A3B8; margin:6px 0 14px;">orchestrates humans, agents and systems across the entire frontline</div>
            <div style="display:flex; gap:12px; justify-content:center;">
              <div style="background:rgba(255,255,255,0.12); border-radius:8px; padding:10px 24px;">
                <div style="font-size:13px; font-weight:800; color:#F59E0B;">Understand</div>
                <div style="font-size:10px; color:#94A3B8;">the Frontline</div>
                <div style="font-size:8px; color:#F59E0B; margin-top:4px; font-weight:700;">Nexus interprets</div>
              </div>
              <div style="background:rgba(255,255,255,0.12); border-radius:8px; padding:10px 24px;">
                <div style="font-size:13px; font-weight:800; color:#1A5AFF;">Run</div>
                <div style="font-size:10px; color:#94A3B8;">the Frontline</div>
                <div style="font-size:8px; color:#1A5AFF; margin-top:4px; font-weight:700;">Agents execute intent</div>
              </div>
              <div style="background:rgba(255,255,255,0.12); border-radius:8px; padding:10px 24px;">
                <div style="font-size:13px; font-weight:800; color:#16A34A;">Govern</div>
                <div style="font-size:10px; color:#94A3B8;">the Frontline</div>
                <div style="font-size:8px; color:#16A34A; margin-top:4px; font-weight:700;">Sentinel enforces trust</div>
              </div>
            </div>
          </div>

          <!-- Arrow down -->
          <div style="display:flex; align-items:center; gap:8px; color:#5C6E84;">
            <div style="font-size:12px; font-weight:700;">orchestration across systems</div>
            <div style="font-size:20px;">&darr;</div>
          </div>

          <!-- Fragmented systems -->
          <div style="display:flex; gap:8px; flex-wrap:wrap; justify-content:center;">
            <span style="background:white; border:1.5px solid #D1D5DB; border-radius:8px; padding:8px 16px; font-size:12px; font-weight:600; color:#5C6E84;">Core Banking</span>
            <span style="background:white; border:1.5px solid #D1D5DB; border-radius:8px; padding:8px 16px; font-size:12px; font-weight:600; color:#5C6E84;">CRM</span>
            <span style="background:white; border:1.5px solid #D1D5DB; border-radius:8px; padding:8px 16px; font-size:12px; font-weight:600; color:#5C6E84;">Cards</span>
            <span style="background:white; border:1.5px solid #D1D5DB; border-radius:8px; padding:8px 16px; font-size:12px; font-weight:600; color:#5C6E84;">Payments</span>
            <span style="background:white; border:1.5px solid #D1D5DB; border-radius:8px; padding:8px 16px; font-size:12px; font-weight:600; color:#5C6E84;">KYC</span>
            <span style="background:white; border:1.5px solid #D1D5DB; border-radius:8px; padding:8px 16px; font-size:12px; font-weight:600; color:#5C6E84;">Fraud</span>
            <span style="background:white; border:1.5px solid #D1D5DB; border-radius:8px; padding:8px 16px; font-size:12px; font-weight:600; color:#5C6E84;">Documents</span>
            <span style="background:white; border:1.5px solid #D1D5DB; border-radius:8px; padding:8px 16px; font-size:12px; font-weight:600; color:#5C6E84;">Case Mgmt</span>
          </div>
          <div style="font-size:11px; color:#94A3B8; text-align:center;">fragmented systems of record, business applications + third party services</div>
        </div>
      </div>
    </section>''')
NOTES[12] = (
    "This is the full Banking OS view. 60 seconds max \u2014 then hand to the live demo.\n\n"
    "PITCH: 'And this is the full picture. Three actors \u2014 customers, employees, "
    "and AI agents \u2014 all operating through one unified frontline.\n\n"
    "Underneath, the Banking OS does three things. It understands the frontline \u2014 "
    "that's Nexus, the shared semantic model. It runs the frontline \u2014 that's "
    "orchestration, the agents and workflows. And it governs the frontline \u2014 "
    "that's Sentinel, enforcing identity, policy, risk, and compliance.\n\n"
    "Below everything \u2014 your existing systems. Core banking, CRM, payments, "
    "KYC, fraud, documents. We don't replace them. We orchestrate across them.\n\n"
    "This is what you just saw applied to trade finance. But it works the same way "
    "for payments operations, cash management, entity onboarding \u2014 any domain "
    "where the work breaks in the handoffs between systems.\n\n"
    "Our Solutions Engineer can show you what this looks like live.'"
)

# ── 10. Danske Bank — in production ──
h.add_case_study(
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
NOTES[13] = (
    "Quick reference hit — don't dwell. 60 seconds max.\n\n"
    "PITCH: 'Danske Bank is your closest Nordic peer on this journey. "
    "Enterprise-wide platform — personal banking, business banking, "
    "large corporates. They consolidated 500 onboarding flows into one "
    "digital journey. 12 design systems into one. Go-live in under 6 months — "
    "2-year acceleration on their original timeline.\n\n"
    "Most relevant for you: they're already applying GenAI to reconciliations "
    "and post-trade processing. 74% of their employees are using DanskeGPT. "
    "This is not a pilot — it's in production.'"
)

# ── 12. The provocative close ──
h.add_statement(
    "You have built trust infrastructure. #1 cash management in the Nordics. Top-ranked trade finance. Among the most mature API platforms in Europe. The question is whether you connect that trust to real-time decisioning \u2014 at scale. That is the shift from products to platform.",
    highlight_words=[
        "trust infrastructure",
        "connect that trust to real-time decisioning",
        "products to platform"
    ]
)
NOTES[14] = (
    "Let this land. Don't rush.\n\n"
    "PITCH: Read the slide slowly. Then pause.\n\n"
    "'You've built trust infrastructure. You are the most trusted bank in the Nordics. "
    "Your cash management is number one. Your trade finance is top-ranked. Your API "
    "platform is among the most mature in Europe.\n\n"
    "The question is whether you connect that trust to real-time decisioning — at scale. "
    "That is the shift from products to platform.'\n\n"
    "PAUSE. Let it land. Then transition to next steps."
)

# ── 13. Next steps ──
h.add_tiles(
    "Where do we go from here?",
    "Three concrete next steps \u2014 scoped to your priorities.",
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
NOTES[15] = (
    "PITCH: 'Three options — all low-commitment, high-insight.\n\n"
    "First: help us understand which TxB domain is the immediate priority. "
    "We'll scope everything else around that.\n\n"
    "Second: a live demonstration — not generic. Your use cases, your scenarios, "
    "your operations. We'll show you what agentic payments operations or "
    "cash management intelligence actually looks like.\n\n"
    "Third: a quantified value case. Modelled against your actual cost-to-income, "
    "FTE, and volume metrics. Conservative, defensible, decision-ready.\n\n"
    "What feels like the right next step for you?'"
)

# ── 14. Handoff to live demo ──
h.add_section_divider(
    "Product Showcase",
    "What this looks like |in practice",
    "Principal Solutions Engineer"
)
NOTES[16] = (
    "Handoff to live demo.\n\n"
    "PITCH: 'Let me hand over to our Solutions Engineer, who can show you what some of this "
    "looks like in practice \u2014 particularly the operations workspace and "
    "how agentic workflows work in a real banking context.'"
)

# ── No reorder needed — slides stay in build order ──

# ── Save HTML ──
out_path = "/Users/shyam/cortex/Engagement/Nordea/Output/nordea_txb_frontline_v2.html"
out = h.save(out_path)
print(f"HTML saved: {out}")
print(f"Scenes: {len(h.scenes)}")

# ── Post-process: inject source citations into specific slides ──
with open(out_path, 'r') as f:
    html = f.read()

# Fix slide 3 stat cards — reduce padding to prevent scrollbar
import re
sections_list = list(re.finditer(r'<section', html))
if len(sections_list) > 2:
    # Find the 3rd section (index 2) and inject a scoped style override
    slide3_pos = sections_list[2].start()
    # Insert a style tag right after the <section> opening tag's >
    next_close = html.index('>', slide3_pos) + 1
    override_css = '<style>.slide:nth-child(3) .stat-card { padding: 20px 16px; } .slide:nth-child(3) .stat-grid { gap: 14px; margin-top: 16px; } .slide:nth-child(3) .stat-number { font-size: clamp(32px, 3.5vw, 48px); margin-bottom: 6px; } .slide:nth-child(3) .stat-label { font-size: 13px; }</style>'
    html = html[:next_close] + override_css + html[next_close:]

# Source citation style
src_style = 'position:absolute;bottom:14px;left:5%;font-size:10px;color:#94A3B8;font-family:\"Libre Franklin\",sans-serif;text-align:left;width:90%;'

# Find all <section> tags and inject sources before their closing </section>
import re
sections = list(re.finditer(r'</section>', html))

# Slide indices (0-based) and their sources
sources = {
    2: "Sources: Nordea 2026\u201330 strategy announcement (Nov 2025) \u00b7 Nordea restructuring press release (17 March 2026) \u00b7 Nordea Q4 2025 earnings",
    3: "Sources: Nordea 2026\u201330 strategy announcement (Nov 2025) \u00b7 Nordea restructuring press release (17 March 2026)",
    6: "Sources: Backbase APA Domain Analysis \u00b7 ICC Global Survey on Trade Finance (discrepancy rates 60\u201370%) \u00b7 Calibrated for Nordic commercial bank, 300\u2013500+ trade finance transactions/yr",
    7: "Sources: Backbase Banking OS platform benchmarks \u00b7 Client deployment data",
    8: "Sources: Backbase APA Domain Analysis \u00b7 Recovery rates based on client deployment outcomes \u00b7 Calibrated for Nordic commercial bank",
}

# Inject in reverse order so positions don't shift
for slide_idx in sorted(sources.keys(), reverse=True):
    if slide_idx < len(sections):
        pos = sections[slide_idx].start()
        src_html = f'\n      <div style="{src_style}">{sources[slide_idx]}</div>'
        html = html[:pos] + src_html + html[pos:]

# ── Post-process: inject speaker notes panel ──

# Build notes data as JS object
notes_js_entries = []
for idx, note in sorted(NOTES.items()):
    escaped_note = note.replace('\\', '\\\\').replace("'", "\\'").replace('\n', '\\n')
    notes_js_entries.append(f"    {idx}: '{escaped_note}'")
notes_js = "{\n" + ",\n".join(notes_js_entries) + "\n  }"

# Inject notes CSS and JS before </body>
notes_injection = f'''
<style>
  .notes-panel {{
    display: none;
    position: fixed;
    bottom: 0;
    left: 0;
    right: 0;
    max-height: 35vh;
    background: rgba(0, 28, 61, 0.95);
    color: #E2E8F0;
    font-family: 'Libre Franklin', sans-serif;
    font-size: 14px;
    line-height: 1.6;
    padding: 20px 40px;
    overflow-y: auto;
    z-index: 9999;
    border-top: 3px solid #1A5AFF;
    backdrop-filter: blur(10px);
  }}
  .notes-panel.visible {{ display: block; }}
  .notes-panel h4 {{
    font-size: 11px;
    font-weight: 800;
    letter-spacing: 2px;
    color: #1A5AFF;
    margin: 0 0 10px 0;
    text-transform: uppercase;
  }}
  .notes-panel pre {{
    white-space: pre-wrap;
    word-wrap: break-word;
    margin: 0;
    font-family: 'Libre Franklin', sans-serif;
    font-size: 13px;
  }}
  .notes-hint {{
    position: fixed;
    bottom: 8px;
    left: 50%;
    transform: translateX(-50%);
    font-size: 11px;
    color: #94A3B8;
    font-family: 'Libre Franklin', sans-serif;
    z-index: 9998;
    pointer-events: none;
  }}
</style>
<div class="notes-panel" id="notesPanel">
  <h4>Speaker Notes</h4>
  <pre id="notesContent"></pre>
</div>
<div class="notes-hint" id="notesHint">Press <b>N</b> for speaker notes</div>
<script>
(function() {{
  const notes = {notes_js};
  const panel = document.getElementById('notesPanel');
  const content = document.getElementById('notesContent');
  const hint = document.getElementById('notesHint');
  let notesVisible = false;
  let currentSlide = 0;

  function updateNotes(idx) {{
    currentSlide = idx;
    if (notes[idx]) {{
      content.textContent = notes[idx];
    }} else {{
      content.textContent = '(No notes for this slide)';
    }}
  }}

  // Hook into existing slide navigation
  const origGoTo = window.__goTo;

  // Override goTo by monkey-patching the keyboard handler
  const slides = document.querySelectorAll('.slide');
  const observer = new MutationObserver(function() {{
    slides.forEach(function(slide, idx) {{
      if (slide.classList.contains('active')) {{
        updateNotes(idx);
      }}
    }});
  }});
  slides.forEach(function(slide) {{
    observer.observe(slide, {{ attributes: true, attributeFilter: ['class'] }});
  }});

  // Toggle notes with N key
  document.addEventListener('keydown', function(e) {{
    if (e.key === 'n' || e.key === 'N') {{
      if (e.key === 'N' && e.shiftKey) return;
      notesVisible = !notesVisible;
      panel.classList.toggle('visible', notesVisible);
      hint.style.display = notesVisible ? 'none' : 'block';
      e.stopPropagation();
    }}
  }}, true);

  // Initialize with first slide notes
  updateNotes(0);
}})();
</script>
'''

html = html.replace('</body>', notes_injection + '\n</body>')

with open(out_path, 'w') as f:
    f.write(html)

final_size = os.path.getsize(out_path) / 1024
print(f"HTML with notes: {final_size:.1f} KB")

# ── Now build PPTX with native speaker notes ──
from tools.frontline_2026_presenter import Frontline2026Presenter

pptx_path = "/Users/shyam/cortex/Engagement/Nordea/Output/nordea_txb_frontline_v2.pptx"
p = Frontline2026Presenter(output_path=pptx_path)

# 1. Cover
p.add_cover_slide("Backbase x Nordea", "Transaction Banking\nA Strategic Conversation", "April 2, 2026")

# 2. Three-layer thesis
p.add_tiles_slide(
    "The architecture beneath payments is being restructured",
    subtitle="Not faster rails. Not better channels. A structural migration of where value sits.",
    section_label="Our Observation",
    columns=3,
    tiles=[
        {"stat": "01", "title": "Execution", "body": "The rail. Speed is baseline. Instant payments, A2A, ISO 20022 \u2014 rails becoming interchangeable. The rail executes. It no longer differentiates.", "accent": "red", "pill": "COMMODITY"},
        {"stat": "02", "title": "Trust", "body": "Identity, consent, risk interpretation. The connective tissue linking wallets, fraud management, and AI-enabled ecosystems. Architectural infrastructure.", "accent": "amber", "pill": "CONNECTIVE TISSUE"},
        {"stat": "03", "title": "Intent", "body": "AI-driven decisioning. Translating verified identity into executable action. AI monitors state, identifies the right moment, acts within governed boundaries.", "accent": "blue", "pill": "EMERGING FRONTIER"},
    ],
)

# 3. Nordea commitment
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

# 4. Productivity paradox
p.add_tiles_slide(
    "The productivity paradox",
    subtitle="Three targets that only coexist with a fundamentally different operating model.",
    section_label="The Challenge",
    columns=3,
    tiles=[
        {"stat": "-1,500", "title": "People", "body": "Workforce reduction in 2026-27. Headcount is the cost line \u2014 not the solution to scaling.", "accent": "red"},
        {"stat": "+50,000", "title": "SME Customers", "body": "Explicit growth target by 2030. Volume must grow while workforce shrinks. Linear scaling is over.", "accent": "green"},
        {"stat": "46\u219240%", "title": "Cost-to-Income", "body": "Three points in four years. Efficiency must improve while serving more customers across four markets.", "accent": "blue"},
    ],
)

# 5. Elastic Operations (triangle approximation for PPTX)
p.add_tiles_slide(
    "Elastic Operations",
    subtitle="AI-native operating model \u2192 scale operations + growth, without losing control.",
    section_label="Business Outcome",
    columns=3,
    tiles=[
        {"stat": "Growth", "title": "Acquire \u2022 Retain \u2022 Expand", "body": "Scale customer acquisition without proportional headcount. AI-powered next-best-action for RMs. Embedded finance distribution through APIs.", "accent": "green"},
        {"stat": "Efficiency", "title": "Higher throughput \u2022 Lower cost-to-serve", "body": "Agentic process automation across operations. 30\u201360% cost-to-serve reduction. Multi-day processes collapsed to hours.", "accent": "blue"},
        {"stat": "Control", "title": "Authority \u2022 Policy \u2022 Proof", "body": "Same governance for humans and AI agents. Compliance is architectural, not additive. Full audit trail on every action.", "accent": "purple"},
    ],
)

# 6. TxB Domain Map (PIVOT) — enhanced with value bleed
p.add_tiles_slide(
    "Your transaction banking remit",
    subtitle="Four domains, each with its own pressure points and measurable value at risk.",
    section_label="Where to Focus",
    columns=4,
    tiles=[
        {"title": "Payments & Cash Mgmt", "body": "ISO 20022 live. #1 cash mgmt in Nordics. Gap: exceptions, disputes, sanctions still manual across 4 countries. Value at risk: $8.9\u201320.5M/yr.", "accent": "red", "pill": "HIGH FRICTION"},
        {"title": "Trade Finance", "body": "Top-ranked by Prospera. Gap: document analysis, compliance, sanctions screening remain multi-day. Value at risk: $9.5\u201320M/yr.", "accent": "amber", "pill": "PROCESS GAP"},
        {"title": "Entity Onboarding", "body": "Complex entity & UBO verification. Gap: 8\u201312 docs, 15\u201325 min review each. No STP. Value at risk: $9.3\u201322M/yr.", "accent": "amber", "pill": "ONBOARDING GAP"},
        {"title": "Open Banking & APIs", "body": "Mature API Market. 14+ integrations. Gap: primarily compliance-driven, not strategic distribution.", "accent": "blue", "pill": "STRATEGIC GAP"},
    ],
)

# 7. Value Bleed — Commercial Trade Finance (Nordic-adapted)
p.add_tiles_slide(
    "Value bleed \u2014 Commercial Trade Finance",
    subtitle="Process health scan across the LC lifecycle. Each step compounds delay, stall, and compliance exposure.",
    section_label="Current State",
    columns=3,
    tiles=[
        {"title": "LC Issuance & Amendment", "body": "Manual SWIFT MT700 construction. UCP 600 checked manually. 45\u201390 min/LC. 40% deals stall. \u20ac2.1M+ fee income at risk.", "accent": "red", "pill": "DAY 5\u201315"},
        {"title": "Document Exam & Discrepancy", "body": "Manual UCP 600 doc check: 8\u201312 docs/LC. 3\u20134 hrs, 60\u201370% discrepancy rate. No OCR. Client abandonment at peak.", "accent": "red", "pill": "DAY 10\u201330"},
        {"title": "Sanctions & Settlement", "body": "Sequential EU/UN screening per party. 8\u201312% false positive. Deals frozen silently. Manual SWIFT MT202 re-keying. \u20ac10M+ penalty exposure.", "accent": "red", "pill": "DAY 10\u201345"},
    ],
)

# 8. Banking OS Simulation — Trade Finance (PPTX)
p.add_tiles_slide(
    "Banking OS in action — Trade Finance",
    subtitle="Six agents orchestrate the LC lifecycle through five Banking OS layers. 14–45 days → 1–3 days.",
    section_label="Future State",
    columns=3,
    tiles=[
        {"title": "Facility Setup Agent", "body": "Auto-loads sublimits from NEXUS. SENTINEL enforces limit authority. Hours vs 3–5 days.", "accent": "blue", "pill": "EFFICIENCY"},
        {"title": "LC Drafting Agent", "body": "Auto-generates MT700. NLP validates against UCP 600. One-click approve. 85% effort saved.", "accent": "blue", "pill": "GROWTH"},
        {"title": "Doc Examination Agent", "body": "IDP extracts 50+ fields. Checks against UCP 600 automatically. 90% faster.", "accent": "blue", "pill": "EFFICIENCY"},
        {"title": "Trade Sanctions Agent", "body": "All parties + vessel + HS codes screened in parallel. SENTINEL freezes NEXUS on any hit.", "accent": "purple", "pill": "CONTROL"},
        {"title": "Settlement Agent", "body": "Auto-matches nostro. Payment released only if NEXUS: Compliance Cleared. Same day.", "accent": "blue", "pill": "EFFICIENCY"},
        {"title": "Reporting Agent", "body": "Complete transaction chain from NEXUS. Regulatory auto-filed per jurisdiction. 100% traceable.", "accent": "purple", "pill": "CONTROL"},
    ],
)

# 9. Elastic Operations — Trade Finance
p.add_tiles_slide(
    "Elastic Operations — Trade Finance",
    subtitle="Total value recovered: €7.9–18.9M/yr. Recovery rate: 72%. Cycle: 14–45 days → 1–3 days.",
    section_label="Value Recovery",
    columns=3,
    tiles=[
        {"stat": "€2.9–7.3M", "title": "Growth Restored", "body": "Same-day LC issuance. 40% stall → <5%. Fee leakage sealed. Win on speed: 1–3 days vs 14–45.", "accent": "green"},
        {"stat": "€3.2–7.3M", "title": "Efficiency Gained", "body": "Doc exam 3–4 hrs → minutes. SWIFT auto-generated. 6–12 FTEs → 2–3. Parallel agents.", "accent": "blue"},
        {"stat": "€1.8–4.3M", "title": "Control Enforced", "body": "EU sanctions screened before issuance. UCP 600 validated per clause. CTR errors <0.5%.", "accent": "purple"},
    ],
)

# 11. Trust \u2192 Intent \u2192 Frontline — Pillar-to-Platform Map
p.add_pillar_platform_map_slide(
    "From trust to intent \u2014 how it maps to the Banking OS",
    subtitle="Each layer serves a specific role in the shift from trust infrastructure to intent orchestration.",
    section_label="The Architecture",
    pillars=[
        {"name": "Trust Infrastructure", "sub": "Nexus + Sentinel", "accent": "#7C3AED",
         "items": [
             {"name": "Customer State Graph", "sub": "Real-time position across Nordic accounts"},
             {"name": "Banking Ontology", "sub": "Safe banking concepts grounding AI"},
             {"name": "Decision Authority", "sub": "Policy evaluation per transaction"},
             {"name": "Audit Trail", "sub": "Immutable evidence chain"},
         ]},
        {"name": "Intent Orchestration", "sub": "Agentic Runtime", "accent": "#1A5AFF",
         "section_above": "From Trust to Intent",
         "items": [
             {"name": "Payment Authorization Agent", "sub": "Validates mandate, routes"},
             {"name": "Fraud & AML Agent", "sub": "Parallel screening, SENTINEL gates"},
             {"name": "Reconciliation Agent", "sub": "Auto-matches, enforces SLA"},
             {"name": "Exception Resolution Agent", "sub": "85% auto-resolved"},
         ]},
        {"name": "Unified Frontline", "sub": "Interaction Layer", "accent": "#1A5AFF",
         "items": [
             {"name": "Operations Workspace", "sub": "Payments ops, trade finance"},
             {"name": "RM Workspace", "sub": "Client 360, advisory"},
             {"name": "Corporate Portal", "sub": "Self-service, treasury"},
             {"name": "Conversational AI", "sub": "Natural language"},
         ]},
        {"name": "Connected Ecosystem", "sub": "Grand Central", "accent": "#5C6E84",
         "items": [
             {"name": "Grand Central", "sub": "50+ connectors, config-based"},
         ]},
    ],
    footer_left="Core Banking, Payments Rails, KYC/AML, ERP \u2014 all stay in place.",
    footer_right="Manual tracking, email escalation, 4-country fragmentation \u2014 retired."
)

# 10. Danske
p.add_case_study_slide(
    "Danske Bank \u2014 enterprise-wide platform, in production",
    body_lines=[
        "Enterprise-wide platform across Personal, Business, and Large Corporates & Institutions",
        "500 onboarding flows consolidated into a unified digital journey",
        "12 design systems rationalised into one",
        "Go-live in under 6 months \u2014 2-year acceleration on original timeline",
        "DanskeGPT adopted by 74% of employees \u2014 GenAI in reconciliations and post-trade processing",
    ],
)

# 12. Provocative close
p.add_statement_slide(
    "You have built trust infrastructure. #1 cash management in the Nordics. Top-ranked trade finance. Among the most mature API platforms in Europe. The question is whether you connect that trust to real-time decisioning \u2014 at scale. That is the shift from products to platform.",
    highlight_words=["trust infrastructure", "connect that trust to real-time decisioning", "products to platform"]
)

# 13. Next steps
p.add_tiles_slide(
    "Where do we go from here?",
    subtitle="Three concrete next steps \u2014 scoped to your priorities.",
    section_label="Next Steps",
    columns=3,
    tiles=[
        {"stat": "01", "title": "Which TxB domain first?", "body": "Which problem is costing Nordea most today \u2014 which unlocks the stakeholders needed for the full 2030 agenda?", "accent": "blue"},
        {"stat": "02", "title": "A live demonstration", "body": "Prioritised use cases against Nordea's own 2030 targets. Your scenarios, your data model, your operations.", "accent": "blue"},
        {"stat": "03", "title": "A value case", "body": "Quantified business case against Nordea's C/I, FTE, and volume metrics. Conservative. Defensible. Decision-ready.", "accent": "blue"},
    ],
)

# 14. Handoff
p.add_section_divider("Product Showcase", "What this looks like\nin practice", "Principal Solutions Engineer")

# Add speaker notes to PPTX slides
for idx, note in sorted(NOTES.items()):
    if idx < len(p.prs.slides):
        slide = p.prs.slides[idx]
        notes_slide = slide.notes_slide
        tf = notes_slide.notes_text_frame
        tf.text = note

p.save()
pptx_size = os.path.getsize(pptx_path) / 1024
print(f"PPTX saved: {pptx_path}")
print(f"PPTX slides: {len(p.slides)}")
print(f"PPTX size: {pptx_size:.1f} KB")
