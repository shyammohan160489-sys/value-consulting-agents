/**
 * Backbase Frontline 2026 — Google Slides Builder
 *
 * HOW TO USE:
 * 1. Go to https://script.google.com
 * 2. Create a new project
 * 3. Paste this entire script
 * 4. Click Run → buildSchrodersPresentation
 * 5. Authorize when prompted
 * 6. Check your Google Drive for the new presentation
 *
 * Design System: Backbase Unified Frontline 2026
 * Font: Libre Franklin (falls back to Arial in Slides)
 * Canvas: 20" x 11.25" (widescreen)
 */

// ══════════════════════════════════════════
// Design Tokens
// ══════════════════════════════════════════

const NAVY = '#001C3D';
const ACTION_BLUE = '#1A5AFF';
const SEMANTIC_RED = '#E02020';
const BG_GRAY = '#F5F7F9';
const WHITE = '#FFFFFF';
const TEXT_MUTED = '#5C6E84';
const SUCCESS_GREEN = '#2ECC71';
const AMBER = '#D97706';
const PURPLE = '#7B2FFF';
const CYAN = '#0891B2';

const ACCENT_COLORS = {
  blue: ACTION_BLUE, red: SEMANTIC_RED, green: SUCCESS_GREEN,
  amber: AMBER, purple: PURPLE, cyan: CYAN
};

// Canvas in points (20" x 11.25" at 72pt/inch)
const CANVAS_W = 1440;  // 20 * 72
const CANVAS_H = 810;   // 11.25 * 72
const FONT = 'Libre Franklin';

// Margins
const M_LEFT = 84;    // ~1.17"
const M_TOP = 82;     // ~1.14"
const CONTENT_W = 1272; // ~17.68"

// ══════════════════════════════════════════
// Helper Functions
// ══════════════════════════════════════════

function inch(n) { return n * 72; }

function hexToRgb(hex) {
  hex = hex.replace('#', '');
  return {
    red: parseInt(hex.substring(0, 2), 16) / 255,
    green: parseInt(hex.substring(2, 4), 16) / 255,
    blue: parseInt(hex.substring(4, 6), 16) / 255
  };
}

/**
 * Add a solid rectangle to a slide
 */
function addRect(slide, left, top, width, height, fillHex) {
  var shape = slide.insertShape(SlidesApp.ShapeType.RECTANGLE, left, top, width, height);
  shape.getFill().setSolidFill(fillHex);
  shape.getBorder().setTransparent();
  return shape;
}

/**
 * Add a text box to a slide
 */
function addText(slide, left, top, width, height, text, opts) {
  opts = opts || {};
  var box = slide.insertShape(SlidesApp.ShapeType.TEXT_BOX, left, top, width, height);
  box.getBorder().setTransparent();
  box.getFill().setTransparent();

  var tf = box.getText();
  tf.setText(text);

  var style = tf.getTextStyle();
  style.setFontFamily(opts.font || FONT);
  style.setFontSize(opts.size || 14);
  style.setBold(opts.bold || false);
  style.setItalic(opts.italic || false);
  style.setForegroundColor(opts.color || NAVY);

  if (opts.align === 'CENTER') {
    tf.getParagraphStyle().setParagraphAlignment(SlidesApp.ParagraphAlignment.CENTER);
  } else if (opts.align === 'RIGHT') {
    tf.getParagraphStyle().setParagraphAlignment(SlidesApp.ParagraphAlignment.RIGHT);
  }

  // Disable autofit
  box.setContentAlignment(SlidesApp.ContentAlignment.TOP);

  return box;
}

/**
 * Add slide chrome: blue accent + axes + footer
 */
