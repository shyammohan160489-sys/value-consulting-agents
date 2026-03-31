#!/usr/bin/env python3
"""
Convert CIH Executive Proposal HTML (scene-based) into a landscape-A4 PDF.
Each .scene div becomes one page.

Uses Playwright (Chromium) for pixel-perfect rendering.
"""

import re, sys, pathlib

# Accept optional CLI arg for source file (e.g. python html_to_pdf.py path/to/file.html)
if len(sys.argv) > 1:
    SRC = pathlib.Path(sys.argv[1]).resolve()
else:
    SRC = pathlib.Path(__file__).resolve().parent.parent / "Engagement/CIH Bank/Output/CIH_Executive_Proposal.html"
DST = SRC.with_suffix(".pdf")

# Landscape A4 in px at 96 dpi  (297mm × 210mm)
PAGE_W_MM = 297
PAGE_H_MM = 210
PAGE_W_PX = 1122  # 297mm * 96/25.4
PAGE_H_PX = 794   # 210mm * 96/25.4

def build_print_html(src_html: str) -> str:
    """Transform interactive scene-based HTML into a print-ready multi-page layout."""

    # ── 1. Remove <script> blocks (navigation JS) ──────────────────────
    html = re.sub(r'<script[\s\S]*?</script>', '', src_html)

    # ── 2. Remove the nav-bar ──────────────────────────────────────────
    html = re.sub(r'<div class="nav-bar">[\s\S]*?</div>\s*\n', '', html, count=1)

    # ── 2b. Inject "Backbase | n" footer into every scene ─────────────
    page_num = [0]
    def _add_footer(m):
        page_num[0] += 1
        footer = (
            f'<div class="scene-footer">'
            f'<span class="footer-brand">Backbase</span>'
            f'<span class="footer-pipe">|</span>'
            f'<span class="footer-num">{page_num[0]}</span>'
            f'</div>\n</div>'
        )
        return footer
    # Replace the closing </div> of each scene (last </div> before next scene or </body>)
    # Easier: insert footer before each scene's closing tag by finding scene blocks
    # Strategy: for each <div class="scene ... add footer before its last </div>
    scene_opens = list(re.finditer(r'<div class="scene[^"]*"', html))
    # Work backwards to preserve offsets
    for idx in range(len(scene_opens) - 1, -1, -1):
        start = scene_opens[idx].start()
        # Find where this scene's top-level div ends
        if idx + 1 < len(scene_opens):
            end_region = scene_opens[idx + 1].start()
        else:
            end_region = html.find('</body>', start)
        # Find the last </div> before end_region
        last_close = html.rfind('</div>', start, end_region)
        if last_close > 0:
            n = idx + 1
            footer_html = (
                f'\n<div class="scene-footer">'
                f'<span class="footer-brand">Backbase</span>'
                f'<span class="footer-pipe">|</span>'
                f'<span class="footer-num">{n}</span>'
                f'</div>\n'
            )
            html = html[:last_close] + footer_html + html[last_close:]

    # ── 3. Inject print-ready CSS overrides ────────────────────────────
    print_css = f"""
<style>
/* ====== PRINT OVERRIDES ====== */
@page {{
  size: {PAGE_W_MM}mm {PAGE_H_MM}mm;
  margin: 0;
}}

html, body {{
  width: {PAGE_W_PX}px !important;
  height: auto !important;
  overflow: visible !important;
  background: transparent !important;
}}

body {{
  display: block !important;
}}

/* Make every scene a fixed-size page */
.scene {{
  position: relative !important;
  opacity: 1 !important;
  transform: none !important;
  pointer-events: all !important;
  width: {PAGE_W_PX}px !important;
  height: {PAGE_H_PX}px !important;
  min-height: {PAGE_H_PX}px !important;
  max-height: {PAGE_H_PX}px !important;
  overflow: hidden !important;
  page-break-after: always !important;
  break-after: page !important;
  display: flex !important;
  flex-direction: column;
  padding: 48px 64px !important;
}}

.scene:last-of-type {{
  page-break-after: avoid !important;
  break-after: avoid !important;
}}

/* Hero / dark scenes keep their bg */
.scene-hero {{
  background: #091C35 !important;
}}

/* Remove animation – show everything immediately */
.ai {{
  opacity: 1 !important;
  transform: none !important;
  transition: none !important;
}}

/* Hide nav elements */
.nav-bar, .nav-dots, .nav-counter {{
  display: none !important;
}}

/* Clamp responsive font sizes to their upper bound for a fixed viewport */
h1 {{
  font-size: 48px !important;
}}

/* Ensure grids don't overflow */
.grid-4 {{ gap: 14px !important; }}
.grid-3 {{ gap: 16px !important; }}
.grid-2 {{ gap: 16px !important; }}
.grid-6 {{ gap: 12px !important; }}

/* Tables: prevent page break inside */
.fin-table {{ page-break-inside: avoid; }}

/* Scene-center (cover / hero): true vertical center */
.scene-center {{
  justify-content: center !important;
  align-items: center !important;
}}
</style>
"""
    # Insert before </head>
    html = html.replace('</head>', print_css + '\n</head>')

    return html


def main():
    print(f"Reading {SRC} …")
    src_html = SRC.read_text(encoding="utf-8")

    print("Building print-ready HTML …")
    print_html = build_print_html(src_html)

    # Write temp file for Playwright
    tmp = SRC.with_name("CIH_Executive_Proposal_print.html")
    tmp.write_text(print_html, encoding="utf-8")
    print(f"Wrote intermediate print HTML → {tmp}")

    # ── Render to PDF via Playwright ───────────────────────────────────
    from playwright.sync_api import sync_playwright

    print("Launching Chromium …")
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(
            viewport={"width": PAGE_W_PX, "height": PAGE_H_PX},
        )
        page.goto(tmp.as_uri(), wait_until="networkidle")

        # Let fonts load
        page.wait_for_timeout(2000)

        page.pdf(
            path=str(DST),
            width=f"{PAGE_W_MM}mm",
            height=f"{PAGE_H_MM}mm",
            margin={"top": "0", "right": "0", "bottom": "0", "left": "0"},
            print_background=True,
            prefer_css_page_size=True,
        )
        browser.close()

    print(f"✅  PDF saved → {DST}")
    print(f"    File size: {DST.stat().st_size / 1024:.0f} KB")


if __name__ == "__main__":
    main()
