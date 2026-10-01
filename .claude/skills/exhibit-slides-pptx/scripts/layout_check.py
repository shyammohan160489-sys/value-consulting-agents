#!/usr/bin/env python3
"""layout_check.py (v5.2.2, 28 Sep 2026): measure every text box in a .pptx against its own text, with the
real Libre Franklin metrics, and report the faults a reader sees as "bleeding", "up and down" and "lines off":

  overflow   a wrapped box whose text needs more height than the box has (the text runs out of the bottom)
  bleed      a no-wrap box whose text is wider than the box (the text runs out of the side)
  overlap    two boxes that both carry text and intersect
  footzone   content that runs into the footnote zone (y + needed height > 6.48) or past the frame (x + w > 12.45)
  rule       a hairline drawn through the text of a box
  title      a title wider than its box: it would wrap, and titles are one line at one size
  label      an in-page uppercase label of more than four words

Run: python3 layout_check.py deck.pptx [--slides 3,10] [--json out.json] [--quiet]
Exit code 1 when any fault is found, so a build can gate on it."""
import os, sys, json, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pptx import Presentation
from pptx.util import Emu
from exhibit_pptx import text_w

EMU = 914400.0
LINE = 1.25         # Libre Franklin's single line height, as a share of the size (renderers add a little)
FOOT_Y = 6.48       # the footnote zone starts here on an Apex page
FRAME_R = 12.70     # the right edge of the content area (recipes run 1.0 to 12.6)


def inches(v):
    return v / EMU


def para_lines(p, inner_w, wrap):
    """(lines, size_pt, line_spacing) for one paragraph, wrapping words greedily at inner_w."""
    runs = [(r.text, (r.font.size.pt if r.font.size else None)) for r in p.runs]
    size = next((s for (_, s) in runs if s), None) or 14.0
    ls = p.line_spacing if isinstance(p.line_spacing, float) else 1.0
    text = p.text.replace("\v", "\n")          # v5.7: <a:br/> reads back as \v; count it as a line break
    if not text.strip():
        return 1, size, ls, 0.0
    if not wrap:
        segs = text.replace("\r", "\n").split("\n")
        return len(segs), size, ls, max(text_w(seg, size) for seg in segs)
    total_w = sum(text_w(t, s or size) for (t, s) in runs)
    lines = 0
    for chunk in text.replace("\r", "\n").split("\n"):
        words = chunk.split(" ")
        cur = 0.0
        n = 1
        space = text_w(" ", size)
        for w in words:
            ww = text_w(w, size)
            if cur == 0.0:
                cur = ww
            elif cur + space + ww <= inner_w:
                cur += space + ww
            else:
                n += 1
                cur = ww
        lines += n
    return lines, size, ls, total_w