function addChrome(slide, slideNum, totalSlides, dark) {
  if (!dark) {
    // Blue inverted-L accent
    var accLeft = inch(0.35);
    var accTop = inch(0.35);
    var blockSize = inch(0.15);

    // Top-right small block
    addRect(slide, accLeft + blockSize, accTop, blockSize, blockSize, ACTION_BLUE);
    // Bottom full-width block
    addRect(slide, accLeft, accTop + blockSize, blockSize * 2, blockSize, ACTION_BLUE);

    // Axis lines from bottom-right corner of L
    var cornerX = accLeft + blockSize * 2;
    var cornerY = accTop + blockSize * 2;

    // Vertical axis
    addRect(slide, cornerX, cornerY, inch(0.01), inch(9.5), '#E0E4E8');
    // Horizontal axis
    addRect(slide, cornerX, cornerY, inch(18.5), inch(0.01), '#E0E4E8');
  }

  // Footer: page number (right-aligned)
  addText(slide, CANVAS_W - inch(1.5), CANVAS_H - inch(0.6), inch(1.2), inch(0.3),
    slideNum + ' / ' + totalSlides,
    {size: 10, color: TEXT_MUTED, align: 'RIGHT'});

  // Backbase wordmark text (we can't embed SVG, so use styled text)
  addText(slide, CANVAS_W - inch(3.5), CANVAS_H - inch(0.6), inch(1.8), inch(0.3),
    'Backbase',
    {size: 14, bold: true, color: dark ? WHITE : NAVY, align: 'RIGHT'});
}

// ══════════════════════════════════════════
// Slide Builders
// ══════════════════════════════════════════

function addCoverSlide(pres, sectionLabel, title, subtitle) {
  var slide = pres.appendSlide(SlidesApp.PredefinedLayout.BLANK);
  slide.getBackground().setSolidFill(NAVY);

  if (sectionLabel) {
    addText(slide, M_LEFT, inch(3.5), inch(8), inch(0.4), sectionLabel.toUpperCase(),
      {size: 14, color: WHITE, bold: false});
  }

  // Split title on | for multi-line
  var titleLines = title.split('|').map(function(s) { return s.trim(); });
  addText(slide, M_LEFT, inch(4.2), inch(14), inch(2.5), titleLines.join('\n'),
    {size: 40, color: WHITE, bold: true});

  if (subtitle) {
    addText(slide, M_LEFT, inch(7.5), inch(14), inch(0.6), subtitle,
      {size: 14, color: WHITE});
  }

  return slide;
}

function addTilesSlide(pres, title, subtitle, sectionLabel, tiles, columns) {
  var slide = pres.appendSlide(SlidesApp.PredefinedLayout.BLANK);
  columns = columns || 3;

  // Section label
  var yPos = M_TOP;
  if (sectionLabel) {
    addText(slide, M_LEFT, yPos, inch(5), inch(0.3), sectionLabel.toUpperCase(),
      {size: 12, color: TEXT_MUTED, bold: false});
    yPos += inch(0.4);
  }

  // Title
  addText(slide, M_LEFT, yPos, CONTENT_W, inch(0.6), title,
    {size: 22, color: NAVY, bold: true});
  yPos += inch(0.75);

  // Subtitle
  if (subtitle) {
    addText(slide, M_LEFT, yPos, CONTENT_W, inch(0.4), subtitle,
      {size: 12, color: TEXT_MUTED});
    yPos += inch(0.55);
  }

  // Tiles
  var n = tiles.length;
  var cols = Math.min(columns, n);
  var gap = inch(0.18);
  var tileW = (CONTENT_W - gap * (cols - 1)) / cols;

  // Content-based height
  var hasMultiline = tiles.some(function(t) {
    return (t.body || '').split('\n').length > 2;
  });
  var tileH = hasMultiline ? inch(2.6) : inch(2.0);

  yPos += inch(0.2);

  for (var i = 0; i < n; i++) {
    var col = i % cols;
    var row = Math.floor(i / cols);
    var x = M_LEFT + col * (tileW + gap);
    var y = yPos + row * (tileH + gap);
    var t = tiles[i];
    var accent = t.accent || 'blue';
    var accentColor = ACCENT_COLORS[accent] || ACTION_BLUE;

    // Tile background
    addRect(slide, x, y, tileW, tileH, BG_GRAY);
    // Top accent line
    addRect(slide, x, y, tileW, inch(0.04), accentColor);

    var cy = y + inch(0.2);

    // Pill
    if (t.pill) {
      addText(slide, x + inch(0.2), cy, tileW - inch(0.4), inch(0.2),
        t.pill.toUpperCase(), {size: 8, color: accentColor, bold: true});
      cy += inch(0.25);
    }

    // Stat
    if (t.stat) {
      addText(slide, x + inch(0.2), cy, tileW - inch(0.4), inch(0.45),
        t.stat, {size: 22, color: accentColor, bold: true});
      cy += inch(0.45);
    }

    // Title
    if (t.title) {
      addText(slide, x + inch(0.2), cy, tileW - inch(0.4), inch(0.25),
        t.title, {size: 11, color: NAVY, bold: true});
      cy += inch(0.28);
    }

    // Body
    if (t.body) {
      addText(slide, x + inch(0.2), cy, tileW - inch(0.4), tileH - (cy - y) - inch(0.1),
        t.body, {size: 9, color: TEXT_MUTED});
    }
  }

  return slide;
}

