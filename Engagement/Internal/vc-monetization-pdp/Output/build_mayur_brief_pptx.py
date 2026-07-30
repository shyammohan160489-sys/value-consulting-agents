#!/usr/bin/env python3
"""Mayur brief — engines, engagement types, activities and the plan (1:1 edition).

Eight slides on the locked exhibit engine. Condenses the 57-slide playbook for
the Mayur conversation and folds in the Tim Rutten 28 Jul direction (Org Chart
Builder as demand gen; outcome-pricing window; buyer-question framing).

Run:  python3 build_mayur_brief_pptx.py [out.pptx]
"""
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(
    _HERE, '..', '..', '..', '..', '.claude', 'skills', 'exhibit-slides-pptx', 'scripts')))
from exhibit_pptx import (ExhibitDeck, NAVY, BLUE, BLUE2, BLUE3, BLUE4, TINT, TINT2,
                          CYAN, CORAL, WHITE, MUT, FN, HAIR, HAIR_ROW, SUB_D, W, H)
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR

OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(_HERE, 'VC_Engines_Mayur_Brief.pptx')
d = ExhibitDeck()


def chip_card(s, x, y, w, h, head, body, fill=TINT2, accent=BLUE):
    d.rect(s, x, y, w, h, fill=fill, round_=True)
    d.rect(s, x, y + 0.06, 0.045, h - 0.12, fill=accent)
    d.txt(s, x + 0.20, y + 0.09, w - 0.36, 0.26, head, size=11, color=NAVY, bold=True)
    d.txt(s, x + 0.20, y + 0.37, w - 0.36, h - 0.44, body, size=9.5, color=NAVY, line_sp=1.14)


# ═════════ S1 · COVER ═════════
s = d.slide(dark=True)
d.step_glyph(s, 0.406, 0.406, 0.167, 0.166, CYAN)
d.txt(s, 1.0, 2.0, 11.0, 0.35, 'VC MONETIZATION · SHYAM × MAYUR · 1:1 BRIEF', size=12.5, color=CYAN, bold=True)
d.txt(s, 1.0, 2.45, 11.4, 1.9, [[('The engines, the engagement', 40, WHITE, False)],
                                [('types, and the plan.', 40, WHITE, True)]], line_sp=1.05)
d.txt(s, 1.0, 4.30, 9.6, 0.9, 'Two engines, six engagement types, the why behind each, the activities per '
                              'offer, and what Tim added on 28 July. Detail lives in the 57-slide playbook.',
      size=14.5, color=SUB_D, line_sp=1.25)
d.txt(s, 1.0, 6.35, 9.0, 0.3, 'Shyam · 28 July 2026 · condensed from the Product Factory playbook + the Tim 1:1 digest',
      size=11, color=MUT)
d.txt(s, 11.7, 7.05, 1.06, 0.3, 'Backbase', size=11, color=WHITE, bold=True, align=PP_ALIGN.RIGHT)
d.notes(s, 'For the Mayur 1:1. Slides 2-3 are the frame, 4-5 the substance, 6 the Tim delta, 7 the plan, 8 the asks.')

# ═════════ S2 · THE TWO ENGINES + WHY ═════════
s = d.slide()
d.chrome(s, 'The frame · two engines', 'Two engines, one wedge: evidence products and the human layer')
d.rect(s, 1.0, 1.95, 5.75, 3.05, fill=TINT, round_=True)
d.txt(s, 1.24, 2.11, 5.2, 0.22, 'ENGINE A · PRODUCT FACTORY', size=10, color=BLUE2, bold=True)
d.txt(s, 1.24, 2.36, 5.3, 0.28, 'Paid diagnostics that install the platform', size=12.5, color=NAVY, bold=True)
for i, line in enumerate(['X-Ray, Cartographer, Guardrail, Telemetry · €15-100K',
                          'Each pre-binds a layer: Missions, Nexus, Sentinel',
                          'Fees credit forward into the Mission POC']):
    d.txt(s, 1.24, 2.74 + i * 0.30, 5.3, 0.28, '· ' + line, size=10, color=NAVY, line_sp=1.1)
