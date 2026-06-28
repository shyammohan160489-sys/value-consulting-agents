window.BB_SHARED_ASSETS = '../backbase-slides-app';

const SPEAKER_NOTES = {
  1: 'Internal playbook — NOT for ABSA. This is the run-of-show for when ABSA\'s Group CIO, CDO, CIO, and CFO visit Amsterdam on 4 May 2026. €32.2M TCV. POC likely for only 1 vendor. Decision by end of May.',
  2: 'The narrative arc: 5 acts, one thread. "We See You → We\'ve Already Started → We Know How → It Makes Sense → Let\'s Build This Together." If any act is skipped, the story breaks.',
  3: 'CRITICAL: None of the 4 executives were at the 2-day RFP defense. They have never seen our product, team, or demos. This is their FIRST impression of Backbase.',
  4: 'Act 1 is the most important 10 minutes. Shyam opens with the ABSA Story — their numbers, not ours. No slides. Eye contact. Then hand to Subash to confirm/adjust.',
  5: 'Act 2: Subash presents ABSA strategy (10 min). Then Shyam mirrors back 5 problems + value at stake (10 min). Aymen covers Backbase corporate (5 min). Ruben covers platform vision (5 min).',
  6: 'Act 3a: Thijs on implementation + demo portal reveal. Shyam on 3 ABSA-specific risks. Marius/EY on local delivery. Q&A buffer.',
  7: 'Act 3b: Digital Factory, support model, Delivery OS, SI ecosystem. Operational reality — what daily life looks like as partners.',
  8: 'Act 4: The CFO moment. Aymen on commercial model + scope evolution (€19M→€32M). Shyam on Investment Logic: R618M vs R7.1bn = 11.5x return. Per-user R11/yr by Year 5.',
  9: 'Act 5: Partnership model + culture demo + Shyam\'s joint scorecard co-creation (the signature move). Close with leave-behind handover.',
  10: 'Shyam presents in 4 interventions across the opening + 4 of 5 agenda items. ~41 minutes stage time. Narrative architect for the full 160 min.',
  11: '14 deliverables to produce before May 4. Shyam owns 5 (blue items). Most are 70-90% done from existing ABSA work.',
  12: 'Prepare honest answers for: TCV sticker shock, "why not Intellect?", Danske reference risk, one-vs-two apps, demo requests, POC criteria.',
  13: 'The goal: they leave Amsterdam feeling like the partnership has already started.'
};

/* ── Helper: Run-of-show block as inline HTML ── */
function ros(time, dur, name, role, title, detail, medium, medNote, isShyam) {
  const bg = isShyam ? 'background:#3366FF;' : 'background:#091C35;';
  const borderStyle = isShyam ? 'border:2px solid #3366FF;' : '';
  return `<div style="display:flex;gap:0;width:100%;border-radius:10px;overflow:hidden;border:1px solid #E2E8F0;margin-bottom:8px;${borderStyle}">
    <div style="min-width:70px;padding:10px;${bg}color:#fff;display:flex;flex-direction:column;justify-content:center;align-items:center">
      <div style="font-size:11px;font-weight:900">${time}</div>
      <div style="font-size:7px;font-weight:600;color:rgba(255,255,255,0.4);text-transform:uppercase;letter-spacing:1px">${dur}</div>
    </div>
    <div style="min-width:85px;padding:10px;background:#F0F4F8;display:flex;flex-direction:column;justify-content:center;border-right:1px solid #E2E8F0">
      <div style="font-size:9px;font-weight:800">${name}</div>
      <div style="font-size:7px;color:#94A3B8">${role}</div>
    </div>
    <div style="flex:1;padding:10px 14px">
      <div style="font-size:11px;font-weight:900;${isShyam ? 'color:#3366FF;' : ''}">${title}</div>
      <div style="font-size:8px;color:#64748B;line-height:1.5;margin-top:3px">${detail}</div>
    </div>
    <div style="min-width:80px;padding:10px;display:flex;flex-direction:column;justify-content:center;align-items:center;border-left:1px solid #E2E8F0">
      <div style="font-size:7px;font-weight:800;letter-spacing:1px;text-transform:uppercase;color:${isShyam ? '#3366FF' : '#64748B'}">${medium}</div>
      <div style="font-size:7px;color:#94A3B8;text-align:center;margin-top:2px">${medNote}</div>
    </div>
  </div>`;
}

function thread(color, text) {
  const colors = { blue: '#3366FF', green: '#059669', amber: '#D97706', purple: '#7B2FFF' };
  const c = colors[color] || colors.blue;
  return `<div style="display:flex;align-items:center;gap:8px;margin:6px 0;padding:7px 14px;border-radius:8px;font-size:9px;font-weight:700;color:${c};background:${c}0F;border-left:3px solid ${c}">&rarr; ${text}</div>`;
}

