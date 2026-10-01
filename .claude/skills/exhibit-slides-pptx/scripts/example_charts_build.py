#!/usr/bin/env python3
"""Example COMPARISON deck — the v3.3 layer, neutral content ("Meridian Bank").
Run:  python3 example_charts_build.py [out.pptx]
Exercises: waterfall (MGI/IBCS walk), paired From-To bars + growth arrow (JPM),
bullet bars with plan ticks (IBCS), segmented to-scale bar (T03), quadrant
bubble (T05), milestone strip (T08). Same laws, same chrome, titles one line.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from exhibit_pptx import (ExhibitDeck, NAVY, BLUE, BLUE2, BLUE3, BLUE4, TINT, TINT2,
                          CYAN, CORAL, WHITE, MUT, FN, HAIR, SUB_D, W, H)
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR

OUT = sys.argv[1] if len(sys.argv) > 1 else "example_charts_deck.pptx"
d = ExhibitDeck()

# ---------------- S1 WATERFALL (T24) ----------------
s = d.slide()
d.chrome(s, "Value · the cost walk", "The cost to serve walks from $48 to $31 per client")
d.txt(s, 1.0, 2.02, 7.5, 0.26, "Annual servicing cost per active client, the four moves", size=11.5, color=MUT)
d.waterfall(s, 1.0, 2.42, 8.5, 3.55, [
    ("Today", 48, 'start', "$48"),
    ("Digital shift", 9, 'down', "-$9"),
    ("Call deflection", 6, 'down', "-$6"),
    ("Voice minutes", 3, 'up', "+$3"),
    ("Back office", 5, 'down', "-$5"),
    ("Target", 31, 'end', "$31"),
], positive='down')
d.so_what_rail(s,
    [("-35%", "cost to serve across the walk, $48 to $31", BLUE),
     ("+$3", "honestly added back: voice minutes on the calls that remain", NAVY)],
    "Three of the four moves are digital adoption doing the work. The walk is "
    "priced per client, so every point of adoption pays twice: fewer calls and "
    "cheaper service.",
    y=2.1)
d.footnote(s, "Baseline: client cost allocation, FY25; moves sized from the value model, ranges in appendix. Illustrative example data.")
d.notes(s, "WATERFALL, positive='down': the savings walk blue, the add-back coral, totals navy. DEFENSE: each step has its own appendix line; the +$3 add-back is shown, not hidden.")

# ---------------- S2 PAIRED BARS + GROWTH ARROW (T26) ----------------
s = d.slide()
d.chrome(s, "Value · completed journeys", "Completed journeys double the digital share of sales")
d.txt(s, 1.0, 2.04, 7.5, 0.26, "Digital share of product sales, today vs with the journey finished", size=11.5, color=MUT)
d.paired_bars(s, 1.0, 2.55, 8.5, 3.40, [
    ("Credit line", 8, 39, "8%", "39%"),
    ("Disputes", 15, 44, "15%", "44%"),
    ("Autopay", 22, 58, "22%", "58%"),
    ("Card activation", 34, 71, "34%", "71%"),
], from_label="Today", to_label="Journey done")
d.growth_arrow(s, 2.75, 4.35, 8.35, 3.15, label="+2.1x on average")
d.so_what_rail(s,
    [("2.1x", "average share gain where the journey finishes end to end", BLUE),
     ("4 of 4", "journeys moved without a new channel, only a finished flow", NAVY)],
    "Share follows completion. Where the flow finishes in-app the channel wins "
    "on its own; no campaign was part of the move.",
    y=2.1)
d.footnote(s, "Shares: delivered-program benchmarks, anonymised; per-journey detail in appendix. Illustrative example data.")
d.notes(s, "PAIRED BARS. From = BLUE4, To = BLUE, the delta arrow carries the average. DEFENSE: benchmark programs named privately; ranges sized with client data in the workshop.")

# ---------------- S3 BULLET BARS (T25, IBCS attainment) ----------------
s = d.slide()
d.chrome(s, "Data · the contract read", "Three of five contract KPIs run ahead of plan")
d.txt(s, 1.0, 2.06, 8.0, 0.26, "August read against the contract-year plan", size=11.5, color=MUT)
d.bullet_bars(s, 1.0, 2.52, 8.55, [
    ("Monthly actives", 2.35, 2.10, "2.35M", "+12%"),
    ("Digital sales share", 44, 40, "44%", "+4pt"),
    ("Self-serve payments", 78, 71, "78%", "+7pt"),
    ("Enrollment rate", 51, 60, "51%", "-9pt"),
    ("Statement adoption", 38, 45, "38%", "-7pt"),
])
d.so_what_rail(s,
    [("3 of 5", "KPIs ahead of the contract plan at the August read", BLUE),
     ("-9pt", "enrollment gap to plan, the pilot's first target", CORAL)],
    "The book runs ahead where journeys finish and behind where enrollment "
    "starts. Wave 1 aims at the two gaps, and the plan ticks keep the claim "
    "auditable.",
    y=2.1)
d.footnote(s, "Actuals: contract reporting, August 2026; plan: the contract-year targets as signed. Illustrative example data.")
d.notes(s, "BULLET BARS, IBCS-style. Solid = actual, tick = plan, delta colored by direction. DEFENSE: both series from the same reporting, no restatement.")

# ---------------- S4 SEGMENTED TO-SCALE BAR (T03, engine-backed) ----------------
s = d.slide()
d.chrome(s, "Data · the call pool", "One pool of 3.5M calls splits into four movable blocks")
d.txt(s, 1.0, 2.10, 8.0, 0.26, "Assisted calls a year, split by what drives them", size=11.5, color=MUT)
d.segbar(s, 1.0, 2.95, 11.708, [
    ("disputes and payments", 1.4, "1.4M"),
    ("access and identity", 0.9, "0.9M"),
    ("card lifecycle", 0.7, "0.7M"),
    ("everything else", 0.5, "0.5M"),
], total="= 3.5M calls a year")
calls = [("Complete ", "takes disputes and payments: the journey finishes, the call never starts", BLUE2),
         ("Enroll ", "takes access and identity: the sleeper logs in, the reset stops", BLUE),
         ("Intercept ", "meets card lifecycle at the door with the answer ready", BLUE3)]
cx = 1.0
for lead, body, col in calls:
    d.rect(s, cx, 4.35, 0.045, 0.55, fill=col)
    d.txt(s, cx + 0.16, 4.33, 3.60, 0.62, [[(lead, 11.5, NAVY, True), (body, 11.5, MUT, False)]], line_sp=1.14)
    cx += 3.95
d.takeaway_band(s, "Every block has a lever: ", "the pool is movable demand, not a fixed cost.", y=5.55)
d.footnote(s, "Split: call-disposition analysis, June 2026 sample; widths strictly proportional. Illustrative example data.")
d.notes(s, "SEGBAR. One total split to scale; each block mapped to the lever that moves it. DEFENSE: split from the client's own disposition data, sample month named.")

# ---------------- S5 QUADRANT BUBBLE (T05, engine-backed) ----------------
s = d.slide()
d.chrome(s, "Priorities · where to start", "Two journeys sit in the fix-first zone")
d.quadrant(s, 2.1, 2.30, 7.1, 3.55, [
    ("Password reset", 0.86, 0.82),
    ("Dispute status", 0.62, 0.86),
    ("Payment failure", 0.74, 0.64),
    ("Card replace", 0.52, 0.36),
    ("Statement copy", 0.26, 0.60),
    ("Address change", 0.16, 0.26),
], "Call volume driven", "Digital fix feasibility",
    zone_caps=(None, "FIX FIRST", "LEAVE FOR NOW", None),
    move=(0.52, 0.38, 0.70, 0.66))
d.so_what_rail(s,
    [("2", "journeys carry most of the volume and are fully fixable in-app", BLUE),
     ("$4.1M", "a year on those two alone, at $15 a call", NAVY)],
    "Volume and feasibility pick the order. The top-right pair funds the "
    "program; the bottom-left pair waits without costing anything.",
    y=2.1)
d.footnote(s, "Volume: disposition analysis; feasibility: joint scoring in the August working session. Illustrative example data.")
d.notes(s, "QUADRANT. Target zone tinted, dashed move arrow = the sequencing claim. DEFENSE: feasibility scored jointly with the client team, not by us alone.")

# ---------------- S6 MILESTONE STRIP (T08, engine-backed) ----------------
s = d.slide()
d.chrome(s, "Implementation · the clock", "Ninety days take the program from data to a priced decision")
d.milestone_strip(s, 1.0, 2.75, 11.708, [
    ("10", "Baseline locked", "nightly feed live, definitions agreed with finance"),
    ("45", "Pilot read", "two use cases scored against the exit criteria"),
    ("90", "Priced decision", "wave 1 go or no-go, every rate client-anchored"),
], band=("Ninety days, three gates: ", "every number priced from your own feed."))
d.footnote(s, "Dates from kickoff; gates are decisions the client owns, criteria fixed before the pilot starts. Illustrative example data.")
d.notes(s, "MILESTONE STRIP. Three oversized day-counts, gates on the line, the band carries the promise. DEFENSE: exit criteria agreed before the pilot, so the read cannot be argued after.")

d.save(OUT)
print(f"Wrote {OUT} ({len(d.prs.slides._sldIdLst)} slides)")