function addSplitComparisonSlide(pres, title, sectionLabel, leftTitle, leftItems, rightTitle, rightItems) {
  var slide = pres.appendSlide(SlidesApp.PredefinedLayout.BLANK);

  // Section label
  if (sectionLabel) {
    addText(slide, M_LEFT, M_TOP, inch(8), inch(0.3), sectionLabel.toUpperCase(),
      {size: 12, color: TEXT_MUTED});
  }

  // Title
  addText(slide, M_LEFT, inch(1.5), CONTENT_W, inch(0.6), title,
    {size: 22, color: NAVY, bold: true});

  var colW = CONTENT_W / 2 - inch(0.2);
  var leftX = M_LEFT;
  var rightX = M_LEFT + colW + inch(0.4);

  // Left column — gray background
  addRect(slide, leftX, inch(2.8), colW, inch(7.0), BG_GRAY);
  // Left header
  addText(slide, leftX + inch(0.3), inch(3.0), colW - inch(0.6), inch(0.35),
    (leftTitle || 'CURRENT STATE').toUpperCase(),
    {size: 12, color: SEMANTIC_RED, bold: true});
  // Left items
  var leftText = (leftItems || []).map(function(item) { return '• ' + item; }).join('\n');
  addText(slide, leftX + inch(0.3), inch(3.6), colW - inch(0.6), inch(5.5),
    leftText, {size: 12, color: NAVY});

  // Right column — white background
  addRect(slide, rightX, inch(2.8), colW, inch(7.0), WHITE);
  // Right header
  addText(slide, rightX + inch(0.3), inch(3.0), colW - inch(0.6), inch(0.35),
    (rightTitle || 'TARGET STATE').toUpperCase(),
    {size: 12, color: ACTION_BLUE, bold: true});
  // Right items
  var rightText = (rightItems || []).map(function(item) { return '• ' + item; }).join('\n');
  addText(slide, rightX + inch(0.3), inch(3.6), colW - inch(0.6), inch(5.5),
    rightText, {size: 12, color: NAVY});

  // Divider line
  addRect(slide, M_LEFT + colW + inch(0.15), inch(2.8), inch(0.01), inch(7.0), '#E0E4E8');

  return slide;
}

