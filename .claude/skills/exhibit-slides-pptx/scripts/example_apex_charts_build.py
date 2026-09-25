#!/usr/bin/env python3
"""The Apex chart sampler: every chart recipe of the Apex look, each page a line-for-line rebuild of
a measured page from the 22 Sep 2026 conversational-banking report (page numbers in the kickers) or
the McKinsey summit deck (team page, close), so a render sits next to its reference for QA.
Client-safe: the bank and the assistant are unnamed; figures are the report's shapes, not a quote.
Run: python3 example_apex_charts_build.py [out.pptx] [--photos DIR]
     --photos DIR uses DIR/1.*, 2.*, 3.* for the team page (else initials tiles)."""
import os, sys, glob
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import exhibit_pptx as X
from pptx.enum.text import PP_ALIGN

args = [a for a in sys.argv[1:] if not a.startswith("--")]
OUT = args[0] if args else "example_apex_charts.pptx"
PHOTOS = None
if "--photos" in sys.argv:
    PHOTOS = sys.argv[sys.argv.index("--photos") + 1]

d = X.ExhibitDeck(look='apex')
P = d.pal
NAVY, BLUE, BLUE3, BLUE4, TINT, TINT2, GREY, CYAN, CORAL, MUT, FN, HAIR, HAIR_ROW, CARD_LINE, LINE_SOFT, DASHC, SUB_D, WHITE = (
    P.NAVY, P.BLUE, P.BLUE3, P.BLUE4, P.TINT, P.TINT2, P.GREY, P.CYAN, P.CORAL, P.MUT, P.FN, P.HAIR, P.HAIR_ROW,
    P.CARD_LINE, P.LINE_SOFT, P.DASHC, P.SUB_D, P.WHITE)


def label(s, x, y, w, text, color=None):
    d.txt(s, x, y, w, 0.19, text.upper(), size=8.5, color=(color or MUT), track="40", wrap=False)


# ---------------- 1 · ranked horizontal bars (report page 25)
s = d.slide()
d.chrome(s, "03 · The business case · page 25", "The eight intents that carry three quarters of it")
d.hbar_rows(s, 1.00, 2.30, 11.60, [
    ("IN-16 · The unauthenticated front door: education, info, how-to", 2.8, "$2.8M", BLUE),
    ("OB-02 · Right-party reach, warm-up and booking", 1.8, "$1.8M", NAVY),
    ("IN-17 · Transfers that arrive with context", 1.05, "$1.05M", BLUE),
    ("OB-04 · Post-sale fulfilment assistant", 1.0, "$1.0M", NAVY),
    ("IN-01 · Debit order reversal, end to end", 0.99, "$0.99M", BLUE),
    ("IN-02 · \"I don't know this transaction\": merchant confusion", 0.77, "$0.77M", BLUE),
    ("OB-03 · Notification-grade campaign calls", 0.76, "$0.76M", NAVY),
    ("OB-01 · \"It's really the bank\": verified outbound", 0.72, "$0.72M", NAVY)])
d.legend(s, 1.00, 6.25, [(BLUE, "inbound · first reception"), (NAVY, "outbound · warm-up and process assistant")],
         note="Released a year at full run, our estimate; the other 14 intents carry the remaining quarter")
d.notes(s, "T56 hbar_rows: page 25 rebuilt. Ranked bars, blue inbound, navy outbound, value after the bar, legend row.")

