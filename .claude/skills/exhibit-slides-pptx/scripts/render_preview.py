#!/usr/bin/env python3
"""Render a .pptx to page PNGs, a contact sheet and a QA page, through LibreOffice.

PowerPoint is never opened (30 Sep 2026, Shyam: "it shows repair, repair, repair... none of us will
have a PowerPoint licence"). Google Slides is the presentation app; LibreOffice is the QA renderer.

Run:  python3 render_preview.py deck.pptx [--out DIR] [--dpi 160] [--cols 2] [--pages 1,4,7]
Writes DIR/<deck>.pdf, DIR/<deck>-NN.png, DIR/<deck>_sheet.png and DIR/index.html (the QA page:
every page with its layout-check faults under it), and points <skill>/_qa/latest at DIR. In Claude
Code: preview_start {name: "apex-qa"} then open http://localhost:8861/latest/index.html in the
browser pane; anywhere else, open DIR/index.html in a browser. Prints the paths."""
import os, sys, glob, subprocess, shutil, html, datetime

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)


def soffice_path():
    for c in (shutil.which("soffice"), "/Applications/LibreOffice.app/Contents/MacOS/soffice",
              "/usr/bin/soffice", "/usr/lib/libreoffice/program/soffice"):
        if c and os.path.exists(c):
            return c
    return None


def to_pdf(pptx, out_dir):
    """The deck as a PDF through LibreOffice headless. Returns the PDF path or None."""
    base = os.path.splitext(os.path.basename(pptx))[0]
    pdf = os.path.join(out_dir, base + ".pdf")
    if os.path.exists(pdf):
        os.remove(pdf)
    soffice = soffice_path()
    if not soffice:
        sys.exit("LibreOffice is not installed (brew install --cask libreoffice); it is the only QA renderer")
    subprocess.run([soffice, "--headless", "--convert-to", "pdf", "--outdir", out_dir, pptx],
                   capture_output=True, timeout=600)
    return pdf if os.path.exists(pdf) else None


def faults_by_page(pptx):
    """{page: [fault dicts]} from scripts/layout_check.py, or {} when the checker is missing."""
    try:
        import layout_check as lc
        from pptx import Presentation
    except Exception:
        return {}
    out = {}
    for i, slide in enumerate(Presentation(pptx).slides, 1):
        try:
            f = lc.check_slide(slide, i)
        except Exception as e:
            f = [dict(kind="checker", text=str(e)[:60])]
        if f:
            out[i] = f
    return out


def fault_line(f):
    parts = [f.get("kind", "?")]
    if f.get("text"):
        parts.append(f["text"])
    extra = {k: v for k, v in f.items() if k not in ("kind", "text")}
    if extra:
        parts.append(" ".join("%s=%s" % (k, v) for k, v in extra.items()))
    return "  ".join(parts)


