---
name: research-evidence-builder
description: >
  Research and evidence building skill for authors. Use this skill whenever an author needs
  supporting material for their book — data, case studies, statistics, counterarguments, real-world
  examples, or expert citations. Trigger for: "find evidence for this", "I need a case study for
  chapter N", "what data supports this claim?", "find me examples of X", "what are the
  counterarguments to this?", "I need a story for this section", "back this up with research",
  "what does the research say about X?", "give me supporting evidence", "find real-world examples",
  "I need statistics for this", "what's the opposing view?", "my chapter feels thin — it needs
  more substance", "strengthen the argument in this section", or any phrasing where the author
  has an idea or claim that needs evidence, examples, or depth behind it. Works at the book level
  (what evidence does the whole book need?) or chapter level (what does this specific claim need?).
  Integrates with chapter-builder Craft Notes that flag weak or unsupported sections.
---

# Research & Evidence Builder

A structured research skill that finds, evaluates, and packages supporting material — data,
case studies, examples, counterarguments, and expert citations — so authors can write with
authority and specificity.

This skill fills the gap that **chapter-builder** flags in its Craft Notes: *"this section
needs a real story"* or *"this claim needs evidence."* It turns those flags into usable material.

The workflow has **four modes**:
1. **Chapter Evidence Audit** — scan a chapter/section and identify every claim that needs backing
2. **Evidence Hunt** — research and surface supporting material for a specific claim or idea
3. **Case Study Builder** — develop a full illustrative case study from scratch or from raw notes
4. **Counterargument Armoury** — surface the strongest objections to the book's arguments + rebuttals

---

## Before Researching: Intake

When the author requests research, collect context before searching. Ask only what isn't
already clear from the conversation:

| Input | What to ask |
|---|---|
| **The claim or idea** | "What's the specific argument or point you need evidence for?" |
| **Chapter context** | "Which chapter is this for, and what's its purpose in the book?" |
| **Evidence type needed** | "Are you looking for data/statistics, a real-world case study, an expert quote, a counterargument, or all of the above?" |
| **Reader sophistication** | "Will your reader expect academic-style citations, or is a well-sourced business/narrative example enough?" |
| **What you already have** | "Do you have any existing evidence that isn't quite landing? Share it — I may be able to strengthen or replace it." |

If the author pastes a chapter section and says "this feels thin," go straight to
**Mode 1: Chapter Evidence Audit** without asking.

---

## Mode 1 — Chapter Evidence Audit

Scan a pasted chapter or section and identify every claim that is:
- **Unsupported** — asserted without evidence
- **Vaguely supported** — backed by a weak or generic reference
- **Potentially contested** — claims a skeptical reader might push back on
- **Story-thin** — conceptual points that would land better with a real example

### Audit Output Format

```
EVIDENCE AUDIT — [Chapter Title]
════════════════════════════════════════════════════════════

UNSUPPORTED CLAIMS (need evidence or a source):
  ① [Quote the exact claim] — Line/paragraph reference
     → Suggested evidence type: [statistic / study / case study / expert citation]
     → Why it needs backing: [why a reader would question this]

  ② [Quote the exact claim]
     → Suggested evidence type: [...]
     → Why it needs backing: [...]

VAGUE SUPPORT (existing evidence that could be stronger):
  ① [Quote the claim + its current support]
     → Problem: [e.g., "Unnamed 'studies show' — needs a real source"]
     → Fix: [what to replace it with]

STORY-THIN SECTIONS (ideas that need a real-world anchor):
  ① [Section title or paragraph summary]
     → The gap: [what's missing — an illustrative case, a before/after, a named example]
     → Story type that would work: [anecdote / case study / hypothetical / interview-style]

POTENTIALLY CONTESTED CLAIMS (anticipate the pushback):
  ① [Quote the claim]
     → Likely objection: [what a skeptic would say]
     → Suggested preemption: [how to address it in the text]

EVIDENCE STRENGTH SCORE:      [X / 10]
PRIORITY FIXES (do these first):
  1. [Most impactful gap to fill]
  2. [Second priority]
  3. [Third priority]
════════════════════════════════════════════════════════════
```

After presenting, ask:
> "Want me to go find the evidence for all of these, or start with the top priorities?"

---

