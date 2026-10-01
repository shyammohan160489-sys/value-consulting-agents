# Install — exhibit-slides-pptx (the Apex design system)

For colleagues running Claude Code, on the Cortex repo or any repo. The team zip
(`apex-design-system-v<engine>.zip`, built by `scripts/package_apex.py`) holds this folder
with the icon sets, the fonts, the humanizer lint and the `/apex` command inside it, so it
needs nothing from the Cortex repo.

1. Unzip so the folder lands at `.claude/skills/exhibit-slides-pptx/` in your repo
   (or `~/.claude/skills/exhibit-slides-pptx/` to have it in every project):

   ```bash
   unzip apex-design-system-v5.7.zip -d your-repo/.claude/skills/
   ```

2. Copy `commands/apex.md` to `.claude/commands/apex.md` so `/apex` works. If you do not
   have the humanizer skill, copy `humanizer/` to `~/.claude/skills/humanizer/`.

3. Dependencies. Building needs python-pptx, Pillow and lxml; QA renders need LibreOffice
   and poppler. PowerPoint is not needed and is never opened; every deck is presented in
   Google Slides.

   ```bash
   pip install python-pptx pillow lxml
   brew install --cask libreoffice
   brew install poppler
   ```

4. Verify the kit works, then look at the QA page it writes:

   ```bash
   python3 .claude/skills/exhibit-slides-pptx/scripts/example_apex_stage_build.py /tmp/apex_example.pptx
   python3 .claude/skills/exhibit-slides-pptx/scripts/render_preview.py /tmp/apex_example.pptx --out /tmp/apex_qa
   ```

   `/tmp/apex_qa/index.html` shows every page with its layout faults. In Claude Code, open it
   in the browser pane (`preview_start` with the file URL).

5. Restart Claude Code (or start a new session). The skill registers automatically; invoke it
   with `/apex`, or by asking for a deck (Apex is the default look).

**If your Claude Code version doesn't pick up `.claude/skills/`** (older builds): copy
`command-shim.md` to `.claude/commands/exhibit-slides-pptx.md`; it points Claude at this
folder's SKILL.md, and `/exhibit-slides-pptx` will work as a slash command.

Keep the folder intact. The engine resolves its logos, icons and fonts relative to its own
path: the Cortex repo's `knowledge/design-system/` when it is there, else the `design-system/`
folder inside the skill, else `$APEX_DESIGN_SYSTEM`.
