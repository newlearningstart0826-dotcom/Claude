---
name: chapter-builder
description: >
  Full chapter writing skill for authors. Use this skill whenever a user wants to write, draft,
  expand, or complete a chapter of their book. Trigger for any of: "write Chapter N", "draft this
  chapter", "build out this chapter", "turn my notes into a chapter", "write the full chapter",
  "expand this into a chapter", "help me write [chapter title]", "I want to write Chapter N now",
  "generate the chapter", "flesh out this chapter", or any phrasing where the user wants to go
  from a chapter outline, key points, or brief to actual prose. Works from inputs produced by the
  book-architect skill (chapter title, key ideas, purpose, hook) OR from the author's own notes.
  Outputs a fully written chapter combining story, logic, and examples — calibrated to the
  author's tone, target word count, and reader level. Also handles chapter revision, section
  rewrites, and adding/strengthening examples.
---

# Chapter Builder

A structured writing workflow that takes chapter inputs (title, key ideas, word count, structural
components) and produces a **fully written chapter** — with story, logic, and examples woven together.

The workflow has **three phases**:
1. **Chapter Brief** — gather all structural inputs before writing
2. **Chapter Draft** — produce the full written chapter
3. **Revision Loop** — refine, expand, or restructure on request

---

## Phase 1 — Chapter Brief

Before writing a single word of the chapter, collect all inputs. If the author is coming from the
**book-architect skill**, many of these are already available — extract them from context rather
than re-asking. Only ask for what's missing.

### Required Inputs

Ask for these if not already available:

| Input | What to ask |
|---|---|
| **Chapter Title** | "What's the title or working title for this chapter?" |
| **Chapter Purpose** | "What does this chapter need to accomplish in the book's arc? (1 sentence)" |
| **Key Ideas** | "What are the 3–5 main points, arguments, or lessons this chapter covers?" |
| **Target Word Count** | "How long should this chapter be? (e.g., 2,000 / 3,500 / 5,000 words)" |
| **Opening Hook Type** | "How do you want the chapter to open? Story / Question / Bold Claim / Statistic / Scene?" |
| **Closing Intent** | "What should the reader feel, know, or be ready to do at the end?" |

### Optional Inputs (ask only if not inferable from context)

| Input | What to ask |
|---|---|
| **Author's Voice** | "How would you describe your writing style? (e.g., conversational, authoritative, warm, direct)" |
| **Reader Level** | "Is the reader a beginner, intermediate, or expert on this topic?" |
| **Signature Framework** | "Does this chapter introduce or use a specific model, process, or framework? Describe it." |
| **Real Stories / Examples** | "Do you have a specific story, case study, or example you want included? Share it — even rough notes." |
| **Things to Avoid** | "Anything you want to steer clear of in this chapter? (tone, topics, phrases, clichés)" |
| **Chapter Position** | "Is this an early, middle, or late chapter? Any chapters that immediately precede or follow it?" |

### Brief Confirmation

Once you have enough to proceed, present a **Chapter Brief** back to the author:

```
CHAPTER BRIEF
─────────────────────────────────────────────────────────
TITLE:          [Chapter title]
PURPOSE:        [1-sentence role in the book]
WORD TARGET:    [e.g., 3,500 words]
STRUCTURE:      [Number of sections, rough flow]
OPENS WITH:     [Type + description of hook]
KEY IDEAS:      [Numbered list]
CLOSES WITH:    [Intended reader outcome]
VOICE/TONE:     [Style notes]
REAL EXAMPLES:  [Any author-supplied stories or data]
─────────────────────────────────────────────────────────
```

Ask: *"Does this capture everything? Any adjustments before I start writing?"*

---

## Phase 2 — Chapter Draft

### Internal Planning (do this silently before writing)

Before generating prose, plan the chapter internally:

1. **Map the section flow** — break the chapter into 4–7 named sections based on the key ideas and word count
2. **Assign word budgets** per section (they should add up to the target)
3. **Identify the story spine** — what narrative thread, case study, or running example will carry the chapter?
4. **Decide the logic sequence** — Problem → Insight → Evidence → Application? Or Story → Lesson → Framework → Action?

### Writing the Chapter

Write the full chapter as **continuous, publication-ready prose**. Do not add internal headings like "Section 1" — use real section titles that would appear in the book. Do not break flow with meta-commentary.

#### Chapter Architecture Template

Every chapter should follow this natural architecture (adapt as needed):

```
[OPENING HOOK]          → Immerse the reader immediately (story, scene, provocative claim)
[BRIDGE]                → Connect the hook to what this chapter is about
[CORE SECTION 1]        → First key idea — with explanation + example
[CORE SECTION 2]        → Second key idea — with logic + evidence or story
[CORE SECTION 3+]       → Continue through key ideas, alternating story and logic
[COMPLEXITY / NUANCE]   → Address the "yes, but..." — edge cases, common objections
[SYNTHESIS]             → Pull the ideas together into a unified insight
[CLOSING / TRANSITION]  → Land the reader, tease what comes next
```

#### The Story–Logic–Example Weave

Every chapter must weave three elements together — never let any one dominate for too long:

- **Story** — Opens emotionally, makes ideas memorable, creates identification
  - Use: anecdotes, case studies, scenes, before/afters, dialogue snippets
  - When to deploy: chapter open, after a dense logic block, to prove a point viscerally

