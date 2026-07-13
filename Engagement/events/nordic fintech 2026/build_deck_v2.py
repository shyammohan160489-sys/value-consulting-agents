"""
Nordic FinTech Forum — Helsinki, May 2026
v2 — Ported to the Backbase Slides format (17-layout engine)

Same narrative as v1 (nordic_fintech_forum_opening_pov.html):
  Act 1 — The Commodity Trap
  Act 2 — Trust Becomes Infrastructure
  Act 3 — The Intent Layer
  Synthesis — Orchestration of trust and intent

v1 used the Frontline 2026 design system (bespoke, single-file).
v2 uses the Backbase Slides engine — 17 pixel-perfect layouts,
presenter mode (P), overview grid (O), go-to-slide (G).
"""

import base64
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]                          # /Users/shyam/cortex
APP = REPO / "presentations" / "backbase-slides-app"

TEMPLATE_HTML = (APP / "deck-template.html").read_text()
ENGINE_JS     = (APP / "engine.js").read_text()
BG_B64        = base64.b64encode((APP / "images" / "bg.jpg").read_bytes()).decode()
BG_DATA_URI   = f"data:image/jpeg;base64,{BG_B64}"

# ── Extract <style>...</style> and <body>...</body> blocks from the template ──
style_match = re.search(r"<style>(.*?)</style>", TEMPLATE_HTML, re.S)
body_match  = re.search(r"<body>(.*?)</body>",   TEMPLATE_HTML, re.S)
CSS      = style_match.group(1)
BODY_RAW = body_match.group(1)

# Drop the two <script src="..."> tags — we inline scripts ourselves.
BODY = re.sub(r'<script src="[^"]+"></script>', "", BODY_RAW).strip()

# Replace shared-asset bg.jpg references in the engine with the inlined data URI.
ENGINE_INLINED = ENGINE_JS.replace("${BB_SHARED_ASSETS}/images/bg.jpg", BG_DATA_URI)

# ─────────────────────────────────────────────────────────────────────
# SLIDES
# ─────────────────────────────────────────────────────────────────────