const SLIDES = [

  // ═══ 1: COVER ═══
  { layout: 'cover-color-block', label: 'ABSA \u00d7 BACKBASE', title: '160 Minutes.\nOne Partnership.', date: 'Internal Playbook \u2014 4 May 2026' },

  // ═══ 2: CONTEXT ═══
  { layout: 'chapter-standard', theme: 'navy', label: 'CONTEXT', title: 'Reading the Room', subtitle: '\u20ac32.2M TCV. 4 senior executives. POC for 1 vendor only. Decision by end of May. None of them were at the RFP defense.' },

  // ═══ 3: THE GOLDEN THREAD ═══
  { layout: 'content-standard', theme: 'light', label: 'THE STORYLINE', title: 'One Story in Five Acts: \u201cFrom Vendor to Partner\u201d', subtitle: 'Every minute serves one narrative arc. Here\u2019s the thread that connects all 5 agenda items.', body: `
    <div style="display:flex;gap:0;width:100%;margin-bottom:14px">
      <div style="flex:1;padding:14px;background:#091C35;color:#fff;border-radius:10px 0 0 10px">
        <div style="font-size:7px;font-weight:800;letter-spacing:2px;color:rgba(255,255,255,0.35)">ACT 1 \u00b7 10 MIN</div>
        <div style="font-size:13px;font-weight:900;margin:4px 0">\u201cWe See You\u201d</div>
        <p style="font-size:8px;color:rgba(255,255,255,0.5);line-height:1.4">Open with ABSA\u2019s world. Their numbers, their challenges. No Backbase slides. Pure empathy.</p>
      </div>
      <div style="flex:1;padding:14px;background:rgba(51,102,255,0.06);border-top:1px solid #E2E8F0;border-bottom:1px solid #E2E8F0">
        <div style="font-size:7px;font-weight:800;letter-spacing:2px;color:#3366FF">ACT 2 \u00b7 30 MIN</div>
        <div style="font-size:13px;font-weight:900;margin:4px 0">\u201cWe\u2019ve Already Started\u201d</div>
        <p style="font-size:8px;color:#64748B;line-height:1.4">Strategic depth. 5 problems. Value at stake. 3-phase plan. Think like a partner, not a vendor.</p>
      </div>
      <div style="flex:1;padding:14px;background:rgba(5,150,105,0.06);border-top:1px solid #E2E8F0;border-bottom:1px solid #E2E8F0">
        <div style="font-size:7px;font-weight:800;letter-spacing:2px;color:#059669">ACT 3 \u00b7 60 MIN</div>
        <div style="font-size:13px;font-weight:900;margin:4px 0">\u201cWe Know How\u201d</div>
        <p style="font-size:8px;color:#64748B;line-height:1.4">Implementation reality. Real risks, real mitigations. Delivery OS. Demo portal reveal.</p>
      </div>
      <div style="flex:1;padding:14px;background:rgba(217,119,6,0.06);border-top:1px solid #E2E8F0;border-bottom:1px solid #E2E8F0">
        <div style="font-size:7px;font-weight:800;letter-spacing:2px;color:#D97706">ACT 4 \u00b7 30 MIN</div>
        <div style="font-size:13px;font-weight:900;margin:4px 0">\u201cIt Makes Sense\u201d</div>
        <p style="font-size:8px;color:#64748B;line-height:1.4">The CFO moment. R618M vs R7.1bn = 11.5x. Per-user cost drops to R11/yr. The math works.</p>
      </div>
      <div style="flex:1;padding:14px;background:rgba(123,47,255,0.06);border-radius:0 10px 10px 0;border:1px solid #E2E8F0;border-left:0">
        <div style="font-size:7px;font-weight:800;letter-spacing:2px;color:#7B2FFF">ACT 5 \u00b7 30 MIN</div>
        <div style="font-size:13px;font-weight:900;margin:4px 0">\u201cLet\u2019s Build This\u201d</div>
        <p style="font-size:8px;color:#64748B;line-height:1.4">Joint scorecard. Co-creation. Culture in action. The emotional close.</p>
      </div>
    </div>
    <div style="padding:12px 16px;border-radius:8px;border:1px solid rgba(51,102,255,0.2);background:rgba(51,102,255,0.03);margin-bottom:8px">
      <div style="font-size:9px;font-weight:800;color:#3366FF;letter-spacing:1px;margin-bottom:4px">THE GOLDEN THREAD</div>
      <p style="font-size:10px;color:#091C35;line-height:1.6">Every act builds on the one before. Act 1 creates empathy. Act 2 earns the right to advise. Act 3 proves you can deliver. Act 4 shows the math works. Act 5 makes them feel what partnership looks like. <strong>If any act is skipped, the story breaks.</strong></p>
    </div>
    <div style="padding:10px 16px;border-radius:8px;border:1px solid rgba(220,38,38,0.2);background:rgba(220,38,38,0.03)">
      <div style="font-size:9px;font-weight:800;color:#DC2626;letter-spacing:1px;margin-bottom:3px">CRITICAL: NONE OF THEM WERE AT THE RFP DEFENSE</div>
      <p style="font-size:9px;color:#64748B;line-height:1.5">Johnson, Subash, Thatayaone, and Christopher have never seen our product, team, or demos. The demo portal (localized, branded, installable) is our secret weapon \u2014 show it briefly but don\u2019t re-demo.</p>
    </div>
  `, bodyFull: true },

  // ═══ 4: ACT 1 — OPENING ═══
  { layout: 'content-standard', theme: 'light', label: 'ACT 1 \u2014 OPENING & WELCOME \u00b7 10 MINUTES', title: '\u201cWe See You\u201d \u2014 Tell Their Story, Not Ours', subtitle: 'The most important 5 minutes of the day. Set the tone before anyone opens a deck.', body:
    ros('0:00', '3 min', 'Aymen', 'RVP Sales', 'Welcome & Introductions', 'Round-the-table introductions \u2014 name, role, one sentence. <strong>No corporate history.</strong>', 'Standing', 'No slides', false) +
    ros('0:03', '5 min', 'Shyam', 'Value Consultant', '\u201cThe ABSA Story\u201d \u2014 3 Beats', '<strong>Beat 1 (2 min):</strong> \u201cHere\u2019s what we see.\u201d R115.7bn revenue. CIB at 21% ROE. Retail losing 300K/yr. NPS 15% vs Capitec 45%. C/I at 53.8%.<br><strong>Beat 2 (2 min):</strong> \u201cHere\u2019s why now.\u201d New PPB division. CEO Fihla. R16.7bn IT investment. The window for a platform decision.<br><strong>Beat 3 (1 min):</strong> \u201cHere\u2019s how we\u2019d measure it.\u201d Plant the seed for Act 5.', 'Conversation', 'No slides.\nEye contact.', true) +
    ros('0:08', '2 min', 'Subash', 'CDO, ABSA', 'ABSA Responds / Aligns', '\u201cSubash, does that resonate?\u201d Let ABSA confirm or adjust our understanding. This validates our homework.', 'Dialogue', 'Listen mode', false) +
    thread('blue', 'We\u2019ve earned the right to advise. Now Subash presents their strategy, and we respond with strategic fit (Act 2).')
  , bodyFull: true },

  // ═══ 5: ACT 2 — STRATEGIC ALIGNMENT ═══
  { layout: 'content-standard', theme: 'light', label: 'ACT 2 \u2014 STRATEGIC ALIGNMENT \u00b7 30 MINUTES', title: '\u201cWe\u2019ve Already Started Thinking Like Your Partner\u201d', subtitle: 'ABSA presents their strategy (10 min). Then we respond with depth no other vendor will have (20 min).', body:
    ros('0:10', '10 min', 'Subash', 'CDO, ABSA', 'ABSA Digital Transformation Strategy', 'Subash presents their vision. <strong>LISTEN DEEPLY.</strong> Take notes. Watch body language from Johnson and Christopher \u2014 what gets nods?', 'ABSA slides', 'Active listening', false) +
    ros('0:20', '10 min', 'Shyam', 'Value Consultant', 'Strategic Fit \u2014 5 Problems & Value at Stake', '<strong>Mirror back:</strong> \u201cBased on what Subash shared and our research, we see 5 interconnected challenges.\u201d P1\u2013P5 cards. Then value at stake: R3.5bn cost gap + R1.5\u20132bn attrition + R1.6bn ROE bridge. <strong>Use ABSA\u2019s own published numbers.</strong><br><em style="color:#3366FF">Key line for CFO: \u201cEach 1pp C/I improvement = R1.16bn in annual savings.\u201d</em>', 'Slides', 'Exec summary\nscenes 2\u20133', true) +
    ros('0:30', '5 min', 'Aymen', 'RVP Sales', 'Backbase Strategy, Financial Health & R&D', 'Privately held, no acquisition risk. 50%+ R&D. 12-month+ roadmap. \u201cWe\u2019re not going anywhere. Our business model is aligned with yours.\u201d', 'Slides', 'Corporate\n3\u20134 slides', false) +
    ros('0:35', '5 min', 'Ruben', 'Field CTO', 'Platform Vision & Roadmap', 'Level 1 \u2192 Level 2 \u2192 Level 3 (Digital Experience \u2192 Unified Frontline \u2192 Agentic Workforce). \u201cABSA is choosing a platform for the next decade.\u201d', 'Slides', 'Banking OS\nvision', false) +
    thread('green', 'We understand their world AND we have the platform vision. Now prove we can deliver (Act 3).')
  , bodyFull: true },

  // ═══ 6: ACT 3A — IMPLEMENTATION & RISK ═══
  { layout: 'content-standard', theme: 'light', label: 'ACT 3A \u2014 IMPLEMENTATION & RISK \u00b7 30 MINUTES', title: '\u201cWe Know How \u2014 and Where It Gets Hard\u201d', subtitle: 'Trust is built through honesty about complexity, not polish.', body:
    ros('0:40', '10 min', 'Thijs', 'VP Services', 'Implementation Methodology & Timeline', 'Phased approach. Phase 1: 6\u20139 months to MVP (cite MCB: 6 months). Resource model: joint BB + EY + ABSA team.<br><strong>Demo portal reveal (2 min):</strong> \u201cYour team has been testing our platform for 4 months. Here\u2019s the localized environment we left behind.\u201d <em>No other vendor did this.</em>', 'Slides +\nLive portal', 'RFP slides\n231\u2013232', false) +
    ros('0:50', '8 min', 'Shyam', 'Value Consultant', 'The 3 Risks That Keep ABSA Leadership Awake', '<strong>Risk 1: Co-existence.</strong> IBM Mainframe + MuleSoft + engagement layer. \u201cCo-existence IS our architecture.\u201d<br><strong>Risk 2: Adoption.</strong> New PPB division, 10K+ employees. Digital Factory + Academy + EY.<br><strong>Risk 3: Scope creep.</strong> R16.7bn IT spend. Phase-gated with value checkpoints. 80% OOTB.<br><em style="color:#DC2626">Tone: honest, not salesy. \u201cWe\u2019re not pretending this is easy.\u201d</em>', 'Slides', 'Risk register\n(new asset)', true) +
    ros('0:58', '5 min', 'Marius', 'EY Partner', 'EY as Local Delivery & Change Partner', 'EY\u2019s institutional knowledge of ABSA. 70+ practitioners enabled on Backbase. \u201cWe\u2019re bringing people who already know your organization.\u201d', 'Conversation', 'EY credibility', false) +
    ros('1:03', '7 min', 'All', 'Q&A', 'Questions from ABSA Delegation', 'Expect probing from Thatayaone (CIO) on resources. Johnson on contingency. <strong>Have Thijs ready with ABSA FTE requirements per phase.</strong>', 'Open floor', 'Be honest', false) +
    thread('green', 'They believe we can deliver. Now show how day-to-day works (Act 3B).')
  , bodyFull: true },

  // ═══ 7: ACT 3B — WAYS OF WORK ═══
  { layout: 'content-standard', theme: 'light', label: 'ACT 3B \u2014 WAYS OF WORK & SUPPORT \u00b7 30 MINUTES', title: '\u201cThis Is How We Work Together, Every Day\u201d', subtitle: 'The \u201cafter the handshake\u201d session. What does daily life look like?', body:
    ros('1:10', '10 min', 'Thijs', 'VP Services', 'Digital Factory & Knowledge Transfer', 'Digital Factory operating model. \u201cTurbocharge with BB \u2192 Training \u2192 Handover \u2192 Independent.\u201d Academy \u2192 Bootcamp \u2192 Hub. \u201cWe don\u2019t create dependency. We transfer ownership.\u201d', 'Slides', 'RFP slides\n234, 241\u2013242', false) +
    ros('1:20', '8 min', 'Ruben', 'Field CTO', 'Support Model, SLAs & Delivery OS', '24/7 follow-the-sun. P1 response: 1 hour. Hypercare 14-day. <strong>Delivery OS:</strong> AI-accelerated SDLC \u2014 30% more efficient, smaller teams. \u201cContinuous acceleration, not just support.\u201d', 'Slides +\nBrief demo', 'Delivery OS\n184\u2013193', false) +
    ros('1:28', '5 min', 'Thijs', 'VP Services', 'SI Ecosystem & Self-Service', 'EY as primary SI. Backbase.io developer portal. Academy certifications. \u201cYou\u2019re enabled to self-serve.\u201d', 'Slides', 'Partner model', false) +
    ros('1:33', '7 min', 'All', 'Q&A', 'Questions from ABSA Delegation', 'Johnson: upgrade paths. Thatayaone: outage controls. Christopher: run costs mentally. <strong>Have SLA penalty specifics ready.</strong>', 'Open floor', '7 min buffer', false) +
    thread('amber', 'They trust the delivery model. Now make the economics irresistible (Act 4).')
  , bodyFull: true },

  // ═══ 8: ACT 4 — PRICING ═══
  { layout: 'content-standard', theme: 'light', label: 'ACT 4 \u2014 PRICING & CONTRACTING \u00b7 30 MINUTES', title: '\u201cThe Investment Makes Sense\u201d', subtitle: 'Christopher Snyman\u2019s session. Don\u2019t just present pricing \u2014 present the investment logic.', body:
    ros('1:40', '5 min', 'Aymen', 'RVP Sales', 'Commercial Model Overview', 'Licensing: subscription, usage-based, pay-as-you-grow. Phased activation. 60% discount from list. \u201cYou pay for what you use, when you use it.\u201d', 'Slides', 'Commercial\nmodel', false) +
    ros('1:45', '5 min', 'Aymen', 'RVP Sales', 'Scope Evolution: Retail to Enterprise', 'Address TCV increase: \u201cYour team saw the platform. They moved 7 capabilities from optional to mandatory. The scope grew because value was proven.\u201d <strong>Position SME/Business Banking option. One app vs two \u2014 get a directional read.</strong>', 'Slides', 'Scope evolution\n(new slide)', false) +
    ros('1:50', '8 min', 'Shyam', 'Value Consultant', 'Investment Logic: The Business Case', '<strong>The CFO card.</strong> R618M 5-year investment vs R7.1bn base-case 3-year value = 11.5x return. Even conservative: 8.7x.<br>Per-user: R24.48 (Y1) \u2192 R11.21 (Y5). <strong>\u201cBy Year 5, per-user cost is less than a single branch transaction.\u201d</strong><br>Sensitivity: R5.4bn | R7.1bn | R10.7bn. <em>\u201cThis card is yours for the board. Every number from your annual report.\u201d</em>', 'CFO card', 'Leave-behind\n(new asset)', true) +
    ros('1:58', '12 min', 'All', 'Negotiation', 'Contracting & Negotiation Flexibility', 'IP ownership, data portability, termination. SLA penalties. <strong>If warm:</strong> explore enterprise licensing \u2014 \u201cretail + business banking together.\u201d', 'Discussion', 'Read the room', false) +
    thread('purple', 'The math works. The contract is negotiable. Now close on the relationship (Act 5).')
  , bodyFull: true },

  // ═══ 9: ACT 5 — PARTNERSHIP ═══
  { layout: 'content-standard', theme: 'light', label: 'ACT 5 \u2014 PARTNERSHIP MODEL \u00b7 30 MINUTES', title: '\u201cLet\u2019s Build This Together\u201d', subtitle: 'The emotional close. Don\u2019t present a slide about partnership. Demonstrate it live.', body:
    ros('2:10', '8 min', 'Aymen', 'RVP Sales', 'Partnership Model & Executive Sponsorship', 'Strategic vs transactional. Named exec sponsor. Quarterly business reviews. Joint steering committee. \u201cThis is not a software purchase. This is a transformation partnership.\u201d', 'Slides', 'Partnership\nmodel', false) +
    ros('2:18', '5 min', 'Aymen', 'RVP Sales', 'Culture Demo: How Clients Experience Backbase', '2\u20133 proof points: localized demo portal, Ignite value advisory, MCB multi-country rollout. \u201cPartnership in practice, not in theory.\u201d', 'Stories', 'Customer proof', false) +
    ros('2:23', '10 min', 'Shyam', 'Value Consultant', 'Joint Success Scorecard \u2014 Live Co-Creation', '<strong>The signature move.</strong> 8 metrics across Customer Impact, Ops Efficiency, Delivery Health. Amber columns = \u201cABSA Input.\u201d<br><em style="color:#3366FF">\u201cWe\u2019ve drafted what success looks like. The amber columns are yours. What would you set as targets? Let\u2019s build this right now.\u201d</em><br>Invite Johnson or Subash to react. Capture input. They co-create an artifact. <strong>THIS is the culture demonstration.</strong>', 'Workshop', 'Scorecard\nprinted +\non screen', true) +
    ros('2:33', '5 min', 'Aymen', 'RVP Sales', 'Closing & Next Steps', 'Summarize the day in 3 sentences. Confirm next steps: reference check, POC timeline. <strong>Hand over the leave-behind</strong> (outside-in HTML or printed doc). \u201cSomething for your board.\u201d', 'Standing', 'Leave-behind\nhandover', false) +
    thread('purple', 'They leave Amsterdam having co-created something with us. That\u2019s not a vendor meeting. That\u2019s a partnership kickoff.')
  , bodyFull: true },

  // ═══ 10: SHYAM'S ROLE ═══
  { layout: 'content-standard', theme: 'light', label: 'SHYAM\u2019S CONTRIBUTION MAP', title: 'Where Shyam Presents, What He Delivers', subtitle: '4 interventions across 160 minutes. ~41 minutes stage time. Narrative architect throughout.', body: `
    <div style="display:grid;grid-template-columns:1fr 1fr 1fr 1fr;gap:12px;margin-bottom:14px">
      <div style="border-radius:10px;padding:14px;border-top:4px solid #091C35;background:#fff;border:1px solid #E2E8F0">
        <div style="font-size:8px;font-weight:800;color:#94A3B8;letter-spacing:1px">0:03 \u2014 ACT 1</div>
        <div style="font-size:14px;font-weight:900;margin:4px 0">\u201cThe ABSA Story\u201d</div>
        <div style="font-size:24px;font-weight:900;color:#3366FF">5 min</div>
        <p style="font-size:8px;color:#64748B;margin-top:4px">No slides. Eye contact. Mirror their world. Plant scorecard seed.</p>
      </div>
      <div style="border-radius:10px;padding:14px;border-top:4px solid #3366FF;background:#fff;border:1px solid #E2E8F0">
        <div style="font-size:8px;font-weight:800;color:#94A3B8;letter-spacing:1px">0:20 \u2014 ACT 2</div>
        <div style="font-size:14px;font-weight:900;margin:4px 0">Strategic Fit</div>
        <div style="font-size:24px;font-weight:900;color:#3366FF">10 min</div>
        <p style="font-size:8px;color:#64748B;margin-top:4px">5 problems. Value at stake. ABSA-specific analysis. Biggest differentiator.</p>
      </div>
      <div style="border-radius:10px;padding:14px;border-top:4px solid #059669;background:#fff;border:1px solid #E2E8F0">
        <div style="font-size:8px;font-weight:800;color:#94A3B8;letter-spacing:1px">0:50 \u2014 ACT 3</div>
        <div style="font-size:14px;font-weight:900;margin:4px 0">Risk Register</div>
        <div style="font-size:24px;font-weight:900;color:#059669">8 min</div>
        <p style="font-size:8px;color:#64748B;margin-top:4px">3 ABSA-specific risks. Honest, not salesy. Builds trust.</p>
      </div>
      <div style="border-radius:10px;padding:14px;border-top:4px solid #7B2FFF;background:#fff;border:1px solid #E2E8F0">
        <div style="font-size:8px;font-weight:800;color:#94A3B8;letter-spacing:1px">1:50 + 2:23 \u2014 ACT 4+5</div>
        <div style="font-size:14px;font-weight:900;margin:4px 0">CFO Card +<br>Scorecard</div>
        <div style="font-size:24px;font-weight:900;color:#7B2FFF">18 min</div>
        <p style="font-size:8px;color:#64748B;margin-top:4px">Investment logic for Snyman. Then the co-creation close.</p>
      </div>
    </div>
    <div style="padding:14px 18px;border-radius:10px;border:2px solid rgba(51,102,255,0.2);background:rgba(51,102,255,0.03);display:flex;justify-content:space-between;align-items:center">
      <div>
        <div style="font-size:9px;font-weight:800;color:#3366FF;letter-spacing:1px">TOTAL SHYAM STAGE TIME</div>
        <div style="font-size:28px;font-weight:900">~41 minutes</div>
        <div style="font-size:9px;color:#64748B">of 160 total (26%) \u2014 present in opening + 4 of 5 agenda items</div>
      </div>
      <div style="text-align:right">
        <div style="font-size:9px;font-weight:800;color:#3366FF;letter-spacing:1px">BEHIND THE SCENES</div>
        <div style="font-size:13px;font-weight:700">Narrative architect for the full 160 min</div>
        <div style="font-size:9px;color:#64748B">Structure, storyline, talking points, visual direction for all speakers</div>
      </div>
    </div>
  `, bodyFull: true },

  // ═══ 11: BUILD LIST ═══
  { layout: 'content-standard', theme: 'light', label: 'DELIVERABLES', title: 'What We Need to Build Before May 4', subtitle: '14 assets. Owners assigned. Green = exists. Amber = to build. Red = critical new.', body: `
    <div style="border-radius:10px;overflow:hidden;border:1px solid #E2E8F0;font-size:10px">
      <table style="width:100%;border-collapse:collapse">
        <thead><tr style="background:#091C35;color:#fff;font-size:8px;font-weight:800;letter-spacing:1px;text-transform:uppercase">
          <th style="padding:8px 10px;text-align:left;width:30px">#</th>
          <th style="padding:8px 10px;text-align:left">Asset</th>
          <th style="padding:8px 10px;text-align:left;width:80px">Owner</th>
          <th style="padding:8px 10px;text-align:left;width:60px">Act</th>
          <th style="padding:8px 10px;text-align:center;width:70px">Status</th>
        </tr></thead>
        <tbody>
          <tr style="border-bottom:1px solid #E2E8F0"><td style="padding:6px 10px;font-weight:900">1</td><td style="padding:6px 10px;font-weight:700">\u201cThe ABSA Story\u201d talking track</td><td style="padding:6px 10px">Shyam</td><td style="padding:6px 10px">1</td><td style="padding:6px 10px;text-align:center"><span style="background:rgba(5,150,105,0.1);color:#059669;padding:2px 8px;border-radius:10px;font-size:8px;font-weight:700">80%</span></td></tr>
          <tr style="border-bottom:1px solid #E2E8F0;background:#F0F4F8"><td style="padding:6px 10px;font-weight:900">2</td><td style="padding:6px 10px;font-weight:700">Strategic Fit slides (5 problems + value)</td><td style="padding:6px 10px">Shyam</td><td style="padding:6px 10px">2</td><td style="padding:6px 10px;text-align:center"><span style="background:rgba(5,150,105,0.1);color:#059669;padding:2px 8px;border-radius:10px;font-size:8px;font-weight:700">90%</span></td></tr>
          <tr style="border-bottom:1px solid #E2E8F0"><td style="padding:6px 10px;font-weight:900">3</td><td style="padding:6px 10px">BB corporate & financial health</td><td style="padding:6px 10px">Aymen</td><td style="padding:6px 10px">2</td><td style="padding:6px 10px;text-align:center"><span style="background:rgba(217,119,6,0.1);color:#D97706;padding:2px 8px;border-radius:10px;font-size:8px;font-weight:700">To build</span></td></tr>
          <tr style="border-bottom:1px solid #E2E8F0;background:#F0F4F8"><td style="padding:6px 10px;font-weight:900">4</td><td style="padding:6px 10px">Platform vision & roadmap</td><td style="padding:6px 10px">Ruben</td><td style="padding:6px 10px">2</td><td style="padding:6px 10px;text-align:center"><span style="background:rgba(5,150,105,0.1);color:#059669;padding:2px 8px;border-radius:10px;font-size:8px;font-weight:700">Exists</span></td></tr>
          <tr style="border-bottom:1px solid #E2E8F0"><td style="padding:6px 10px;font-weight:900">5</td><td style="padding:6px 10px">Implementation timeline + milestones</td><td style="padding:6px 10px">Thijs</td><td style="padding:6px 10px">3a</td><td style="padding:6px 10px;text-align:center"><span style="background:rgba(5,150,105,0.1);color:#059669;padding:2px 8px;border-radius:10px;font-size:8px;font-weight:700">Exists</span></td></tr>
          <tr style="border-bottom:1px solid #E2E8F0;background:#F0F4F8"><td style="padding:6px 10px;font-weight:900">6</td><td style="padding:6px 10px">Demo portal walkthrough (2 min)</td><td style="padding:6px 10px">Jesse</td><td style="padding:6px 10px">3a</td><td style="padding:6px 10px;text-align:center"><span style="background:rgba(5,150,105,0.1);color:#059669;padding:2px 8px;border-radius:10px;font-size:8px;font-weight:700">Live</span></td></tr>
          <tr style="border-bottom:1px solid #E2E8F0"><td style="padding:6px 10px;font-weight:900">7</td><td style="padding:6px 10px;font-weight:700">Risk Register (3 ABSA risks)</td><td style="padding:6px 10px">Shyam</td><td style="padding:6px 10px">3a</td><td style="padding:6px 10px;text-align:center"><span style="background:rgba(5,150,105,0.1);color:#059669;padding:2px 8px;border-radius:10px;font-size:8px;font-weight:700">80%</span></td></tr>
          <tr style="border-bottom:1px solid #E2E8F0;background:#F0F4F8"><td style="padding:6px 10px;font-weight:900">8</td><td style="padding:6px 10px">Digital Factory & support slides</td><td style="padding:6px 10px">Thijs</td><td style="padding:6px 10px">3b</td><td style="padding:6px 10px;text-align:center"><span style="background:rgba(5,150,105,0.1);color:#059669;padding:2px 8px;border-radius:10px;font-size:8px;font-weight:700">Exists</span></td></tr>
          <tr style="border-bottom:1px solid #E2E8F0"><td style="padding:6px 10px;font-weight:900">9</td><td style="padding:6px 10px">Delivery OS slides + demo</td><td style="padding:6px 10px">Ruben</td><td style="padding:6px 10px">3b</td><td style="padding:6px 10px;text-align:center"><span style="background:rgba(5,150,105,0.1);color:#059669;padding:2px 8px;border-radius:10px;font-size:8px;font-weight:700">Exists</span></td></tr>
          <tr style="border-bottom:1px solid #E2E8F0;background:#F0F4F8"><td style="padding:6px 10px;font-weight:900">10</td><td style="padding:6px 10px">Commercial model + scope evolution</td><td style="padding:6px 10px">Aymen</td><td style="padding:6px 10px">4</td><td style="padding:6px 10px;text-align:center"><span style="background:rgba(217,119,6,0.1);color:#D97706;padding:2px 8px;border-radius:10px;font-size:8px;font-weight:700">To build</span></td></tr>
          <tr style="border-bottom:1px solid #E2E8F0"><td style="padding:6px 10px;font-weight:900;color:#3366FF">11</td><td style="padding:6px 10px;font-weight:700;color:#3366FF">CFO Investment Logic card</td><td style="padding:6px 10px;font-weight:700">Shyam</td><td style="padding:6px 10px">4</td><td style="padding:6px 10px;text-align:center"><span style="background:rgba(220,38,38,0.1);color:#DC2626;padding:2px 8px;border-radius:10px;font-size:8px;font-weight:700">To build</span></td></tr>
          <tr style="border-bottom:1px solid #E2E8F0;background:#F0F4F8"><td style="padding:6px 10px;font-weight:900">12</td><td style="padding:6px 10px">Partnership model slides</td><td style="padding:6px 10px">Aymen</td><td style="padding:6px 10px">5</td><td style="padding:6px 10px;text-align:center"><span style="background:rgba(217,119,6,0.1);color:#D97706;padding:2px 8px;border-radius:10px;font-size:8px;font-weight:700">To build</span></td></tr>
          <tr style="border-bottom:1px solid #E2E8F0"><td style="padding:6px 10px;font-weight:900;color:#3366FF">13</td><td style="padding:6px 10px;font-weight:700;color:#3366FF">Joint Success Scorecard</td><td style="padding:6px 10px;font-weight:700">Shyam</td><td style="padding:6px 10px">5</td><td style="padding:6px 10px;text-align:center"><span style="background:rgba(5,150,105,0.1);color:#059669;padding:2px 8px;border-radius:10px;font-size:8px;font-weight:700">80%</span></td></tr>
          <tr><td style="padding:6px 10px;font-weight:900;color:#3366FF">14</td><td style="padding:6px 10px;font-weight:700;color:#3366FF">Outside-in leave-behind</td><td style="padding:6px 10px;font-weight:700">Shyam</td><td style="padding:6px 10px">Post</td><td style="padding:6px 10px;text-align:center"><span style="background:rgba(5,150,105,0.1);color:#059669;padding:2px 8px;border-radius:10px;font-size:8px;font-weight:700">70%</span></td></tr>
        </tbody>
      </table>
    </div>
  `, bodyFull: true },

  // ═══ 12: DANGER ZONES ═══
  { layout: 'content-standard', theme: 'light', label: 'DANGER ZONES & PREPARATION', title: 'What Could Go Wrong \u2014 and How to Handle It', subtitle: 'Anticipate the hard questions. Prepare the honest answers.', body: `
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:10px">
      <div style="border-radius:10px;padding:14px;border:1px solid rgba(220,38,38,0.15);border-top:3px solid #DC2626">
        <div style="font-size:8px;font-weight:800;color:#DC2626;letter-spacing:1px;margin-bottom:3px">DANGER: TCV STICKER SHOCK</div>
        <p style="font-size:9px;color:#64748B;line-height:1.4"><strong>Trigger:</strong> Christopher sees \u20ac32.2M (up from \u20ac19M). \u201cWhy did this nearly double?\u201d</p>
        <p style="font-size:9px;color:#091C35;line-height:1.4;margin-top:3px"><strong>Response:</strong> \u201cYour team moved 7 capabilities from optional to mandatory. This isn\u2019t scope creep \u2014 it\u2019s scope validation. At R11/user/year by Y5, you\u2019re paying less per customer than a branch visit.\u201d</p>
      </div>
      <div style="border-radius:10px;padding:14px;border:1px solid rgba(217,119,6,0.15);border-top:3px solid #D97706">
        <div style="font-size:8px;font-weight:800;color:#D97706;letter-spacing:1px;margin-bottom:3px">DANGER: \u201cONE APP OR TWO APPS?\u201d</div>
        <p style="font-size:9px;color:#64748B;line-height:1.4"><strong>Trigger:</strong> The SME question is still open. They might ask us to decide.</p>
        <p style="font-size:9px;color:#091C35;line-height:1.4;margin-top:3px"><strong>Response:</strong> \u201cOur recommendation: one app with segment-driven UX. One login, one relationship, seamless cross-sell between personal and business.\u201d</p>
      </div>
      <div style="border-radius:10px;padding:14px;border:1px solid rgba(217,119,6,0.15);border-top:3px solid #D97706">
        <div style="font-size:8px;font-weight:800;color:#D97706;letter-spacing:1px;margin-bottom:3px">DANGER: \u201cWHY NOT INTELLECT?\u201d</div>
        <p style="font-size:9px;color:#64748B;line-height:1.4"><strong>Trigger:</strong> Johnson asks why engagement layer vs full-stack core+channels.</p>
        <p style="font-size:9px;color:#091C35;line-height:1.4;margin-top:3px"><strong>Response:</strong> \u201cYou\u2019ve invested in your core and MuleSoft. An engagement layer preserves those investments. Your team called it \u2018build, launch, hollow.\u2019 That\u2019s exactly what we enable.\u201d</p>
      </div>
      <div style="border-radius:10px;padding:14px;border:1px solid rgba(217,119,6,0.15);border-top:3px solid #D97706">
        <div style="font-size:8px;font-weight:800;color:#D97706;letter-spacing:1px;margin-bottom:3px">DANGER: \u201cCAN WE SEE A DEMO?\u201d</div>
        <p style="font-size:9px;color:#64748B;line-height:1.4"><strong>Trigger:</strong> Executives who missed the defense want to see product live.</p>
        <p style="font-size:9px;color:#091C35;line-height:1.4;margin-top:3px"><strong>Response:</strong> Show demo portal briefly. \u201cThe app is on test devices right here. We\u2019ll set up a session over lunch.\u201d Have Jesse ready with devices.</p>
      </div>
      <div style="border-radius:10px;padding:14px;border:1px solid rgba(217,119,6,0.15);border-top:3px solid #D97706">
        <div style="font-size:8px;font-weight:800;color:#D97706;letter-spacing:1px;margin-bottom:3px">DANGER: DANSKE REFERENCE GOES WRONG</div>
        <p style="font-size:9px;color:#64748B;line-height:1.4"><strong>Trigger:</strong> Reference check before visit. Danske mentions go-live delays.</p>
        <p style="font-size:9px;color:#091C35;line-height:1.4;margin-top:3px"><strong>Response:</strong> \u201cDanske\u2019s timeline reflects internal complexity, not platform limitations. That\u2019s why we\u2019re investing in Digital Factory + EY for ABSA.\u201d <em>Check with Ilko before the visit.</em></p>
      </div>
      <div style="border-radius:10px;padding:14px;border:1px solid rgba(5,150,105,0.15);border-top:3px solid #059669">
        <div style="font-size:8px;font-weight:800;color:#059669;letter-spacing:1px;margin-bottom:3px">OPPORTUNITY: POC CONVERSATION</div>
        <p style="font-size:9px;color:#64748B;line-height:1.4"><strong>Signal:</strong> If warm by Act 5, probe: \u201cWhat would a successful POC look like?\u201d</p>
        <p style="font-size:9px;color:#091C35;line-height:1.4;margin-top:3px"><strong>Intel:</strong> Deputy CDO said POC likely for 1 vendor only. Decision by end May. <strong>Win Amsterdam = win POC = win deal. Don\u2019t leave without understanding their POC criteria.</strong></p>
      </div>
    </div>
  `, bodyFull: true },

  // ═══ 13: THE CLOSE ═══
  { layout: 'statement', variant: 'dark', label: 'THE CLOSE',
    text: 'They should leave Amsterdam feeling like <span class="hl">the partnership has already started.</span>' },

  // ═══ 14: THANK YOU ═══
  { layout: 'thank-you' }
];
