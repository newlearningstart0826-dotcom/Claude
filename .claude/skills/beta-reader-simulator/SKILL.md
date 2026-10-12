---
name: beta-reader-simulator
description: >
  Beta reader simulation skill for authors. Use this skill whenever an author wants to know how
  real readers will experience their writing before publishing or sharing it. Trigger for: "simulate
  a beta reader", "how will readers react to this?", "what will my reader think?", "test this
  chapter on a reader", "does this land?", "will readers follow this?", "read this as my target
  reader", "where will readers get confused?", "where will they disengage?", "what questions does
  this raise?", "does this resonate?", "read this as a skeptic", "play devil's advocate on this
  chapter", "where will I lose the reader?", "does the opening hook work?", "will readers trust
  me here?", or any phrasing where the author wants to pressure-test their writing through a
  reader's eyes rather than an editor's. Different from editor-sharpener (which looks at craft)
  — this skill looks at comprehension, engagement, emotion, and belief. Works on individual
  chapters, sections, or a full manuscript.
---

# Beta Reader Simulator

A skill that reads the author's writing through the eyes of real reader personas — simulating
the comprehension, engagement, confusion, skepticism, and emotional response a live reader
would have, page by page.

**This is different from the editor-sharpener.** The editor looks at craft: clarity, flow,
authority, fluff. The beta reader looks at *experience*: Did I follow that? Do I believe this?
Did I care? Where did I skim? What question is burning in my head right now? Where did I feel
seen — or talked down to?

The workflow has **four modes**:
1. **Full Beta Read** — simulate 2–3 reader personas reading a full chapter with live reactions
2. **Targeted Reader Test** — test a specific element (opening hook, a key argument, the close)
3. **Confusion Mapper** — identify exactly where comprehension breaks down and why
4. **Manuscript-Level Read** — simulate reader experience across multiple chapters

---

## Before Reading: Intake

Collect context before simulating. If the author is coming from **book-architect**, most of
this is already available — extract from context, only ask for what's missing.

| Input | What to ask |
|---|---|
| **Target reader profile** | "Who is your ideal reader — their background, what they already know, what they're hoping to get from this book?" |
| **Chapter purpose** | "What should the reader feel, know, or be ready to do by the end of this chapter?" |
| **Where it sits in the book** | "Is this an early, middle, or late chapter? Will the reader have context from earlier chapters?" |
| **What you're most unsure about** | "What's the one thing about this chapter you most want reader feedback on?" |

If the author just pastes content without context, infer what you can and proceed with
**Mode 1**, flagging any assumptions made.

---

## Reader Personas Library

Always simulate at least **2 personas** per read. Select from this library based on the
book's target audience — or build a custom persona if the author specifies one.

### Core Personas (select the most relevant 2–3)

---

**PERSONA A — The Ideal Reader**
*The person the book is written for, exactly.*
- Knows enough to follow without hand-holding
- Came to this book with a specific problem or aspiration
- Will give the book the benefit of the doubt — but won't finish it if it stops delivering
- Reading voice: engaged, slightly impatient, mentally checking the book against their own experience
- What they notice: whether the ideas are real and actionable, whether the author understands
  their world, whether the examples ring true
- What makes them put the book down: when it feels like the author is talking about their
  experience rather than to them

---

**PERSONA B — The Skeptic**
*Intelligent, has read widely in this space, and arrives with arms partially crossed.*
- Has read similar books and found them overpromising
- Will push back on any claim that feels too neat or too universal
- Notices every hedge, every unsupported assertion, every cliché
- Reading voice: analytical, slightly combative, making mental counterarguments
- What they notice: evidence quality, intellectual honesty, whether the author acknowledges
  complexity or smooths it over
- What makes them trust the author: admitting limitations, engaging with counterarguments,
  being specific where others are vague

---

