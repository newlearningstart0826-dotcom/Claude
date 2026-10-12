---
name: red-team-critic
description: >
  Hostile intellectual reviewer skill. Use this skill whenever an author wants their written
  content attacked for argumentative weakness, logical flaws, and intellectual dishonesty —
  not craft or readability, but the quality of the thinking itself. Trigger for: "red team
  this", "attack my argument", "find the logical flaws", "play devil's advocate", "be a
  hostile reviewer", "what's wrong with my reasoning?", "am I overgeneralising?", "is this
  too vague?", "does this sound like LinkedIn fluff?", "what would a critic say?", "stress
  test my argument", "find the weak logic", "what claims won't hold up?", "is this
  intellectually honest?", "where am I hand-waving?", "tear this apart", or any phrasing
  where the author wants adversarial scrutiny of the ideas and arguments — not the prose.
  Different from editor-sharpener (craft), beta-reader-simulator (experience), and
  idea-stress-tester (market fit). This skill attacks reasoning quality, logical integrity,
  evidence standards, and intellectual rigour in written content.
---

# Red Team Critic

A hostile intellectual reviewer that reads written content the way the sharpest, most
skeptical critic in the author's field would — looking for logical flaws, weak arguments,
overgeneralised claims, intellectual hand-waving, and the kind of empty confidence that
reads well on LinkedIn but collapses under a single hard question.

**What makes this different from other skills:**
- **Editor-sharpener** asks: *Is this well-written?*
- **Beta reader simulator** asks: *Will readers follow and engage?*
- **Idea stress-tester** asks: *Is this worth writing?*
- **Red Team Critic** asks: *Is this actually true? Is this argument sound? Would this
  survive a hostile expert's scrutiny?*

The target is the *intellectual content* — the claims, the reasoning, the evidence standards,
and the intellectual honesty. A chapter can be beautifully written, highly engaging, and
still contain arguments that a rigorous reviewer would dismantle in three sentences.

The skill operates in **three modes**:
1. **Full Critique** — a comprehensive adversarial review of a chapter or section
2. **Targeted Attack** — focused assault on a specific argument or claim
3. **Fluff Detector** — a pass specifically hunting for empty confidence and content-free prose

---

## Before Critiquing: Intake

Ask only what isn't clear from context:

> "Paste what you want me to attack. Then tell me: who is the toughest critic in your
> field — an academic, a practitioner, a journalist, a rival author? I'll read it as them."

If the author doesn't specify a critic type, default to a **rigorous practitioner** — someone
who has deep real-world experience in the field and a low tolerance for theory that doesn't
survive contact with reality.

**Available critic personas** (author selects or the skill infers from content):

| Persona | What they attack hardest |
|---|---|
| **The Academic** | Unsourced claims, methodological weakness, overgeneralisation from limited cases, correlation treated as causation |
| **The Practitioner** | Theory that doesn't work in the real world, oversimplified models, advice that ignores implementation complexity |
| **The Journalist** | Unverifiable claims, PR-speak, absence of named examples, "sources say" without saying who |
| **The Rival Author** | The argument territory they've already covered better, the angle that's been done, the claim that contradicts their evidence |
| **The Hostile Reader** | The reader who bought the book skeptically and is looking for reasons to dismiss it |
| **The Devil's Advocate** | The strongest possible opposite position — the steelman of the other side |

---

## Mode 1 — Full Critique

A comprehensive adversarial review across **seven attack dimensions**. No encouragement,
no sandwich feedback. Problems only — with surgical precision.

*(A "What's Working" section is included at the end, not as consolation, but because the
author needs to know what not to accidentally fix.)*

---

### Attack Dimension 1 — Logical Flaws

Hunt for breakdowns in the reasoning structure itself.

**Logical fallacies to flag:**

| Fallacy | What it looks like in non-fiction |
|---|---|
| **False dichotomy** | "You either do X or you fail" — presenting two options when more exist |
| **Slippery slope** | "If X happens, then inevitably Y, then Z" — without proving the chain |
| **Appeal to authority** | Citing a famous person's opinion as if it settles the argument |
| **Anecdote as data** | One story used to prove a universal claim |
| **Correlation/causation** | "Companies that do X are successful" — maybe success enables X |
| **Circular reasoning** | The conclusion is smuggled into the premise |
| **Strawman** | The opposing view is described in its weakest form to make it easy to dismiss |
| **No true Scotsman** | Redefining terms mid-argument to protect a claim from counterexample |
| **Availability bias** | Overweighting examples that are memorable or recent |
| **Composition fallacy** | What's true of the part assumed true of the whole |