## Mode 2 — Evidence Hunt

Research and surface the best available evidence for a specific claim or argument.

### Step 1 — Clarify the claim

Before searching, restate the claim precisely:
> "Just to make sure I'm searching for the right thing — the claim is: *[restate]*. Is that right?"

A sharply stated claim finds better evidence than a vague topic.

### Step 2 — Search strategy

Search across multiple evidence types simultaneously. For each claim, look for:

**A. Hard data & statistics**
- Specific numbers that support or quantify the claim
- Research studies (academic, institutional, or well-regarded industry research)
- Survey data from credible organisations
- Historical data showing trends

**B. Real-world case studies**
- Companies, individuals, or organisations that illustrate the point
- Before/after transformations that prove the mechanism
- Both success cases AND instructive failure cases (more credible)

**C. Expert citations**
- Researchers, authors, or practitioners who have made this argument
- Contrarian experts whose agreement would be surprising and therefore powerful
- Classic sources the reader might already know (adds credibility)

**D. Analogies & adjacent evidence**
- Evidence from a different field that illuminates the same principle
- Historical parallels — the same pattern in a different era
- Scientific or psychological principles that underpin the claim

### Step 3 — Evidence Package Output

Present findings in a structured, ready-to-use format:

```
EVIDENCE PACKAGE — "[The Claim]"
════════════════════════════════════════════════════════════

HEADLINE STATISTIC:
  Stat:     [The number/finding]
  Source:   [Organisation / Study / Year]
  Context:  [What makes this stat credible and relevant]
  Use it:   [Suggested sentence showing how to deploy it in prose]

SUPPORTING DATA POINTS:
  • [Stat 1] — [Source]
  • [Stat 2] — [Source]
  • [Stat 3] — [Source]

BEST CASE STUDY:
  Who:      [Company / person / organisation]
  What:     [What happened — the situation and result]
  Why it works: [Why this case proves the claim]
  Source:   [Where this comes from — book, article, report]
  ⚠ Watch for: [Any nuance or context needed to use it fairly]

ADDITIONAL EXAMPLES:
  • [Example 1] — [brief description + source]
  • [Example 2] — [brief description + source]

EXPERT CITATION:
  Who:      [Name + credentials]
  Said:     [The argument they make — paraphrased]
  Source:   [Book / paper / talk title + year]
  Use it:   [How to reference this in the chapter]

HISTORICAL / ADJACENT PARALLEL:
  [A pattern from history or a different field that mirrors the claim]
  Why it works: [Why this parallel is illuminating, not just decorative]

COUNTEREVIDENCE TO ACKNOWLEDGE:
  [Evidence that appears to contradict the claim]
  How to handle: [How the author can address this honestly and strengthen
                  their argument by engaging with it, not ignoring it]

EVIDENCE STRENGTH ASSESSMENT:
  Confidence level:   [High / Medium / Uncertain — and why]
  Strongest piece:    [The one piece of evidence that does the most work]
  Weakest link:       [What a skeptic would challenge first]
  Recommendation:     [How to deploy this evidence in the chapter]
════════════════════════════════════════════════════════════
```

### Evidence Credibility Tiers

When evaluating sources, use this hierarchy (always prefer higher tiers):

| Tier | Source Type | Use |
|---|---|---|
| 1 | Peer-reviewed research, government data, landmark studies | Highest credibility — cite directly |
| 2 | Well-regarded books by recognised experts, major institutional reports | Strong — cite with author name |
| 3 | Quality journalism (FT, Economist, HBR, NYT), industry research | Good for business books — cite source |
| 4 | TED talks, conference papers, well-cited blog posts | Use carefully — verify the underlying claim |
| 5 | Anecdotal, uncited, or single-source claims | Flag for the author — needs corroboration |

Always tell the author the tier of the evidence provided, and flag Tier 4–5 material clearly.

---

## Mode 3 — Case Study Builder

When a chapter needs a real-world illustration but no obvious example exists — or when the
author has a rough story they want to develop into a proper case study.

### Sub-mode A: Find a Case Study

The author describes the principle or outcome they need illustrated. Research and surface
2–3 candidate case studies, then build out the best one.

