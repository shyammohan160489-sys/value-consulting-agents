"""
SEB Baltic — Aija Mikelsone POV Deck
Frontline 2026 Slide Engine (self-contained HTML)
"""
import base64, os

BASE = '/Users/shyam/cortex'
OUT = f'{BASE}/Engagement/SEB/Output/SEB_Baltic_Aija_Frontline2026.html'

# Read components
with open(f'{BASE}/presentations/backbase-slides-app/deck-template.html') as f:
    template = f.read()
with open(f'{BASE}/presentations/backbase-slides-app/engine.js') as f:
    engine_js = f.read()
with open(f'{BASE}/presentations/backbase-slides-app/images/bg.jpg', 'rb') as f:
    bg_b64 = base64.b64encode(f.read()).decode()

# Extract CSS from template (between <style> and </style>)
css_start = template.index('<style>') + 7
css_end = template.index('</style>')
css = template[css_start:css_end]

# Extract body content (between <body> and </body>)
body_start = template.index('<body>') + 6
body_end = template.index('</body>')
body_html = template[body_start:body_end]

# Remove the two script tags from body
body_html = body_html.replace('<script src="slides.js"></script>', '')
body_html = body_html.replace('<script src="../backbase-slides-app/engine.js"></script>', '')

# Replace bg.jpg references in engine.js
engine_js_inline = engine_js.replace(
    '${BB_SHARED_ASSETS}/images/bg.jpg',
    f'data:image/jpeg;base64,{bg_b64}'
)

