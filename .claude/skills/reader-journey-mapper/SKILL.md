---
name: reader-journey-mapper
description: >
  Reader engagement mapping skill for authors. Use this skill whenever an author wants to
  visualise where readers get hooked, where they disengage, where they experience
  transformation, and where they risk abandoning the book. Trigger for: "map the reader
  journey", "where will readers get bored?", "plot the engagement curve", "where are the
  drop-off risks?", "engagement map", "where is the transformation moment?", "where will
  readers lose interest?", "re-engagement suggestions", "chapter-by-chapter engagement",
  "where are the dead zones?", "reader attention map", "where does momentum drop?", or any
  phrasing where the author wants a diagnostic view of reader engagement across the full
  book. Different from beta-reader-simulator (persona reactions) and narrative-spine-builder
  (intended arc design). Diagnoses what current content will produce in reader engagement —
  a structural heat map of hook zones, drop-off risks, transformation moments, and
  re-engagement prescriptions, chapter by chapter.
---

# Reader Journey Mapper

A diagnostic instrument that maps the reader's engagement curve across the entire book —
identifying precisely where readers hook, where momentum builds, where attention drifts,
where transformation lands, and where drop-off risk is highest.

**What makes this different from similar skills:**
- **Narrative spine builder** designs the *intended* emotional arc — what the author
  wants readers to feel
- **Beta reader simulator** simulates *persona reactions* — what specific reader types
  say and feel while reading
- **Reader Journey Mapper** produces a *predictive engagement heat map* — a structural
  analysis of what the current content will actually generate in reader engagement,
  independent of persona. It identifies the mechanisms that cause engagement to rise or
  fall, and prescribes specific interventions at every drop-off point.

Think of it as the author's equivalent of an analytics dashboard — not "how did users
feel?" but "where did they click away, and why, and what do we change?"

The skill produces **five outputs**:
1. **Engagement Curve** — chapter-by-chapter engagement scored and plotted
2. **Hook Zone Analysis** — where and how the book captures the reader
3. **Drop-Off Risk Register** — every disengagement threat, ranked by severity
4. **Transformation Moment Map** — where insight and change actually land
5. **Re-Engagement Prescription** — specific interventions for every risk zone

---

## Intake

Collect what's needed. This skill works from chapter summaries or full manuscript —
the more content provided, the more precise the map.

**Minimum viable input:** Chapter titles + 2–3 sentence summaries of each, plus the
book's core premise and target reader.

**Ideal input:** Chapter titles + key ideas + openings and closings of each chapter
(the most engagement-critical passages), plus reader profile and book positioning.

Ask only what's missing from context:

| Input | What to ask |
|---|---|
| **Chapter inventory** | "Give me your chapters — title and a brief description of what each one does." |
| **Target reader** | "Who is this reader? What are they hoping to get from this book?" |
| **Reader's entry state** | "What does your reader believe, feel, or know when they open page one?" |
| **Book's core promise** | "What does the book promise to deliver — explicitly or implicitly — in the opening pages?" |
| **Known weak spots** | "Are there any chapters you already suspect might lose readers?" |

If coming from **book-architect** or **narrative-spine-builder**, extract the chapter
inventory and reader profile from context without re-asking.

Confirm before mapping:
> "I have [N] chapters to map. I'll produce the full engagement curve with hook zones,
> drop-off risks, transformation moments, and re-engagement prescriptions. Ready?"

---

## The Engagement Mechanics

Before mapping, understand the forces that drive engagement up and down. Every movement
in the engagement curve has a mechanical cause.

### Forces That Drive Engagement UP

| Force | What triggers it |
|---|---|
| **Open Loop** | A question is raised that the reader needs answered |
| **Tension** | Conflict, stakes, or unresolved problems the reader cares about |
| **Recognition** | The reader sees their own experience described precisely |
| **Surprise** | An idea, fact, or turn the reader didn't anticipate |
| **Momentum** | A sense of forward movement — things are building toward something |
| **Intimacy** | The author speaks directly to the reader's private experience |
| **Proof** | A claim is backed by evidence compelling enough to shift belief |
| **Transformation Signal** | The reader feels themselves beginning to think differently |

