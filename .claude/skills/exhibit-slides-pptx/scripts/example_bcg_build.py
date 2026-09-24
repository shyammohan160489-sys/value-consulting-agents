#!/usr/bin/env python3
"""Example EVIDENCE deck — the v3.4 layer, neutral content ("Meridian", fictional).
Run:  python3 example_bcg_build.py [out.pptx]
Exercises: player dossier (fact rail + leader notes + logo wall + ring stat),
harvey evaluation matrix, grouped logo wall, tile grid, agenda tracker rail,
RAG coverage matrix, honesty tags. Same chrome, same laws, titles one line.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from exhibit_pptx import (ExhibitDeck, NAVY, BLUE, BLUE2, BLUE3, BLUE4, TINT, TINT2,
                          CYAN, CORAL, WHITE, MUT, FN, HAIR, SUB_D, W, H)
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR

OUT = sys.argv[1] if len(sys.argv) > 1 else "example_bcg_deck.pptx"
d = ExhibitDeck()

# ---------------- S1 PLAYER DOSSIER (T32+T33+T34+T37) ----------------
s = d.slide()
d.chrome(s, "Landscape · player profile 3 of 9", "MeridianPay in one page: reach, model, and who it runs with")
d.chip(s, 1.0, 2.02, 1.7, 0.30, "SEA · EST. 2019", fill=TINT2, tc=NAVY, fs=9, bold=True)
d.fact_rail(s, 1.0, 2.55, 3.35, [
    ("F", "Founded", "2019, Singapore"),
    ("$", "Funding", "$140M raised, Series C"),
    ("#", "Users", "2.1M customers (Jun 2026)"),
    ("G", "Markets", "Singapore, Vietnam, Philippines"),
    ("T", "Type", "digital challenger, SME focus"),
    ("P", "Products", "accounts, payments, BNPL, FX"),
])
d.rect(s, 5.30, 2.55, 1.75, 3.45, fill=NAVY, round_=True)
d.rect(s, 5.44, 2.72, 1.47, 3.11, fill=TINT2, round_=True)
d.rect(s, 5.58, 2.90, 1.19, 0.55, fill=BLUE, round_=True)
for i in range(3):
    d.rect(s, 5.58, 3.62 + i * 0.62, 1.19, 0.46, fill=TINT, round_=True)
d.leader_note(s, 7.05, 3.05, 7.55, 2.75, "Instant onboarding",
              "an SME account opens in 4 minutes, eKYC only")
d.leader_note(s, 7.05, 4.05, 7.55, 3.95, "One balance, three markets",
              "collections in local rails settle to one wallet")
d.leader_note(s, 6.95, 5.25, 7.55, 5.15, "Lending inside the flow",
              "BNPL underwritten from live receivables")
d.txt(s, 9.95, 2.55, 2.7, 0.24, "WORKS WITH", size=10, color=NAVY, bold=True, track="110")
d.logo_wall(s, 9.95, 2.88, 2.71, ["Visa", "Adyen", "Xero", "AWS"], cols=2, chip_h=0.52)
d.ring_stat(s, 10.55, 4.55, 0.95, "4.2", "app rating held across all three markets")
d.footnote(s, "Profile: company site, funding announcements, app-store data, June 2026. Illustrative example data.")
d.notes(s, "PLAYER DOSSIER (serial template: one per player, repeat verbatim). DEFENSE: every fact sourced in the footnote; no logos fabricated — text chips until assets are supplied.")

# ---------------- S2 HARVEY EVALUATION MATRIX (T30+T31) ----------------
s = d.slide()
d.chrome(s, "Selection · the long-list read", "Two vendors clear the bar on the four gating criteria")
d.eval_matrix(s, 1.0, 2.15, 11.7,
              [{"name": "Vendor A", "sub": "core platform"},
               {"name": "Vendor B", "sub": "digital core"},
               {"name": "Vendor C", "sub": "legacy suite"},
               {"name": "Vendor D", "sub": "cloud native"},
               {"name": "Vendor E", "sub": "regional"}],
              [("R", "Live neobank references"),
               ("M", "Market position and momentum"),
               ("T", "Technical fit and integration"),
               ("$", "Commercials inside the envelope")],
              [[1.0, 0.75, 0.5, 1.0, 0.25],
               [1.0, 0.5, 0.75, 0.75, 0.5],
               [0.75, 0.5, 0.25, 1.0, 0.5],
               [0.75, 0.75, 0.5, 0.75, 0.25]])
d.takeaway_band(s, "Two clear the bar: ", "deep-dive A and D against the pilot scope next.", y=5.78)
d.footnote(s, "Scoring: joint working session, criteria fixed before the read; detail per vendor in appendix. Illustrative example data.")
d.notes(s, "HARVEY MATRIX. Verdict per cell, criteria fixed BEFORE scoring. DEFENSE: scoring done jointly with the client team, appendix carries the per-cell rationale.")

# ---------------- S3 GROUPED LOGO WALL (T32+T39) ----------------
s = d.slide()
d.chrome(s, "Landscape · who is in the market", "The ecosystem splits into four camps around the client")
d.tag_chip(s, "Not exhaustive")
camps = [
    ("INCUMBENT BANKS", "4", ["First National", "Union Trust", "Coastal Bank", "Meridian Bank"]),
    ("DIGITAL CHALLENGERS", "3", ["NovaPay", "Finlio", "Brightbank"]),
    ("INFRASTRUCTURE", "4", ["RailsCo", "LedgerWorks", "PayMesh", "CloudCore"]),
    ("BIG TECH ADJACENT", "3", ["ShopOS", "SuperApp One", "MarketPlaceX"]),
]
cx = 1.0
for title, count, names in camps:
    d.chip(s, cx, 2.15, 2.83, 0.36, title, fill=TINT, tc=NAVY, fs=9.5, bold=True)
    d.oval(s, cx + 2.45, 2.19, 0.28, 0.28, BLUE, label=count, fs=10)
    d.logo_wall(s, cx, 2.66, 2.83, names, cols=1, chip_h=0.48, gap=0.10)
    cx += 2.96
d.takeaway_band(s, "The middle is crowded: ", "infrastructure players set the pace, and two camps buy rather than build.", y=5.55)
d.footnote(s, "Mapping: public registers and press, August 2026; camp assignment is ours. Illustrative example data.")
d.notes(s, "GROUPED LOGO WALL. Text chips stand in until logo assets are dropped per deck; client's own account stays clean text always.")

# ---------------- S4 TILE GRID (T35) ----------------
s = d.slide()
d.chrome(s, "Plan · the first quarter", "Six moves carry the first ninety days")
d.tiles(s, 1.0, 2.20, 11.7, [
    {"title": "Lock the baseline", "body": "nightly feed live, definitions agreed with finance before anything is scored.", "stat": "day 10", "accent": BLUE2},
    {"title": "Stand up the door", "body": "the front door answers on two intents, contained end to end.", "stat": "day 30", "accent": BLUE},
    {"title": "Read the pilot", "body": "two use cases scored against exit criteria fixed on day one.", "stat": "day 45", "accent": BLUE},
    {"title": "Price wave one", "body": "rates anchored to the client's own feed, not benchmarks.", "stat": "day 60", "accent": BLUE3},
    {"title": "Clear the data gap", "body": "consent scope for transaction signals is the one open dependency.", "stat": "owner: client data office", "accent": CORAL},
    {"title": "Decide at ninety", "body": "go or no-go at the gate, with the criteria already signed.", "stat": "day 90", "accent": BLUE2},
], cols=3, h=1.52)
d.footnote(s, "Dates from kickoff; the coral tile is the single dependency the client owns. Illustrative example data.")
d.notes(s, "TILE GRID. Uniform tiles, accent top bars carry meaning (coral = the dependency). Whitespace law: tiles never stretch to fill.")

# ---------------- S5 AGENDA TRACKER RAIL (T36) ----------------
s = d.slide()
d.chrome(s, "This session · where we are", "Capability read is done, and pricing is the next gate")
d.agenda_rail(s, 1.0, 2.35, 6.2, [
    "The market picture, and where the pools sit",
    "Capability read: what runs out of the box",
    "Pricing wave one from your own volumes",
    "The pilot plan and its exit criteria",
    "Conditions, owners, dates",
], active=3)
d.ring_stat(s, 8.30, 2.50, 0.90, "6 of 8", "capabilities confirmed out of the box in the read")
d.ring_stat(s, 10.60, 2.50, 0.90, "2", "gaps carried into the pricing conversation")
d.implication_card(s, 8.05, 4.10, 4.63, 1.55,
    "The read held: most of the scope runs as shipped. The two gaps move into "
    "pricing as scope choices, not surprises, and the pilot plan absorbs both.")
d.footnote(s, "Tracker re-shown at each chapter; capability read as scored in session two. Illustrative example data.")
d.notes(s, "AGENDA RAIL, the serial-tracker device: same slide at every chapter, the light moves. Rings carry the running score.")

# ---------------- S6 RAG COVERAGE MATRIX (T38) ----------------
s = d.slide()
d.chrome(s, "Capability read · the coverage board", "Coverage: two gaps stand between the scope and wave one")
d.tag_chip(s, "Illustrative")
d.rag_matrix(s, 1.0, 2.25, 11.7,
             ["Digital onboarding", "Payments and transfers", "Conversational front door",
              "Card lifecycle", "Collections outreach", "Partner data feeds"],
             ["Out of the box", "Configuration", "Custom build", "Wave"],
             [[('g', "ships"), ('g', "flows"), ('n', ""), ('g', "wave 1")],
              [('g', "ships"), ('g', "limits"), ('n', ""), ('g', "wave 1")],
              [('g', "ships"), ('g', "intents"), ('p', "voice pack"), ('g', "wave 1")],
              [('g', "ships"), ('p', "issuer link"), ('n', ""), ('p', "wave 2")],
              [('p', "partial"), ('p', "sequences"), ('r', "dialer link"), ('r', "gap")],
              [('p', "partial"), ('n', ""), ('r', "consent API"), ('r', "gap")]],
             row_h=0.46)
d.footnote(s, "Read against the shipped platform, September 2026; the two coral rows are scope decisions for pricing. Illustrative example data.")
d.notes(s, "RAG COVERAGE MATRIX. Blue = shipped, light = configuration, coral = the honest gaps; legend always on. DEFENSE: read done against the live platform, not a datasheet.")

d.save(OUT)
print(f"Wrote {OUT} ({len(d.prs.slides._sldIdLst)} slides)")
