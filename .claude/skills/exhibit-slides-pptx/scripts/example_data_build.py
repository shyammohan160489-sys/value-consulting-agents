#!/usr/bin/env python3
"""Example DATA deck — the v3.2 data-exhibit layer, neutral content ("Meridian Bank").
Run:  python3 example_data_build.py [out.pptx]
Exercises every chart primitive: bars + so-what rail, line panels, pulse-panel grid,
double-click stage board, swimlane wave roadmap, codified dot grid. Copy the slide
you need next to example_build.py's patterns; same laws, same chrome, zero restyling.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from exhibit_pptx import (ExhibitDeck, NAVY, BLUE, BLUE2, BLUE3, BLUE4, TINT, TINT2,
                          CYAN, CORAL, WHITE, MUT, FN, HAIR, SUB_D, W, H)
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR

OUT = sys.argv[1] if len(sys.argv) > 1 else "example_data_deck.pptx"
d = ExhibitDeck()

# ---------------- S1 COLUMN CHART + SO-WHAT RAIL (P1 + P2) ----------------
s = d.slide()
d.chrome(s, "Data · digital reach", "Monthly actives doubled, and first-time growth is slowing")
d.txt(s, 1.0, 2.02, 7.0, 0.26, "Cumulative monthly-active investors, contract year 2", size=11.5, color=MUT)
d.bars(s, 1.0, 2.42, 8.5, 3.55, [
    ("Apr 25", 1.05, "1.05M"),
    ("Jul 25", 1.72, "1.72M", "+0.67M"),
    ("Sep 25", 1.96, "1.96M", "+0.24M"),
    ("Nov 25", 2.12, "2.12M", "+0.16M"),
    ("Jan 26", 2.26, "2.26M", "+0.14M"),
    ("Mar 26", 2.35, "2.35M", "+0.09M"),
], mode='time')
d.so_what_rail(s,
    [("+1.30M", "actives added across year 2, from 1.05M to 2.35M", BLUE),
     ("45K", "first-time users a month by March, from 220K in April", CORAL)],
    "The base is real and the easy growth is over. At 45K a month the absent "
    "1.9M arrive on their own in four years; bringing them in must be engineered.",
    y=2.1)
d.footnote(s, "Source: cumulative unique actives, platform contract reporting, year 2 (Apr 2025 to Mar 2026); six of eleven months shown. Illustrative example data.")
d.notes(s, "COLUMN CHART + RAIL. The chart is the evidence, the rail is the argument. "
           "DEFENSE: actives from contract reporting, not analytics estimates; months elided for readability, full table in appendix.")

# ---------------- S2 LINE PANELS + RAIL (P3) ----------------
s = d.slide()
d.chrome(s, "Data · the broadcast ceiling", "The campaign engine tripled its volume and response halved")
d.txt(s, 1.0, 2.00, 8.2, 0.26, "Banner delivery and response, aligned monthly panels", size=11.5, color=MUT)
imp = [2.1, 3.4, 4.6, 8.5, 9.8, 11.4, 13.2, 15.6, 18.9, 23.6, 15.4, 17.8]
clk = [24.1, 18.9, 27.5, 35.8, 30.2, 24.8, 33.1, 17.5, 21.4, 63.8, 41.2, 36.9]
d.line_panel(s, 1.0, 2.38, 8.5, 1.72, imp, label="Impressions per month", color=BLUE3,
             annos=[(3, "8.5M", None, 'down'), (9, "23.6M", None, 'up')])
d.line_panel(s, 1.0, 4.28, 8.5, 1.95, clk, label="Clicks per month", color=NAVY,
             annos=[(3, "35.8K", None, 'up'), (7, "17.5K", None, 'down'),
                    (9, "63.8K", "record clicks, the month new campaigns launched", 'up')],
             ticks=[(0, "Nov 24"), (4, "Mar 25"), (8, "Nov 25"), (11, "Apr 26")])
d.so_what_rail(s,
    [("2.8x", "more impressions across twelve months", BLUE),
     ("0.07%", "response rate by the end of the climb, from 0.42%", CORAL)],
    "The record month came from new, relevant things to respond to, not from "
    "more banners. Relevance is the mechanism; attribution is part of the fix.",
    y=2.1)
d.footnote(s, "Source: campaign cloud monitoring, monthly banner telemetry, Nov 2024 to Apr 2026; test and partial months excluded. Illustrative example data.")
d.notes(s, "LINE PANELS. Two thin panels beat one dual-axis chart. DEFENSE: same telemetry system both panels, comparisons hold within it.")

# ---------------- S3 PULSE-PANEL GRID (P4) ----------------
s = d.slide()
d.chrome(s, "Data · the daily pulse", "A day in the digital estate: the signals fire all day")
d.txt(s, 1.0, 1.98, 11.5, 0.26,
      "Every measured task, four sampled days · the day job in blue, friction in coral, growth in deep blue",
      size=11.5, color=MUT)
cells = [
    {"label": "Sign-ins",            "series": [69.8, 109.4, 84.2, 95.1], "range": "69.8K - 109.4K a day", "theme": BLUE3},
    {"label": "Payments set up",     "series": [20.8, 35.0, 27.4, 31.2],  "range": "20.8K - 35.0K a day",  "theme": BLUE},
    {"label": "Statement downloads", "series": [3.9, 6.4, 5.2, 5.8],      "range": "3.9K - 6.4K a day",    "theme": BLUE3},
    {"label": "Autopay setups",      "series": [420, 661, 540, 610],      "range": "420 - 661 a day",      "theme": BLUE3},
    {"label": "Reset, recovery",     "series": [3.3, 5.2, 4.1, 4.8],      "range": "3.3K - 5.2K a day",    "theme": CORAL},
    {"label": "Declined, retried",   "series": [1.1, 1.9, 1.4, 1.7],      "range": "1.1K - 1.9K a day",    "theme": CORAL},
    {"label": "Card activations",    "series": [1.0, 1.9, 1.3, 1.6],      "range": "1.0K - 1.9K a day",    "theme": BLUE3},
    {"label": "Enrollments",         "series": [587, 1000, 720, 890],     "range": "587 - 1.0K a day",     "theme": BLUE3},
    {"label": "Profile updates",     "series": [458, 711, 520, 640],      "range": "458 - 711 a day",      "theme": BLUE3},
    {"label": "Income updates",      "series": [325, 492, 380, 445],      "range": "325 - 492 a day",      "theme": BLUE2},
    {"label": "Credit line asks",    "series": [196, 324, 240, 310],      "range": "196 - 324 a day",      "theme": BLUE2},
    {"label": "Offer activations",   "series": [0, 90, 180, 288],         "range": "0 → 288 a day",   "theme": BLUE2},
]
d.panel_grid(s, 1.0, 2.32, 11.708, cells, cols=6)
calls = [("Frequency sets priority ", "payments then statements are the pilot's first use cases", BLUE),
         ("Distress is visible, live ", "3 to 5K recovery struggles a day, each one a call being born", CORAL),
         ("Growth barely registers ", "income, credit line, offers: under 1K a day combined", BLUE2)]
cx = 1.0
for lead, body, col in calls:
    d.rect(s, cx, 4.80, 0.045, 0.55, fill=col)
    d.txt(s, cx + 0.16, 4.78, 3.60, 0.62, [[(lead, 11.5, NAVY, True), (body, 11.5, MUT, False)]], line_sp=1.14)
    cx += 3.95
d.takeaway_band(s, "The signals fire all day ", "and nothing acts on them; the fix is a reflex inside the app.", y=5.66)
d.footnote(s, "Source: nightly data feed, four sampled days as measured; two are Sundays, so weekday levels run higher. Illustrative example data.")
d.notes(s, "PULSE GRID. Live telemetry = instant operational credibility; every panel is already a baseline. DEFENSE: as-measured days, no smoothing.")

# ---------------- S4 DOUBLE-CLICK STAGE BOARD (P8) ----------------
s = d.slide()
d.chrome(s, "Solution · double-click 4 of 4", "Four plays meet the calls that still arrive")
d.frame_band(s, 1.0, 1.98, 11.708, "OPPORTUNITY",
             "all 2.1M calls reach this door · 58% contained today · every lever's removals are read here, counted once")
cols = [
    ("Before the dial", [(1, "Pre-empt SMS", "distress scored before the dial; the fix arrives first")]),
    ("At the door", [(2, "The knowing door", "intent read from number and signals; greeted in plain speech"),
                     (3, "SMS bridge", "the task fits digital; link sent, line held to the finish")]),
    ("The pressure valve", [(4, "The rage-quit path", "say operator twice and a human connects instantly, context attached")]),
    ("After every call", [(5, "The learning loop", "stated reasons become taxonomy; transcripts train the next intercept")]),
]
cx = 1.0
for title, plays in cols:
    d.stage_column(s, cx, 2.55, 2.12, 3.30, title, plays)
    cx += 2.24
d.rect(s, 9.98, 2.55, 2.71, 3.30, fill=NAVY, round_=True)
d.txt(s, 10.18, 2.71, 2.31, 0.24, "SOLUTION", size=10.5, color=CYAN, bold=True, track="120")
d.txt(s, 10.18, 3.05, 2.31, 2.70, [
    [("RELATIONSHIP", 10.5, CYAN, True)], [("INTELLIGENCE", 10.5, CYAN, True)],
    [("Scores call-risk before the dial, joins number with signals, remembers declines.", 10, WHITE, False)],
    [("", 4, WHITE, False)],
    [("CONVERSATIONAL", 10.5, CYAN, True)], [("BANKING", 10.5, CYAN, True)],
    [("Meets the call as a conversation: the knowing greeting, the graceful handoff.", 10, WHITE, False)],
], line_sp=1.16, sp_after=3)
d.frame_band(s, 1.0, 6.02, 11.708, "VALUE",
             "about 35K calls per containment point above 58% · about $0.5M a point at $15 a call · a rate, not a pool")
d.footnote(s, "Containment and cost per call: client contact-center reporting; play mapping from the working session. Illustrative example data.")
d.notes(s, "STAGE BOARD. Opportunity band, plays by stage, product rail, value band. DEFENSE: value stated as a rate per point, never a pool.")

# ---------------- S5 SWIMLANE WAVE ROADMAP (P9) ----------------
s = d.slide()
d.chrome(s, "Implementation · by capability and wave", "The roadmap: front door first, intelligence next")
wave_x = [3.05, 6.28, 9.51]
for wx, (t, sub) in zip(wave_x, [("Wave 1 · pilot", "proves the lift"),
                                  ("Wave 2", "after the lift is proven"),
                                  ("Wave 3", "after the adoption read")]):
    d.txt(s, wx, 2.06, 3.0, 0.24, t, size=13, color=NAVY, bold=True)
    d.txt(s, wx, 2.30, 3.0, 0.22, sub, size=10, color=MUT)
lanes = [("Conversational Banking", "the front door"),
         ("Relationship Intelligence", "the always-on intelligence"),
         ("Customer Operations", "agentic process automation")]
ly = 2.62
for title, sub in lanes:
    d.lane_row(s, 1.0, ly, 1.92, 1.08, title, sub)
    ly += 1.18
d.chip(s, 3.05, 2.74, 2.95, 0.40, "Guided payments · COMPLETE", fill=BLUE, tc=WHITE, fs=9.5, bold=True)
d.chip(s, 3.05, 3.22, 2.95, 0.40, "IVR intercept bridge · INTERCEPT", fill=BLUE3, tc=WHITE, fs=9.5, bold=True)
d.chip(s, 6.28, 2.74, 2.95, 0.40, "Containment across top intents", fill=BLUE3, tc=WHITE, fs=9.5, bold=True)
d.txt(s, 9.51, 2.80, 3.1, 0.60, "access, card lifecycle, disputes · priced at each pilot read", size=10, color=BLUE, line_sp=1.15)
d.txt(s, 3.05, 4.00, 2.95, 0.55, "enroll + engage + complete · 240-430K calls, every rate client-anchored", size=10, color=BLUE, line_sp=1.15)
d.chip(s, 6.28, 3.92, 2.95, 0.40, "Personalized home and nudges", fill=BLUE4, tc=NAVY, fs=9.5, bold=True)
d.chip(s, 9.51, 4.40, 2.95, 0.40, "Offers timed by signals · ENROLL", fill=BLUE4, tc=NAVY, fs=9.5, bold=True)
d.chip(s, 9.51, 5.10, 2.95, 0.40, "Message resolution · autopay", fill=BLUE2, tc=WHITE, fs=9.5, bold=True)
d.hline(s, 3.05, 6.18, 12.66, 6.18, color=HAIR, wpt=0.75)
d.diamond(s, 6.21, 6.11, 0.14, 0.14, CORAL)
d.txt(s, 6.42, 6.24, 2.6, 0.24, "gate · pilot lift proven", size=10, color=MUT)
d.diamond(s, 9.44, 6.11, 0.14, 0.14, CORAL)
d.txt(s, 9.65, 6.24, 2.6, 0.24, "gate · adoption read", size=10, color=MUT)
d.footnote(s, "Sequence indicative; every coral gate is a decision the client owns, priced at the preceding read. Illustrative example data.")
d.notes(s, "WAVE ROADMAP. Lanes are products, waves are gated by reads, chips carry the lever tag. DEFENSE: no date promises, gates carry the commitment.")

# ---------------- S6 DOT GRID + HERO (T09 codified) ----------------
s = d.slide()
d.chrome(s, "Data · your base", "Registration is won; activation is where the value sits")
d.txt(s, 1.0, 2.06, 6.4, 0.26, "Registered base, 3.2M clients · one dot = 40,000", size=11.5, color=MUT)
d.dot_grid(s, 1.0, 2.48, 10, 8, 20, dot=0.22, gap=0.09)
d.rect(s, 1.0, 5.10, 0.05, 0.60, fill=BLUE)
d.txt(s, 1.18, 5.10, 5.6, 0.40, [[("= 800K of 3.2M", 17, NAVY, True)]])
d.txt(s, 1.18, 5.44, 5.6, 0.30, "monthly-active investors today (25%)", size=12, color=MUT)
d.hero_stat(s, 7.60, 2.55, 5.0, "25%", "of the base already invests monthly, ahead of most peers on reach", BLUE)
d.hero_stat(s, 7.60, 3.62, 5.0, "+1pt", "of monthly activity is 32K clients trading again", NAVY)
d.implication_card(s, 7.60, 4.72, 5.06, 1.30,
    "Reach is won; frequency is the pool. Every point of monthly activity is 32K "
    "clients back in the app, and the program is priced on that rate.")
d.footnote(s, "Base and actives: client-provided (discovery); peer comparators directional. Illustrative example data.")
d.notes(s, "DOT GRID codified + hero stats + implication. DEFENSE: actives from the client's own reporting; peers directional only.")

d.save(OUT)
print(f"Wrote {OUT} ({len(d.prs.slides._sldIdLst)} slides)")
