/* The Advisor Cockpit — A Backbase Point of View
   Wealth & Private Banking · 2026
   Built on the Frontline 2026 Slide Engine */

window.BB_SHARED_ASSETS = '.';

const SLIDES = [

  /* ── COVER ─────────────────────────────────────────────── */
  { layout: 'cover-color-block', label: 'A BACKBASE POINT OF VIEW',
    title: 'The advisor cockpit.\nDashboard to decision engine.',
    date: 'Wealth & Private Banking · The cockpit and AI maturity · 2026' },

  /* ── AGENDA ────────────────────────────────────────────── */
  { layout: 'toc', label: 'WHAT WE’LL COVER', title: 'Four parts', numbered: true, items: [
    'The advisor’s reality today',
    'What good looks like — best practice',
    'Where it’s going — AI maturity',
    'How we build it — Backbase today'
  ]},

  /* ═══ 01 · THE STARTING POINT ══════════════════════════════ */
  { layout: 'chapter-numbered', theme: 'navy', number: '01', label: 'THE STARTING POINT',
    title: 'The advisor’s reality today',
    subtitle: 'The cockpit most advisors have is a dashboard. It shows the past. It doesn’t act.' },

  { layout: 'content-standard', theme: 'light', label: 'THE STARTING POINT',
    title: 'A dashboard, not a cockpit',
    subtitle: 'It shows what happened. The advisor still does the joining-up — by hand.',
    body: `<div style="display:flex;align-items:center;gap:1.4em">
      <div style="width:34%;flex-shrink:0;background:#041326;border-radius:0.4em;padding:1em 1.05em">
        <div style="font-size:0.46em;font-weight:700;letter-spacing:0.12em;text-transform:uppercase;color:#69FEFF;margin-bottom:0.7em">The hidden tax</div>
        <div style="display:flex;justify-content:space-between;align-items:baseline;padding:0.5em 0;border-bottom:1px solid rgba(255,255,255,0.12)"><span style="font-size:0.85em;font-weight:800;color:#fff">6–12</span><span style="font-size:0.46em;color:rgba(255,255,255,0.65);text-align:right">systems per<br>client journey</span></div>
        <div style="display:flex;justify-content:space-between;align-items:baseline;padding:0.5em 0;border-bottom:1px solid rgba(255,255,255,0.12)"><span style="font-size:0.85em;font-weight:800;color:#fff">30–60%</span><span style="font-size:0.46em;color:rgba(255,255,255,0.65);text-align:right">of the work<br>done manually</span></div>
        <div style="display:flex;justify-content:space-between;align-items:baseline;padding:0.5em 0"><span style="font-size:0.85em;font-weight:800;color:#FF503C">0</span><span style="font-size:0.46em;color:rgba(255,255,255,0.65);text-align:right">one shared<br>client truth</span></div>
      </div>
      <div style="flex:1;display:flex;flex-direction:column;gap:0.5em">
        <div style="background:#F3F6F9;border-left:0.16em solid #3367FF;border-radius:0.25em;padding:0.6em 0.9em"><div style="font-size:0.6em;font-weight:700;color:#041326">Swivel-chair servicing</div><div style="font-size:0.5em;color:#6B7786;line-height:1.4;margin-top:0.15em">Answers live across core, CRM, portfolio and document systems. The advisor is the integration layer.</div></div>
        <div style="background:#F3F6F9;border-left:0.16em solid #3367FF;border-radius:0.25em;padding:0.6em 0.9em"><div style="font-size:0.6em;font-weight:700;color:#041326">Reactive, not proactive</div><div style="font-size:0.5em;color:#6B7786;line-height:1.4;margin-top:0.15em">The advisor goes looking. Risks and moments surface late — or not at all.</div></div>
        <div style="background:#F3F6F9;border-left:0.16em solid #3367FF;border-radius:0.25em;padding:0.6em 0.9em"><div style="font-size:0.6em;font-weight:700;color:#041326">Insight ≠ action</div><div style="font-size:0.5em;color:#6B7786;line-height:1.4;margin-top:0.15em">Seeing something and doing something happen in different tools.</div></div>
        <div style="background:#F3F6F9;border-left:0.16em solid #3367FF;border-radius:0.25em;padding:0.6em 0.9em"><div style="font-size:0.6em;font-weight:700;color:#041326">Measured by logins</div><div style="font-size:0.5em;color:#6B7786;line-height:1.4;margin-top:0.15em">Adoption charts — not advice delivered, or outcomes moved.</div></div>
      </div>
    </div>` },

  { layout: 'statement-stat', accent: 'blue', label: 'THE HIDDEN TAX', stat: '60%',
    text: 'of the bank’s work lives in the <span class="hl">whitespace between systems</span> — the handoffs, exceptions and manual coordination no dashboard reaches.',
    source: 'Backbase Banking OS, 2026' },

  { layout: 'statement', variant: 'dark', accent: 'blue', label: 'THE TRAP',
    text: 'A better dashboard won’t fix this. <span class="hl">AI bolted onto a fragmented desk just makes the mess faster</span> — and more expensive.' },

  /* ═══ 02 · BEST PRACTICE ═══════════════════════════════════ */
  { layout: 'chapter-numbered', theme: 'blue', number: '02', label: 'BEST PRACTICE',
    title: 'What good looks like',
    subtitle: 'Six properties separate a decision engine from a dashboard.' },

  { layout: 'content-standard', theme: 'light', label: 'BEST PRACTICE',
    title: 'Six properties of a decision engine',
    body: `<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:0.6em">
      ${[
        ['1','One shared truth','Client 360 from every system — not six open tabs.'],
        ['2','Prioritised, not noisy','The few things that matter today, ranked and filtered.'],
        ['3','Insight → action in place','Decide and act on one screen — governed.'],
        ['4','Advisory-led','Guidance for a human. Never robo for the client.'],
        ['5','Governed by design','Every action authorised, every step audited.'],
        ['6','Measured in advice time','Admin hours reclaimed, outcomes moved.']
      ].map(c => `<div style="background:#F3F6F9;border-top:0.16em solid #3367FF;border-radius:0.3em;padding:0.75em 0.85em">
        <div style="display:flex;align-items:center;gap:0.55em;margin-bottom:0.35em"><span style="width:1.5em;height:1.5em;flex-shrink:0;border-radius:50%;background:#3367FF;color:#fff;font-size:0.55em;font-weight:700;display:flex;align-items:center;justify-content:center">${c[0]}</span><span style="font-size:0.62em;font-weight:700;color:#041326;line-height:1.1">${c[1]}</span></div>
        <div style="font-size:0.5em;color:#6B7786;line-height:1.45">${c[2]}</div></div>`).join('')}
    </div>` },

  { layout: 'content-standard', theme: 'light', label: 'THE SHIFT',
    title: 'From dashboard to decision engine',
    body: `<div style="display:flex;gap:0.8em;align-items:stretch">
      <div style="flex:1;background:#FAE0DE;border-radius:0.35em;padding:0.85em 1em">
        <div style="font-size:0.5em;font-weight:700;letter-spacing:0.1em;text-transform:uppercase;color:#C0392B;margin-bottom:0.5em">Dashboard · today</div>
        ${['Shows data you go and find','A screen for every system','You carry insight to another tool','Reactive — you drive','Counts logins'].map((t,idx,a)=>`<div style="font-size:0.54em;color:#7A3B36;line-height:1.4;padding:0.42em 0;${idx<a.length-1?'border-bottom:1px solid rgba(192,57,43,0.18)':''}">${t}</div>`).join('')}
      </div>
      <div style="display:flex;align-items:center;font-size:1.1em;font-weight:800;color:#3367FF">→</div>
      <div style="flex:1;background:#E5EBFF;border-radius:0.35em;padding:0.85em 1em">
        <div style="font-size:0.5em;font-weight:700;letter-spacing:0.1em;text-transform:uppercase;color:#3367FF;margin-bottom:0.5em">Decision engine · the goal</div>
        ${['Surfaces the few things that matter','One shared client truth','Act in the same place, governed','Proactive — it prompts you','Counts advice time &amp; outcomes'].map((t,idx,a)=>`<div style="font-size:0.54em;color:#1F3A8A;font-weight:500;line-height:1.4;padding:0.42em 0;${idx<a.length-1?'border-bottom:1px solid rgba(51,103,255,0.18)':''}">${t}</div>`).join('')}
      </div>
    </div>` },

  /* ═══ 03 · AI MATURITY ═════════════════════════════════════ */
  { layout: 'chapter-numbered', theme: 'navy', number: '03', label: 'THE TRAJECTORY',
    title: 'Where it’s going — AI maturity',
    subtitle: 'The cockpit is becoming an agentic workspace. Here’s the curve.' },

  { layout: 'content-standard', theme: 'light', label: 'AI MATURITY',
    title: 'Two tracks — don’t confuse them',
    body: `<div>
      <div style="display:flex;gap:0.9em;align-items:stretch">
        ${[
          ['Predictive · quiet ML','Predictive NBA','#E5EBFF','#3367FF','#1F3A8A',
            ['Ranks the next best action, per client','Flags risk and opportunity early','Quiet, cheap ML — runs at scale'],
            'Morgan Stanley: advisor NBA since ~2018'],
          ['Generative · language','Generative copilots','#F3F6F9','#041326','#3A4654',
            ['Drafts the outreach, briefs the meeting','Answers “what changed?” in plain English','Powerful — token-heavy, governance-sensitive'],
            'Use it where it earns its place']
        ].map(p=>`<div style="flex:1;background:${p[2]};border-radius:0.4em;padding:1.05em 1.15em;display:flex;flex-direction:column">
          <div style="font-size:0.44em;font-weight:700;letter-spacing:0.1em;text-transform:uppercase;color:${p[3]};margin-bottom:0.3em">${p[0]}</div>
          <div style="font-size:0.82em;font-weight:700;color:#041326;margin-bottom:0.6em">${p[1]}</div>
          ${p[5].map(b=>`<div style="display:flex;gap:0.5em;align-items:flex-start;padding:0.3em 0;font-size:0.54em;color:${p[4]};line-height:1.35"><span style="color:${p[3]};font-weight:800;flex-shrink:0">•</span><span>${b}</span></div>`).join('')}
          <div style="font-size:0.48em;color:#6B7786;margin-top:auto;padding-top:0.7em;border-top:1px solid rgba(9,28,53,0.1)">${p[6]}</div>
        </div>`).join('')}
      </div>
      <div style="font-size:0.52em;font-weight:600;color:#3367FF;text-align:center;margin-top:0.8em">You need both — and you govern them differently.</div>
    </div>` },

  { layout: 'content-standard', theme: 'light', label: 'THE MATURITY MODEL',
    title: 'The Frontline Autonomy Scale',
    subtitle: 'How far does the cockpit go — from assisting the advisor to acting for them?',
    body: `<div>
      <div style="display:flex;align-items:center;gap:0.8em;padding:0 0.7em 0.4em;font-size:0.44em;font-weight:700;letter-spacing:0.08em;text-transform:uppercase;color:#6B7786">
        <span style="width:8.5em;flex-shrink:0">Level</span><span style="flex:1.5">What the AI does</span><span style="flex:1">The human</span><span style="width:7em;flex-shrink:0">Loop</span>
      </div>
      ${[
        ['A1','Assist','Answers, drafts, retrieves — on request','Does the work','In the loop','#E5EBFF','#041326'],
        ['A2','Recommend','Proactively suggests the next best action, ranked','Approves each','In the loop','#9DB8FF','#041326'],
        ['A3','Execute on approval','Completes a task end-to-end, pauses for sign-off','Approves before commit','On the loop','#5C86FF','#FFFFFF'],
        ['A4','Execute by exception','Acts within policy; escalates edge cases only','Handles exceptions','On → out','#3367FF','#FFFFFF'],
        ['A5','Self-directed','Sets sub-goals, acts and self-corrects','Sets intent &amp; guardrails','Out of loop','#041326','#FFFFFF']
      ].map(r=>`<div style="display:flex;align-items:center;gap:0.8em;padding:0.46em 0.7em;border-bottom:1px solid #EEF1F6">
        <span style="width:8.5em;flex-shrink:0;display:flex;align-items:center;gap:0.4em"><span style="background:${r[5]};color:${r[6]};font-size:0.5em;font-weight:800;padding:0.25em 0.5em;border-radius:0.25em">${r[0]}</span><span style="font-size:0.56em;font-weight:700;color:#041326">${r[1]}</span></span>
        <span style="flex:1.5;font-size:0.54em;color:#3A4654;line-height:1.3">${r[2]}</span>
        <span style="flex:1;font-size:0.54em;color:#6B7786;line-height:1.3">${r[3]}</span>
        <span style="width:7em;flex-shrink:0;font-size:0.5em;font-weight:600;color:#3367FF">${r[4]}</span>
      </div>`).join('')}
      <div style="font-size:0.46em;color:#6B7786;margin-top:0.6em;padding-left:0.7em">Climbing the scale = more autonomy · higher maturity · less human effort per outcome.</div>
    </div>` },

  { layout: 'content-standard', theme: 'light', label: 'GOVERNANCE',
    title: 'Autonomy is capped by accountability — not capability',
    body: `<div style="display:flex;align-items:center;gap:1.3em">
      <div style="width:37%;flex-shrink:0;background:#041326;border-radius:0.4em;padding:1em 1.05em">
        <div style="font-size:0.44em;font-weight:700;letter-spacing:0.1em;text-transform:uppercase;color:#69FEFF;margin-bottom:0.55em">Licence to operate</div>
        <div style="font-size:0.52em;color:rgba(255,255,255,0.82);line-height:1.5">Under FCA Consumer Duty + SM&amp;CR, the regulator wrote <b style="color:#fff">no new AI rules</b>. Human-in-the-loop, overridable and fully audited maps to them one-to-one.</div>
        <div style="font-size:0.52em;font-weight:700;color:#69FEFF;margin-top:0.6em">It’s a feature, not a limit.</div>
      </div>
      <div style="flex:1;display:flex;flex-direction:column;gap:0.45em">
        ${[
          ['Regulated advice','A named human stays accountable','A3'],
          ['Client financial actions','Within strict limits + step-up auth','A4'],
          ['Servicing &amp; operations','Where low-risk and high-volume','A4–A5'],
          ['Fraud, risk &amp; compliance','Gated at every level, always a trail','Gate']
        ].map(c=>`<div style="display:flex;align-items:center;justify-content:space-between;gap:0.8em;background:#F3F6F9;border-radius:0.25em;padding:0.6em 0.9em">
          <div><div style="font-size:0.58em;font-weight:700;color:#041326">${c[0]}</div><div style="font-size:0.48em;color:#6B7786;margin-top:0.1em">${c[1]}</div></div>
          <span style="flex-shrink:0;background:#E5EBFF;color:#3367FF;font-size:0.52em;font-weight:800;padding:0.3em 0.6em;border-radius:0.25em">${c[2]}</span>
        </div>`).join('')}
      </div>
    </div>` },

  { layout: 'content-columns', label: 'OUTSIDE-IN · MARKET SIGNALS', title: 'Already happening — at scale', columns: [
    { subtitle: 'Morgan Stanley', body: 'ML “Next Best Action” for advisors since ~2018 — plus GenAI copilots (Assistant, Debrief) for retrieval and meeting notes. The clean two-track split.' },
    { subtitle: 'CommBank', body: 'Customer Engagement Engine: ~1,000 ML models making ~55m next-best decisions a day. NBA at industrial scale.' },
    { subtitle: 'DBS', body: 'Hyper-personalised nudges off a ~15,000-data-point single client view.' },
    { subtitle: 'RBC · NOMI', body: 'Predictive nudges in the hands of millions — proof the pattern generalises beyond wealth.' }
  ]},

  { layout: 'statement', accent: 'blue', label: 'THE REALITY CHECK',
    text: 'Only about <span class="hl">one in six</span> advisor “AI” use cases truly need bespoke AI. The rest is shared truth, governance and orchestration — <span class="hl">the control plane underneath</span>.' },

  /* ═══ 04 · BACKBASE TODAY ══════════════════════════════════ */
  { layout: 'chapter-numbered', theme: 'blue', number: '04', label: 'HOW WE BUILD IT',
    title: 'The cockpit on Backbase',
    subtitle: 'The advisor’s window into a unified frontline.' },

  { layout: 'statement', variant: 'dark', accent: 'blue', label: 'THE SHIFT',
    text: 'The next decade won’t be won on better channels. It’ll be won on better <span class="hl">operating models</span>.' },

  { layout: 'content-standard', theme: 'light', label: 'THE FOUNDATION',
    title: 'Banking OS — the control plane',
    subtitle: 'One shared truth and one execution engine, beneath the cockpit.',
    body: `<div>
      <div style="display:flex;gap:0.8em;align-items:stretch">
        <div style="flex:1;background:#041326;border-radius:0.4em;padding:1em 1.1em">
          <div style="font-size:0.44em;font-weight:700;letter-spacing:0.12em;text-transform:uppercase;color:#69FEFF;margin-bottom:0.4em">Understand</div>
          <div style="font-size:0.72em;font-weight:700;color:#fff;margin-bottom:0.35em">Nexus — shared client truth</div>
          <div style="font-size:0.5em;color:rgba(255,255,255,0.75);line-height:1.5">Links core, portfolio, CRM, documents and interactions into one real-time client truth. The system of truth — not another data lake.</div>
        </div>
        <div style="flex:1;background:#041326;border-radius:0.4em;padding:1em 1.1em">
          <div style="font-size:0.44em;font-weight:700;letter-spacing:0.12em;text-transform:uppercase;color:#69FEFF;margin-bottom:0.4em">Authorize</div>
          <div style="font-size:0.72em;font-weight:700;color:#fff;margin-bottom:0.35em">Sentinel — governed execution</div>
          <div style="font-size:0.5em;color:rgba(255,255,255,0.75);line-height:1.5">Who may decide, under which rules, with which entitlements. Authority spectrum: recommend → approve → execute. Every action audited.</div>
        </div>
      </div>
      <div style="font-size:0.48em;color:#6B7786;margin-top:0.7em;text-align:center">Add-on-top, no rip-and-replace · Orchestration · Integration · Intelligence — across hundreds of downstream systems.</div>
    </div>` },

  { layout: 'content-columns', label: 'DIGITAL ASSIST · THE RM WORKSPACE', title: 'What the advisor sees', columns: [
    { subtitle: 'Client 360', body: 'One truth from every system — portfolio, cash, risk, documents and recent conversations. Powered by Nexus.' },
    { subtitle: 'Smart Signals', body: 'Proactive next-best-actions, ranked. The growth and retention nudges — Relationship Intelligence.' },
    { subtitle: 'Needs attention', body: 'Notifications, tasks and alerts in one place. Compliance gates always surface.' },
    { subtitle: 'Agents in-line', body: 'Meeting Prep, Market Move Explainer, Personalised Outreach — at the advisor’s elbow.' }
  ]},

  { layout: 'content-standard', theme: 'light', label: 'THE MECHANIC',
    title: 'From signal to next-best-action',
    subtitle: 'And the make-or-break in the middle: prioritisation.',
    body: `<div>
      <div style="display:flex;align-items:stretch;gap:0.35em">
        ${[
          ['Signal source','3rd-party · rule-based · agentic',false],
          ['NBA framework','rank &amp; filter · the make-or-break',true],
          ['The cockpit','surface to the advisor',false],
          ['Next-best-action','surface · task · agent',false]
        ].map((n,idx,a)=>`<div style="flex:1;background:${n[2]?'#3367FF':'#F3F6F9'};border-radius:0.3em;padding:0.75em 0.55em;text-align:center;display:flex;flex-direction:column;justify-content:center">
            <div style="font-size:0.58em;font-weight:700;color:${n[2]?'#fff':'#041326'}">${n[0]}</div>
            <div style="font-size:0.44em;color:${n[2]?'rgba(255,255,255,0.85)':'#6B7786'};margin-top:0.2em;line-height:1.3">${n[1]}</div>
          </div>${idx<a.length-1?'<div style="display:flex;align-items:center;font-size:0.85em;font-weight:800;color:#3367FF">›</div>':''}`).join('')}
      </div>
      <div style="display:flex;align-items:center;justify-content:space-between;gap:0.8em;background:#041326;border-radius:0.3em;padding:0.6em 0.95em;margin-top:0.7em">
        <span style="font-size:0.5em;color:rgba(255,255,255,0.82)">Governed by <b style="color:#fff">Sentinel</b> — every step authorised and audited.</span>
        <span style="flex-shrink:0;font-size:0.5em;font-weight:800;color:#69FEFF">~2,000 signals / RM / month — prioritisation is the ROI</span>
      </div>
    </div>` },

  { layout: 'content-columns', label: 'OUR STANCE', title: 'Buy the plane. Bring the intelligence.', columns: [
    { subtitle: 'Buy the control plane', body: 'Rebuilding the agentic fabric in-house is a multi-year, ~50-FTE programme. Buy it — and start now.' },
    { subtitle: 'Bring your intelligence', body: 'Your data and your rule-book are the edge — not the plumbing. Start rule-based; graduate to models as the data earns it.' },
    { subtitle: 'Configure, don’t rebuild', body: 'One component library, themed per segment in config — so your “touch” survives every upgrade.' }
  ]},

  { layout: 'content-columns', label: 'THE PRIZE', title: 'Where the value lands', columns: [
    { subtitle: 'Lower cost-to-serve', body: '<div style="font-size:2.6em;font-weight:800;color:#3367FF;line-height:1">20–40%</div><div style="margin-top:0.4em">Front-to-back resolution — less swivel-chair work.</div>' },
    { subtitle: 'Growth &amp; retention', body: '<div style="font-size:2.6em;font-weight:800;color:#3367FF;line-height:1">10–25%</div><div style="margin-top:0.4em">Higher conversion, cross-sell and retention from timely advice.</div>' },
    { subtitle: 'AI to production', body: '<div style="font-size:2.6em;font-weight:800;color:#3367FF;line-height:1">3–5×</div><div style="margin-top:0.4em">Faster from pilot to production, on one governed platform.</div>' }
  ]},

  { layout: 'statement-stat', accent: 'blue', label: 'PROOF', stat: '120+',
    text: 'banks already run on Backbase. Analysts call the platform <span class="hl">“light years ahead of traditional banking vendors.”</span>',
    source: 'Gartner; Backbase, 2026' },

  { layout: 'statement', variant: 'dark', accent: 'blue', label: 'THE GOAL',
    text: 'Put advisors back in the <span class="hl">driver’s seat</span> — equipped to lead the relationship, not just log into it.' },

  { layout: 'content-columns', label: 'WHERE TO START', title: 'Start small. Prove fast. Expand.', columns: [
    { subtitle: 'Ignite (light)', body: 'Our consultants and your senior bankers pick one high-ROI, low-risk use case.' },
    { subtitle: 'Mission Sprint', body: 'Specify and prototype it live — in 6–12 weeks, on the real platform.' },
    { subtitle: 'Land &amp; expand', body: 'Prove the value, then light up the next use case on the same Banking OS.' }
  ]},

  { layout: 'thank-you' }

];

