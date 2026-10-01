#!/usr/bin/env python3
"""Build the Apex design-system zip for the team, and prove it works from an empty folder.

Run:  python3 package_apex.py [--out DIR] [--verify] [--keep]
Writes DIR/apex-design-system-v<engine>.zip (default DIR: the current folder). The zip holds one
folder, exhibit-slides-pptx/, that drops into any repo's .claude/skills/ (or ~/.claude/skills/):
the skill, the engine and its checker, the renderer, the references, the icon sets and their
licences, the Libre Franklin files the checker measures with, the humanizer lint, and the /apex
command. --verify unzips into a fresh folder with an empty HOME, builds two example decks there,
checks them for zero-size freeforms and layout faults, and renders one page through LibreOffice
when it is installed. Nothing in the zip points back at this machine."""
import os, sys, re, io, shutil, zipfile, tempfile, subprocess, datetime

HERE = os.path.dirname(os.path.abspath(__file__))
SKILL = os.path.abspath(os.path.join(HERE, ".."))
REPO = os.path.abspath(os.path.join(SKILL, "..", "..", ".."))
DS = os.path.join(REPO, "knowledge", "design-system")
HUMANIZER = os.path.expanduser("~/.claude/skills/humanizer")
COMMAND = os.path.join(REPO, ".claude", "commands", "apex.md")


def engine_version():
    with open(os.path.join(HERE, "exhibit_pptx.py")) as f:
        head = f.read(4000)
    m = re.search(r"^v(\d+\.\d+(?:\.\d+)?) \(", head, re.M)
    return m.group(1) if m else "0"


def copy_tree(src, dst, keep=None):
    """Copy src into dst, skipping caches and anything keep() rejects."""
    for root, dirs, files in os.walk(src):
        dirs[:] = [d for d in dirs if d not in ("__pycache__", ".DS_Store", "_preview", "_qa")]
        rel = os.path.relpath(root, src)
        for fn in files:
            if fn.startswith(".") or fn.endswith((".pyc", ".pptx", ".pdf", ".png~")):
                continue
            if keep and not keep(os.path.join(rel, fn)):
                continue
            d = os.path.join(dst, rel) if rel != "." else dst
            os.makedirs(d, exist_ok=True)
            shutil.copy2(os.path.join(root, fn), os.path.join(d, fn))


README = """# Apex design system for PowerPoint decks (engine v%(ver)s, packed %(date)s)

Apex is the Backbase deck look since 24 September 2026: white pages, a three-rule hairline frame,
a 9pt navy kicker, 28pt regular titles, no bold, navy #091C35 and blue #3366FF, tinted cards and
hero numbers, drawn charts, a source footnote on every numeric page, and copy that reads like a
person wrote it. This folder is the whole system: a Claude Code skill with the engine that draws
it, the checker that measures every text box, the renderer for QA, and the assets.

Every deck is opened, edited and presented in Google Slides. Nothing here needs PowerPoint, and
nothing here ever opens it. Native PowerPoint chart objects are not used (Google Slides turns
them into pictures); charts are drawn shapes and stay editable.

## Install (three steps)

1. Unzip so the folder lands at `.claude/skills/exhibit-slides-pptx/` in your repo, or at
   `~/.claude/skills/exhibit-slides-pptx/` to have it in every project.
2. Copy `exhibit-slides-pptx/commands/apex.md` to `.claude/commands/apex.md` (so `/apex` works),
   and, if you do not have the humanizer skill yet, copy `exhibit-slides-pptx/humanizer/` to
   `~/.claude/skills/humanizer/`.
3. Install the dependencies:

   ```bash
   pip install python-pptx pillow lxml
   brew install --cask libreoffice
   brew install poppler
   ```

   LibreOffice and poppler are only for QA renders. Libre Franklin for your screen:
   `exhibit-slides-pptx/design-system/fonts/libre-franklin/` (double-click to install).

## First build

```bash
python3 .claude/skills/exhibit-slides-pptx/scripts/example_apex_stage_build.py /tmp/apex_example.pptx
python3 .claude/skills/exhibit-slides-pptx/scripts/render_preview.py /tmp/apex_example.pptx --out /tmp/apex_qa
```

Open `/tmp/apex_qa/index.html` in a browser (in Claude Code: the browser pane, `preview_start`
with that file URL). Every page is shown with its layout faults under it. The deck itself goes
to Google Drive and opens in Google Slides.

## How a deck gets built

Ask Claude for a deck ("/apex", "an Apex deck", or just a deck: Apex is the default). Claude
writes a build script next to the output, runs it, renders the pages, reads them, and ships the
`.pptx` with the script. The script is the source; the `.pptx` is never edited by hand before it
reaches Google Slides.

The rules the engine enforces on save:

- every text box is measured in the real font; overflow, bleed, overlap and a box crossing the
  footnote zone are reported (`APEX_LAYOUT=strict` refuses the deck);
- banned writing shapes are reported by the humanizer lint (the save refuses on a hard hit;
  `APEX_VOICE=warn` reports only);
- one title size, one line; in-page labels of four words at most; stat numbers on one line
  with the icon above; icons small and rare.

The catalogue of page forms is `references/exhibit-catalog.md`; the laws are in `SKILL.md`.

## What is in the folder

| Path | What |
|---|---|
| `SKILL.md`, `INSTALL.md` | the skill Claude follows, and the install notes |
| `scripts/exhibit_pptx.py` | the engine (`ExhibitDeck(look='apex')`) |
| `scripts/layout_check.py` | the text-box checker (runs on every save; also a CLI) |
| `scripts/render_preview.py` | LibreOffice render to PNG, contact sheet and QA page |
| `scripts/example_*.py` | example builds, one per family of recipes |
| `scripts/package_apex.py` | builds this zip |
| `references/` | the page catalogue, chrome spec, storyline patterns |
| `assets/` | logos and the packed line icons |
| `design-system/icons/` | Lucide (ISC) and Tabler (MIT) icon sets, with licences |
| `design-system/fonts/` | Libre Franklin (SIL OFL), used by the checker to measure text |
| `humanizer/` | the writing lint and its skill |
| `commands/apex.md` | the `/apex` command |

## Versions

The engine's own history is at the top of `scripts/exhibit_pptx.py`. This zip is engine
v%(ver)s. To update, replace the folder with the newer zip; build scripts keep working.
"""


