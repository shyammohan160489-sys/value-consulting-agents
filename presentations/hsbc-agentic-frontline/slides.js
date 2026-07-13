window.BB_SHARED_ASSETS = '../backbase-slides-app';

/* HSBC — The Path to Agentic Banking (cut-down) · Frontline 2026 Slide Engine build.
   Edits vs. May source: (1) "Neo" codename dropped → "HSBC" / descriptive framing; (2) added Conversational Banking landing-accelerator slide.
   Structured content-standard slides (structured:true) flow at NATURAL height, top-anchored — the bottom
   margin flexes with content, exactly like the hand-authored deck. NO stretch-to-fill.
   All sizes via em(px)=px/21.376, which reproduces the hand-authored deck's px measurements on this frame. */

const NAVY = '#041326', BLUE = '#3367FF', BLUED = '#264EC7', BLUEL = '#E5EBFF',
      OFF = '#F3F6F9', BORDER = '#CED2D7', MUTED = '#6B7786', FAINT = '#9CA3AF',
      RED = '#FF503C', REDL = '#FAE0DE', GREEN = '#2ECC71', GRNL = '#ECFDF5',
      PURPLE = '#6A1B9A', PURPLEL = '#F3E5F5', TEAL = '#0097A7';

/* Root is 1.67vw ⇒ 1em ≈ 1.67% of frame width; a hand-authored px (1280 frame) = 21.376px/em. */
const em = px => +(px / 21.376).toFixed(3) + 'em';

/* ---- reusable bits (natural height, top-anchored; hand-authored measurements via em()) ---- */
const card = (inner, top) =>
  `<div style="background:#fff;border:1px solid ${BORDER};${top?`border-top:3px solid ${top};`:''}padding:${em(24)} ${em(26)}">${inner}</div>`;
const badge = (t, bg, fg) =>
  `<span style="padding:0.34em 0.95em;font-size:${em(10)};font-weight:600;letter-spacing:0.09em;text-transform:uppercase;background:${bg};color:${fg};white-space:nowrap">${t}</span>`;
const cardHead = (t, b, bg, fg) =>
  `<div style="display:flex;align-items:center;gap:${em(8)};margin-bottom:${em(12)}"><h4 style="font-size:${em(17)};font-weight:600;color:${NAVY};flex:1;margin:0;line-height:1.2">${t}</h4>${b?badge(b,bg,fg):''}</div>`;
const p = (t) => `<p style="font-size:${em(14)};color:${MUTED};line-height:1.6;margin:0">${t}</p>`;
const bullets = (arr, col) => `<ul style="margin:0;padding:0 0 0 ${em(18)};font-size:${em(14)};color:${col||NAVY};line-height:1.7">${arr.map(l=>`<li style="margin-bottom:${em(5)}">${l}</li>`).join('')}</ul>`;
const callout = (strong, body, tone) => {
  const bg = tone === 'green' ? GRNL : BLUEL, bd = tone === 'green' ? GREEN : BLUE,
        tc = tone === 'green' ? '#1c7a45' : BLUED;
  return `<div style="padding:${em(16)} ${em(20)};border-left:3px solid ${bd};background:${bg}">
    <strong style="display:block;color:${NAVY};font-size:${em(15)};margin-bottom:${em(5)}">${strong}</strong>
    <span style="font-size:${em(14)};color:${tc};line-height:1.55">${body}</span></div>`;
};
const chip = (t, border, col, bg) =>
  `<span style="padding:0.34em 1em;border:1px solid ${border};${bg?`background:${bg};`:''}border-radius:2em;font-size:${em(12)};color:${col}">${t}</span>`;

const SPEAKER_NOTES = {
  1: 'Cover. Joint Backbase & Microsoft perspective for HSBC Innovation Banking. July 2026.',
  5: 'The corporate banking platform (HSBCnet successor); the "Neo" codename is dropped per Ad van der Poel — refer to it as HSBC or descriptively.',
  8: 'NEW slide — Conversational Banking as the landing accelerator: standalone offering, embedded AI, scales up the maturity curve onto the same spine.'
};