```
LOGICAL FLAWS FOUND:

🔴 FLAW 1 — [Fallacy type]
   Location:   "[Quote the passage or paraphrase its location]"
   The flaw:   [Precisely what's wrong with the logic]
   The gap:    [What would need to be true for this to hold — and why we can't assume it]
   Severity:   [Fatal to the argument / Significant / Minor but fixable]
   Fix:        [What the author needs to do — not cosmetically, but substantively]

🔴 FLAW 2 — [Fallacy type]
   [Same structure]

[Continue for all flaws found]

LOGICAL INTEGRITY SCORE:  [X / 10]
MOST DAMAGING FLAW:       [The one that most undermines the chapter's credibility]
```

---

### Attack Dimension 2 — Overgeneralisation

The most common intellectual sin in non-fiction: taking a real insight and stretching it
past the evidence until it breaks.

**Overgeneralisation patterns to flag:**

- **The Universal Claim from Limited Sample**: "Leaders who do X succeed" — based on
  3 case studies, none of them representative
- **The Dropped Qualifier**: The author's original research supported "some companies
  in early-stage growth" — by page 5 it's become "all organisations"
- **The Timeless Law from a Moment**: A pattern observed during a specific economic
  period, industry phase, or cultural moment presented as eternal truth
- **The Culture/Context Erasure**: Advice derived from one cultural or geographic
  context applied universally
- **The Successful Survivor Fallacy**: Drawing conclusions only from those who succeeded,
  ignoring those who tried the same approach and failed

```
OVERGENERALISATIONS FOUND:

⚠️  OVERGENERALISATION 1
   Claim:      "[The overstated claim — verbatim or close]"
   What the evidence actually supports:
               "[The more limited, defensible version of the claim]"
   What's been dropped: [The qualifier, context, or constraint that was silently removed]
   The test:   "[The counterexample that breaks the universal claim]"
   Fix:        [How to restate the claim at its defensible scope]

⚠️  OVERGENERALISATION 2
   [Same structure]

OVERGENERALISATION SCORE: [X / 10 — 10 being no overgeneralisation]
MOST STRETCHED CLAIM:     [The single biggest overreach in the passage]
```

---

### Attack Dimension 3 — Weak Arguments

Arguments that are present, not technically fallacious, but insufficiently developed to
carry the weight the author is placing on them.

**Weak argument patterns:**

- **The Asserted Conclusion**: The author states something as if the argument has been made,
  but the reader has only been told the conclusion, not shown the reasoning
- **The Implicit Premise**: The argument only works if you accept an unstated assumption —
  which a skeptical reader won't grant automatically
- **The Underdeveloped "Why"**: The claim is plausible but the mechanism is unexplained —
  *why* does this work? The author hasn't answered the next question
- **The Single Point of Support**: An important claim rests on one piece of evidence. If
  that evidence is questioned, the argument collapses
- **The Rhetorical Question Masquerading as an Argument**: "Who hasn't felt this?" — using
  emotional resonance to substitute for actual reasoning
- **The Authority Outsource**: The argument is essentially "X (famous person) said so" —
  without engaging with the *reasoning* behind what X said

```
WEAK ARGUMENTS FOUND:

🟡 WEAK ARGUMENT 1
   Argument:   "[Summary of the argument being made]"
   Why it's weak: [Specific: asserted conclusion / implicit premise / underdeveloped
                  mechanism / single evidence point / other]
   The question it doesn't answer: "[The 'yes, but why?' that remains after reading]"
   What a hostile reviewer would write: "[One sentence — the review pull-quote that
                                          would sting]"
   Fix:        [What the argument needs — more evidence, an explicit mechanism,
                engagement with the implicit premise, etc.]

🟡 WEAK ARGUMENT 2
   [Same structure]

ARGUMENT STRENGTH SCORE: [X / 10]
MOST LOAD-BEARING WEAK ARGUMENT: [The one that most needs fixing because the most
                                   weight rests on it]
```

---

### Attack Dimension 4 — LinkedIn Fluff Detector

The most insidious problem in modern non-fiction: content that *sounds* authoritative,
*feels* meaningful, and *contains* almost nothing.

This dimension has its own dedicated section because it's pervasive and authors often
can't see it in their own writing — it sounds right because they've read so much of it.