def build(out_dir):
    ver = engine_version()
    name = "apex-design-system-v%s" % ver
    stage = tempfile.mkdtemp(prefix="apex_pack_")
    root = os.path.join(stage, "exhibit-slides-pptx")
    os.makedirs(root)
    # the skill itself
    for fn in ("SKILL.md", "INSTALL.md", "command-shim.md"):
        p = os.path.join(SKILL, fn)
        if os.path.exists(p):
            shutil.copy2(p, root)
    copy_tree(os.path.join(SKILL, "references"), os.path.join(root, "references"))
    copy_tree(os.path.join(SKILL, "assets"), os.path.join(root, "assets"))
    copy_tree(os.path.join(SKILL, "scripts"), os.path.join(root, "scripts"), keep=lambda p: p.endswith(".py"))
    # design-system assets the engine resolves (icons, fonts) and the writing lint
    for fam in ("lucide", "tabler"):
        src = os.path.join(DS, "icons", fam)
        if os.path.isdir(src):
            copy_tree(src, os.path.join(root, "design-system", "icons", fam))
    for fn in ("README.md", "LICENSE"):
        p = os.path.join(DS, "icons", fn)
        if os.path.exists(p):
            shutil.copy2(p, os.path.join(root, "design-system", "icons", fn))
    copy_tree(os.path.join(DS, "fonts", "libre-franklin"), os.path.join(root, "design-system", "fonts", "libre-franklin"),
              keep=lambda p: not p.endswith(".zip"))
    if os.path.isdir(HUMANIZER):
        copy_tree(HUMANIZER, os.path.join(root, "humanizer"))
    if os.path.exists(COMMAND):
        os.makedirs(os.path.join(root, "commands"), exist_ok=True)
        shutil.copy2(COMMAND, os.path.join(root, "commands", "apex.md"))
    with open(os.path.join(root, "README.md"), "w") as f:
        f.write(README % dict(ver=ver, date=datetime.date.today().strftime("%d %b %Y")))
    # zip it
    os.makedirs(out_dir, exist_ok=True)
    zpath = os.path.join(out_dir, name + ".zip")
    if os.path.exists(zpath):
        os.remove(zpath)
    n = 0
    with zipfile.ZipFile(zpath, "w", zipfile.ZIP_DEFLATED) as z:
        for r, _, files in os.walk(stage):
            for fn in files:
                full = os.path.join(r, fn)
                z.write(full, os.path.relpath(full, stage))
                n += 1
    shutil.rmtree(stage)
    print("packed %s: %d files, %.1f MB -> %s" % (name, n, os.path.getsize(zpath) / 1e6, zpath))
    return zpath


