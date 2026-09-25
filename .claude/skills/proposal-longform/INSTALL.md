# Install — proposal-longform

For colleagues already running Claude Code on the Cortex repo (or any repo).

1. Unzip so the folder lands at `.claude/skills/proposal-longform/` in your repo
   (or `~/.claude/skills/proposal-longform/` to have it in every project):

   ```bash
   unzip proposal-longform.zip -d your-repo/.claude/skills/
   ```

2. Restart Claude Code (or start a new session). Invoke by asking for an "interactive
   proposal", "bilingual proposal with pricing sliders", or via `/proposal-longform`.

3. No dependencies — the output is a single HTML file. Try the demo right away:
   open `assets/proposal_longform_template.html` in a browser, flip EN/العربية, move the
   sliders, click "Executive readout (PDF)".

**If your Claude Code version doesn't pick up `.claude/skills/`** (older builds): copy
`command-shim.md` to `.claude/commands/proposal-longform.md` — it points Claude at this
folder's SKILL.md, and `/proposal-longform` will work as a slash command.