SLIDES = [
    # 1. COVER
    {
        "layout": "cover-color-block",
        "label": "DIFFERENTIATION IN THE AGE OF AI",
        "title": "Intelligence,\nCommoditised.",
        "date": "Nordic FinTech Forum · Helsinki · May 2026",
    },

    # 2. PROVOCATION
    {
        "layout": "statement",
        "accent": "blue",
        "label": "THE PROVOCATION",
        "text": 'Every bank is shipping AI. None of them are <span class="hl">different</span>.',
    },

    # 3. ARCHITECTURE IS SHIFTING — Products → Trust → Intent (3-pillar setup arc)
    {
        "layout": "content-standard",
        "theme": "light",
        "label": "OUR OBSERVATION",
        "title": "The architecture of banking is shifting.",
        "subtitle": "Most banks have built strong products. The question is what connects them — and what acts on that connection.",
        "body": (
            "<div style='display:grid;grid-template-columns:1fr 0.18fr 1fr 0.18fr 1fr;gap:0.4em;align-items:stretch;margin-top:0.4em'>"

            # Pillar 1 — Products (red)
            "<div style='padding:0.95em 1em;border:1.5px solid #FF503C;border-radius:0.45em;display:flex;flex-direction:column;gap:0.5em;background:#fff'>"
            "<span style='align-self:flex-start;padding:0.32em 0.7em;background:#FFE6E2;color:#FF503C;font-size:0.5em;font-weight:700;letter-spacing:0.15em;text-transform:uppercase;border-radius:0.3em'>STRONG BUT ISOLATED</span>"
            "<div style='font-size:1.55em;font-weight:700;color:#FF503C;line-height:1'>Products</div>"
            "<div style='font-size:0.62em;color:#091C35;line-height:1.55'>Banks have built strong products &mdash; vertically, in silos. Onboarding lives in one system. Lending in another. Wealth in a third.</div>"
            "<div style='font-size:0.62em;color:#091C35;line-height:1.55;font-weight:500;margin-top:auto'>The products work. The connections between them are manual.</div>"
            "</div>"

            # Arrow 1
            "<div style='display:flex;align-items:center;justify-content:center;color:#FF503C;font-size:1.4em;font-weight:600'>&rarr;</div>"

            # Pillar 2 — Trust (navy)
            "<div style='padding:0.95em 1em;border:1.5px solid #091C35;border-radius:0.45em;display:flex;flex-direction:column;gap:0.5em;background:#fff'>"
            "<span style='align-self:flex-start;padding:0.32em 0.7em;background:#E5EAF0;color:#091C35;font-size:0.5em;font-weight:700;letter-spacing:0.15em;text-transform:uppercase;border-radius:0.3em'>CONNECTIVE TISSUE</span>"
            "<div style='font-size:1.55em;font-weight:700;color:#091C35;line-height:1'>Trust</div>"
            "<div style='font-size:0.62em;color:#091C35;line-height:1.55'>Identity, consent, risk, compliance &mdash; not as checkboxes, but as <strong>shared infrastructure</strong> that connects everything.</div>"
            "<div style='font-size:0.62em;color:#091C35;line-height:1.55;margin-top:auto'>Reusable across products, markets, and channels. The same framework governing onboarding, a payment, and an API call.</div>"
            "</div>"

            # Arrow 2
            "<div style='display:flex;align-items:center;justify-content:center;color:#3366FF;font-size:1.4em;font-weight:600'>&rarr;</div>"

            # Pillar 3 — Intent (blue)
            "<div style='padding:0.95em 1em;border:1.5px solid #3366FF;border-radius:0.45em;display:flex;flex-direction:column;gap:0.5em;background:#fff'>"
            "<span style='align-self:flex-start;padding:0.32em 0.7em;background:#E5EBFF;color:#3366FF;font-size:0.5em;font-weight:700;letter-spacing:0.15em;text-transform:uppercase;border-radius:0.3em'>EMERGING FRONTIER</span>"
            "<div style='font-size:1.55em;font-weight:700;color:#3366FF;line-height:1'>Intent</div>"
            "<div style='font-size:0.62em;color:#091C35;line-height:1.55'>AI that doesn&rsquo;t just report or respond &mdash; it <strong>acts</strong>.</div>"
            "<div style='font-size:0.62em;color:#091C35;line-height:1.55;margin-top:auto'>An agent that approves a top-up the moment the facility allows. An agent that books a wealth review when a life event triggers. An agent that settles a dispute the moment evidence clears &mdash; within governed boundaries.</div>"
            "</div>"

            "</div>"

            # Tagline strip
            "<div style='margin-top:0.65em;padding:0.6em 1em;background:#E5EBFF;border-radius:0.35em;text-align:center;font-size:0.65em;line-height:1.5;color:#091C35'>"
            "Value is migrating from the product to the trust layer, and from trust to intent. "
            "<strong>The banks that connect trust to real-time decisioning at scale</strong> will define the next decade of banking."
            "</div>"
        ),
    },

    # 4. ACT 1 DIVIDER
    {
        "layout": "chapter-numbered",
        "theme": "navy",
        "number": "01",
        "label": "ACT 1",
        "title": "The Commodity Trap",
        "subtitle": "Intelligence is becoming electricity. Everyone has it. Nobody wins on it.",
    },

    # 5. ACT 1 — signals (3 stats as columns)
    {
        "layout": "content-columns",
        "label": "ACT 1 · SIGNALS",
        "title": "Why the AI advantage will not hold",
        "columns": [
            {
                "body": (
                    "<div style='font-size:3.4em;font-weight:700;color:#3366FF;line-height:1;margin-bottom:0.25em'>&lt;5%</div>"
                    "<div style='font-weight:500;color:#091C35;font-size:1.05em;margin-bottom:0.4em'>Performance gap between frontier models on banking-relevant tasks</div>"
                    "<div>Closing — and closing fast.</div>"
                    "<div style='margin-top:0.8em;font-size:0.78em;color:#8a95a5;font-style:italic'>Backbase analysis; Stanford AI Index 2025, HELM benchmarks</div>"
                ),
            },
            {
                "body": (
                    "<div style='font-size:3.4em;font-weight:700;color:#3366FF;line-height:1;margin-bottom:0.25em'>~100%</div>"
                    "<div style='font-weight:500;color:#091C35;font-size:1.05em;margin-bottom:0.4em'>Of global top-50 banks have shipped a GenAI assistant since 2024</div>"
                    "<div>The feature is saturated.</div>"
                    "<div style='margin-top:0.8em;font-size:0.78em;color:#8a95a5;font-style:italic'>Evident AI Index, 2024</div>"
                ),
            },
            {
                "body": (
                    "<div style='font-size:3.4em;font-weight:700;color:#3366FF;line-height:1;margin-bottom:0.25em'>~18 mo</div>"
                    "<div style='font-weight:500;color:#091C35;font-size:1.05em;margin-bottom:0.4em'>Until feature parity — your copilot will look like theirs</div>"
                    "<div>Converging on a single UX.</div>"
                    "<div style='margin-top:0.8em;font-size:0.78em;color:#8a95a5;font-style:italic'>Backbase estimate; Gartner AI Hype Cycle 2024, BCG GenAI Banking Pulse</div>"
                ),
            },
        ],
    },

    # 6. ACT 1 PROOF — This has happened before (AWS, Spotify)
    {
        "layout": "content-columns",
        "label": "PROOF · IT HAS HAPPENED BEFORE",
        "title": "Every intelligence layer commoditises. The winners own what sits above it.",
        "columns": [
            {
                "subtitle": "AWS · 2008 → 2020",
                "body": (
                    "<div style='font-size:2.4em;font-weight:700;color:#3366FF;line-height:1;margin-bottom:0.3em'>$100B+</div>"
                    "<div style='font-weight:500;color:#091C35;font-size:1.05em;margin-bottom:0.4em'>Compute commoditised. Orchestration became the moat.</div>"
                    "<div>EC2 reached parity with Azure and GCP within ~24 months. AWS pulled ahead on primitives, developer experience, and a trust layer regulators could verify. "
                    "The silicon became a line item; the orchestration layer became the largest infrastructure business in history.</div>"
                    "<div style='margin-top:0.8em;font-size:0.78em;color:#8a95a5;font-style:italic'>Synergy Research Cloud Market Share 2024; AWS segment results</div>"
                ),
            },
            {
                "subtitle": "Spotify · 2008 → 2024",
                "body": (
                    "<div style='font-size:2.4em;font-weight:700;color:#3366FF;line-height:1;margin-bottom:0.3em'>675M</div>"
                    "<div style='font-weight:500;color:#091C35;font-size:1.05em;margin-bottom:0.4em'>Every catalogue became identical. Discovery became the product.</div>"
                    "<div>Rivals streamed the same songs. Spotify won on intent orchestration — Discover Weekly, Release Radar, algorithmic playlists — and turned a commoditised catalogue "
                    "into a 675M-user moat no competitor has closed.</div>"
                    "<div style='margin-top:0.8em;font-size:0.78em;color:#8a95a5;font-style:italic'>Spotify MAU, Q4 2024; IFPI Global Music Report 2024</div>"
                ),
            },
        ],
    },

    # 7. ACT 1 — tension
    {
        "layout": "statement",
        "accent": "blue",
        "label": "ACT 1 · TENSION",
        "text": 'If intelligence is a utility, the moat moves <span class="hl">up the stack</span>.',
    },

    # 7. ACT 2 DIVIDER
    {
        "layout": "chapter-numbered",
        "theme": "navy",
        "number": "02",
        "label": "ACT 2",
        "title": "Trust Becomes Infrastructure",
        "subtitle": "Not a brand claim. Not a policy. Plumbing.",
    },

    # 8. ACT 2 — GAP / SHIFT / EDGE tiles
    {
        "layout": "content-columns",
        "label": "THE NEW PLUMBING",
        "title": "Trust shifts from promise to performance",
        "columns": [
            {
                "subtitle": "GAP · 1 in 3",
                "body": (
                    "<div style='margin-bottom:0.4em'><strong style='color:#091C35'>Firms at maturity level 3+ on AI governance.</strong></div>"
                    "Two-thirds of the industry cannot yet prove how their AI decides. That is the gap — and the opportunity."
                    "<div style='margin-top:0.8em;font-size:0.78em;color:#8a95a5;font-style:italic'>McKinsey, The State of AI 2024; directionally confirmed by BCG Responsible AI survey</div>"
                ),
            },
            {
                "subtitle": "SHIFT · Promise → Performance",
                "body": (
                    "<div style='margin-bottom:0.4em'><strong style='color:#091C35'>Trust is becoming a KPI, not a principle.</strong></div>"
                    "Explainability, provenance, and human oversight are moving from policy to product instrumentation."
                    "<div style='margin-top:0.8em;font-size:0.78em;color:#8a95a5;font-style:italic'>Backbase POV; EU AI Act Articles 13–15, NIST AI RMF 1.0</div>"
                ),
            },
            {
                "subtitle": "EDGE · Nordics",
                "body": (
                    "<div style='margin-bottom:0.4em'><strong style='color:#091C35'>Best-positioned region globally.</strong></div>"
                    "High-trust societies, mature regulators, interoperable digital identity. Trust-as-infrastructure is an export, not a cost."
                    "<div style='margin-top:0.8em;font-size:0.78em;color:#8a95a5;font-style:italic'>Edelman Trust Barometer 2024; OECD Trust Survey 2024; Nordic eID interoperability</div>"
                ),
            },
        ],
    },

    # 9. ACT 2 PROOF — Where trust is already infrastructure
    {
        "layout": "content-columns",
        "label": "PROOF · TRUST AS INFRASTRUCTURE",
        "title": "Three institutions that made trust a product — not a policy page.",
        "columns": [
            {
                "subtitle": "BankID + Swish · Nordics",
                "body": (
                    "<div style='font-size:2.4em;font-weight:700;color:#3366FF;line-height:1;margin-bottom:0.3em'>>85%</div>"
                    "<div style='font-weight:500;color:#091C35;font-size:1.05em;margin-bottom:0.4em'>Shared identity. Shared rails. Cooperated on the plumbing.</div>"
                    "<div>Nordic banks cooperated on BankID (digital identity) and Swish (real-time payments) — and competed on the experience above. "
                    "Both exceed 85% adult reach. Trust-as-infrastructure became exportable.</div>"
                    "<div style='margin-top:0.8em;font-size:0.78em;color:#8a95a5;font-style:italic'>Finansiell ID-Teknik BID AB; Getswish AB, 2024</div>"
                ),
            },
            {
                "subtitle": "Apple · 2017 →",
                "body": (
                    "<div style='font-size:2.4em;font-weight:700;color:#3366FF;line-height:1;margin-bottom:0.3em'>ATT</div>"
                    "<div style='font-weight:500;color:#091C35;font-size:1.05em;margin-bottom:0.4em'>Trust made measurable — and premium-priced.</div>"
                    "<div>App Tracking Transparency, on-device ML, and privacy nutrition labels moved trust from brand claim to instrumented product surface. "
                    "Apple charges a premium for it; the mobile ad market reshaped around it.</div>"
                    "<div style='margin-top:0.8em;font-size:0.78em;color:#8a95a5;font-style:italic'>Apple ATT, iOS 14.5 (2021); Privacy Labels, iOS 14 (2020)</div>"
                ),
            },
            {
                "subtitle": "Mastercard · 2016 →",
                "body": (
                    "<div style='font-size:2.4em;font-weight:700;color:#3366FF;line-height:1;margin-bottom:0.3em'>~165B</div>"
                    "<div style='font-weight:500;color:#091C35;font-size:1.05em;margin-bottom:0.4em'>AI-graded trust, sold as infrastructure.</div>"
                    "<div>Mastercard moved upstream into auditable, network-wide fraud scoring — scoring ~165B transactions per year. "
                    "Banks integrate rather than rebuild. Trust became a service with a P&amp;L.</div>"
                    "<div style='margin-top:0.8em;font-size:0.78em;color:#8a95a5;font-style:italic'>Mastercard Decision Intelligence, 2016; FY24 Cyber &amp; Intelligence segment</div>"
                ),
            },
        ],
    },

    # 10. ACT 3 DIVIDER
    {
        "layout": "chapter-numbered",
        "theme": "navy",
        "number": "03",
        "label": "ACT 3",
        "title": "The Intent Layer",
        "subtitle": "When your customer stops using your app — but still needs your bank.",
    },

    # 10. ACT 3 — the intent economy (3 stats)
    {
        "layout": "content-columns",
        "label": "THE INTENT ECONOMY",
        "title": "The interface is disappearing. The balance sheet is not.",
        "columns": [
            {
                "body": (
                    "<div style='font-size:3.4em;font-weight:700;color:#3366FF;line-height:1;margin-bottom:0.25em'>$3–5T</div>"
                    "<div style='font-weight:500;color:#091C35;font-size:1.05em;margin-bottom:0.4em'>Agentic commerce revenue at stake by 2030</div>"
                    "<div>A new platform shift.</div>"
                    "<div style='margin-top:0.8em;font-size:0.78em;color:#8a95a5;font-style:italic'>McKinsey, The Economic Potential of Generative AI (updated 2024); agentic AI follow-on research</div>"
                ),
            },
            {
                "body": (
                    "<div style='font-size:3.4em;font-weight:700;color:#3366FF;line-height:1;margin-bottom:0.25em'>~57%</div>"
                    "<div style='font-weight:500;color:#091C35;font-size:1.05em;margin-bottom:0.4em'>Of banking execs expect AI agents embedded in core ops within 3 years</div>"
                    "<div>The exec consensus has shifted.</div>"
                    "<div style='margin-top:0.8em;font-size:0.78em;color:#8a95a5;font-style:italic'>Backbase analysis; NVIDIA State of AI in Financial Services 2025, EY FS AI Pulse</div>"
                ),
            },
            {
                "body": (
                    "<div style='font-size:3.4em;font-weight:700;color:#3366FF;line-height:1;margin-bottom:0.25em'>~24 mo</div>"
                    "<div style='font-weight:500;color:#091C35;font-size:1.05em;margin-bottom:0.4em'>Until agents transact on customers' behalf at scale</div>"
                    "<div>Your next customer may be a machine.</div>"
                    "<div style='margin-top:0.8em;font-size:0.78em;color:#8a95a5;font-style:italic'>Backbase estimate; Gartner Agentic AI Outlook 2025, Accenture Technology Vision 2025</div>"
                ),
            },
        ],
    },

    # 12. ACT 3 PROOF — When the bank becomes the rail
    {
        "layout": "content-columns",
        "label": "PROOF · WHEN SOMEONE ELSE OWNS THE INTENT",
        "title": "Three cases where another player owned the intent — and captured the relationship.",
        "columns": [
            {
                "subtitle": "Klarna · Sweden, 2005 →",
                "body": (
                    "<div style='font-size:2.4em;font-weight:700;color:#3366FF;line-height:1;margin-bottom:0.3em'>150M</div>"
                    "<div style='font-weight:500;color:#091C35;font-size:1.05em;margin-bottom:0.4em'>The shopping agent owned the credit.</div>"
                    "<div>Klarna owned the checkout moment — the intent layer of consumer commerce. 150M+ consumers globally. "
                    "The bank extending credit became invisible; Klarna became the brand on the screen.</div>"
                    "<div style='margin-top:0.8em;font-size:0.78em;color:#8a95a5;font-style:italic'>Klarna investor materials, 2024; BCG Global Payments Report 2024</div>"
                ),
            },
            {
                "subtitle": "Plaid · US, 2013 →",
                "body": (
                    "<div style='font-size:2.4em;font-weight:700;color:#3366FF;line-height:1;margin-bottom:0.3em'>1 in 4</div>"
                    "<div style='font-weight:500;color:#091C35;font-size:1.05em;margin-bottom:0.4em'>The API between customers and their banks.</div>"
                    "<div>One in four US adults have connected an account through Plaid. Every consumer-fintech app routes through it; "
                    "banks became the backend. The intent layer moved to a seven-year-old startup.</div>"
                    "<div style='margin-top:0.8em;font-size:0.78em;color:#8a95a5;font-style:italic'>Plaid public statements, 2024; CFPB Section 1033 filings</div>"
                ),
            },
            {
                "subtitle": "M-Pesa · Kenya, 2007 →",
                "body": (
                    "<div style='font-size:2.4em;font-weight:700;color:#3366FF;line-height:1;margin-bottom:0.3em'>~60%</div>"
                    "<div style='font-weight:500;color:#091C35;font-size:1.05em;margin-bottom:0.4em'>A telco became the bank.</div>"
                    "<div>Safaricom's M-Pesa captured trust + intent before Kenyan banks modernised. It now moves ~60% of Kenya's GDP. "
                    "Banks remain — they are no longer the primary layer the customer interacts with.</div>"
                    "<div style='margin-top:0.8em;font-size:0.78em;color:#8a95a5;font-style:italic'>Safaricom FY24 annual report; CBK National Payments Strategy 2022–25</div>"
                ),
            },
        ],
    },

    # 13. SYNTHESIS — 3-layer stack (custom HTML in content-standard body)
    {
        "layout": "content-standard",
        "theme": "light",
        "label": "THE THESIS",
        "title": "Differentiation is the orchestration layer",
        "subtitle": "Three layers. The bottom commoditises. The top two are the competition.",
        "body": (
            "<div style='display:flex;flex-direction:column;gap:0.55em;margin-top:0.4em'>"

            # Intent Layer (dark)
            "<div style='background:#091C35;color:#fff;padding:0.9em 1.1em;border-radius:0.25em;display:flex;align-items:center;gap:1.2em'>"
            "<div style='flex:0 0 30%'>"
            "<div style='font-size:0.55em;font-weight:700;letter-spacing:0.12em;text-transform:uppercase;color:#3366FF;margin-bottom:0.3em'>LAYER 3 · INTENT</div>"
            "<div style='font-size:0.85em;font-weight:400;color:#fff'>Where customers and their agents act</div>"
            "</div>"
            "<div style='display:flex;flex-wrap:wrap;gap:0.4em;flex:1'>"
            + "".join(
                f"<span style='padding:0.32em 0.75em;border:1px solid rgba(51,102,255,0.6);border-radius:2em;font-size:0.7em;color:#fff'>{x}</span>"
                for x in ["Agent-to-bank APIs", "Intent routing", "Delegated authority", "Outcome contracts"]
            ) +
            "</div></div>"

            # Trust Layer (light blue)
            "<div style='background:#E5EBFF;color:#091C35;padding:0.9em 1.1em;border-radius:0.25em;display:flex;align-items:center;gap:1.2em'>"
            "<div style='flex:0 0 30%'>"
            "<div style='font-size:0.55em;font-weight:700;letter-spacing:0.12em;text-transform:uppercase;color:#3366FF;margin-bottom:0.3em'>LAYER 2 · TRUST</div>"
            "<div style='font-size:0.85em;font-weight:400'>The moat — instrumented, audited, provable</div>"
            "</div>"
            "<div style='display:flex;flex-wrap:wrap;gap:0.4em;flex:1'>"
            + "".join(
                f"<span style='padding:0.32em 0.75em;border:1px solid #3366FF;border-radius:2em;font-size:0.7em;background:#fff;color:#091C35'>{x}</span>"
                for x in ["Explainability", "Provenance", "Human oversight", "Consent & identity", "Audit trail"]
            ) +
            "</div></div>"

            # Intelligence Layer (muted)
            "<div style='background:#F3F6F9;color:#5C6E84;padding:0.9em 1.1em;border-radius:0.25em;display:flex;align-items:center;gap:1.2em'>"
            "<div style='flex:0 0 30%'>"
            "<div style='font-size:0.55em;font-weight:700;letter-spacing:0.12em;text-transform:uppercase;color:#5C6E84;margin-bottom:0.3em'>LAYER 1 · INTELLIGENCE</div>"
            "<div style='font-size:0.85em;font-weight:400'>The commodity — assume parity in 18 months</div>"
            "</div>"
            "<div style='display:flex;flex-wrap:wrap;gap:0.4em;flex:1'>"
            + "".join(
                f"<span style='padding:0.32em 0.75em;border:1px solid #C4CDD9;border-radius:2em;font-size:0.7em;color:#5C6E84'>{x}</span>"
                for x in ["Foundation models", "Retrieval", "Agents & tool use", "Fine-tuning"]
            ) +
            "</div></div>"

            "</div>"
        ),
    },

    # 15. CONVICTION 01 — Value migrates up the banking stack (Share of Wallet → Mind → Moments → Trust)
    {
        "layout": "content-standard",
        "theme": "light",
        "label": "THE STACK · WHERE BANKING VALUE IS MIGRATING",
        "title": "Value is migrating up the banking stack.",
        "subtitle": "From a transaction-centric utility to a relationship-centric ubiquity. Most banks compete at level 1 today — the next decade is won at 3 and 4.",
        "body": (
            "<div style='display:flex;flex-direction:column;gap:0.18em;margin-top:0.3em'>"
            # 04 — Share of Trust (gradient, top)
            "<div style='padding:0.65em 1.1em;border-radius:0.4em;background:linear-gradient(135deg,#264EC7 0%,#3366FF 50%,#3366FF 100%);color:#fff;display:flex;justify-content:space-between;align-items:center;gap:1em;box-shadow:0 0.25em 0.7em rgba(51,102,255,0.22)'>"
            "<div><div style='font-size:0.5em;font-weight:700;letter-spacing:0.18em;opacity:0.85'>04 · THE MOAT</div>"
            "<div style='font-size:0.95em;font-weight:700;margin-top:0.1em'>Share of Trust</div></div>"
            "<div style='font-size:0.6em;line-height:1.4;text-align:right;max-width:14em;opacity:0.95'>Governed AI — explainable, human-in-the-loop, audit-ready</div>"
            "</div>"
            # arrow
            "<div style='text-align:center;color:#3366FF;font-size:0.55em;opacity:0.55;line-height:0.6'>▲</div>"
            # 03 — Share of Moments (solid blue)
            "<div style='padding:0.65em 1.1em;border-radius:0.4em;background:#3366FF;color:#fff;display:flex;justify-content:space-between;align-items:center;gap:1em'>"
            "<div><div style='font-size:0.5em;font-weight:700;letter-spacing:0.18em;opacity:0.78'>03 · THE FRONTIER</div>"
            "<div style='font-size:0.95em;font-weight:700;margin-top:0.1em'>Share of Moments</div></div>"
            "<div style='font-size:0.6em;line-height:1.4;text-align:right;max-width:14em;opacity:0.95'>Right offer, right context, right channel — in the moment</div>"
            "</div>"
            # arrow
            "<div style='text-align:center;color:#3366FF;font-size:0.55em;opacity:0.4;line-height:0.6'>▲</div>"
            # 02 — Share of Mind (light blue)
            "<div style='padding:0.65em 1.1em;border-radius:0.4em;background:#E5EBFF;color:#264EC7;display:flex;justify-content:space-between;align-items:center;gap:1em'>"
            "<div><div style='font-size:0.5em;font-weight:700;letter-spacing:0.18em;opacity:0.78'>02 · THE TISSUE</div>"
            "<div style='font-size:0.95em;font-weight:700;margin-top:0.1em'>Share of Mind</div></div>"
            "<div style='font-size:0.6em;line-height:1.4;text-align:right;max-width:14em;opacity:0.9'>One consistent fabric of identity, consent and service across every channel</div>"
            "</div>"
            # arrow
            "<div style='text-align:center;color:#3366FF;font-size:0.55em;opacity:0.3;line-height:0.6'>▲</div>"
            # 01 — Share of Wallet (muted)
            "<div style='padding:0.65em 1.1em;border-radius:0.4em;background:#F3F6F9;color:#5C6E84;display:flex;justify-content:space-between;align-items:center;gap:1em;border:1px solid #CED2D7'>"
            "<div><div style='font-size:0.5em;font-weight:700;letter-spacing:0.18em;opacity:0.7'>01 · THE FLOOR</div>"
            "<div style='font-size:0.95em;font-weight:700;margin-top:0.1em'>Share of Wallet</div></div>"
            "<div style='font-size:0.6em;line-height:1.4;text-align:right;max-width:14em;opacity:0.9'>Strong individual products — but isolated, surface-level, easy to commoditise</div>"
            "</div>"
            "</div>"
        ),
    },

    # 16. CONVICTION 02 — Bolt-on programmes lose. Re-platforms win.
    {
        "layout": "content-standard",
        "theme": "light",
        "label": "THE PATTERN · TWO RESPONSES TO AI",
        "title": "Bolt-on programmes lose. Re-platforms win.",
        "subtitle": "An identity shift, not a tech upgrade. The decision is not whether to use AI — it is what AI plugs into.",
        "body": (
            "<div style='display:grid;grid-template-columns:1fr 1fr;gap:1em;margin-top:0.3em'>"
            # Pattern A — Bolt-on
            "<div style='padding:0.95em 1.1em;background:#FAE0DE;border-radius:0.4em;border-left:0.22em solid #FF503C;display:flex;flex-direction:column;gap:0.45em'>"
            "<div style='font-size:0.55em;font-weight:700;letter-spacing:0.18em;color:#FF503C;text-transform:uppercase'>PATTERN A · BOLT-ON</div>"
            "<div style='font-size:0.95em;font-weight:600;color:#091C35;line-height:1.3'>AI added to product silos.</div>"
            "<div style='display:flex;flex-direction:column;gap:0.28em'>"
            + "".join(
                f"<div style='font-size:0.65em;color:#5C6E84;line-height:1.45;padding-left:1em;position:relative'><span style='position:absolute;left:0;color:#FF503C'>▸</span>{x}</div>"
                for x in [
                    "Channel-by-channel agents, each owned by a different P&amp;L",
                    "Five copies of the customer; none authoritative",
                    "AI fluent at the front, broken at the back",
                    "NPS plateaus, cost-to-serve doesn&rsquo;t move",
                ]
            ) +
            "</div>"
            "<div style='margin-top:auto;padding:0.5em 0.8em;background:#fff;border-radius:0.35em;font-size:0.6em;color:#5C6E84;line-height:1.4;font-style:italic'>&ldquo;Faster cars on the same broken roads.&rdquo; &mdash; what we have seen at most tier-1 banks attempting transformation.</div>"
            "</div>"
            # Pattern B — Re-platform
            "<div style='padding:0.95em 1.1em;background:#E5EBFF;border-radius:0.4em;border-left:0.22em solid #3366FF;display:flex;flex-direction:column;gap:0.45em'>"
            "<div style='font-size:0.55em;font-weight:700;letter-spacing:0.18em;color:#3366FF;text-transform:uppercase'>PATTERN B · RE-PLATFORM</div>"
            "<div style='font-size:0.95em;font-weight:600;color:#091C35;line-height:1.3'>A single fabric for the customer life.</div>"
            "<div style='display:flex;flex-direction:column;gap:0.28em'>"
            + "".join(
                f"<div style='font-size:0.65em;color:#091C35;line-height:1.45;padding-left:1em;position:relative'><span style='position:absolute;left:0;color:#3366FF'>▸</span>{x}</div>"
                for x in [
                    "One identity, one consent, one customer record",
                    "Orchestration layer any AI agent can plug into",
                    "Consistent CX from app to branch to advisor",
                    "Lift compounds &mdash; NPS, NTB, cost and ROE move together",
                ]
            ) +
            "</div>"
            "<div style='margin-top:auto;padding:0.5em 0.8em;background:#fff;border-radius:0.35em;font-size:0.6em;color:#091C35;line-height:1.4;font-style:italic'>&ldquo;One operating fabric for the customer life.&rdquo; &mdash; the pattern in every bank that has actually moved up the stack.</div>"
            "</div>"
            "</div>"
            # Anchor box
            "<div style='margin-top:0.6em;padding:0.6em 1em;background:#fff;border:1px solid #CED2D7;border-left:0.22em solid #3366FF;border-radius:0.4em;display:flex;align-items:center;gap:1.2em'>"
            "<div style='font-size:0.7em;color:#091C35;line-height:1.45;flex:1'>The decision is not <em>whether to use AI</em>. It is <strong style='color:#3366FF'>what AI plugs into</strong>. A bolt-on programme adds intelligence to silos. A re-platform turns the bank into the platform.</div>"
            "</div>"
        ),
    },

    # 17. DISCUSSION — three questions
    {
        "layout": "content-columns",
        "label": "DISCUSSION",
        "title": "Three questions to open the room",
        "columns": [
            {
                "subtitle": "Act 1 — Commodity Trap",
                "body": (
                    "<div style='font-weight:500;color:#091C35;margin-bottom:0.5em'>If your AI looks like theirs in 18 months, what is left to compete on?</div>"
                    "Name one capability your bank owns that a competitor cannot buy."
                ),
            },
            {
                "subtitle": "Act 2 — Trust as Infrastructure",
                "body": (
                    "<div style='font-weight:500;color:#091C35;margin-bottom:0.5em'>Is trust a marketing claim, a compliance cost, or a product?</div>"
                    "If it is a product — who owns the roadmap?"
                ),
            },
            {
                "subtitle": "Act 3 — Intent Layer",
                "body": (
                    "<div style='font-weight:500;color:#091C35;margin-bottom:0.5em'>When an agent shops for a mortgage on behalf of a customer, does it pick your bank — or route around you?</div>"
                    "What would make you the default choice of a machine?"
                ),
            },
        ],
    },

    # 13. CLOSING STATEMENT
    {
        "layout": "statement",
        "accent": "blue",
        "label": "THE THESIS",
        "text": 'The next decade of banking is not won on intelligence. It is won on the <span class="hl">orchestration of trust and intent</span>.',
    },

    # 14. THANK YOU
    {"layout": "thank-you"},
]