def check_slide(slide, idx):
    faults = []
    boxes = []   # (x, y, w, h, need_h, text, wrap)
    rules = []   # (x, y, w)
    # the footnote zone starts where this page's footnote starts (a wide box low on the page), else at 6.48
    foot_y = FOOT_Y
    for sh in slide.shapes:
        if getattr(sh, "has_text_frame", False) and sh.has_text_frame and sh.text_frame.text.strip():
            fy, fw = inches(sh.top), inches(sh.width)
            if 6.2 <= fy < 6.9 and fw >= 11.0:
                foot_y = min(foot_y, fy - 0.04)
    for sh in slide.shapes:
        if getattr(sh, "has_text_frame", False) and sh.has_text_frame and sh.text_frame.text.strip():
            tf = sh.text_frame
            x, y, w, h = inches(sh.left), inches(sh.top), inches(sh.width), inches(sh.height)
            ml = inches(tf.margin_left or 0); mr = inches(tf.margin_right or 0)
            mt = inches(tf.margin_top or 0); mb = inches(tf.margin_bottom or 0)
            inner_w = max(0.1, w - ml - mr)
            wrap = tf.word_wrap is not False
            need = mt + mb
            widest = 0.0
            paras = list(tf.paragraphs)
            for k, p in enumerate(paras):
                n, size, ls, tw = para_lines(p, inner_w, wrap)
                need += n * size / 72.0 * LINE * ls
                if k < len(paras) - 1:
                    need += (p.space_after.pt if p.space_after is not None else 0.0) / 72.0
                widest = max(widest, tw)
            text = tf.text.strip().replace("\n", " / ")
            snippet = (text[:48] + "…") if len(text) > 48 else text
            ext_w = min(w, widest) if wrap else widest      # what the text actually covers
            ext_h = need
            boxes.append(dict(x=x, y=y, w=w, h=h, ew=ext_w, eh=ext_h, text=snippet, wrap=wrap))
            if wrap and need > h + 0.06:
                faults.append(dict(kind="overflow", text=snippet, box_h=round(h, 2), need_h=round(need, 2), y=round(y, 2)))
            if not wrap and widest > inner_w + 0.03:
                faults.append(dict(kind="bleed", text=snippet, box_w=round(w, 2), text_w=round(widest, 2), y=round(y, 2)))
            is_foot = (6.2 <= y < 6.9 and w >= 11.0)
            # the title: one line at one size (v5.4); a title wider than its box would wrap
            first_size = next((p.runs[0].font.size.pt for p in paras if p.runs and p.runs[0].font.size), None)
            if 1.0 <= y < 1.7 and first_size and first_size >= 26 and widest > inner_w + 0.03:
                faults.append(dict(kind="title", text=snippet, chars=len(text), text_w=round(widest, 2), box_w=round(inner_w, 2)))
            # an in-page label (uppercase, small) runs at most four words (Shyam, 28 Sep 2026)
            if 1.9 <= y < 6.2 and first_size and first_size <= 11 and text.upper() == text and any(ch.isalpha() for ch in text):
                words = [t for t in text.replace("·", " ").split() if t.replace(",", "").replace(".", "").replace("'", "").isalpha()]
                if len(words) > 4 and sum(ch.isalpha() for ch in text) >= 6:
                    faults.append(dict(kind="label", text=snippet, words=len(words)))
            content = (1.9 <= y < foot_y) or (y >= foot_y and not is_foot and y < 7.0)
            if content and y + ext_h > foot_y + 0.02:
                faults.append(dict(kind="footzone", text=snippet, y=round(y, 2), bottom=round(y + ext_h, 2)))
            if content and x + ext_w > FRAME_R:
                faults.append(dict(kind="footzone", text=snippet, right=round(x + ext_w, 2)))
        elif sh.shape_type is not None and not getattr(sh, "has_chart", False):
            try:
                x, y, w, h = inches(sh.left), inches(sh.top), inches(sh.width), inches(sh.height)
            except Exception:
                continue
            if h <= 0.02 and w > 0.5:
                rules.append((x, y, w))
    # overlaps between content boxes
    content = [b for b in boxes if 1.9 <= b["y"] < 7.0 and not (6.2 <= b["y"] < 6.9 and b["w"] >= 11.0)]
    for i in range(len(content)):
        for j in range(i + 1, len(content)):
            a, b = content[i], content[j]
            ah, bh = a["eh"], b["eh"]
            ix = min(a["x"] + a["ew"], b["x"] + b["ew"]) - max(a["x"], b["x"])
            iy = min(a["y"] + ah, b["y"] + bh) - max(a["y"], b["y"])
            if ix > 0.05 and iy > 0.05 and ix * iy > 0.03:
                faults.append(dict(kind="overlap", text=a["text"], other=b["text"], area=round(ix * iy, 2)))
    # rules through text
    for (rx, ry, rw) in rules:
        for b in content:
            bh = b["eh"]
            if b["y"] + 0.06 < ry < b["y"] + bh - 0.06 and rx < b["x"] + b["ew"] and rx + rw > b["x"]:
                faults.append(dict(kind="rule", text=b["text"], rule_y=round(ry, 2), text_bottom=round(b["y"] + bh, 2)))
    return faults


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if not args:
        print(__doc__); sys.exit(2)
    prs = Presentation(args[0])
    only = None
    if "--slides" in sys.argv:
        only = {int(v) for v in sys.argv[sys.argv.index("--slides") + 1].split(",")}
    quiet = "--quiet" in sys.argv
    report = {}
    total = 0
    kinds = {}
    for i, s in enumerate(prs.slides, 1):
        if only and i not in only:
            continue
        f = check_slide(s, i)
        if f:
            report[i] = f
            total += len(f)
            for x in f:
                kinds[x["kind"]] = kinds.get(x["kind"], 0) + 1
            if not quiet:
                print("slide %d: %d fault(s)" % (i, len(f)))
                for x in f:
                    detail = {k: v for k, v in x.items() if k not in ("kind", "text")}
                    print("   %-9s %s  %s" % (x["kind"], x["text"], detail))
    print("=== %s: %d fault(s) on %d slide(s) of %d · %s" % (os.path.basename(args[0]), total, len(report), len(prs.slides),
                                                          ", ".join("%s %d" % kv for kv in sorted(kinds.items()))))
    if "--json" in sys.argv:
        json.dump(report, open(sys.argv[sys.argv.index("--json") + 1], "w"), indent=1)
    sys.exit(1 if total else 0)


if __name__ == "__main__":
    main()
