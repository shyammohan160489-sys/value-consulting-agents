#!/usr/bin/env python3
"""Shyam × Tim — the leadership case behind the playbook (talent programme, 1 hour).

A separate 5-slide package (dark cover + 4 exhibit slides) on the locked
exhibit-slides-pptx engine. Every claim traces to a repo artifact; nothing
is invented. Companion to Product_Factory_Execution_Plan_Exhibit.pptx.

Run:  python3 build_tim_leadership_pptx.py [out.pptx]
"""
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(
    _HERE, '..', '..', '..', '..', '.claude', 'skills', 'exhibit-slides-pptx', 'scripts')))
from exhibit_pptx import (ExhibitDeck, NAVY, BLUE, BLUE2, BLUE3, BLUE4, TINT, TINT2,
                          CYAN, CORAL, WHITE, MUT, FN, HAIR, SUB_D, W, H)
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR

OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(_HERE, 'Shyam_Talent_Programme_Tim.pptx')
d = ExhibitDeck()


def pillar(s, x, y, w, h, tag, c, head, items, punch):
    d.rect(s, x, y, w, h, fill=TINT2, round_=True)
    d.rect(s, x, y, w, 0.34, fill=c, round_=True)
    d.txt(s, x + 0.16, y + 0.06, w - 0.3, 0.24, tag, size=9.5,
          color=WHITE if c in (BLUE, BLUE2, NAVY) else NAVY, bold=True)
    d.txt(s, x + 0.18, y + 0.46, w - 0.36, 0.28, head, size=12, color=NAVY, bold=True, line_sp=1.05)
    d.txt(s, x + 0.18, y + 0.84, w - 0.36, h - 1.4,
          [[('· ' + it, 9.5, NAVY, False)] for it in items], line_sp=1.2, sp_after=3)
    d.txt(s, x + 0.18, y + h - 0.48, w - 0.36, 0.42, punch, size=9.5, color=BLUE2, bold=True, line_sp=1.1)


# ═════════ S1 · COVER (dark) ═════════
s = d.slide(dark=True)
d.step_glyph(s, 0.406, 0.406, 0.167, 0.166, CYAN)
d.txt(s, 1.0, 2.0, 11.0, 0.35, 'TALENT PROGRAMME · SHYAM × TIM RUTTNER · ONE HOUR', size=12.5, color=CYAN, bold=True)
d.txt(s, 1.0, 2.45, 11.4, 1.9, [[('The operator behind', 44, WHITE, False)],
                                [('the playbook.', 44, WHITE, True)]], line_sp=1.05)
d.txt(s, 1.0, 4.35, 9.2, 0.9, 'Where I already operate, the philosophy the 57 slides are written in, what I see '
                              'coming for the industry, and what I am asking this programme for.',
      size=15, color=SUB_D, line_sp=1.25)
d.txt(s, 1.0, 6.35, 9.0, 0.3, 'Shyam · July 2026 · companion to the Product Factory execution playbook',
      size=11, color=MUT)
d.txt(s, 11.7, 7.05, 1.06, 0.3, 'Backbase', size=11, color=WHITE, bold=True, align=PP_ALIGN.RIGHT)
d.notes(s, 'FRAME THE HOUR: 10 min this deck, 10 min the playbook short version, 40 min working the asks. '
           'This deck answers who is asking; the playbook answers what for.')

# ═════════ S2 · WHERE I OPERATE ═════════
s = d.slide()
d.chrome(s, 'The record · where I operate', 'I already run at three altitudes: accounts, market, machine')
pillar(s, 1.0, 1.95, 3.77, 3.60, 'ACCOUNTS & PURSUITS', BLUE, 'Deals shaped and closed',
       ['SNB Capital: the 37-slide VC-track + journey maps that set the team’s deck standard',
        'BACB: pre-RFP pursuit run on a 24-hour loop, close deck delivered',
        'ABSA: five parallel workstreams, strategy to toolkit',
        'HSBC agentic frontline · Schroders · SEB · NFIS and the ROI validation cohort'],
       'Pattern: pursuit artifacts that become the client’s own decision documents.')