def verify(zpath, keep=False):
    """Unzip into a fresh folder with an empty HOME and build from there."""
    box = tempfile.mkdtemp(prefix="apex_verify_")
    home = os.path.join(box, "home"); os.makedirs(home)
    with zipfile.ZipFile(zpath) as z:
        z.extractall(box)
    skill = os.path.join(box, "exhibit-slides-pptx")
    env = dict(os.environ, HOME=home, APEX_VOICE="warn")
    env.pop("APEX_DESIGN_SYSTEM", None)
    env.pop("APEX_LAYOUT", None)
    # the empty HOME hides ~/.claude/skills (so the bundled lint must be found) but would also hide a
    # user-site python-pptx; hand the child the user site explicitly
    import site
    env["PYTHONPATH"] = os.pathsep.join(p for p in [site.getusersitepackages(), env.get("PYTHONPATH", "")] if p)
    ok = True
    # 1. the engine resolves fonts, icons and the lint from inside the folder
    probe = subprocess.run([sys.executable, "-c", (
        "import sys, os; sys.path.insert(0, %r); import exhibit_pptx as X\n"
        "print('fonts', X._FONT_DIR.startswith(%r), 'icons', (X.icon_path('users') or '').startswith(%r), "
        "'width', round(X.text_w('Apex', 28), 3))" % (os.path.join(skill, "scripts"), skill, skill))],
        capture_output=True, text=True, env=env)
    print("  probe:", (probe.stdout.strip() or probe.stderr.strip()[-300:]))
    ok &= "fonts True icons True" in probe.stdout
    # 2. two example builds, from the empty folder
    import importlib
    for ex in ("example_apex_stage_build.py", "example_apex_frameworks_build.py"):
        out = os.path.join(box, ex.replace(".py", ".pptx"))
        r = subprocess.run([sys.executable, os.path.join(skill, "scripts", ex), out], capture_output=True, text=True, env=env, cwd=box)
        built = os.path.exists(out)
        tail = [l for l in (r.stdout + r.stderr).splitlines() if l.startswith(("saved", "  LAYOUT:", "REFUSED", "Traceback", "voice check"))]
        print("  %s: %s | %s" % (ex, "built" if built else "FAILED", " | ".join(tail[-2:]) or (r.stderr.strip()[-200:])))
        ok &= built
        if built:
            import zipfile as zf, re as re_
            from lxml import etree
            A = "{http://schemas.openxmlformats.org/drawingml/2006/main}"
            zz = zf.ZipFile(out); zero = 0
            for n in zz.namelist():
                if re_.match(r"ppt/slides/slide\d+\.xml$", n):
                    root = etree.fromstring(zz.read(n))
                    zero += sum(1 for p in root.iter(A + "path") if int(p.get("w")) <= 0 or int(p.get("h")) <= 0)
            print("    zero-size freeforms: %d" % zero)
            ok &= zero == 0
    # 3. the humanizer lint came from the folder, not from HOME
    ok &= os.path.exists(os.path.join(skill, "humanizer", "scripts", "humanizer_lint.py"))
    # 4. one LibreOffice render when it is installed
    sys.path.insert(0, HERE)
    try:
        import render_preview as rp
        so = rp.soffice_path()
    except Exception:
        so = None
    if so:
        r = subprocess.run([sys.executable, os.path.join(skill, "scripts", "render_preview.py"),
                            os.path.join(box, "example_apex_stage_build.pptx"), "--out", os.path.join(box, "qa"), "--dpi", "60"],
                           capture_output=True, text=True, env=env, cwd=box)
        print("  render:", (r.stdout.strip().splitlines() or [r.stderr.strip()[-200:]])[0])
        ok &= os.path.exists(os.path.join(box, "qa", "index.html"))
    else:
        print("  render: LibreOffice not installed here, skipped")
    print("VERIFY %s (%s)" % ("PASSED" if ok else "FAILED", box if keep else "folder removed"))
    if not keep:
        shutil.rmtree(box)
    return ok


if __name__ == "__main__":
    out = sys.argv[sys.argv.index("--out") + 1] if "--out" in sys.argv else os.getcwd()
    z = build(out)
    if "--verify" in sys.argv:
        sys.exit(0 if verify(z, keep="--keep" in sys.argv) else 1)
