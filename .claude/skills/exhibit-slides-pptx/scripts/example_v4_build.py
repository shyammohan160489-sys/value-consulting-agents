#!/usr/bin/env python3
"""Example v4 deck: four pages of the 18 Sep 2026 Nedbank ENBI Voice VC report rebuilt with the
v4 helpers (the Claude Design look), for a side-by-side check against the reference export.
Pages: the eight-number floor (ref slide 6), the architecture grid with lanes and count badges
(ref slide 15), the three states (ref slide 31), the mutual-plan timeline with who-signs chips
(ref slide 61). Copy from the reference is kept so the render can be compared line for line;
the client name in the plan's lane is neutralised. The client logo is a placeholder PNG drawn
next to the output (never a real client asset). Run:

    python3 example_v4_build.py [out.pptx] [--logo path.png]
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import exhibit_pptx as X
from pptx.enum.text import PP_ALIGN

args = [a for a in sys.argv[1:] if not a.startswith("--")]
OUT = args[0] if args else "example_v4_deck.pptx"
LOGO = None
if "--logo" in sys.argv:
    LOGO = sys.argv[sys.argv.index("--logo") + 1]


def make_placeholder_logo(path):
    """A neutral 354 x 354 placeholder mark (a teal disc with a white notch), never a real logo."""
    try:
        from PIL import Image, ImageDraw
    except ImportError:
        return None
    im = Image.new("RGBA", (354, 354), (0, 0, 0, 0))
    dr = ImageDraw.Draw(im)
    dr.ellipse((22, 22, 332, 332), fill=(0, 110, 96, 255))
    dr.rectangle((150, 96, 204, 258), fill=(255, 255, 255, 255))
    dr.rectangle((96, 150, 258, 204), fill=(255, 255, 255, 255))
    im.save(path)
    return path


if not LOGO:
    LOGO = make_placeholder_logo(os.path.join(os.path.dirname(os.path.abspath(OUT)) or ".",
                                              "placeholder_client_logo.png"))

# The v4 look: v4 palette, three-rule frame, 9pt navy kicker, 28pt regular title, client logo.
d = X.ExhibitDeck(look='v4', client_logo=LOGO)
NAVY, BLUE, BLUE3, BLUE4, TINT, TINT2, GREY, HAIR, MUT, FN, WHITE = (
    d.pal.NAVY, d.pal.BLUE, d.pal.BLUE3, d.pal.BLUE4, d.pal.TINT, d.pal.TINT2, d.pal.GREY,
    d.pal.HAIR, d.pal.MUT, d.pal.FN, d.pal.WHITE)

# ---------------- P1 · THE FLOOR, IN EIGHT NUMBERS (ref slide 6: stat_grid) ----------------
s = d.slide()
d.chrome(s, "01 · What we found", "The floor, in eight numbers")
d.stat_grid(s, 1.00, 1.73, [
    dict(number="~2,000", caption="bankers who serve and sell, one leader per 15"),
    dict(number="800K", caption="inbound calls answered a month, 9.6M a year"),
    dict(number="1.2M", caption="outbound attempts a month, the committed basis; three in ten reach the right person"),
    dict(number="6 min", caption="the average call; 20% under a minute, 20% over twenty"),
    dict(number="98% → 20%", caption="service level, a normal day to month-end", dark=True, num_size=25.5),
    dict(number="19%", caption="of calls transferred, so the caller repeats the story"),
    dict(number="30%", caption="of contacts never logged as a case", dark=True),
    dict(number="95%", caption="agree to apply once an offer is presented"),
])
d.footnote(s, "Sources: your workforce-lead sessions on 31 August, 8 and 11 September, and the CXone console on 8 September. "
              "All bank-stated, to be confirmed by the data drop. The case runs on 1.2M attempts a month; the console read 1.4M.",
           y=6.50, size=7.5, color=NAVY)
d.notes(s, "Eight numbers, all the bank's own. Two dark blocks carry the tension numbers.")

# ---------------- P2 · THE ARCHITECTURE (ref slide 15: lane_grid + weight_legend) ----------------
s = d.slide()
d.chrome(s, "02 · The solution", "The architecture: built once, used by all 22 intents")
C = lambda title, sub=None, count=None, span=1: dict(title=title, sub=sub, count=count, span=span)
d.lane_grid(s, 1.00, 2.12, [
    dict(label="Channels", sub="same brain", cards=[
        C("Voice · CXone", "SIP · Azure Speech SA", 22),
        C("Enbi chat", "same brain · today's chat channel, outside this scope", 22),
        C("SMS rail", "references, proofs, reminders", 5),
        C("WhatsApp", "With Digi 2.0", 0)]),
    dict(label="Orchestration", sub="one for every story", cards=[
        C("Enbi Voice · orchestrator", "language · intent · route · one record", 22, span=2),
        C("Compliance checker", "checks after every conversation", 22, span=2)]),
    dict(label="Agents", sub="by lane", cards=[
        C("Front door", "IN-16 · IN-11 · IN-12 · IN-13", 4),
        C("Transact", "IN-01…06 · IN-08 · IN-10", 8),
        C("Protect", "IN-09 · IN-07 · IN-15", 3),
        C("Warm-up", "OB-01 · OB-02 · OB-03", 3),
        C("Process assistant", "OB-04", 1),
        C("Lead engine", "OB-05", 1)]),
    dict(label="Shared fragments", sub="built once", cards=[
        C("Identity ladder", "voice-bio → app → questions", 15, span=2),
        C("Outcome written to the case", "on-call · referred · repeat", 17, span=2),
        C("Handover with the thread", "identity · intent · summary · sentiment", 16, span=2)]),
    dict(label="Your systems", sub="read · write · verify", unit_w=1.20, h=0.50, gap=0.10, cols=8, cards=[
        C("D365 · case", count=17), C("CXone identity", count=16), C("CXone handoff", count=16),
        C("Voice biometrics", count=15), C("Money app", count=15), C("Security questions", count=14),
        C("Core banking API", count=8), C("Card system", count=6),
        C("SMS rail", count=5), C("D365 campaigns", count=5), C("Knowledge hub", count=3),
        C("Core bank write · P2", count=2), C("WFM calendar", count=2), C("Dora", count=1),
        C("Digital identity", count=1), C("Web/app events", count=1)]),
])
d.weight_legend(s, 1.00, 6.40, [('faint', "1 or 2 intents"), ('light', "3 to 8"), ('mid', "9 to 16"),
                                ('dark', "17 to 22, all of them")],
                note="Number = how many of the 22 intents use the box")
d.notes(s, "Built once, reused by all 22 intents. The count on every box is the weight: navy for the boxes every intent uses.")

# ---------------- P3 · THREE STATES (ref slide 31: panel + mini_stat + a drawn bar) ----------------
s = d.slide()
d.chrome(s, "03 · The business case", "Three states · today, with the router, with small models")
STATES = [
    dict(label="Today · as solutioned", sub="every turn on a frontier model, on your Azure",
         body="Fixed replies, lookups, how-to and write paths all on gpt-5.4; cascaded speech in South Africa",
         price=0.29, disp="$0.29", bar=GREY, accent=False,
         stats=[("A year, full run", "$1.86M", None), ("Tokens / finished", "60K", None)],
         floor=("Plan floor, year one", "$0.70M", "· 44 cents a finished call")),
    dict(label="Next · the smart router", sub="product target; write paths stay on the frontier model",
         body="Fixed replies, lookups and how-to on a small model; write paths and the hardest turns stay on the frontier tier",
         price=0.17, disp="$0.17", bar=BLUE3, accent=True,
         stats=[("A year, full run", "$1.07M", "−43%"), ("Tokens / finished", "60K · half the price per token", None)],
         floor=("Plan floor, year one", "$0.40M", "· 25 cents a finished call")),
    dict(label="Beyond · small models", sub="serving paths: cache, templates, pre-rendered audio, a small RAG model",
         body="Fixed replies and lookups need no model; how-to from a cache or a small RAG model; write paths held until a small model qualifies",
         price=0.12, disp="$0.12", bar=BLUE, accent=True,
         stats=[("A year, full run", "$0.79M", "−57%"), ("Tokens / finished", "30K", None)],
         floor=("Plan floor, year one", "$0.30M", "· 19 cents a finished call")),
]
for i, st in enumerate(STATES):
    x, y = 1.00 + i * 3.86, 1.69
    ix = x + 0.21
    d.panel(s, x, y, 3.63, 4.38)
    d.txt(s, ix, y + 0.19, 3.3, 0.18, st["label"].upper(), size=7.9, color=(BLUE if st["accent"] else NAVY), track="20")
    sub_lines = d._est_lines(st["sub"], 3.31, 8.25)
    d.txt(s, ix, y + 0.35, 3.31, 0.20 * sub_lines, st["sub"], size=8.25, color=NAVY, line_sp=1.05)
    shift = 0.16 * (sub_lines - 1)
    d.txt(s, ix, y + 0.63 + shift, 3.31, 0.58, st["body"], size=9, color=NAVY, line_sp=1.1)
    base = y + 2.86 + shift                       # the rule the bar stands on
    bh = st["price"] * 4.66                       # 4.66 in per dollar, as measured
    d.rect(s, ix, base - bh, 0.94, bh, fill=st["bar"])
    d.rect(s, ix, base, 3.21, 0.01, fill=HAIR)
    d.txt(s, ix + 1.08, base - 0.83, 1.6, 0.50, st["disp"], size=33, color=(BLUE if st["accent"] else NAVY), wrap=False)
    d.txt(s, ix + 1.08, base - 0.33, 1.39, 0.31, "per finished conversation, handovers included", size=7.9, color=NAVY, line_sp=1.05)
    sy = base + 0.14
    tall = False
    for k, (lab, val, suf) in enumerate(st["stats"]):
        d.mini_stat(s, ix + k * 1.66, sy, 1.71, lab, val, suffix=suf, suffix_color=BLUE)
        tall = tall or d._est_lines(val, 1.64, 13.5) > 1
    ry = sy + 0.47 + (0.21 if tall else 0.0)
    d.rect(s, ix, ry, 3.21, 0.01, fill=HAIR)
    fl, fv, fs = st["floor"]
    d.mini_stat(s, ix, ry + 0.11, 3.54, fl, fv, suffix=fs, suffix_color=NAVY)
d.footnote(s, "Inbound $0.29 → $0.15 → $0.11 a finished conversation; outbound $0.29 → $0.19 → $0.15, where the saving is mostly on speech synthesis. "
              "If the small tier proves itself on write paths: $0.07. Today is our compute model for a finished conversation (page 28). The next two states apply the router's "
              "measured route economics as ratios, with three cautious assumptions: write paths stay on the frontier model, the router's banking complexity split applies, "
              "no cache credit until reuse is measured on voice. Speech at Azure list prices in South Africa; carrier, hosting and post-processing excluded. "
              "Every state is validated on your transcripts before it is committed.", y=6.25, size=7.5, color=NAVY)
d.notes(s, "Three states of the running cost. The bar height is the price; the number sits beside it; the floor line closes each panel.")

# ---------------- P4 · THE MUTUAL PLAN (ref slide 61: timeline_lanes + who_signs) ----------------
s = d.slide()
d.chrome(s, "Your turn · the mutual plan", "From today to go-live: the plan we run together")
NODES = [
    dict(date="Today · 18 Sep", title="The plan, agreed", kind='start', bold=True, texts=[
        "Agree the steps and the dates. Name the signing path: sponsor, budget holder, procurement, risk. Confirm next week's session.",
        "This deck today. A one-page summary for the people who were not in the room, by Monday."]),
    dict(date="Week of 21 Sep", title="The executive session", texts=[
        "The executive sponsor and the budget holder in the room, with the questions they need answered.",
        "The demo on your intents, the case on one page, and the decisions listed for October."]),
    dict(date="By 30 Sep", title="Your calls, by intent", texts=[
        "Recordings or transcripts, around fifty for each of the 22 intents, inbound and outbound, with the call reason and the outcome.",
        "Replayed through the router in shadow mode: which turns route where, on your calls. Measured, in the October proposal."]),
    dict(date="October", title="Proposal and decisions", texts=[
        "Decisions before signature: build window, quarter-unit, speech, identity, intent baseline, Enbi for staff, languages. Owners for CXone, Foundry, Digi 2.0.",
        "The revised proposal: the meter, the whole bill, the routing measured on your calls, the model options (page 48)."]),
    dict(date="November", title="The voice order", texts=[
        "Commercial approval, procurement and legal. The order signed.",
        "Contract and order form. The build team named and the kick-off dated."]),
    dict(date="Dec to Apr", title="The build, once", kind='future', texts=[
        "The SIP bridge from CXone, the Foundry key and models, the rails for the first intents, sign-off on recording and consent.",
        "The voice path, the intents on today's rails, the handover with the thread. Every state validated on your transcripts."]),
    dict(date="May 2027", title="Go-live", kind='end', texts=[
        "Year one and the meter start. The first monthly read, together.",
        "Live on the first rails. The router states as they qualify, each validated before it is committed."]),
]
y_end = d.timeline_lanes(s, 1.00, 2.00, 11.60, NODES, [("Client", "what you own"), ("Backbase", "what we own")], committed=4)
d.who_signs(s, 1.00, y_end + 0.10, 11.60,
            ["Executive sponsor", "Budget holder", "Procurement", "Risk and compliance",
             "Architecture and the AI CoE", "Contact centre operations"],
            desc="The signature runs through people who are not here today. Tell us who, and we prepare the session for them.")
d.footnote(s, "May 2027 holds if the order is signed in November. This plan is a shared page, one owner on each side, updated after every session; the routing measured "
              "on your calls and the model options land in the October proposal. No finance extract is asked for: the case runs on benchmarks and the numbers you gave in the room.",
           y=6.48)
d.notes(s, "The plan we ask the client to carry: who signs, next week's session, the transcripts by intent.")

d.save(OUT)
print("saved", OUT, "slides:", d.page, "logo:", LOGO)