### Forces That Drive Engagement DOWN

| Force | What triggers it |
|---|---|
| **Closed Loop** | All questions answered too early — nothing left to wonder about |
| **Friction** | Dense prose, unexplained jargon, or concepts requiring too much effort |
| **Repetition** | The reader has already understood this — saying it again creates boredom |
| **Abstraction Overload** | Too many ideas too quickly, without concrete anchoring |
| **Trust Erosion** | A claim that doesn't hold up, a gap in logic the reader notices |
| **Relevance Loss** | The reader can't see how this section applies to their situation |
| **Pace Mismatch** | Moving too slowly (patience exhausted) or too fast (reader lost) |
| **Promise Debt** | The book promised something earlier that hasn't been delivered yet |

---

## Output 1 — Engagement Curve

The backbone of the skill. A chapter-by-chapter engagement score with an annotated curve
showing every significant rise, plateau, dip, and recovery.

### Scoring Method

Score each chapter on **three dimensions**, each 1–10:

- **Hook Strength** — How strongly does this chapter pull the reader forward?
- **Delivery** — Does the chapter deliver on what the previous chapter promised?
- **Exit Momentum** — Does the reader finish this chapter *more* eager to continue than when they started?

Combined score = overall engagement level for that chapter.

### Engagement Curve Output

```
╔══════════════════════════════════════════════════════════════╗
║                  READER ENGAGEMENT CURVE                     ║
║                  [Book Title]                                ║
╚══════════════════════════════════════════════════════════════╝

ENGAGEMENT SCALE:  1 = Reader considers abandoning │ 10 = Unputdownable

┌─────────────────────────────────────────────────────────────┐
│  10 │                                                        │
│   9 │         ●                           ●                  │
│   8 │    ●         ●               ●           ●             │
│   7 │                   ●     ●                    ●         │
│   6 │                                                   ●    │
│   5 │  ●                                                     │
│   4 │                         ▼ ← DROP-OFF RISK             │
│   3 │                                                        │
│   2 │                                                        │
│   1 │                                                        │
└─────┴──────────────────────────────────────────────────────┘
      Ch1  Ch2  Ch3  Ch4  Ch5  Ch6  Ch7  Ch8  Ch9  Ch10 Ch11

[Note: Replace with actual chapter-by-chapter plot based on scores]

CHAPTER SCORES:
┌──────────────────────────────────────────────────────────────────────┐
│ Ch  │ Title              │ Hook │ Delivery │ Exit Momentum │ SCORE   │
├──────────────────────────────────────────────────────────────────────┤
│  1  │ [Title]            │  8   │    —     │      7        │  7.5    │
│  2  │ [Title]            │  7   │    8     │      8        │  7.7    │
│  3  │ [Title]            │  5   │    6     │      5        │  5.3  ⚠ │
│  4  │ [Title]            │  6   │    5     │      4        │  5.0  ⚠ │
│  5  │ [Title]            │  4   │    7     │      6        │  5.7  ⚠ │
│  6  │ [Title]            │  8   │    6     │      9        │  7.7    │
│  7  │ [Title]            │  9   │    9     │      9        │  9.0  ★ │
│  8  │ [Title]            │  7   │    9     │      7        │  7.7    │
│  9  │ [Title]            │  6   │    8     │      8        │  7.3    │
│ 10  │ [Title]            │  8   │    7     │      6        │  7.0    │
│ 11  │ [Title]            │  5   │    8     │      9        │  7.3    │
└──────────────────────────────────────────────────────────────────────┘
★ = Engagement peak     ⚠ = Drop-off risk zone (score below 6.0)

CURVE SHAPE:   [Describe: e.g., "Strong open, dangerous sag in Ch3–5,
                recovery and peak at Ch7, solid close"]

ENGAGEMENT PEAK:       Ch [N] — "[Title]" — [Why it peaks here]
ENGAGEMENT TROUGH:     Ch [N] — "[Title]" — [Why it dips here]
CRITICAL DROP-OFF WINDOW: Ch [N]–Ch [N] — [The window where readers are most
                           likely to abandon the book]

CURVE HEALTH:   [Strong / Solid / Problematic sag / Dangerous trough / Front-loaded]
╚══════════════════════════════════════════════════════════════╝
```

