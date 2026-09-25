# Install — exhibit-slides-pptx

For colleagues already running Claude Code on the Cortex repo (or any repo).

1. Unzip so the folder lands at `.claude/skills/exhibit-slides-pptx/` in your repo
   (or `~/.claude/skills/exhibit-slides-pptx/` to have it in every project):

   ```bash
   unzip exhibit-slides-pptx.zip -d your-repo/.claude/skills/
   ```

2. Restart Claude Code (or start a new session). The skill registers automatically;
   invoke it by asking for an "exhibit style deck" or via `/exhibit-slides-pptx`.

3. Dependency: `python-pptx` (`pip install python-pptx`). Verify the kit works:

   ```bash
   python3 .claude/skills/exhibit-slides-pptx/scripts/example_build.py /tmp/test_deck.pptx
   ```

**If your Claude Code version doesn't pick up `.claude/skills/`** (older builds): copy
`command-shim.md` to `.claude/commands/exhibit-slides-pptx.md` — it points Claude at this
folder's SKILL.md, and `/exhibit-slides-pptx` will work as a slash command.

Keep the folder intact — the engine resolves the logo assets relative to its own path.
