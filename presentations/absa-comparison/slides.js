window.BB_SHARED_ASSETS = '../backbase-slides-app';

const SPEAKER_NOTES = {
  1: 'This deck maps every ABSA bullet point to our run-of-show. Use it to rally the internal team: "We cover 100% of what they asked. We ADD 41 minutes of strategic value that no other vendor will bring."',
  2: 'The key reframe: ABSA gave us a list of topics. Every vendor will check the boxes. We turn those boxes into a STORY with a golden thread. Same content, different impact.',
  3: 'Walk the team through: left column is ABSA\'s format. Right column is our format. Same timing. Different outcome.',
  4: 'Shyam\'s opening is the single biggest differentiation. No slides, no deck. 5 minutes of "here\'s what we see when we look at ABSA." Every other vendor will say "Hi, I\'m X from Company Y."',
  5: 'Item 1 has 6 bullet points. We cover all 6. But "demonstration of culture" — the last bullet — we reframe from a values slide into a mirror-back of their own strategy. Culture = showing you understand their world.',
  6: 'Item 2 has 8 bullet points. We cover all 8. The 3 risks bullet gets ELEVATED into its own 8-minute segment with ABSA-specific risks. Plus the demo portal reveal.',
  7: 'Item 3 is mostly straightforward — Thijs and Ruben own it. The add is Delivery OS which is a competitive differentiator Intellect and Plumery can\'t match.',
  8: 'Item 4 is the CFO\'s session. Every vendor shows a price table. We ADD the Investment Logic card: R618M vs R7.1bn = 11.5x.',
  9: 'Item 5: "culture demonstration" appears here AND in Item 1. Our answer: don\'t present a slide about culture. CO-CREATE an artifact. The scorecard exercise IS the culture demonstration.',
  10: 'Summary: 100% coverage. 41 minutes of strategic adds. 5 speakers orchestrated into one story.',
};

