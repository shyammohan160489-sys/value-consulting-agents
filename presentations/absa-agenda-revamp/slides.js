window.BB_SHARED_ASSETS = '../backbase-slides-app';

const SPEAKER_NOTES = {
  // PART 1: COMPARISON
  1: 'This deck has two parts. Part 1: How we reframe ABSA\'s agenda. Part 2: The actual content for each intervention. Share this with the team to align on structure AND substance.',
  2: 'The key principle. Don\'t change WHAT they asked for. Change HOW we deliver it.',
  3: 'Walk the team through: left = what every vendor does. Right = what we do. Same timing, different impact.',
  4: 'Opening: Shyam\'s 5-min ABSA Story is the single biggest differentiation. No other vendor opens with the client\'s world.',
  5: 'Item 1: 6 bullets covered. "Culture demonstration" elevated from a values slide into ABSA-specific market analysis.',
  6: 'Item 2: 8 bullets covered. Risks elevated (Jesse). Demo portal reveal (Jesse). Contingency via CS.',
  7: 'Item 3: straightforward. Thijs + Ruben. Delivery OS is the competitive add.',
  8: 'Item 4: TONED DOWN per Ronnie. Executive-level view only. No negotiation. Investment Logic card as context, not a pitch. Quote Ronnie if challenged.',
  9: 'Item 5: culture demo appears in Items 1 AND 5. Our answer: co-create the scorecard live. Shyam / CS.',
  10: '34 bullets covered. +5 strategic adds. ~41 min of value consulting stage time.',
  11: 'NEW: Ronnie\'s exact words. "How will ABSA be better off?" Three themes: leadership accountability, operational resilience, executive alignment. These now tag each intervention chapter.',
  12: 'Transition. Content is backup — keep it conversational per Matthijs. Use selectively.',
  // PART 2: TOOLKIT
  12: 'INTERVENTION 1: The ABSA Story. TALKING TRACK — not slides. Speaker notes are the script. Eye contact. No deck on screen.',
  13: 'Beat 1: Let each number land. Pause after "300,000 customers a year." All from ABSA 2025 Annual Report.',
  14: 'Beat 2: Emotional — "the window is now." Kenny Fihla\'s public commitment. New PPB division.',
  16: 'Beat 3: NOW uses Ronnie\'s phrase "when it matters most." Plant the scorecard seed. Don\'t elaborate.',
  16: 'INTERVENTION 2: Strategic Fit. Earn the right to advise. Every data point sourced from ABSA\'s own numbers.',
  17: '5 problems — not features. Each maps to ABSA\'s own annual report and CEO statements. Note the PHASE BADGES on each card.',
  18: 'NEW SLIDE: Problem-by-Problem mapping table. This is the killer slide — it connects each problem to a specific Backbase capability, a phase, and a measurable outcome. The blue-highlighted Backbase column is the visual anchor.',
  19: 'Value at stake BY PHASE. Each phase delivers measurable value before the next begins. The 3-column structure mirrors the phase model ABSA\'s team already loves.',
  19: 'INTERVENTION 3: Risk Register. Tone is HONEST. "We\'re not pretending this is easy." Name their specific systems.',
  20: '3 risks. Each with a concrete mitigation grounded in their own environment.',
  21: 'INTERVENTION 4: Investment Logic. Frame €32M not as cost but as investment with 11.5x return.',
  22: 'The card. Print it. Hand it to Christopher Snyman. "This is yours for the board."',
  23: 'INTERVENTION 5: Joint Scorecard. THE signature move. Print copies. Have on screen. Invite live editing.',
  24: 'Amber columns are intentionally blank — the invitation for ABSA to fill in targets.',
  25: 'ABOVE AND BEYOND — 3 extras no other vendor brings.',
  26: 'ABSA 2028 Vision. What headlines could be written. Aspirational but grounded in platform capabilities.',
  27: 'The provocation. Make them feel the urgency.',
  29: 'NEW SLIDE: Detailed 5-row comparison table from exec summary. Integration, Time to Value, Africa Track Record, Platform Breadth, Enterprise Readiness. Backbase column highlighted with blue border. Much richer than the old 3-card version.',
  30: 'NEW SLIDE: Enterprise at Scale — stats bar (100+, 5 continents, 60+ OOTB, 6 Mo, 24/7) + 4 capability cards. The proof behind the claim.',
  31: 'Leave-behind: outside-in doc + demo portal + CFO card. Something for the Group CEO and board.',
  32: 'The closing line. They asked for a vendor visit. We gave them a partnership preview.',
};

/* ── Helpers (from comparison deck) ── */
function compRow(asked, approach, who, isAdd) {
  const leftBg = isAdd ? 'background:rgba(51,102,255,0.04);' : '';
  const icon = isAdd ? '<span style="color:#3366FF;font-weight:900;font-size:10px">+ ELEVATED</span>' : '<span style="color:#059669;font-weight:900;font-size:10px">\u2713 COVERED</span>';
  return `<div style="display:flex;gap:0;width:100%;border-bottom:1px solid #E2E8F0;${leftBg}">
    <div style="flex:1;padding:8px 12px;border-right:1px solid #E2E8F0"><div style="font-size:9px;color:#64748B;line-height:1.5">${asked}</div></div>
    <div style="flex:1.3;padding:8px 12px;border-right:1px solid #E2E8F0"><div style="font-size:9px;color:#091C35;line-height:1.5;font-weight:${isAdd ? '700' : '500'}">${approach}</div></div>
    <div style="min-width:70px;padding:8px 10px;border-right:1px solid #E2E8F0;font-size:9px;font-weight:700;color:#091C35">${who}</div>
    <div style="min-width:80px;padding:8px 10px;display:flex;align-items:center;justify-content:center">${icon}</div>
  </div>`;
}
function tableHeader() {
  return `<div style="display:flex;gap:0;width:100%;background:#091C35;border-radius:8px 8px 0 0">
    <div style="flex:1;padding:8px 12px;border-right:1px solid rgba(255,255,255,0.1)"><div style="font-size:8px;font-weight:800;color:rgba(255,255,255,0.5);letter-spacing:1px;text-transform:uppercase">What ABSA Asked</div></div>
    <div style="flex:1.3;padding:8px 12px;border-right:1px solid rgba(255,255,255,0.1)"><div style="font-size:8px;font-weight:800;color:#3366FF;letter-spacing:1px;text-transform:uppercase">Our Approach</div></div>
    <div style="min-width:70px;padding:8px 10px;border-right:1px solid rgba(255,255,255,0.1)"><div style="font-size:8px;font-weight:800;color:rgba(255,255,255,0.5);letter-spacing:1px;text-transform:uppercase">Who</div></div>
    <div style="min-width:80px;padding:8px 10px"><div style="font-size:8px;font-weight:800;color:rgba(255,255,255,0.5);letter-spacing:1px;text-transform:uppercase">Status</div></div>
  </div>`;
}