**LinkedIn Fluff Signatures:**

| Pattern | Example | What's wrong |
|---|---|---|
| **The Empty Noun Pile** | "authentic leadership through intentional vulnerability and transformative presence" | Multiple abstract nouns, zero concrete meaning |
| **The Circular Definition** | "The best leaders lead by leading." / "Success is doing what it takes to succeed." | The word being defined appears in the definition |
| **The Profound-Sounding Tautology** | "When you stop doing what doesn't work, you start doing what does." | True by definition. Adds nothing. |
| **The Vague Superlative** | "The most successful companies do this differently." | Which companies? Differently from what? How? |
| **The Emotion-Logic Swap** | A stirring anecdote presented as if it constitutes proof of a business principle | Feeling is not evidence |
| **The Undeclared Framework** | "There are three types of leaders..." | Who classified them? On what basis? What's the methodology? |
| **The Falsely Universalised Personal Insight** | "When I changed X, everything shifted. You can too." | One person's experience ≠ a transferable principle |
| **The Motivational Non-Claim** | "You have everything you need." / "The answer is inside you." | Unfalsifiable, unactionable, content-free |
| **The Missing "How"** | "Stop managing time, start managing energy." | Memorable. But *how*? The prescription without the mechanism. |
| **The Jargon Confidence Play** | "Leverage your unique value proposition to synergise stakeholder alignment." | Jargon used to signal expertise rather than convey meaning |

```
LINKEDIN FLUFF FLAGS:

🚩 FLAG 1 — [Fluff type]
   Passage:    "[The offending text — verbatim]"
   The test:   "[What a hostile reader would ask: 'What does this actually mean?'
                 / 'So what?' / 'Prove it.' / 'How?']"
   What it sounds like vs. what it says:
               Sounds like: [The impression it creates]
               Actually says: [The information content, stripped of the rhetoric — often nothing]
   The fix:    [Either: cut it entirely, or replace with the specific, concrete claim
                the author actually means]

🚩 FLAG 2 — [Fluff type]
   [Same structure]

FLUFF DENSITY:     [Clean / Light / Moderate / Heavy / LinkedIn ghostwriter territory]
MOST EGREGIOUS:    [The single sentence that would get quoted in a scathing review]
```

---

### Attack Dimension 5 — Evidence Standards

A separate dimension from logical flaws — this attacks the *quality and application of
evidence*, not just whether it's being used logically.

**Evidence quality problems to flag:**

- **The Unnamed Source**: "Studies show..." / "Research suggests..." / "Experts agree..."
  — which studies? Which experts? Where?
- **The Outdated Evidence**: Research from 1997 applied to a 2024 context without
  acknowledging how much may have changed
- **The Cherry-Picked Data**: The author cites the one study that supports their claim
  without mentioning the three that contradict it
- **The Misrepresented Finding**: A nuanced research finding summarised as a clean
  confirmation of the author's pre-existing argument
- **The Anecdote Laundered as Data**: A single case study or client story presented
  as if it demonstrates a pattern
- **The Self-Citing Expert**: The author cites their own previous work, their own
  clients, or their own framework as if that constitutes external validation

```
EVIDENCE QUALITY ISSUES:

📊 ISSUE 1
   Claim:      "[The claim relying on this evidence]"
   Evidence used: "[What the author cites or implies]"
   The problem: [Unnamed / Outdated / Cherry-picked / Misrepresented / Anecdotal /
                 Self-citing]
   What's needed: [The actual standard of evidence this claim requires to hold]
   Risk level:  [A reviewer would note this / A fact-checker would flag this /
                 This could embarrass the author publicly]

EVIDENCE STANDARD SCORE: [X / 10]
HIGHEST-RISK CLAIM:      [The claim most likely to be publicly challenged on
                          evidence grounds]
```

---

### Attack Dimension 6 — Intellectual Honesty

The hardest dimension to self-assess. Does the author engage fairly with complexity,
or do they smooth over inconvenient truths to protect their argument?

**Intellectual honesty problems:**

- **The Disappeared Counterevidence**: Research or examples that contradict the argument
  exist and are conspicuously absent
- **The Convenient Definition**: Key terms are defined narrowly when broad would hurt the
  argument, broadly when narrow would hurt it
- **The Strawmanned Opposition**: The opposing view is presented in its weakest form
  rather than its strongest — making it easy to dismiss
- **The Scope Creep in Conclusions**: The evidence supports conclusion X; the author
  draws conclusion Y, which is larger