**PERSONA C — The Newcomer**
*Motivated but new to the topic — doesn't have the background the author assumes.*
- Will get lost if jargon isn't defined
- Needs more context and signposting than the ideal reader
- Will feel excluded if the author writes only for people who already get it
- Reading voice: eager but easily overwhelmed, sometimes unsure if they're following correctly
- What they notice: unexplained terms, assumed knowledge, jumps in logic that feel too big
- What makes them feel safe: recaps, clear signposting, moments where the author acknowledges
  "this might be new to you"

---

**PERSONA D — The Busy Professional**
*Reads in 15-minute windows, skims when it's dense, won't finish chapters that don't pay off fast.*
- Will skip to subheadings to decide whether to read a section
- Needs a reason to keep reading in the first paragraph of every section
- Will not tolerate three pages of setup before the payoff
- Reading voice: efficient, slightly distracted, conscious of time
- What they notice: whether the chapter opener justifies the time investment, whether key ideas
  are easy to extract, whether there's fat they can trim
- What makes them stay: quick wins, clear structure, sentences that reward reading every word

---

**PERSONA E — The Practitioner**
*Already doing some version of what the book teaches — came to go deeper, not to be convinced.*
- Will be irritated by basics they already know
- Wants nuance, edge cases, advanced applications
- Most valuable reader for business/professional non-fiction
- Reading voice: "I know this part... I know this too... oh, *this* is new"
- What they notice: whether the author is ahead of them or slightly behind, whether examples
  reflect real-world complexity or textbook simplicity
- What makes them recommend the book: one insight they genuinely hadn't considered before

---

**PERSONA F — The Resistant Reader**
*Was given this book, or picked it up under mild obligation — not fully bought in yet.*
- Needs to be won over, not assumed into agreement
- Will seize on any moment of inauthenticity to disengage
- Often represents a real reader segment the author hasn't fully considered
- Reading voice: "convince me", waiting for the book to justify its own existence
- What they notice: whether the author earns the reader's time, whether the premise holds up
- What makes them convert: a moment where the book says something that directly addresses
  their specific situation in a way no one else has

---

### Custom Persona Builder

If the author's target reader doesn't fit any of the above, build a custom persona:

> "Describe your reader in as much detail as you can — their job, their current situation, what
> they believe about this topic right now, what they're hoping this book will do for them."

Then construct a named persona with: background, reading voice, what they notice, and what
would make them stop reading.

---

## Mode 1 — Full Beta Read

Simulate 2–3 personas reading the full chapter. Present reactions as a **live reading log** —
thoughts, questions, and emotional responses triggered in real time as they move through the text.

### Reading Log Format

For each persona, produce a running log structured as follows:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
BETA READ — [Chapter Title]
PERSONA: [Name] — [One-line description]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[OPENING — first 200 words]
  💬 "[Their immediate reaction — a thought, feeling, or question]"
  📌 Note: [What landed well or what missed]

[SECTION 1 TITLE OR PASSAGE]
  💬 "[Reaction mid-section]"
  ❓ Question raised: "[What they're now wondering]"
  ⚡ Engagement: [Hooked / Following / Drifting / Skimming]

[SECTION 2 TITLE OR PASSAGE]
  💬 "[Reaction]"
  ❓ Question raised: "[...]"
  ⚡ Engagement: [...]
  ⚠️  Flag: [If a specific problem — confusion, disbelief, irritation — triggered here]

[... continue through the chapter ...]

[CLOSING — last 200 words]
  💬 "[Final reaction as they finish]"
  📌 Note: [Did the close deliver? What are they left with?]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
POST-READ DEBRIEF — [Persona Name]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

OVERALL EXPERIENCE:   [1 sentence — how did reading this feel overall?]

ENGAGEMENT CURVE:
  [Map the chapter in 4–6 beats, like a graph in words]
  → Opened strong / slow / immediately hooked
  → Built well through [section] / started to drag at [section]
  → [Key turning point in engagement]
  → Closed [strongly / weakly / promisingly]

