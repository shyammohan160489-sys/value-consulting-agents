#!/usr/bin/env python3
"""The Apex STAGE scale, side by side with the report scale: the same five pages built twice, so the
trade-off is visible (bigger type, fewer rows per page). Stage is the summit-deck scale Shyam chose
on 25 Sep 2026 (32pt titles, 12pt kicker, 12 to 13pt body, 15pt statement, 12pt footnote, navy
secondary text, the navy rule above the footer). Client-safe, unnamed bank.
Run: python3 example_apex_stage_build.py [out.pptx]"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import exhibit_pptx as X

OUT = sys.argv[1] if len(sys.argv) > 1 else "example_apex_stage.pptx"


def build(d, tag):
    P = d.pal
    NAVY, BLUE, BLUE3, BLUE4, TINT, TINT2, GREY, MUT = P.NAVY, P.BLUE, P.BLUE3, P.BLUE4, P.TINT, P.TINT2, P.GREY, P.MUT
    f = d.tf

    # 1 · ranked bars: five rows at stage, eight at report
    s = d.slide()
    d.chrome(s, "03 · The business case · %s scale" % tag, "Five intents carry two thirds of the cost today")
    rows = [("IN-16 · The unauthenticated front door", 2.8, "$2.8M", BLUE), ("OB-02 · Right-party reach and warm-up", 1.8, "$1.8M", NAVY),
            ("IN-17 · Transfers that arrive with context", 1.05, "$1.05M", BLUE), ("OB-04 · Post-sale fulfilment assistant", 1.0, "$1.0M", NAVY),
            ("IN-01 · Debit order reversal, end to end", 0.99, "$0.99M", BLUE)]
    if d.scale == 'report':
        rows += [("IN-02 · Merchant confusion", 0.77, "$0.77M", BLUE), ("OB-03 · Notification-grade campaign calls", 0.76, "$0.76M", NAVY),
                 ("OB-01 · Verified outbound", 0.72, "$0.72M", NAVY)]
    y = d.hbar_rows(s, 1.00, 2.30 if d.scale == 'report' else 2.45, 11.60, rows)
    d.legend(s, 1.00, min(y + 0.25, 6.2), [(BLUE, "inbound · first reception"), (NAVY, "outbound · warm-up and process assistant")],
             note="Released a year at full run, our estimate")
    d.footnote(s, "Cost from minutes × a loaded banker hour; released = cost × the take rate per intent. Bank-stated volumes, September 2026.")

    # 2 · the eight-number floor: four numbers at stage, eight at report
    s = d.slide()
    d.chrome(s, "01 · What we found · %s scale" % tag, "The floor, in the numbers the bank gave us")
    cells = [dict(number="~2,000", caption="bankers who serve and sell, one leader per 15", icon=X.icon("users")),
             dict(number="800K", caption="inbound calls answered a month, 9.6M a year", icon=X.icon("phone_incoming")),
             dict(number="6 min", caption="the average call; 20% under a minute, 20% over twenty", icon=X.icon("headset")),
             dict(number="98% → 20%", caption="service level, a normal day to month-end", dark=True, num_size=25.5, icon=X.icon("brightness"))]
    if d.scale == 'report':
        cells += [dict(number="1.2M", caption="outbound attempts a month; three in ten reach the right person", icon=X.icon("route")),
                  dict(number="19%", caption="of calls transferred, so the caller repeats the story", icon=X.icon("person")),
                  dict(number="30%", caption="of contacts never logged as a case", dark=True, icon=X.icon("document")),
                  dict(number="95%", caption="agree to apply once an offer is presented", icon=X.icon("check"))]
        d.stat_grid(s, 1.00, 1.73, cells)
    else:
        d.stat_grid(s, 1.00, 2.25, cells, cols=4, w=2.73, h=3.10)
    d.footnote(s, "Sources: the bank's workforce-lead sessions and its contact-centre console, September 2026. All bank-stated, to be confirmed by the data drop.")

    # 3 · two options
    s = d.slide()
    d.chrome(s, "05 · Commercials · %s scale" % tag, "Two options, one meter")
    h = 3.2 if d.scale == 'stage' else 2.9
    d.option_card(s, 1.00, 2.35, 5.72, h, "Option A", "Committed coverage", "Platform + units on the ladder; three years; two-way review at the floor.",
                  [("year one", "$2.05M"), ("three years", "$7.2M")], kind="dark", badge="recommended")
    d.option_card(s, 6.98, 2.35, 5.72, h, "Option B", "Pay as you go", "Same meter, $0.75 a unit; no ladder, no rollover, no re-base.",
                  [("year one", "$2.37M"), ("three years", "$9.2M")], kind="faint")
    d.statement_line(s, 1.00, 2.35 + h + 0.25, 11.7, "The only difference is the price of certainty:", "the units are the same, the meter is the same.")
    d.footnote(s, "Plan-floor volumes. Compute at cost on the bank's own cloud in both options; the implementation is one-off in year one.")

    # 4 · what moved it (the summit ledger, native to stage)
    s = d.slide()
    d.chrome(s, "The practitioner's view · %s scale" % tag, "Where the needle moved, and what it took")
    d.proof_ledger(s, 0.98, 2.43, 8.19, [
        ("Retail concierge", "South Africa · 3 yrs · 14.1M requests", 88.6, "88.6%", "Six domains. Two-layer stack."),
        ("Retail engagement", "South Africa · 5 yrs · 26.4M requests", 80, "~80%", "About 60% of requests after hours."),
        ("Business banking", "North America · 1 qtr · 29.7K requests", 74.0, "74.0%", "Payments a quarter of intents."),
        ("Wealth and advice", "Australia · 6 mo · 127.8K requests", 67.9, "67.9%", "Advisers and investors, one assistant."),
        ("Voice collections", "United States · 3 deployments · 30.7K calls", 55.6, "55.6%", "$1.3M+ banked in the call.", NAVY)])
    d.hero_column(s, 10.14, 2.43, "76%", "tool-call rate at an agentic deployment, 29 days in",
                  "Resolution stops near 80%. The next number comes from actions: tool calls, payments in the call, leads.")
    d.footnote(s, "Backbase production data, July 2026. Banks anonymised. Periods differ, so read as directional.")

    # 5 · a walk
    s = d.slide()
    d.chrome(s, "03 · The business case · %s scale" % tag, "How the running cost falls: from 44 to 18 cents a finished call")
    d.bars(s, 1.00, 2.45, 7.0, 3.3 if d.scale == 'stage' else 2.8, [
        ("Today · reference", 0.44, "$0.44", None, BLUE4), ("Year 1 · router", 0.25, "$0.25", "−43%", BLUE3),
        ("Year 2 · small models", 0.18, "$0.18", "−57%", BLUE), ("Year 3 · small tier on writes", 0.10, "$0.10", "−77%", BLUE)], dashed=(3,))
    d.kpi_stack(s, 8.90, 2.45, 3.80, [("Compute, at cost", "44c → 18c", "on the bank's own cloud key, never marked up"),
                                      ("Our fee", "unchanged", "the same in every state; only finished work bills")])
    d.footnote(s, "Today's profile is the committed compute basis; the router and small-model states are applied to that line. The dashed bar is the state not yet certified.")


d = X.ExhibitDeck(look='apex', scale='stage')
build(d, "stage")
d.save(OUT)
print("saved", OUT, "slides:", d.page, "scale stage")
r = X.ExhibitDeck(look='apex', scale='report')
build(r, "report")
rout = OUT.replace(".pptx", "_report.pptx")
r.save(rout)
print("saved", rout, "slides:", r.page, "scale report")