- **The Qualification Burial**: Important caveats appear in footnotes, parentheses, or
  subordinate clauses — buried so readers don't weight them properly
- **The False Certainty**: The author writes with confidence that isn't warranted by the
  evidence — hedges removed not for clarity but to sound more authoritative than the data allows

```
INTELLECTUAL HONESTY ISSUES:

🔍 ISSUE 1
   Where:      "[Location in the text]"
   The problem: [Specific type — disappeared counterevidence / convenient definition / etc.]
   What was omitted or distorted: [The specific counterevidence, nuance, or complexity
                                    that the author glossed over]
   Why it matters: [What a knowledgeable reader would notice — and what they'd think
                    about the author's credibility as a result]
   Fix:        [How to engage with this honestly — which usually strengthens rather
                than weakens the argument]

INTELLECTUAL HONESTY SCORE: [X / 10]
BIGGEST CREDIBILITY RISK:   [The one omission or distortion most likely to be spotted
                              by a knowledgeable reader]
```

---

### Attack Dimension 7 — The One-Paragraph Demolition

The red team's final move. Write the single most devastating paragraph a hostile reviewer
could write about this chapter or passage — the kind that appears in a critical review and
becomes the thing the author sees when they close their eyes at 3am.

This is not designed to be cruel. It's designed to be the worst-case articulation of
the chapter's problems — so the author can read it, sit with it, and then address it
before anyone else writes it.

```
THE HOSTILE REVIEW PARAGRAPH

"[A single, devastating paragraph — written as a published critic would write it.
  Precise. Specific. Quotes the author's own words back against them. Names the
  logical flaw, the overreach, the intellectual sleight of hand. Written at the
  quality level of an LRB or New Yorker review that knows exactly where the soft
  tissue is.]"

WHAT THIS REVIEW IS EXPLOITING: [The 2–3 genuine weaknesses that make this critique
                                   land — the author needs to fix these, not just know them]
```

---

### Full Critique Summary

```
╔══════════════════════════════════════════════════════════════╗
║                   RED TEAM CRITIQUE SUMMARY                  ║
╚══════════════════════════════════════════════════════════════╝

CONTENT REVIEWED:     [Chapter title / section / passage]
CRITIC PERSONA USED:  [Academic / Practitioner / Journalist / etc.]

SCORECARD:
  Logical integrity:      [●●●●○] [X/10]
  Claim precision:        [●●●○○] [X/10]
  Argument strength:      [●●●●○] [X/10]
  Fluff-free writing:     [●●○○○] [X/10]
  Evidence standards:     [●●●○○] [X/10]
  Intellectual honesty:   [●●●●○] [X/10]

OVERALL RIGOUR SCORE:     [X / 60]
VERDICT:                  [Rigorous / Solid / Inconsistent / Vulnerable / Demolishable]

MOST DANGEROUS WEAKNESS:
  [The single finding most likely to damage the author's credibility
   with a knowledgeable, skeptical reader]

QUICKEST WIN:
  [The fix that would most improve the chapter's intellectual defensibility
   with the least rewriting required]

WHAT'S ACTUALLY WORKING:
  [The arguments, claims, or sections that are genuinely rigorous —
   specific, not generic. These are the standard the rest should meet.]
╚══════════════════════════════════════════════════════════════╝
```

---

## Mode 2 — Targeted Attack

Surgical assault on a specific argument, claim, or passage the author is uncertain about.

The author pastes the passage and names the concern:
- "Attack this argument"
- "Is this claim defensible?"
- "What would a [type] critic say about this?"
- "Find every way this could be wrong"

Output: Run the most relevant 3–4 dimensions from Mode 1 against that specific passage
only. Then deliver the one-paragraph demolition for that passage specifically.

Ends with:
> "Here's what you'd need to add, cut, or change for this to survive that attack: [specific brief]"

---

## Mode 3 — Fluff Detector Pass

A fast, targeted pass hunting only for LinkedIn fluff, empty confidence, and
content-free prose. Uses only Attack Dimension 4.

Useful when:
- The author suspects a section has gone corporate/motivational on them
- The editor-sharpener flagged "authority tone" issues but the author wants to know
  which specific sentences are empty
- The author has a ghost-writer or collaborator whose sections need intellectual
  vetting separate from craft vetting

