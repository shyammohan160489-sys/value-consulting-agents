window.BB_SHARED_ASSETS = '../backbase-slides-app';

const SPEAKER_NOTES = {
  1: 'Cover slide. The 5-slide arc designed for the Strategic Alignment section after Subash and the CIO/CDO speak. Shyam to deliver.',
  2: 'Slide 1 of 5: The North Star. Anchor with ABSA\'s validated 3 pillars. Open with: "You\'ve shared your North Star. We\'ve spent the last 4 months looking at ABSA from the outside in. Here\'s what we see — and what we believe is in the way."',
  3: 'Slide 2 of 5: What\'s stopping ABSA today. Each pillar has 2 specific obstacles grounded in ABSA\'s own data. Don\'t generalize — every number is from their annual report or RFP defense.',
  4: 'Slide 3 of 5: Strategic Fit. Map Backbase building blocks to each pillar, then connect to the validated metrics in the bottom ribbon (the same ones from the original deck). This is where we earn the right to advise.',
  5: 'Slide 4 of 5: The 3-phase strategy with client proof points. ABSA\'s team validated this phasing in the RFP defense — Aymen confirmed they liked it. Each phase has a real client example with quantified outcomes.',
  6: 'Slide 5 of 5: Why Backbase. Position it as "supplier selection" not "vendor comparison" — same framing as the colleague\'s template. 5 dimensions tailored to ABSA\'s reality (build-launch-hollow, IBM Mainframe + MuleSoft, 9.3M scale).',
  7: 'Closing statement. Plant the seed for the scorecard discussion that comes in Item 5.',
};