---

## Output 2 — Hook Zone Analysis

Maps every moment where the book has the power to *capture* the reader — the opening
of the book, the opening of each chapter, and any mid-chapter moments of peak pull.

There are **four types of hooks** — each with different mechanisms and ideal placement:

### Hook Type 1 — The Entry Hook (Book Opening)
The most important hook in the book. Pages 1–5 determine whether the reader commits.
Analyse: Does the opening create an immediate open loop? Does it signal that this book
understands the reader's exact situation? Does it create a reason to keep reading *today*?

### Hook Type 2 — The Chapter Hook (Chapter Openings)
The mini-commitment at the start of each chapter. The reader who finishes Chapter 3 and
opens Chapter 4 has already re-committed — but only if Chapter 4's first page justifies it.
Analyse: Does each chapter open with enough pull to honour the reader's recommitment?

### Hook Type 3 — The Tension Hook (Mid-Chapter)
Moments mid-chapter that spike engagement by introducing a new question, a surprise, or
a stakes-raising revelation just as attention might be drifting.
Analyse: Are there chapters long enough to need a mid-chapter tension spike, and do they
have one?

### Hook Type 4 — The Chapter-End Hook (Chapter Closings)
The mechanism that makes the reader turn the page instead of putting the book down.
Analyse: Does each chapter end with an open loop, a forward tease, or a micro-cliffhanger?
Or does it close completely — resolving all tension and giving the reader permission to stop?

```
HOOK ZONE ANALYSIS
════════════════════════════════════════════════════════════

THE ENTRY HOOK (Book Opening)
  Type:           [Story / Question / Provocative claim / Contradiction / Scene]
  Strength:       [X / 10]
  Open loop created: "[What question does it leave in the reader's mind?"]
  Risk:           [What would make a reader not continue past page 5?]
  Verdict:        [Hooks strongly / Hooks adequately / At risk of losing readers early]

CHAPTER-BY-CHAPTER HOOK ANALYSIS:

Ch [N]: "[Title]"
  Opening hook:   [Type + 1-sentence description]
  Hook strength:  [X / 10]
  Open loop:      "[What question does it create?]"
  Chapter-end hook: [Does it pull forward? How?]
  End hook type:  [Open loop / Forward tease / Cliffhanger / Closed — risk of stopping]
  Mid-chapter tension spike: [Present / Absent — needed at ~[word count]?]

Ch [N]: "[Title]"
  [Same structure for each chapter]

HOOK HEALTH SUMMARY:
  Strongest chapter hook:   Ch [N] — [Why it works]
  Weakest chapter hook:     Ch [N] — [Why it fails and what to fix]
  Chapters with no end hook: [List] — [Risk: readers may stop here]
  Chapters needing mid-chapter spike: [List] — [Too long without a tension reset]
════════════════════════════════════════════════════════════
```

---

## Output 3 — Drop-Off Risk Register

Every point in the book where a reader is statistically likely to stop — scored by severity
and explained by the specific mechanism causing the disengagement.

### Drop-Off Risk Types

**Type A — The Early Abandonment (Ch 1–2)**
The reader who commits tentatively but finds the opening doesn't deliver on the implicit
promise of the title and cover. Usually caused by: a hook that over-promises, an opening
that's slower than the cover implied, or a failure to signal quickly enough that this book
understands the reader's exact problem.

**Type B — The Mid-Book Sag (typically 30–50% through)**
The most common drop-off point in non-fiction. The reader has received the opening
argument and is waiting for the payoff — but the middle chapters feel like elaboration
rather than escalation. The book stops moving forward and starts circling.