MOST MEMORABLE MOMENT:
  "[The sentence, idea, or passage that stuck most — and why]"

BIGGEST CONFUSION:
  "[The moment they were most lost — exact passage if possible]"

TRUST LEVEL:          [Fully trusted / Mostly trusted / Earned over time / Questioned at X point]

WHAT THEY'LL TELL A FRIEND:
  "[How they'd describe this chapter to someone — in their own words, not the author's]"

WOULD THEY READ THE NEXT CHAPTER?   [Yes / Probably / Only if / No — and why]

TOP 3 FIXES FOR THIS PERSONA:
  1. [Most impactful change for this reader type]
  2. [Second priority]
  3. [Third priority]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### Cross-Persona Summary

After all personas have read, present a consolidated summary:

```
╔══════════════════════════════════════════════════════════════╗
║             BETA READ SUMMARY — [Chapter Title]             ║
╚══════════════════════════════════════════════════════════════╝

PERSONAS:        [A] [B] [C]

CHAPTER HEALTH:  [Overall score — Strong / Solid / Needs Work / Major Rework]

WHERE ALL PERSONAS AGREED:
  ✅ Strengths:   [What every reader responded to positively]
  ⚠️  Weaknesses:  [What every reader flagged as a problem]

WHERE PERSONAS DIVERGED:
  [Ideal Reader loved X, but Skeptic pushed back on Y...]
  → Implication: [What this tension means for the author's choices]

THE ONE THING TO FIX FIRST:
  [Single highest-impact change that would improve experience for the most readers]

THE ONE THING TO PROTECT:
  [The element that's working best — don't accidentally edit this out]

ENGAGEMENT LOW POINT:   [The exact section where readers were most at risk of drifting]
TRUST HIGH POINT:       [The exact moment readers most believed the author]

RECOMMENDED NEXT STEP:
  [ ] Fix confusion at [section] — send to editor-sharpener with this brief
  [ ] Strengthen evidence at [claim] — send to research-evidence-builder
  [ ] Rewrite opening — the hook isn't earning the read yet
  [ ] Chapter is ready — move to editor-sharpener for final polish
╚══════════════════════════════════════════════════════════════╝
```

---

## Mode 2 — Targeted Reader Test

When the author wants to test one specific element rather than the whole chapter.

### Targeted Test Types

#### `"Does the opening hook work?"`
Simulate 3 personas reading only the first 200–300 words.
- Report: first impression, whether they're hooked or indifferent, what question (if any) the
  opening created in their mind, would they continue reading
- Option: generate 2 alternative openings and simulate the same test on each

#### `"Will they follow this argument?"`
Simulate the Skeptic and the Newcomer reading a specific argument or logical chain.
- Map where each reader follows cleanly, where they need more, where they get lost
- Identify the weakest link in the logic chain

#### `"Does this example land?"`
Simulate 2 personas reading a specific case study or example.
- Report: did it prove the point? Did it feel real? Was it relatable? Was it too niche or too
  generic? What it made them think of
- Option: suggest a stronger example if this one isn't landing

#### `"Will they trust me here?"`
Simulate the Skeptic reading a bold or controversial claim.
- Report: their immediate reaction, what evidence they'd need to believe it, what makes it feel
  credible or not, whether it damages overall trust in the book if they don't accept it

#### `"Does the close earn it?"`
Simulate 2 personas reading the final 300 words of a chapter.
- Report: did it feel like a payoff or a summary? What emotional state do they close in? Would
  they turn the page immediately or put the book down? What's the last thought in their head?

#### `"Where will they skim?"`
Simulate the Busy Professional reading the full chapter.
- Mark every passage where this reader would likely skim or skip
- Explain why (too dense, too slow, no clear payoff signal)
- Recommend the minimum edits needed to earn those passages back

---

## Mode 3 — Confusion Mapper

A precision tool for identifying exactly where readers lose comprehension — and why.