# ---------------- 2 · stacked horizontal rows (report page 12)
s = d.slide()
d.chrome(s, "01 · What we found · page 12", "What a call costs today: the top inbound intents, by the minute")
rows = [
    dict(label="IN-16 · Front door: how-to, info", sub="disposition; a third never logged", vol="200K", vol_sub="a month",
         segments=[(2.5, NAVY), (1.0, BLUE)], end="3.5 min", right="$1.78"),
    dict(label="IN-17 · Transfers", sub="the receiver re-logs the case", vol="165K", vol_sub="a month",
         segments=[(1.5, NAVY), (1.0, BLUE)], end="2.5 min", right="$1.32"),
    dict(label="IN-02 · Merchant confusion", sub="case, fraud-fear note, service request", vol="29K", vol_sub="a month",
         segments=[(5.0, NAVY), (2.0, BLUE)], end="7 min", right="$3.37"),
    dict(label="IN-01 · Debit order reversal", sub="case lock, back-office steps, notes; back-office minutes", vol="26K", vol_sub="a month",
         segments=[(6.0, NAVY), (3.0, BLUE), (0.5, BLUE3)], end="9.5 min", right="$4.51"),
    dict(label="IN-03 · Balance, and the question behind it", sub="case lock only", vol="25K", vol_sub="a month",
         segments=[(4.0, NAVY), (1.0, BLUE)], end="5 min", right="$2.46"),
    dict(label="IN-04 · Payment confirmations", sub="case, proof sent", vol="18K", vol_sub="a month",
         segments=[(4.0, NAVY), (1.5, BLUE)], end="5.5 min", right="$2.69"),
    dict(label="IN-09 · Fraud triage and card block", sub="block, evidence, case, fraud-desk handover", vol="10K", vol_sub="a month",
         segments=[(6.0, NAVY), (4.5, BLUE)], end="10.5 min", right="$4.97")]
d.hstack_rows(s, 1.00, 2.22, 11.60, rows, scale=0.50)
d.legend(s, 1.00, 6.33, [(NAVY, "talk time, our estimate by intent"), (BLUE, "after-call work, ours"), (BLUE3, "downstream human minutes")],
         note="$ per call at $27 an agent-hour, talk and after-call only")
d.notes(s, "T57 hstack_rows: page 12 rebuilt. Label and sub, volume column, stacked minutes at 0.5 in a minute, end label, dollar value right.")

# ---------------- 3 · paired horizontal rows (report page 24)
s = d.slide()
d.chrome(s, "03 · The business case · page 24", "22 intents: what they cost today and what the assistant releases")
d.paired_hrows(s, 1.00, 2.35, 11.60, [
    ("US3 · First reception", "17 intents · 581K calls a month", 15.0, "$15.0M today", 9.1, "$9.1M released"),
    ("US1 · Leads warm-up", "3 intents · 328K attempts a month", 6.3, "$6.3M today", 3.3, "$3.3M released"),
    ("US2 · Process assistant", "1 intent · 27K applications a month", 2.0, "$2.0M today", 1.0, "$1.0M released · your own target since 2024")])
d.rect(s, 1.00, 5.30, 11.60, 0.01, fill=CARD_LINE)
for x, num, cap, col in ((1.00, "$23.3M", "cost today, 22 intents, a year", NAVY), (3.30, "$13.4M", "released a year at full run", BLUE),
                         (5.40, "$11.6M", "of it from go-live, on rails that exist today", BLUE)):
    d.txt(s, x, 5.45, 2.2, 0.31, num, size=19, color=col, wrap=False)
    d.txt(s, x, 5.89, 2.2, 0.42, cap, size=9.5, color=NAVY, line_sp=1.1)
d.txt(s, 8.20, 5.50, 4.50, 0.62, "Our estimate at $27 an agent-hour, talk and after-call minutes only; downstream minutes and the outbound miss rate are on top.", size=9, color=MUT, line_sp=1.12)
d.notes(s, "T58 paired_hrows: page 24 rebuilt. Reference bar in tint, the released share in blue under it, the three totals on a rule.")

# ---------------- 4 · funnel rows + hero blocks (report page 37)
s = d.slide()
d.chrome(s, "03 · The business case · revenue view · page 37", "More people hear the offer: what it is worth on your funnel")
d.funnel_rows(s, 1.00, 1.77, 7.5, [
    ("Leads worked", "your campaign book", 3.0, "3.0M", 3.0, "3.0M", "—"),
    ("Right party reached", "49.8% → 55% when the caller is known", 1.49, "1.49M", 1.65, "1.65M", "+156K"),
    ("Hear the offer", "31% → 36% with warm-up and a booked call", 0.463, "463K", 0.594, "594K", "+131K"),
    ("Agree to apply", "your 95%, unchanged", 0.440, "440K", 0.564, "564K", "+124K"),
    ("Booked", "half of agreed, our floor", 0.220, "220K", 0.282, "282K", "+62K")],
    headers=("Step, a year", "Today", "With the assistant", "Change"))
