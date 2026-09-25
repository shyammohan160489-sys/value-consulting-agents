#!/usr/bin/env python3
"""The framework sampler: twelve pages, one framework each, at the Apex stage scale, with Lucide icons
drawn as native shapes. The forms Shyam asked for after the BCG archive: flywheel, cascade, funnel, zoom
(one row of the value map opened up), value map, chevron flow, rings, stack (ziggurat), hub and spoke,
icon rows, venn, pillars. Client-safe conversational-banking content, the bank unnamed.
Run: python3 example_apex_frameworks_build.py [out.pptx]"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import exhibit_pptx as X

OUT = sys.argv[1] if len(sys.argv) > 1 else "example_apex_frameworks.pptx"
d = X.ExhibitDeck(look='apex')
P = d.pal
NAVY, BLUE, BLUE3, BLUE4, TINT, TINT2, MUT, WHITE = P.NAVY, P.BLUE, P.BLUE3, P.BLUE4, P.TINT, P.TINT2, P.MUT, P.WHITE

# 1 · flywheel
s = d.slide()
d.chrome(s, "The operating model · flywheel", "Every finished call pays for the next rail")
d.flywheel(s, 4.3, 4.35, 1.4, [
    ("More calls finished", "on the bank's own case states", "phone-call"),
    ("Fewer banker minutes", "released to advice and the close", "users"),
    ("More rails certified", "each write path validated once", "shield-check"),
    ("More intents in scope", "more of the call log", "list-checks"),
    ("Lower cost a call", "the router and small models", "trending-down"),
    ("More volume presented", "the bank chooses what to serve", "chart-column")],
    center=("One brain", "paid on finished work"), start=-60)
d.hero_number(s, 8.9, 2.6, 3.8, 1.45, "44c → 18c", "compute a finished conversation, three states, each certified on the bank's calls", dark=True, layout='stack', num_size=30)
d.txt(s, 8.9, 4.3, 3.8, 1.4, "The wheel turns once a quarter: the intents certified in one review widen the scope of the next, and the unit cost falls as the router learns the bank's mix.", size=11, color=NAVY, line_sp=1.15)
d.footnote(s, "The loop is the operating model of the conversational assistant; the numbers are the live fire's three states, September 2026.")

# 2 · cascade
s = d.slide()
d.chrome(s, "The business case · cascade", "Where the released value comes from")
d.cascade(s, 1.0, 2.2, 11.7, 3.9,
          dict(title="Released a year, full run", number="$13.4M", sub="of $23.3M the bank spends today on the 22 intents; capacity, in banker minutes"),
          [dict(title="First reception", number="$9.1M", sub="17 inbound intents", leaves=[("IN-16 · The unauthenticated front door", "$2.8M"), ("IN-17 · Transfers with context", "$1.05M"), ("IN-01 · Debit order reversal", "$0.99M"), ("IN-02 · Merchant confusion", "$0.77M")]),
           dict(title="Leads warm-up", number="$3.3M", sub="3 outbound intents", leaves=[("OB-02 · Right-party reach and booking", "$1.8M"), ("OB-03 · Campaign calls", "$0.76M"), ("OB-01 · Verified outbound", "$0.72M")]),
           dict(title="Process assistant", number="$1.0M", sub="1 intent", leaves=[("OB-04 · Post-sale fulfilment", "$1.0M")])])
d.footnote(s, "Cost from minutes × a loaded banker hour; released = cost × the take rate per intent. Bank-stated volumes, September 2026. Twelve smaller intents carry the rest.")

# 3 · funnel
s = d.slide()
d.chrome(s, "The revenue view · funnel", "From three million leads to 282 thousand booked")
d.funnel(s, 1.0, 2.15, 6.2, 3.95, [
    ("Leads worked", 3.0, "3.0M"), ("Right party reached", 1.65, "1.65M", "55%"),
    ("Hear the offer", 0.594, "594K", "36%"), ("Agree to apply", 0.564, "564K", "95%"), ("Booked", 0.282, "282K", "50%")])
d.icon_rows(s, 8.1, 2.2, 4.6, [
    ("phone-outgoing", "Reach lifts with a known caller", "49.8% to 55% when the assistant verifies before the banker dials."),
    ("message-square", "The offer is heard after warm-up", "31% to 36% with an SMS reference and a booked call."),
    ("check", "Nothing else moves", "Agree and book rates stay the bank's own; the floor is half of agreed.")], pitch=1.25)
d.footnote(s, "The bank's campaign book for the year; the two lifts are the stated points and nothing else. +62K booked a year, $2.2M to $3.8M at full run.")

# 4 · zoom
s = d.slide()
d.chrome(s, "The value map · one row opened", "First reception is the biggest row, and it is four intents")
box = d.zoom(s, 1.0, 2.2, 11.7, 3.8, [("US1 · Leads warm-up", "$3.3M"), ("US2 · Process assistant", "$1.0M"), ("US3 · First reception", "$9.1M"), ("US4 · Lead engine", "multiplies")], 2, title="First reception · the four intents")
d.icon_rows(s, box[0], box[1], box[2], [
    ("help-circle", "The front door", "Education, info and how-to: 200K calls a month, 3.5 minutes each, $2.8M released."),
    ("arrow-left-right", "Transfers with context", "165K a month; the receiver re-logs the case today. $1.05M."),
    ("rotate-ccw", "Debit order reversal", "26K a month, 9.5 minutes, a case lock and back-office steps. $0.99M."),
    ("search", "Merchant confusion", "29K a month, seven minutes, a fraud-fear note on the case. $0.77M.")], cols=2, pitch=1.55)
d.footnote(s, "Values are released capacity a year at full run, our estimate on bank-stated volumes. The other three rows open the same way.")

# 5 · value map
s = d.slide()
d.chrome(s, "The value map · three pools", "Three pools, twelve levers, one meter")
d.value_map(s, 1.0, 2.0, 11.7, [
    dict(name="Cost to serve", value="$9.1M", icon="coins", levers=[("First reception, 17 intents", "$9.1M"), ("After-call minutes", "0.3 to 4.5"), ("Contacts never logged", "a third")]),
    dict(name="Revenue", value="$2.2M to $3.8M", icon="trending-up", levers=[("Right party reached", "+156K"), ("Hear the offer", "+131K"), ("Booked", "+62K")]),
    dict(name="Risk and conduct", value="fewer gaps", icon="shield-check", levers=[("Every contact written to a case", "all"), ("Consent and recording, every call", "by design"), ("Vulnerable callers to a person", "always")])],
    total=("$13.4M", "released a year at full run across the three pools; the meter bills finished work only"))
d.footnote(s, "Pools follow the canon's three value pools. Cost and revenue from the live fire; risk levers are design commitments and carry no figure.")

# 6 · chevron flow
s = d.slide()
d.chrome(s, "How a deal runs · flow", "Five steps and twenty weeks to go-live")
d.chevron_flow(s, 1.0, 2.9, 11.7, [
    ("Demo", "Capability first, on their intents if we have them.", "play"),
    ("Ignite, two weeks", "Free. Four sessions, no forms: demand map, baseline in the room, writing room, decision day.", "sparkles"),
    ("Proof of value", "Two weeks with a ring-fenced team on the bank's own intents; a scorecard per tester.", "flask-conical"),
    ("Approval pack", "In the bank's own template, with the case in their figures.", "file-check"),
    ("Order", "Twenty weeks to go-live on things that already run; the meter starts at go-live.", "pen-line")], h=1.0)
d.statement_line(s, 1.0, 5.75, 11.7, "Decision day goes in the calendar before session one.", "No date, no engagement.")
d.footnote(s, "Ignite effort: seven or eight consultant days. The VC on the region runs it; the AE owns the commercial thread; the SE owns the architecture hour.")

# 7 · rings
s = d.slide()
d.chrome(s, "Where the assistant sits · rings", "One brain at the core, the bank's systems on the outside")
d.rings(s, 3.6, 4.3, 2.0, [
    ("The brain", "intent, identity, context and the router, built once"),
    ("The rails", "the bank's certified write paths, one per intent"),
    ("The channels", "voice, chat, the app, messaging, the kiosk"),
    ("The bank's systems", "the case system, the core, the CRM, telephony: read through the gateway, nothing copied")], label_x=6.6, label_w=6.0)
d.footnote(s, "The rings are the placement rule: the assistant reads through the gateway or MCP, writes only on certified rails, and the case system stays the master record.")

# 8 · stack, ziggurat
s = d.slide()
d.chrome(s, "The architecture · ziggurat", "Two layers of ours on the bank's rails")
d.stack(s, 1.0, 2.15, 11.7, [
    dict(title="The front end and intent layer", sub="language, identity, intent, context and channel", icon="message-circle", verb="answers", thesis="The caller is verified and understood in fifteen seconds, in their language."),
    dict(title="Orchestration and governance", sub="routing, policy, the specialised agents, the evaluator", icon="route", verb="decides", thesis="Each turn takes the cheapest safe path; every conversation is checked after."),
    dict(title="The router and the meter", sub="model choice per turn; the bill on finished work", icon="gauge", verb="meters", thesis="Route, cost and outcome sit on one record, so the bill is attributable."),
    dict(title="The bank's rails", sub="the case system, the core, the CRM, telephony, identity", icon="landmark", verb="stays", thesis="Nothing is copied or moved; writes are governed and certified per path.")],
    shape='ziggurat', band_h=1.0)
d.footnote(s, "The placements against the bank's own engine (on top, as a node under theirs, as the caller of theirs) are configuration of the top two layers, never a rebuild.")

# 9 · hub and spoke
s = d.slide()
d.chrome(s, "One brain, six surfaces · hub and spoke", "The app and the kiosk consume the brain the phone installed")
d.hub_spoke(s, 6.6, 4.15, ("The assistant", "built once", "bot"), [
    ("Voice", "the contact centre, first", "phone"), ("Chat", "the app's front door", "message-square"), ("The app", "nine in ten intents guided", "smartphone"),
    ("Messaging", "WhatsApp, a reference", "send"), ("The kiosk", "the branch queue", "monitor"), ("The staff desk", "the brief before hello", "headset")], r=1.55, start=-60)
d.footnote(s, "80 to 90% of the build is reused across surfaces: intent, identity, context and the rails are built once. The second channel costs a fraction of the first.")

# 10 · icon rows
s = d.slide()
d.chrome(s, "Where to enter · five doors", "Five doors into a bank, one rule: enter where the volume is")
d.icon_rows(s, 1.0, 2.25, 11.7, [
    ("moon", "The after-hours assistant", "When the centre cuts hours the calls still come; 60% of requests at one bank arrive after hours."),
    ("door-open", "First reception", "A third of inbound calls arrive unauthenticated; the assistant takes identity, intent and the routine ones."),
    ("recycle", "The aging bot trade-in", "Dead ends and escalations are the headline; transactions on rails are the fix."),
    ("phone-outgoing", "Outbound warm-up", "Half the dials miss and the pitch starts cold; an SMS with a reference and a call that books."),
    ("hand-coins", "Collections", "Promise to pay and the payment link inside the call; $1.3M banked in-call at one specialist.")], cols=2, pitch=1.25)
d.statement_line(s, 1.0, 5.95, 11.7, "Deflection alone is the crowded corner.", "Enter there only with a short tenure, then widen and deepen.")
d.footnote(s, "Each door has one value line and one proof point; pick the door the bank's call log opens.")

# 11 · venn
s = d.slide()
d.chrome(s, "Where we win · overlap", "The value sits where the bank's rails meet our brain")
d.venn(s, 5.2, 4.35, 2.05, ("What the bank owns", "its case states, its core, its telephony, its data, its people at the close"),
       ("What we bring", "the brain, the router, the meter, the evaluator, the certified write paths"),
       ("Finished work", "on the bank's own case states, paid per conversation"))
d.icon_rows(s, 9.15, 2.5, 3.6, [("lock", "Sovereignty is a setting", "the bank's cloud, its keys, its region."),
                                ("receipt", "The bill is a receipt", "route, cost and outcome on one record."),
                                ("user-check", "A person keeps the hard calls", "advice, the close, the vulnerable caller.")], pitch=1.3)
d.footnote(s, "The overlap is what the meter bills and nothing else: a conversation finished in the bank's own case states.")

# 12 · pillars
s = d.slide()
d.chrome(s, "The strategy frame · pillars", "Six programmes on one foundation")
d.pillars(s, 1.0, 2.15, 11.7, ("The conversational AI strategy any bank can hold", "read the bank's own strategy onto it"), [
    ("The assistant core", "one brain across every touchpoint; hybrid handover", "brain"),
    ("Chat", "messaging first in Africa, in-app first in Europe", "message-square"),
    ("The app", "consumes the brain instead of building its own", "smartphone"),
    ("Voice", "first reception, warm-up, after-hours", "phone"),
    ("Branch and kiosk", "the same assistant on a different surface", "monitor"),
    ("The staff assistant", "the brief before hello, the case written", "headset")],
    ("Governance, compliance, phased delivery, the meter as the discipline", "the gates the bank owns"), col_h=2.4)
d.footnote(s, "The ladder per programme: nothing → rules bot → generative answers → agents that act → proactive. Ask the bank to place each programme on it; the gaps set the sequence.")

d.save(OUT)
print("saved", OUT, "slides:", d.page)