- **Logic** — The argument, framework, or reasoning behind the idea
  - Use: cause-effect chains, data points, frameworks, step-by-step explanations
  - When to deploy: after a story lands, when building the "why this works" case

- **Example** — Concrete, specific illustration of the idea in practice
  - Use: real-world scenarios, hypothetical "imagine you're..." situations, comparisons
  - When to deploy: after each key idea, when an abstraction needs grounding

**Rhythm rule:** No more than 3 consecutive paragraphs of pure logic without a story beat or example. No story that runs more than ~400 words without anchoring back to the idea.

#### Voice & Prose Standards

- Write in the **author's voice** (from the brief). If none specified: warm, direct, confident, accessible.
- Use **short paragraphs** (3–5 sentences max). Vary sentence length for rhythm.
- Use **subheadings** for sections longer than ~600 words (use real section titles, not labels).
- Avoid: passive voice, throat-clearing openers ("In this chapter, we will..."), over-hedging, clichés.
- Favour: concrete over abstract, specific over general, active over passive, show over tell.
- **Transitions between sections** should feel natural — not "Now let's move on to..."

#### Word Count Calibration

| Target | Typical Structure |
|---|---|
| 1,500–2,000 words | 3 sections + short open/close |
| 2,500–3,500 words | 4–5 sections, moderate depth |
| 4,000–5,000 words | 5–7 sections, rich examples + framework |
| 6,000+ words | 7+ sections, multi-story spine, deep evidence |

If the content runs significantly short or long, flag it and offer to expand or trim.

### Presenting the Draft

After writing, present the chapter in full. Then add a short **Craft Note** at the end (outside the chapter text) like this:

```
─── CRAFT NOTE ────────────────────────────────────────────────────
Word count:     ~[X] words
Sections:       [N] — [Section Title 1] / [Section Title 2] / ...
Story spine:    [Describe the narrative thread used]
What worked:    [1–2 things that came together well]
Flagged:        [Anything that felt thin, assumed, or that needs real data/story from you]
────────────────────────────────────────────────────────────────────
```

---

## Phase 3 — Revision Loop

After presenting the draft, offer targeted revision modes. The author can invoke any of these:

### Revision Commands

| Command | What to do |
|---|---|
| `"Expand [section name]"` | Deepen that section — more story, evidence, or explanation to hit a higher word count |
| `"Tighten [section name]"` | Cut that section for pace without losing the key idea |
| `"Rewrite the opening"` | Generate 3 alternative opening hooks (story / bold claim / scene) for author to choose from |
| `"Add an example to [section]"` | Generate a concrete example, case study, or hypothetical for that section |
| `"Make it more [tone]"` | Rewrite in a different register — warmer / sharper / more authoritative / more conversational |
| `"Strengthen the logic in [section]"` | Tighten the argument, add evidence structure, remove hand-waving |
| `"Rewrite the close"` | Generate 2 alternative chapter endings with different emotional tones |
| `"Add my story"` | Author pastes a rough anecdote — weave it into the chapter at the right point |
| `"Full rewrite"` | Start fresh with the same brief but a different structural approach |
| `"Section breakdown"` | Pull out just the section titles + 1-sentence summary of each — for the author to approve before a full rewrite |

### Targeted Feedback Mode

If the author gives vague feedback ("this feels flat" / "not quite right"), ask one diagnostic question:

> "Is it the *voice* (how it sounds), the *structure* (what order things are in), or the *substance* (what ideas are covered)?"

Then address specifically.

---

## Writing Quality Standards

Every chapter produced must pass these internal checks before presenting:

- [ ] **Hook lands** — the opening draws the reader in within the first 3 sentences
- [ ] **Key ideas are all present** — nothing from the brief is missing
- [ ] **Story–Logic–Example weave** — no section is pure abstraction or pure narration
- [ ] **Specific, not vague** — concrete details, real numbers, named scenarios
- [ ] **Voice consistent** — tone doesn't shift mid-chapter
- [ ] **Closing earns it** — the final paragraph feels like a payoff, not a summary
- [ ] **Word count met** — within 10% of target (flag if outside this range)

---

## Integration with Book Architect

If the author used the **book-architect skill** to plan the book:

- Pull the **Chapter Brief** directly from the architecture output (Purpose, Key Ideas, Opens With, Closes With, Word Estimate)
- Carry forward the **Book Positioning Plan** (Tone & Style, Target Reader, Central Framework) as the writing context
- After completing each chapter, offer: *"Ready to move to the next chapter, or want to revisit the architecture first?"*
- Keep a running **Chapter Status** tracker in the conversation:

```
CHAPTER STATUS
──────────────────────────────────
Ch 1: [Title] ............. ✅ Draft complete
Ch 2: [Title] ............. ✅ Draft complete
Ch 3: [Title] ............. ✍️  In progress
Ch 4: [Title] ............. ⬜ Not started
...
──────────────────────────────────
```

---

## Quick Commands (invoke anytime)

| Command | Action |
|---|---|
| `"Write Chapter N"` | Start full chapter from book-architect output |
| `"I'll give you the brief"` | Collect inputs fresh without book-architect context |
| `"Just the opening"` | Write only the hook + bridge (first ~400 words) |
| `"Just the close"` | Write only the synthesis + closing (~300 words) |
| `"Section outline first"` | Produce section titles + 1-line descriptions before committing to full draft |
| `"What needs a real story here?"` | Flag which sections are weakest without author-supplied anecdotes |
| `"How long will this be?"` | Estimate word count from the current brief before writing |