const SLIDES = [

/* 1 — COVER (native) */
{ layout: 'cover-color-block', label: 'HSBC × BACKBASE',
  title: 'HSBC — the path to\nAgentic Banking', date: 'July 2026' },

/* 2 — MARKET THESIS (native content-columns) */
{ layout: 'content-columns', label: 'THE MARKET THESIS',
  title: 'Three signals frame the next phase of banking.',
  columns: [
    { subtitle: 'Intelligence is becoming electricity.',
      body: 'Frontier model gaps on enterprise tasks are below 5% and closing. Tier-1 banks ship GenAI at parity. Feature differentiation has an 18-month half-life. <em>How</em> AI runs is the differentiator, not which model.' },
    { subtitle: 'Trust becomes infrastructure.',
      body: "Explainability, provenance, oversight and audit move from policy page to instrumented product surface. Apple's privacy stack, Mastercard's Decision Intelligence, the Nordic identity rails — trust plumbed, not marketed." },
    { subtitle: 'The intent layer is moving.',
      body: 'McKinsey sizes agentic commerce at $3–5T by 2030. A majority of executives expect AI agents to act on their behalf within 24 months. When intent moves to another player, the balance sheet becomes invisible.' }
  ]},

/* 3 — DIFFERENTIATION (content-standard, structured — 3-layer stack, natural height) */
{ layout: 'content-standard', label: 'DIFFERENTIATION, VISUALISED', structured: true,
  title: 'Three horizontal layers.',
  subtitle: 'The bottom commoditises. The top two define the next decade of banking economics.',
  body: `<div style="display:flex;flex-direction:column;gap:${em(10)}">
    <div style="display:flex;align-items:center;gap:${em(24)};padding:${em(18)} ${em(26)};border-radius:6px;background:${NAVY};color:#fff">
      <div style="flex:0 0 28%"><div style="font-size:${em(11)};font-weight:700;letter-spacing:0.14em;text-transform:uppercase;color:#C5D1FF;margin-bottom:${em(5)}">Layer 3 · Intent</div><div style="font-size:${em(16)};font-weight:600">Where customers and their agents act</div></div>
      <div style="display:flex;flex-wrap:wrap;gap:${em(8)};flex:1">${['Agent-to-bank APIs','Intent routing','Delegated authority','Outcome contracts'].map(c=>chip(c,'rgba(51,103,255,.6)','#fff')).join('')}</div>
    </div>
    <div style="display:flex;align-items:center;gap:${em(24)};padding:${em(18)} ${em(26)};border-radius:6px;background:${BLUEL};color:${NAVY}">
      <div style="flex:0 0 28%"><div style="font-size:${em(11)};font-weight:700;letter-spacing:0.14em;text-transform:uppercase;color:${BLUE};margin-bottom:${em(5)}">Layer 2 · Trust</div><div style="font-size:${em(16)};font-weight:600">Instrumented, audited, provable</div></div>
      <div style="display:flex;flex-wrap:wrap;gap:${em(8)};flex:1">${['Explainability','Provenance','Human oversight','Consent & identity','Audit trail'].map(c=>chip(c,BLUE,NAVY,'#fff')).join('')}</div>
    </div>
    <div style="display:flex;align-items:center;gap:${em(24)};padding:${em(18)} ${em(26)};border-radius:6px;background:${OFF};color:${MUTED};border:1px solid ${BORDER}">
      <div style="flex:0 0 28%"><div style="font-size:${em(11)};font-weight:700;letter-spacing:0.14em;text-transform:uppercase;color:${MUTED};margin-bottom:${em(5)}">Layer 1 · Intelligence</div><div style="font-size:${em(16)};font-weight:600;color:${MUTED}">Commoditising on an 18-month curve</div></div>
      <div style="display:flex;flex-wrap:wrap;gap:${em(8)};flex:1">${['Foundation models','Retrieval','Agents & tool use','Fine-tuning'].map(c=>chip(c,BORDER,MUTED)).join('')}</div>
    </div></div>` },

/* 4 — CIB RISK PROFILE (content-standard, structured — table, natural rows) */
{ layout: 'content-standard', label: 'THE CIB RISK PROFILE', structured: true,
  title: 'In CIB, the economics of an AI mistake are different.',
  subtitle: 'Stakes are larger, regulators closer, and the intent layer is being claimed by ERP-embedded treasury and agentic procurement tools.',
  body: `<table style="width:100%;border-collapse:collapse;font-size:${em(14)}">
    <thead><tr style="background:${NAVY};color:#fff">
      <th style="text-align:left;padding:1.15em 1.5em;font-size:${em(11)};font-weight:600;letter-spacing:0.1em;text-transform:uppercase;width:22%">Dimension</th>
      <th style="text-align:left;padding:1.15em 1.5em;font-size:${em(11)};font-weight:600;letter-spacing:0.1em;text-transform:uppercase;width:34%">Retail framing</th>
      <th style="text-align:left;padding:1.15em 1.5em;font-size:${em(11)};font-weight:600;letter-spacing:0.1em;text-transform:uppercase;width:44%">CIB framing</th></tr></thead>
    <tbody>
    ${[['Cost of an AI error','Reputational; a poor answer.','Movement on the balance sheet, capital, or a regulator-watched book.'],
       ['Trust counterparty','Customer trusting the bank.','Three-way: corporate client trusts HSBC; HSBC trusts the agent; regulator audits both.'],
       ['Where intent now sits',"Often the bank's own app.",'Increasingly TMS / ERP / treasury-agent stacks owned by the corporate.'],
       ['Failure mode at scale',"Pilots that don't graduate.",'Pilots that graduate into governance incidents.']]
      .map(r=>`<tr><td style="padding:0.9em 1.28em;border-bottom:1px solid ${BORDER};color:${NAVY};font-weight:600">${r[0]}</td><td style="padding:0.9em 1.28em;border-bottom:1px solid ${BORDER};color:${MUTED}">${r[1]}</td><td style="padding:0.9em 1.28em;border-bottom:1px solid ${BORDER};color:${MUTED}">${r[2]}</td></tr>`).join('')}
    <tr style="background:${BLUEL}"><td style="padding:0.9em 1.28em;color:${NAVY};font-weight:600">Structural conclusion</td><td style="padding:0.9em 1.28em;color:${NAVY}">Banking OS as accelerant.</td><td style="padding:0.9em 1.28em;color:${NAVY};font-weight:600">Banking OS as prerequisite to safe Agentic scale.</td></tr>
    </tbody></table>` },

/* 5 — NEW HSBC (content-standard, structured — 2 cards + callout; was "Neo") */
{ layout: 'content-standard', label: 'THE FOCUS AREA', structured: true,
  title: 'HSBC — to prove out the Agentic thesis.',
  subtitle: "HSBC's next-generation corporate banking platform, succeeding HSBCnet — the largest digital programme in the pipeline, and the natural place to prove the Agentic platform thesis.",
  body: `<div style="display:grid;grid-template-columns:1fr 1fr;gap:${em(22)}">
    ${card(cardHead('Today','Scope',BLUEL,BLUE)+bullets(['Replacement programme for HSBCnet','Conversational AI scoped as a channel capability','Cloud-native build on Azure','Integrated with Microsoft productivity and identity']))}
    <div style="background:#fff;border:1px solid ${BORDER};border-left:3px solid ${BLUE};padding:${em(24)} ${em(26)}">${cardHead('With the Agentic platform extended','Opportunity',BLUEL,BLUE)}${bullets(['Agents that act, not only respond — payments, exceptions, sanctions, settlement','One semantic model behind the agent population','One authority model governing what each agent can touch','Regulator-grade audit trail by construction'])}</div>
  </div>${callout('The platform question.','Conversational AI on a channel is a now-feature. Agentic operations across systems is the next-decade architecture. The decision is not whether AI sits inside a chat surface — it is what AI plugs into.')}` },

/* 6 — FRAGMENTATION (native content-columns, 4) */
{ layout: 'content-columns', label: 'THE FRAGMENTATION WE OBSERVE',
  title: 'A hundred-plus pilots is a sign of intent — and a structural risk.',
  columns: [
    { subtitle: 'Pilot redundancy', body: 'The same agent — KYC summarisation, document extraction, sanction triage — gets rebuilt across business units, on different stacks. None reuse the others’ work.' },
    { subtitle: 'No shared spine', body: 'Each agent reads its own source data and defines “client,” “exposure,” “limit” on its own terms. There is no semantic layer agents can stand on.' },
    { subtitle: 'No common authority model', body: 'Rules baked into code. No single place to express “this agent can adjust limits up to X for this client profile.” Without it, agents stay advisory.' },
    { subtitle: 'No factory', body: 'Each pilot built by hand. Time-to-second-agent equals time-to-first. No template, no harness, no governance pre-wiring — leverage never arrives.' }
  ]},

/* 7 — TWO RESPONSES (content-standard, structured — vs columns + callout, natural height) */
{ layout: 'content-standard', label: 'TWO RESPONSES TO AI', structured: true,
  title: 'A pattern we see consistently across Tier-1 transformations.',
  body: `<div style="display:grid;grid-template-columns:1fr 1fr;gap:${em(24)}">
    <div style="padding:${em(26)} ${em(28)};background:${REDL};border-radius:6px;border-left:4px solid ${RED}">
      <div style="font-size:${em(11)};font-weight:700;letter-spacing:0.14em;color:${RED};text-transform:uppercase;margin-bottom:${em(10)}">Bolt-on</div>
      <div style="font-size:${em(20)};font-weight:600;color:${NAVY};margin-bottom:${em(14)};line-height:1.2">AI added to product silos.</div>
      ${bullets(['Channel-by-channel agents, each owned by a different P&L','Multiple copies of the customer, none authoritative','AI fluent at the front, broken at the back','NPS plateaus, cost-to-serve does not move'],MUTED)}
    </div>
    <div style="padding:${em(26)} ${em(28)};background:${BLUEL};border-radius:6px;border-left:4px solid ${BLUE}">
      <div style="font-size:${em(11)};font-weight:700;letter-spacing:0.14em;color:${BLUE};text-transform:uppercase;margin-bottom:${em(10)}">Re-platform</div>
      <div style="font-size:${em(20)};font-weight:600;color:${NAVY};margin-bottom:${em(14)};line-height:1.2">One fabric for the customer life.</div>
      ${bullets(['One identity, one consent, one customer record','Orchestration any agent can plug into','Consistent CX across channel, branch, advisor','NPS, NTB, cost and ROE move together'])}
    </div>
  </div>${callout('The decision is not <em>whether</em> to use AI.','It is <strong>what AI plugs into</strong>.')}` },

/* 8 — CONVERSATIONAL BANKING · LANDING ACCELERATOR (NEW; content-standard, structured) */
{ layout: 'content-standard', label: 'CONVERSATIONAL BANKING · THE LANDING ACCELERATOR', structured: true,
  title: 'Conversational Banking — value in weeks, built to scale.',
  body: `<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:${em(20)}">
    ${card(cardHead('A standalone offering','Adopt',BLUEL,BLUE)+p('Deploys on its own, on Azure — no re-platform, no big-bang. A banking-grade conversational surface for corporate clients and RMs, live in weeks.'),BLUE)}
    ${card(cardHead('Embedded AI, banking-grade','Trust',BLUEL,BLUE)+p("HSBC's chosen models, grounded in the Nexus semantic layer and governed by Sentinel from day one — answers, retrieves and drafts with provenance and audit wired in."),BLUE)}
    ${card(cardHead('Scale potential','Expand',GRNL,GREEN)+p('The surface that answers today executes tomorrow. Conversational (P1) → Process (P2) → Agentic Operations (P3) on one spine. Land narrow, expand by configuration.'),GREEN)}
  </div>${callout('Why it accelerates.','It earns its keep as a standalone product, and every deployment lands onto the same Banking OS spine. The entry point and the destination are one architecture — so the first win funds the next, and nothing is thrown away.','green')}` },

/* 9 — BANKING OS (content-standard, structured — pyramid, natural bars + arrows) */
{ layout: 'content-standard', label: 'THE BANKING OS WITH BACKBASE', structured: true,
  title: 'A control plane — above systems, below agents.',
  subtitle: 'It connects and governs cores, ERPs, risk engines and model providers — the spine on which Agentic banking is built. The next decade is won at Levels 3 and 4.',
  body: (() => {
    const rows = [
      ['04 · THE MOAT','Share of Trust','Governed AI — explainable, human-in-the-loop, audit-ready',`background:linear-gradient(135deg,${BLUED},${BLUE});color:#fff`,'rgba(255,255,255,.85)'],
      ['03 · THE FRONTIER','Share of Moments','Right offer, right context, right channel, in the moment',`background:${BLUE};color:#fff`,'rgba(255,255,255,.8)'],
      ['02 · THE TISSUE','Share of Mind','A single fabric of identity, consent and service across every channel',`background:${BLUEL};color:${BLUED}`,BLUE],
      ['01 · THE FLOOR','Share of Wallet','Strong individual products — isolated, surface-level, easy to commoditise',`background:${OFF};color:${MUTED};border:1px solid ${BORDER}`,FAINT]
    ];
    return `<div style="display:flex;flex-direction:column;gap:${em(6)}">` + rows.map((r,i)=>
      `${i?`<div style="text-align:center;color:${BLUE};font-size:${em(12)};line-height:0.4;opacity:${(1-i*0.18).toFixed(2)}">▲</div>`:''}<div style="padding:${em(13)} ${em(26)};border-radius:6px;display:flex;justify-content:space-between;align-items:center;gap:${em(24)};${r[3]}"><div><div style="font-size:${em(10)};font-weight:700;letter-spacing:0.2em;color:${r[4]}">${r[0]}</div><div style="font-size:${em(20)};font-weight:700;margin-top:${em(2)}">${r[1]}</div></div><div style="font-size:${em(12)};line-height:1.4;text-align:right;max-width:22em;opacity:.95">${r[2]}</div></div>`
    ).join('') + `</div>`;
  })() },

/* 10 — ARCHITECTURE (content-standard, structured — layer stack, natural height) */
{ layout: 'content-standard', label: 'THE ARCHITECTURE', structured: true,
  title: 'Five layers, each doing a specific job.',
  body: `<div style="border:1px solid ${BORDER};border-radius:8px;overflow:hidden">
    ${[['Interaction',`background:${BLUEL};border-bottom:3px solid ${BLUE}`,BLUE,[['Composable apps · customer + employee',BORDER,NAVY],['Conversational AI surfaces',BORDER,NAVY]]],
       ['Orchestration — running the work',`background:#fff;border-bottom:1px solid ${BORDER}`,NAVY,[['Banking capabilities · micro-services',GREEN,GREEN],['Deterministic + agentic workflows',GREEN,GREEN]]],
       ['Authority — governing the work (Sentinel)',`background:${PURPLEL};border-bottom:1px solid ${BORDER}`,PURPLE,[['Decision authority + policy evaluation',PURPLE,PURPLE],['Autonomy governance + audit',PURPLE,PURPLE]]],
       ['Semantic — understanding the work (Nexus)',`background:#E0F7FA;border-bottom:1px solid ${BORDER}`,TEAL,[['Banking ontology + customer state graph',TEAL,TEAL],['Actions + context graph',TEAL,TEAL]]],
       ['Connectivity — Grand Central',`background:${NAVY}`,'#fff',[['Connectors + event streams','rgba(255,255,255,.25)','#fff'],['Marketplace ecosystem','rgba(255,255,255,.25)','#fff']]]]
      .map(l=>`<div style="padding:${em(11)} ${em(24)};${l[1]}"><div style="font-size:${em(11)};font-weight:700;letter-spacing:0.1em;text-transform:uppercase;color:${l[2]};margin-bottom:${em(7)}">${l[0]}</div><div style="display:flex;flex-wrap:wrap;gap:${em(8)}">${l[3].map(it=>`<div style="padding:0.5em 1em;background:${l[2]==='#fff'?'rgba(255,255,255,.1)':'#fff'};border:1px solid ${it[1]};border-radius:6px;font-size:${em(13)};font-weight:500;color:${it[2]};white-space:nowrap">${it[0]}</div>`).join('')}</div></div>`).join('')}
  </div>` },

/* 11 — WHAT THIS DELIVERS (native content-columns, 3) */
{ layout: 'content-columns', label: 'WHAT THIS DELIVERS',
  title: 'One spine. A factory to build on it. A runtime to run it safely.',
  columns: [
    { subtitle: 'Agentic Platform', body: 'The Banking OS itself — the spine on which every agent stands. Purpose-built for banking, model-agnostic, cloud-agnostic.' },
    { subtitle: 'Agent Factory', body: 'A repeatable build harness: templates, evaluation, governance pre-wiring, deployment pipeline, reusable skills catalogue. Time-to-Nth-agent collapses.' },
    { subtitle: 'Agentic Runtime', body: 'The execution environment: policy evaluation, decision tokens, audit, SLA and cost controls, regulator-grade observability.' }
  ]},

/* 12 — JOINT BACKBASE & MICROSOFT (content-standard, structured — 3 cards + callout) */
{ layout: 'content-standard', label: 'A JOINT BACKBASE & MICROSOFT PERSPECTIVE', structured: true,
  title: 'One architectural conversation. Two commercial wrappers.',
  subtitle: 'The Banking OS extends Microsoft’s foundation with a banking-specialist control plane; Microsoft anchors the cloud, models and productivity stack HSBC has already chosen.',
  body: `<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:${em(20)}">
    ${card(cardHead('Microsoft','Foundation',BLUEL,BLUE)+bullets(['Azure cloud','Foundation models (OpenAI / GPT-class)','Microsoft 365 + Copilot Studio','Enterprise procurement & commercials']),BLUE)}
    ${card(cardHead('Backbase','Control plane',BLUEL,BLUE)+bullets(['Banking-grade Agentic platform (Sentinel + Nexus)','Banking-domain orchestration & workflow library','Banking ontology & pre-built integrations','Azure Marketplace SKU & managed hosting']),BLUE)}
    ${card(cardHead('HSBC outcome','Outcome',GRNL,GREEN)+bullets(['A true Agentic platform, beyond channel','One Azure tenancy, one commercial wrapper','Banking-specialist tooling above a horizontal stack','A path from P1 to P3 with both partners aligned']),GREEN)}
  </div>${callout('Commercial mechanics.',"Backbase is an Azure Marketplace vendor. HSBC's existing Azure commitment draws down to procure the Banking OS — no new vendor onboarding, no new paper. Procurement compresses from quarters to weeks; Microsoft retains the customer relationship.")}` },

/* 13 — CLOSE (native thank-you) */
{ layout: 'thank-you' }

];