d.hero_number(s, 8.71, 1.73, 3.65, 1.28, "+62K", "more booked loans and cards a year, the same people, the same offer", dark=True, layout='stack')
d.hero_number(s, 8.71, 3.18, 3.65, 1.35, "$2.2M to $3.8M", "a year at full run, outside the cost case and on top of it", dark=False, layout='stack', num_size=22.5)
d.txt(s, 8.71, 4.69, 3.76, 0.59, "Every input is yours or deliberately low: the reach lift is the known-caller rate, the offer lift is warm-up, the floor is half of agreed.", size=9, color=MUT, line_sp=1.12)
d.footnote(s, "Bars to scale against 3.0M leads. The funnel is the bank's own campaign book for the year; lifts are the two stated points and nothing else.")
d.notes(s, "T59 funnel_rows: page 37 rebuilt. Thin grey and blue bars per step, the change column in blue, the two hero blocks right.")

# ---------------- 5 · columns in Apex weight, dashed estimate (report page 33)
s = d.slide()
d.chrome(s, "03 · The business case · page 33", "How the running cost falls: from 44 to 18 cents a finished call")
label(s, 1.00, 2.17, 4.5, "Per finished conversation on the plan floor, by state")
d.bars(s, 1.00, 2.42, 6.40, 2.65, [
    ("Today's profile · reference", 0.44, "$0.44", None, BLUE4),
    ("Year 1 · router from go-live", 0.25, "$0.25", "−43%", BLUE3),
    ("Year 2 · small models", 0.18, "$0.18", "−57%", BLUE),
    ("Year 3 · small tier on writes", 0.10, "$0.10", "−77%", BLUE)], dashed=(3,), badge=(3, "once certified"))
label(s, 7.90, 2.17, 2.0, "The levers, in order")
levers = [("Stable prompt and cache:", "from go-live, about a quarter of the model line"),
          ("The smart router, from go-live:", "fixed replies, lookups and how-to on a small model; write paths stay on the frontier model once it qualifies; hard turns stay on the frontier tier"),
          ("Serving paths and small models, year two:", "cache, templates, pre-rendered audio, a small RAG model"),
          ("Provider price cuts:", "pass through to you; prices are re-verified yearly"),
          ("Speech-to-speech:", "when it is ready, for latency and naturalness rather than cost")]
yy = 2.45
for lead, rest in levers:
    n = d._est_lines(lead + " " + rest, 4.84, 9.5)
    d.txt(s, 7.90, yy, 4.84, 0.22 * n, [[(lead + " ", 9.5, NAVY, False), (rest, 9.5, MUT, False)]], line_sp=1.1)
    yy += 0.22 * n + 0.12
label(s, 7.90, 4.77, 2.0, "Whose cost")
d.txt(s, 7.90, 5.00, 4.84, 0.62, "On your cloud, at cost: model tokens, speech, the router's classifier nodes, a hosted small model. Our fee is the same in every state.", size=9.5, color=NAVY, line_sp=1.12)
d.txt(s, 1.00, 5.48, 6.59, 0.79, "The plan-floor line by year: $0.40M in year one with the router against $0.70M on today's profile; $0.43M in year two with small models against $1.0M; $0.28M in year three of the committed case. Tokens per finished conversation 60K → 60K → 30K.", size=9.5, color=NAVY, line_sp=1.15)
d.footnote(s, "Today's profile is the committed compute basis on the commercial pages; the router and small-model states are applied to that line at the 22-intent mix. The dashed bar is the state not yet certified.")
d.notes(s, "T60 bars (Apex weight): page 33 rebuilt. 15pt values, muted deltas, the fourth bar dashed with its badge.")

