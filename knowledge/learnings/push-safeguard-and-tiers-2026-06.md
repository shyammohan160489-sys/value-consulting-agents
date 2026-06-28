# Guardrails for builder-level edits (and how the tiers actually work)

**Date:** 2026-06-09 · **For:** Shyam (repo owner of `shyammohan160489-sys/value-consulting-agents`)

## The three layers (what stops a "crazy edit", and when)

| Layer | Where it acts | What it does |
|---|---|---|
| **1. Nothing** | Your laptop (local edits) | There is *no* restriction on editing `tools/**`, `.claude/**`, etc. locally. Edits and local test builds are always allowed. |
| **2. CI scope guard** | GitHub **PRs** only | `.github/workflows/enforce-contribution-scope.yml`. Blocks PRs from non-architects that touch builders/skills/tools/templates/workflows. You are now on the architect allowlist, so it won't block *your* PRs. It still protects the repo from everyone else. |
| **3. Pre-push guard** ⭐ | Your `git push` to origin | `.git/hooks/pre-push` (+ tracked copy in `.githooks/pre-push`). **Warns and BLOCKS** when a push includes architect-tier files, lists them, and requires a deliberate override. This is the real backstop against accidental builder pushes. |

Because you're now an architect, Layer 2 no longer says "no" to you — so **Layer 3 is what keeps an accidental builder change from reaching origin.**

## The pre-push guard — how it behaves

- **Sensitive paths** (block + explain): `tools/`, `.claude/`, `templates/`, `presentations/backbase-slides-app/` (slide engine), `knowledge/design-system/` (tokens), `.github/workflows/`, `.githooks/`, `CLAUDE.md`.
- **Never blocked**: `knowledge/`, `benchmarks/`, and everything under `Engagement/` — including per-client **build scripts** (`build_*_pptx.py`). You can ship decks and notes freely; only the *builders themselves* are gated.
- **Override (deliberate)**: `ALLOW_ARCHITECT_PUSH=1 git push origin <branch>`

So a normal "publish my Pictet deck + learnings" push goes through silently. A push that *also* changed `tools/frontline_2026_presenter.py` stops with a list and the override instruction.

### Reinstall / share
The active hook lives in `.git/hooks/pre-push` (not version-controlled). The tracked source is `.githooks/pre-push`. To reinstall on a fresh clone:
```bash
cp .githooks/pre-push .git/hooks/pre-push && chmod +x .git/hooks/pre-push
```

## The behavioural contract (how I, Claude, will work)
- I will **call out builder-level edits explicitly** before making them, and explain why.
- I will **never push `tools/**` or `.claude/**` to origin without showing you the file list and getting your OK** — and the hook enforces it even if I forget.
- Builder changes are prepared as **proposals in the working tree**; you decide when (and whether) they go to origin.
- Day-to-day deck/report work stays in consultant-scope paths, which are never gated.