const SLIDES = [

  // ════════════════════════════════════════════════════════════════
  // COVER
  // ════════════════════════════════════════════════════════════════
  { layout: 'cover-color-block', label: 'ABSA \u00d7 BACKBASE', title: 'Agenda\nRevamp', date: 'Amsterdam \u2014 Internal \u2014 May 2026' },

  // ════════════════════════════════════════════════════════════════
  // PART 1: COMPARISON (slides 2-11)
  // ════════════════════════════════════════════════════════════════
  { layout: 'statement', variant: 'dark', label: 'THE PRINCIPLE',
    text: 'We don\u2019t change <span class="hl">what</span> ABSA asked for. We change <span class="hl">how</span> we deliver it. Every bullet point covered. One story with a golden thread.' },

  { layout: 'content-standard', theme: 'light', label: 'STRUCTURE COMPARISON', title: 'Same 5 Items, Different Impact', subtitle: 'Left: what every vendor will do. Right: what we will do.', body: `
    <div style="display:flex;gap:20px;width:100%;margin-top:8px">
      <div style="flex:1">
        <div style="font-size:9px;font-weight:800;letter-spacing:2px;color:#DC2626;margin-bottom:10px;text-transform:uppercase">What Every Vendor Will Do</div>
        <div style="display:flex;flex-direction:column;gap:6px">
          <div style="padding:10px 14px;background:rgba(220,38,38,0.04);border:1px solid rgba(220,38,38,0.12);border-radius:8px;font-size:10px;color:#64748B">Opening: round-table introductions + corporate overview deck</div>
          <div style="padding:10px 14px;background:rgba(220,38,38,0.04);border:1px solid rgba(220,38,38,0.12);border-radius:8px;font-size:10px;color:#64748B">Item 1: revenue slide, R&D %, generic roadmap</div>
          <div style="padding:10px 14px;background:rgba(220,38,38,0.04);border:1px solid rgba(220,38,38,0.12);border-radius:8px;font-size:10px;color:#64748B">Item 2: methodology deck, generic risk matrix, timeline</div>
          <div style="padding:10px 14px;background:rgba(220,38,38,0.04);border:1px solid rgba(220,38,38,0.12);border-radius:8px;font-size:10px;color:#64748B">Item 3: support tiers, SLA numbers, training catalogue</div>
          <div style="padding:10px 14px;background:rgba(220,38,38,0.04);border:1px solid rgba(220,38,38,0.12);border-radius:8px;font-size:10px;color:#64748B">Item 4: price table, license model, T&Cs</div>
          <div style="padding:10px 14px;background:rgba(220,38,38,0.04);border:1px solid rgba(220,38,38,0.12);border-radius:8px;font-size:10px;color:#64748B">Item 5: partnership values slide, governance org chart</div>
        </div>
        <div style="margin-top:10px;padding:8px 12px;background:rgba(220,38,38,0.06);border-radius:6px;font-size:9px;color:#DC2626;font-weight:700;text-align:center">6 disconnected presentations. No story. Forgettable.</div>
      </div>
      <div style="flex:1">
        <div style="font-size:9px;font-weight:800;letter-spacing:2px;color:#3366FF;margin-bottom:10px;text-transform:uppercase">What We Will Do</div>
        <div style="display:flex;flex-direction:column;gap:6px">
          <div style="padding:10px 14px;background:rgba(51,102,255,0.04);border:1px solid rgba(51,102,255,0.15);border-radius:8px;font-size:10px;color:#091C35;font-weight:600">Act 1 \u201cWe See You\u201d: open with THEIR story, not ours</div>
          <div style="padding:10px 14px;background:rgba(51,102,255,0.04);border:1px solid rgba(51,102,255,0.15);border-radius:8px;font-size:10px;color:#091C35;font-weight:600">Act 2 \u201cWe\u2019ve Already Started\u201d: 5 problems + value at stake</div>
          <div style="padding:10px 14px;background:rgba(51,102,255,0.04);border:1px solid rgba(51,102,255,0.15);border-radius:8px;font-size:10px;color:#091C35;font-weight:600">Act 3 \u201cWe Know How\u201d: risks + demo portal + Delivery OS</div>
          <div style="padding:10px 14px;background:rgba(51,102,255,0.04);border:1px solid rgba(51,102,255,0.15);border-radius:8px;font-size:10px;color:#091C35;font-weight:600">Act 3b: Digital Factory + support. Operational reality.</div>
          <div style="padding:10px 14px;background:rgba(51,102,255,0.04);border:1px solid rgba(51,102,255,0.15);border-radius:8px;font-size:10px;color:#091C35;font-weight:600">Act 4 \u201cIt Makes Sense\u201d: pricing + Investment Logic card</div>
          <div style="padding:10px 14px;background:rgba(51,102,255,0.04);border:1px solid rgba(51,102,255,0.15);border-radius:8px;font-size:10px;color:#091C35;font-weight:600">Act 5 \u201cLet\u2019s Build This\u201d: scorecard co-creation</div>
        </div>
        <div style="margin-top:10px;padding:8px 12px;background:rgba(51,102,255,0.06);border-radius:6px;font-size:9px;color:#3366FF;font-weight:700;text-align:center">1 story. 5 acts. Golden thread. Unforgettable.</div>
      </div>
    </div>
  `, bodyFull: true },

  // OPENING
  { layout: 'content-standard', theme: 'light', label: 'OPENING \u00b7 10 MIN', title: 'Opening & Welcome', subtitle: 'ABSA asked for introductions. We open with their story.', body:
    tableHeader() + `<div style="border:1px solid #E2E8F0;border-top:0;border-radius:0 0 8px 8px;overflow:hidden">` +
    compRow('Absa Team introduction', 'Subash introduces the ABSA delegation', 'Subash', false) +
    compRow('Vendor Team introduction', 'Aymen: brief round-table. Name, role, one sentence. <strong>No corporate history.</strong>', 'Aymen', false) +
    compRow('<em>(not asked for)</em>', '<strong>\u201cThe ABSA Story\u201d \u2014 3 Beats.</strong> R115.7bn revenue, 300K customer bleed, NPS 15% vs Capitec 45%, C/I 53.8%. <em>No slides. Eye contact. 5 min.</em>', '<strong>Shyam</strong>', true) +
    `</div><div style="margin-top:10px;padding:10px 14px;border-radius:8px;border-left:3px solid #3366FF;background:rgba(51,102,255,0.04);font-size:10px;color:#091C35;line-height:1.6"><strong style="color:#3366FF">Why this matters:</strong> Every other vendor opens with \u201cHi, I\u2019m X from Company Y.\u201d We open with \u201cHere\u2019s what we see when we look at ABSA.\u201d <strong>The tone is set in these 5 minutes.</strong></div>`
  , bodyFull: true },

  // ITEM 1
  { layout: 'content-standard', theme: 'light', label: 'ITEM 1 \u00b7 30 MIN', title: 'Strategic Alignment', subtitle: '6 bullet points. All covered. \u201cCulture demonstration\u201d elevated.', body:
    tableHeader() + `<div style="border:1px solid #E2E8F0;border-top:0;border-radius:0 0 8px 8px;overflow:hidden">` +
    compRow('Absa Digital Transformation Strategy', 'Subash presents. We <strong>listen deeply</strong>.', 'Subash', false) +
    compRow('Company background, ownership, financial health', 'Privately held. No acquisition risk. 20+ years.', 'Aymen', false) +
    compRow('Revenue, growth trajectory, profitability', 'Corporate overview. 3\u20134 slides.', 'Aymen', false) +
    compRow('R&D investment, 12-month+ roadmap', 'Level 1\u21922\u21923. Banking OS. Agentic Platform.', 'Ruben', false) +
    compRow('Long-term viability and exit risk', '\u201cWe don\u2019t need to be acquired.\u201d', 'Aymen', false) +
    compRow('Demonstration of culture', '<strong>5 problems + value at stake using ABSA\u2019s own numbers.</strong> Culture = understanding their world.', '<strong>Shyam</strong>', true) +
    `</div><div style="margin-top:10px;padding:10px 14px;border-radius:8px;border-left:3px solid #3366FF;background:rgba(51,102,255,0.04);font-size:10px;color:#091C35;line-height:1.6"><strong style="color:#3366FF">The reframe:</strong> Most vendors show a values slide. <strong>We demonstrate culture by mirroring their strategy back with more depth than expected.</strong></div>`
  , bodyFull: true },

  // ITEM 2
  { layout: 'content-standard', theme: 'light', label: 'ITEM 2 \u00b7 30 MIN', title: 'Implementation & Risk', subtitle: '8 bullets covered. Risks elevated. Demo portal added.', body:
    tableHeader() + `<div style="border:1px solid #E2E8F0;border-top:0;border-radius:0 0 8px 8px;overflow:hidden">` +
    compRow('Implementation methodology', 'Phased. Phase 1: 6\u20139 months. MCB: 6 months. 80% OOTB.', 'Thijs', false) +
    compRow('Go-live timeline and milestones', 'Timeline visual. Y0 = setup. Y1 = go-live + upgrade.', 'Thijs', false) +
    compRow('Resource requirements', 'Joint BB + EY + ABSA. Specific FTE ask per phase.', 'Thijs', false) +
    compRow('Change management', 'EY as local change partner. 70+ practitioners.', 'Marius', false) +
    compRow('Ability to pivot', 'Digital Factory = built for pivoting. No lock-in.', 'Thijs', false) +
    compRow('3 main risks', '<strong>ABSA-specific:</strong> (1) Co-existence (2) Adoption (3) Scope creep. Each with specific mitigation.', '<strong>Jesse</strong>', true) +
    compRow('Contingency planning', 'Phase-gated with value checkpoints. ROI proven before next phase.', '<strong>CS</strong>', true) +
    compRow('AI/automation', 'Delivery OS. Moved to Item 3.', 'Ruben', false) +
    compRow('<em>(not asked for)</em>', '<strong>Demo portal reveal.</strong> Localized app, 4 months with the bank.', '<strong>Jesse</strong>', true) +
    `</div>`
  , bodyFull: true },

  // ITEM 3
  { layout: 'content-standard', theme: 'light', label: 'ITEM 3 \u00b7 30 MIN', title: 'Ways of Work & Support', subtitle: '7 bullets. Thijs + Ruben. Delivery OS is the add.', body:
    tableHeader() + `<div style="border:1px solid #E2E8F0;border-top:0;border-radius:0 0 8px 8px;overflow:hidden">` +
    compRow('Support tiers and response times', '24/7 follow-the-sun. P1: 1hr. Hypercare 14-day.', 'Ruben', false) +
    compRow('Account management and escalation', 'One entry point \u2192 4 support areas.', 'Ruben', false) +
    compRow('Training and knowledge transfer', '\u201cTurbocharge \u2192 Train \u2192 Handover \u2192 Independent.\u201d', 'Thijs', false) +
    compRow('SI ecosystem and self-service', 'EY primary SI. Backbase.io. Partner ecosystem.', 'Thijs', false) +
    compRow('Outage controls', 'SOC 2. Multi-zone. Datadog. Managed Azure.', 'Ruben', false) +
    compRow('Upgrades and version management', 'Assess \u2192 Plan \u2192 Validate \u2192 Test \u2192 Deploy.', 'Ruben', false) +
    compRow('AI/automation', '<strong>Delivery OS demo.</strong> AI agents across SDLC. 30% efficiency.', 'Ruben', true) +
    `</div><div style="margin-top:10px;padding:10px 14px;border-radius:8px;border-left:3px solid #059669;background:rgba(5,150,105,0.04);font-size:10px;color:#091C35;line-height:1.6"><strong style="color:#059669">Delivery OS</strong> is a differentiator Intellect and Plumery can\u2019t match.</div>`
  , bodyFull: true },

  // ITEM 4 — TONED DOWN per Ronnie's email: "concise executive-level view, not to negotiate"
  { layout: 'content-standard', theme: 'light', label: 'ITEM 4 \u00b7 30 MIN', title: 'Pricing & Contracting', subtitle: 'Executive-level view. Ronnie: \u201cNot to negotiate, but to understand.\u201d Keep concise.', body:
    tableHeader() + `<div style="border:1px solid #E2E8F0;border-top:0;border-radius:0 0 8px 8px;overflow:hidden">` +
    compRow('Licensing model', 'Subscription + usage-based. Pay-as-you-grow. Phase-gated activation.', 'Aymen', false) +
    compRow('Implementation costs', 'High-level overview. Details already shared in RFP response.', 'Aymen', false) +
    compRow('Multi-year pricing', '5-year model. Per-user cost decreases at scale.', 'Aymen', false) +
    compRow('Contractual protections', 'Concise overview. IP, data portability, termination. Detail for later.', 'Aymen', false) +
    compRow('SLA commitments', 'P1: 1hr. 99.9% uptime. Service credits for breach.', 'Aymen', false) +
    compRow('<em>(not asked for)</em>', '<strong>Investment Logic card.</strong> Executive-level: total investment vs total value created. One page for context.', '<strong>Shyam</strong>', true) +
    `</div><div style="margin-top:10px;padding:10px 14px;border-radius:8px;border-left:3px solid #D97706;background:rgba(217,119,6,0.04);font-size:10px;color:#091C35;line-height:1.6"><strong style="color:#D97706">Ronnie\u2019s guidance:</strong> \u201cWe are not looking to spend limited time in detailed discussion. A concise executive-level view is more than adequate. The focus is not to negotiate.\u201d <strong>Keep this section tight.</strong></div>`
  , bodyFull: true },

  // ITEM 5
  { layout: 'content-standard', theme: 'light', label: 'ITEM 5 \u00b7 30 MIN', title: 'Partnership Model', subtitle: '\u201cCulture demonstration\u201d = the most important bullet. Actions > slides.', body:
    tableHeader() + `<div style="border:1px solid #E2E8F0;border-top:0;border-radius:0 0 8px 8px;overflow:hidden">` +
    compRow('Strategic vs transactional', 'Transformation partnership. Exec sponsor. QBRs.', 'Aymen', false) +
    compRow('Executive sponsorship', 'Joint steering committee with KPIs.', 'Aymen', false) +
    compRow('Joint success metrics', '<strong>Live co-creation.</strong> 8 metrics. Amber columns = ABSA\u2019s targets.', '<strong>Shyam / CS</strong>', true) +
    compRow('Commitment to success', 'Demo portal, Ignite model, MCB rollout.', 'Aymen', false) +
    compRow('Culture demonstration', '<strong>The scorecard IS the culture demo.</strong> Co-create an artifact. Actions > slides.', '<strong>Shyam / CS</strong>', true) +
    `</div><div style="margin-top:10px;padding:10px 14px;border-radius:8px;border-left:3px solid #7B2FFF;background:rgba(123,47,255,0.04);font-size:10px;color:#091C35;line-height:1.6"><strong style="color:#7B2FFF">Why this wins:</strong> \u201cCulture\u201d appears in Items 1 AND 5. <strong>We demonstrate it by co-creating in the room.</strong></div>`
  , bodyFull: true },

  // COMPARISON SUMMARY
  { layout: 'content-standard', theme: 'light', label: 'THE BOTTOM LINE', title: '100% Coverage + 5 Strategic Adds', subtitle: 'Every ABSA bullet covered. Plus 5 things no other vendor brings.', body: `
    <div style="display:flex;gap:16px;width:100%">
      <div style="flex:1">
        <div style="font-size:9px;font-weight:800;letter-spacing:2px;color:#3366FF;margin-bottom:10px">THE 5 STRATEGIC ADDS</div>
        <div style="display:flex;flex-direction:column;gap:5px">
          <div style="display:flex;gap:10px;align-items:center;padding:8px 12px;background:#F0F4F8;border-radius:8px;border-left:3px solid #091C35"><div style="font-size:16px;font-weight:900;color:#091C35;min-width:18px">1</div><div><div style="font-weight:800;font-size:10px">\u201cThe ABSA Story\u201d</div><div style="font-size:8px;color:#64748B">5 min. Their world, not ours.</div></div></div>
          <div style="display:flex;gap:10px;align-items:center;padding:8px 12px;background:#F0F4F8;border-radius:8px;border-left:3px solid #3366FF"><div style="font-size:16px;font-weight:900;color:#3366FF;min-width:18px">2</div><div><div style="font-weight:800;font-size:10px">Strategic fit analysis</div><div style="font-size:8px;color:#64748B">10 min. 5 problems + value at stake.</div></div></div>
          <div style="display:flex;gap:10px;align-items:center;padding:8px 12px;background:#F0F4F8;border-radius:8px;border-left:3px solid #059669"><div style="font-size:16px;font-weight:900;color:#059669;min-width:18px">3</div><div><div style="font-weight:800;font-size:10px">ABSA-specific risks</div><div style="font-size:8px;color:#64748B">8 min. Not generic. Their systems.</div></div></div>
          <div style="display:flex;gap:10px;align-items:center;padding:8px 12px;background:#F0F4F8;border-radius:8px;border-left:3px solid #D97706"><div style="font-size:16px;font-weight:900;color:#D97706;min-width:18px">4</div><div><div style="font-weight:800;font-size:10px">CFO Investment Logic</div><div style="font-size:8px;color:#64748B">8 min. R618M vs R7.1bn = 11.5x.</div></div></div>
          <div style="display:flex;gap:10px;align-items:center;padding:8px 12px;background:#F0F4F8;border-radius:8px;border-left:3px solid #7B2FFF"><div style="font-size:16px;font-weight:900;color:#7B2FFF;min-width:18px">5</div><div><div style="font-weight:800;font-size:10px">Scorecard co-creation</div><div style="font-size:8px;color:#64748B">10 min. Culture in action.</div></div></div>
        </div>
      </div>
      <div style="flex:0.6">
        <div style="padding:16px;background:#091C35;border-radius:10px;color:#fff;margin-bottom:10px">
          <div style="font-size:28px;font-weight:900;color:#3366FF">34</div><div style="font-size:8px;color:rgba(255,255,255,0.4)">ABSA bullets covered</div>
          <div style="font-size:28px;font-weight:900;color:#7B2FFF;margin-top:10px">+5</div><div style="font-size:8px;color:rgba(255,255,255,0.4)">strategic adds</div>
        </div>
        <div style="padding:10px;border:2px solid rgba(51,102,255,0.2);border-radius:10px;text-align:center">
          <div style="font-size:8px;font-weight:800;color:#3366FF;letter-spacing:1px">STAGE TIME</div>
          <div style="font-size:24px;font-weight:900">~41 min</div>
          <div style="font-size:8px;color:#64748B">of 160 (26%)</div>
        </div>
      </div>
    </div>
  `, bodyFull: true },

  // ════════════════════════════════════════════════════════════════
  // TRANSITION TO TOOLKIT
  // ════════════════════════════════════════════════════════════════
  { layout: 'statement', variant: 'dark', label: 'FROM RONNIE\u2019S BRIEF',
    text: '\u201cHow will ABSA be better off, operationally and strategically, with Backbase as a long-term partner?\u201d Three themes: <span class="hl">leadership accountability, operational resilience, executive alignment.</span>' },

  { layout: 'statement', variant: 'dark', label: 'PART 2',
    text: 'That\u2019s the structure. Now here\u2019s <span class="hl">the actual content</span> for each intervention. Use selectively \u2014 not every slide is presented. Keep it conversational.' },

  // ════════════════════════════════════════════════════════════════
  // PART 2: TOOLKIT CONTENT (slides 12-30)
  // ════════════════════════════════════════════════════════════════

  // ── 01: THE ABSA STORY ──
  { layout: 'chapter-numbered', theme: 'navy', number: '01', label: 'INTERVENTION', title: '"The ABSA Story"', subtitle: '5 minutes. No slides. Eye contact. Speaker notes = your script.' },

  { layout: 'statement', variant: 'dark', label: 'BEAT 1 \u00b7 2 MIN \u2014 "WHAT WE SEE"',
    text: 'R115.7 billion in revenue. CIB at <span class="hl">21% ROE.</span> But retail losing <span class="hl">300,000 customers a year.</span> NPS 15\u2009\u2014\u200930 points behind Capitec. Cost-to-income 3 points above industry.' },

  { layout: 'statement', accent: 'blue', label: 'BEAT 2 \u00b7 2 MIN \u2014 "WHY NOW"',
    text: 'New PPB division. A CEO who <span class="hl">publicly committed</span> to retail market share. R16.7bn IT investment. The question isn\u2019t whether to transform \u2014 it\u2019s whether the <span class="hl">next decade</span> will be built on the right platform.' },

  { layout: 'statement', accent: 'blue', label: 'BEAT 3 \u00b7 1 MIN \u2014 "WHEN IT MATTERS MOST"',
    text: 'You asked us to show you how we\u2019d work together <span class="hl">when it matters most.</span> We have a view on what success looks like \u2014 digital adoption, cost-to-income, NPS. At the end of today, we\u2019d like to <span class="hl">build that scorecard with you.</span>' },

  // ── 02: STRATEGIC FIT ──
  { layout: 'chapter-numbered', theme: 'navy', number: '02', label: 'INTERVENTION \u2014 EXECUTIVE ALIGNMENT', title: 'Strategic Fit', subtitle: '10 minutes. 5 problems + value at stake. ABSA\u2019s own numbers. Addresses: executive alignment.' },

  { layout: 'content-standard', theme: 'light', label: 'FIVE CHALLENGES \u2014 MAPPED TO THE 3-PHASE ROADMAP', title: 'What We See When We Look at ABSA', subtitle: 'Each problem maps to a phase your team already validated during the RFP defense.', body: `
    <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:12px;margin-top:6px">
      <div style="border-radius:10px;padding:14px;border:1px solid rgba(220,38,38,0.15);border-top:3px solid #DC2626"><div style="display:flex;justify-content:space-between;align-items:center"><div style="font-size:8px;font-weight:800;letter-spacing:2px;color:#DC2626">P1 \u2014 CUSTOMER HEMORRHAGE</div><div style="font-size:7px;font-weight:800;color:#fff;background:#059669;padding:2px 6px;border-radius:4px">PHASE 1</div></div><div style="font-size:20px;font-weight:900;margin:4px 0">-300K/yr</div><p style="font-size:8px;color:#64748B;line-height:1.4">NPS 15% vs Capitec 45%. Onboarding friction. Self-service gaps.</p></div>
      <div style="border-radius:10px;padding:14px;border:1px solid rgba(217,119,6,0.15);border-top:3px solid #D97706"><div style="display:flex;justify-content:space-between;align-items:center"><div style="font-size:8px;font-weight:800;letter-spacing:2px;color:#D97706">P2 \u2014 CHANNEL FRAGMENTATION</div><div style="font-size:7px;font-weight:800;color:#fff;background:#059669;padding:2px 6px;border-radius:4px">PHASE 1</div></div><div style="font-size:20px;font-weight:900;margin:4px 0">Zero Continuity</div><p style="font-size:8px;color:#64748B;line-height:1.4">No save-and-resume. No 360\u00b0 view. Context lost across channels.</p></div>
      <div style="border-radius:10px;padding:14px;border:1px solid rgba(220,38,38,0.15);border-top:3px solid #DC2626"><div style="display:flex;justify-content:space-between;align-items:center"><div style="font-size:8px;font-weight:800;letter-spacing:2px;color:#DC2626">P3 \u2014 COST STRUCTURE</div><div style="font-size:7px;font-weight:800;color:#fff;background:#059669;padding:2px 6px;border-radius:4px">PHASE 1</div></div><div style="font-size:20px;font-weight:900;margin:4px 0">~R3.5bn Excess</div><p style="font-size:8px;color:#64748B;line-height:1.4">C/I 53.8% vs 50.7%. 42% not digital. Branch R150\u2013250 vs R5\u201315.</p></div>
    </div>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-top:8px">
      <div style="border-radius:10px;padding:14px;border:1px solid rgba(217,119,6,0.15);border-top:3px solid #D97706"><div style="display:flex;justify-content:space-between;align-items:center"><div style="font-size:8px;font-weight:800;letter-spacing:2px;color:#D97706">P4 \u2014 ONE-SIZE-FITS-ALL</div><div style="font-size:7px;font-weight:800;color:#fff;background:#3366FF;padding:2px 6px;border-radius:4px">PHASE 2</div></div><div style="font-size:20px;font-weight:900;margin:4px 0">9.3M = 1 Segment</div><p style="font-size:8px;color:#64748B;line-height:1.4">No tailored value props. GenZ = HNWI = sole prop. Drives attrition.</p></div>
      <div style="border-radius:10px;padding:14px;border:1px solid rgba(123,47,255,0.15);border-top:3px solid #7B2FFF"><div style="display:flex;justify-content:space-between;align-items:center"><div style="font-size:8px;font-weight:800;letter-spacing:2px;color:#7B2FFF">P5 \u2014 INNOVATION BOTTLENECK</div><div style="font-size:7px;font-weight:800;color:#fff;background:#7B2FFF;padding:2px 6px;border-radius:4px">PHASE 3</div></div><div style="font-size:20px;font-weight:900;margin:4px 0">R16.7bn \u2192 15% ROE</div><p style="font-size:8px;color:#64748B;line-height:1.4">Massive IT spend but ROE below target. Each initiative bespoke.</p></div>
    </div>
  `, bodyFull: true },

  // STRATEGIC FIT — PROBLEM BY PROBLEM TABLE
  { layout: 'content-standard', theme: 'light', label: 'STRATEGIC FIT', title: 'Why Backbase \u2014 Problem by Problem', subtitle: 'Each problem maps to a specific Backbase capability, a delivery phase, and a measurable outcome.', body: `
    <div style="border-radius:10px;overflow:hidden;border:1px solid #E2E8F0">
      <table style="width:100%;border-collapse:collapse;font-size:9px">
        <thead><tr style="background:#091C35;color:#fff;font-size:8px;font-weight:800;letter-spacing:1px;text-transform:uppercase">
          <th style="padding:8px 10px;text-align:left;width:100px">Problem</th>
          <th style="padding:8px 10px;text-align:left;width:20%">What\u2019s Broken</th>
          <th style="padding:8px 10px;text-align:left;width:26%;color:#3366FF">Backbase Answer</th>
          <th style="padding:8px 10px;text-align:center;width:50px">Phase</th>
          <th style="padding:8px 10px;text-align:left;width:22%">Expected Impact</th>
        </tr></thead>
        <tbody>
          <tr style="border-bottom:1px solid #E2E8F0">
            <td style="padding:7px 10px;font-weight:800;color:#DC2626;background:#F0F4F8">Customer Hemorrhage</td>
            <td style="padding:7px 10px;color:#64748B">Friction onboarding, poor self-service, NPS 15% vs Capitec 45%</td>
            <td style="padding:7px 10px;color:#3366FF;font-weight:600;border-left:2px solid rgba(51,102,255,0.15);background:rgba(51,102,255,0.02)">Digital Banking Premium + Onboarding STP. 60+ OOTB capabilities. Omni-channel save-and-resume.</td>
            <td style="padding:7px 10px;text-align:center"><span style="background:rgba(5,150,105,0.1);color:#059669;padding:2px 6px;border-radius:4px;font-size:7px;font-weight:800">P1</span></td>
            <td style="padding:7px 10px;color:#64748B">Adoption 58%\u219278%. Onboarding -60\u201380%. NPS +7pp Y1.</td>
          </tr>
          <tr style="border-bottom:1px solid #E2E8F0">
            <td style="padding:7px 10px;font-weight:800;color:#D97706;background:#F0F4F8">Channel Fragmentation</td>
            <td style="padding:7px 10px;color:#64748B">No shared context. Siloed employee views. No save-and-resume.</td>
            <td style="padding:7px 10px;color:#3366FF;font-weight:600;border-left:2px solid rgba(51,102,255,0.15);background:rgba(51,102,255,0.02)">Single Engagement Layer. Digital Assist Premium with 360\u00b0 view. Act-on-behalf.</td>
            <td style="padding:7px 10px;text-align:center"><span style="background:rgba(5,150,105,0.1);color:#059669;padding:2px 6px;border-radius:4px;font-size:7px;font-weight:800">P1</span></td>
            <td style="padding:7px 10px;color:#64748B">Calls -25\u201335%. First-contact +20%. Branch seamless.</td>
          </tr>
          <tr style="border-bottom:1px solid #E2E8F0">
            <td style="padding:7px 10px;font-weight:800;color:#DC2626;background:#F0F4F8">Cost Structure</td>
            <td style="padding:7px 10px;color:#64748B">C/I 53.8% vs 50.7%. 42% on high-cost channels (R150\u2013250/contact).</td>
            <td style="padding:7px 10px;color:#3366FF;font-weight:600;border-left:2px solid rgba(51,102,255,0.15);background:rgba(51,102,255,0.02)">Self-service maximization + Grand Central iPaaS. Digital Factory for build efficiency.</td>
            <td style="padding:7px 10px;text-align:center"><span style="background:rgba(5,150,105,0.1);color:#059669;padding:2px 6px;border-radius:4px;font-size:7px;font-weight:800">P1</span></td>
            <td style="padding:7px 10px;color:#64748B">C/I -1\u20132pp = R1.2\u20132.3bn. Cost/interaction \u221910\u201320x.</td>
          </tr>
          <tr style="border-bottom:1px solid #E2E8F0">
            <td style="padding:7px 10px;font-weight:800;color:#D97706;background:#F0F4F8">One-Size-Fits-All</td>
            <td style="padding:7px 10px;color:#64748B">9.3M = 1 segment. No tailored props. Cross-sell suppressed.</td>
            <td style="padding:7px 10px;color:#3366FF;font-weight:600;border-left:2px solid rgba(51,102,255,0.15);background:rgba(51,102,255,0.02)">Segment-driven UX (ONE APP). Digital Engage Premium. Family &amp; Household Banking.</td>
            <td style="padding:7px 10px;text-align:center"><span style="background:rgba(51,102,255,0.1);color:#3366FF;padding:2px 6px;border-radius:4px;font-size:7px;font-weight:800">P2</span></td>
            <td style="padding:7px 10px;color:#64748B">Revenue +3\u20135%. Attrition -20\u201330%. Cross-sell +0.3\u20130.5x.</td>
          </tr>
          <tr>
            <td style="padding:7px 10px;font-weight:800;color:#7B2FFF;background:#F0F4F8">Innovation Bottleneck</td>
            <td style="padding:7px 10px;color:#64748B">Bespoke builds. No reusable components. R16.7bn IT, 15% ROE.</td>
            <td style="padding:7px 10px;color:#3366FF;font-weight:600;border-left:2px solid rgba(51,102,255,0.15);background:rgba(51,102,255,0.02)">Intelligence Fabric + CLO. Composable Adopt &amp; Build. Agentic process automation.</td>
            <td style="padding:7px 10px;text-align:center"><span style="background:rgba(123,47,255,0.1);color:#7B2FFF;padding:2px 6px;border-radius:4px;font-size:7px;font-weight:800">P3</span></td>
            <td style="padding:7px 10px;color:#64748B">TTM -50\u201360%. Cost/interaction -40\u201350%. ROE \u219216%+.</td>
          </tr>
        </tbody>
      </table>
    </div>
    <div style="margin-top:8px;padding:8px 14px;border-radius:8px;border:1px solid rgba(51,102,255,0.15);background:rgba(51,102,255,0.03);font-size:9px;color:#091C35;line-height:1.5;text-align:center">
      <strong style="color:#3366FF">The thread:</strong> Every problem traces to one root cause \u2014 <strong>ABSA\u2019s digital engagement layer is fragmented, inflexible, and expensive to change.</strong> Backbase replaces that fragmentation with a single platform that wraps around existing core systems.
    </div>
  `, bodyFull: true },

  { layout: 'content-standard', theme: 'light', label: 'VALUE AT STAKE \u2014 BY PHASE', title: 'R7.1\u201310.7bn Over 3 Years, Phase by Phase', subtitle: 'Each phase delivers measurable value before the next begins. Your team validated this roadmap.', body: `
    <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:12px;margin-top:6px">
      <div style="border-radius:10px;padding:14px;border:1px solid rgba(5,150,105,0.15);border-top:3px solid #059669">
        <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:6px"><div style="font-size:9px;font-weight:800;letter-spacing:1px;color:#059669">PHASE 1: FIX THE FOUNDATIONS</div><div style="font-size:7px;color:#94A3B8">Months 0\u201312</div></div>
        <div style="font-size:9px;color:#64748B;line-height:1.6">
          <div style="display:flex;justify-content:space-between;margin-bottom:3px"><span>C/I improvement -1 to 2pp</span><span style="font-weight:800;color:#059669">~R1.2\u20132.3bn</span></div>
          <div style="display:flex;justify-content:space-between;margin-bottom:3px"><span>Digital adoption 58% \u2192 78%</span><span style="font-weight:800;color:#059669">+20pp</span></div>
          <div style="display:flex;justify-content:space-between;margin-bottom:3px"><span>Onboarding time</span><span style="font-weight:800;color:#059669">-60\u201380%</span></div>
          <div style="display:flex;justify-content:space-between"><span>Contact centre deflection</span><span style="font-weight:800;color:#059669">-25\u201335%</span></div>
        </div>
      </div>
      <div style="border-radius:10px;padding:14px;border:1px solid rgba(51,102,255,0.15);border-top:3px solid #3366FF">
        <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:6px"><div style="font-size:9px;font-weight:800;letter-spacing:1px;color:#3366FF">PHASE 2: AMPLIFY GROWTH</div><div style="font-size:7px;color:#94A3B8">Months 12\u201324</div></div>
        <div style="font-size:9px;color:#64748B;line-height:1.6">
          <div style="display:flex;justify-content:space-between;margin-bottom:3px"><span>Retail revenue uplift</span><span style="font-weight:800;color:#3366FF">+3\u20135%</span></div>
          <div style="display:flex;justify-content:space-between;margin-bottom:3px"><span>Customer attrition</span><span style="font-weight:800;color:#3366FF">-20\u201330%</span></div>
          <div style="display:flex;justify-content:space-between;margin-bottom:3px"><span>Cross-sell ratio</span><span style="font-weight:800;color:#3366FF">+0.3\u20130.5x</span></div>
          <div style="display:flex;justify-content:space-between"><span>Digital lending conversion</span><span style="font-weight:800;color:#3366FF">+15\u201325%</span></div>
        </div>
      </div>
      <div style="border-radius:10px;padding:14px;border:1px solid rgba(123,47,255,0.15);border-top:3px solid #7B2FFF">
        <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:6px"><div style="font-size:9px;font-weight:800;letter-spacing:1px;color:#7B2FFF">PHASE 3: NEXT GEN INNOVATION</div><div style="font-size:7px;color:#94A3B8">Months 24\u201336</div></div>
        <div style="font-size:9px;color:#64748B;line-height:1.6">
          <div style="display:flex;justify-content:space-between;margin-bottom:3px"><span>NPS improvement</span><span style="font-weight:800;color:#7B2FFF">+10\u201315pp</span></div>
          <div style="display:flex;justify-content:space-between;margin-bottom:3px"><span>Cost per interaction</span><span style="font-weight:800;color:#7B2FFF">-40\u201350%</span></div>
          <div style="display:flex;justify-content:space-between;margin-bottom:3px"><span>ROE contribution</span><span style="font-weight:800;color:#7B2FFF">\u219216%+</span></div>
          <div style="display:flex;justify-content:space-between"><span>Time-to-market</span><span style="font-weight:800;color:#7B2FFF">-50\u201360%</span></div>
        </div>
      </div>
    </div>
    <div style="margin-top:10px;padding:10px 20px;background:#091C35;border-radius:10px;display:flex;justify-content:space-between;align-items:center">
      <div style="color:rgba(255,255,255,0.5);font-size:8px;font-weight:800;letter-spacing:1px">3-YEAR CUMULATIVE</div>
      <div style="display:flex;gap:28px">
        <div style="text-align:center"><div style="font-size:13px;font-weight:900;color:#D97706">R5.4bn</div><div style="font-size:7px;color:rgba(255,255,255,0.35)">CONSERVATIVE</div></div>
        <div style="text-align:center"><div style="font-size:17px;font-weight:900;color:#3366FF">R7.1bn</div><div style="font-size:7px;color:rgba(255,255,255,0.35)">BASE CASE</div></div>
        <div style="text-align:center"><div style="font-size:13px;font-weight:900;color:#059669">R10.7bn</div><div style="font-size:7px;color:rgba(255,255,255,0.35)">ASPIRATIONAL</div></div>
      </div>
    </div>
  `, bodyFull: true },

  // ── 03: RISK REGISTER ──
  { layout: 'chapter-numbered', theme: 'navy', number: '03', label: 'INTERVENTION \u2014 OPERATIONAL RESILIENCE', title: 'Risk Register', subtitle: '8 minutes. ABSA-specific. Honest, not salesy. Addresses: operational resilience.' },

  { layout: 'content-standard', theme: 'light', label: '3 RISKS', title: 'Where It Gets Hard', subtitle: 'We\u2019re not pretending this is easy. Here\u2019s specifically where, and how we mitigate.', body: `
    <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:12px;margin-top:6px">
      <div style="border-radius:10px;padding:14px;border:1px solid rgba(220,38,38,0.15);border-top:4px solid #DC2626"><div style="font-size:8px;font-weight:800;letter-spacing:2px;color:#DC2626;margin-bottom:4px">RISK 1</div><div style="font-size:14px;font-weight:900;margin-bottom:6px">Co-Existence</div><p style="font-size:8px;color:#64748B;line-height:1.4;margin-bottom:8px">IBM Mainframe + MuleSoft + engagement layer. \u201cBuild, launch, hollow.\u201d Integration seams = failure points.</p><div style="padding:8px;background:rgba(5,150,105,0.05);border:1px solid rgba(5,150,105,0.15);border-radius:6px"><div style="font-size:7px;font-weight:800;color:#059669">MITIGATION</div><p style="font-size:8px;color:#091C35;line-height:1.4;margin-top:2px">Grand Central iPaaS. BIAN APIs. MCB: 3-country, 6 months. <strong>Co-existence IS our architecture.</strong></p></div></div>
      <div style="border-radius:10px;padding:14px;border:1px solid rgba(217,119,6,0.15);border-top:4px solid #D97706"><div style="font-size:8px;font-weight:800;letter-spacing:2px;color:#D97706;margin-bottom:4px">RISK 2</div><div style="font-size:14px;font-weight:900;margin-bottom:6px">Org Adoption</div><p style="font-size:8px;color:#64748B;line-height:1.4;margin-bottom:8px">New PPB division (June 2025). 10K+ employees. Digital adoption = behavior change.</p><div style="padding:8px;background:rgba(5,150,105,0.05);border:1px solid rgba(5,150,105,0.15);border-radius:6px"><div style="font-size:7px;font-weight:800;color:#059669">MITIGATION</div><p style="font-size:8px;color:#091C35;line-height:1.4;margin-top:2px">Digital Factory + Academy path + EY as local change partner. Phased rollout by segment.</p></div></div>
      <div style="border-radius:10px;padding:14px;border:1px solid rgba(123,47,255,0.15);border-top:4px solid #7B2FFF"><div style="font-size:8px;font-weight:800;letter-spacing:2px;color:#7B2FFF;margin-bottom:4px">RISK 3</div><div style="font-size:14px;font-weight:900;margin-bottom:6px">Scope Creep</div><p style="font-size:8px;color:#64748B;line-height:1.4;margin-bottom:8px">R16.7bn IT spend. Board scrutiny. Scope grew \u20ac19M \u2192 \u20ac32M after defense.</p><div style="padding:8px;background:rgba(5,150,105,0.05);border:1px solid rgba(5,150,105,0.15);border-radius:6px"><div style="font-size:7px;font-weight:800;color:#059669">MITIGATION</div><p style="font-size:8px;color:#091C35;line-height:1.4;margin-top:2px">Phase-gated delivery. Value checkpoints. 80% OOTB. Fixed-scope Phase 1. MCB: 6 months.</p></div></div>
    </div>
  `, bodyFull: true },

  // ── 04: CFO CARD ──
  { layout: 'chapter-numbered', theme: 'navy', number: '04', label: 'INTERVENTION \u2014 LEADERSHIP ACCOUNTABILITY', title: 'Investment\nLogic Card', subtitle: 'Executive-level view of the investment and its value. Phase-gated. Addresses: leadership accountability.' },

  { layout: 'content-standard', theme: 'light', label: 'EXECUTIVE VIEW', title: 'ABSA Digital Platform Investment Logic', subtitle: 'A concise view of the investment and the value it creates. For leadership context.', body: `
    <div style="border:2px solid #3366FF;border-radius:12px;padding:18px;background:rgba(51,102,255,0.02)">
      <div style="display:grid;grid-template-columns:170px 1fr;gap:18px">
        <div>
          <div style="font-size:8px;font-weight:800;letter-spacing:2px;color:#3366FF;margin-bottom:4px">5-YEAR INVESTMENT</div>
          <div style="font-size:32px;font-weight:900">R618M</div>
          <div style="font-size:9px;color:#64748B;margin-top:4px">\u20ac32.2M \u00d7 19.2 ZAR</div>
          <div style="margin-top:10px;font-size:8px;font-weight:800;color:#091C35">PHASE-GATED</div>
          <div style="font-size:8px;color:#64748B;margin-top:3px;line-height:1.6">
            <span style="color:#059669;font-weight:700">P1</span> Y0\u2013Y1: R185M<br>
            <span style="color:#3366FF;font-weight:700">P2</span> Y1\u2013Y2: activated<br>
            <span style="color:#7B2FFF;font-weight:700">P3</span> Y2+: SME added<br>
            <em style="font-size:7px;color:#94A3B8">Pay as you grow</em>
          </div>
        </div>
        <div>
          <div style="font-size:8px;font-weight:800;letter-spacing:2px;color:#091C35;margin-bottom:6px">VALUE LEVERS</div>
          <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:8px;margin-bottom:10px">
            <div style="background:#F0F4F8;border-radius:6px;padding:8px;text-align:center"><div style="font-size:7px;font-weight:800;color:#059669">COST REDUCTION</div><div style="font-size:18px;font-weight:900;color:#059669;margin:3px 0">R3.8bn</div><div style="font-size:7px;color:#64748B">C/I 53.8% \u2192 50.5%</div></div>
            <div style="background:#F0F4F8;border-radius:6px;padding:8px;text-align:center"><div style="font-size:7px;font-weight:800;color:#3366FF">REVENUE PROTECTION</div><div style="font-size:18px;font-weight:900;color:#3366FF;margin:3px 0">R2.3bn</div><div style="font-size:7px;color:#64748B">Attrition -20\u201330%</div></div>
            <div style="background:#F0F4F8;border-radius:6px;padding:8px;text-align:center"><div style="font-size:7px;font-weight:800;color:#7B2FFF">REVENUE GROWTH</div><div style="font-size:18px;font-weight:900;color:#7B2FFF;margin:3px 0">R1.0bn</div><div style="font-size:7px;color:#64748B">Segments + cross-sell</div></div>
          </div>
          <div style="display:grid;grid-template-columns:1fr 1fr 1fr 1fr;gap:8px">
            <div style="background:#091C35;border-radius:6px;padding:8px;text-align:center"><div style="font-size:7px;font-weight:800;color:rgba(255,255,255,0.4)">BASE VALUE</div><div style="font-size:16px;font-weight:900;color:#3366FF;margin-top:3px">R7.1bn</div></div>
            <div style="background:#091C35;border-radius:6px;padding:8px;text-align:center"><div style="font-size:7px;font-weight:800;color:rgba(255,255,255,0.4)">ROI</div><div style="font-size:16px;font-weight:900;color:#059669;margin-top:3px">11.5x</div></div>
            <div style="background:#091C35;border-radius:6px;padding:8px;text-align:center"><div style="font-size:7px;font-weight:800;color:rgba(255,255,255,0.4)">CONSERVATIVE</div><div style="font-size:16px;font-weight:900;color:#D97706;margin-top:3px">8.7x</div></div>
            <div style="background:#091C35;border-radius:6px;padding:8px;text-align:center"><div style="font-size:7px;font-weight:800;color:rgba(255,255,255,0.4)">PER-USER Y5</div><div style="font-size:16px;font-weight:900;color:#fff;margin-top:3px">R11.21</div></div>
          </div>
        </div>
      </div>
      <div style="margin-top:10px;border-top:1px solid #E2E8F0;padding-top:8px;font-size:8px;color:#64748B;line-height:1.5"><strong style="color:#3366FF">By Year 5, the cost per active user is less than the cost of a single branch transaction.</strong></div>
    </div>
  `, bodyFull: true },

  // ── 05: JOINT SCORECARD ──
  { layout: 'chapter-numbered', theme: 'navy', number: '05', label: 'INTERVENTION', title: 'Joint Success\nScorecard', subtitle: '10 min. Live co-creation. Amber columns = theirs. This IS the culture demo.' },

  { layout: 'content-standard', theme: 'light', label: 'DRAFT \u2014 FOR LIVE CO-CREATION', title: 'How We\u2019d Measure Success Together', subtitle: '\u201cThe amber columns are yours. Let\u2019s build this right now.\u201d', body: `
    <div style="border-radius:10px;overflow:hidden;border:1px solid #E2E8F0">
      <table style="width:100%;border-collapse:collapse;font-size:10px">
        <thead><tr style="background:#091C35;color:#fff;font-size:7px;font-weight:800;letter-spacing:1px;text-transform:uppercase">
          <th style="padding:7px 10px;text-align:left;width:100px">Category</th><th style="padding:7px 10px;text-align:left">Metric</th><th style="padding:7px 10px;text-align:center;width:60px">Current</th><th style="padding:7px 10px;text-align:center;width:60px">Year 1</th><th style="padding:7px 10px;text-align:center;width:60px">Year 3</th><th style="padding:7px 10px;text-align:center;width:70px;color:rgba(255,255,255,0.4)">ABSA Target</th>
        </tr></thead>
        <tbody>
          <tr style="border-bottom:1px solid #E2E8F0"><td style="padding:6px 10px;font-weight:800;color:#3366FF;background:#F0F4F8" rowspan="3">Customer</td><td style="padding:6px 10px">Digital Adoption</td><td style="padding:6px 10px;text-align:center">58%</td><td style="padding:6px 10px;text-align:center">70%</td><td style="padding:6px 10px;text-align:center">85%</td><td style="padding:6px 10px;text-align:center;background:rgba(217,119,6,0.06);color:#D97706;font-weight:700;font-size:13px">?</td></tr>
          <tr style="border-bottom:1px solid #E2E8F0"><td style="padding:6px 10px">NPS</td><td style="padding:6px 10px;text-align:center">15%</td><td style="padding:6px 10px;text-align:center">22%</td><td style="padding:6px 10px;text-align:center">30%+</td><td style="padding:6px 10px;text-align:center;background:rgba(217,119,6,0.06);color:#D97706;font-weight:700;font-size:13px">?</td></tr>
          <tr style="border-bottom:1px solid #E2E8F0"><td style="padding:6px 10px">Customer Base</td><td style="padding:6px 10px;text-align:center">9.3M \u2193</td><td style="padding:6px 10px;text-align:center">9.5M</td><td style="padding:6px 10px;text-align:center">10.2M</td><td style="padding:6px 10px;text-align:center;background:rgba(217,119,6,0.06);color:#D97706;font-weight:700;font-size:13px">?</td></tr>
          <tr style="border-bottom:1px solid #E2E8F0"><td style="padding:6px 10px;font-weight:800;color:#059669;background:#F0F4F8" rowspan="3">Ops</td><td style="padding:6px 10px">Cost-to-Income</td><td style="padding:6px 10px;text-align:center">53.8%</td><td style="padding:6px 10px;text-align:center">52.5%</td><td style="padding:6px 10px;text-align:center">50.5%</td><td style="padding:6px 10px;text-align:center;background:rgba(217,119,6,0.06);color:#D97706;font-weight:700;font-size:13px">?</td></tr>
          <tr style="border-bottom:1px solid #E2E8F0"><td style="padding:6px 10px">Digital Sales Conv.</td><td style="padding:6px 10px;text-align:center">~5\u20138%</td><td style="padding:6px 10px;text-align:center">12\u201315%</td><td style="padding:6px 10px;text-align:center">20\u201325%</td><td style="padding:6px 10px;text-align:center;background:rgba(217,119,6,0.06);color:#D97706;font-weight:700;font-size:13px">?</td></tr>
          <tr style="border-bottom:1px solid #E2E8F0"><td style="padding:6px 10px">Call Deflection</td><td style="padding:6px 10px;text-align:center">TBD</td><td style="padding:6px 10px;text-align:center">+25%</td><td style="padding:6px 10px;text-align:center">+35%</td><td style="padding:6px 10px;text-align:center;background:rgba(217,119,6,0.06);color:#D97706;font-weight:700;font-size:13px">?</td></tr>
          <tr style="border-bottom:1px solid #E2E8F0"><td style="padding:6px 10px;font-weight:800;color:#7B2FFF;background:#F0F4F8" rowspan="2">Delivery</td><td style="padding:6px 10px">Phase 1 Go-Live</td><td style="padding:6px 10px;text-align:center">\u2014</td><td style="padding:6px 10px;text-align:center">6\u20139 mo</td><td style="padding:6px 10px;text-align:center">\u2014</td><td style="padding:6px 10px;text-align:center;background:rgba(217,119,6,0.06);color:#D97706;font-weight:700;font-size:13px">?</td></tr>
          <tr><td style="padding:6px 10px">Uptime</td><td style="padding:6px 10px;text-align:center">\u2014</td><td style="padding:6px 10px;text-align:center">99.9%</td><td style="padding:6px 10px;text-align:center">99.9%</td><td style="padding:6px 10px;text-align:center;background:rgba(217,119,6,0.06);color:#D97706;font-weight:700;font-size:13px">?</td></tr>
        </tbody>
      </table>
    </div>
  `, bodyFull: true },

  // ── ABOVE & BEYOND ──
  { layout: 'chapter-standard', theme: 'blue', label: 'ABOVE & BEYOND', title: 'Going Further', subtitle: 'Three things no other vendor will bring.' },

  // 2028 VISION
  { layout: 'content-standard', theme: 'dark', label: 'IMAGINE ABSA IN 2028', title: 'What the Headlines Could Read', subtitle: 'Not a promise \u2014 a vision grounded in what the platform enables.', body: `
    <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:14px;margin-top:10px">
      <div style="border-radius:10px;padding:16px;background:rgba(255,255,255,0.04);border:1px solid rgba(255,255,255,0.08)">
        <div style="font-size:7px;font-weight:800;letter-spacing:2px;color:rgba(255,255,255,0.3)">BUSINESSTECH \u00b7 2028</div>
        <div style="font-size:16px;font-weight:900;color:#fff;line-height:1.2;margin:8px 0">\u201cABSA overtakes FNB in digital app satisfaction\u201d</div>
        <p style="font-size:8px;color:rgba(255,255,255,0.4);line-height:1.4">NPS 28%. Segment-driven UX cited as key. Digital adoption 78%.</p>
        <div style="margin-top:8px;padding:6px;background:rgba(5,150,105,0.15);border-radius:4px;font-size:7px;font-weight:700;color:#059669;text-align:center">Phase 1 (Fix) + Phase 2 (Amplify)</div>
      </div>
      <div style="border-radius:10px;padding:16px;background:rgba(255,255,255,0.04);border:1px solid rgba(255,255,255,0.08)">
        <div style="font-size:7px;font-weight:800;letter-spacing:2px;color:rgba(255,255,255,0.3)">MONEYWEB \u00b7 2028</div>
        <div style="font-size:16px;font-weight:900;color:#fff;line-height:1.2;margin:8px 0">\u201cABSA halts customer bleed \u2014 first net positive quarter\u201d</div>
        <p style="font-size:8px;color:rgba(255,255,255,0.4);line-height:1.4">Net growth Q2 2028. 200K+ new-to-bank via digital. Sole prop +34%.</p>
        <div style="margin-top:8px;padding:6px;background:rgba(51,102,255,0.15);border-radius:4px;font-size:7px;font-weight:700;color:#3366FF;text-align:center">Phase 2 (Amplify) + Phase N (SME)</div>
      </div>
      <div style="border-radius:10px;padding:16px;background:rgba(255,255,255,0.04);border:1px solid rgba(255,255,255,0.08)">
        <div style="font-size:7px;font-weight:800;letter-spacing:2px;color:rgba(255,255,255,0.3)">CNBC AFRICA \u00b7 2028</div>
        <div style="font-size:16px;font-weight:900;color:#fff;line-height:1.2;margin:8px 0">\u201cABSA PPB hits 16% ROE as C/I drops below 51%\u201d</div>
        <p style="font-size:8px;color:rgba(255,255,255,0.4);line-height:1.4">CEO credits digital transformation. C/I down 2.8pp in 30 months. AI CLO drives 40% contact centre reduction.</p>
        <div style="margin-top:8px;padding:6px;background:rgba(123,47,255,0.15);border-radius:4px;font-size:7px;font-weight:700;color:#7B2FFF;text-align:center">Phase 3 (Next Gen) \u2014 AI + CLO + Delivery OS</div>
      </div>
    </div>
  `, bodyFull: true },

  { layout: 'statement-stat', accent: 'blue', label: 'THE QUESTION', stat: '2028',
    text: 'Will ABSA be the bank that <span class="hl">redefined retail banking in South Africa</span> \u2014 or the one that let Capitec and FNB write that story?', source: '' },

  // COMPETITIVE — DETAILED COMPARISON TABLE (from exec summary)
  { layout: 'content-standard', theme: 'light', label: 'WHY BACKBASE AT THIS SCALE', title: 'What ABSA Needs at This Scale', subtitle: 'A transformation of 9.3M customers demands enterprise maturity, Africa experience, and a platform approach.', body: `
    <div style="border-radius:10px;overflow:hidden;border:1px solid #E2E8F0">
      <table style="width:100%;border-collapse:collapse;font-size:9px">
        <thead><tr style="background:#091C35;color:#fff;font-size:7px;font-weight:800;letter-spacing:1px;text-transform:uppercase">
          <th style="padding:8px 10px;text-align:left;width:100px">Criteria</th>
          <th style="padding:8px 10px;text-align:left;width:28%">Full-Stack Core Replacement<br><span style="font-weight:400;font-size:6px;letter-spacing:0;text-transform:none;opacity:0.5">Higher risk, longer timelines</span></th>
          <th style="padding:8px 10px;text-align:left;width:28%">Front-End Builder<br><span style="font-weight:400;font-size:6px;letter-spacing:0;text-transform:none;opacity:0.5">Fast start, limited scale</span></th>
          <th style="padding:8px 10px;text-align:left;width:28%;border-left:2px solid #3366FF">Engagement Banking Platform<br><span style="font-weight:400;font-size:6px;letter-spacing:0;text-transform:none;opacity:0.5">Progressive modernization at scale</span></th>
        </tr></thead>
        <tbody>
          <tr style="border-bottom:1px solid #E2E8F0">
            <td style="padding:7px 10px;font-weight:800;color:#091C35;background:#F0F4F8">Integration</td>
            <td style="padding:7px 10px;color:#64748B">Requires core replacement or deep commitment. Existing systems at risk.</td>
            <td style="padding:7px 10px;color:#64748B">API layer on top. No core dependency, but no back-office either.</td>
            <td style="padding:7px 10px;color:#3366FF;font-weight:600;border-left:2px solid rgba(51,102,255,0.15);background:rgba(51,102,255,0.02)">Grand Central iPaaS. Keep your core. Zero migration risk.</td>
          </tr>
          <tr style="border-bottom:1px solid #E2E8F0">
            <td style="padding:7px 10px;font-weight:800;color:#091C35;background:#F0F4F8">Time to Value</td>
            <td style="padding:7px 10px;color:#64748B">18\u201324+ months. Complex migration path.</td>
            <td style="padding:7px 10px;color:#64748B">3\u20136 months front-end. Back-office disconnected.</td>
            <td style="padding:7px 10px;color:#3366FF;font-weight:600;border-left:2px solid rgba(51,102,255,0.15);background:rgba(51,102,255,0.02)">6\u20139 months live (MCB: 6). Full front-to-back from Day 1.</td>
          </tr>
          <tr style="border-bottom:1px solid #E2E8F0">
            <td style="padding:7px 10px;font-weight:800;color:#091C35;background:#F0F4F8">Africa Track Record</td>
            <td style="padding:7px 10px;color:#64748B">Greenfield/small banks (Ethiopia, Zimbabwe). No Tier-1 at ABSA scale.</td>
            <td style="padding:7px 10px;color:#64748B">Early-stage. No bank at 9.3M scale. Limited support.</td>
            <td style="padding:7px 10px;color:#3366FF;font-weight:600;border-left:2px solid rgba(51,102,255,0.15);background:rgba(51,102,255,0.02)">MCB, I&M, 100+ banks. Multi-country rollout across 3 African markets.</td>
          </tr>
          <tr style="border-bottom:1px solid #E2E8F0">
            <td style="padding:7px 10px;font-weight:800;color:#091C35;background:#F0F4F8">Platform Breadth</td>
            <td style="padding:7px 10px;color:#64748B">Core + channels tightly coupled. All-or-nothing.</td>
            <td style="padding:7px 10px;color:#64748B">Front-end only. No orchestration, AI, or employee tools.</td>
            <td style="padding:7px 10px;color:#3366FF;font-weight:600;border-left:2px solid rgba(51,102,255,0.15);background:rgba(51,102,255,0.02)">Servicing + Sales + AI + Employee Assist + Process Orchestration.</td>
          </tr>
          <tr>
            <td style="padding:7px 10px;font-weight:800;color:#091C35;background:#F0F4F8">Enterprise Readiness</td>
            <td style="padding:7px 10px;color:#64748B">Enterprise delivery but complex, high-risk migration.</td>
            <td style="padding:7px 10px;color:#64748B">$3.3M funded startup. No managed services or 24/7 support.</td>
            <td style="padding:7px 10px;color:#3366FF;font-weight:600;border-left:2px solid rgba(51,102,255,0.15);background:rgba(51,102,255,0.02)">Digital Factory, 24/7 support, proven methodology. 100+ deployments.</td>
          </tr>
        </tbody>
      </table>
    </div>
  `, bodyFull: true },

  // ENTERPRISE AT SCALE — STATS + CAPABILITY CARDS (from exec summary)
  { layout: 'content-standard', theme: 'light', label: 'ENTERPRISE AT SCALE', title: 'Built for Banks Like ABSA', subtitle: 'The proof points behind the platform claim.', body: `
    <div style="display:flex;justify-content:center;gap:32px;width:100%;padding:12px 20px;background:#091C35;border-radius:10px;margin-bottom:14px">
      <div style="text-align:center"><div style="font-size:20px;font-weight:900;color:#3366FF">100+</div><div style="font-size:7px;font-weight:600;color:rgba(255,255,255,0.35);letter-spacing:1px;text-transform:uppercase;margin-top:2px">Banks Worldwide</div></div>
      <div style="text-align:center"><div style="font-size:20px;font-weight:900;color:#0891B2">5</div><div style="font-size:7px;font-weight:600;color:rgba(255,255,255,0.35);letter-spacing:1px;text-transform:uppercase;margin-top:2px">Continents</div></div>
      <div style="text-align:center"><div style="font-size:20px;font-weight:900;color:#059669">60+</div><div style="font-size:7px;font-weight:600;color:rgba(255,255,255,0.35);letter-spacing:1px;text-transform:uppercase;margin-top:2px">OOTB Capabilities</div></div>
      <div style="text-align:center"><div style="font-size:20px;font-weight:900;color:#D97706">6 Mo</div><div style="font-size:7px;font-weight:600;color:rgba(255,255,255,0.35);letter-spacing:1px;text-transform:uppercase;margin-top:2px">First Go-Live</div></div>
      <div style="text-align:center"><div style="font-size:20px;font-weight:900;color:#7B2FFF">24/7</div><div style="font-size:7px;font-weight:600;color:rgba(255,255,255,0.35);letter-spacing:1px;text-transform:uppercase;margin-top:2px">Managed Support</div></div>
    </div>
    <div style="display:grid;grid-template-columns:1fr 1fr 1fr 1fr;gap:10px">
      <div style="border-radius:10px;padding:12px;border:1px solid rgba(51,102,255,0.15);border-top:3px solid #3366FF">
        <div style="font-size:8px;font-weight:800;letter-spacing:2px;color:#3366FF;margin-bottom:6px">SINGLE ENGAGEMENT LAYER</div>
        <p style="font-size:8px;color:#64748B;line-height:1.4">One platform for Retail, SME, Wealth, Corporate. No point solutions. Consistent CX across all segments and channels.</p>
      </div>
      <div style="border-radius:10px;padding:12px;border:1px solid rgba(5,150,105,0.15);border-top:3px solid #059669">
        <div style="font-size:8px;font-weight:800;letter-spacing:2px;color:#059669;margin-bottom:6px">PROGRESSIVE MODERNIZATION</div>
        <p style="font-size:8px;color:#64748B;line-height:1.4">Phase 1 live in 6\u20139 months. No rip-and-replace. Wrap around existing core. Each phase builds on the last.</p>
      </div>
      <div style="border-radius:10px;padding:12px;border:1px solid rgba(123,47,255,0.15);border-top:3px solid #7B2FFF">
        <div style="font-size:8px;font-weight:800;letter-spacing:2px;color:#7B2FFF;margin-bottom:6px">AI-NATIVE INTELLIGENCE</div>
        <p style="font-size:8px;color:#64748B;line-height:1.4">Intelligence Fabric and CLO embedded, not bolted on. Hyper-personalization, NBA, churn prevention from Phase 3.</p>
      </div>
      <div style="border-radius:10px;padding:12px;border:1px solid rgba(217,119,6,0.15);border-top:3px solid #D97706">
        <div style="font-size:8px;font-weight:800;letter-spacing:2px;color:#D97706;margin-bottom:6px">DIGITAL FACTORY MODEL</div>
        <p style="font-size:8px;color:#64748B;line-height:1.4">Joint operating model. Governance across tech, security, UX, data. Full ownership transfer \u2014 no vendor lock-in.</p>
      </div>
    </div>
  `, bodyFull: true },

  // LEAVE-BEHIND
  { layout: 'content-columns', label: 'THE LEAVE-BEHIND', title: 'What We Send After the Visit', columns: [
    { subtitle: 'Outside-In Perspective', body: 'Competitive position, 5 problems, value at stake, peer benchmarks, co-created scorecard. For the Group CEO and board.' },
    { subtitle: 'Demo Portal Access', body: 'Continued access to the localized, branded demo environment. Extended for the decision period.' },
    { subtitle: 'Investment Logic Card', body: 'Printed + digital. R618M, R7.1bn value, 11.5x ROI. Ready for board forwarding.' }
  ]},

  // ════════════════════════════════════════════════════════════════
  // CLOSE
  // ════════════════════════════════════════════════════════════════
  { layout: 'statement', variant: 'dark', label: 'THE OUTCOME',
    text: 'They asked to understand how we\u2019d work together <span class="hl">when it matters most.</span> We showed them it\u2019s <span class="hl">already started.</span>' },

  { layout: 'thank-you' }
];