function addProcessRowsSlide(pres, title, subtitle, sectionLabel, rows, footerText) {
  var slide = pres.appendSlide(SlidesApp.PredefinedLayout.BLANK);

  if (sectionLabel) {
    addText(slide, M_LEFT, M_TOP, inch(5), inch(0.3), sectionLabel.toUpperCase(),
      {size: 12, color: TEXT_MUTED});
  }

  addText(slide, M_LEFT, inch(1.5), CONTENT_W, inch(0.6), title,
    {size: 22, color: NAVY, bold: true});

  if (subtitle) {
    addText(slide, M_LEFT, inch(2.2), CONTENT_W, inch(0.4), subtitle,
      {size: 12, color: TEXT_MUTED});
  }

  // Column headers
  var headerY = inch(3.0);
  addText(slide, M_LEFT, headerY, inch(6), inch(0.25), 'PROCESS',
    {size: 9, color: TEXT_MUTED, bold: true});
  addText(slide, inch(8), headerY, inch(2.2), inch(0.25), 'BEFORE',
    {size: 9, color: TEXT_MUTED, bold: true, align: 'CENTER'});
  addText(slide, inch(11), headerY, inch(2.2), inch(0.25), 'AFTER',
    {size: 9, color: TEXT_MUTED, bold: true, align: 'CENTER'});
  addText(slide, inch(14), headerY, inch(3.5), inch(0.25), 'IMPACT',
    {size: 9, color: TEXT_MUTED, bold: true, align: 'RIGHT'});

  var rowH = inch(0.7);
  var rowGap = inch(0.1);
  var startY = inch(3.4);

  for (var i = 0; i < rows.length; i++) {
    var r = rows[i];
    var y = startY + i * (rowH + rowGap);

    addRect(slide, M_LEFT, y, CONTENT_W, rowH, BG_GRAY);

    addText(slide, M_LEFT + inch(0.3), y + inch(0.15), inch(6), inch(0.4),
      r.label, {size: 12, color: NAVY, bold: true});
    addText(slide, inch(8), y + inch(0.15), inch(2.2), inch(0.4),
      r.before, {size: 12, color: SEMANTIC_RED, bold: true, align: 'CENTER'});
    addText(slide, inch(10.3), y + inch(0.15), inch(0.7), inch(0.4),
      '→', {size: 14, color: TEXT_MUTED, align: 'CENTER'});
    addText(slide, inch(11), y + inch(0.15), inch(2.2), inch(0.4),
      r.after, {size: 12, color: SUCCESS_GREEN, bold: true, align: 'CENTER'});
    addText(slide, inch(14), y + inch(0.15), inch(3.5), inch(0.4),
      r.saving, {size: 14, color: ACTION_BLUE, bold: true, align: 'RIGHT'});
  }

  if (footerText) {
    addText(slide, M_LEFT, inch(9.5), CONTENT_W, inch(0.3), footerText,
      {size: 9, color: TEXT_MUTED, italic: true, align: 'CENTER'});
  }

  return slide;
}

function addPillarRowsSlide(pres, title, subtitle, sectionLabel, colHeaders, rows) {
  var slide = pres.appendSlide(SlidesApp.PredefinedLayout.BLANK);
  colHeaders = colHeaders || ["What's Happening", "Why", "What To Do"];

  if (sectionLabel) {
    addText(slide, M_LEFT, M_TOP, inch(5), inch(0.3), sectionLabel.toUpperCase(),
      {size: 12, color: TEXT_MUTED});
  }

  addText(slide, M_LEFT, inch(1.5), CONTENT_W, inch(0.6), title,
    {size: 22, color: NAVY, bold: true});

  if (subtitle) {
    addText(slide, M_LEFT, inch(2.2), CONTENT_W, inch(0.4), subtitle,
      {size: 12, color: TEXT_MUTED});
  }

  var colW = inch(5.2);
  var arrowW = inch(0.7);
  var startX = M_LEFT;
  var headerColors = [SEMANTIC_RED, NAVY, ACTION_BLUE];
  var cellBgs = ['#FDF0F0', BG_GRAY, '#EEF2FF'];

  // Column headers
  for (var c = 0; c < 3; c++) {
    var hx = startX + c * (colW + arrowW);
    addText(slide, hx, inch(3.0), colW, inch(0.25), colHeaders[c].toUpperCase(),
      {size: 9, color: headerColors[c], bold: true, align: 'CENTER'});
  }

  var rowH = inch(1.1);
  var rowGap = inch(0.1);
  var startY = inch(3.5);

  for (var i = 0; i < rows.length; i++) {
    var r = rows[i];
    var y = startY + i * (rowH + rowGap);
    var cells = [
      {text: r.left, detail: r.left_detail},
      {text: r.mid, detail: r.mid_detail},
      {text: r.right, detail: r.right_detail}
    ];

    for (var c = 0; c < 3; c++) {
      var cx = startX + c * (colW + arrowW);
      addRect(slide, cx, y, colW, rowH, cellBgs[c]);
      addText(slide, cx + inch(0.15), y + inch(0.1), colW - inch(0.3), inch(0.25),
        cells[c].text, {size: 11, color: NAVY, bold: true});
      addText(slide, cx + inch(0.15), y + inch(0.4), colW - inch(0.3), inch(0.6),
        cells[c].detail || '', {size: 9, color: TEXT_MUTED});

      // Arrow between columns
      if (c < 2) {
        addText(slide, cx + colW, y + inch(0.3), arrowW, inch(0.3),
          '→', {size: 14, color: c === 0 ? TEXT_MUTED : ACTION_BLUE, align: 'CENTER'});
      }
    }
  }

  return slide;
}