# ---------------- 6 · the cost walk + component table (report page 55)
s = d.slide()
d.chrome(s, "06 · Your questions · differentiation · page 55", "Why the bill falls with us: eight components and what each does")
label(s, 1.00, 1.75, 4.58, "Per finished conversation · plan floor, year one")
d.column_walk(s, 1.00, 2.10, 4.17, 3.90, [
    dict(label="Today", value=44, display="44c", delta=19, delta_display="−19c", fill=NAVY, delta_fill=BLUE3),
    dict(label="Router", value=25, display="25c", delta=6, delta_display="−6c", fill=BLUE, delta_fill=BLUE3),
    dict(label="Serving paths", value=19, display="19c", delta=9, delta_display="−9c", fill=BLUE, delta_fill=BLUE3, delta_dashed=True),
    dict(label="Small tier on writes", value=10, display="10c", fill=BLUE, dashed=True)])
for x, w, t in ((5.75, 2.41, "Component"), (7.94, 1.72, "Status"), (9.50, 3.14, "What it does")):
    d.txt(s, x, 1.75, w, 0.18, t.upper(), size=7.9, color=NAVY, track="20", wrap=False)
comps = [("Stable prompt and caching", "live", "solid", "About a quarter off the model line, inside the 44c"),
         ("The smart router, sticky per-turn", "operational Q1 2027", "mid", "44 → 25c · writes held on the strong tier"),
         ("Serving paths: no generation, templates, pre-rendered audio", "in development, Q1 2027", "mid", "25 → 19c · speech falls too"),
         ("Semantic cache, answers reused", "provisioned, switched off", "dashed", "More, once measured on voice; no credit taken"),
         ("A banking small model on your data", "in development", "mid", "19 → 10c · writes on the small tier once certified"),
         ("Your own model through the router", "option", "dashed", "Your model, your price, the same telemetry"),
         ("Cross-session memory", "roadmap", "dashed", "Fewer re-discovery turns on repeat callers")]
yy = 1.99
for comp, status, kind, what in comps:
    d.rect(s, 5.62, yy, 6.73, 0.51, fill=TINT2)
    d.txt(s, 5.75, yy + 0.08, 2.27, 0.40, comp, size=9, color=NAVY, line_sp=1.05)
    cw = 0.22 + len(status) * 0.062
    if kind == "dashed":
        d.rect(s, 7.94, yy + 0.16, cw, 0.20, fill=WHITE, line=BLUE3, line_w=0.75, dash='dash')
    else:
        d.rect(s, 7.94, yy + 0.16, cw, 0.20, fill=(BLUE if kind == "solid" else BLUE3))
    d.txt(s, 8.02, yy + 0.19, cw, 0.18, status, size=7.9, color=(WHITE if kind == "solid" else NAVY), wrap=False)
    d.txt(s, 9.50, yy + 0.08, 2.81, 0.40, what, size=8.6, color=NAVY, line_sp=1.05)
    yy += 0.57
d.footnote(s, "The last step is dashed: it is the state that is not yet certified on your calls. Every other component carries a dated status word.")
d.notes(s, "T61 column_walk: page 55 rebuilt. Column pairs with the delta beside each step; the component table right with status chips.")

# ---------------- 7 · grouped stacked columns + KPI stack (report page 28)
s = d.slide()
d.chrome(s, "03 · The business case · page 28", "Three years: what you pay and what you get")
d.stacked_columns(s, 1.00, 2.20, 7.25, 3.30, [
    dict(label="Year 1", sub="from go-live · 50% coverage", columns=[
        dict(segments=[(2.05, TINT), (0.68, ('dashed', CARD_LINE, TINT2)), (0.30, ('dashed', BLUE))], total="$3.1M"),
        dict(segments=[(3.9, BLUE)], total="$3.9M"), dict(segments=[(6.3, NAVY)], total="$6.3M")]),
    dict(label="Year 2", sub="75% coverage", columns=[
        dict(segments=[(2.5, TINT), (1.0, ('dashed', CARD_LINE, TINT2))], total="$3.5M"),
        dict(segments=[(5.8, BLUE)], total="$5.8M"), dict(segments=[(9.5, NAVY)], total="$9.5M")]),
    dict(label="Year 3", sub="90% coverage", columns=[
        dict(segments=[(2.65, TINT), (1.15, ('dashed', CARD_LINE, TINT2))], total="$3.8M"),
        dict(segments=[(7.0, BLUE)], total="$7.0M"), dict(segments=[(11.4, NAVY)], total="$11.4M")])])