# SLIDES data
# Use regular string. For JS line breaks in titles, use \\n (Python writes \n to file,
# which JS interprets as newline char, and engine replaces with <br>)
slides_js = """
window.BB_SHARED_ASSETS = '.';

const SLIDES = [
  // 1. COVER
  { layout: 'cover-color-block', label: 'BACKBASE × SEB BALTIC', title: 'Savings, Investments\\n& Pensions', date: 'May 2026' },

  // 2. TOC
  { layout: 'toc', label: 'AGENDA', title: 'Today\\'s\\nConversation', numbered: true, items: [
    'SEB Baltic Context & Consolidation',
    'The Customer Lifecycle Opportunity',
    'Five Value Drivers',
    'Danske Bank Reference',
    'Ignite — The Method to Go Deeper'
  ]},

  // 3. BACKBASE INTRO
  { layout: 'overview-about', label: 'WHO WE ARE', title: 'The AI-native\\nBanking OS',
    subtitle: 'Backbase builds the system that orchestrates every customer, employee, and AI agent interaction across a bank\'s entire frontline.',
    stats: [
      { value: '150+', label: 'Financial institutions' },
      { value: '€200M+', label: 'Annual revenue' },
      { value: '2,500+', label: 'People globally' },
      { value: '13', label: 'Product lines' },
      { value: 'Danske', label: 'Nordic reference' }
    ]},

  // 4. SEB BALTIC CONTEXT
  { layout: 'chapter-numbered', theme: 'navy', number: '01', label: 'CONTEXT', title: 'SEB Baltic —\\nA Platform Moment', subtitle: 'Pan-Baltic consolidation, unified proposition, digital-first mandate.' },

  // 5. PAN-BALTIC CONSOLIDATION
  { layout: 'content-standard', theme: 'light', label: 'PAN-BALTIC CONSOLIDATION', title: 'Three banks becoming one — by 2027',
    subtitle: 'One bank, one proposition, one platform.',
    body: `<div style="display:flex;gap:0.8em;margin-top:0.3em">
      <div style="flex:1;padding:0.6em;background:#E5EBFF;border-radius:0.3em">
        <div style="font-size:0.45em;font-weight:700;letter-spacing:0.08em;text-transform:uppercase;color:rgba(4,19,38,0.5)">Latvia</div>
        <div style="font-size:1.2em;font-weight:700;color:#041326">20.1%</div>
        <div style="font-size:0.45em;color:rgba(4,19,38,0.5)">market share · #2</div>
      </div>
      <div style="flex:1;padding:0.6em;background:#E5EBFF;border-radius:0.3em">
        <div style="font-size:0.45em;font-weight:700;letter-spacing:0.08em;text-transform:uppercase;color:rgba(4,19,38,0.5)">Lithuania</div>
        <div style="font-size:1.2em;font-weight:700;color:#041326">24.6%</div>
        <div style="font-size:0.45em;color:rgba(4,19,38,0.5)">market share · #2</div>
      </div>
      <div style="flex:1;padding:0.6em;background:#E5EBFF;border-radius:0.3em">
        <div style="font-size:0.45em;font-weight:700;letter-spacing:0.08em;text-transform:uppercase;color:rgba(4,19,38,0.5)">Estonia</div>
        <div style="font-size:1.2em;font-weight:700;color:#041326">16.0%</div>
        <div style="font-size:0.45em;color:rgba(4,19,38,0.5)">market share · #3</div>
      </div>
    </div>
    <div style="margin-top:0.8em;display:flex;gap:0.5em">
      <div style="flex:1;padding:0.5em 0.8em;background:#F3F6F9;border-radius:0.3em;border-left:0.15em solid #3367FF">
        <div style="font-size:0.55em;font-weight:700;color:#041326">Legal consolidation</div>
        <div style="font-size:0.45em;color:rgba(4,19,38,0.5)">Three entities → one bank headquartered in Tallinn. Target: early 2027.</div>
      </div>
      <div style="flex:1;padding:0.5em 0.8em;background:#F3F6F9;border-radius:0.3em;border-left:0.15em solid #3367FF">
        <div style="font-size:0.55em;font-weight:700;color:#041326">Platform implication</div>
        <div style="font-size:0.45em;color:rgba(4,19,38,0.5)">One bank needs one customer platform. Reduce time-to-market for new products across all three markets.</div>
      </div>
      <div style="flex:1;padding:0.5em 0.8em;background:#F3F6F9;border-radius:0.3em;border-left:0.15em solid #3367FF">
        <div style="font-size:0.55em;font-weight:700;color:#041326">Strategic plan 2025-2027</div>
        <div style="font-size:0.45em;color:rgba(4,19,38,0.5)">Business growth + Technology efficiency. FTEs reduced for first time since 2018. Digital pension developed in Baltics.</div>
      </div>
    </div>` },

  // 6. COMPETITOR LANDSCAPE
  { layout: 'content-standard', theme: 'light', label: 'COMPETITIVE CONTEXT', title: 'Baltic wealth & savings — who\'s moving',
    body: `<div style="display:flex;flex-direction:column;gap:0.3em;margin-top:0.2em">
      <div style="display:flex;align-items:center;gap:0.5em;padding:0.4em 0.6em;background:#F3F6F9;border-radius:0.3em">
        <div style="min-width:5em;font-size:0.6em;font-weight:700;color:#041326">Swedbank</div>
        <div style="flex:1;font-size:0.5em;color:rgba(4,19,38,0.6)">#1 across all three markets. Strong retail investing app (Robur funds). Better savings UX in some areas.</div>
        <div style="font-size:0.4em;font-weight:700;color:#FF503C;min-width:4em;text-align:right">THREAT</div>
      </div>
      <div style="display:flex;align-items:center;gap:0.5em;padding:0.4em 0.6em;background:#F3F6F9;border-radius:0.3em">
        <div style="min-width:5em;font-size:0.6em;font-weight:700;color:#041326">Luminor</div>
        <div style="flex:1;font-size:0.5em;color:rgba(4,19,38,0.6)">DNB + Nordea merger. New Wealth Management head. Still consolidating tech post-merger.</div>
        <div style="font-size:0.4em;font-weight:700;color:#B45309;min-width:4em;text-align:right">WATCH</div>
      </div>
      <div style="display:flex;align-items:center;gap:0.5em;padding:0.4em 0.6em;background:#F3F6F9;border-radius:0.3em">
        <div style="min-width:5em;font-size:0.6em;font-weight:700;color:#041326">Citadele</div>
        <div style="flex:1;font-size:0.5em;color:rgba(4,19,38,0.6)">Latvia-focused, expanding. Digital-first. Aggressive on retail + SME. Private capital growing.</div>
        <div style="font-size:0.4em;font-weight:700;color:#B45309;min-width:4em;text-align:right">WATCH</div>
      </div>
      <div style="display:flex;align-items:center;gap:0.5em;padding:0.4em 0.6em;background:#F3F6F9;border-radius:0.3em">
        <div style="min-width:5em;font-size:0.6em;font-weight:700;color:#041326">Neobanks</div>
        <div style="flex:1;font-size:0.5em;color:rgba(4,19,38,0.6)">Revolut growing fast in Baltics. Stocks, crypto, savings vaults. Eroding younger savers.</div>
        <div style="font-size:0.4em;font-weight:700;color:#FF503C;min-width:4em;text-align:right">THREAT</div>
      </div>
    </div>
    <div style="margin-top:0.5em;padding:0.4em 0.6em;background:#FAE0DE;border-radius:0.3em;border-left:0.15em solid #FF503C">
      <div style="font-size:0.5em;color:#041326"><strong>The risk:</strong> If SEB consolidates legally but doesn't upgrade the digital savings &amp; investment experience simultaneously, the merger transition becomes a vulnerability — not an opportunity.</div>
    </div>` },

  // 7. LIFECYCLE CHAPTER
  { layout: 'chapter-numbered', theme: 'navy', number: '02', label: 'THE OPPORTUNITY', title: 'Five Value Drivers\\nAcross the Lifecycle', subtitle: 'Where the problem is, what\'s at stake, and how leaders are solving it.' },

  // 8. OPPORTUNITY 1: CROSS-SELL
  { layout: 'content-standard', theme: 'light', label: 'OPPORTUNITY 1 — ACQUIRE + ENGAGE', title: 'Banking-to-investing cross-sell',
    subtitle: 'The bank owns the client — but not their investment wallet.',
    body: `<div style="display:flex;gap:0.8em;margin-top:0.2em">
      <div style="flex:1">
        <div style="font-size:0.45em;font-weight:700;letter-spacing:0.08em;text-transform:uppercase;color:#FF503C;margin-bottom:0.3em">THE PROBLEM</div>
        <div style="font-size:0.5em;color:rgba(4,19,38,0.7);line-height:1.6">Only 5-15% of banking clients use investment services. The rest go to competitors or don't invest at all. No in-app prompts, no NBA, no seamless journey from banking to investing.</div>
      </div>
      <div style="flex:1">
        <div style="font-size:0.45em;font-weight:700;letter-spacing:0.08em;text-transform:uppercase;color:#3367FF;margin-bottom:0.3em">HOW LEADERS SOLVE IT</div>
        <div style="font-size:0.5em;color:rgba(4,19,38,0.7);line-height:1.6"><strong>Danske Bank:</strong> Unified banking + investing app. NBA engine identifies clients with wealth potential. Pre-populated investment onboarding from banking profile — zero re-KYC. In-app prompt: "You have €3K earning 0.5% — move to your portfolio?"</div>
      </div>
      <div style="flex:0.8;padding:0.5em;background:#E5EBFF;border-radius:0.3em;text-align:center">
        <div style="font-size:0.45em;font-weight:700;letter-spacing:0.08em;text-transform:uppercase;color:rgba(4,19,38,0.5)">VALUE AT STAKE</div>
        <div style="font-size:1.4em;font-weight:700;color:#3367FF;margin:0.15em 0">€300K+</div>
        <div style="font-size:0.4em;color:rgba(4,19,38,0.5)">incremental annual fee revenue<br>(compounds as AUM grows)</div>
      </div>
    </div>` },

  // 9. OPPORTUNITY 2: PENSION ENGAGEMENT
  { layout: 'content-standard', theme: 'light', label: 'OPPORTUNITY 2 — ENGAGE + RETAIN', title: 'Savings & pension engagement',
    subtitle: 'Aija\'s core domain — turning "set and forget" into active growth.',
    body: `<div style="display:flex;gap:0.8em;margin-top:0.2em">
      <div style="flex:1">
        <div style="font-size:0.45em;font-weight:700;letter-spacing:0.08em;text-transform:uppercase;color:#FF503C;margin-bottom:0.3em">THE PROBLEM</div>
        <div style="font-size:0.5em;color:rgba(4,19,38,0.7);line-height:1.6">Pension and savings products are "set and forget." No goal tracking, no contribution nudges, no tax-deadline prompts. AUM growth is passive. Engaged investors contribute 15-25% more than non-engaged.</div>
      </div>
      <div style="flex:1">
        <div style="font-size:0.45em;font-weight:700;letter-spacing:0.08em;text-transform:uppercase;color:#3367FF;margin-bottom:0.3em">HOW LEADERS SOLVE IT</div>
        <div style="font-size:0.5em;color:rgba(4,19,38,0.7);line-height:1.6">Goal-based savings with progress bars. Pension dashboard showing all pillars. Tax-deadline contribution reminders. "Excess cash in savings" detection → investment prompts. Proactive fund performance alerts.</div>
      </div>
      <div style="flex:0.8;padding:0.5em;background:#E5EBFF;border-radius:0.3em;text-align:center">
        <div style="font-size:0.45em;font-weight:700;letter-spacing:0.08em;text-transform:uppercase;color:rgba(4,19,38,0.5)">VALUE AT STAKE</div>
        <div style="font-size:1.4em;font-weight:700;color:#3367FF;margin:0.15em 0">€1.5M+</div>
        <div style="font-size:0.4em;color:rgba(4,19,38,0.5)">incremental annual fee revenue<br>from AUM uplift</div>
      </div>
    </div>` },

  // 10. OPPORTUNITY 3: RM PRODUCTIVITY
  { layout: 'content-standard', theme: 'light', label: 'OPPORTUNITY 3 — EFFICIENCY', title: 'Advisor productivity — freeing RMs for holistic advice',
    subtitle: 'From admin executor to strategic advisor.',
    body: `<div style="display:flex;gap:0.8em;margin-top:0.2em">
      <div style="flex:1">
        <div style="font-size:0.45em;font-weight:700;letter-spacing:0.08em;text-transform:uppercase;color:#FF503C;margin-bottom:0.3em">THE PROBLEM</div>
        <div style="font-size:0.5em;color:rgba(4,19,38,0.7);line-height:1.6">RMs spend 60-70% of time on admin (McKinsey). Meeting prep: 2-4 hours. Toggling 5-8 systems. Top-quartile RM productivity = 2x AUM growth vs. industry average.</div>
      </div>
      <div style="flex:1">
        <div style="font-size:0.45em;font-weight:700;letter-spacing:0.08em;text-transform:uppercase;color:#3367FF;margin-bottom:0.3em">HOW LEADERS SOLVE IT</div>
        <div style="font-size:0.5em;color:rgba(4,19,38,0.7);line-height:1.6"><strong>Danske Bank:</strong> Unified advisor workspace. AI-generated meeting briefs. Client 360 across banking + wealth + insurance. Holistic advice: one view of the full relationship. The advisor sees everything — not just their product silo.</div>
      </div>
      <div style="flex:0.8;padding:0.5em;background:#E5EBFF;border-radius:0.3em;text-align:center">
        <div style="font-size:0.45em;font-weight:700;letter-spacing:0.08em;text-transform:uppercase;color:rgba(4,19,38,0.5)">VALUE AT STAKE</div>
        <div style="font-size:1.4em;font-weight:700;color:#3367FF;margin:0.15em 0">€4.2M</div>
        <div style="font-size:0.4em;color:rgba(4,19,38,0.5)">annual capacity freed<br>(200 Baltic RMs)</div>
      </div>
    </div>` },

  // 11. OPPORTUNITY 4: RETENTION
  { layout: 'statement-stat', accent: 'blue', label: 'OPPORTUNITY 4 — RETAIN', stat: '€750K+',
    text: 'Annual revenue protected by <span class="hl">2% retention improvement</span> on a €5B Baltic AUM book. Multi-product clients (banking + wealth + pension) churn 15-25% less. The pan-Baltic consolidation is a risk moment — or an opportunity.',
    source: 'McKinsey Wealth Management Analytics · Backbase engagement data' },

  // 12. OPPORTUNITY 5: PLATFORM UNIFICATION
  { layout: 'statement-stat', accent: 'blue', label: 'OPPORTUNITY 5 — STRATEGIC', stat: '3→1',
    text: 'Three countries, one bank, <span class="hl">one platform.</span> One codebase localized per country. Reduce time-to-market. Consistent experience across LV/LT/EE. Stop paying the cost of three separate tech stacks.',
    source: 'SEB press release — simplifying Baltic legal structure, 2024' },

  // 13. VALUE SUMMARY
  { layout: 'content-standard', theme: 'light', label: 'VALUE AT STAKE — SUMMARY', title: 'Total annual opportunity: €6.75M+',
    body: `<div style="display:flex;gap:0.5em;margin-top:0.3em">
      <div style="flex:1;padding:0.5em;background:#E5EBFF;border-radius:0.3em;text-align:center">
        <div style="font-size:0.9em;font-weight:700;color:#3367FF">€300K+</div>
        <div style="font-size:0.4em;color:rgba(4,19,38,0.5)">Cross-sell</div>
      </div>
      <div style="flex:1;padding:0.5em;background:#E5EBFF;border-radius:0.3em;text-align:center">
        <div style="font-size:0.9em;font-weight:700;color:#3367FF">€1.5M+</div>
        <div style="font-size:0.4em;color:rgba(4,19,38,0.5)">Pension engagement</div>
      </div>
      <div style="flex:1;padding:0.5em;background:#E5EBFF;border-radius:0.3em;text-align:center">
        <div style="font-size:0.9em;font-weight:700;color:#3367FF">€4.2M</div>
        <div style="font-size:0.4em;color:rgba(4,19,38,0.5)">RM productivity</div>
      </div>
      <div style="flex:1;padding:0.5em;background:#E5EBFF;border-radius:0.3em;text-align:center">
        <div style="font-size:0.9em;font-weight:700;color:#3367FF">€750K+</div>
        <div style="font-size:0.4em;color:rgba(4,19,38,0.5)">Retention</div>
      </div>
      <div style="flex:1;padding:0.5em;background:#041326;border-radius:0.3em;text-align:center">
        <div style="font-size:0.9em;font-weight:700;color:#69FEFF">Strategic</div>
        <div style="font-size:0.4em;color:rgba(255,255,255,0.5)">Platform 3→1</div>
      </div>
    </div>
    <div style="margin-top:0.6em;padding:0.4em 0.6em;background:#F3F6F9;border-radius:0.3em;border-left:0.15em solid #3367FF">
      <div style="font-size:0.5em;color:rgba(4,19,38,0.7);line-height:1.6"><strong>Note:</strong> These are illustrative figures for directional conversation. An Ignite engagement validates with SEB's actual data — making the case defensible for internal decision-making.</div>
    </div>` },

  // 14. DANSKE REFERENCE
  { layout: 'chapter-numbered', theme: 'navy', number: '03', label: 'REFERENCE', title: 'Danske Bank —\\nHolistic Financial Advice', subtitle: 'Same Nordic context. Same complexity. Building the hybrid wealth model on Backbase.' },

  // 15. DANSKE DETAIL
  { layout: 'content-columns', label: 'DANSKE BANK × BACKBASE', title: 'From fragmented channels to unified engagement',
    columns: [
      { subtitle: 'The Challenge', body: 'Multiple digital channels, disconnected from advisor tools. Clients couldn\'t move seamlessly between self-service and expert advice. Advisors lacked a unified view.' },
      { subtitle: 'The Platform', body: 'Backbase Engagement Banking Platform. Unified across web, mobile, and advisor workspace. Single platform consolidating data, business logic, and workflows.' },
      { subtitle: 'The Model', body: 'Hybrid wealth: digital + human advisory as one experience. Mobile-first engagement. Seamless handoff between automated and expert advice. Holistic financial advice at scale.' },
      { subtitle: 'The Fit for SEB', body: 'Same Nordic banking context. Pan-Baltic scope adds multi-market localization. Pension and savings focus aligns with Aija\'s mandate. Consolidation timeline creates urgency.' }
    ]},

  // 16. IGNITE
  { layout: 'chapter-numbered', theme: 'navy', number: '04', label: 'NEXT STEP', title: 'Ignite — Baltic\\nInvestment Platform', subtitle: 'A scoped 2-day engagement to quantify the opportunity and build the case.' },

  // 17. IGNITE DETAIL
  { layout: 'content-columns', label: 'IGNITE — SCOPED FOR BALTIC SAVINGS & INVESTMENTS', title: '2 days. 3 deliverables. Aligned to the consolidation timeline.',
    columns: [
      { subtitle: 'Day 1: Discovery', body: 'Map the current digital savings & investment experience across LV/LT/EE. Assess maturity per lifecycle stage. Identify the platform gaps. Validate use cases with Aija\'s team.' },
      { subtitle: 'Day 2: Architecture & Value', body: 'Design the unified pan-Baltic investment platform. Quantify the business case (cross-sell, AUM uplift, RM productivity, retention). Build the phased roadmap aligned to the 2027 consolidation.' },
      { subtitle: 'SEB Gets', body: '1. Quantified value case across the lifecycle\n2. Architecture blueprint for pan-Baltic investment platform\n3. Phased roadmap: quick wins → foundation → target state' }
    ]},

  // 18. THANK YOU
  { layout: 'thank-you' }
];

const SPEAKER_NOTES = {
  1: 'Introduction meeting with Aija Mikelsone, Baltic Head of Savings, Investments and Retail Pension Offer. She owns what gets sold (product/proposition), not how it gets sold.',
  5: 'Key point: Legal consolidation creates a platform consolidation moment. One bank needs one customer platform. This is the opening.',
  8: 'Lead with this if she is focused on growth. The bank owns the client but not their investment wallet.',
  9: 'This is Aija\'s core domain. Pension and savings engagement. Lead with this if she responds to the "set and forget" problem.',
  10: 'She comes from Private Banking — she knows the RM pain. Danske is the reference here: unified workspace + AI meeting briefs.',
  11: 'The consolidation is a risk moment for retention. Clients may reassess during the merger transition.',
  14: 'Danske is the closest Nordic peer on Backbase. Same context. Use this to build credibility.',
  17: 'Close with this. The ask: Can we get 2 days before the legal consolidation is finalized? Timing creates urgency.'
};
"""

# Replace bg.jpg in engine_js
engine_js_final = engine_js_inline

# Assemble the HTML
html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>SEB Baltic — Savings, Investments & Pensions | Backbase</title>
<style>
{css}
</style>
</head>
<body>

{body_html}

<script>
{slides_js}
</script>
<script>
{engine_js_final}
</script>
</body>
</html>"""

with open(OUT, 'w') as f:
    f.write(html)

print(f"Saved: {OUT}")
print(f"Slides: 18")
print(f"Size: {len(html) // 1024}KB")
