#!/usr/bin/env python3
"""Example exhibit deck — neutral content ("Meridian Bank", fictional).
Run:  python3 example_build.py [out.pptx]
Shows the canonical patterns: dark cover, stat grid + takeaway band, sorted bars,
unit dot-grid, impact close (stat-card row — the default value visual), chapter
divider, plain table. Copy this file as the starting point for a real deck build,
then replace content slide by slide.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from exhibit_pptx import (ExhibitDeck, NAVY, BLUE, BLUE2, BLUE3, BLUE4, TINT, TINT2,
                          CYAN, CORAL, WHITE, MUT, FN, HAIR, HAIR_ROW, SUB_D, W, H)
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR

OUT = sys.argv[1] if len(sys.argv) > 1 else "example_exhibit_deck.pptx"
d = ExhibitDeck()

# ---------------- S1 COVER (dark) ----------------
s = d.slide(dark=True)
d.step_glyph(s, 0.406, 0.406, 0.167, 0.166, CYAN)
d.rect(s, 0.57, 0.57, 12.19, 0.013, fill=None)
d.txt(s, 1.0, 2.0, 11.0, 0.35, "MERIDIAN BANK · BACKBASE · WORKING SESSION", size=12.5, color=CYAN, bold=True)
d.txt(s, 1.0, 2.45, 11.0, 1.9, [[("One bank, one app.", 44, WHITE, False)],
                                 [("The value conversation.", 44, WHITE, True)]], line_sp=1.05)
d.txt(s, 1.0, 4.35, 8.6, 0.9, "The market picture, the activation opportunity, and a value-led path for the priorities you have set.",
      size=15, color=SUB_D, line_sp=1.25)
d.txt(s, 11.7, 7.05, 1.06, 0.3, "Backbase", size=11, color=WHITE, bold=True, align=PP_ALIGN.RIGHT)
d.notes(s, "COVER. One line and move: 'Three pictures about the market you are in and the value on the table.'")

# ---------------- S2 STAT GRID + TAKEAWAY ----------------
s = d.slide()
d.chrome(s, "Opening · the market", "Digital investing is an experience race, and it is compounding", title_size=25)
stats = [
    ("4.2M", "retail investors in market", "+380K added last year alone (1)"),
    ("EUR 1.8bn", "robo-advisory AUM", "+72% in one year, regulator-licensed since 2025 (2)"),
    ("58%", "of flow via digital-first brokers", "up from 31% three years ago (3)"),
    ("+37%", "active clients at the market leader", "the year it unified investing into its banking app (4)"),
]
cells = [(1.0, 2.45), (7.05, 2.45), (1.0, 3.95), (7.05, 3.95)]
d.rect(s, 6.55, 2.45, 0.012, 2.75, fill=HAIR)
for (n, l, det), (cx, cy) in zip(stats, cells):
    d.txt(s, cx, cy, 5.45, 0.42, [[(n + "  ", 22, BLUE, True), (l, 13, NAVY, True)]])
    d.txt(s, cx, cy + 0.46, 5.35, 0.5, det, size=11.5, color=MUT, line_sp=1.12)
d.takeaway_band(s, "What it means: ", "you own the scale; the race is who turns it into daily activity.")
d.footnote(s, "1 Market regulator, 2026 · 2 Regulator bulletin, 2026 · 3 Exchange flow data, 2025 · 4 Leader annual report 2025. Illustrative example data.", y=6.4)
d.notes(s, "STAT GRID. Four sourced numbers, one message. DEFENSE: every number footnoted; if challenged, attribute to the named source and move on.")

# ---------------- S3 SORTED BARS ----------------
s = d.slide()
d.chrome(s, "Opening · proof from peers", "Peers that unified investing turned reach into daily activity", title_size=25)
d.txt(s, 1.0, 2.12, 5.8, 0.3, "INVESTING PENETRATION OF THE BANK BASE", size=11, color=NAVY, bold=True)
bars = [("Leading Asian retail bank (1)", "29%", BLUE, 1.00),
        ("Meridian Bank today (0)", "25-30%", NAVY, 0.95),
        ("Australian bank + broker (2)", "17%", BLUE3, 0.59),
        ("LatAm digital bank (3)", "16%", BLUE3, 0.55),
        ("US wealth giant (4)", "5.7%", BLUE4, 0.20)]
y = 2.48; bw = 5.9
for name, lab, col, frac in bars:
    d.txt(s, 1.0, y, bw - 0.7, 0.26, name, size=12, color=NAVY, bold=(col == NAVY))
    d.txt(s, 1.0 + bw - 0.78, y, 0.78, 0.26, lab, size=12, color=NAVY, bold=True, align=PP_ALIGN.RIGHT)
    d.rect(s, 1.0, y + 0.28, bw * frac, 0.22, fill=col)
    y += 0.66
d.txt(s, 1.0, y + 0.06, bw, 0.56, [[("You are already in the band on reach. ", 11.5, NAVY, True),
                                    ("What peers built next is the open race.", 11.5, NAVY, False)]], line_sp=1.12)
cases = [
    [("A US universal bank", True), (" folded investing into its main app: self-directed assets ", False), ("+80% in two years", True)],
    [("A LatAm digital bank", True), (" retired its separate investing app: ", False), ("15M investor customers, one login", True)],
    [("A Gulf bank", True), (" built wealth into its banking app: assets ", False), ("~3x in one year", True)],
]
d.txt(s, 7.35, 2.12, 5.4, 0.3, "WHAT ONE APP DID FOR THEM", size=11, color=NAVY, bold=True)
y = 2.48
for c in cases:
    d.rect(s, 7.35, y, 5.42, 0.86, fill=TINT2, round_=True)
    d.txt(s, 7.55, y + 0.12, 5.05, 0.64, [[(t, 12.5, NAVY, b) for t, b in c]], line_sp=1.12)
    y += 0.98
d.open_badge(s, 7.35, y, 5.42, "Still open · ", "client split per segment, the last number the value case needs.")
d.footnote(s, "0 Client-provided figures · 1-4 public annual reports. Definitions differ; comparison directional. Illustrative example data.")
d.notes(s, "SORTED BARS + case cards. Client bar in navy, plotted from THEIR number. Coral dashed box = the one remaining data ask.")

# ---------------- S4 UNIT DOT-GRID ----------------
s = d.slide()
d.chrome(s, "Opening · your base", "Registration is won; activation is where the value sits", title_size=25)
d.txt(s, 1.0, 2.15, 6.4, 0.3, "Registered base, 3.2M clients · one dot = 100,000", size=11.5, color=MUT)
dd = 0.30; gap = 0.115; x0 = 1.0; y0 = 2.55
for i in range(32):
    row, col = divmod(i, 8)
    d.oval(s, x0 + col * (dd + gap), y0 + row * (dd + gap), dd, dd, BLUE if i < 2 else TINT)
d.rect(s, 1.0, 4.42, 0.05, 0.72, fill=BLUE)
d.txt(s, 1.18, 4.42, 6.1, 0.85, [[("= 250K of 3.2M", 17, NAVY, True),
                                   ("  monthly-active investors today (8%)", 13, NAVY, False)]], line_sp=1.15)
d.rect(s, 7.65, 2.15, 5.11, 1.42, fill=TINT2, round_=True)
d.txt(s, 7.9, 2.30, 4.6, 0.3, "PENETRATION IS ALREADY WON", size=11, color=BLUE, bold=True)
d.txt(s, 7.9, 2.62, 4.62, 0.9, "About 1 in 4 of the bank's retail customers already hold an investing relationship, ahead of most peers on reach.", size=12.5, color=NAVY, line_sp=1.18)
d.rect(s, 7.65, 3.72, 5.11, 1.42, fill=TINT, round_=True)
d.txt(s, 7.9, 3.87, 4.6, 0.3, "ACTIVATION IS THE POOL", size=11, color=BLUE2, bold=True)
d.txt(s, 7.9, 4.19, 4.62, 0.9, "Frequency, not reach, is the gap; every +1pt monthly active is ~32K clients trading again.", size=12.5, color=NAVY, line_sp=1.18)
d.takeaway_band(s, "8% monthly active ", "is the number this program moves.", y=5.75)
d.footnote(s, "Base and actives: client-provided (discovery). Comparators directional. Illustrative example data.", y=6.42)
d.notes(s, "DOT GRID. One dot = one unit. Filled = active. The takeaway band names the single number the program moves.")

# ---------------- S5 IMPACT CLOSE (stat-card row — THE default value visual) ----------------
s = d.slide()
d.chrome(s, "Impact · onboarding", "Onboarding stops leaking the growth you already win")
d.txt(s, 1.0, 1.98, 11.7, 0.3, [[("One dynamic flow for new and existing clients", 13, BLUE, True),
                                  (" — self-serve or assisted, flexed by segment.", 13, BLUE, False)]])
d.txt(s, 1.0, 2.42, 5.0, 0.24, "WHAT IT MOVES", size=10, color=MUT, bold=True, track="100")
cards = [("42% abandoned", "6%", "application fall-out with transparent, reflexive flows"),
         ("9 days", "same day", "time to a funded, trading account"),
         ("5 hrs", "45 min", "operations effort per application"),
         ("manual", "automatic", "KYC refresh from registry data")]
cx = 1.0
for f, v, l in cards:
    d.stat_card(s, cx, 2.72, f, v, l)
    cx += 2.975
d.rect(s, 1.0, 4.50, 5.6, 0.82, fill=NAVY, round_=True)
d.txt(s, 1.25, 4.50, 5.10, 0.82, "+8 to 15% active clients within 18-24 months",
      size=15, color=WHITE, bold=True, anchor=MSO_ANCHOR.MIDDLE, line_sp=1.12)
d.txt(s, 6.95, 4.54, 5.75, 0.85,
      [[("Cost per account opened falls 60-80% at digital-first peers", 11.5, NAVY, False)],
       [("Open-banking funding removes the stated top drop-off cause", 11.5, NAVY, False)]],
      sp_after=8, line_sp=1.15)
d.proven_band(s, "two delivered programs live (Nordics, UK) · one in delivery (Gulf)")
d.footnote(s, "Benchmarks: anonymised delivered programs + public sources (appendix). Ranges: value model, sized with client data in the workshop. Illustrative example data.")
d.notes(s, "IMPACT CLOSE — the default value visual (ratified 28 Jul 2026; supersedes the 3-hero-tile close). Four moved metrics, ONE hero claim in navy, receipts beside it, proven-here strip. DEFENSE: card benchmarks from delivered programs; ranges from the value model, sized in the workshop.")

# ---------------- S6 DIVIDER ----------------
s = d.divider("02", "What it is worth, and how we start", "Ten minutes on value, then the plan.")
d.notes(s, "DIVIDER. Resume after the demo. Frame: 'You have seen the how. Now what it is worth.'")

# ---------------- S6 PLAIN TABLE (the ONE table) ----------------
s = d.slide()
d.chrome(s, "Closing · conditions", "Five conditions, five owners, one date each", title_size=25)
rows = [("Condition", "Owner", "Date"),
        ("Segment split confirmed (Q5)", "Client data office", "Within 2 weeks"),
        ("Value workshop scheduled", "Joint", "Week 3"),
        ("Architecture review", "Client IT + Backbase", "Week 4"),
        ("Commercial frame agreed", "Steering group", "Week 6")]
x = 1.0; yw = [6.2, 3.4, 2.1]; y = 2.35
for ri, row in enumerate(rows):
    cx = x
    for ci, cell in enumerate(row):
        if ri == 0:
            d.txt(s, cx, y, yw[ci], 0.3, cell.upper(), size=11, color=BLUE, bold=True)
        else:
            d.txt(s, cx, y, yw[ci], 0.3, cell, size=12.5, color=NAVY, bold=(ci == 0))
        cx += yw[ci]
    d.hline(s, x, y + 0.42, x + sum(yw), y + 0.42, color=HAIR_ROW if ri else HAIR, wpt=0.75)
    y += 0.56
d.takeaway_band(s, "One page, five commitments: ", "if these hold, the value case holds.", y=5.5)
d.footnote(s, "Dates indicative, to be confirmed in the kickoff. Illustrative example data.", y=6.35)
d.notes(s, "PLAIN TABLE. The one intentional table in the deck: condition, owner, date. Nothing else gets a table.")

d.save(OUT)
print(f"Wrote {OUT} ({len(d.prs.slides._sldIdLst)} slides)")