pillar(s, 4.97, 1.95, 3.77, 3.60, 'MARKET & CATEGORY', BLUE2, 'A public point of view',
       ['Nordic FinTech Forum 2026: opening POV, “Differentiation in the Age of AI”',
        'The Advisor Cockpit POV: a Backbase position, authored',
        'The exhibit design language: validated on live decks, ratified as the team default',
        'Autonomy framework: the value-side twin of the conversational cost model'],
       'Pattern: opinions strong enough to carry a stage, grounded enough to survive one.')
pillar(s, 8.94, 1.95, 3.77, 3.60, 'THE MACHINE', NAVY, 'Systems the team runs',
       ['Cortex: the VC AgenticOS, launched — agents, skills, telemetry, governance',
        'The Flywheel: engagements feed telemetry; fixes ship themselves for approval',
        'The Pursuit Loop, codified so any consultant or agent can run it',
        'Peers enabled: ROI improvement guide, publish-without-git protocol'],
       'Pattern: everything I touch becomes a system someone else can run.')
d.footnote(s, 'Every line traces to a repo artifact: engagement outputs, learnings, methods and launch records in the Cortex repository.')
d.notes(s, 'DEFENSE: nothing on this slide is aspiration; each bullet is a shipped artifact Tim can be shown live. '
           'The three-altitude framing is the leadership claim: account operator, category voice, systems builder at once.')