d.legend(s, 1.00, 6.02, [(TINT, "fee"), (('dashed', CARD_LINE), "compute at cost"), (('dashed', BLUE), "implementation, one-off"),
                        (BLUE, "at $2.40 a call"), (NAVY, "at $3.90 a call")])
d.kpi_stack(s, 8.90, 2.35, 3.80, [
    ("You pay", "$10.4M", "$7.2M to us, $2.9M of compute at cost, $0.3M of implementation"),
    ("You get", "$17M to $27M", "6.9M finished conversations at $2.40 to $3.90 a call"),
    ("Back per dollar", "1.6× to 2.6×", "38 to 62% of the value stays with the bank")])
d.footnote(s, "Option A at plan-floor volumes. Compute at cost on the bank's own cloud key; the implementation is one-off in year one. Value at the two readings of a call.")
d.notes(s, "T62 stacked_columns + T63 kpi_stack: page 28 rebuilt. Pay stacks in tints and dashed outlines, the two get columns solid, the KPI column right.")

# ---------------- 8 · stacked columns by year and state (report page 47)
s = d.slide()
d.chrome(s, "05 · Commercials · page 47", "How your bill travels: per finished conversation, by year and state")
def col(fee, comp, cfill, build=None, small=None, total=""):
    segs = [(fee, TINT), (comp, cfill)]
    if small: segs.append((small, ('dashed', NAVY)))
    if build: segs.append((build, ('dashed', BLUE)))
    return dict(segments=segs, total=total)
d.stacked_columns(s, 0.90, 2.40, 8.23, 3.35, [
    dict(label="Year 1", sub="50% coverage · from go-live", columns=[col(1.28, 0.44, BLUE4, build=0.20, total="$1.92"), col(1.28, 0.25, BLUE3, build=0.20, total="$1.73"), col(1.28, 0.19, BLUE, build=0.20, total="$1.67")]),
    dict(label="Year 2", sub="75% coverage", columns=[col(1.04, 0.42, BLUE4, total="$1.46"), col(1.04, 0.24, BLUE3, total="$1.28"), col(1.04, 0.18, BLUE, total="$1.22")]),
    dict(label="Year 3", sub="90% coverage · full run", columns=[col(0.90, 0.42, BLUE4, total="$1.14"), col(0.90, 0.24, BLUE3, total="$1.08"), col(0.90, 0.18, BLUE, small=0.10, total="$1.00")])],
    col_w=0.62, gap=0.10)
d.legend(s, 1.00, 6.22, [(TINT, "fee"), (BLUE4, "compute today"), (BLUE3, "with the router"), (BLUE, "with small models"),
                        (('dashed', BLUE), "build, once"), (('dashed', NAVY), "small tier on writes")], size=8)
d.kpi_stack(s, 9.55, 2.35, 3.20, [
    ("All in, a finished conversation", "$1.92 → $1.08", "over the term, with the router and small models as each is certified on your calls"),
    ("Our fee", "$1.28 → $0.90", "steps down with coverage: the ladder's three unit rates"),
    ("Compute, at cost", "44c → 18c", "on your own cloud key, never marked up")], val_size=19, pitch=1.39)
d.footnote(s, "Option A at plan-floor volumes: 1.6M finished conversations in year one, 6.9M over three. Build spread over year one; the small tier on writes dashed until certified.")
d.notes(s, "T62 stacked_columns by year and state: page 47 rebuilt. Three states per year, the build as a dashed cap, the KPI column right.")

