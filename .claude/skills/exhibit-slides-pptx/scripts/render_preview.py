#!/usr/bin/env python3
"""Render a .pptx to page PNGs and a contact sheet for QA, through PowerPoint itself when it is
installed (the true renderer: real fonts, real shapes), else through LibreOffice.

Run:  python3 render_preview.py deck.pptx [--out DIR] [--dpi 160] [--cols 2] [--pages 1,4,7]
Writes DIR/<deck>.pdf, DIR/<deck>-NN.png and DIR/<deck>_sheet.png; prints the paths."""
import os, sys, glob, subprocess, shutil

def to_pdf(pptx, out_dir):
    base = os.path.splitext(os.path.basename(pptx))[0]
    pdf = os.path.join(out_dir, base + ".pdf")
    if os.path.exists(pdf):
        os.remove(pdf)
    if os.path.isdir("/Applications/Microsoft PowerPoint.app"):
        # open a renamed copy, so a deck the user has open in PowerPoint never collides
        qa_copy = os.path.join(out_dir, base + "__qa.pptx")
        shutil.copy(pptx, qa_copy)
        hfs = subprocess.run(["osascript", "-e", 'POSIX file "%s" as string' % pdf], capture_output=True, text=True).stdout.strip()
        script = '''
with timeout of 90 seconds
tell application "Microsoft PowerPoint"
    open POSIX file "%s"
    delay 1
    set thePres to active presentation
    save thePres in "%s" as save as PDF
    close thePres saving no
end tell
end timeout''' % (os.path.abspath(qa_copy), hfs)
        for attempt in (1, 2):
            r = subprocess.run(["osascript", "-e", script], capture_output=True, text=True, timeout=240)
            if os.path.exists(pdf):
                return pdf, "PowerPoint"
            sys.stderr.write("PowerPoint export attempt %d failed: %s\n" % (attempt, r.stderr.strip()[:160]))
            import time; time.sleep(2)
        sys.stderr.write("falling back to LibreOffice\n")
    soffice = shutil.which("soffice") or "/Applications/LibreOffice.app/Contents/MacOS/soffice"
    subprocess.run([soffice, "--headless", "--convert-to", "pdf", "--outdir", out_dir, pptx], capture_output=True, timeout=300)
    return (pdf if os.path.exists(pdf) else None), "LibreOffice"

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
    pdf, how = to_pdf(pptx, out_dir)
    if not pdf:
        sys.exit("no PDF produced")
    cmd = ["pdftoppm", "-r", str(dpi), "-png"]
    if pages:
        pass
    subprocess.run(cmd + [pdf, os.path.join(out_dir, base)], check=True)
    pngs = sorted(glob.glob(os.path.join(out_dir, base + "-*.png")))
    if pages:
        want = [int(p) for p in pages.split(",")]
        pngs = [p for p in pngs if int(p.rsplit("-", 1)[1].split(".")[0]) in want]
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
        sp = None; sys.stderr.write("sheet skipped: %s\n" % e)
    print("rendered with %s: %d pages -> %s" % (how, len(pngs), out_dir))
    if sp:
        print("sheet:", sp)

if __name__ == "__main__":
    main()