SPEAKER_NOTES = {
    1: """WHY THIS SLIDE
The opener does two jobs: it sets the format (Chatham House, no attribution, co-authored output) and lets the title — "Intelligence, Commoditised." — work as a two-word thesis. Resist the urge to over-explain it.

STORY TRACK
"Welcome. Thanks to the organisers for the room. One reminder before we start — this is Chatham House. Names won't be attributed. So please be more candid than you would be on a panel stage. The session's collective answers will be published — anonymised — as the Helsinki Principles. You're not just consumers of a roundtable today. You're co-authors of the output."

AUDIENCE CUE
Pause for ~5 seconds on the title before speaking. Let "Intelligence, Commoditised" sit. Don't rush to slide 2.

[Press P during presentation for these notes + timer + next-slide preview.]""",

    2: """WHY THIS SLIDE
The provocation has to land hard or the rest of the deck reads as academic. This is the discomfort the next 15 minutes resolve.

STORY TRACK
"Here's the line I'd like to leave with you. Every bank in this room is shipping AI. Pilots, copilots, automation, agents. The vendors are pitching, the proofs of concept are stacking up. And by every benchmark that matters — none of you are different from each other."

AUDIENCE CUE
After "different" — full stop. 5-second pause. Look up. Do NOT explain the line. Let the next slides do the work. If anyone laughs uncomfortably, smile and move on.""",

    3: """WHY THIS SLIDE
The colleague-friendly setup. Banks understand "products in silos" instantly — it's their lived reality. This slide gives the audience a mental map of the entire talk in 30 seconds: Act 1 attacks the Products silo problem, Act 2 builds the Trust connective tissue, Act 3 unlocks the Intent layer. If your colleague nails this slide, the rest of the deck has scaffolding to hang on. The three pillars in this slide ARE the three acts that follow.

STORY TRACK
"Here's our observation. The architecture of banking is shifting. Most banks in this room have built strong products — onboarding lives in one system, lending in another, wealth in a third. The products work. What's broken is what connects them — and what acts on those connections. Three layers. Products: strong, but isolated. Trust: identity, consent, risk, compliance — not as checkboxes, but as shared infrastructure. The same framework governing onboarding, a payment, and an API call. And Intent: AI that doesn't report or respond — it acts. An agent that approves a top-up when the facility allows. An agent that books a wealth review when a life event triggers. An agent that settles a dispute the moment evidence clears — within governed boundaries. Value is migrating from the product to the trust layer, and from trust to intent. The banks that connect trust to real-time decisioning at scale will define the next decade of banking. The next ten minutes are about why."

AUDIENCE CUE
Walk the room across the three pillars left-to-right. Point at each as you name it. Pause briefly after the closing tagline strip — let "next decade of banking" sit. Then say: "The next ten minutes are about why." Move to Act 1.""",

    4: """WHY THIS SLIDE
Act 1 divider. Title-card pacing. Use it as a breath after the provocation.

STORY TRACK
"Act 1. The uncomfortable truth. Intelligence is becoming electricity. Everyone has it. Nobody wins on it."

AUDIENCE CUE
Let the navy slide breathe for 3 seconds. Move on.""",

    5: """WHY THIS SLIDE
Three numbers grounded in real sources. The <5% is the killer (frontier model gap on banking tasks is closing). 100% proves saturation. 18 months is the executive horizon. Every claim has a footnote — point at them if anyone challenges.

STORY TRACK
"Three signals. First — the performance gap between frontier models on banking-relevant tasks is under 5% and closing. Stanford AI Index, HELM benchmarks. The model is not the moat. Second — roughly 100% of global top-50 banks have shipped a GenAI assistant since 2024. Evident AI Index. The feature is saturated. Third — about 18 months until feature parity. Your copilot will look like your competitor's. That's not a forecast — it's the roadmap horizon every analyst is now publishing."

AUDIENCE CUE
After the third stat — turn to the room. "If you've shipped GenAI in the last 12 months, what differentiation are you actually buying?" Don't wait for an answer. Move on. The question seeds the discussion later.""",

    6: """WHY THIS SLIDE
This is the parallel slide. It does the work of making "intelligence commoditises" feel inevitable rather than theoretical. Everyone in the room has lived through AWS. Spotify is the consumer parallel everyone understands. If you can land both parallels, the rest of the deck clicks into place.

STORY TRACK
"Before anyone says 'this is different' — it isn't. We've watched it play out twice in fifteen years. AWS, 2008 to 2014. EC2 reached parity with Azure and GCP within 24 months. AWS pulled ahead on primitives, developer experience, and a trust layer regulators could verify. The silicon became a line item. The orchestration layer became the largest infrastructure business in history. Same pattern, Spotify. Every catalogue became identical. Spotify won on intent orchestration — Discover Weekly, Release Radar, algorithmic playlists. They turned a commoditised input into a 675-million-user moat. The pattern is consistent. The intelligence layer commoditises. The orchestration layer wins."

AUDIENCE CUE
This is a 60–90 second slide. Don't rush. If anyone in the room has lived through AWS migrations, they will nod. That's your signal to move on. If you see blank faces, give one more concrete AWS example before moving.""",

    7: """WHY THIS SLIDE
Single-line transition. Sets up Acts 2 and 3 by asking the question they answer. Don't answer it on this slide.

STORY TRACK
"If intelligence is a utility, the moat moves up the stack. So where does it go? Two places."

AUDIENCE CUE
Don't pause too long. Move directly to Act 2.""",

    8: """WHY THIS SLIDE
Act 2 divider. The contrast — "plumbing, not branding" — is the whole frame for Act 2. Banks default to talking about trust as a marketing concept; we're claiming it's an operational one.

STORY TRACK
"Act 2. Trust as plumbing, not branding. Not a marketing claim. Not a compliance line in the annual report. Plumbing."

AUDIENCE CUE
Pause. Let "plumbing" sit. Move on.""",

    9: """WHY THIS SLIDE
Three observations across one frame: where the gap is, where the shift is going, and where the edge sits. The EDGE column is the room-flatterer — Nordics are genuinely best-positioned globally, and you're saying it with a McKinsey number behind you.

STORY TRACK
"Three observations. The GAP — only 1 in 3 firms is at AI governance maturity level 3 or higher. McKinsey, BCG. Two-thirds of the industry literally cannot prove how their AI decides. That is the gap, and the opportunity. The SHIFT — trust is becoming an instrumented KPI, not a brand claim. Explainability, provenance, oversight are moving from policy page to product surface. EU AI Act articles 13 to 15, NIST AI RMF — the regulatory floor is rising. The EDGE — and this is for the room. The Nordics are the best-positioned region globally to own this. High-trust societies, mature regulators, interoperable digital identity. The infrastructure is built. The question is: do you know it's an asset, and are you packaging it as one?"

AUDIENCE CUE
Show of hands moment. "How many of your banks today actively MEASURE trust as a KPI? Not 'comply with GDPR' — actually measure trust." Pause. Read the room. Most hands stay down. Note that. Move on.""",

    10: """WHY THIS SLIDE
Three institutions that already turned trust into a product. BankID + Swish is the hometown story — use it. Apple is the consumer parallel that proves trust can be premium-priced. Mastercard shows it can be sold as infrastructure with its own P&L.

STORY TRACK
"Same exercise as Act 1 — this isn't theoretical. Three institutions already made trust a product surface. BankID and Swish — the Nordics' own. Banks here cooperated on shared identity and shared payment rails, and competed on the experience above. Both exceed 85% adult reach. Trust became infrastructure, and Nordic banks have been quietly exporting it. Apple — App Tracking Transparency, on-device ML, privacy nutrition labels. Trust moved from brand claim to instrumented product surface. Apple charges a premium for it; the mobile ad market reshaped around it. Mastercard — Decision Intelligence, 2016. They moved upstream into auditable, network-wide fraud scoring. Banks integrate rather than rebuild. Trust became a service with its own P&L. The pattern: you can build trust into the product, or you can market it as a value. The first is a moat. The second is a press release."

AUDIENCE CUE
After BankID — turn to the room. "How many of you sit on the boards or governance of BankID, Swish, or their equivalents?" Beat. Most hands. "Then you already own this asset. The question is — have you instrumented it for the AI era?"
""",

    11: """WHY THIS SLIDE
Act 3 divider. The bigger shift, the most consequential. The subtitle is the hook: "when your customer stops using your app — but still needs your bank."

STORY TRACK
"Act 3. The bigger shift. When your customer stops using your app — but still needs your bank."

AUDIENCE CUE
This line is meant to make people lean in. Pause. Don't elaborate yet. Move on.""",

    12: """WHY THIS SLIDE
Three numbers that quantify the intent shift. McKinsey for the size, NVIDIA + EY for the executive sentiment, Gartner + Accenture for the horizon. Numbers softened to "~" because they're directional.

STORY TRACK
"Three numbers. Three to five trillion dollars of agentic commerce revenue at stake by 2030 — McKinsey. About 57% of banking executives expect AI agents embedded in core operations within three years — NVIDIA, EY. And about 24 months until agents are transacting on customers' behalf at scale. Most of the room has had a chatbot for a year. Within two more, the chatbot is the customer."

AUDIENCE CUE
Beat. Look up. "Think about what that means. Your next customer may be a machine. Optimised to compare, switch, route. It doesn't care about your brand. It cares about your terms, your latency, and whether it can trust you to execute. That's the intent layer."
""",

    13: """WHY THIS SLIDE
The Act 3 parallel. When the bank doesn't own the intent layer, someone else does — and they capture the customer relationship. Klarna for the checkout, Plaid for the API, M-Pesa for the population-scale takeover. Three different geographies, same lesson.

STORY TRACK
"Same exercise. When the bank doesn't own the intent layer, someone else does. Klarna — owned the checkout moment. The intent layer of consumer commerce. The bank extending the credit became invisible. Klarna became the brand on the screen. Plaid — the API between customers and their banks. One in four US adults has connected an account through it. Every fintech app routes through Plaid; banks became the backend. M-Pesa, Kenya — Safaricom captured trust and intent before Kenyan banks modernised. It moves about 60% of Kenya's GDP today. Banks remain. They are no longer the layer customers interact with."

AUDIENCE CUE
Land this hard. "Look at your customer relationship today. Is there already a Klarna, a Plaid, a Tink, an M-Pesa circling it? And do you know who it is?" Pause. Don't take answers — let it sit and move on. The discomfort is the point.""",

    14: """WHY THIS SLIDE
The synthesis. Three horizontal layers — intelligence (commoditises), trust (the moat), intent (the new interface). Hold it for 30 seconds. Let people read. The visual itself is the argument.

STORY TRACK
"Synthesis. Three layers. The bottom — intelligence. Foundation models, retrieval, agents and tool-use, fine-tuning. Assume parity in 18 months. This commoditises. The middle — trust. Explainability, provenance, oversight, consent, audit trail. The moat. Instrumented, audited, provable. The top — intent. Agent-to-bank APIs, intent routing, delegated authority, outcome contracts. Where customers and their agents act. Differentiation lives in the top two layers. The bottom is your power outlet."

AUDIENCE CUE
30-second hold. Physically point to the bottom layer — "this commoditises". Point to the top two — "this is where you compete". Don't move on quickly. The pause is the punctuation.""",

    15: """WHY THIS SLIDE
The complementary thesis. Slide 14 said WHERE banks compete (3 horizontal layers). This slide says WHAT they compete for (4 vertical tiers of value migration). Use it to walk the room up the stack one tier at a time. This is the framing your colleague will hear quoted back to them in coffee breaks.

STORY TRACK
"And here's what you're competing FOR. Banking value is migrating up four levels. Level 1 — Share of Wallet. Strong individual products, but isolated. Easy to commoditise. Most of this room competes here today. Level 2 — Share of Mind. The connective tissue. One identity, one consent, one service across every channel. Level 3 — Share of Moments. The frontier. AI agents that act when it matters — not chatbots that respond after the fact. Level 4 — Share of Trust. The moat. Governed AI. Explainable. Human-in-the-loop. Audit-ready. Most banks compete at level 1 today. The banks that win the next decade compete at 3 and 4."

AUDIENCE CUE
Show of hands. "Where do most of your AI investments today land — level 1, 2, 3, or 4?" Take a quick read. Most go to 1 or 2. Use that. "That's the gap between where the spend is and where the win lives."
""",

    16: """WHY THIS SLIDE
The most important slide in the deck. Most boards underestimate the scope of what's needed. Bolt-on programmes lose. Re-platforms win. Land this hard — it's the call to action that frames the entire discussion that follows. If your colleague only nails ONE slide, this is the one.

STORY TRACK
"Across the banks we've seen — and we've watched this play out at thirty-plus institutions globally — this is binary. The banks that bolted AI onto product silos lost. They got faster cars on the same broken roads. Channel-by-channel agents, each owned by a different P&L. Five copies of the customer, none authoritative. AI fluent at the front, broken at the back. NPS plateaus. Cost-to-serve doesn't move. The banks that won re-platformed around the customer life. One identity, one consent, one customer record. An orchestration layer that any AI agent — yours or someone else's — can plug into. Consistent CX from app to branch to advisor. And here, the lift compounds. NPS, NTB, cost, ROE move together. This isn't a digital programme. It's an organisational identity shift. That's the harder change to lead. And it's where most boards underestimate the scope. The decision is not whether to use AI. It is what AI plugs into."

AUDIENCE CUE
After "the decision is not whether to use AI. It is what AI plugs into." — full stop. 5-second pause. Don't elaborate. This is the pivot to the discussion. Move when ready.""",

    17: """WHY THIS SLIDE
Hand the room over. Three questions, one per act. ~20 minutes per question. Whiteboard the answers — they become the Helsinki Principles. The questions are deliberately uncomfortable; that's the design.

STORY TRACK
"We've used about twelve minutes. Now the room is yours. Three questions. One per act. Twenty minutes each. Chatham House. Names not attributed. The collective answers become the Helsinki Principles, published anonymised after the forum. Question one — Act 1, the commodity trap: if your AI looks like theirs in 18 months, what's left to compete on? Name one capability your bank owns that a competitor cannot buy. Question two — Act 2, trust: is trust a marketing claim, a compliance cost, or a product? If it's a product — who owns the roadmap? Question three — Act 3, intent: when an agent shops for a mortgage on behalf of a customer, does it pick your bank, or route around you? What would make you the default choice of a machine?"

AUDIENCE CUE
Stop talking. Take question one to the room. "Let's start with question one. Who wants to open?" Wait. Don't fill the silence. Someone will go. If nobody does after 10 seconds, point at someone friendly and ask them by name (or visible role). Whiteboard the answers as you go.""",

    18: """WHY THIS SLIDE
The closing line. The thesis condensed. Don't add anything after.

STORY TRACK
"Last slide before we close. The next decade of banking is not won on intelligence. It is won on the orchestration of trust and intent."

AUDIENCE CUE
Stop talking. Don't elaborate. Don't summarise. Let the line stand. Then quietly: "Thank you." Move to the thank-you slide.""",

    19: """WHY THIS SLIDE
End slide. Use it for the Q&A wrap-up if there's time. Otherwise — thanks and depart.

STORY TRACK
(none — silence is fine here)

AUDIENCE CUE
If running short, this is where Q&A spills over. If on time, this is where you thank the organisers and exit cleanly.""",
}

# ─────────────────────────────────────────────────────────────────────
# Assemble
# ─────────────────────────────────────────────────────────────────────

slides_js = (
    "window.BB_SHARED_ASSETS = '.';\n"
    f"const SLIDES = {json.dumps(SLIDES, ensure_ascii=False, indent=2)};\n"
    f"const SPEAKER_NOTES = {json.dumps(SPEAKER_NOTES, ensure_ascii=False, indent=2)};\n"
)

OUT_HTML = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Differentiation in the Age of AI — Nordic FinTech Forum 2026 (v2)</title>
<style>
{CSS}
</style>
</head>
<body>

{BODY}

<script>
{slides_js}
</script>
<script>
{ENGINE_INLINED}
</script>
</body>
</html>
"""

out_path = HERE / "nordic_fintech_forum_opening_pov_v2.html"
out_path.write_text(OUT_HTML)
print(f"Wrote: {out_path}")
print(f"Size : {out_path.stat().st_size / 1024:.1f} KB")
print(f"Slides: {len(SLIDES)}")