This mode goes deeper than the full beta read on the specific question: *where does
understanding break down, and what type of breakdown is it?*

### Confusion Types

| Type | What it looks like | Common cause |
|---|---|---|
| **Logic Gap** | Reader can't see how A connects to B | Missing step in the argument |
| **Knowledge Gap** | Reader lacks context to understand the term or concept | Assumed knowledge |
| **Pace Gap** | Reader hasn't absorbed the previous idea before the next arrives | Too fast |
| **Credibility Gap** | Reader doesn't believe the claim and stops following | Weak evidence or overreach |
| **Relevance Gap** | Reader can't see why this matters to them | Missing "so what" |
| **Reference Gap** | Reader doesn't recognise the example or analogy | Too niche or obscure |

### Confusion Map Output

```
CONFUSION MAP — [Chapter Title / Section]
════════════════════════════════════════════════════════════

PERSONA: [Name]
COMPREHENSION LEVEL GOING IN: [What they know / don't know]

CONFUSION POINTS (in order of appearance):

📍 CONFUSION POINT 1
   Location:      [Section title or passage quote]
   Type:          [Logic Gap / Knowledge Gap / Pace Gap / etc.]
   What broke:    [Exactly what the reader can't follow and why]
   Severity:      [Minor stumble / Significant confusion / Reader lost]
   Fix:           [Precise edit: add a bridge sentence / define the term /
                  slow down with an example / cut and simplify]

📍 CONFUSION POINT 2
   [...]

📍 CONFUSION POINT 3
   [...]

COMPREHENSION SCORE:   [X / 10]
CLEAREST SECTION:      [Where the reader followed most easily — and why]
DENSEST SECTION:       [Where the most cognitive load is concentrated]
OVERALL DIAGNOSIS:     [Is confusion localised or systemic?]
PRIORITY FIX:          [Single most impactful edit to improve comprehension]
════════════════════════════════════════════════════════════
```

---

## Mode 4 — Manuscript-Level Read

For when the author has 3+ chapters complete and wants to understand the reader experience
across the full arc — not just within individual chapters.

### What this mode assesses

**Momentum across chapters**
Does the reader's engagement build, hold, or decay as they move through the book?
Flag: chapters that interrupt the flow, chapters that feel like the same chapter twice,
the point at which a real reader would most likely abandon the book.

**Trust arc**
How does the reader's trust in the author develop? Does it build consistently or are there
chapters that erode what earlier chapters earned?

**Promise tracking**
What does the opening chapter promise? Are those promises being kept chapter by chapter?
Flag: any promise made early that hasn't been fulfilled by the current draft.

**Reader transformation**
At what point does the reader's thinking start to shift? Is it happening at the right pace?
Flag: a book that transforms readers too slowly (they give up before it happens) or too
fast (the later chapters have nothing new to do).

**Fatigue points**
Where does the book feel long? Which chapter would a busy reader skip?

### Manuscript Read Output

```
╔══════════════════════════════════════════════════════════════╗
║           MANUSCRIPT BETA READ — [Book Title]               ║
║           Chapters reviewed: [list]                         ║
╚══════════════════════════════════════════════════════════════╝

PERSONA: [Name]

CHAPTER-BY-CHAPTER ENGAGEMENT:
  Ch 1: [Title]  ████████░░  [8/10] — [1-line note]
  Ch 2: [Title]  ███████░░░  [7/10] — [1-line note]
  Ch 3: [Title]  █████░░░░░  [5/10] — [1-line note — flag if dip]
  ...

MOMENTUM ARC:    [Building / Holding / Decaying / Uneven]
TRUST ARC:       [How trust develops chapter by chapter]
ABANDONMENT RISK:[The chapter where a real reader is most likely to stop — and why]

PROMISES MADE (Ch 1–2):
  ① "[Promise]" — [Kept / Partially kept / Not yet delivered — in which chapter?]
  ② "[Promise]" — [...]

READER TRANSFORMATION:
  Current pace:   [Too fast / Right / Too slow]
  Shift point:    [Where the reader's thinking first genuinely changes]
  Gap:            [If there's a section where nothing new is happening for the reader]

FATIGUE POINTS:
  ① [Chapter or section that feels long or redundant — and why]

TOP 5 MANUSCRIPT-LEVEL FIXES:
  1. [...]
  2. [...]
  3. [...]
  4. [...]
  5. [...]

WHAT'S WORKING ACROSS THE BOOK:
  [Genuine manuscript-level strengths to protect]
╚══════════════════════════════════════════════════════════════╝
```

