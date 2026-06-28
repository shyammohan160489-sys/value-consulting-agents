#!/usr/bin/env python3
"""
Assembles the Evelyn Partners Backbase Slides deck from engine files.
Produces a single self-contained HTML file.
"""

import base64
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
APP = ROOT / "presentations" / "backbase-slides-app"
OUT = ROOT / "Engagement" / "Evelyn Partners" / "Output" / "Evelyn_Business_Case_for_Change.html"

# 1. Read template parts
template_html = (APP / "deck-template.html").read_text()

# Extract CSS (between <style> and </style>)
css_start = template_html.index("<style>") + len("<style>")
css_end = template_html.index("</style>")
css = template_html[css_start:css_end]

# Extract body (between <body> and the first <script>)
body_start = template_html.index("<body>") + len("<body>")
# Find the closing </body> but exclude scripts
# Get everything up to the first <script
first_script = template_html.index("<script", body_start)
body_html = template_html[body_start:first_script].strip()

# 2. Read engine.js
engine_js = (APP / "engine.js").read_text()

# 3. Base64 encode bg.jpg
bg_path = APP / "images" / "bg.jpg"
bg_b64 = base64.b64encode(bg_path.read_bytes()).decode()
bg_data_uri = f"data:image/jpeg;base64,{bg_b64}"

# Replace bg.jpg references in engine
engine_js = engine_js.replace("${BB_SHARED_ASSETS}/images/bg.jpg", bg_data_uri)