d.rect(s, 1.24, 3.80, 5.28, 0.98, fill=WHITE, round_=True)
d.txt(s, 1.40, 3.90, 5.0, 0.2, 'WHY THIS ENGINE', size=8.5, color=BLUE, bold=True)
d.txt(s, 1.40, 4.12, 5.0, 0.6, 'Banks already pay for weaker diagnostics (AIB ~€80K). Ours harvests evidence '
                               'only we can hold and leaves the platform installed.', size=9.5, color=NAVY, line_sp=1.15)
d.rect(s, 6.95, 1.95, 5.75, 3.05, fill=NAVY, round_=True)
d.txt(s, 7.19, 2.11, 5.2, 0.22, 'ENGINE B · AI-NATIVE SERVICES', size=10, color=CYAN, bold=True)
d.txt(s, 7.19, 2.36, 5.3, 0.28, 'The operating model and the org chart', size=12.5, color=WHITE, bold=True)
for i, line in enumerate(['Maturity · workforce · AI-Native Org Design (v0.1)',
                          'Pyramid to inverted-T on the A1-A5 autonomy curve',
                          'Pre-binds the human layer: Mission Owners, AgentOps']):
    d.txt(s, 7.19, 2.74 + i * 0.30, 5.3, 0.28, '· ' + line, size=10, color=SUB_D, line_sp=1.1)
d.rect(s, 7.19, 3.80, 5.28, 0.98, fill=NAVY, line=CYAN, line_w=0.9, round_=True)
d.txt(s, 7.35, 3.90, 5.0, 0.2, 'WHY THIS ENGINE', size=8.5, color=CYAN, bold=True)
d.txt(s, 7.35, 4.12, 5.0, 0.6, 'Nobody explains what Banking OS means for people and org. Tim (28 Jul): '
                               '"the exercise will sell." Opens the CEO and CHRO door.', size=9.5, color=SUB_D, line_sp=1.15)
d.takeaway_band(s, 'The rule that links them: ', 'Engine B services run on Engine A evidence; the Builder tool now runs in front of both.')
d.footnote(s, 'Detail: playbook ch 01 (frameworks) and ch 03 (operating model). Tim direction: Input/2026-07-28_tim-rutten-1to1_digest.md.')
d.notes(s, 'The two engines with an explicit WHY box each. The takeaway carries the Tim update: the Builder sits in front as demand gen.')

# ═════════ S3 · THE ENGAGEMENT TYPES + WHY ═════════
s = d.slide()
d.chrome(s, 'The frame · engagement types', 'Six engagement types, one funnel: each exists for one reason')
heads = [('WHAT IT IS', 3.30), ('WHY IT EXISTS', 6.80), ('COMMERCIAL MODEL', 10.10)]
for h_, hx in heads:
    d.txt(s, hx, 1.86, 3.0, 0.2, h_, size=8.5, color=BLUE, bold=True)
types = [
    ('Org Chart Builder + tool series', 'AWARENESS', 'Self-serve: drop your bank in, get benchmarked org models instantly (with demo generator + LLM tracker)', 'Demand gen at AI-native cost; shows the product before any call (Tim, 28 Jul)', 'Free · intent captured'),
    ('Ignite Inspire', 'FREE WEDGE', '~4 meetings: benchmark, leakage hypotheses, wedge choice, specimen pack', 'Qualifies the pain and the sponsor; feeds the funnel with zero friction', 'Free'),
    ('Wedge diagnostics (4 SKUs)', 'PAID EVIDENCE', 'X-Ray, Cartographer, Guardrail or Telemetry, deep on the bank’s own data', 'Paid proof that installs a layer and pre-writes the POC proposal', '€15-100K fixed · credits forward'),
    ('Mission POC', 'GO-LIVE PROOF', 'Factory Mission Sprint: top candidate live in 6-12 weeks under a named objective', 'Selling go-live, not slideware; the objective gives it a payback date', '€60K · wedge fee credited'),
    ('Value Assurance', 'RECURRING', 'Quarterly cost-per-outcome proof on live deployments', 'The renewal and expansion engine; funds the next domain', '€30-50K a year + gain share'),
    ('AI-Native Org Design', 'C-SUITE SERVICE', 'Six workshops: evidence to signed target org and transition roadmap', 'The CEO/CHRO conversation; binds the org to the OS', '€80-150K · downstream of a wedge'),
]
for i, (name, tag, what, why, comm) in enumerate(types):
    y = 2.10 + i * 0.72
    d.rect(s, 1.0, y, 11.708, 0.64, fill=TINT if i == 0 else TINT2, round_=True)
    d.rect(s, 1.0, y + 0.05, 0.045, 0.54, fill=CORAL if i == 0 else BLUE)
    d.txt(s, 1.18, y + 0.06, 2.05, 0.3, name, size=9, color=NAVY, bold=True, line_sp=1.0)
    d.txt(s, 1.18, y + 0.40, 2.05, 0.2, tag, size=7, color=BLUE2, bold=True)
    d.txt(s, 3.30, y + 0.07, 3.35, 0.54, what, size=8, color=NAVY, line_sp=1.1)
    d.txt(s, 6.80, y + 0.07, 3.15, 0.54, why, size=8, color=NAVY, line_sp=1.1)
    d.txt(s, 10.10, y + 0.07, 2.5, 0.54, comm, size=8, color=BLUE2, bold=True, line_sp=1.1)
