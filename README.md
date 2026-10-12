# Claude — Book Writing Studio

The [awesome-book-writing-suite](https://github.com/nkme2007/awesome-book-writing-suite)
(12 skills + orchestrating instructions) set up for both Claude Code and claude.ai.

## Option A — Claude Code (this repo, ready to go)

Open this repo in Claude Code (CLI, desktop, or claude.ai/code). It picks up:

- `CLAUDE.md` — the studio conductor (pipeline, handoffs, review loop)
- `.claude/skills/*/SKILL.md` — the 12 skills, invokable as `/idea-stress-tester`,
  `/chapter-builder`, etc., or triggered automatically by what you ask
- `book/` — where your project state, drafts, and reviews are saved

Start with: *"Let's start my book. Here's the idea: …"*

## Option B — claude.ai Project

1. claude.ai → **Settings → Capabilities → Skills** → upload each zip in
   [`claude-ai-upload/`](claude-ai-upload/) (12 files). Code execution must be enabled.
2. **Projects → New Project** → name it `Book Writing Studio`.
3. Paste [`claude-ai-upload/PROJECT_INSTRUCTIONS.md`](claude-ai-upload/PROJECT_INSTRUCTIONS.md)
   into the project's instructions.
4. Start a chat — the studio opens with a first-session intake.

## The pipeline

idea-stress-tester → voice-calibrator → book-architect → narrative-spine-builder →
research-evidence-builder → chapter-builder → review loop (red-team-critic,
beta-reader-simulator, reader-journey-mapper) → editor-sharpener →
book-launch-kit → content-repurposer