---

## Reading Principles

These guide every simulation — the goal is honest, useful feedback, not reassurance.

**Read as the persona, not as an editor.** Don't flag craft problems (that's editor-sharpener's
job). Flag experience problems: confusion, disbelief, disengagement, feeling talked down to,
or feeling unexpectedly seen.

**Be specific about location.** Vague feedback ("this section is slow") is useless. Precise
feedback ("by the third paragraph of the 'Execution Gap' section, this reader has mentally
checked out because they've been told the same thing twice") is actionable.

**Protect what's working.** Every beta read must identify strengths — not as consolation, but
because the author needs to know what not to accidentally edit out.

**Distinguish persona-specific from universal.** Some problems will bother every reader. Others
will only matter to the Skeptic or only confuse the Newcomer. Flag which is which — the author
may decide to write for some personas more than others.

**Don't solve — diagnose.** This skill identifies what a reader experiences. The *fix* goes
back to chapter-builder (for structural rebuilds), editor-sharpener (for craft fixes), or
research-evidence-builder (for evidence gaps). This skill hands off with a clear brief.

---

## Integration with Other Skills

**← chapter-builder**: After a chapter draft is complete, before it goes to editor-sharpener,
run a beta read. The Craft Note from chapter-builder tells you what the drafter already flagged
as weak — test those exact sections first.

**← editor-sharpener**: After a polished chapter, run a beta read to catch experience problems
that editing didn't fix. A beautifully crafted sentence the reader doesn't believe is still a
problem.

**→ editor-sharpener**: When the beta read identifies confusion or disengagement, pass the
Confusion Map or engagement low point to editor-sharpener as a targeted fix brief:
*"Readers are drifting in the second section — run a Mode 3 Targeted Fix on the flow here."*

**→ research-evidence-builder**: When the Skeptic doesn't believe a claim, pass it to
research-evidence-builder: *"The Skeptic flagged this claim as unsupported — find evidence."*

**→ book-architect**: When the manuscript read shows promise gaps or arc problems, go back to
book-architect to restructure the chapter order or rewrite chapter purposes.

---

## Quick Commands

| Command | Mode | Action |
|---|---|---|
| `"Beta read this chapter"` | 1 | Full read with 2–3 personas + summary |
| `"Read this as my target reader"` | 1 | Single persona full read |
| `"Read this as a skeptic"` | 1 | Skeptic persona only |
| `"Does the opening hook work?"` | 2 | Hook test — 3 personas on first 300 words |
| `"Where will I lose the reader?"` | 2 | Skim test — Busy Professional persona |
| `"Will they follow this argument?"` | 2 | Logic chain test — Skeptic + Newcomer |
| `"Does this example land?"` | 2 | Example/case study test |
| `"Will they trust me here?"` | 2 | Credibility test on a bold claim |
| `"Map the confusion in this section"` | 3 | Full confusion map with fix briefs |
| `"Where does comprehension break down?"` | 3 | Confusion mapper — all types |
| `"Read across all my chapters"` | 4 | Manuscript-level engagement + arc read |
| `"Which chapter will readers abandon?"` | 4 | Abandonment risk assessment |
| `"Am I keeping my promises?"` | 4 | Promise tracking across manuscript |