d.footnote(s, 'Row one is the 28 Jul addition (coral: new, to be built next-Friday-fast). Outcome-based pricing variant to be added inside Tim’s 3-6 month market window.')
d.notes(s, 'THE LADDER AS A TABLE. Read top-down as the funnel: free tools → free wedge → paid evidence → go-live → recurring → C-suite service. Every row has one why.')

# ═════════ S4 · FIVE OFFERS: WHAT / WHY US / OUTCOME / FEASIBILITY ═════════
s = d.slide()
d.chrome(s, 'The offers · at a glance', 'Five offers: what each sells, why us, and what the bank gets')
heads = [('WHAT IT SELLS', 3.05), ('WHY ONLY US', 5.70), ('WHAT THE BANK GETS', 8.35), ('FEASIBILITY', 11.02)]
for h_, hx in heads:
    d.txt(s, hx, 1.88, 2.55, 0.2, h_, size=8.5, color=BLUE, bold=True)
offers = [
    ('Process X-Ray', '€50-75K',
     'Observes real flows across the 6-12 systems per journey; prices the leakage.',
     'Productizes the Factory Designer; runs the APA matrix on live client data.',
     'Mission candidates + ROI evidence + the integration landscape map.',
     'HIGH', BLUE, 'Assets exist; lite mode needs no InfoSec.'),
    ('Value Telemetry', '€15-50K + share',
     'Cost-per-outcome observability on live AI; waste scan, ROI re-proof.',
     'Only the vendor in the execution path sees cost per resolved outcome.',
     'Waste register + re-proved ROI; the recurring line.',
     'HIGH · GATED', BLUE3, 'Needs a live deployment + keystone study.'),
    ('Guardrail Studio', '€50-100K',
     'Codifies authority, policy, entitlements into executable guardrails.',
     'Rules load straight into Sentinel at install.',
     'The risk committee’s approval pack; unblocks Conversational deals.',
     'HIGH', BLUE, 'Documents and workshops only.'),
    ('Ontology Cartographer', '€75-100K',
     'Maps scattered data into the shared banking ontology; prices the truth gap.',
     'Pre-installs Nexus; metadata only, customer data stays in the bank.',
     'The € case for shared truth + the Nexus blueprint.',
     'MEDIUM', TINT, 'Deepest build; R&D alignment first.'),
    ('AI-Native Org Design', '€80-150K',
     'Redesigns the org chart on the A1-A5 curve: pyramid to inverted-T.',
     'Runs on Engine A evidence no consultancy holds; Builder generates demand.',
     'Target org + transition roadmap; CEO and CHRO altitude.',
     'MEDIUM', TINT, 'v0.1 exists; Builder pivot per Tim.'),
]
for i, (name, price, what, why, gets, feas, fc, freason) in enumerate(offers):
    y = 2.12 + i * 0.86
    d.rect(s, 1.0, y, 11.708, 0.78, fill=TINT2, round_=True)
    d.rect(s, 1.0, y + 0.06, 0.045, 0.66, fill=BLUE)
    d.txt(s, 1.18, y + 0.09, 1.85, 0.4, name, size=10, color=NAVY, bold=True, line_sp=1.02)
    d.txt(s, 1.18, y + 0.50, 1.85, 0.22, price, size=8.5, color=BLUE2, bold=True)
    d.txt(s, 3.05, y + 0.08, 2.50, 0.66, what, size=8.5, color=NAVY, line_sp=1.14)
    d.txt(s, 5.70, y + 0.08, 2.50, 0.66, why, size=8.5, color=NAVY, line_sp=1.14)
    d.txt(s, 8.35, y + 0.08, 2.50, 0.66, gets, size=8.5, color=NAVY, line_sp=1.14)
    d.rect(s, 11.02, y + 0.09, 1.55, 0.24, fill=fc, round_=True)
    d.txt(s, 11.02, y + 0.12, 1.55, 0.2, feas, size=8,
          color=WHITE if fc in (BLUE, BLUE3) else NAVY, bold=True, align=PP_ALIGN.CENTER)
    d.txt(s, 11.02, y + 0.38, 1.62, 0.4, freason, size=7.5, color=MUT, line_sp=1.1)