def qa_page(out_dir, base, pngs, faults, dpi):
    """index.html: one card per page, the page image and its faults, a faults-only switch."""
    n = len(pngs)
    nf = sum(len(v) for v in faults.values())
    cards = []
    for p in pngs:
        page = int(p.rsplit("-", 1)[1].split(".")[0])
        fl = faults.get(page, [])
        rows = "".join("<li>%s</li>" % html.escape(fault_line(f)) for f in fl)
        status = ('<ul class="faults">%s</ul>' % rows) if fl else '<div class="clean">clean</div>'
        cards.append('<section class="card%s" id="p%d"><a href="%s" target="_blank"><img src="%s" alt="page %d" loading="lazy"></a>'
                     '<div class="meta"><span class="num">%d</span>%s</div></section>'
                     % (" bad" if fl else "", page, os.path.basename(p), os.path.basename(p), page, page, status))
    doc = '''<!doctype html><html lang="en"><head><meta charset="utf-8"><title>QA %(base)s</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
:root{--navy:#091C35;--blue:#3366FF;--mut:#55647E;--hair:#D2D4D8;--tint:#F3F6F9;--red:#C0392B}
body{margin:0;background:#fff;color:var(--navy);font:14px/1.45 "Libre Franklin",-apple-system,Helvetica,Arial,sans-serif}
header{position:sticky;top:0;background:#fff;border-bottom:1px solid var(--hair);padding:12px 20px;display:flex;gap:18px;align-items:baseline;flex-wrap:wrap}
header h1{font-size:16px;font-weight:400;margin:0}
header .k{color:var(--mut);font-size:12px}
header label{margin-left:auto;font-size:12px;color:var(--mut);cursor:pointer}
main{display:grid;grid-template-columns:repeat(auto-fill,minmax(560px,1fr));gap:18px;padding:18px 20px}
.card{border:1px solid var(--hair);background:var(--tint);padding:8px}
.card.bad{border-color:var(--red)}
.card img{display:block;width:100%%;height:auto;border:1px solid var(--hair);background:#fff}
.meta{display:flex;gap:10px;padding:8px 2px 0;align-items:flex-start}
.num{color:var(--mut);font-size:12px;min-width:26px}
.clean{color:var(--mut);font-size:12px}
.faults{margin:0;padding-left:16px;font-size:12px;color:var(--red)}
body.only .card:not(.bad){display:none}
@media (max-width:640px){main{grid-template-columns:1fr;padding:12px 16px}}
</style></head><body>
<header><h1>%(base)s</h1><span class="k">%(n)d pages</span><span class="k">%(nf)d layout fault%(s)s</span>
<span class="k">LibreOffice render, %(dpi)d dpi, %(when)s</span>
<label><input type="checkbox" id="only"> faults only</label></header>
<main>%(cards)s</main>
<script>document.getElementById('only').onchange=e=>document.body.classList.toggle('only',e.target.checked)</script>
</body></html>''' % dict(base=html.escape(base), n=n, nf=nf, s="" if nf == 1 else "s", dpi=dpi,
                           when=datetime.datetime.now().strftime("%d %b %Y %H:%M"), cards="\n".join(cards))
    path = os.path.join(out_dir, "index.html")
    with open(path, "w") as f:
        f.write(doc)
    return path, nf


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if not args:
        print(__doc__); sys.exit(2)
    pptx = args[0]

    def opt(name, default):
        return sys.argv[sys.argv.index(name) + 1] if name in sys.argv else default
    out_dir = opt("--out", os.path.join(os.path.dirname(os.path.abspath(pptx)), "_preview"))
    dpi = int(opt("--dpi", "160")); cols = int(opt("--cols", "2"))
    pages = opt("--pages", None)
    os.makedirs(out_dir, exist_ok=True)
    base = os.path.splitext(os.path.basename(pptx))[0]
    for old in glob.glob(os.path.join(out_dir, base + "-*.png")):
        os.remove(old)
    pdf = to_pdf(pptx, out_dir)
    if not pdf:
        sys.exit("no PDF produced by LibreOffice")
    subprocess.run(["pdftoppm", "-r", str(dpi), "-png", pdf, os.path.join(out_dir, base)], check=True)
    pngs = sorted(glob.glob(os.path.join(out_dir, base + "-*.png")))
    if pages:
        want = [int(p) for p in pages.split(",")]
        pngs = [p for p in pngs if int(p.rsplit("-", 1)[1].split(".")[0]) in want]
    sp = None
    try:
        from PIL import Image
        ims = [Image.open(p).convert("RGB") for p in pngs]
        w = 900 if cols <= 2 else 560
        h = int(ims[0].height * w / ims[0].width); rows = (len(ims) + cols - 1) // cols
        sheet = Image.new("RGB", (cols * w + (cols + 1) * 10, rows * h + (rows + 1) * 10), (200, 200, 200))
        for i, im in enumerate(ims):
            sheet.paste(im.resize((w, h), Image.LANCZOS), (10 + (i % cols) * (w + 10), 10 + (i // cols) * (h + 10)))
        sp = os.path.join(out_dir, base + "_sheet.png"); sheet.save(sp)
    except Exception as e:
        sys.stderr.write("sheet skipped: %s\n" % e)
    qa, nf = qa_page(out_dir, base, pngs, faults_by_page(pptx), dpi)
    # <skill>/_qa/latest always points at the newest render, so one launch.json entry ("apex-qa",
    # serving <skill>/_qa) shows every deck's QA page in the Claude browser pane at /latest/index.html
    try:
        qa_dir = os.path.abspath(os.path.join(HERE, "..", "_qa"))
        os.makedirs(qa_dir, exist_ok=True)
        latest = os.path.join(qa_dir, "latest")
        if os.path.islink(latest) or os.path.exists(latest):
            os.remove(latest)
        os.symlink(os.path.abspath(out_dir), latest)
    except Exception as e:
        sys.stderr.write("latest link skipped: %s\n" % e)
    print("rendered with LibreOffice: %d pages -> %s" % (len(pngs), out_dir))
    if sp:
        print("sheet:", sp)
    print("QA page: %s  (%d layout fault%s)" % (qa, nf, "" if nf == 1 else "s"))


if __name__ == "__main__":
    main()