**Type C — The Concept Overload Drop (after a dense chapter)**
A chapter that introduces too many new frameworks, terms, or ideas simultaneously. The
reader reaches saturation and needs a recovery chapter before the next push — but if
recovery doesn't come, they stop.

**Type D — The Trust Break Drop (after a claim that doesn't hold)**
The reader notices a logical flaw, an overstated claim, or a gap between the author's
confidence and the evidence. Trust erodes. The reader continues with diminishing
investment until a second trust break causes them to stop.

**Type E — The Promise Debt Drop (when a forward reference is forgotten)**
An early chapter says "we'll explore this fully in Chapter 8." Chapter 8 arrives and
delivers only a partial answer, or the promise is quietly dropped. The reader feels misled.

**Type F — The Completion Drift (final 20%)**
Paradoxically, the end of the book is a drop-off risk zone. The reader who has gotten the
main ideas may feel the final chapters are epilogue rather than payoff — and starts
skimming or stops. Usually caused by: a final section that applies rather than elevates,
or a conclusion that summarises instead of transforms.

```
DROP-OFF RISK REGISTER
════════════════════════════════════════════════════════════

RISK LEVEL KEY:
  🔴 CRITICAL    — High probability of permanent abandonment
  🟠 HIGH        — Significant disengagement risk; many readers pause here
  🟡 MODERATE    — Attention dip; readers continue but with lower investment
  🟢 LOW         — Minor friction; self-correcting

─────────────────────────────────────────────────────────────
RISK 1
  Location:     Ch [N] — "[Title]" — [Opening / Mid-chapter / Close]
  Risk type:    [A / B / C / D / E / F — with description]
  Risk level:   [🔴 / 🟠 / 🟡 / 🟢]
  The mechanism: [Exactly what causes disengagement here — specific to this
                  chapter's content, not generic]
  Who is most at risk: [Which reader type is most likely to drop here]
  Early warning sign:  [What the reader is experiencing just before this moment]
  Intervention window: [Where the fix must appear to prevent the drop]

RISK 2
  [Same structure]

[Continue for all identified risks]

─────────────────────────────────────────────────────────────
DROP-OFF RISK SUMMARY:

CRITICAL RISKS:     [Count] — Chapters [N, N]
HIGH RISKS:         [Count] — Chapters [N, N, N]
TOTAL RISK POINTS:  [Count]

THE MOST DANGEROUS MOMENT IN THIS BOOK:
  "[The single location where reader loss is most likely — and the precise
    mechanism. This is the one the author must fix before anything else.]"

STATISTICAL SURVIVAL ESTIMATE:
  [Of 100 readers who open page 1, roughly how many will finish — and where
   the major losses occur. Based on the risk register, not guesswork.]
  e.g., "~85 finish Ch 2, ~70 survive the Ch 4–5 sag, ~60 reach Ch 8,
         ~55 complete the book."
════════════════════════════════════════════════════════════
```

---

## Output 3B — The Survivor Profile

Not all readers who drop off were wrong to. This section identifies *which* readers are
most likely to complete the book, and what that means for the author's choices.

```
SURVIVOR PROFILE
─────────────────────────────────────────────────────────────
READERS MOST LIKELY TO FINISH:
  [Profile: what they have in common — level of prior knowledge, motivation,
   tolerance for density, specific pain point the book addresses]

READERS MOST LIKELY TO DROP:
  [Profile: where they come in with the wrong expectations, or where the book
   stops serving their specific need]

IMPLICATION:
  [Is the drop-off pattern a problem the author should fix, or a filtering
   mechanism that's working correctly — keeping the right readers and losing
   the wrong ones?]

CALIBRATION QUESTION:
  "[The question the author must answer: Am I writing for the readers who
    will finish, or am I trying to keep readers I should let go?]"
─────────────────────────────────────────────────────────────
```

---

## Output 4 — Transformation Moment Map

The most emotionally significant output. Maps the specific moments where the reader
doesn't just *receive information* — but where their thinking, belief, or self-perception
actually *shifts*.

Transformation moments are rare and precious. Most chapters deliver information. A few
chapters — if well-constructed — deliver genuine insight that changes how the reader sees
something. These are the moments readers quote in reviews, recommend the book for, and
remember years later.

### The Four Transformation Types

**Intellectual Transformation** — "I now understand something I didn't before."
The reader grasps a mechanism, a framework, or a connection that reorganises existing
knowledge into a new structure. *Feels like:* clarity, relief, the "click" of understanding.

**Belief Transformation** — "I now believe something I didn't before, or disbelieve
something I did."
The reader's position on a claim or idea genuinely shifts. Not just informed — *changed*.
*Feels like:* mild discomfort followed by conviction, or the deflation of a previously
held certainty.

**Identity Transformation** — "I now see myself differently."
The reader recognises themselves in a new category, or stops seeing themselves in an old
one. The most powerful transformation type — the one that drives word-of-mouth.
*Feels like:* recognition, relief, or the unsettling pleasure of being seen accurately.

**Agency Transformation** — "I now know what to do, and believe I can do it."
The shift from understanding to capability. The reader closes the gap between knowing
and acting.
*Feels like:* energy, urgency, the impulse to do something immediately.

```
TRANSFORMATION MOMENT MAP
════════════════════════════════════════════════════════════

INTENDED TRANSFORMATION (from book positioning):
  "[What the author wants readers to walk away believing/feeling/able to do]"

MAPPED TRANSFORMATION MOMENTS:

★ TRANSFORMATION 1
  Location:     Ch [N] — "[Title]" — [Section or passage]
  Type:         [Intellectual / Belief / Identity / Agency]
  The shift:    From: "[What the reader believed/understood/felt before this moment]"
                To:   "[What they believe/understand/feel after]"
  Trigger:      [What specifically causes the shift — the story, the argument,
                 the data point, the reframe]
  Emotional register: [What it feels like — clarity / discomfort / recognition /
                       energy / relief]
  Strength:     [Potential for transformation: Strong / Moderate / Weak]
  Why it works (or doesn't): [The mechanics of why this moment lands or falls short]

★ TRANSFORMATION 2
  [Same structure]

[Continue for all identified transformation moments]

─────────────────────────────────────────────────────────────
TRANSFORMATION HEALTH:

TRANSFORMATION COUNT:     [N moments identified]
TRANSFORMATION SPREAD:    [Early / Middle / Late / Clustered / Well-distributed]
TRANSFORMATION TYPES:     [Intellectual: N / Belief: N / Identity: N / Agency: N]

STRONGEST TRANSFORMATION: Ch [N] — [Why this is the book's most powerful moment]
WEAKEST TRANSFORMATION:   Ch [N] — [The chapter that claims to transform but doesn't
                                     deliver the mechanism]

FINAL TRANSFORMATION:     [Does the book end with its most powerful transformation,
                            or does the peak come too early?]

THE BOOK'S SIGNATURE MOMENT:
  "[The single moment most likely to be quoted in a 5-star review.
    The sentence or passage the reader texts to a friend.
    The moment the book justifies its existence.]"

MISSING TRANSFORMATION:
  [Any transformation the book's premise promises but the current chapters
   don't deliver — the gap between what the book claims to do and what it
   actually does to the reader]
════════════════════════════════════════════════════════════
```

---

## Output 5 — Re-Engagement Prescription

For every drop-off risk identified in Output 3, a specific, actionable prescription —
not generic advice, but a targeted intervention designed for that exact location and
mechanism.

### Prescription Types

**Opening Injection** — Add a new hook element at the start of the at-risk chapter.
Used when: the chapter hook is weak or the chapter opens with setup instead of pull.

**Tension Spike** — Introduce a new question, surprise, or stakes-raising moment
mid-chapter to reset attention.
Used when: a chapter is too long without a pull mechanism, or mid-chapter drift
is the identified risk.

**Chapter-End Hook Retrofit** — Add or sharpen the chapter-ending pull forward.
Used when: chapters close completely, giving readers permission to stop.

**Pace Reset** — Insert a short, fast-moving section (a case study, a quick story,
a sharp observation) after a dense conceptual passage.
Used when: concept overload is the identified drop-off mechanism.

**Promise Payment** — Deliver a forward reference made in an earlier chapter.
Used when: promise debt is causing late-book drift.

**Relevance Signal** — Add a direct "here's why this matters to you" bridge.
Used when: readers are losing sight of why a section applies to their situation.

**Chapter Restructure** — The risk is structural, not additive. The chapter needs
rebuilding, not patching.
Used when: the disengagement is caused by a wrong chapter order, a missing section,
or a chapter that's doing two jobs badly.

**Chapter Removal / Merge** — The risk is that the chapter shouldn't exist as a
standalone. Its content belongs in another chapter, or isn't needed at all.
Used when: the chapter repeats another, or its value doesn't justify the engagement
cost of a full chapter.

```
RE-ENGAGEMENT PRESCRIPTION
════════════════════════════════════════════════════════════

PRESCRIPTION 1 — Ch [N]: "[Title]"
  Risk addressed:   [From the Drop-Off Risk Register]
  Risk level:       [🔴 / 🟠 / 🟡]
  Prescription type: [Opening Injection / Tension Spike / End Hook / etc.]
  SPECIFIC FIX:
    "[Concrete, specific instruction — not 'add more energy' but 'open with the
      story of [X] that you reference in passing on page Y — put it first,
      before the framework introduction. The reader needs to care about the
      problem before they care about the solution.']"
  Where to place it: [Exact location — opening / after section 2 / chapter end]
  Effort level:      [Add 1 paragraph / Rewrite the opening / Restructure the chapter]
  Expected impact:   [How this specific fix addresses the identified mechanism]

PRESCRIPTION 2 — Ch [N]: "[Title]"
  [Same structure]

[Continue for all identified risks]

─────────────────────────────────────────────────────────────
PRESCRIPTION PRIORITY ORDER:

MUST FIX (critical risks, highest ROI):
  1. [Prescription for 🔴 risk — Ch N]
  2. [Prescription for 🔴 risk — Ch N]

FIX NEXT (high risk, significant impact):
  3. [Prescription for 🟠 risk — Ch N]
  4. [Prescription for 🟠 risk — Ch N]

ADDRESS IF BANDWIDTH ALLOWS:
  5. [Prescription for 🟡 risk — Ch N]
  ...

SINGLE HIGHEST-ROI FIX:
  "[If the author can only do one thing — the single intervention that would
    most improve overall completion rate and reader satisfaction. Specific and
    immediately actionable.]"
════════════════════════════════════════════════════════════
```

---

## The Journey Map Summary

After all five outputs, produce a single **Reader Journey Map** — a one-page visual
summary the author can use as a diagnostic reference throughout revision.

```
╔══════════════════════════════════════════════════════════════╗
║                  READER JOURNEY MAP                          ║
║                  [Book Title]                                ║
╚══════════════════════════════════════════════════════════════╝

ENGAGEMENT CURVE (simplified):
  Ch 1  [████████░░]  7.5  — Entry hook: STRONG
  Ch 2  [████████░░]  7.7  — Building well
  Ch 3  [█████░░░░░]  5.3  ⚠ DROP-OFF RISK
  Ch 4  [█████░░░░░]  5.0  ⚠ DROP-OFF RISK — CRITICAL WINDOW
  Ch 5  [██████░░░░]  5.7  ⚠ Recovery insufficient
  Ch 6  [████████░░]  7.7  — Recovery achieved
  Ch 7  [██████████]  9.0  ★ PEAK ENGAGEMENT / TRANSFORMATION
  Ch 8  [████████░░]  7.7  — Solid delivery
  Ch 9  [███████░░░]  7.3  — Holding
  Ch 10 [███████░░░]  7.0  — Slight drift
  Ch 11 [███████░░░]  7.3  — Close: adequate

KEY MOMENTS:
  🎣 ENTRY HOOK:        Ch 1 — [What captures the reader]
  ⚡ FIRST PEAK:         Ch [N] — [First engagement high point]
  ⚠️  CRITICAL RISK:     Ch [N–N] — [The dangerous window]
  ★  TRANSFORMATION:    Ch [N] — [The book's signature moment]
  📉 COMPLETION DRIFT:  Ch [N+] — [If present — late-book risk]
  🏁 EXIT STATE:        "[How the reader feels on the final page"]

SURVIVAL ESTIMATE:      ~[X]% of readers who open page 1 will finish
BIGGEST THREAT:         [The one risk that most needs addressing]
BIGGEST ASSET:          [The one moment that most justifies the book's existence]

PRIORITY PRESCRIPTIONS:
  1. [Most urgent fix — one sentence]
  2. [Second priority — one sentence]
  3. [Third priority — one sentence]
╚══════════════════════════════════════════════════════════════╝
```

---

## Audit Mode

For authors who want to re-map engagement after revisions — to measure whether
interventions improved the curve.

Run the same scoring against the revised chapter and show the **before/after delta**:

```
REVISION IMPACT AUDIT — Ch [N]: "[Title]"
─────────────────────────────────────────────────────────────
BEFORE:  Hook [X] / Delivery [X] / Exit Momentum [X] → Score [X.X]
AFTER:   Hook [X] / Delivery [X] / Exit Momentum [X] → Score [X.X]
DELTA:   [+X.X improvement]
VERDICT: [The specific intervention worked / Partially worked / Insufficient —
          and why]
─────────────────────────────────────────────────────────────
```

---

## Integration with Other Skills

**← narrative-spine-builder**: The spine builder designs the *intended* emotional arc.
The Journey Mapper diagnoses whether the *actual content* produces that arc. Feed the
spine's emotional progression into this skill's intake — then compare intended vs.
mapped engagement to find where execution diverges from design.

**← chapter-builder Craft Note**: Chapters flagged in the Craft Note as "thin" or
"needing more story" are almost always in the drop-off risk zone. The Journey Mapper
confirms it with a score and a specific mechanism — then the prescription tells the
author exactly what type of addition is needed.

**→ editor-sharpener**: Every re-engagement prescription that involves adding a hook,
rewriting an opening, or retrofitting a chapter-end pull feeds into editor-sharpener
as a targeted brief: *"Mode 3 — Fix the opening / Rewrite the close for Ch [N] using
this specific prescription."*

**→ beta-reader-simulator**: The drop-off risk register predicts *where* engagement
breaks. The beta reader simulator then *confirms* it by simulating a persona reading
through those exact chapters: *"Test the Ch 3–5 window with the Skeptic and the Busy
Professional — the journey map says this is the critical abandonment zone."*

**→ red-team-critic**: Trust Break drop-offs (Type D) require the red team, not a
re-engagement prescription. If a reader is dropping because they don't believe a claim,
the answer is intellectual — fix the argument. Pass the flagged claim to the red-team
critic for a targeted attack before attempting a prose fix.

---

## Quick Commands

| Command | Output | Action |
|---|---|---|
| `"Map the reader journey"` | All | Full five-output journey map |
| `"Plot the engagement curve"` | 1 | Engagement curve + chapter scores only |
| `"Where will readers get hooked?"` | 2 | Hook zone analysis only |
| `"Where are the drop-off risks?"` | 3 | Drop-off risk register only |
| `"Where is the transformation?"` | 4 | Transformation moment map only |
| `"Give me re-engagement prescriptions"` | 5 | Prescriptions only — assumes prior mapping |
| `"Give me the journey map summary"` | Summary | One-page diagnostic reference |
| `"Score this chapter's engagement"` | 1 (single) | Score one chapter on all three dimensions |
| `"How many readers will finish this book?"` | 3 | Survival estimate + risk analysis |
| `"What's the book's signature moment?"` | 4 | Single most powerful transformation point |
| `"What's the single most important fix?"` | 5 | Highest-ROI prescription only |
| `"Re-map after my revisions"` | Audit | Before/after engagement delta |
| `"Where will readers stop?"` | 3 | Drop-off risk register — critical and high only |
