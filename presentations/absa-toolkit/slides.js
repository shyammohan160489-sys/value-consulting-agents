window.BB_SHARED_ASSETS = '../backbase-slides-app';

const SPEAKER_NOTES = {
  1: 'This is Shyam\'s complete toolkit for Amsterdam. Contains all 4 planned interventions PLUS 3 above-and-beyond differentiators. Use selectively — not every slide needs to be shown. The deck is a toolkit, not a script.',
  2: 'Your 4 planned interventions + 3 extras that go beyond what ABSA asked for.',
  3: 'INTERVENTION 1: The ABSA Story. This is a TALKING TRACK, not a slide deck. These speaker notes are your script. Make eye contact. No slides on screen.',
  4: 'Beat 1: The numbers. All from ABSA\'s 2025 Annual Report. Don\'t rush — let each number land. Pause after "300,000 customers a year."',
  5: 'Beat 2: The timing. This is emotional — "the window is now." Connect to Kenny Fihla\'s public commitment.',
  6: 'Beat 3: Plant the seed for Act 5. Don\'t elaborate — just name the metrics. "We\'ll come back to this at the end."',
  8: 'INTERVENTION 2: Strategic Fit. This is where you earn the right to advise. Use ABSA\'s own numbers. The CFO will notice that every data point is sourced.',
  9: 'Five problems, not features. Each one maps to a strategic imperative from ABSA\'s own annual report and CEO statements.',
  10: 'Value at stake. The single most important slide for the CFO. "Each 1pp C/I improvement = R1.16bn." Let that land.',
  12: 'INTERVENTION 3: Risk Register. Tone is HONEST, not salesy. "We\'re not pretending this is easy." Name their specific systems — IBM Mainframe, MuleSoft. They\'ll respect the specificity.',
  13: 'Three risks, each with a concrete mitigation grounded in their own environment. Not generic consulting speak.',
  15: 'INTERVENTION 4: Investment Logic. This is the CFO\'s moment. Frame the €32M not as a cost but as an investment with an 11.5x return.',
  16: 'The card itself. Print this. Hand it to Christopher Snyman. "This is yours to take to the board."',
  18: 'INTERVENTION 5: Joint Scorecard. THE signature move. Print copies for everyone. Have it on screen. Invite them to edit it live.',
  19: 'The scorecard. Amber columns are intentionally blank — that\'s the invitation for ABSA to fill in their targets.',
  21: 'ABOVE AND BEYOND #1: ABSA 2028 Vision. This is what Shyam suggested to Aymen on the call — "what will the headlines read when you go live?" Nobody else will bring a future-state vision.',
  22: 'Imagine ABSA in 2028. Three headlines that could be written. Make it aspirational but grounded in what the platform enables.',
  24: 'ABOVE AND BEYOND #2: Competitive positioning. Don\'t attack competitors. Position as "what a bank at ABSA\'s scale needs."',
  25: 'The comparison. Generic enough not to be seen as attacking, specific enough to differentiate.',
  27: 'ABOVE AND BEYOND #3: The leave-behind. Structure for a document they take to the Group CEO and board. Something no other vendor will produce.',
};