d.footnote(s, 'Tickets are price points to pressure-test. Deep-dives with week-by-week activities and sample outputs: playbook ch 02-03, slides 14-34.')
d.notes(s, 'Same grid as the playbook short version. If Mayur wants depth on any row, the playbook chapter carries it.')

# ═════════ S5 · ACTIVITIES PER OFFER → TRANSLATION → PLAN ═════════
s = d.slide()
d.chrome(s, 'The offers · activities and plan', 'What we actually do in each, what it becomes, and by when')
heads = [('THE ACTIVITIES', 3.05), ('TRANSLATES INTO', 7.35), ('THE PLAN', 10.30)]
for h_, hx in heads:
    d.txt(s, hx, 1.88, 3.0, 0.2, h_, size=8.5, color=BLUE, bold=True)
acts = [
    ('Process X-Ray',
     'Scope 2-3 journeys · inventory systems + interfaces · mine logs, shadow the floor · price leakage per step · rank Missions',
     'Leakage heatmap · integration map · Mission backlog · the POC proposal, pre-written',
     'Build Aug-Oct · pilot Oct-Dec · revenue Jan'),
    ('Value Telemetry',
     'Instrument live AI · tag outcomes · compute cost per outcome · waste scan · re-prove ROI · quarterly cadence',
     'Cost-per-outcome baseline · waste register with owners · the recurring contract',
     'Keystone Sep · pilot Nov-Dec · revenue Jan'),
    ('Guardrail Studio',
     'Harvest policy + authority docs · map recommend/approve/execute · score A1-A5 · codify 20-30 rules · audit design',
     'Authority map · guardrail backlog · Sentinel readiness score + blueprint',
     'Build Jan-Mar · pilot Apr-May · revenue Jun'),
    ('Ontology Cartographer',
     'Inventory data landscape · harvest schemas (metadata) · map to ontology · price truth gaps · phase the binding',
     'Coverage map · truth-gap € case · phased Nexus blueprint',
     'R&D gate Feb · pilot May-Jul · revenue Aug'),
    ('AI-Native Org Design',
     'Six workshops: evidence readout · loop postures · permission map · target org · workforce plan · transition roadmap',
     'The signed reorg paper: inverted-T target + function-by-function path',
     'Harden v0.1 Sep · first sale ~May, downstream'),
    ('Org Chart Builder (NEW)',
     'Ingest public org data · three benchmarked model flavors · instant self-serve · email capture · monthly refresh',
     'Demand gen at scale + the session opener ("here is your future org chart")',
     'Next-Friday mock · ENGAGE kiosk + workshop'),
]
for i, (name, what, out_, plan) in enumerate(acts):
    y = 2.12 + i * 0.72
    d.rect(s, 1.0, y, 11.708, 0.64, fill=TINT if 'NEW' in name else TINT2, round_=True)
    d.rect(s, 1.0, y + 0.05, 0.045, 0.54, fill=CORAL if 'NEW' in name else BLUE)
    d.txt(s, 1.18, y + 0.10, 1.80, 0.5, name, size=9, color=NAVY, bold=True, line_sp=1.02)
    d.txt(s, 3.05, y + 0.07, 4.15, 0.54, what, size=7.5, color=NAVY, line_sp=1.12)
    d.txt(s, 7.35, y + 0.07, 2.80, 0.54, out_, size=7.5, color=NAVY, line_sp=1.12)
    d.txt(s, 10.30, y + 0.07, 2.30, 0.54, plan, size=7.5, color=BLUE2, bold=True, line_sp=1.12)
