#!/usr/bin/env python3
"""Assemble a single self-contained HTML deck from the Frontline 2026 engine.
Inlines the deck-template CSS/body, engine.js, slides.js, and the bg.jpg as base64."""
import base64
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
APP = HERE.parent / "backbase-slides-app"
TITLE = "The Advisor Cockpit — A Backbase Point of View"
OUT = HERE / "advisor-cockpit-pov.html"

template = (APP / "deck-template.html").read_text()
engine = (APP / "engine.js").read_text()
slides = (HERE / "slides.js").read_text()
bg_b64 = base64.b64encode((APP / "images" / "bg.jpg").read_bytes()).decode()
bg_uri = f"data:image/jpeg;base64,{bg_b64}"

# Inline the background image referenced inside engine.js template literals.
engine = engine.replace("${BB_SHARED_ASSETS}/images/bg.jpg", bg_uri)

# Swap the two external <script> tags for inline scripts (slides BEFORE engine).
html = template.replace("<title>DECK_TITLE</title>", f"<title>{TITLE}</title>")
html = html.replace('<script src="slides.js"></script>', f"<script>\n{slides}\n</script>")
html = html.replace(
    '<script src="../backbase-slides-app/engine.js"></script>',
    f"<script>\n{engine}\n</script>",
)

OUT.write_text(html)
size_kb = OUT.stat().st_size / 1024
print(f"Wrote {OUT.name} ({size_kb:.0f} KB)")
assert "DECK_TITLE" not in html, "title placeholder not replaced"
assert 'src="slides.js"' not in html and "engine.js\"" not in html, "external scripts remain"
assert "${BB_SHARED_ASSETS}/images/bg.jpg" not in html, "bg.jpg not inlined"
print("Self-contained: OK")