# ---------------- 9 · share bar with values above (report page 46, left)
s = d.slide()
d.chrome(s, "05 · Commercials · page 46", "What a finished conversation costs you, all in, and how it travels")
label(s, 1.00, 1.69, 5.96, "Year one, per finished conversation", color=NAVY)
d.share_bar(s, 1.00, 1.97, 5.41, [(1.28, "$1.28", None, 'blue'), (0.44, "$0.44", None, 'mid'), (0.20, "$0.20", None, 'light')],
            h=0.35, val_size=9, total=("$1.92", "a finished conversation"), total_pos='below', label="All in, year one")
items = [(BLUE, "Our fee", "$1.28", "$775K platform and five connectors a year; units on the ladder, only finished conversations bill"),
         (BLUE3, "Compute at cost, on your key", "$0.44", "model tokens about $0.26, speech about $0.18, at list prices; 44c falls to 18c by design"),
         (TINT, "The build, one-off", "$0.20", "$318,500 spread over the first year's finished conversations")]
yy = 2.86
for fill, name, val, sub in items:
    d.rect(s, 1.00, yy, 5.42, 0.01, fill=LINE_SOFT)
    d.rect(s, 1.00, yy + 0.15, 0.12, 0.12, fill=fill)
    d.txt(s, 1.25, yy + 0.12, 4.4, 0.20, name, size=9.4, color=NAVY, wrap=False)
    d.txt(s, 5.80, yy + 0.12, 0.70, 0.23, val, size=11.25, color=NAVY, align=PP_ALIGN.RIGHT, wrap=False)
    d.txt(s, 1.25, yy + 0.35, 4.9, 0.34, sub, size=7.9, color=MUT, line_sp=1.1)
    yy += 0.67
d.txt(s, 1.00, 4.68, 5.58, 0.39, "Against $2.40 for the calls the assistant finishes, and $3.90 for the calls a banker takes today.", size=8.6, color=NAVY, line_sp=1.1)
label(s, 6.83, 1.69, 6.07, "How it travels: three years, three states, all in", color=NAVY)
d.stacked_columns(s, 6.94, 1.95, 5.40, 3.10, [
    dict(label="Year 1", columns=[dict(segments=[(1.28, BLUE), (0.44, GREY), (0.20, ('dashed', NAVY))], total="$1.92", sub="today"), dict(segments=[(1.28, BLUE), (0.25, BLUE3), (0.20, ('dashed', NAVY))], total="$1.73", sub="router"), dict(segments=[(1.28, BLUE), (0.19, NAVY), (0.20, ('dashed', NAVY))], total="$1.67", sub="small")]),
    dict(label="Year 2", columns=[dict(segments=[(1.04, BLUE), (0.42, GREY)], total="$1.46", sub="today"), dict(segments=[(1.04, BLUE), (0.24, BLUE3)], total="$1.28", sub="router"), dict(segments=[(1.04, BLUE), (0.18, NAVY)], total="$1.22", sub="small")]),
    dict(label="Year 3", columns=[dict(segments=[(0.90, BLUE), (0.42, GREY)], total="$1.14", sub="today"), dict(segments=[(0.90, BLUE), (0.24, BLUE3)], total="$1.08", sub="router"), dict(segments=[(0.90, BLUE), (0.18, NAVY)], total="$1.00", sub="small")])],
    col_w=0.46, gap=0.08, val_size=8.25, label_size=9)
d.legend(s, 6.83, 5.34, [(BLUE, "our fee"), (GREY, "compute, today's profile"), (BLUE3, "compute, router"), (NAVY, "compute, small models"), (('dashed', NAVY), "the build")], size=7.9, swatch=0.10)
d.footnote(s, "Option A at plan-floor volumes: the year-one unit of $1.92 falls to $1.08 in year three as the router and small models are certified; the build is spread over year one.")
d.notes(s, "T64 share_bar (values above, total) + small stacked_columns: page 46 rebuilt.")