# ═════════ S3 · THE PHILOSOPHY ═════════
s = d.slide()
d.chrome(s, 'The philosophy · why 57 slides', 'The playbook is how I lead: systems that outlive the meeting')
prins = [
    ('SHIP INSTALLATIONS, NEVER REPORTS',
     'Every artifact is written as the entry contract of the next step: the wedge ladder, the pursuit loop, '
     'the specimen packs. A deliverable that only informs is a miss.'),
    ('CODIFY EVERYTHING',
     'Methods become files, decks become engines, engagements become learnings. The next person starts where '
     'I finished; that is the only compounding asset a services team has.'),
    ('EVIDENCE OVER ENTHUSIASM',
     'Every number is tagged known, assumed or ask. The playbook critiques its own capacity math before '
     'anyone else can, and phases year one down to what 1.5 FTE can actually deliver.'),
    ('DIVERGE FREELY, CONVERGE ON THE PLATFORM',
     'Think as wide as org design, FinOps and co-innovation programs; land every thread on Banking OS. '
     'Free-spirited in the room, ruthless at the point of convergence.'),
]
for i, (h_, b_) in enumerate(prins):
    x = 1.0 + (i % 2) * 5.95
    y = 1.95 + (i // 2) * 1.62
    d.rect(s, x, y, 5.75, 1.48, fill=TINT2, round_=True)
    d.rect(s, x, y + 0.08, 0.045, 1.32, fill=BLUE)
    d.txt(s, x + 0.22, y + 0.13, 5.3, 0.22, h_, size=10, color=BLUE2, bold=True)
    d.txt(s, x + 0.22, y + 0.42, 5.35, 1.0, b_, size=10.5, color=NAVY, line_sp=1.22)
d.takeaway_band(s, 'The 57 slides are that style, written down: ', 'an operating system for a business line, not a deck.')
d.footnote(s, 'The same four principles produced Cortex, the Pursuit Loop and the exhibit engine before they produced the playbook.')
d.notes(s, 'This is the answer to “why did you build 57 slides for a talent programme”: because I build the system, '
           'not the meeting. The playbook runs without me in the room; that is the point.')

# ═════════ S4 · WHAT I SEE COMING ═════════
s = d.slide()
d.chrome(s, 'The future · what I am thinking about', 'The next decade is operating models; I want us ahead of it')
hors = [
    ('COST PER OUTCOME', BLUE, 'becomes the number that matters',
     'Boards will stop asking “do we have AI” and start asking what a resolved outcome costs. Whoever '
     'measures it owns the renewal conversation.',
     'My move: the keystone model with Deepak, Value Telemetry, gain-share pricing.'),
    ('ORGS FOLLOW THE AUTONOMY CURVE', BLUE2, 'the chart is the next battleground',
     'In, on and above the loop become org-design vocabulary. Banks will redraw their pyramids into thin '
     'judgment layers over agent workforces, and they will pay whoever holds the evidence.',
     'My move: AI-Native Org Design on Engine A evidence; the CEO and CHRO door.'),
    ('VENDORS WIN BY INSTALLING', NAVY, 'the pitch deck era is ending',
     'Paid diagnostics that leave working components will beat capability decks everywhere. Co-innovation '
     'programs replace tenders for the banks that matter.',
     'My move: the wedge ladder, the Early Access route, product-led growth for Banking OS.'),
]
for i, (tag, c, head, body, move) in enumerate(hors):
    x = 1.0 + i * 3.97
    d.rect(s, x, 1.95, 3.77, 3.45, fill=TINT2, round_=True)
    d.rect(s, x, 1.95, 3.77, 0.34, fill=c, round_=True)
    d.txt(s, x + 0.16, 2.01, 3.5, 0.24, tag, size=9.5, color=WHITE, bold=True)
    d.txt(s, x + 0.18, 2.42, 3.4, 0.5, head, size=12, color=NAVY, bold=True, line_sp=1.08)
    d.txt(s, x + 0.18, 2.98, 3.4, 1.5, body, size=10, color=NAVY, line_sp=1.22)
    d.txt(s, x + 0.18, 4.62, 3.4, 0.68, move, size=9.5, color=BLUE2, bold=True, line_sp=1.15)
d.footnote(s, 'Each horizon already has a live thread in the playbook: Telemetry (ch 02), the operating model (ch 03), the wedge ladder and EAP (ch 01, 06).')
d.notes(s, 'The forward-looking slide Tim asked the objectives question about. DEFENSE: these are theses, not '
           'forecasts; each is falsifiable and each already has a funded first step in the execution plan.')

# ═════════ S5 · WHERE I AM + THE ASK ═════════
s = d.slide()
d.chrome(s, 'The ask · where this goes', 'I am asking for ownership, sponsorship and a seed, in order')
d.txt(s, 1.0, 1.95, 5.0, 0.24, 'THE MOVE I AM MAKING', size=10, color=MUT, bold=True, track='100')
cards = [('senior consultant', 'Line P&L', 'owner of the products + services line, with a real quota'),
         ('one pair of hands', 'Cortex', 'the team runs what I build: the AgenticOS, kits, methods'),
         ('deliverables', 'Installs', 'every engagement leaves Banking OS components behind'),
         ('€5,000 budget', 'Seed', 'product one packaged, demoed and launched with marketing')]
cx = 1.0
for f_, v_, l_ in cards:
    d.stat_card(s, cx, 2.28, f_, v_, l_)
    cx += 2.975
asks = [
    ('1 · A named path to owning the line', 'The leadership development I want is commercial ownership: the product + services P&L, reviewed on revenue.'),
    ('2 · ExCo-altitude sponsorship', 'CMO air cover on the category story and launch collateral; a door to the EAP nominations.'),
    ('3 · The €5,000 as seed, not training', 'It funds the Process X-Ray launch kit; the course it replaces would have taught me less than January will.'),
]
for i, (h_, b_) in enumerate(asks):
    y = 3.80 + i * 0.72
    d.rect(s, 1.0, y, 11.708, 0.62, fill=TINT2, round_=True)
    d.rect(s, 1.0, y + 0.06, 0.045, 0.50, fill=BLUE)
    d.txt(s, 1.24, y + 0.07, 3.85, 0.5, h_, size=10.5, color=NAVY, bold=True, line_sp=1.05)
    d.txt(s, 5.25, y + 0.10, 7.3, 0.46, b_, size=10, color=NAVY, line_sp=1.12)
d.takeaway_band(s, 'Judge me on January: ', 'one product in market, sold exactly the way the playbook says.', y=6.02)
d.footnote(s, 'The measurable commitments behind this sit in the playbook: proof-year targets, gates and the honest capacity math (chapters 05-06).', y=6.55)
d.notes(s, 'CLOSE OF THE HOUR. The ask ladder is deliberate: ownership is the development goal, sponsorship is '
           'Tim’s currency, the seed is the smallest and easiest yes. Leave the playbook as the appendix.')

d.save(OUT)
print(f'Wrote {OUT} ({len(d.prs.slides._sldIdLst)} slides)')