const SPEAKER_NOTES = {
  1: 'Frame: this is our point of view on the advisor/RM cockpit and on AI maturity. ~15–20 min. Three questions: what does good look like, where is it going, and how do we build it. Thesis in one line — the cockpit must move from a dashboard that shows, to a decision engine that acts (within guardrails).',
  3: 'Start with empathy for the advisor. The tool they have today is a rear-view mirror. Everything proactive still depends on the advisor remembering, hunting, and stitching systems together.',
  4: 'Walk the four symptoms. The left box is the tax: 6–12 systems, 30–60% manual, no single client truth. The point: the advisor is the integration layer — that’s the waste.',
  5: 'The killer number: ~60% of the work lives between systems, in the handoffs and exceptions. No dashboard reaches it because a dashboard reads systems — it doesn’t coordinate across them.',
  6: 'The wedge. This reframes “we’re already doing AI.” AI on a fragmented desk automates chaos. You need the operating model underneath first. Pause here.',
  8: 'These six are the scorecard for any advisor cockpit — the bank’s or a vendor’s. Note 4 and 5: advisory-led and governed. In wealth, that’s non-negotiable.',
  9: 'The signature contrast. Read it left to right. “Dashboard” is the verb “show.” “Decision engine” is the verb “act.” Equal weight, deliberately — same screen, opposite behaviour.',
  10: 'Pivot from “what good looks like” to “where it’s going.” AI maturity is the spine of the next three slides.',
  11: 'Most important clarification in the AI conversation. Predictive NBA is quiet, cheap ML — ranking. Generative is the loud, token-heavy, governance-sensitive part. Banks conflate them and either over-spend on LLMs or under-invest in decisioning. You need both, governed differently.',
  12: 'The centrepiece. Our Frontline Autonomy Scale — a single ladder that doubles as a maturity model. As you climb: more autonomy, higher maturity, less human effort per outcome. The human moves from in-the-loop to on-the-loop to out. Use this to place any agent or any roadmap.',
  13: 'The counter-intuitive point execs love: you don’t go to A5 everywhere. The ceiling is set by accountability and harm, not by what’s technically possible. And capping advice at A3 is exactly the architecture FCA/SM&CR already reward. Governance as a selling point, not a tax.',
  14: 'Proof it’s not theory — cite, don’t claim. Morgan Stanley is the clean two-track example. CommBank is the scale example. The recurring lesson: value lives in the single client view and the governance, not in the model itself.',
  15: 'The myth-buster. ~1 in 6 use cases need bespoke AI. The rest is the control plane. This is the bridge into how we build it.',
  16: 'Now — how Backbase presents this today. Keep it product-true but CEO-level.',
  17: 'Our thesis in one line. Lead with the operating model, not channels. Everything else hangs off this.',
  18: 'Banking OS is the control plane beneath the cockpit. Name two layers only: Nexus (shared truth) and Sentinel (governed execution). Add-on-top, no rip-and-replace — critical for incumbents.',
  19: 'The cockpit itself — Digital Assist, the RM workspace. Four surfaces. Each maps to the architecture: Client 360 = Nexus, Smart Signals = Relationship Intelligence, alerts = Sentinel gates, agents = Factory missions.',
  20: 'The product mechanic. The middle box — the NBA framework that ranks and filters — is the make-or-break. ~2,000 signals per RM per month means prioritisation IS the ROI. The whole flow is governed by Sentinel.',
  21: 'Our build-vs-buy stance. Buy the plane; bring your own intelligence and context. Configure, don’t rebuild — the single biggest upgrade-risk lever for an incumbent.',
  22: 'The three value pools — ranges, bank-size dependent, sized in Ignite. No off-the-shelf ROI; we size it on your book. Keep it outcomes-first.',
  23: 'Credibility beat. 120+ banks live; the analyst line is attributed, not claimed.',
  24: 'Land the close. From dashboard to decision engine — governed, on one shared truth. Advisors in the driver’s seat.',
  25: 'Soft CTA. Low-risk way in: Ignite → a Mission Sprint → live in 6–12 weeks → land and expand. Invite the one-use-case conversation.'
};