# ---------------- 10 · area block (report page 8)
s = d.slide()
d.chrome(s, "01 · What we found · page 8", "Half your clients are not on the app; the phone reaches them")
label(s, 1.00, 2.17, 3.96, "Your clients, by the channel that reaches them")
d.area_block(s, 1.00, 2.80, 1.40, 2.50, [
    (0.56, TINT, "About 4M reached by phone, USSD or a branch", "30 to 40% have no app, for the device or the data; what the app would take, the phone takes"),
    (0.44, BLUE, "About 3.5M on the app", "digitally active; 393K app chats a month and rising")], top_label="7.5M to 8M clients")
d.txt(s, 1.00, 5.38, 5.46, 0.41, "800K inbound calls and 1.2M outbound attempts a month come from the whole base; the half without the app leans on the phone for everything routine.", size=9, color=NAVY, line_sp=1.12)
label(s, 7.00, 2.17, 5.7, "What the assistant changes for the half not on the app")
ry = 2.45
for lead, body in (("Served at the assistant's cost, not a banker's or a branch's", "The routine the app would take is taken on the call: balance, transfers, reversals, confirmations, in the caller's language."),
                   ("Enrolled on the call", "App access, activation and education become a conversation, with the reference sent by SMS."),
                   ("The offer heard, by the people the app cannot reach", "Warm-up and booking land where the campaign book lives: the phone.")):
    d.txt(s, 7.00, ry, 5.7, 0.21, lead, size=10.5, color=NAVY, wrap=False)
    d.txt(s, 7.00, ry + 0.30, 5.77, 0.62, body, size=9, color=MUT, line_sp=1.12)
    d.rect(s, 7.00, ry + 1.08, 5.60, 0.01, fill=HAIR_ROW)
    ry += 1.20
d.footnote(s, "Population as stated in the baseline sessions; the app share from the digital team's active-user count. Sizing the split of callers by app status is the first data ask.")
d.notes(s, "T65 area_block: page 8 rebuilt. A proportional block with the smaller part in blue, labels beside each part, the baseline under.")

# ---------------- 11 · donut and pie (no reference page; the requested form)
s = d.slide()
d.chrome(s, "The forms the report did not need", "Where the minutes of a call go, as a donut and as a pie")
label(s, 1.00, 2.05, 5.0, "Share of a six-minute call, a donut with the total in the hole")
d.donut(s, 1.00, 2.40, 3.20, [(0.55, NAVY, "Talk time", "55%"), (0.25, BLUE, "After-call work", "25%"), (0.20, BLUE3, "Downstream minutes", "20%")],
        center=("6 min", "the average call"), legend=True)
label(s, 7.30, 2.05, 5.0, "The same split as a pie, labels outside")
d.donut(s, 7.30, 2.40, 3.20, [(0.55, NAVY, "Talk time", "55%"), (0.25, BLUE, "After-call work", "25%"), (0.20, BLUE3, "Downstream minutes", "20%")],
        thickness=1.0, legend=True)
d.statement_line(s, 1.00, 5.85, 11.7, "Use a donut for one share of one whole.", "For a share across years or states, the share bar or the stacked columns read faster.")
d.footnote(s, "Illustrative split. The measured reports carried no pie; the form is here because it was asked for, in the same tokens and weight.")
d.notes(s, "T66 donut: block arcs clockwise from 12 o'clock; thickness=1.0 gives the pie. Legend to the right with swatch, label and share.")

# ---------------- 12 · the production runs (summit deck page 8)
s = d.slide()
d.chrome(s, "The practitioner's view · Backbase production deployments · summit page 8", "Where the needle moved, and what it took")
d.proof_ledger(s, 0.98, 2.43, 8.19, [
    ("Retail concierge", "South Africa · 3 yrs · 14.1M requests", 88.6, "88.6%", "Six domains. Two-layer stack."),
    ("Retail engagement", "South Africa · 5 yrs · 26.4M requests", 80, "~80%", "About 60% of requests after hours."),
    ("Business banking", "North America · 1 qtr · 29.7K requests", 74.0, "74.0%", "Payments a quarter of intents."),
    ("Wealth and advice", "Australia · 6 mo · 127.8K requests", 67.9, "67.9%", "Advisers and investors, one assistant."),
    ("Voice collections", "United States · 3 deployments · 30.7K calls", 55.6, "55.6%", "$1.3M+ banked in the call.", NAVY)])