d.footnote(s, 'Effort, pods and gates per the playbook register (±30%): builds 6-12 pw each, delivery 2-8 wks per install, pod = VC 1.0 + SE 0.5 + on-call SME/FDE.')
d.notes(s, 'THE ANSWER SLIDE for "what are the activities per layer, what do they translate to, how do we plan." '
           'Full week-by-week detail: playbook deep-dive slides per offer.')

# ═════════ S6 · WHAT TIM ADDED (28 JUL) ═════════
s = d.slide()
d.chrome(s, 'The Tim delta · 28 July', 'Tim’s direction changes four things in how we take this to market')
deltas = [
    ('Builder in front, service behind', 'The org-design idea flips into a self-serve demand-gen tool (orgchart.backbase.com), third in his series after the per-bank demo generator and the LLM visibility tracker. The paid engagement converts mid-funnel.'),
    ('Outcome pricing is coming', 'His read: the €350K-entry enterprise motion loses to outcome-based AI-native competitors within 3-6 months. Our small fixed wedges survive; we add an outcome variant to the ladder now.'),
    ('Frame on buyer questions', 'Buyers do not buy our internal product buckets. The narrative spine becomes: "what stays deterministic, what becomes reasoning-level, and how do I do it safely."'),
    ('Prove it on ourselves, weekly', 'Map Backbase’s own 2024→2026 org as the blueprint (he is doing marketing himself). First market: agentic banking GTM at weekly cadence. His speed test: idea to live by next Friday.'),
]
for i, (h_, b_) in enumerate(deltas):
    x = 1.0 + (i % 2) * 5.95
    y = 1.98 + (i // 2) * 1.68
    d.rect(s, x, y, 5.75, 1.54, fill=TINT2, round_=True)
    d.rect(s, x, y + 0.07, 0.045, 1.40, fill=CORAL)
    d.txt(s, x + 0.22, y + 0.12, 5.3, 0.24, h_, size=11, color=NAVY, bold=True)
    d.txt(s, x + 0.22, y + 0.42, 5.35, 1.05, b_, size=9.5, color=NAVY, line_sp=1.2)
d.takeaway_band(s, 'Validation to bank: ', '"the exercise will sell" and "one of the great angles in the toolbox to get in the door."')
d.footnote(s, 'Source: Tim Rutten 1:1, 28 Jul (full digest in the engagement folder). He is on leave two weeks from this week; next touchpoint should show shipped material.')
d.notes(s, 'For Mayur: this is the CMO direction the plan now absorbs. None of it contradicts the PDP economics; it adds a free top-of-funnel and a pricing to-do.')

# ═════════ S7 · THE PLAN (roadmap) ═════════
s = d.slide()
d.chrome(s, 'The plan · twelve months', 'One product at a time reaches six live motions inside a year')
months = ['Aug', 'Sep', 'Oct', 'Nov', 'Dec', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul']
gx0, gy0, colw, rowh = 2.72, 2.50, 0.828, 0.545
d.txt(s, gx0, gy0 - 0.62, 2.0, 0.2, '2026', size=9, color=MUT)
d.txt(s, gx0 + 5 * colw, gy0 - 0.62, 2.0, 0.2, '2027', size=9, color=MUT)
for i, m in enumerate(months):
    d.txt(s, gx0 + i * colw, gy0 - 0.36, colw, 0.22, m, size=9, color=MUT, bold=True, align=PP_ALIGN.CENTER)
    d.hline(s, gx0 + i * colw, gy0 - 0.08, gx0 + i * colw, gy0 + 7 * rowh - 0.15, color=HAIR_ROW)
grows = [
    ('Org Chart Builder', [(0, 1, CORAL, 'Mock'), (1, 2, BLUE, 'Build + ENGAGE'), (3, 9, NAVY, 'Live demand gen')], []),
    ('Keystone study', [(1, 2, BLUE2, 'With Deepak')], []),
    ('Process X-Ray', [(0, 1, BLUE4, ''), (1, 2, BLUE, 'Prototype'), (3, 2, BLUE2, 'Proof'), (5, 7, NAVY, 'Sell + install')], []),
    ('Value Telemetry', [(1, 1, BLUE4, ''), (2, 1, BLUE, ''), (3, 2, BLUE2, 'Proof'), (5, 7, NAVY, 'Recurring')], []),
    ('Guardrail Studio', [(5, 1, BLUE4, ''), (6, 2, BLUE, 'Prototype'), (8, 2, BLUE2, 'Proof'), (10, 2, NAVY, 'Sell')], []),
    ('Ontology Cartographer', [(6, 1, BLUE4, ''), (7, 2, BLUE, 'Prototype'), (9, 3, BLUE2, 'Proof')], []),
    ('Org Design (service)', [(1, 1, BLUE4, ''), (2, 3, BLUE, 'Evidence binding'), (7, 3, BLUE2, 'First engagement')], []),
]
for r, (label, bars, _g) in enumerate(grows):
    y = gy0 + r * rowh
    d.txt(s, 1.0, y + 0.04, 1.68, 0.42, label, size=9.5, color=NAVY, bold=True, line_sp=1.02)
    for (start, dur, color, blabel) in bars:
        bx = gx0 + start * colw + 0.02
        bw = dur * colw - 0.04
        d.rect(s, bx, y + 0.05, bw, 0.26, fill=color, round_=True)
        if blabel and bw > 1.1:
            d.txt(s, bx + 0.09, y + 0.09, bw - 0.14, 0.2, blabel, size=8, color=WHITE, bold=True)
d.footnote(s, 'Year one is the proof year: 3-4 paid installs (€0.4-0.5M); ten a year is the cost-neutral rate from year two. Gates and owners: playbook ch 05-06.')
d.notes(s, 'The playbook roadmap plus the Builder row on top (coral mock = the next-Friday test). Capacity-checked; never two builds at once.')

# ═════════ S8 · THE ASKS OF MAYUR ═════════
s = d.slide()
d.chrome(s, 'The asks · this 1:1', 'Four decisions from this conversation unlock the whole plan')
asks = [
    ('1 · Name the solution engineer', '0.5 FTE from the regional pool by September. The single critical-path resource for every build.'),
    ('2 · Green-light one prospect pilot', 'AIB-profile account for the X-Ray proof by October. Also decide: does the prospect-only rule apply to Telemetry, which needs a live deployment?'),
    ('3 · Back the keystone study', 'Cost-per-outcome model with Deepak in September; Telemetry, gain-share pricing and the FinOps line all depend on it.'),
    ('4 · Agree the commercial treatment', 'Quota recognition (~€200K) and the KPI choice: credited fees count as pipeline, uncredited installs as revenue. Plus: sponsor the outcome-pricing variant inside Tim’s 3-6 month window.'),
]
for i, (h_, b_) in enumerate(asks):
    chip_card(s, 1.0, 1.98 + i * 0.98, 11.708, 0.86, h_, b_)
d.takeaway_band(s, 'Everything is sequenced behind these: ', 'say yes to the four, and January reports revenue.', y=6.00)
d.footnote(s, 'The five open contradictions with owners (tollbooth, EAP eligibility, Engine B sequencing…) are in the playbook critique chapter, ready for this agenda.', y=6.52)
d.notes(s, 'Close the 1:1 on these four. Items 1-3 are unchanged PDP backlog asks; item 4 now carries the Tim pricing window as added urgency.')

d.save(OUT)
print(f'Wrote {OUT} ({len(d.prs.slides._sldIdLst)} slides)')
