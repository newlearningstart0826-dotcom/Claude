---
name: ai-motion-inspiration
description: Search a curated catalog of 968 AI-made motion graphics, product videos, explainers, animated shorts, 3D/interactive pieces and music videos (from guanmo-ai/awesome-ai-motion), including 128 creators' real public prompts and links to source code. Use when the user wants to make an animated video, motion graphics, a product explainer, a showreel, a code-driven animation (HTML/Canvas/Three.js/Remotion), or asks for inspiration, reference examples, or proven prompts for AI video/motion work.
---

# AI Motion Inspiration

A local, searchable copy of the [Awesome AI Motion](https://github.com/guanmo-ai/awesome-ai-motion)
catalog (MIT, © Guanmo / @guanmo_ai). Each entry is a real AI-assisted video work with its
creator, the model used, a summary and, where the creator shared one, the full prompt.

## When to use it

- The user wants to **make** a motion piece and would benefit from seeing what has worked.
- The user asks for **examples, references or inspiration** for AI video / motion design.
- The user wants a **starting prompt** for a product video, explainer, showreel, etc.

## How to search

Run the bundled script (Python 3, stdlib only). Paths are relative to this skill's folder.

```bash
python3 scripts/search.py product explainer --with-prompt --limit 5
python3 scripts/search.py --category interactive --with-code --sort bookmarks
python3 scripts/search.py showreel --max-seconds 30
python3 scripts/search.py --show 2103918792845963545     # full record incl. prompt text
python3 scripts/search.py --stats
```

Categories: `product`, `education`, `motion`, `characters`, `interactive`, `stories`, `music`.
Query terms are ANDed and matched against title, summary, prompt text, author and model.

`promptStatus` meanings: `original` = the creator's full prompt is included in `prompt`;
`brief` = the creator described the approach but shared no full prompt (see `promptSource`);
`unknown` = no prompt was shared.

## Workflow

1. Clarify the user's goal (format, length, subject, style, tool/stack) if it isn't clear.
2. Search for 3–6 relevant works; prefer ones with `--with-prompt` or `--with-code` when the
   user wants something they can reproduce.
3. Present each pick briefly: title, why it is relevant, author, and the gallery link
   (where the video plays). Credit the creator; link the original post.
4. If the user wants to build something, draft **their own** prompt adapted from the patterns in
   the matching originals (structure, level of detail, stack named, duration, voice/music
   instructions) — don't just copy someone else's prompt verbatim.
5. Then, if asked, build it (e.g. an HTML/Canvas/SVG or Remotion animation) in the current project.

## Caveats to pass on

- Model attribution comes from creators' own statements; prompts were not independently re-run.
- Videos are hosted on the original posts; redistribution permission is not verified.
- Some original prompts contain placeholder API keys or references to tools the user may lack —
  replace those with the user's own setup and never paste real secrets into prompts.
- The catalog is a snapshot (source commit `a37176e`, Oct 2026). For the newest works, open
  https://guanmo-ai.github.io/awesome-ai-motion/?lang=en