d.hero_column(s, 10.14, 2.43, "76%", "tool-call rate at an agentic deployment, 29 days in",
              "Resolution stops near 80%. The next number comes from actions: tool calls, payments in the call, leads.")
d.footnote(s, "Backbase production data, July 2026. Banks anonymised. Periods differ, so read as directional. RESOLVED = resolved without a person.", size=12, y=6.62)
d.notes(s, "T68 proof_ledger + T70 hero_column: summit page 8 rebuilt. A resolution bar per deployment, the newest number as the hero.")

# ---------------- 13 · the value pools on the loop (summit deck page 9)
s = d.slide()
d.chrome(s, "The roll-up · where the work goes · summit page 9", "Impact follows where the work sits on the loop")
y_end = d.loop_matrix(s, 0.98, 2.26, 8.19,
    [("cost", "Cost to serve", "blue"), ("loyalty", "Loyalty and retention", "navy"), ("revenue", "Revenue", "tint"), ("risk", "Risk and conduct", "outline")],
    [dict(label="Out of the loop", desc="AI resolves inside policy, alone.",
          chips=[("Everyday servicing: cards, balances, resets", "cost"), ("After-hours and overflow", "cost"), ("Travel notices, limits, statements", "cost"), ("Proactive alerts that act", "loyalty")]),
     dict(label="On the loop", desc="AI acts; a person takes the exceptions.",
          chips=[("Disputes and fraud moments", "loyalty"), ("Address and mandate changes", "cost"), ("Collections and promise-to-pay", "revenue"), ("Onboarding and KYC refresh", "risk")]),
     dict(label="In the loop", desc="A person decides; AI prepares the file.",
          chips=[("Credit decisions, restructuring", "risk"), ("Sales moments, licensed advice", "revenue"), ("Complex complaints", "loyalty"), ("Morning handoffs, case prep", "cost")]),
     dict(label="Person only", desc="AI does not act; it clears the queue.",
          chips=[("Vulnerable customers", "risk"), ("Bereavement", "loyalty"), ("Escalated complaints", "risk")])])
d.statement_line(s, 0.98, y_end + 0.03, 8.0, "The decision is the row,", "not the bot.", size=15)
d.hero_column(s, 10.14, 2.26, "4 of 4", "rows have live examples on this continent today",
              "The prize is the top two rows. $1.4tn+ moved through mobile money in Africa last year (1).", num_size=55)
d.footnote(s, "Families from Backbase programmes, 2024 to 2026. Rows are design choices. 1 GSMA Mobile Money 2026, Sub-Saharan scope; the continent total is higher.", size=12, y=6.62)
d.notes(s, "T69 loop_matrix + T70 hero_column: summit page 9 rebuilt. Value pools as chips on the autonomy rows; the hero counts the rows with live examples.")

# ---------------- 12 · team page (summit deck page 10)
photos = [None, None, None]
if PHOTOS:
    for i in range(3):
        hit = sorted(glob.glob(os.path.join(PHOTOS, "%d.*" % (i + 1))))
        photos[i] = hit[0] if hit else None
d.team_page("Come say hello", [("The ", NAVY), ("Backbase", None), (" team with you today", NAVY)],
            [(photos[0], "Justin Arnoldi", "Director of Sales, EMEA"),
             (photos[1], "Byron Wolff", "Director of Customer Success, EMEA and APAC"),
             (photos[2], "Shyam Mohan", "Director of Strategy Consulting, EMEA and APAC")])
d.notes(d.prs.slides[-1], "T67 team_page: summit deck page 10. Photos fill the column between the rules; name and role beside each.")

# ---------------- 13 · the close (summit deck page 11)
d.closing_page("Thank you")

d.save(OUT)
print("saved", OUT, "slides:", d.page)