**Input needed:**
- What principle or mechanism needs illustrating?
- What outcome should the case study demonstrate? (transformation, failure, contrast, etc.)
- Any constraints? (industry, geography, company size, time period)

**Output:** A fully developed case study in narrative form, ready to drop into the chapter.

### Sub-mode B: Develop the Author's Raw Notes

The author has a story — a client, a personal experience, something they read — but it's
rough. They paste their notes. Build it into a case study.

**Input needed:** The author's raw notes (even bullet points or a rough paragraph)

**Development process:**
1. Identify the narrative structure: **Setup → Tension → Turning Point → Resolution**
2. Extract the key details that prove the chapter's point
3. Identify what's missing (dates, specific numbers, the precise outcome)
4. Flag gaps: *"To make this case study land, you'll need to provide: [X, Y, Z]"*
5. Write the case study in draft form, with [FILL IN] placeholders where real details are needed

### Case Study Output Format

Every case study produced follows this structure:

```
CASE STUDY: [Title — give it a name]
─────────────────────────────────────────────────────────────
THE SETUP:
[1–2 paragraphs. Who is this person/company? What was their
situation? What was at stake? Make the reader care before
anything happens.]

THE PROBLEM / TENSION:
[What went wrong, what wasn't working, what challenge
they faced. This is the "before" state.]

THE TURNING POINT:
[The decision, discovery, or shift that changed things.
This is where the chapter's key idea shows up in action.]

THE RESULT:
[Specific, concrete outcomes. Numbers if available.
The "after" state — what changed and by how much.]

THE LESSON:
[1–2 sentences: what this case proves about the chapter's
argument. This is the bridge back to the book's ideas.]

SOURCE / ATTRIBUTION: [Where this comes from]
WORD COUNT: ~[X] words
GAPS TO FILL: [What the author needs to verify or add]
─────────────────────────────────────────────────────────────
```

---

## Mode 4 — Counterargument Armoury

The strongest books don't avoid objections — they anticipate and disarm them. This mode
surfaces the best counterarguments to the book's central claims and builds rebuttals.

### When to use this mode

- Before writing a chapter that makes a bold or controversial claim
- When the author's argument feels too one-sided or easy
- When the editor-sharpener flags that a section is over-certain without addressing obvious objections
- Before the book is finalised — as a "stress test" of the whole argument

### Counterargument Hunt Process

For each major claim or thesis, surface:

**Level 1 — The Obvious Objection**
The first thing a skeptical reader thinks. Usually addressed by "yes, but..." or "this only works if..."

**Level 2 — The Data Objection**
Evidence or research that appears to contradict the claim. This is the most important one to
address — a reader who has encountered this data will stop trusting the author if it's ignored.

**Level 3 — The Edge Case**
Situations where the claim breaks down or doesn't apply. Naming these actually *strengthens*
the argument by showing the author understands the limits of their ideas.

**Level 4 — The Expert Dissenter**
A credible person in the field who holds the opposite view. Engaging with their argument
(and explaining where you disagree) is a mark of intellectual seriousness.

### Counterargument Output Format

```
COUNTERARGUMENT ARMOURY — "[Claim or Chapter]"
════════════════════════════════════════════════════════════

CLAIM BEING STRESS-TESTED:
"[The exact claim]"

THE OBVIOUS OBJECTION:
  What they'll think:   [The natural pushback]
  Strength:             [How seriously to take it — Low / Medium / High]
  Rebuttal:             [How the author addresses this without dismissing it]
  Where to deploy:      [Preemptively in the text, or save for a FAQ/appendix]

THE DATA OBJECTION:
  The contradicting evidence: [What studies or data seem to argue against this]
  Source:               [Where it comes from]
  Strength:             [How credible this counterevidence is]
  Rebuttal:             [Acknowledge it, then explain why your claim still holds:
                         different context? different population? confounding factor?]

THE EDGE CASE:
  Where the claim breaks down: [Specific situation where it doesn't apply]
  How to handle:        [Name it explicitly in the chapter — "This doesn't apply when..."]
  Why naming it helps:  [It builds trust — shows you're not overselling]

THE EXPERT DISSENTER:
  Who:                  [Name + credentials of someone who disagrees]
  Their argument:       [What they say and why]
  Your rebuttal:        [Where you agree with them + where you diverge + why]
  How to reference:     [Suggested framing in the text]

STEELMANNED OPPOSITION:
  [The single strongest possible version of the opposing argument —
   the one that would most challenge the author's thesis. If you can
   rebut this, you can rebut anything.]
  Rebuttal:             [The author's best response]

OVERALL STRESS-TEST RESULT:
  Argument robustness:  [Strong / Solid / Needs work]
  Most dangerous gap:   [The objection that most needs addressing in the text]
  Recommended action:   [Specific addition to the chapter to preempt the biggest risk]
════════════════════════════════════════════════════════════
```