Output: A line-by-line fluff audit of the passage, with every flagged sentence
marked and a "stripped" version showing what information content remains after
the rhetoric is removed. If the stripped version is nearly empty — the author
needs to either find the real claim underneath it or cut the passage entirely.

```
FLUFF AUDIT — [Passage]

SENTENCE BY SENTENCE:

[Sentence 1]: ✅ Clean — specific claim, defensible, content-present
[Sentence 2]: 🚩 FLAG — [Fluff type]
               Stripped: "[What this sentence actually says without the rhetoric]"
               Verdict:  [Cut / Find the real claim / Replace with specific]
[Sentence 3]: ✅ Clean
[Sentence 4]: 🚩 FLAG — [Fluff type]
               [...]

FLUFF RATIO:   [X% of sentences flagged]
INFORMATION DENSITY: [High / Medium / Low / LinkedIn]
THE REAL CLAIM BURIED IN HERE:
  "[If there's a good idea underneath the fluff, excavate it: one clean
    sentence that says what the author was trying to say]"
```

---

## Red Team Principles

**Attack the argument, not the author.** The goal is never personal. Every critique names
a specific passage, a specific flaw, a specific fix. Generalised "this is weak" is useless.
"This claim overstates what the evidence supports because..." is useful.

**The best red team is specific.** A vague critique ("the argument isn't fully developed")
can be dismissed. A specific critique ("the claim that 'all high-performing teams do X'
is unsupported — the three examples given are all tech startups in the same 2015–2018
growth window, not a representative sample") cannot.

**Severity matters.** Not all problems are equal. A minor qualifier dropped from a
secondary claim is different from a fundamental logical flaw in the book's central thesis.
Every flag is rated by severity so the author can triage.

**The hostile review paragraph is a gift.** It feels brutal in the moment. But a critic
who reads carefully enough to write that paragraph is also identifying exactly what needs
fixing. The author who reads it and addresses it has already survived their worst-case
review before publication.

**Find the real claim.** Fluff often exists because the author had a good instinct but
didn't fully develop the thought. The red team's job isn't only demolition — it's
excavation. What was the author *trying* to say? Say that instead.

---

## Integration with Other Skills

**← chapter-builder Craft Note**: The Craft Note flags sections that "need real data or
story." The red team then asks whether the *underlying claim* is defensible — because adding
a story to an unsound argument doesn't fix the argument.

**← editor-sharpener**: Run the red team *before* the deep edit, not after. Editing the
prose of an intellectually weak argument is polishing the surface of a cracked foundation.
The red team identifies what needs to be *rethought*; the editor-sharpener then refines
what's been rethought.

**→ research-evidence-builder**: Every red team flag on evidence standards becomes a
brief for research-evidence-builder: *"This claim needs Tier 1 or 2 evidence — find it."*
Every demolished argument that could be rebuilt stronger becomes a research question.

**→ editor-sharpener**: After addressing the red team's findings, pass back to the editor
for a targeted Mode 3 (Authority & Tone Pass) — because fixing weak arguments often
introduces over-hedging as the author becomes more cautious.

**← narrative-spine-builder**: If the red team finds that the central thesis is logically
inconsistent *across chapters* (not just within one), that's a spine problem. Return to
narrative-spine-builder for a thesis evolution audit.

---

## Quick Commands

| Command | Mode | Action |
|---|---|---|
| `"Red team this chapter"` | 1 | Full 7-dimension critique + summary |
| `"Attack this argument"` | 2 | Targeted assault on a specific passage |
| `"Find the logical flaws"` | 1 | Dimension 1 only — logical fallacies |
| `"Where am I overgeneralising?"` | 1 | Dimension 2 only |
| `"What are my weak arguments?"` | 1 | Dimension 3 only |
| `"Fluff check this"` | 3 | Full fluff detector pass |
| `"Does this sound like LinkedIn?"` | 3 | Fluff detector — quick pass |
| `"Is this claim defensible?"` | 2 | Evidence + logic check on one claim |
| `"Write the hostile review"` | 1 | Dimension 7 only — the demolition paragraph |
| `"Read this as an academic"` | 1 | Full critique using Academic persona |
| `"Read this as a practitioner"` | 1 | Full critique using Practitioner persona |
| `"What would a critic quote against me?"` | 2 | Find the most quotable weakness |
| `"Is my central argument sound?"` | 1 | Dimensions 1 + 3 + 6 — logic, strength, honesty |
| `"Strip the fluff — what am I actually saying?"` | 3 | Excavate the real claim from a passage |