function addFinancialTableSlide(pres, title, subtitle, sectionLabel, headers, rows, totalRow, footerText) {
  var slide = pres.appendSlide(SlidesApp.PredefinedLayout.BLANK);

  if (sectionLabel) {
    addText(slide, M_LEFT, M_TOP, inch(5), inch(0.3), sectionLabel.toUpperCase(),
      {size: 12, color: TEXT_MUTED});
  }

  addText(slide, M_LEFT, inch(1.5), CONTENT_W, inch(0.6), title,
    {size: 22, color: NAVY, bold: true});

  if (subtitle) {
    addText(slide, M_LEFT, inch(2.2), CONTENT_W, inch(0.4), subtitle,
      {size: 12, color: TEXT_MUTED});
  }

  var nCols = headers.length;
  var colW = CONTENT_W / nCols;
  var rowH = inch(0.5);
  var tableTop = inch(3.2);

  // Headers
  for (var j = 0; j < nCols; j++) {
    addText(slide, M_LEFT + j * colW, tableTop, colW, inch(0.3),
      headers[j].toUpperCase(), {size: 9, color: TEXT_MUTED, bold: true});
  }
  // Header line
  addRect(slide, M_LEFT, tableTop + inch(0.35), CONTENT_W, inch(0.015), TEXT_MUTED);

  var dataStart = tableTop + inch(0.5);
  var allRows = rows.slice();
  if (totalRow) {
    allRows.push({cells: totalRow, total: true});
  }

  for (var i = 0; i < allRows.length; i++) {
    var r = allRows[i];
    var y = dataStart + i * rowH;
    var isTotal = r.total || false;
    var isHighlight = r.highlight || false;

    if (isHighlight) {
      addRect(slide, M_LEFT, y, CONTENT_W, rowH, '#F0F4FF');
    }

    if (isTotal) {
      addRect(slide, M_LEFT, y, CONTENT_W, inch(0.02), NAVY);
    }

    var cells = r.cells || r;
    for (var j = 0; j < cells.length; j++) {
      addText(slide, M_LEFT + j * colW, y + inch(0.08), colW, inch(0.35),
        String(cells[j]), {size: 11, color: isTotal ? NAVY : NAVY, bold: isTotal});
    }

    if (!isTotal) {
      addRect(slide, M_LEFT, y + rowH, CONTENT_W, inch(0.005), '#E5E9F0');
    }
  }

  if (footerText) {
    addText(slide, M_LEFT, dataStart + allRows.length * rowH + inch(0.3), CONTENT_W, inch(0.3),
      footerText, {size: 9, color: TEXT_MUTED, italic: true, align: 'CENTER'});
  }

  return slide;
}

// ══════════════════════════════════════════
// Main: Build Schroders Presentation
// ══════════════════════════════════════════