const SLIDES = [

  // ── COVER ──
  { layout: 'cover-color-block', label: 'ABSA × BACKBASE', title: 'Strategic\nAlignment', date: 'Amsterdam — 4 May 2026' },

  // ════════════════════════════════════════════════════════════════
  // SLIDE 1 OF 5: THE NORTH STAR (validated)
  // ════════════════════════════════════════════════════════════════
  { layout: 'content-standard', theme: 'light', label: 'OUR UNDERSTANDING OF YOUR NORTH STAR', title: 'A Vision Already Aligned with the Market Shift', subtitle: '“A fundamental shift from a transaction-processing bank to a partner powering customer life moments.”', body: `
    <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:14px;margin-top:8px">
      <div style="background:#091C35;border-radius:12px;padding:18px;color:#fff;position:relative;overflow:hidden">
        <div style="position:absolute;top:6px;right:10px;font-size:32px;font-weight:900;color:rgba(255,255,255,0.06)">01</div>
        <div style="font-size:9px;font-weight:800;letter-spacing:2px;color:#3366FF;margin-bottom:8px">PILLAR 1</div>
        <div style="font-size:18px;font-weight:900;line-height:1.2;margin-bottom:8px;color:#fff">Customer-Centric &<br>Hyper-Personalised CX</div>
        <p style="font-size:10px;color:rgba(255,255,255,0.6);line-height:1.5">Best-in-class UX/UI and engaging experience with <strong style="color:#fff">segment-specific value propositions</strong> across the full customer lifecycle.</p>
      </div>
      <div style="background:#091C35;border-radius:12px;padding:18px;color:#fff;position:relative;overflow:hidden">
        <div style="position:absolute;top:6px;right:10px;font-size:32px;font-weight:900;color:rgba(255,255,255,0.06)">02</div>
        <div style="font-size:9px;font-weight:800;letter-spacing:2px;color:#3366FF;margin-bottom:8px">PILLAR 2</div>
        <div style="font-size:18px;font-weight:900;line-height:1.2;margin-bottom:8px;color:#fff">Growth & Market<br>Leadership</div>
        <p style="font-size:10px;color:rgba(255,255,255,0.6);line-height:1.5">Leverage ABSA’s scale to compete with agile entrants by shifting from <strong style="color:#fff">product-led to ecosystem-driven and segment-led growth</strong>.</p>
      </div>
      <div style="background:#091C35;border-radius:12px;padding:18px;color:#fff;position:relative;overflow:hidden">
        <div style="position:absolute;top:6px;right:10px;font-size:32px;font-weight:900;color:rgba(255,255,255,0.06)">03</div>
        <div style="font-size:9px;font-weight:800;letter-spacing:2px;color:#3366FF;margin-bottom:8px">PILLAR 3</div>
        <div style="font-size:18px;font-weight:900;line-height:1.2;margin-bottom:8px;color:#fff">Future-Fit &<br>Scalable Platform</div>
        <p style="font-size:10px;color:rgba(255,255,255,0.6);line-height:1.5">Move beyond legacy constraints to enable <strong style="color:#fff">speed to market, flexible innovation, and scalable digital operations</strong> across Retail & Business Banking.</p>
      </div>
    </div>
    <div style="margin-top:14px;padding:10px 16px;border-radius:8px;border-left:3px solid #3366FF;background:rgba(51,102,255,0.04);font-size:11px;color:#091C35;line-height:1.6">
      <strong style="color:#3366FF">Validated:</strong> This vision is aligned with the broader market shift. The question isn’t <em>where</em> ABSA is going — it’s <em>what’s in the way</em>, and <em>how</em> to get there.
    </div>
  `, bodyFull: true },

  // ════════════════════════════════════════════════════════════════
  // SLIDE 2 OF 5: WHAT'S STOPPING YOU TODAY
  // ════════════════════════════════════════════════════════════════
  { layout: 'content-standard', theme: 'light', label: 'WHAT’S STOPPING YOU TODAY?', title: 'Six Specific Obstacles — Two Per Pillar', subtitle: 'Every number sourced from ABSA’s 2025 Annual Results or RFP defense.', body: `
    <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:14px;margin-top:8px">
      <div style="display:flex;flex-direction:column;gap:10px">
        <div style="background:#091C35;border-radius:8px;padding:10px 14px;color:#fff">
          <div style="font-size:9px;font-weight:800;letter-spacing:2px;color:#3366FF">PILLAR 1 · CUSTOMER-CENTRIC CX</div>
        </div>
        <div style="border-radius:10px;padding:14px;border:1px solid rgba(220,38,38,0.15);border-top:3px solid #DC2626">
          <div style="font-size:8px;font-weight:800;letter-spacing:1px;color:#DC2626;margin-bottom:4px">OBSTACLE 1</div>
          <div style="font-size:14px;font-weight:900;margin-bottom:4px">9.3M customers,<br>one experience</div>
          <p style="font-size:9px;color:#64748B;line-height:1.5">No segmentation engine. GenZ gets the same app as HNWI. <strong>NPS 15% vs Capitec 45%.</strong></p>
        </div>
        <div style="border-radius:10px;padding:14px;border:1px solid rgba(220,38,38,0.15);border-top:3px solid #DC2626">
          <div style="font-size:8px;font-weight:800;letter-spacing:1px;color:#DC2626;margin-bottom:4px">OBSTACLE 2</div>
          <div style="font-size:14px;font-weight:900;margin-bottom:4px">Channel context lost</div>
          <p style="font-size:9px;color:#64748B;line-height:1.5">No save-and-resume. No 360° employee view. <strong>Customers restart journeys</strong> when they switch channels.</p>
        </div>
      </div>
      <div style="display:flex;flex-direction:column;gap:10px">
        <div style="background:#091C35;border-radius:8px;padding:10px 14px;color:#fff">
          <div style="font-size:9px;font-weight:800;letter-spacing:2px;color:#3366FF">PILLAR 2 · GROWTH & LEADERSHIP</div>
        </div>
        <div style="border-radius:10px;padding:14px;border:1px solid rgba(217,119,6,0.15);border-top:3px solid #D97706">
          <div style="font-size:8px;font-weight:800;letter-spacing:1px;color:#D97706;margin-bottom:4px">OBSTACLE 3</div>
          <div style="font-size:14px;font-weight:900;margin-bottom:4px">Customer hemorrhage</div>
          <p style="font-size:9px;color:#64748B;line-height:1.5"><strong>300K customers lost per year</strong> to Capitec and FNB. Digital sales contribution stuck at 37%. NTB onboarding broken.</p>
        </div>
        <div style="border-radius:10px;padding:14px;border:1px solid rgba(217,119,6,0.15);border-top:3px solid #D97706">
          <div style="font-size:8px;font-weight:800;letter-spacing:1px;color:#D97706;margin-bottom:4px">OBSTACLE 4</div>
          <div style="font-size:14px;font-weight:900;margin-bottom:4px">Single-product mindset</div>
          <p style="font-size:9px;color:#64748B;line-height:1.5"><strong>5M cards issued, 1.4M active.</strong> No lifecycle orchestration. Cross-sell ratio suppressed.</p>
        </div>
      </div>
      <div style="display:flex;flex-direction:column;gap:10px">
        <div style="background:#091C35;border-radius:8px;padding:10px 14px;color:#fff">
          <div style="font-size:9px;font-weight:800;letter-spacing:2px;color:#3366FF">PILLAR 3 · FUTURE-FIT PLATFORM</div>
        </div>
        <div style="border-radius:10px;padding:14px;border:1px solid rgba(123,47,255,0.15);border-top:3px solid #7B2FFF">
          <div style="font-size:8px;font-weight:800;letter-spacing:1px;color:#7B2FFF;margin-bottom:4px">OBSTACLE 5</div>
          <div style="font-size:14px;font-weight:900;margin-bottom:4px">Each initiative is bespoke</div>
          <p style="font-size:9px;color:#64748B;line-height:1.5">No reusable components. <strong>R16.7bn IT spend, ROE still 15%.</strong> Time-to-market in quarters, not weeks.</p>
        </div>
        <div style="border-radius:10px;padding:14px;border:1px solid rgba(123,47,255,0.15);border-top:3px solid #7B2FFF">
          <div style="font-size:8px;font-weight:800;letter-spacing:1px;color:#7B2FFF;margin-bottom:4px">OBSTACLE 6</div>
          <div style="font-size:14px;font-weight:900;margin-bottom:4px">Co-existence complexity</div>
          <p style="font-size:9px;color:#64748B;line-height:1.5">IBM Mainframe + MuleSoft + new builds. <strong>“Build, launch, hollow”</strong> stated as strategy — but no platform to enable it.</p>
        </div>
      </div>
    </div>
  `, bodyFull: true },

  // ════════════════════════════════════════════════════════════════
  // SLIDE 3 OF 5: BACKBASE STRATEGIC FIT (building blocks + metrics)
  // ════════════════════════════════════════════════════════════════
  { layout: 'content-standard', theme: 'light', label: 'BACKBASE STRATEGIC FIT', title: 'How Each Pillar Maps to Backbase Building Blocks', subtitle: 'Building blocks connect directly to your validated North Star metrics.', body: `
    <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:12px;margin-top:6px">
      <div style="border-radius:10px;padding:14px;border:1px solid rgba(51,102,255,0.2);border-top:4px solid #3366FF;background:rgba(51,102,255,0.02)">
        <div style="font-size:8px;font-weight:800;letter-spacing:2px;color:#3366FF;margin-bottom:6px">PILLAR 1 — CX</div>
        <div style="font-size:11px;font-weight:900;margin-bottom:8px;line-height:1.3">Customer-centric & hyper-personalised</div>
        <div style="font-size:9px;color:#091C35;line-height:1.6">
          <div style="margin-bottom:4px">• <strong>Digital Banking Premium</strong> with segment-driven UX (ONE APP, multiple personas)</div>
          <div style="margin-bottom:4px">• <strong>Digital Engage / CLO</strong> for hyper-personalisation, NBA, churn prevention</div>
          <div>• <strong>Digital Assist Premium</strong> with 360° view + act-on-behalf</div>
        </div>
      </div>
      <div style="border-radius:10px;padding:14px;border:1px solid rgba(5,150,105,0.2);border-top:4px solid #059669;background:rgba(5,150,105,0.02)">
        <div style="font-size:8px;font-weight:800;letter-spacing:2px;color:#059669;margin-bottom:6px">PILLAR 2 — GROWTH</div>
        <div style="font-size:11px;font-weight:900;margin-bottom:8px;line-height:1.3">Growth & market leadership</div>
        <div style="font-size:9px;color:#091C35;line-height:1.6">
          <div style="margin-bottom:4px">• <strong>Digital Onboarding STP</strong> (NBB: 5 minutes, near-zero abandonment)</div>
          <div style="margin-bottom:4px">• <strong>Digital Lending</strong> end-to-end origination journeys</div>
          <div>• <strong>Family, Household & Beyond Banking (PFM)</strong> for segment monetisation</div>
        </div>
      </div>
      <div style="border-radius:10px;padding:14px;border:1px solid rgba(123,47,255,0.2);border-top:4px solid #7B2FFF;background:rgba(123,47,255,0.02)">
        <div style="font-size:8px;font-weight:800;letter-spacing:2px;color:#7B2FFF;margin-bottom:6px">PILLAR 3 — PLATFORM</div>
        <div style="font-size:11px;font-weight:900;margin-bottom:8px;line-height:1.3">Future-fit & scalable platform</div>
        <div style="font-size:9px;color:#091C35;line-height:1.6">
          <div style="margin-bottom:4px">• <strong>Banking OS</strong> — control plane for the unified frontline</div>
          <div style="margin-bottom:4px">• <strong>Grand Central iPaaS</strong> — wraps existing core, no rip-and-replace</div>
          <div style="margin-bottom:4px">• <strong>Delivery OS</strong> — AI-native SDLC, 30% efficiency</div>
          <div>• <strong>Adopt & Build</strong> — 60+ OOTB capabilities, no lock-in</div>
        </div>
      </div>
    </div>
    <div style="margin-top:14px;padding:14px 18px;background:#091C35;border-radius:10px">
      <div style="font-size:9px;font-weight:800;letter-spacing:2px;color:rgba(255,255,255,0.5);margin-bottom:8px;text-align:center">CONNECTING TO YOUR VALIDATED NORTH STAR METRICS</div>
      <div style="display:grid;grid-template-columns:repeat(6,1fr);gap:8px">
        <div style="text-align:center;padding:8px"><div style="font-size:13px;font-weight:900;color:#3366FF">+10M</div><div style="font-size:7px;color:rgba(255,255,255,0.5);margin-top:2px">Active Customers<br>(scalable to 20M)</div></div>
        <div style="text-align:center;padding:8px;border-left:1px solid rgba(255,255,255,0.08)"><div style="font-size:13px;font-weight:900;color:#3366FF">58%→85%</div><div style="font-size:7px;color:rgba(255,255,255,0.5);margin-top:2px">Digital<br>Adoption</div></div>
        <div style="text-align:center;padding:8px;border-left:1px solid rgba(255,255,255,0.08)"><div style="font-size:13px;font-weight:900;color:#3366FF">15→30%+</div><div style="font-size:7px;color:rgba(255,255,255,0.5);margin-top:2px">NPS</div></div>
        <div style="text-align:center;padding:8px;border-left:1px solid rgba(255,255,255,0.08)"><div style="font-size:13px;font-weight:900;color:#3366FF">+200K</div><div style="font-size:7px;color:rgba(255,255,255,0.5);margin-top:2px">New Customers<br>per Month</div></div>
        <div style="text-align:center;padding:8px;border-left:1px solid rgba(255,255,255,0.08)"><div style="font-size:13px;font-weight:900;color:#3366FF">→50%</div><div style="font-size:7px;color:rgba(255,255,255,0.5);margin-top:2px">Faster<br>Time-to-Market</div></div>
        <div style="text-align:center;padding:8px;border-left:1px solid rgba(255,255,255,0.08)"><div style="font-size:13px;font-weight:900;color:#3366FF">−3pp</div><div style="font-size:7px;color:rgba(255,255,255,0.5);margin-top:2px">Cost-to-Income<br>(53.8%→50.5%)</div></div>
      </div>
    </div>
  `, bodyFull: true },

  // ════════════════════════════════════════════════════════════════
  // SLIDE 4 OF 5: 3-PHASE STRATEGY WITH CLIENT EXAMPLES
  // ════════════════════════════════════════════════════════════════
  { layout: 'content-standard', theme: 'light', label: 'RECOMMENDING A 3-PHASED GROWTH STRATEGY', title: 'Each Phase Proven by a Reference Client', subtitle: 'Your team validated this phasing during the RFP defense. Here’s the proof at each step.', body: `
    <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:14px;margin-top:6px">
      <div style="border-radius:10px;border:1px solid rgba(5,150,105,0.2);overflow:hidden">
        <div style="background:#059669;padding:12px 14px;color:#fff;position:relative">
          <div style="position:absolute;top:8px;right:12px;font-size:32px;font-weight:900;color:rgba(255,255,255,0.15)">01</div>
          <div style="font-size:8px;font-weight:800;letter-spacing:2px;color:rgba(255,255,255,0.6)">PHASE 1 · MONTHS 0–12</div>
          <div style="font-size:14px;font-weight:900;margin-top:4px;color:#fff">Establish a Premium<br>Digital Experience</div>
        </div>
        <div style="padding:14px">
          <p style="font-size:9px;color:#64748B;line-height:1.5;margin-bottom:10px">Build a differentiated, premium digital foundation to drive adoption and engagement from day one.</p>
          <div style="font-size:9px;color:#091C35;line-height:1.5;margin-bottom:10px">
            <strong style="color:#059669">Includes:</strong> Onboarding STP, Digital Banking Premium, Digital Assist, omnichannel servicing
          </div>
          <div style="padding:10px;background:rgba(5,150,105,0.06);border-radius:6px;border:1px solid rgba(5,150,105,0.15)">
            <div style="font-size:8px;font-weight:800;color:#059669;letter-spacing:1px;margin-bottom:4px">CLIENT PROOF: MCB</div>
            <p style="font-size:9px;color:#091C35;line-height:1.5;margin-bottom:6px">Progressive modernisation across 4 business lines (SME, Retail, Wealth, Commercial) and 3 countries (Mauritius, Madagascar, Seychelles).</p>
            <div style="display:flex;flex-direction:column;gap:3px">
              <div style="display:flex;justify-content:space-between;font-size:9px"><span style="color:#64748B">Digital adoption</span><span style="font-weight:800;color:#059669">48% → 93%</span></div>
              <div style="display:flex;justify-content:space-between;font-size:9px"><span style="color:#64748B">NPS</span><span style="font-weight:800;color:#059669">41 → 71</span></div>
              <div style="display:flex;justify-content:space-between;font-size:9px"><span style="color:#64748B">Customer growth (3yr)</span><span style="font-weight:800;color:#059669">+138%</span></div>
            </div>
          </div>
        </div>
      </div>
      <div style="border-radius:10px;border:1px solid rgba(51,102,255,0.2);overflow:hidden">
        <div style="background:#3366FF;padding:12px 14px;color:#fff;position:relative">
          <div style="position:absolute;top:8px;right:12px;font-size:32px;font-weight:900;color:rgba(255,255,255,0.15)">02</div>
          <div style="font-size:8px;font-weight:800;letter-spacing:2px;color:rgba(255,255,255,0.6)">PHASE 2 · MONTHS 12–24</div>
          <div style="font-size:14px;font-weight:900;margin-top:4px;color:#fff">Amplify &<br>Accelerate Growth</div>
        </div>
        <div style="padding:14px">
          <p style="font-size:9px;color:#64748B;line-height:1.5;margin-bottom:10px">Unlock revenue growth through advanced personalisation, premium experiences, and digitised end-to-end origination journeys.</p>
          <div style="font-size:9px;color:#091C35;line-height:1.5;margin-bottom:10px">
            <strong style="color:#3366FF">Includes:</strong> CLO campaigns, Digital Lending, Family Banking, Household Banking, segment propositions
          </div>
          <div style="padding:10px;background:rgba(51,102,255,0.06);border-radius:6px;border:1px solid rgba(51,102,255,0.15)">
            <div style="font-size:8px;font-weight:800;color:#3366FF;letter-spacing:1px;margin-bottom:4px">CLIENT PROOF: NBB / YALLA FAMILY BANKING</div>
            <p style="font-size:9px;color:#091C35;line-height:1.5;margin-bottom:6px">Onboarded 65% New-to-Bank customers digitally in Year 1. Family Banking proposition drove segment expansion.</p>
            <div style="display:flex;flex-direction:column;gap:3px">
              <div style="display:flex;justify-content:space-between;font-size:9px"><span style="color:#64748B">NTB digital onboarding</span><span style="font-weight:800;color:#3366FF">65% in Y1</span></div>
              <div style="display:flex;justify-content:space-between;font-size:9px"><span style="color:#64748B">Account opening time</span><span style="font-weight:800;color:#3366FF">5 minutes STP</span></div>
              <div style="display:flex;justify-content:space-between;font-size:9px"><span style="color:#64748B">Deposit growth</span><span style="font-weight:800;color:#3366FF">$200M</span></div>
            </div>
          </div>
        </div>
      </div>
      <div style="border-radius:10px;border:1px solid rgba(123,47,255,0.2);overflow:hidden">
        <div style="background:#7B2FFF;padding:12px 14px;color:#fff;position:relative">
          <div style="position:absolute;top:8px;right:12px;font-size:32px;font-weight:900;color:rgba(255,255,255,0.15)">03</div>
          <div style="font-size:8px;font-weight:800;letter-spacing:2px;color:rgba(255,255,255,0.6)">PHASE 3 · MONTHS 24–36</div>
          <div style="font-size:14px;font-weight:900;margin-top:4px;color:#fff">Expand into<br>New Segments</div>
        </div>
        <div style="padding:14px">
          <p style="font-size:9px;color:#64748B;line-height:1.5;margin-bottom:10px">Extend the platform to unlock new growth business lines, segments, and markets with conversational AI and ecosystem play.</p>
          <div style="font-size:9px;color:#091C35;line-height:1.5;margin-bottom:10px">
            <strong style="color:#7B2FFF">Includes:</strong> Conversational Banking, SME/Business expansion, Diaspora, Wealth, ecosystem partners
          </div>
          <div style="padding:10px;background:rgba(123,47,255,0.06);border-radius:6px;border:1px solid rgba(123,47,255,0.15)">
            <div style="font-size:8px;font-weight:800;color:#7B2FFF;letter-spacing:1px;margin-bottom:4px">CLIENT PROOF: NEO BY SNB / ILA BY ABC</div>
            <p style="font-size:9px;color:#091C35;line-height:1.5;margin-bottom:6px">Neo-banks for tech-savvy clients. Conversational banking deployed in production at scale.</p>
            <div style="display:flex;flex-direction:column;gap:3px">
              <div style="display:flex;justify-content:space-between;font-size:9px"><span style="color:#64748B">NEO onboardings (week 1)</span><span style="font-weight:800;color:#7B2FFF">100K</span></div>
              <div style="display:flex;justify-content:space-between;font-size:9px"><span style="color:#64748B">ILA customer growth Y1</span><span style="font-weight:800;color:#7B2FFF">+23%</span></div>
              <div style="display:flex;justify-content:space-between;font-size:9px"><span style="color:#64748B">Conversational AI</span><span style="font-weight:800;color:#7B2FFF">In production</span></div>
            </div>
          </div>
        </div>
      </div>
    </div>
  `, bodyFull: true },

  // ════════════════════════════════════════════════════════════════
  // SLIDE 5 OF 5: WHY BACKBASE OVER COMPETITION
  // ════════════════════════════════════════════════════════════════
  { layout: 'content-standard', theme: 'light', label: 'SUPPLIER SELECTION', title: 'Why Backbase — Purposefully Built for Banking at ABSA Scale', subtitle: 'Five dimensions that matter at 9.3M customers, IBM Mainframe + MuleSoft, "build, launch, hollow."', body: `
    <div style="border-radius:10px;overflow:hidden;border:1px solid #E2E8F0">
      <table style="width:100%;border-collapse:collapse;font-size:9px">
        <thead>
          <tr style="background:#091C35;color:#fff;font-size:8px;font-weight:800;letter-spacing:1px;text-transform:uppercase">
            <th style="padding:10px 12px;text-align:left;width:130px"></th>
            <th style="padding:10px 12px;text-align:left;width:25%">Plumery <span style="font-weight:400;font-size:7px;letter-spacing:0;text-transform:none;opacity:0.5;display:block">Low-code front-end</span></th>
            <th style="padding:10px 12px;text-align:left;width:35%;border-left:2px solid #3366FF;background:rgba(51,102,255,0.15)"><span style="color:#fff">Backbase</span> <span style="font-weight:400;font-size:7px;letter-spacing:0;text-transform:none;color:rgba(255,255,255,0.6);display:block">Engagement banking platform</span></th>
            <th style="padding:10px 12px;text-align:left;width:25%">Intellect <span style="font-weight:400;font-size:7px;letter-spacing:0;text-transform:none;opacity:0.5;display:block">Core + channels</span></th>
          </tr>
        </thead>
        <tbody>
          <tr style="border-bottom:1px solid #E2E8F0">
            <td style="padding:8px 12px;font-weight:800;color:#091C35;background:#F0F4F8;font-size:9px">Purpose-built for banking at scale</td>
            <td style="padding:8px 12px;color:#64748B"><span style="color:#DC2626;font-weight:900">✗</span> Early-stage startup ($3.3M funded). No bank at 9.3M scale. Front-end builder, not platform.</td>
            <td style="padding:8px 12px;color:#091C35;font-weight:600;border-left:2px solid #3366FF;background:rgba(51,102,255,0.04)"><span style="color:#059669;font-weight:900">✓</span> <strong style="color:#3366FF">Purpose-built engagement banking platform.</strong> 100+ banks worldwide. Tier-1 references. MCB at 3-country scale.</td>
            <td style="padding:8px 12px;color:#64748B"><span style="color:#DC2626;font-weight:900">✗</span> Core-first vendor extending into channels. African references are greenfield/small banks (Ethiopia, Zimbabwe), not Tier-1.</td>
          </tr>
          <tr style="border-bottom:1px solid #E2E8F0">
            <td style="padding:8px 12px;font-weight:800;color:#091C35;background:#F0F4F8;font-size:9px">Co-existence with your core</td>
            <td style="padding:8px 12px;color:#64748B"><span style="color:#DC2626;font-weight:900">✗</span> Sits on top of APIs but no orchestration layer. Every integration is custom.</td>
            <td style="padding:8px 12px;color:#091C35;font-weight:600;border-left:2px solid #3366FF;background:rgba(51,102,255,0.04)"><span style="color:#059669;font-weight:900">✓</span> <strong style="color:#3366FF">Grand Central iPaaS abstracts your core.</strong> “Build, launch, hollow” is our default architecture, not a migration phase. Keep IBM Mainframe + MuleSoft.</td>
            <td style="padding:8px 12px;color:#64748B"><span style="color:#DC2626;font-weight:900">✗</span> Tightly coupled to Intellect’s core. <strong>High migration risk.</strong> If you stay on IBM Mainframe, you carry their core anyway.</td>
          </tr>
          <tr style="border-bottom:1px solid #E2E8F0">
            <td style="padding:8px 12px;font-weight:800;color:#091C35;background:#F0F4F8;font-size:9px">Africa track record at Tier-1 scale</td>
            <td style="padding:8px 12px;color:#64748B"><span style="color:#DC2626;font-weight:900">✗</span> No bank at ABSA’s complexity. Limited managed services or 24/7 support.</td>
            <td style="padding:8px 12px;color:#091C35;font-weight:600;border-left:2px solid #3366FF;background:rgba(51,102,255,0.04)"><span style="color:#059669;font-weight:900">✓</span> <strong style="color:#3366FF">MCB, I&M, 100+ banks globally.</strong> Multi-country rollout proven across 3 African markets. 6-month MVP at MCB.</td>
            <td style="padding:8px 12px;color:#64748B"><span style="color:#DC2626;font-weight:900">✗</span> References are smaller African banks. No equivalent of MCB’s multi-country, multi-line modernisation at ABSA scale.</td>
          </tr>
          <tr style="border-bottom:1px solid #E2E8F0">
            <td style="padding:8px 12px;font-weight:800;color:#091C35;background:#F0F4F8;font-size:9px">Platform breadth — single contract</td>
            <td style="padding:8px 12px;color:#64748B"><span style="color:#DC2626;font-weight:900">✗</span> Front-end only. <strong>Equivalent scope requires 4–5 additional vendors</strong> + integration.</td>
            <td style="padding:8px 12px;color:#091C35;font-weight:600;border-left:2px solid #3366FF;background:rgba(51,102,255,0.04)"><span style="color:#059669;font-weight:900">✓</span> <strong style="color:#3366FF">Single platform, single contract.</strong> Servicing + Sales + AI + Employee Assist + Process Orchestration + iPaaS + Delivery OS.</td>
            <td style="padding:8px 12px;color:#64748B"><span style="color:#DC2626;font-weight:900">✗</span> Core + channels coupled. <strong>Equivalent engagement scope requires 5–6 additional vendors</strong> + heavy middleware.</td>
          </tr>
          <tr>
            <td style="padding:8px 12px;font-weight:800;color:#091C35;background:#F0F4F8;font-size:9px">AI-native, not bolted on</td>
            <td style="padding:8px 12px;color:#64748B"><span style="color:#D97706;font-weight:900">–</span> AI emerging — config copilot only. No production-grade agents at scale.</td>
            <td style="padding:8px 12px;color:#091C35;font-weight:600;border-left:2px solid #3366FF;background:rgba(51,102,255,0.04)"><span style="color:#059669;font-weight:900">✓</span> <strong style="color:#3366FF">AI across the full stack.</strong> Intelligence Fabric, CLO, Conversational Banking, Delivery OS — all live in production.</td>
            <td style="padding:8px 12px;color:#64748B"><span style="color:#D97706;font-weight:900">–</span> AI strong on the core side, but engagement-layer AI is limited. Customer-facing AI requires newer modules + integration.</td>
          </tr>
        </tbody>
      </table>
    </div>
    <div style="margin-top:14px;padding:12px 18px;border-radius:8px;background:#091C35;color:#fff;text-align:center">
      <div style="font-size:9px;font-weight:800;letter-spacing:2px;color:rgba(255,255,255,0.5);margin-bottom:6px">THE BOTTOM LINE</div>
      <p style="font-size:11px;font-weight:600;line-height:1.5;color:#fff">Core banking and middleware stay in their roles. <span style="color:#3366FF">Backbase is the only option that covers digital banking, onboarding, lending, employee assist, AI, and integration in a single platform.</span> Every alternative requires assembling multiple vendors — and rebuilding when the core changes.</p>
    </div>
  `, bodyFull: true },

  // ════════════════════════════════════════════════════════════════
  // CLOSE
  // ════════════════════════════════════════════════════════════════
  { layout: 'statement', variant: 'dark', label: 'TRANSITION TO ITEM 5',
    text: '“You’ve told us where you’re going. We’ve shown you why we’re the right partner. <span class="hl">At the end of today, let’s build the success scorecard together.</span>”' }
];