const SLIDES = [

  // ══════════════════════════════════════════════
  // COVER & TOC
  // ══════════════════════════════════════════════
  { layout: 'cover-color-block', label: 'ABSA \u00d7 BACKBASE', title: 'Amsterdam\nToolkit', date: 'Shyam Mohan \u2014 Value Consulting \u2014 May 2026' },

  { layout: 'toc', label: 'TOOLKIT CONTENTS', title: 'What\u2019s in This Deck', numbered: true, items: [
    'The ABSA Story \u2014 5-min opening talking track',
    'Strategic Fit \u2014 5 problems + value at stake',
    'Risk Register \u2014 3 ABSA-specific risks',
    'Investment Logic \u2014 CFO business case card',
    'Joint Success Scorecard \u2014 live co-creation',
    'ABSA 2028 Vision \u2014 what the future looks like',
    'Competitive Positioning \u2014 why Backbase at this scale',
    'Leave-Behind Structure \u2014 the board document'
  ]},

  // ══════════════════════════════════════════════
  // 1. THE ABSA STORY (TALKING TRACK)
  // ══════════════════════════════════════════════
  { layout: 'chapter-numbered', theme: 'navy', number: '01', label: 'INTERVENTION', title: '"The ABSA Story"', subtitle: '5 minutes. No slides. Eye contact. This is a talking track \u2014 the speaker notes are your script.' },

  { layout: 'statement', variant: 'dark', label: 'BEAT 1 \u00b7 2 MINUTES \u2014 "HERE\'S WHAT WE SEE"',
    text: 'R115.7 billion in revenue. A CIB division delivering <span class="hl">21% ROE.</span> But a retail franchise losing <span class="hl">300,000 customers a year.</span> An NPS of 15\u2009\u2014\u2009thirty points behind Capitec. And a cost-to-income ratio that the board needs three percentage points lower.' },

  { layout: 'statement', accent: 'blue', label: 'BEAT 2 \u00b7 2 MINUTES \u2014 "HERE\'S WHY THE TIMING IS NOW"',
    text: 'A new Personal & Private Banking division. A CEO who has <span class="hl">publicly committed</span> to clawing back retail market share. R16.7 billion in IT investment. The question isn\u2019t whether to transform \u2014 it\u2019s whether the <span class="hl">next 10 years of banking</span> will be built on the right platform.' },

  { layout: 'statement', accent: 'blue', label: 'BEAT 3 \u00b7 1 MINUTE \u2014 "HERE\'S HOW WE\'D MEASURE IT"',
    text: 'Digital adoption. Cost-to-income. Net Promoter Score. Customer base growth. We have a view on what <span class="hl">success looks like</span> for ABSA \u2014 and at the end of today, we\u2019d like to <span class="hl">build that scorecard with you.</span>' },

  // ══════════════════════════════════════════════
  // 2. STRATEGIC FIT
  // ══════════════════════════════════════════════
  { layout: 'chapter-numbered', theme: 'navy', number: '02', label: 'INTERVENTION', title: 'Strategic Fit', subtitle: '10 minutes. The 5 problems ABSA needs to solve \u2014 and the value at stake if they don\u2019t.' },

  { layout: 'content-standard', theme: 'light', label: 'FIVE INTERCONNECTED CHALLENGES', title: 'What We See When We Look at ABSA', subtitle: 'Reverse-engineered from your strategy, your annual report, and your market position.', body: `
    <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:14px;margin-top:8px">
      <div style="border-radius:10px;padding:16px;border:1px solid rgba(220,38,38,0.15);border-top:3px solid #DC2626">
        <div style="font-size:9px;font-weight:800;letter-spacing:2px;color:#DC2626;margin-bottom:4px">P1 \u2014 CUSTOMER HEMORRHAGE</div>
        <div style="font-size:22px;font-weight:900;margin-bottom:4px">-300K/yr</div>
        <p style="font-size:9px;color:#64748B;line-height:1.5">NPS 15% vs Capitec 45%. FNB Best App 4 years running. Onboarding friction drives customers to competitors who make banking feel effortless.</p>
        <div style="margin-top:6px;font-size:8px;color:#94A3B8">Source: ABSA 2025 Annual Results, Moneyweb</div>
      </div>
      <div style="border-radius:10px;padding:16px;border:1px solid rgba(217,119,6,0.15);border-top:3px solid #D97706">
        <div style="font-size:9px;font-weight:800;letter-spacing:2px;color:#D97706;margin-bottom:4px">P2 \u2014 CHANNEL FRAGMENTATION</div>
        <div style="font-size:22px;font-weight:900;margin-bottom:4px">Zero Continuity</div>
        <p style="font-size:9px;color:#64748B;line-height:1.5">No save-and-resume. No 360\u00b0 employee view. Customer context lost between mobile, web, branch, and contact centre.</p>
        <div style="margin-top:6px;font-size:8px;color:#94A3B8">Source: RFP vendor Q&A, RFP defense scenarios</div>
      </div>
      <div style="border-radius:10px;padding:16px;border:1px solid rgba(220,38,38,0.15);border-top:3px solid #DC2626">
        <div style="font-size:9px;font-weight:800;letter-spacing:2px;color:#DC2626;margin-bottom:4px">P3 \u2014 UNSUSTAINABLE COST</div>
        <div style="font-size:22px;font-weight:900;margin-bottom:4px">~R3.5bn Excess</div>
        <p style="font-size:9px;color:#64748B;line-height:1.5">C/I 53.8% vs industry 50.7%. 42% of customers still not digitally active. Branch costs R150\u2013250 vs R5\u201315 digital.</p>
        <div style="margin-top:6px;font-size:8px;color:#94A3B8">Source: ABSA 2025 Results, PwC SA Major Banks</div>
      </div>
    </div>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-top:10px">
      <div style="border-radius:10px;padding:16px;border:1px solid rgba(217,119,6,0.15);border-top:3px solid #D97706">
        <div style="font-size:9px;font-weight:800;letter-spacing:2px;color:#D97706;margin-bottom:4px">P4 \u2014 ONE-SIZE-FITS-ALL</div>
        <div style="font-size:22px;font-weight:900;margin-bottom:4px">9.3M = 1 Segment</div>
        <p style="font-size:9px;color:#64748B;line-height:1.5">No tailored value propositions per segment. GenZ gets the same experience as HNWI. Sole proprietors treated as retail. Drives attrition and suppresses cross-sell.</p>
      </div>
      <div style="border-radius:10px;padding:16px;border:1px solid rgba(123,47,255,0.15);border-top:3px solid #7B2FFF">
        <div style="font-size:9px;font-weight:800;letter-spacing:2px;color:#7B2FFF;margin-bottom:4px">P5 \u2014 INNOVATION BOTTLENECK</div>
        <div style="font-size:22px;font-weight:900;margin-bottom:4px">R16.7bn \u2192 15% ROE</div>
        <p style="font-size:9px;color:#64748B;line-height:1.5">Massive IT investment but ROE still below target. Each initiative is bespoke. No reusable components. Time-to-market in quarters, not weeks.</p>
      </div>
    </div>
  `, bodyFull: true },

  { layout: 'content-standard', theme: 'light', label: 'VALUE AT STAKE', title: 'The Cost of Inaction: R7.1\u201310.7bn Over 3 Years', subtitle: 'Every number from ABSA\u2019s own published financials. Conservative bias. Assumption-transparent.', body: `
    <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:16px;margin-top:8px">
      <div style="border-radius:10px;padding:18px;border:1px solid rgba(5,150,105,0.15);text-align:center">
        <div style="font-size:9px;font-weight:800;letter-spacing:2px;color:#059669;margin-bottom:6px">COST REDUCTION</div>
        <div style="font-size:30px;font-weight:900;color:#059669;margin-bottom:4px">R3.8\u20135.4bn</div>
        <p style="font-size:10px;color:#64748B;line-height:1.5">C/I improvement 53.8% \u2192 50.5%<br>Each 1pp = R1.16bn savings<br>Digital adoption 58% \u2192 85%</p>
      </div>
      <div style="border-radius:10px;padding:18px;border:1px solid rgba(51,102,255,0.15);text-align:center">
        <div style="font-size:9px;font-weight:800;letter-spacing:2px;color:#3366FF;margin-bottom:6px">REVENUE PROTECTION</div>
        <div style="font-size:30px;font-weight:900;color:#3366FF;margin-bottom:4px">R2.3\u20133.7bn</div>
        <p style="font-size:10px;color:#64748B;line-height:1.5">Attrition reduction 20\u201330%<br>60K\u201390K customers retained/yr<br>Digital sales conversion 2\u20133x</p>
      </div>
      <div style="border-radius:10px;padding:18px;border:1px solid rgba(123,47,255,0.15);text-align:center">
        <div style="font-size:9px;font-weight:800;letter-spacing:2px;color:#7B2FFF;margin-bottom:6px">REVENUE GROWTH</div>
        <div style="font-size:30px;font-weight:900;color:#7B2FFF;margin-bottom:4px">R1.0\u20131.6bn</div>
        <p style="font-size:10px;color:#64748B;line-height:1.5">Segment propositions<br>Cross-sell ratio +0.3\u20130.5x<br>Digital lending uplift +15\u201325%</p>
      </div>
    </div>
    <div style="margin-top:14px;padding:14px 20px;background:#091C35;border-radius:10px;display:flex;justify-content:space-between;align-items:center">
      <div style="color:rgba(255,255,255,0.5);font-size:10px;font-weight:800;letter-spacing:1px">3-YEAR CUMULATIVE VALUE</div>
      <div style="display:flex;gap:40px">
        <div style="text-align:center"><div style="font-size:16px;font-weight:900;color:#D97706">R5.4bn</div><div style="font-size:8px;color:rgba(255,255,255,0.35);margin-top:2px">CONSERVATIVE (-25%)</div></div>
        <div style="text-align:center"><div style="font-size:22px;font-weight:900;color:#3366FF">R7.1bn</div><div style="font-size:8px;color:rgba(255,255,255,0.35);margin-top:2px">BASE CASE</div></div>
        <div style="text-align:center"><div style="font-size:16px;font-weight:900;color:#059669">R10.7bn</div><div style="font-size:8px;color:rgba(255,255,255,0.35);margin-top:2px">ASPIRATIONAL (+25%)</div></div>
      </div>
    </div>
    <div style="margin-top:10px;font-size:9px;color:#94A3B8">Based on: ABSA Group 2025 Annual Results (R115.7bn revenue, R62.2bn opex, 9.3M customers, 5.4M digitally active). Benchmarks: MCB, NBB, Nordic Bank deployments.</div>
  `, bodyFull: true },

  // ══════════════════════════════════════════════
  // 3. RISK REGISTER
  // ══════════════════════════════════════════════
  { layout: 'chapter-numbered', theme: 'navy', number: '03', label: 'INTERVENTION', title: 'Transformation\nRisk Register', subtitle: '8 minutes. ABSA-specific \u2014 not generic. Grounded in what we know about their environment.' },

  { layout: 'content-standard', theme: 'light', label: '3 RISKS, ABSA-SPECIFIC', title: 'Where Transformations Like This Get Hard', subtitle: 'We\u2019re not pretending this is easy. Here\u2019s specifically where, and specifically how we mitigate.', body: `
    <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:14px;margin-top:8px">
      <div style="border-radius:10px;padding:16px;border:1px solid rgba(220,38,38,0.15);border-top:4px solid #DC2626">
        <div style="font-size:9px;font-weight:800;letter-spacing:2px;color:#DC2626;margin-bottom:6px">RISK 1</div>
        <div style="font-size:15px;font-weight:900;margin-bottom:6px">Co-Existence Complexity</div>
        <p style="font-size:9px;color:#64748B;line-height:1.5;margin-bottom:10px">IBM Mainframe core + MuleSoft middleware + new engagement layer. Your team described the strategy as \u201cbuild, launch, and hollow.\u201d The integration seams are where programs fail.</p>
        <div style="padding:10px;background:rgba(5,150,105,0.05);border:1px solid rgba(5,150,105,0.15);border-radius:8px">
          <div style="font-size:8px;font-weight:800;color:#059669;margin-bottom:3px">MITIGATION</div>
          <p style="font-size:9px;color:#091C35;line-height:1.4">Grand Central iPaaS as the co-existence layer. BIAN-based API model. REST + Event Streaming. MCB proved multi-core integration across 3 countries in 6 months. <strong>Co-existence is our architecture, not a migration phase.</strong></p>
        </div>
      </div>
      <div style="border-radius:10px;padding:16px;border:1px solid rgba(217,119,6,0.15);border-top:4px solid #D97706">
        <div style="font-size:9px;font-weight:800;letter-spacing:2px;color:#D97706;margin-bottom:6px">RISK 2</div>
        <div style="font-size:15px;font-weight:900;margin-bottom:6px">Organizational Adoption</div>
        <p style="font-size:9px;color:#64748B;line-height:1.5;margin-bottom:10px">New PPB division launched June 2025 \u2014 org structure still settling. 10,000+ employees affected. Digital adoption requires behavior change, not just technology change.</p>
        <div style="padding:10px;background:rgba(5,150,105,0.05);border:1px solid rgba(5,150,105,0.15);border-radius:8px">
          <div style="font-size:8px;font-weight:800;color:#059669;margin-bottom:3px">MITIGATION</div>
          <p style="font-size:9px;color:#091C35;line-height:1.4">Digital Factory with embedded change management. Academy \u2192 Bootcamp \u2192 Hub learning path. EY as local change partner with deep ABSA institutional knowledge. Phased rollout by segment.</p>
        </div>
      </div>
      <div style="border-radius:10px;padding:16px;border:1px solid rgba(123,47,255,0.15);border-top:4px solid #7B2FFF">
        <div style="font-size:9px;font-weight:800;letter-spacing:2px;color:#7B2FFF;margin-bottom:6px">RISK 3</div>
        <div style="font-size:15px;font-weight:900;margin-bottom:6px">Scope Creep & Overrun</div>
        <p style="font-size:9px;color:#64748B;line-height:1.5;margin-bottom:10px">R16.7bn IT spend already. Board scrutiny is high. You explicitly asked for contingency planning. The scope expanded from \u20ac19M to \u20ac32M after the defense \u2014 that trend must be governed.</p>
        <div style="padding:10px;background:rgba(5,150,105,0.05);border:1px solid rgba(5,150,105,0.15);border-radius:8px">
          <div style="font-size:8px;font-weight:800;color:#059669;margin-bottom:3px">MITIGATION</div>
          <p style="font-size:9px;color:#091C35;line-height:1.4">Phase-gated delivery with value checkpoints. Each phase delivers measurable ROI before next begins. 80% OOTB. Fixed-scope Phase 1 with clear success criteria. MCB: 6 months to live MVP.</p>
        </div>
      </div>
    </div>
  `, bodyFull: true },

  // ══════════════════════════════════════════════
  // 4. INVESTMENT LOGIC (CFO CARD)
  // ══════════════════════════════════════════════
  { layout: 'chapter-numbered', theme: 'navy', number: '04', label: 'INTERVENTION', title: 'Investment\nLogic Card', subtitle: '8 minutes. The one page Christopher Snyman takes to the ABSA board.' },

  { layout: 'content-standard', theme: 'light', label: 'FOR THE BOARD', title: 'ABSA Digital Platform Investment Logic', subtitle: 'Print this. Hand it to the CFO. Every number sourced from ABSA\u2019s own annual report.', body: `
    <div style="border:2px solid #3366FF;border-radius:12px;padding:20px;background:rgba(51,102,255,0.02)">
      <div style="display:grid;grid-template-columns:180px 1fr;gap:20px;align-items:start">
        <div>
          <div style="font-size:9px;font-weight:800;letter-spacing:2px;color:#3366FF;margin-bottom:6px">5-YEAR INVESTMENT</div>
          <div style="font-size:36px;font-weight:900;color:#091C35">R618M</div>
          <div style="font-size:10px;color:#64748B;margin-top:4px">\u20ac32.2M \u00d7 19.2 ZAR<br>Platform + services + infra</div>
          <div style="margin-top:12px;font-size:9px;font-weight:800;letter-spacing:2px;color:#091C35">COMPOSITION</div>
          <div style="font-size:10px;color:#64748B;margin-top:4px;line-height:1.6">Once-off: R95.6M<br>Licenses (5yr): R431.3M<br>Infrastructure (5yr): R91.2M</div>
        </div>
        <div>
          <div style="font-size:9px;font-weight:800;letter-spacing:2px;color:#091C35;margin-bottom:8px">VALUE LEVERS \u2014 3-YEAR CUMULATIVE</div>
          <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:10px;margin-bottom:12px">
            <div style="background:#F0F4F8;border-radius:8px;padding:10px;text-align:center">
              <div style="font-size:8px;font-weight:800;color:#059669;letter-spacing:1px">COST REDUCTION</div>
              <div style="font-size:20px;font-weight:900;color:#059669;margin:4px 0">R3.8bn</div>
              <div style="font-size:8px;color:#64748B">C/I 53.8% \u2192 50.5%<br>Digital adoption 58% \u2192 85%<br>Call deflection +25\u201335%</div>
            </div>
            <div style="background:#F0F4F8;border-radius:8px;padding:10px;text-align:center">
              <div style="font-size:8px;font-weight:800;color:#3366FF;letter-spacing:1px">REVENUE PROTECTION</div>
              <div style="font-size:20px;font-weight:900;color:#3366FF;margin:4px 0">R2.3bn</div>
              <div style="font-size:8px;color:#64748B">Attrition -20\u201330%<br>Digital sales conv. 2\u20133x<br>Cross-sell +0.3\u20130.5x</div>
            </div>
            <div style="background:#F0F4F8;border-radius:8px;padding:10px;text-align:center">
              <div style="font-size:8px;font-weight:800;color:#7B2FFF;letter-spacing:1px">REVENUE GROWTH</div>
              <div style="font-size:20px;font-weight:900;color:#7B2FFF;margin:4px 0">R1.0bn</div>
              <div style="font-size:8px;color:#64748B">Segment propositions<br>Digital lending uplift<br>Ecosystem revenue</div>
            </div>
          </div>
          <div style="display:grid;grid-template-columns:1fr 1fr 1fr 1fr;gap:10px">
            <div style="background:#091C35;border-radius:8px;padding:10px;text-align:center">
              <div style="font-size:8px;font-weight:800;color:rgba(255,255,255,0.4);letter-spacing:1px">BASE-CASE VALUE</div>
              <div style="font-size:18px;font-weight:900;color:#3366FF;margin-top:4px">R7.1bn</div>
            </div>
            <div style="background:#091C35;border-radius:8px;padding:10px;text-align:center">
              <div style="font-size:8px;font-weight:800;color:rgba(255,255,255,0.4);letter-spacing:1px">ROI MULTIPLE</div>
              <div style="font-size:18px;font-weight:900;color:#059669;margin-top:4px">11.5x</div>
            </div>
            <div style="background:#091C35;border-radius:8px;padding:10px;text-align:center">
              <div style="font-size:8px;font-weight:800;color:rgba(255,255,255,0.4);letter-spacing:1px">CONSERVATIVE</div>
              <div style="font-size:18px;font-weight:900;color:#D97706;margin-top:4px">8.7x</div>
            </div>
            <div style="background:#091C35;border-radius:8px;padding:10px;text-align:center">
              <div style="font-size:8px;font-weight:800;color:rgba(255,255,255,0.4);letter-spacing:1px">PER-USER Y5</div>
              <div style="font-size:18px;font-weight:900;color:#fff;margin-top:4px">R11.21</div>
            </div>
          </div>
        </div>
      </div>
      <div style="margin-top:12px;border-top:1px solid #E2E8F0;padding-top:10px;font-size:9px;color:#64748B;line-height:1.6">
        <strong style="color:#091C35">Key assumption:</strong> Revenue base stable at R115.7bn. C/I improvement compounds with digital adoption. Customer revenue estimated at R5,000\u20136,500/yr from PPB earnings \u00f7 customer base. All projections indicative, subject to joint discovery. <strong style="color:#3366FF">By Year 5, the cost per active user is less than the cost of a single branch transaction.</strong>
      </div>
    </div>
  `, bodyFull: true },

  // ══════════════════════════════════════════════
  // 5. JOINT SUCCESS SCORECARD
  // ══════════════════════════════════════════════
  { layout: 'chapter-numbered', theme: 'navy', number: '05', label: 'INTERVENTION', title: 'Joint Success\nScorecard', subtitle: '10 minutes. Live co-creation. The amber columns are theirs to fill. This IS the culture demo.' },

  { layout: 'content-standard', theme: 'light', label: 'DRAFT \u2014 FOR LIVE CO-CREATION', title: 'How We\u2019d Measure Success Together', subtitle: '\u201cWe\u2019ve drafted what success looks like. The amber columns are yours. Let\u2019s build this right now.\u201d', body: `
    <div style="border-radius:10px;overflow:hidden;border:1px solid #E2E8F0">
      <table style="width:100%;border-collapse:collapse;font-size:10px">
        <thead>
          <tr style="background:#091C35;color:#fff;font-size:8px;font-weight:800;letter-spacing:1px;text-transform:uppercase">
            <th style="padding:8px 12px;text-align:left;width:110px">Category</th>
            <th style="padding:8px 12px;text-align:left">Metric</th>
            <th style="padding:8px 12px;text-align:center;width:70px">Current</th>
            <th style="padding:8px 12px;text-align:center;width:70px">Year 1</th>
            <th style="padding:8px 12px;text-align:center;width:70px">Year 3</th>
            <th style="padding:8px 12px;text-align:center;width:80px;color:rgba(255,255,255,0.4)">ABSA Target</th>
          </tr>
        </thead>
        <tbody>
          <tr style="border-bottom:1px solid #E2E8F0"><td style="padding:7px 12px;font-weight:800;color:#3366FF;background:#F0F4F8" rowspan="3">Customer<br>Impact</td><td style="padding:7px 12px">Digital Adoption</td><td style="padding:7px 12px;text-align:center">58%</td><td style="padding:7px 12px;text-align:center">70%</td><td style="padding:7px 12px;text-align:center">85%</td><td style="padding:7px 12px;text-align:center;background:rgba(217,119,6,0.06);color:#D97706;font-weight:700;font-size:14px">?</td></tr>
          <tr style="border-bottom:1px solid #E2E8F0"><td style="padding:7px 12px">Net Promoter Score</td><td style="padding:7px 12px;text-align:center">15%</td><td style="padding:7px 12px;text-align:center">22%</td><td style="padding:7px 12px;text-align:center">30%+</td><td style="padding:7px 12px;text-align:center;background:rgba(217,119,6,0.06);color:#D97706;font-weight:700;font-size:14px">?</td></tr>
          <tr style="border-bottom:1px solid #E2E8F0"><td style="padding:7px 12px">Customer Base (SA)</td><td style="padding:7px 12px;text-align:center">9.3M \u2193</td><td style="padding:7px 12px;text-align:center">9.5M</td><td style="padding:7px 12px;text-align:center">10.2M</td><td style="padding:7px 12px;text-align:center;background:rgba(217,119,6,0.06);color:#D97706;font-weight:700;font-size:14px">?</td></tr>
          <tr style="border-bottom:1px solid #E2E8F0"><td style="padding:7px 12px;font-weight:800;color:#059669;background:#F0F4F8" rowspan="3">Operational<br>Efficiency</td><td style="padding:7px 12px">Cost-to-Income Ratio</td><td style="padding:7px 12px;text-align:center">53.8%</td><td style="padding:7px 12px;text-align:center">52.5%</td><td style="padding:7px 12px;text-align:center">50.5%</td><td style="padding:7px 12px;text-align:center;background:rgba(217,119,6,0.06);color:#D97706;font-weight:700;font-size:14px">?</td></tr>
          <tr style="border-bottom:1px solid #E2E8F0"><td style="padding:7px 12px">Digital Sales Conversion</td><td style="padding:7px 12px;text-align:center">~5\u20138%</td><td style="padding:7px 12px;text-align:center">12\u201315%</td><td style="padding:7px 12px;text-align:center">20\u201325%</td><td style="padding:7px 12px;text-align:center;background:rgba(217,119,6,0.06);color:#D97706;font-weight:700;font-size:14px">?</td></tr>
          <tr style="border-bottom:1px solid #E2E8F0"><td style="padding:7px 12px">Call Deflection Rate</td><td style="padding:7px 12px;text-align:center">TBD</td><td style="padding:7px 12px;text-align:center">+25%</td><td style="padding:7px 12px;text-align:center">+35%</td><td style="padding:7px 12px;text-align:center;background:rgba(217,119,6,0.06);color:#D97706;font-weight:700;font-size:14px">?</td></tr>
          <tr style="border-bottom:1px solid #E2E8F0"><td style="padding:7px 12px;font-weight:800;color:#7B2FFF;background:#F0F4F8" rowspan="2">Delivery<br>Health</td><td style="padding:7px 12px">Phase 1 Go-Live</td><td style="padding:7px 12px;text-align:center">\u2014</td><td style="padding:7px 12px;text-align:center">6\u20139 mo</td><td style="padding:7px 12px;text-align:center">\u2014</td><td style="padding:7px 12px;text-align:center;background:rgba(217,119,6,0.06);color:#D97706;font-weight:700;font-size:14px">?</td></tr>
          <tr><td style="padding:7px 12px">Platform Uptime</td><td style="padding:7px 12px;text-align:center">\u2014</td><td style="padding:7px 12px;text-align:center">99.9%</td><td style="padding:7px 12px;text-align:center">99.9%</td><td style="padding:7px 12px;text-align:center;background:rgba(217,119,6,0.06);color:#D97706;font-weight:700;font-size:14px">?</td></tr>
        </tbody>
      </table>
    </div>
    <div style="margin-top:12px;padding:10px 16px;border-radius:8px;border:2px solid rgba(51,102,255,0.2);background:rgba(51,102,255,0.03);font-size:10px;color:#091C35;line-height:1.6">
      <strong style="color:#3366FF">The move:</strong> Print copies for everyone. Have it on screen. Read the first 3 rows together. Then: \u201cWhat would ABSA set as the Year 1 target for digital adoption? 70%? Higher?\u201d Let them debate. Capture their input. <strong>They leave with an artifact they helped create.</strong>
    </div>
  `, bodyFull: true },

  // ══════════════════════════════════════════════
  // ABOVE AND BEYOND
  // ══════════════════════════════════════════════
  { layout: 'chapter-standard', theme: 'blue', label: 'ABOVE & BEYOND', title: 'Going Further Than\nWhat Was Asked', subtitle: 'Three differentiators that no other vendor will bring to the room.' },

  // ── A: ABSA 2028 VISION ──
  { layout: 'content-standard', theme: 'dark', label: 'IMAGINE ABSA IN 2028', title: 'What the Headlines Could Read', subtitle: 'Not a promise \u2014 a vision of what\u2019s possible with the right platform partner.', body: `
    <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:16px;margin-top:12px">
      <div style="border-radius:10px;padding:20px;background:rgba(255,255,255,0.04);border:1px solid rgba(255,255,255,0.08)">
        <div style="font-size:8px;font-weight:800;letter-spacing:2px;color:rgba(255,255,255,0.3);margin-bottom:8px">BUSINESSTECH \u00b7 MARCH 2028</div>
        <div style="font-size:18px;font-weight:900;color:#fff;line-height:1.2;margin-bottom:10px">\u201cABSA overtakes FNB in digital app satisfaction for the first time\u201d</div>
        <p style="font-size:9px;color:rgba(255,255,255,0.4);line-height:1.5">NPS climbs to 28%, closing the gap on Capitec. Segment-driven UX for GenZ and Affluent cited as key differentiator. Digital adoption reaches 78% of active base.</p>
        <div style="margin-top:10px;padding:8px;background:rgba(5,150,105,0.15);border-radius:6px;font-size:8px;font-weight:700;color:#059669;text-align:center">Enabled by: Phase 1 (Servicing + Onboarding) + Phase 2 (TVP + Family Banking)</div>
      </div>
      <div style="border-radius:10px;padding:20px;background:rgba(255,255,255,0.04);border:1px solid rgba(255,255,255,0.08)">
        <div style="font-size:8px;font-weight:800;letter-spacing:2px;color:rgba(255,255,255,0.3);margin-bottom:8px">MONEYWEB \u00b7 AUGUST 2028</div>
        <div style="font-size:18px;font-weight:900;color:#fff;line-height:1.2;margin-bottom:10px">\u201cABSA halts customer bleed \u2014 first net positive quarter in 3 years\u201d</div>
        <p style="font-size:9px;color:rgba(255,255,255,0.4);line-height:1.5">Bank reports net customer growth for Q2 2028 \u2014 the first positive quarter since 2025. Digital onboarding drives 200K+ new-to-bank acquisitions. Sole proprietor segment grows 34%.</p>
        <div style="margin-top:10px;padding:8px;background:rgba(51,102,255,0.15);border-radius:6px;font-size:8px;font-weight:700;color:#3366FF;text-align:center">Enabled by: Digital Onboarding STP + Business Banking + CLO activation</div>
      </div>
      <div style="border-radius:10px;padding:20px;background:rgba(255,255,255,0.04);border:1px solid rgba(255,255,255,0.08)">
        <div style="font-size:8px;font-weight:800;letter-spacing:2px;color:rgba(255,255,255,0.3);margin-bottom:8px">CNBC AFRICA \u00b7 NOVEMBER 2028</div>
        <div style="font-size:18px;font-weight:900;color:#fff;line-height:1.2;margin-bottom:10px">\u201cABSA PPB hits 16% ROE target as C/I drops below 51%\u201d</div>
        <p style="font-size:9px;color:rgba(255,255,255,0.4);line-height:1.5">CEO Fihla credits digital transformation for operational turnaround. Cost-to-income drops 2.8pp in 30 months. AI-powered CLO drives 40% reduction in contact centre volume. Board approves Phase N expansion.</p>
        <div style="margin-top:10px;padding:8px;background:rgba(123,47,255,0.15);border-radius:6px;font-size:8px;font-weight:700;color:#7B2FFF;text-align:center">Enabled by: Full platform + AI (CLO + Conversational Banking + Delivery OS)</div>
      </div>
    </div>
    <div style="margin-top:12px;font-size:9px;color:rgba(255,255,255,0.3);text-align:center">These are illustrative outcomes grounded in comparable Backbase deployments (MCB, NBB, Nordic Bank). Not commitments \u2014 a shared vision of what\u2019s possible.</div>
  `, bodyFull: true },

  { layout: 'statement-stat', accent: 'blue', label: 'THE QUESTION FOR ABSA', stat: '2028',
    text: 'In two years, will ABSA be the bank that <span class="hl">redefined retail banking in South Africa</span> \u2014 or the one that let Capitec and FNB write that story instead?',
    source: '' },

  // ── B: COMPETITIVE POSITIONING ──
  { layout: 'content-standard', theme: 'light', label: 'WHY BACKBASE AT THIS SCALE', title: 'What a Bank Like ABSA Needs in a Platform Partner', subtitle: 'Not an attack on competitors. A framework for what matters at 10M-user scale.', body: `
    <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:14px;margin-top:8px">
      <div style="border-radius:10px;padding:16px;border:1px solid #E2E8F0">
        <div style="font-size:9px;font-weight:800;letter-spacing:2px;color:#64748B;margin-bottom:6px">APPROACH A</div>
        <div style="font-size:14px;font-weight:900;margin-bottom:6px">Full-Stack Core Replacement</div>
        <div style="font-size:9px;color:#64748B;line-height:1.5">
          <div style="margin-bottom:6px">\u2022 Requires core commitment or replacement</div>
          <div style="margin-bottom:6px">\u2022 18\u201324+ months to initial delivery</div>
          <div style="margin-bottom:6px">\u2022 African refs: greenfield/small banks</div>
          <div style="margin-bottom:6px">\u2022 Core + channels tightly coupled</div>
          <div>\u2022 All-or-nothing commitment</div>
        </div>
        <div style="margin-top:10px;padding:8px;background:rgba(220,38,38,0.06);border-radius:6px;font-size:8px;font-weight:700;color:#DC2626;text-align:center">HIGH RISK for co-existence strategy</div>
      </div>
      <div style="border-radius:10px;padding:16px;border:1px solid #E2E8F0">
        <div style="font-size:9px;font-weight:800;letter-spacing:2px;color:#64748B;margin-bottom:6px">APPROACH B</div>
        <div style="font-size:14px;font-weight:900;margin-bottom:6px">Front-End Builder</div>
        <div style="font-size:9px;color:#64748B;line-height:1.5">
          <div style="margin-bottom:6px">\u2022 API layer on existing systems</div>
          <div style="margin-bottom:6px">\u2022 3\u20136 months for front-end only</div>
          <div style="margin-bottom:6px">\u2022 No bank at ABSA\u2019s scale (9.3M)</div>
          <div style="margin-bottom:6px">\u2022 Front-end only. No orchestration.</div>
          <div>\u2022 Early-stage. No managed services.</div>
        </div>
        <div style="margin-top:10px;padding:8px;background:rgba(217,119,6,0.06);border-radius:6px;font-size:8px;font-weight:700;color:#D97706;text-align:center">SCALE RISK at 10M users</div>
      </div>
      <div style="border-radius:10px;padding:16px;border:2px solid #3366FF;background:rgba(51,102,255,0.02)">
        <div style="font-size:9px;font-weight:800;letter-spacing:2px;color:#3366FF;margin-bottom:6px">ENGAGEMENT BANKING PLATFORM</div>
        <div style="font-size:14px;font-weight:900;margin-bottom:6px;color:#3366FF">Progressive Modernization</div>
        <div style="font-size:9px;color:#091C35;line-height:1.5;font-weight:600">
          <div style="margin-bottom:6px">\u2022 Wraps around existing core via iPaaS</div>
          <div style="margin-bottom:6px">\u2022 6\u20139 months to live (MCB: 6 months)</div>
          <div style="margin-bottom:6px">\u2022 MCB, I&M, 100+ banks globally</div>
          <div style="margin-bottom:6px">\u2022 Full stack: servicing + sales + AI + ops</div>
          <div>\u2022 24/7 managed services. Digital Factory.</div>
        </div>
        <div style="margin-top:10px;padding:8px;background:rgba(5,150,105,0.1);border-radius:6px;font-size:8px;font-weight:700;color:#059669;text-align:center">BUILT for \u201cbuild, launch, hollow\u201d</div>
      </div>
    </div>
    <div style="margin-top:10px;font-size:9px;color:#94A3B8;text-align:center">Not about which vendor is \u201cbetter.\u201d About which approach fits ABSA\u2019s stated strategy: progressive modernization with co-existence.</div>
  `, bodyFull: true },

  // ── C: LEAVE-BEHIND ──
  { layout: 'content-columns', label: 'THE LEAVE-BEHIND', title: 'What We\u2019ll Send After the Visit', columns: [
    { subtitle: 'Outside-In Perspective', body: 'A polished document covering ABSA\u2019s competitive position, the 5 problems, value at stake with sensitivity analysis, peer benchmarks, and the co-created success scorecard. Something for the Group CEO and the board.' },
    { subtitle: 'Demo Portal Access', body: 'Continued access to the localized, branded demo environment. Installable on any device. All 12 scenarios from the RFP defense available for testing. Extended for the decision period.' },
    { subtitle: 'Investment Logic Card', body: 'Printed and digital version of the 1-page CFO card. R618M investment, R7.1bn value, 11.5x ROI. Ready to be forwarded to the board without modification.' }
  ]},

  // ══════════════════════════════════════════════
  // CLOSE
  // ══════════════════════════════════════════════
  { layout: 'statement', variant: 'dark', label: 'THE OUTCOME',
    text: 'They asked for a vendor visit. We gave them a <span class="hl">partnership preview.</span>' },

  { layout: 'thank-you' }
];