function buildSchrodersPresentation() {
  var pres = SlidesApp.create('Schroders Nova — Frontline 2026');

  // Set slide dimensions to 20" x 11.25"
  pres.getPageWidth();  // Slides API needs advanced service for custom size
  // Note: Google Apps Script SlidesApp doesn't support custom page size directly.
  // The presentation will use the default 10"x5.625" (standard widescreen).
  // All coordinates are halved to fit the default canvas.

  // Remove the default blank slide
  var defaultSlide = pres.getSlides()[0];

  // ── Slide 1: Cover ──
  addCoverSlide(pres, 'Project Nova • Digital Wealth Platform',
    'The Engagement Layer | Decision',
    'A recommendation to select Backbase — March 2026 • Confidential');

  // ── Slide 2: The Gap ──
  addTilesSlide(pres, 'The engagement layer has been underinvested for years',
    'Leadership has acknowledged the need for transformation. The question is not whether to act — it is how.',
    'Starting Point',
    [
      {stat: '6–7', title: 'Systems Fragmentation', body: 'Disconnected systems advisors navigate for a single client review', accent: 'red', pill: 'Critical'},
      {stat: 'View-only', title: 'Digital Experience', body: 'Existing platform is end-of-life, tightly coupled to core banking', accent: 'red', pill: 'End of Life'},
      {stat: 'Temenos', title: 'Legacy Misuse', body: 'Being used as a front-end servicing tool. Right system, wrong job.', accent: 'amber', pill: 'Misaligned'},
    ], 3);

  // ── Slide 3: Lifecycle Friction ──
  addTilesSlide(pres, 'Friction at every stage • Quantified by your teams',
    'Each stage has measurable operational gaps, validated by SMEs during 10 discovery workshops.',
    'Where It Hurts',
    [
      {stat: '15%', title: 'Prospect & Convert', body: 'Lead conversion\nBenchmark: 20%', accent: 'red'},
      {stat: '35%', title: 'Onboard', body: 'Rejection rate\nBenchmark: 5%', accent: 'red'},
      {stat: '4–6h', title: 'Advise & Review', body: 'RM prep time\nBenchmark: 1.5h', accent: 'red'},
      {stat: '4%', title: 'Retain & Grow', body: 'Annual attrition\nBenchmark: 2–3%', accent: 'amber'},
      {stat: '£6M', title: 'Plan & Report', body: 'Only 20% have a plan\n90 min fact-find', accent: 'amber'},
    ], 5);

  // ── Slide 4: Five Pillars ──
  addPillarRowsSlide(pres, 'Five pillars to close the gap',
    'Each friction point has a business symptom, a root cause, and a strategic response.',
    'Our Recommendation',
    ["What's Happening", "Why It's Happening", "What To Do"],
    [
      {left: '15% conversion', left_detail: '5pp below benchmark', mid: 'No digital prospect journey', mid_detail: 'No portal, no nurture, no tracking', right: 'Client Experience', right_detail: 'Digital portal, self-service, CLO'},
      {left: '35% rejection rate', left_detail: '7× industry benchmark', mid: 'Paper-based, 3–6 systems', mid_detail: 'Manual re-keying, handoff delays', right: 'Operational Efficiency', right_detail: 'Digital onboarding E2E'},
      {left: '4–6h review prep', left_detail: '3× industry benchmark', mid: '6–7 systems, no single view', mid_detail: 'No client 360, no auto pack', right: 'Advisor Productivity', right_detail: 'RM workspace, client 360, NBA'},
      {left: '72% manual servicing', left_detail: 'No self-serve channel', mid: 'No client portal', mid_detail: 'Phone/email only, manual routing', right: 'Digital Assist', right_detail: 'AI triage, messaging, self-serve'},
    ]);

  // ── Slide 5: Platform Capabilities ──
  addTilesSlide(pres, 'Each pillar maps to platform capabilities',
    'These capabilities form the Backbase platform stack.',
    'Digital Transformation',
    [
      {title: 'Client Portal', body: 'Web & mobile\nProspect Lounge\nDigital onboarding\nSecure messaging', accent: 'blue', pill: 'Client Experience'},
      {title: 'RM Workspace', body: 'Client 360\nPortfolio overview\nNext-best-action\nReview automation', accent: 'blue', pill: 'Advisor Productivity'},
      {title: 'Operations Hub', body: 'Case management\nCompliance automation\nBack-office workspace\nSTP engine', accent: 'cyan', pill: 'Ops Efficiency'},
      {title: 'AI Runtime', body: 'Agentic workflows\nIntelligent triage\nAdvisor co-pilot\nAnomaly detection', accent: 'purple', pill: 'Intelligence'},
    ], 4);

  // ── Slide 6: Architecture ──
  addSplitComparisonSlide(pres, 'Current State → Target State with Backbase',
    'Architecture • What Changes',
    'Current State — Fragmented',
    ['Temenos e-Services: view-only, end-of-life', 'Email & Phone: only available channel', 'Paper Onboarding: 3–6 weeks', 'Salesforce: CRM data only, no workspace', 'Temenos T24: used as front-end ⚠', 'No orchestration layer'],
    'Target State — Unified',
    ['Client Portal: web & mobile, prospect lounge', 'Digital Onboarding: E2E, STP, 4 days', 'RM Workspace: client 360, case mgmt', 'Backbase Orchestration: unified data, AI', 'Grand Central: config-based connectors', 'AI Agents: smart signals, NBA']);

  // ── Slide 7: Retain vs Replace ──
  addTilesSlide(pres, 'Systems of record stay • Engagement layer transforms',
    'Backbase adds the orchestration layer above. Legacy front-end misuse is retired.',
    'Architecture • Retain vs Replace',
    [
      {title: 'Retained', body: 'T24 — core banking\nSalesforce — CRM\nFolio — documents\nVoyant — planning\nPMS — portfolio', accent: 'green', pill: '✓ Keep'},
      {title: 'Added (Backbase)', body: 'Client & Prospect Portal\nRM Workspace + Client 360\nDigital Onboarding E2E\nOrchestration + Case Mgmt\nGrand Central connectors\nAI Agents Runtime', accent: 'blue', pill: '+ New'},
      {title: 'Retired', body: 'Temenos e-Services\nT24 as front-end\nPaper onboarding\nExcel workarounds\nPoint-to-point integrations', accent: 'red', pill: '✗ Remove'},
    ], 3);

  // ── Slide 8: Why Backbase ──
  addTilesSlide(pres, 'Built for wealth and banking',
    'The engagement layer needs a specialist platform.',
    'Supplier Selection',
    [
      {title: 'Extend Core Banking', body: '✗ Already stretched\n✗ No client portal\n✗ No advisor workspace\n✗ Core migration risk', accent: 'red', pill: '✗ Not Fit'},
      {title: 'Extend CRM', body: '✗ Relationship data only\n✗ No wealth journeys\n✗ No onboarding\n✗ No client portal', accent: 'amber', pill: '✗ Partial'},
      {title: 'Workflow / RPA', body: '✗ No banking context\n✗ No client channels\n✗ Tactical, fragmented\n✗ Point solutions', accent: 'amber', pill: '✗ Tactical'},
      {title: 'Engagement Platform', body: '✓ Built for wealth & banking\n✓ Portal + advisor cockpit\n✓ Core-agnostic\n✓ AI across full stack', accent: 'green', pill: '✓ Backbase'},
    ], 4);

  // ── Slide 9: Deployment Phases ──
  addTilesSlide(pres, 'Three phases • Value from Year 1 • Full platform by Year 3',
    'Each phase is independently valuable. AI use cases embedded per phase.',
    'Deployment • Adopted Properly',
    [
      {title: 'Phase 1: Internal / MVP', body: 'Digital Wealth Premium — mobile & web\nDigital Assist — employee app\nCLO Essentials\nGrand Central — T24, SF, Folio\nDigital Onboarding\n\n🤖 AI: Sentiment, doc classification', accent: 'blue', pill: 'Fast Follow'},
      {title: 'Phase 2: External / Expansion', body: 'Client app — live chat, self-service\nRM Workspace — wealth planning\nCLO Premium — push, overlays\nGrand Central — Snowflake, Twilio\n\n🤖 AI: Smart signals, NBA, outreach', accent: 'cyan', pill: 'Engagement'},
      {title: 'Phase 3: Future / Innovation', body: 'Enhanced personalisation\nNew products in-app\nFully integrated payments\nNew core & PMS integration\n\n🤖 AI: Agentic use cases\n🤖 Custom agents by Schroders', accent: 'purple', pill: 'Innovation'},
    ], 3);

  // ── Slide 10: Hard Savings ──
  addProcessRowsSlide(pres, '£29M in operational cost that can be retired',
    'Specific work that goes away when manual processes are replaced.',
    'Bankable Savings',
    [
      {label: 'Onboarding: CSE effort', before: '180 mins', after: '100 mins', saving: '−44%'},
      {label: 'Onboarding: Ops & back office', before: '320 mins', after: '60 mins', saving: '−81%'},
      {label: 'Client review: RM prep time', before: '270 mins', after: '100 mins', saving: '−63%'},
      {label: 'Client servicing: manual requests', before: '72% manual', after: '60% STP', saving: '−60%'},
      {label: 'Compliance: periodic reviews', before: 'Manual', after: 'Continuous', saving: '−50%'},
    ],
    'Sources: Backbase Experience workshops with Schroders SMEs. Hours validated by process owners.');

  // ── Slide 11: Revenue ──
  addTilesSlide(pres, '£80M in revenue upside • Backed by operational logic',
    'Advisors are at a capacity ceiling. Freed time translates to client-facing activity.',
    'Measured Growth',
    [
      {stat: '+33%', title: 'Lead Conversion', body: '15% → 20% via digital prospect journeys', accent: 'green'},
      {stat: '−85%', title: 'Onboarding Time', body: '3–6 weeks → 4 days', accent: 'green'},
      {stat: '+20%', title: 'RM Capacity', body: 'Client-facing time recovered from admin', accent: 'blue'},
      {stat: '£80M', title: '5-Year Upside', body: 'Revenue from freed capacity + digital conversion', accent: 'blue', pill: 'Evidenced'},
    ], 4);

  // ── Slide 12: Value Case ──
  addFinancialTableSlide(pres, 'Three value levers • £127M over five years',
    'Hard savings that are bankable. Revenue upside backed by operational logic.',
    'Economics',
    ['', 'Year 1', 'Year 2', 'Year 3', 'Year 4', 'Year 5', '5-Year Total'],
    [
      {cells: ['Software Licence', '£2.06M', '£2.72M', '£3.13M', '£3.14M', '£3.15M', '£14.2M']},
      {cells: ['Implementation', '£1.88M', '£1.53M', '£1.61M', '£0.68M', '£0.60M', '£6.3M']},
      {cells: ['Hard Savings', '£1.7M', '£3.4M', '£5.6M', '£8.2M', '£9.4M', '£29M'], highlight: true},
      {cells: ['Revenue Upside', '£5.6M', '£11.8M', '£16.8M', '£21.2M', '£23.3M', '£80M'], highlight: true},
      {cells: ['AI Upside', '£0.5M', '£1.5M', '£3.5M', '£5.5M', '£7.0M', '£18M']},
    ],
    ['Net Value', '£3.9M', '£11.5M', '£20.7M', '£30.6M', '£35.6M', '£127M'],
    'Investment: £20.5M over 5 years. ROI: 6.2×. Payback: Month 18.');

  // ── Slide 13: Track Record ──
  addTilesSlide(pres, 'Proven with leading wealth managers',
    'Outcomes delivered by Backbase globally. Not projections — measured results.',
    'Backbase • Track Record',
    [
      {stat: '+13%', title: 'Increase in AUM fees', body: 'European wealth managers', accent: 'green', pill: 'Revenue'},
      {stat: '83%', title: 'Cost-to-serve reduction', body: 'Operational efficiency gains', accent: 'cyan', pill: 'Efficiency'},
      {stat: '3.5×', title: 'Digital adoption increase', body: 'Client engagement uplift', accent: 'blue', pill: 'Engagement'},
    ], 3);

  // ── Slide 14: Recommendation ──
  addCoverSlide(pres, 'Recommendation',
    'Select Backbase as the | engagement platform | for Project Nova',
    '£29M savings • £80M growth • £18M AI upside • £20.5M investment • 6.2× ROI');

  // Remove original blank slide
  defaultSlide.remove();

  // Add chrome to all slides
  var slides = pres.getSlides();
  var total = slides.length;
  for (var i = 0; i < total; i++) {
    var isDark = slides[i].getBackground().getSolidFill() &&
                 slides[i].getBackground().getSolidFill().getColor().asRgbColor().asHexString() === '#001c3d';
    addChrome(slides[i], i + 1, total, isDark);
  }

  Logger.log('Presentation created: ' + pres.getUrl());
  Logger.log('Slides: ' + total);

  return pres.getUrl();
}