---

## Evidence Integration Guide

Once evidence is found, it needs to be *placed* in the chapter correctly. Follow these
principles when advising the author on how to use the evidence:

### Placement Rules

**Statistics** — place after the claim they support, not before. The claim first creates
the need; the stat satisfies it. *Wrong: "73% of managers avoid conflict. This is a problem."*
→ *Right: "Most managers actively avoid the conversations that would solve their problems.
Research backs this up: in a 2022 survey of 1,400 leaders, 73% admitted..."*

**Case studies** — open a section or follow a logical argument. Use them to *prove*, not to
*introduce*. The reader should already understand the principle when the case study arrives,
so it confirms rather than teaches.

**Expert citations** — use sparingly. One strong citation beats three weak ones. Don't cite
an expert just to show you've done research — cite them when their phrasing or authority
adds something the author's own words can't.

**Historical parallels** — use mid-chapter to add depth and perspective. They work best as
a "this isn't new" moment that contextualises the author's idea in a longer pattern.

**Counterarguments** — address early in a section that makes a bold claim. Don't save them
for the end — it looks defensive. Instead, raise the objection yourself and answer it before
the reader can use it against you.

### The Evidence Sandwich

For any claim needing support, use this structure in prose:

```
CLAIM     → State the argument clearly
EVIDENCE  → Introduce the supporting data/case/citation
BRIDGE    → Explain what the evidence proves (don't leave it implicit)
IMPLICATION → What this means for the reader's situation
```

Example:
- *Claim:* "Most organisations fix the wrong problem."
- *Evidence:* "A McKinsey study of 1,800 transformation projects found that 70% failed — not
  from poor execution, but from misdiagnosis of the root cause."
- *Bridge:* "They weren't solving the wrong problem badly. They were solving the wrong problem
  very well."
- *Implication:* "Before you invest in fixing what's in front of you, the question worth asking
  is whether you've correctly identified what's actually broken."

---

## Integration with Other Skills

**→ chapter-builder Craft Note**: When chapter-builder flags *"this section needs a real story"*
or *"this claim needs data"*, paste that Craft Note here. The skill uses it as the research brief.

**→ editor-sharpener Lens 5 (Specificity)**: When editor-sharpener scores a chapter low on
specificity and flags vague assertions, those flagged passages become the research brief for
this skill.

**→ book-architect**: At the architecture stage, run Mode 1 (Evidence Audit) on the full chapter
plan — not the prose, but the key ideas. Identify where the book's core arguments are
evidence-light *before* writing begins.

**→ voice-calibrator**: Evidence should match the author's established evidence style. If the
voice fingerprint shows the author is "story-led not data-led", prioritise case studies over
statistics. If they're "data-led", lead with research and use stories as illustration.

---

## Quick Commands

| Command | Mode | Action |
|---|---|---|
| `"Audit this chapter for evidence gaps"` | 1 | Full evidence audit with priority fixes |
| `"Find evidence for this claim"` | 2 | Full evidence package for a specific claim |
| `"Find me a case study for [principle]"` | 3A | Surface 2–3 candidates + build the best one |
| `"Here are my rough notes — build this into a case study"` | 3B | Develop author's raw story |
| `"What are the counterarguments to this?"` | 4 | Full counterargument armoury |
| `"Stress-test my main thesis"` | 4 | Run the steelman opposition on the book's core argument |
| `"What data exists on [topic]?"` | 2 | Data and statistics hunt only |
| `"Find a failure case study"` | 3A | Specifically look for instructive failure examples |
| `"What do critics say about this idea?"` | 4 | Expert dissenter research only |
| `"How do I use this evidence in the chapter?"` | — | Evidence placement + integration advice |