# 4. Define the SLIDES array
slides_js = r"""
window.BB_SHARED_ASSETS = '.';

const SLIDES = [
  // ── SLIDE 1: Cover ──
  { layout: 'cover-color-block',
    label: 'EVELYN PARTNERS \u00d7 BACKBASE',
    title: 'Business Case\nfor Change',
    date: 'April 2026',
    partner: false },

  // ── SLIDE 2: Agenda ──
  { layout: 'toc', label: 'AGENDA', title: 'Contents', numbered: true,
    items: [
      'Why Now \u2014 Three forces that make this the right moment',
      'Business Outcomes \u2014 What the upgrade delivers for Evelyn',
      'The Cost of Standing Still \u2014 What happens if nothing changes',
      'Three Paths to Consider \u2014 Options with escalating commitment and investment',
      'Our Commitment \u2014 What Backbase will do to help you build the case',
      'Mutual Activity Plan \u2014 Timeline from today to contract signature'
    ]},

  // ── SLIDE 3: Why Now \u2014 3 forcing functions ──
  { layout: 'content-columns',
    label: 'BUSINESS CASE FOR CHANGE',
    title: 'A Convergence of Timing and Ambition',
    columns: [
      { subtitle: 'Renewal Window',
        body: 'Contract renewal in May 2027 creates a natural decision point. Early action secures preferential terms, avoids disruption, and locks in the upgrade path before the current stack reaches end-of-support.' },
      { subtitle: 'Post-Acquisition Scrutiny',
        body: 'NatWest ownership brings new governance, new reporting standards, and heightened expectations on operational efficiency. The digital platform must be board-ready \u2014 not legacy-dependent.' },
      { subtitle: 'AI Momentum',
        body: 'The successful AI POC proved the art of the possible. Waiting risks losing internal champions and falling behind peers who are moving to production AI now. The window to capitalise is open.' }
    ]},

  // ── SLIDE 4: Quote ──
  { layout: 'statement', accent: 'blue', label: 'THE IMPERATIVE',
    text: 'The question is not whether to modernise \u2014 it\u2019s whether to do it <span class="hl">on your terms or under pressure.</span>' },

  // ── SLIDE 5: Business Outcomes \u2014 4 stat cards ──
  { layout: 'content-standard', theme: 'light',
    label: 'BUSINESS CASE FOR CHANGE',
    title: 'What This Means for Evelyn',
    subtitle: 'Quantified business outcomes from the platform upgrade and AI enablement.',
    body: `<div style="display:grid;grid-template-columns:1fr 1fr;gap:0.5em;margin-top:0.3em">
      <div style="padding:0.7em;background:#E5EBFF;border-radius:0.3em;border-left:0.15em solid #3366FF">
        <div style="font-size:1.6em;font-weight:800;color:#3366FF;letter-spacing:-0.02em">40%</div>
        <div style="font-size:0.45em;font-weight:700;letter-spacing:0.08em;text-transform:uppercase;color:#3366FF;margin:0.3em 0 0.5em">Reduction in Advisor Admin Time</div>
        <div style="font-size:0.5em;font-weight:300;color:rgba(9,28,53,0.6);line-height:1.6">Advisor Workspace and AI assistants shift advisors from data gathering to client engagement. Industry benchmark: advisors spend 60%+ of time on admin; best-in-class is under 40%.</div>
      </div>
      <div style="padding:0.7em;background:rgba(5,150,105,0.06);border-radius:0.3em;border-left:0.15em solid #059669">
        <div style="font-size:1.6em;font-weight:800;color:#059669;letter-spacing:-0.02em">4x Faster</div>
        <div style="font-size:0.45em;font-weight:700;letter-spacing:0.08em;text-transform:uppercase;color:#059669;margin:0.3em 0 0.5em">Meeting Preparation</div>
        <div style="font-size:0.5em;font-weight:300;color:rgba(9,28,53,0.6);line-height:1.6">AI-powered meeting prep \u2014 demonstrated in the Evelyn POC \u2014 reduces prep from 2+ hours to under 30 minutes. Immediate, measurable savings per advisor, per day.</div>
      </div>
      <div style="padding:0.7em;background:rgba(123,47,255,0.06);border-radius:0.3em;border-left:0.15em solid #7B2FFF">
        <div style="font-size:1.6em;font-weight:800;color:#7B2FFF;letter-spacing:-0.02em">6x</div>
        <div style="font-size:0.45em;font-weight:700;letter-spacing:0.08em;text-transform:uppercase;color:#7B2FFF;margin:0.3em 0 0.5em">Faster Client Onboarding</div>
        <div style="font-size:0.5em;font-weight:300;color:rgba(9,28,53,0.6);line-height:1.6">Wealth 2.0 digital onboarding with document vault and e-signature compresses onboarding from weeks to days. Peer benchmark: 31 days to 5 days.</div>
      </div>
      <div style="padding:0.7em;background:rgba(217,119,6,0.06);border-radius:0.3em;border-left:0.15em solid #D97706">
        <div style="font-size:1.6em;font-weight:800;color:#D97706;letter-spacing:-0.02em">Lower TCO</div>
        <div style="font-size:0.45em;font-weight:700;letter-spacing:0.08em;text-transform:uppercase;color:#D97706;margin:0.3em 0 0.5em">Platform Consolidation</div>
        <div style="font-size:0.5em;font-weight:300;color:rgba(9,28,53,0.6);line-height:1.6">Moving from custom legacy to product-standard reduces maintenance burden, eliminates custom code risk, and positions for continuous innovation.</div>
      </div>
    </div>
    <div style="font-size:0.4em;color:rgba(9,28,53,0.35);margin-top:0.6em;text-align:center">Benchmarks from Backbase wealth management engagements (Goodbody, HNB, industry analysis)</div>` },

  // ── SLIDE 6: Cost of Standing Still \u2014 LIGHT theme ──
  { layout: 'content-standard', theme: 'light',
    label: 'BUSINESS CASE FOR CHANGE',
    title: 'What Happens If Nothing Changes',
    subtitle: 'A side-by-side view: auto-renewal on the current stack vs. early renewal with upgrade.',
    body: `<div style="display:flex;gap:0.6em;margin-top:0.3em">
      <div style="flex:1;padding:0.7em;background:rgba(220,38,38,0.04);border:1px solid rgba(220,38,38,0.15);border-radius:0.3em;border-top:0.12em solid #FF503C">
        <div style="font-size:0.5em;font-weight:700;letter-spacing:0.1em;text-transform:uppercase;color:#FF503C;margin-bottom:0.8em">\u2718 Stay on Current Stack</div>
        <div style="font-size:0.5em;font-weight:300;color:rgba(9,28,53,0.6);line-height:2">\u2014 Custom code = growing maintenance cost<br>\u2014 Manual advisor workflows persist<br>\u2014 Legacy onboarding = slow client acquisition<br>\u2014 No AI foundation = starting from scratch later<br>\u2014 Harder to demonstrate value to NatWest board</div>
        <div style="margin-top:0.6em;padding-top:0.5em;border-top:1px solid rgba(220,38,38,0.12);font-size:0.42em;color:rgba(9,28,53,0.45);line-height:1.6"><strong style="color:#FF503C">Net result:</strong> Increasing technical debt, no competitive differentiation, and a harder conversation with new ownership every quarter.</div>
      </div>
      <div style="flex:1;padding:0.7em;background:rgba(5,150,105,0.04);border:1px solid rgba(5,150,105,0.15);border-radius:0.3em;border-top:0.12em solid #059669">
        <div style="font-size:0.5em;font-weight:700;letter-spacing:0.1em;text-transform:uppercase;color:#059669;margin-bottom:0.8em">\u2714 Move to Wealth 2.0 + AI</div>
        <div style="font-size:0.5em;font-weight:300;color:rgba(9,28,53,0.6);line-height:2">\u2714 Product-standard = continuous innovation<br>\u2714 AI-augmented advisors from day one<br>\u2714 Digital-first onboarding = competitive advantage<br>\u2714 POC momentum \u2192 production in 2027<br>\u2714 Clear modernisation story for new ownership</div>
        <div style="margin-top:0.6em;padding-top:0.5em;border-top:1px solid rgba(5,150,105,0.12);font-size:0.42em;color:rgba(9,28,53,0.45);line-height:1.6"><strong style="color:#059669">Net result:</strong> A modern, AI-ready platform that demonstrates digital leadership to NatWest from day one of the new contract term.</div>
      </div>
    </div>` },

  // ── SLIDE 7: Quote ──
  { layout: 'statement', accent: 'blue', label: 'THE CHOICE',
    text: 'Auto-renewal preserves the status quo. Early renewal with upgrade positions Evelyn as <span class="hl">a digital leader under NatWest \u2014 at preferential economics.</span>' },

  // ── SLIDE 8: Three Options \u2014 LIGHT theme, NO premium/signature labels ──
  { layout: 'content-standard', theme: 'light',
    label: 'PATH FORWARD',
    title: 'Three Paths to Consider',
    subtitle: 'Each path reflects a different level of commitment \u2014 and a different level of Backbase investment.',
    body: `<div style="display:flex;gap:0.5em;margin-top:0.3em">
      <div style="flex:1;padding:0.6em;background:#F3F6F9;border:1px solid #CED2D7;border-radius:0.3em;border-top:0.12em solid #CED2D7">
        <div style="font-size:0.65em;font-weight:700;color:#091C35">Auto-Renew</div>
        <div style="font-size:0.4em;font-weight:600;letter-spacing:0.08em;text-transform:uppercase;color:rgba(9,28,53,0.35);margin-bottom:0.6em">Do Nothing</div>
        <div style="border-top:1px solid #CED2D7;padding-top:0.5em;font-size:0.45em;font-weight:300;color:rgba(9,28,53,0.55);line-height:1.9">\u2192 12-month rolling renewal<br>\u2192 Stay on current LTS 2409<br>\u2192 Extended support becomes chargeable (Oct \u201926)<br>\u2192 No Backbase investment</div>
        <div style="margin-top:0.5em;padding-top:0.4em;border-top:1px solid #CED2D7;font-size:0.4em;color:rgba(9,28,53,0.4);line-height:1.6">Unsupported Alpha stack core when NatWest arrives. No innovation story. Reactive.</div>
        <div style="display:flex;gap:0.8em;margin-top:0.5em;padding-top:0.4em;border-top:1px solid #CED2D7">
          <div><div style="font-size:0.3em;font-weight:700;letter-spacing:0.08em;color:rgba(9,28,53,0.3);text-transform:uppercase">BB Investment</div><div style="font-size:0.6em;font-weight:800;color:rgba(9,28,53,0.3)">None</div></div>
          <div><div style="font-size:0.3em;font-weight:700;letter-spacing:0.08em;color:rgba(9,28,53,0.3);text-transform:uppercase">NatWest Ready</div><div style="font-size:0.6em;font-weight:800;color:rgba(9,28,53,0.3)">Weak</div></div>
        </div>
      </div>
      <div style="flex:1;padding:0.6em;background:rgba(217,119,6,0.04);border:1px solid rgba(217,119,6,0.2);border-radius:0.3em;border-top:0.12em solid #D97706">
        <div style="font-size:0.65em;font-weight:700;color:#091C35">Upgrade Only</div>
        <div style="font-size:0.4em;font-weight:600;letter-spacing:0.08em;text-transform:uppercase;color:#D97706;margin-bottom:0.6em">Stay Current</div>
        <div style="border-top:1px solid rgba(217,119,6,0.15);padding-top:0.5em;font-size:0.45em;font-weight:300;color:rgba(9,28,53,0.55);line-height:1.9">\u2192 Upgrade to LTS 26.09<br>\u2192 Short-term renewal (1\u20132 years)<br>\u2192 Digital Wealth (feature parity)<br>\u2192 Evelyn funds the upgrade</div>
        <div style="margin-top:0.5em;padding-top:0.4em;border-top:1px solid rgba(217,119,6,0.15);font-size:0.4em;color:#D97706;line-height:1.6">Current but not competitive. No advisor workspace, no AI, no NatWest story.</div>
        <div style="display:flex;gap:0.8em;margin-top:0.5em;padding-top:0.4em;border-top:1px solid rgba(217,119,6,0.15)">
          <div><div style="font-size:0.3em;font-weight:700;letter-spacing:0.08em;color:rgba(9,28,53,0.3);text-transform:uppercase">BB Investment</div><div style="font-size:0.6em;font-weight:800;color:#D97706">Limited</div></div>
          <div><div style="font-size:0.3em;font-weight:700;letter-spacing:0.08em;color:rgba(9,28,53,0.3);text-transform:uppercase">NatWest Ready</div><div style="font-size:0.6em;font-weight:800;color:#D97706">Moderate</div></div>
        </div>
      </div>
      <div style="flex:1;padding:0.6em;background:rgba(51,102,255,0.04);border:2px solid rgba(51,102,255,0.25);border-radius:0.3em;border-top:0.12em solid #3366FF;position:relative">
        <div style="position:absolute;top:0.25em;right:0.35em;background:#3366FF;color:#fff;font-size:0.3em;font-weight:800;letter-spacing:0.08em;padding:0.15em 0.5em;border-radius:0.5em">RECOMMENDED</div>
        <div style="font-size:0.65em;font-weight:700;color:#091C35">Strategic Partnership</div>
        <div style="font-size:0.4em;font-weight:600;letter-spacing:0.08em;text-transform:uppercase;color:#3366FF;margin-bottom:0.6em">Commit & Innovate</div>
        <div style="border-top:1px solid rgba(51,102,255,0.15);padding-top:0.5em;font-size:0.45em;font-weight:300;color:rgba(9,28,53,0.55);line-height:1.9">\u2192 Multi-year renewal (3\u20135 years)<br>\u2192 Upgrade to 26.09 + Digital Wealth<br>\u2192 Advisor Workspace + AI capabilities<br>\u2192 Backbase invests in the upgrade<br>\u2192 Incremental discounting on commitment</div>
        <div style="margin-top:0.5em;padding-top:0.4em;border-top:1px solid rgba(51,102,255,0.15);font-size:0.4em;color:#3366FF;line-height:1.6;font-weight:500">Positions Evelyn as digital leader under NatWest. Proactive, not reactive.</div>
        <div style="display:flex;gap:0.8em;margin-top:0.5em;padding-top:0.4em;border-top:1px solid rgba(51,102,255,0.15)">
          <div><div style="font-size:0.3em;font-weight:700;letter-spacing:0.08em;color:rgba(9,28,53,0.3);text-transform:uppercase">BB Investment</div><div style="font-size:0.6em;font-weight:800;color:#059669">Material</div></div>
          <div><div style="font-size:0.3em;font-weight:700;letter-spacing:0.08em;color:rgba(9,28,53,0.3);text-transform:uppercase">NatWest Ready</div><div style="font-size:0.6em;font-weight:800;color:#059669">Strong</div></div>
        </div>
      </div>
    </div>` },

  // ── SLIDE 9: Engagement Plan \u2014 what WE will do for THEM ──
  { layout: 'content-standard', theme: 'light',
    label: 'OUR COMMITMENT TO YOU',
    title: 'If You Choose the Strategic Path',
    subtitle: 'Here is what Backbase will do to help you build the case and make it happen.',
    body: `<div style="display:grid;grid-template-columns:1fr 1fr;gap:0.5em;margin-top:0.2em">
      <div style="padding:0.6em;background:#E5EBFF;border-radius:0.3em">
        <div style="font-size:0.5em;font-weight:700;color:#3366FF;margin-bottom:0.4em">\u2460 Sharpen the Value Story Together</div>
        <div style="font-size:0.45em;font-weight:300;color:rgba(9,28,53,0.6);line-height:1.7">We will run 2\u20133 deep-dive workshops with your team to validate the solution scope, map integrations, and quantify the business outcomes. No guesswork \u2014 evidence-based.</div>
      </div>
      <div style="padding:0.6em;background:#E5EBFF;border-radius:0.3em">
        <div style="font-size:0.5em;font-weight:700;color:#3366FF;margin-bottom:0.4em">\u2461 Build Your Executive Decision Paper</div>
        <div style="font-size:0.45em;font-weight:300;color:rgba(9,28,53,0.6);line-height:1.7">We will produce a board-ready business case with ROI modelling, showing 5\u20137x return on the incremental investment. Designed to arm you for NatWest conversations.</div>
      </div>
      <div style="padding:0.6em;background:#E5EBFF;border-radius:0.3em">
        <div style="font-size:0.5em;font-weight:700;color:#3366FF;margin-bottom:0.4em">\u2462 Backbase Services Investment</div>
        <div style="font-size:0.45em;font-weight:300;color:rgba(9,28,53,0.6);line-height:1.7">Michiel and the European services team will make a material investment into the upgrade delivery \u2014 directly reducing your cost to execute. Conditional on renewal commitment.</div>
      </div>
      <div style="padding:0.6em;background:#E5EBFF;border-radius:0.3em">
        <div style="font-size:0.5em;font-weight:700;color:#3366FF;margin-bottom:0.4em">\u2463 Present Back by Mid-May</div>
        <div style="font-size:0.45em;font-weight:300;color:rgba(9,28,53,0.6);line-height:1.7">Within one month, we come back with: validated solution scope, commercial proposal, and the decision paper \u2014 ready for you to take to Bids, Paul Gettis, and NatWest when the time is right.</div>
      </div>
    </div>
    <div style="font-size:0.45em;font-weight:600;color:#3366FF;margin-top:0.5em;padding:0.4em 0.6em;background:rgba(51,102,255,0.06);border:1px solid rgba(51,102,255,0.15);border-radius:0.25em;text-align:center">What we need from you: a point of contact for deep-dives \u2022 confirmation of appetite for Option 3 \u2022 visibility on who holds budget authority post-June</div>` },

  // ── SLIDE 10: Mutual Activity Plan \u2014 condensed, white theme ──
  { layout: 'content-standard', theme: 'light',
    label: 'PATH FORWARD',
    title: 'Mutual Activity Plan',
    subtitle: 'From today to upgrade kickoff \u2014 six milestones over six months.',
    body: `<table style="width:100%;border-collapse:separate;border-spacing:0 0.2em;margin-top:0.2em">
      <thead><tr>
        <th style="font-size:0.45em;font-weight:700;letter-spacing:0.1em;text-transform:uppercase;color:rgba(9,28,53,0.35);padding:0.3em 0.5em;text-align:left;width:5%">#</th>
        <th style="font-size:0.45em;font-weight:700;letter-spacing:0.1em;text-transform:uppercase;color:rgba(9,28,53,0.35);padding:0.3em 0.5em;text-align:left;width:30%">Milestone</th>
        <th style="font-size:0.45em;font-weight:700;letter-spacing:0.1em;text-transform:uppercase;color:rgba(9,28,53,0.35);padding:0.3em 0.5em;text-align:left">What happens</th>
        <th style="font-size:0.45em;font-weight:700;letter-spacing:0.1em;text-transform:uppercase;color:rgba(9,28,53,0.35);padding:0.3em 0.5em;text-align:left;width:15%">When</th>
      </tr></thead>
      <tbody>
        <tr style="background:rgba(51,102,255,0.06)">
          <td style="font-size:0.55em;font-weight:700;color:#3366FF;padding:0.4em 0.5em;border-radius:0.2em 0 0 0.2em">1</td>
          <td style="font-size:0.55em;font-weight:600;color:#091C35;padding:0.4em 0.5em">Strategic Alignment</td>
          <td style="font-size:0.5em;font-weight:300;color:rgba(9,28,53,0.6);padding:0.4em 0.5em">Confirm appetite for Option 3, identify decision-makers, agree next steps</td>
          <td style="font-size:0.5em;font-weight:600;color:#3366FF;padding:0.4em 0.5em;border-radius:0 0.2em 0.2em 0">Today</td>
        </tr>
        <tr style="background:#F3F6F9">
          <td style="font-size:0.55em;font-weight:700;color:#3366FF;padding:0.4em 0.5em;border-radius:0.2em 0 0 0.2em">2</td>
          <td style="font-size:0.55em;font-weight:600;color:#091C35;padding:0.4em 0.5em">Deep-Dive Workshops</td>
          <td style="font-size:0.5em;font-weight:300;color:rgba(9,28,53,0.6);padding:0.4em 0.5em">2\u20133 sessions: solution scope, integration mapping, bill of materials</td>
          <td style="font-size:0.5em;font-weight:400;color:rgba(9,28,53,0.6);padding:0.4em 0.5em;border-radius:0 0.2em 0.2em 0">Apr \u2013 May</td>
        </tr>
        <tr style="background:rgba(51,102,255,0.06)">
          <td style="font-size:0.55em;font-weight:700;color:#3366FF;padding:0.4em 0.5em;border-radius:0.2em 0 0 0.2em">3</td>
          <td style="font-size:0.55em;font-weight:600;color:#091C35;padding:0.4em 0.5em">Decision Paper Delivered</td>
          <td style="font-size:0.5em;font-weight:300;color:rgba(9,28,53,0.6);padding:0.4em 0.5em">Executive business case with ROI model \u2014 ready to take to NatWest</td>
          <td style="font-size:0.5em;font-weight:400;color:rgba(9,28,53,0.6);padding:0.4em 0.5em;border-radius:0 0.2em 0.2em 0">Mid-May</td>
        </tr>
        <tr style="background:#F3F6F9">
          <td style="font-size:0.55em;font-weight:700;color:#3366FF;padding:0.4em 0.5em;border-radius:0.2em 0 0 0.2em">4</td>
          <td style="font-size:0.55em;font-weight:600;color:#091C35;padding:0.4em 0.5em">NatWest Green Light</td>
          <td style="font-size:0.5em;font-weight:300;color:rgba(9,28,53,0.6);padding:0.4em 0.5em">FCA regulatory approval \u2192 NatWest\u2013Evelyn communication opens</td>
          <td style="font-size:0.5em;font-weight:400;color:rgba(9,28,53,0.6);padding:0.4em 0.5em;border-radius:0 0.2em 0.2em 0">June</td>
        </tr>
        <tr style="background:rgba(51,102,255,0.06)">
          <td style="font-size:0.55em;font-weight:700;color:#3366FF;padding:0.4em 0.5em;border-radius:0.2em 0 0 0.2em">5</td>
          <td style="font-size:0.55em;font-weight:600;color:#091C35;padding:0.4em 0.5em">Commercial & Contract</td>
          <td style="font-size:0.5em;font-weight:300;color:rgba(9,28,53,0.6);padding:0.4em 0.5em">Best & final proposal, legal review, procurement, signature</td>
          <td style="font-size:0.5em;font-weight:400;color:rgba(9,28,53,0.6);padding:0.4em 0.5em;border-radius:0 0.2em 0.2em 0">Jul \u2013 Sep</td>
        </tr>
        <tr style="background:rgba(5,150,105,0.06)">
          <td style="font-size:0.55em;font-weight:700;color:#059669;padding:0.4em 0.5em;border-radius:0.2em 0 0 0.2em">6</td>
          <td style="font-size:0.55em;font-weight:600;color:#059669;padding:0.4em 0.5em">Upgrade Kickoff</td>
          <td style="font-size:0.5em;font-weight:300;color:rgba(9,28,53,0.6);padding:0.4em 0.5em">Backbase-led LTS 26.09 upgrade with services investment</td>
          <td style="font-size:0.5em;font-weight:600;color:#059669;padding:0.4em 0.5em;border-radius:0 0.2em 0.2em 0">October</td>
        </tr>
      </tbody>
    </table>
    <div style="font-size:0.45em;font-weight:600;color:#3366FF;margin-top:0.5em;padding:0.4em 0.6em;background:rgba(51,102,255,0.06);border:1px solid rgba(51,102,255,0.15);border-radius:0.25em;text-align:center">Immediate next step: schedule deep-dive workshop #1 in late April</div>` },

  // ── SLIDE 10: Thank you ──
  { layout: 'thank-you' }
];

const SPEAKER_NOTES = {
  1: 'This section bridges the product/feature slides and the commercial offer. It answers WHY before WHAT.',
  2: 'Quick orientation for Martin. Six topics, ending with the activity plan.',
  3: 'Three forcing functions: renewal timing, NatWest scrutiny, AI momentum. Each creates urgency from a different angle.',
  4: 'Pause here. Let this land. The question is framed as WHEN, not IF.',
  5: 'All benchmarks from real Backbase wealth engagements. The 4x meeting prep was demonstrated in Evelyn\\u0027s own POC \u2014 reference it.',
  6: 'This is the urgency slide. Left = auto-renewal world. Right = what the upgrade delivers. Let Martin feel the contrast.',
  8: 'THE decision slide. Do NOT say premium or signature \u2014 just Digital Wealth and Advisor Workspace. Let them choose the path, then we scope the details in deep-dives.',
  9: 'This is Shyam\\u0027s commitment: we will build them an executive decision paper within a month. Ask for a point of contact and confirmation of appetite.',
  10: 'Six milestones. Steps 1\u20133 are in our control before June. Step 4 is the NatWest gate. Steps 5\u20136 follow once they can communicate. Jeroen to ask: who holds budget authority post-June?'
};
"""

# 5. Assemble HTML
html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Evelyn Partners \u2014 Business Case for Change</title>
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
{engine_js}
</script>

</body>
</html>
"""

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(html)
size_kb = OUT.stat().st_size // 1024
print(f"\u2713 Saved {OUT} ({size_kb} KB, 10 slides)")
print(f"  Open in browser: file://{OUT}")