/* helper: comparison row */
function compRow(asked, approach, who, isAdd) {
  const leftBg = isAdd ? 'background:rgba(51,102,255,0.04);' : '';
  const icon = isAdd ? '<span style="color:#3366FF;font-weight:900;font-size:10px">+ ELEVATED</span>' : '<span style="color:#059669;font-weight:900;font-size:10px">\u2713 COVERED</span>';
  return `<div style="display:flex;gap:0;width:100%;border-bottom:1px solid #E2E8F0;${leftBg}">
    <div style="flex:1;padding:8px 12px;border-right:1px solid #E2E8F0">
      <div style="font-size:9px;color:#64748B;line-height:1.5">${asked}</div>
    </div>
    <div style="flex:1.3;padding:8px 12px;border-right:1px solid #E2E8F0">
      <div style="font-size:9px;color:#091C35;line-height:1.5;font-weight:${isAdd ? '700' : '500'}">${approach}</div>
    </div>
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

  // ═══ 1: COVER ═══
  { layout: 'cover-color-block', label: 'ABSA AMSTERDAM', title: 'Asked vs\nDelivered', date: 'Internal \u2014 Team Alignment' },

  // ═══ 2: THE REFRAME ═══
  { layout: 'statement', variant: 'dark', label: 'THE PRINCIPLE',
    text: 'We don\u2019t change <span class="hl">what</span> ABSA asked for. We change <span class="hl">how</span> we deliver it. Every bullet point covered. But instead of 5 disconnected vendor presentations, one story with a golden thread.' },

  // ═══ 3: OVERVIEW ═══
  { layout: 'content-standard', theme: 'light', label: 'STRUCTURE COMPARISON', title: 'Same 5 Items, Different Impact', subtitle: 'Left: what every vendor will do. Right: what we will do. Same timing. Different outcome.', body: `
    <div style="display:flex;gap:20px;width:100%;margin-top:8px">
      <div style="flex:1">
        <div style="font-size:9px;font-weight:800;letter-spacing:2px;color:#DC2626;margin-bottom:10px;text-transform:uppercase">What Every Vendor Will Do</div>
        <div style="display:flex;flex-direction:column;gap:6px">
          <div style="padding:10px 14px;background:rgba(220,38,38,0.04);border:1px solid rgba(220,38,38,0.12);border-radius:8px;font-size:10px;color:#64748B">Opening: round-table introductions + corporate overview deck</div>
          <div style="padding:10px 14px;background:rgba(220,38,38,0.04);border:1px solid rgba(220,38,38,0.12);border-radius:8px;font-size:10px;color:#64748B">Item 1: Backbase revenue slide, R&D %, generic roadmap</div>
          <div style="padding:10px 14px;background:rgba(220,38,38,0.04);border:1px solid rgba(220,38,38,0.12);border-radius:8px;font-size:10px;color:#64748B">Item 2: methodology deck, generic risk matrix, timeline chart</div>
          <div style="padding:10px 14px;background:rgba(220,38,38,0.04);border:1px solid rgba(220,38,38,0.12);border-radius:8px;font-size:10px;color:#64748B">Item 3: support tiers table, SLA numbers, training catalogue</div>
          <div style="padding:10px 14px;background:rgba(220,38,38,0.04);border:1px solid rgba(220,38,38,0.12);border-radius:8px;font-size:10px;color:#64748B">Item 4: price table, license model, T&Cs</div>
          <div style="padding:10px 14px;background:rgba(220,38,38,0.04);border:1px solid rgba(220,38,38,0.12);border-radius:8px;font-size:10px;color:#64748B">Item 5: partnership values slide, governance org chart</div>
        </div>
        <div style="margin-top:10px;padding:8px 12px;background:rgba(220,38,38,0.06);border-radius:6px;font-size:9px;color:#DC2626;font-weight:700;text-align:center">6 disconnected presentations. No story. Forgettable.</div>
      </div>
      <div style="flex:1">
        <div style="font-size:9px;font-weight:800;letter-spacing:2px;color:#3366FF;margin-bottom:10px;text-transform:uppercase">What We Will Do</div>
        <div style="display:flex;flex-direction:column;gap:6px">
          <div style="padding:10px 14px;background:rgba(51,102,255,0.04);border:1px solid rgba(51,102,255,0.15);border-radius:8px;font-size:10px;color:#091C35;font-weight:600">Act 1 \u201cWe See You\u201d: open with THEIR story, not ours. No slides.</div>
          <div style="padding:10px 14px;background:rgba(51,102,255,0.04);border:1px solid rgba(51,102,255,0.15);border-radius:8px;font-size:10px;color:#091C35;font-weight:600">Act 2 \u201cWe\u2019ve Already Started\u201d: 5 problems + value at stake using ABSA\u2019s own numbers</div>
          <div style="padding:10px 14px;background:rgba(51,102,255,0.04);border:1px solid rgba(51,102,255,0.15);border-radius:8px;font-size:10px;color:#091C35;font-weight:600">Act 3 \u201cWe Know How\u201d: ABSA-specific risks + demo portal reveal + Delivery OS</div>
          <div style="padding:10px 14px;background:rgba(51,102,255,0.04);border:1px solid rgba(51,102,255,0.15);border-radius:8px;font-size:10px;color:#091C35;font-weight:600">Act 3b: Digital Factory + support. Operational reality, not theory.</div>
          <div style="padding:10px 14px;background:rgba(51,102,255,0.04);border:1px solid rgba(51,102,255,0.15);border-radius:8px;font-size:10px;color:#091C35;font-weight:600">Act 4 \u201cIt Makes Sense\u201d: pricing + Investment Logic card for the CFO\u2019s board</div>
          <div style="padding:10px 14px;background:rgba(51,102,255,0.04);border:1px solid rgba(51,102,255,0.15);border-radius:8px;font-size:10px;color:#091C35;font-weight:600">Act 5 \u201cLet\u2019s Build This\u201d: live co-creation of success scorecard. Culture in action.</div>
        </div>
        <div style="margin-top:10px;padding:8px 12px;background:rgba(51,102,255,0.06);border-radius:6px;font-size:9px;color:#3366FF;font-weight:700;text-align:center">1 story. 5 acts. Golden thread. Unforgettable.</div>
      </div>
    </div>
  `, bodyFull: true },

  // ═══ 4: OPENING ═══
  { layout: 'content-standard', theme: 'light', label: 'OPENING \u00b7 10 MIN', title: 'Opening & Welcome', subtitle: 'ABSA asked for introductions. We open with their story.', body:
    tableHeader() +
    `<div style="border:1px solid #E2E8F0;border-top:0;border-radius:0 0 8px 8px;overflow:hidden">` +
    compRow('Absa Team introduction', 'Subash introduces the ABSA delegation', 'Subash', false) +
    compRow('Vendor Team introduction', 'Aymen: brief round-table. Name, role, one sentence. <strong>No corporate history.</strong>', 'Aymen', false) +
    compRow('<em>(not asked for)</em>', '<strong>\u201cThe ABSA Story\u201d \u2014 3 Beats.</strong> Shyam opens with ABSA\u2019s world: R115.7bn revenue, 300K customer bleed, NPS 15% vs Capitec 45%, C/I at 53.8%. Then: \u201cHere\u2019s why now.\u201d Then: \u201cHow we\u2019d measure success.\u201d <em>No slides. Eye contact. 5 min.</em>', '<strong>Shyam</strong>', true) +
    `</div>
    <div style="margin-top:10px;padding:10px 14px;border-radius:8px;border-left:3px solid #3366FF;background:rgba(51,102,255,0.04);font-size:10px;color:#091C35;line-height:1.6">
      <strong style="color:#3366FF">Why this matters:</strong> Every other vendor opens with \u201cHi, I\u2019m X from Company Y, we do Z.\u201d We open with \u201cHere\u2019s what we see when we look at ABSA.\u201d <strong>The tone for the entire 160 minutes is set in these 5 minutes.</strong>
    </div>`
  , bodyFull: true },

  // ═══ 5: ITEM 1 ═══
  { layout: 'content-standard', theme: 'light', label: 'ITEM 1 \u00b7 30 MIN', title: 'Strategic Alignment', subtitle: 'ABSA listed 6 bullet points. We cover all 6 \u2014 and elevate the last one.', body:
    tableHeader() +
    `<div style="border:1px solid #E2E8F0;border-top:0;border-radius:0 0 8px 8px;overflow:hidden">` +
    compRow('Absa Digital Transformation Strategy', 'Subash presents. We <strong>listen deeply</strong>, take notes, watch body language.', 'Subash', false) +
    compRow('Company background, ownership, financial health', 'Privately held. No acquisition risk. 20+ years. Revenue growth.', 'Aymen', false) +
    compRow('Revenue, growth trajectory, profitability', 'Folded into corporate overview. 3\u20134 slides.', 'Aymen', false) +
    compRow('R&D investment, 12-month+ roadmap', 'Level 1\u21922\u21923 vision. Banking OS. Agentic Platform. Delivery OS.', 'Ruben', false) +
    compRow('Long-term viability and exit risk', '\u201cWe\u2019re not going anywhere. We don\u2019t need to be acquired.\u201d', 'Aymen', false) +
    compRow('Demonstration of culture to align on vision', '<strong>5 problems + value at stake using ABSA\u2019s own numbers.</strong> R3.5bn cost gap. R1.5\u20132bn attrition. \u201cEach 1pp C/I = R1.16bn.\u201d <em>Culture = showing you understand their world.</em>', '<strong>Shyam</strong>', true) +
    `</div>
    <div style="margin-top:10px;padding:10px 14px;border-radius:8px;border-left:3px solid #3366FF;background:rgba(51,102,255,0.04);font-size:10px;color:#091C35;line-height:1.6">
      <strong style="color:#3366FF">The reframe:</strong> ABSA wrote \u201cdemonstration of culture\u201d as a bullet. Most vendors show a values slide. <strong>We demonstrate culture by mirroring their strategy back with more depth than expected.</strong>
    </div>`
  , bodyFull: true },

  // ═══ 6: ITEM 2 ═══
  { layout: 'content-standard', theme: 'light', label: 'ITEM 2 \u00b7 30 MIN', title: 'Implementation, Experience & Risk', subtitle: '8 bullet points from ABSA. All covered \u2014 risks elevated, demo portal added.', body:
    tableHeader() +
    `<div style="border:1px solid #E2E8F0;border-top:0;border-radius:0 0 8px 8px;overflow:hidden">` +
    compRow('Proposed implementation methodology', 'Phased. Phase 1: 6\u20139 months. MCB: 6 months. 80% OOTB.', 'Thijs', false) +
    compRow('Realistic go-live timeline and milestones', 'Timeline visual. Y0 = setup. Y1 = go-live + upgrade.', 'Thijs', false) +
    compRow('Resource requirements from both sides', 'Joint BB + EY + ABSA. Specific ABSA FTE ask per phase.', 'Thijs', false) +
    compRow('Change management and user adoption', 'EY as local change partner. 70+ practitioners. Deep ABSA knowledge.', 'Marius', false) +
    compRow('Ability to pivot with Absa strategy', 'Digital Factory = built for pivoting. Composable. No lock-in.', 'Thijs', false) +
    compRow('3 main risks, how to manage', '<strong>ABSA-specific:</strong> (1) Co-existence: IBM + MuleSoft. (2) Adoption: new PPB, 10K staff. (3) Scope creep: R16.7bn IT spend. Each with specific mitigation.', '<strong>Jesse</strong>', true) +
    compRow('Contingency if over budget/timeline', 'Phase-gated with value checkpoints. ROI proven before next phase starts.', '<strong>CS</strong>', true) +
    compRow('AI/automation capabilities', 'Delivery OS. AI SDLC agents. 30% efficiency. Moved to Item 3.', 'Ruben', false) +
    compRow('<em>(not asked for)</em>', '<strong>Demo portal reveal.</strong> Localized, branded app left with the bank for 4 months. \u201cNo other vendor did this.\u201d', '<strong>Jesse</strong>', true) +
    `</div>`
  , bodyFull: true },

  // ═══ 7: ITEM 3 ═══
  { layout: 'content-standard', theme: 'light', label: 'ITEM 3 \u00b7 30 MIN', title: 'Ways of Work, Support & SLAs', subtitle: '7 bullet points. Straightforward \u2014 Thijs and Ruben. Add: Delivery OS demo.', body:
    tableHeader() +
    `<div style="border:1px solid #E2E8F0;border-top:0;border-radius:0 0 8px 8px;overflow:hidden">` +
    compRow('Post-go-live support tiers and response times', '24/7 follow-the-sun. P1: 1hr. P2: 1 day. Hypercare 14-day.', 'Ruben', false) +
    compRow('Dedicated account management and escalation', 'One entry point \u2192 4 support areas. Named account team.', 'Ruben', false) +
    compRow('Training and knowledge transfer', 'Digital Factory. \u201cTurbocharge \u2192 Train \u2192 Handover \u2192 Independent.\u201d', 'Thijs', false) +
    compRow('SI ecosystem and self-service resources', 'EY primary SI. Backbase.io. Academy certifications. Partner ecosystem.', 'Thijs', false) +
    compRow('Risk management and outage controls', 'SOC 2. Multi-zone redundancy. Datadog monitoring. Managed Azure.', 'Ruben', false) +
    compRow('Platform upgrades and version management', 'Assess \u2192 Plan \u2192 Validate \u2192 Test \u2192 Deploy. Security patches < 24hrs.', 'Ruben', false) +
    compRow('AI/automation capabilities', '<strong>Delivery OS demo.</strong> AI agents for BA, SA, Dev, UX. 30% efficiency. \u201cNot just support \u2014 continuous acceleration.\u201d', 'Ruben', true) +
    `</div>
    <div style="margin-top:10px;padding:10px 14px;border-radius:8px;border-left:3px solid #059669;background:rgba(5,150,105,0.04);font-size:10px;color:#091C35;line-height:1.6">
      <strong style="color:#059669">The add:</strong> Delivery OS is a competitive differentiator Intellect and Plumery don\u2019t have. Brief demo, not just slides.
    </div>`
  , bodyFull: true },

  // ═══ 8: ITEM 4 ═══
  { layout: 'content-standard', theme: 'light', label: 'ITEM 4 \u00b7 30 MIN', title: 'Pricing, Licensing & Contracting', subtitle: '8 bullet points. All covered \u2014 plus the Investment Logic card for the CFO\u2019s board.', body:
    tableHeader() +
    `<div style="border:1px solid #E2E8F0;border-top:0;border-radius:0 0 8px 8px;overflow:hidden">` +
    compRow('Licensing model', 'Subscription + usage-based. Pay-as-you-grow. Phased activation.', 'Aymen', false) +
    compRow('Implementation and PS costs', 'R95.6M once-off (Y0+Y1). Implementation + customization + migration.', 'Aymen', false) +
    compRow('Hidden costs \u2014 customization, integrations, upgrades', '<strong>Scope evolution slide.</strong> \u201cYour team moved 7 items from optional to mandatory. \u20ac19M \u2192 \u20ac32M = scope validation, not scope creep.\u201d', 'Aymen', true) +
    compRow('Multi-year pricing protection and renewal', '5-year model. 60% discount locked. Per-user R24 (Y1) \u2192 R11 (Y5).', 'Aymen', false) +
    compRow('Contractual protections (IP, data, termination)', '12 min open discussion. Negotiation segment.', 'All', false) +
    compRow('SLA penalties and service credits', 'Per priority level. Response times defined. Credits for breach.', 'All', false) +
    compRow('Liability and indemnification', 'Standard commercial / legal discussion.', 'All', false) +
    compRow('Negotiation flexibility and deal structure', 'If warm: enterprise licensing (retail + SME together). One app option.', 'Aymen', false) +
    compRow('<em>(not asked for)</em>', '<strong>Investment Logic card.</strong> R618M vs R7.1bn = 11.5x return. Conservative: 8.7x. \u201cBy Y5, per-user cost < one branch transaction.\u201d <em>This card is for your board.</em>', '<strong>Shyam</strong>', true) +
    `</div>`
  , bodyFull: true },

  // ═══ 9: ITEM 5 ═══
  { layout: 'content-standard', theme: 'light', label: 'ITEM 5 \u00b7 30 MIN', title: 'Partnership & Relationship Model', subtitle: '5 bullet points. The last one \u2014 \u201cculture demonstration\u201d \u2014 is what matters most.', body:
    tableHeader() +
    `<div style="border:1px solid #E2E8F0;border-top:0;border-radius:0 0 8px 8px;overflow:hidden">` +
    compRow('Strategic vs transactional expectations', '\u201cThis is a transformation partnership, not a software purchase.\u201d Exec sponsor. QBRs.', 'Aymen', false) +
    compRow('Executive sponsorship and governance', 'Joint steering committee with KPIs. Monthly/quarterly cadence.', 'Aymen', false) +
    compRow('Joint success metrics and business reviews', '<strong>Live co-creation.</strong> 8 metrics pre-populated. Amber \u201cABSA Input\u201d columns. \u201cLet\u2019s build this right now.\u201d', '<strong>Shyam / CS</strong>', true) +
    compRow('Supplier\u2019s commitment to success', 'Proof points: demo portal, Ignite model, MCB rollout. \u201cPartnership in practice.\u201d', 'Aymen', false) +
    compRow('Culture demonstration to align on visions', '<strong>The scorecard IS the culture demo.</strong> They co-create an artifact. They leave with something they built. Actions > slides.', '<strong>Shyam / CS</strong>', true) +
    `</div>
    <div style="margin-top:10px;padding:10px 14px;border-radius:8px;border-left:3px solid #7B2FFF;background:rgba(123,47,255,0.04);font-size:10px;color:#091C35;line-height:1.6">
      <strong style="color:#7B2FFF">Why this wins:</strong> \u201cCulture demonstration\u201d appears in both Item 1 AND Item 5. It\u2019s what ABSA cares about most. <strong>We demonstrate culture by co-creating an artifact in the room.</strong> They leave feeling like the partnership has already started.
    </div>`
  , bodyFull: true },

  // ═══ 10: SUMMARY ═══
  { layout: 'content-standard', theme: 'light', label: 'THE BOTTOM LINE', title: '100% Coverage + 41 Minutes of Strategic Value', subtitle: 'Every ABSA bullet point covered. Plus 5 adds no other vendor will bring.', body: `
    <div style="display:flex;gap:16px;width:100%;margin-top:4px">
      <div style="flex:1">
        <div style="font-size:9px;font-weight:800;letter-spacing:2px;color:#3366FF;margin-bottom:10px">THE 5 STRATEGIC ADDS</div>
        <div style="display:flex;flex-direction:column;gap:6px">
          <div style="display:flex;gap:10px;align-items:start;padding:10px 14px;background:#F0F4F8;border-radius:8px;border-left:3px solid #091C35">
            <div style="font-size:18px;font-weight:900;color:#091C35;min-width:20px">1</div>
            <div><div style="font-weight:800;font-size:11px">\u201cThe ABSA Story\u201d opening</div><div style="font-size:9px;color:#64748B;margin-top:2px">5 min. Start with their world, not ours. No slides.</div></div>
          </div>
          <div style="display:flex;gap:10px;align-items:start;padding:10px 14px;background:#F0F4F8;border-radius:8px;border-left:3px solid #3366FF">
            <div style="font-size:18px;font-weight:900;color:#3366FF;min-width:20px">2</div>
            <div><div style="font-weight:800;font-size:11px">ABSA-specific strategic fit analysis</div><div style="font-size:9px;color:#64748B;margin-top:2px">10 min. 5 problems + value at stake. Their own numbers.</div></div>
          </div>
          <div style="display:flex;gap:10px;align-items:start;padding:10px 14px;background:#F0F4F8;border-radius:8px;border-left:3px solid #059669">
            <div style="font-size:18px;font-weight:900;color:#059669;min-width:20px">3</div>
            <div><div style="font-weight:800;font-size:11px">ABSA-specific risk register</div><div style="font-size:9px;color:#64748B;margin-top:2px">8 min. IBM Mainframe + MuleSoft + PPB reorg. Not generic.</div></div>
          </div>
          <div style="display:flex;gap:10px;align-items:start;padding:10px 14px;background:#F0F4F8;border-radius:8px;border-left:3px solid #D97706">
            <div style="font-size:18px;font-weight:900;color:#D97706;min-width:20px">4</div>
            <div><div style="font-weight:800;font-size:11px">CFO Investment Logic card</div><div style="font-size:9px;color:#64748B;margin-top:2px">8 min. R618M vs R7.1bn = 11.5x. Arms the CFO for the board.</div></div>
          </div>
          <div style="display:flex;gap:10px;align-items:start;padding:10px 14px;background:#F0F4F8;border-radius:8px;border-left:3px solid #7B2FFF">
            <div style="font-size:18px;font-weight:900;color:#7B2FFF;min-width:20px">5</div>
            <div><div style="font-weight:800;font-size:11px">Joint success scorecard co-creation</div><div style="font-size:9px;color:#64748B;margin-top:2px">10 min. Live workshop. Culture demonstrated through action.</div></div>
          </div>
        </div>
      </div>
      <div style="flex:0.7">
        <div style="font-size:9px;font-weight:800;letter-spacing:2px;color:#091C35;margin-bottom:10px">BY THE NUMBERS</div>
        <div style="padding:16px;background:#091C35;border-radius:10px;color:#fff;margin-bottom:10px">
          <div style="font-size:32px;font-weight:900;color:#3366FF">34</div>
          <div style="font-size:9px;color:rgba(255,255,255,0.4);margin-top:2px">ABSA bullet points across 5 items</div>
          <div style="font-size:32px;font-weight:900;color:#059669;margin-top:12px">34</div>
          <div style="font-size:9px;color:rgba(255,255,255,0.4);margin-top:2px">covered in our run-of-show</div>
          <div style="font-size:32px;font-weight:900;color:#7B2FFF;margin-top:12px">+5</div>
          <div style="font-size:9px;color:rgba(255,255,255,0.4);margin-top:2px">strategic adds no competitor will have</div>
        </div>
        <div style="padding:12px;border:2px solid rgba(51,102,255,0.2);border-radius:10px;text-align:center">
          <div style="font-size:9px;font-weight:800;color:#3366FF;letter-spacing:1px">SHYAM STAGE TIME</div>
          <div style="font-size:28px;font-weight:900;color:#091C35">~41 min</div>
          <div style="font-size:9px;color:#64748B">of 160 total (26%)</div>
        </div>
      </div>
    </div>
  `, bodyFull: true },

  // ═══ 11: CLOSE ═══
  { layout: 'statement', variant: 'dark', label: 'THE OUTCOME',
    text: 'Same agenda. Same timing. Same bullet points. <span class="hl">Completely different experience.</span>' },

  // ═══ THANK YOU ═══
  { layout: 'thank-you' }
];
