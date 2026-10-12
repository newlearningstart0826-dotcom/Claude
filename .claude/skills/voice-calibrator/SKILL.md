---
name: voice-calibrator
description: >
  Author voice calibration skill. Use this skill whenever an author wants to define, capture, or
  codify their writing voice — so that all drafting and editing stays true to how they actually
  write. Trigger for: "calibrate my voice", "capture my writing style", "here are some writing
  samples", "write in my voice", "it doesn't sound like me", "make it sound more like me",
  "extract my voice from this", "build a voice profile", "analyse my writing style", "what's my
  writing voice?", or any time the author pastes existing writing (blog posts, emails, LinkedIn
  posts, talks, essays, previous book excerpts) and wants it used as a style benchmark. Also
  trigger before starting chapter-builder if no voice has been established yet — a calibrated
  voice fingerprint makes every downstream draft and edit significantly more accurate. Outputs a
  precise, reusable Voice Fingerprint document that plugs directly into chapter-builder and
  editor-sharpener.
---

# Voice Calibrator

A skill that extracts the author's precise writing voice from real writing samples — and produces
a **Voice Fingerprint** that all other skills (chapter-builder, editor-sharpener) can use as a
concrete benchmark.

This replaces the vague "describe your voice" question in other skills with something far more
accurate: analysis of how the author *actually* writes, not how they *think* they write.

The workflow has **three phases**:
1. **Sample Collection** — gather writing samples from the author
2. **Voice Analysis** — extract the fingerprint across 8 dimensions
3. **Voice Fingerprint Output** — produce the reusable profile + calibration test

---

## Phase 1 — Sample Collection

### Ask for samples

Open with:

> "To capture your voice accurately, I need to read how you already write — not how you'd
> describe your style. Paste 2–5 samples of your writing. These can be blog posts, LinkedIn
> articles, email newsletters, talk transcripts, a previous book, essays, even long thoughtful
> emails. The more variety, the better the fingerprint."

**Ideal sample set:**
- At minimum: 2 samples, each at least 300 words
- Best case: 3–5 samples across different contexts (one explanatory, one story-driven, one opinion/argument)
- If the author has no writing samples: see **No-Sample Protocol** below

### What to do with samples

Once received, tell the author:
> "Got them. Give me a moment to read closely — I'll come back with your Voice Fingerprint."

Then run Phase 2 silently. Do not ask clarifying questions before analysing — read first, ask later.

### No-Sample Protocol

If the author has no existing writing samples:

1. Run a **Voice Interview** (5 questions, conversational):
   - "Tell me about a time a piece of advice completely changed how you worked. Just talk — don't write carefully."
   - "What's a belief you hold about your field that most people in it get wrong?"
   - "Describe your ideal reader as if you were telling a friend about them."
   - "What's the most important thing your book needs to make the reader *feel* by the end?"
   - "What's a word or phrase you hate seeing in books like yours?"

2. Capture their *spoken* voice from the answers — people write more guardedly than they speak, but their true voice lives in how they explain things naturally.

3. Flag in the output: *"This fingerprint is based on how you speak, not existing writing. Treat it as a starting point — update it once you've written your first chapter draft."*

---

## Phase 2 — Voice Analysis

Analyse the samples across **8 dimensions**. Do this silently and thoroughly before presenting
anything. The quality of the fingerprint depends on noticing specifics, not generalities.

---

### Dimension 1 — Sentence Architecture

Study the author's sentence patterns:

- **Average sentence length** — count roughly. Under 15 words = punchy. 15–25 = conversational. 25+ = dense/academic.
- **Sentence variety** — do they vary length deliberately, or is it uniform?
- **Signature structures** — do they use em-dashes for asides? Colons to pivot? Fragments for emphasis? Opening questions?
- **Paragraph length** — short and punchy (1–3 sentences) or developed blocks (4–7)?

Look for: **the sentence rhythm that feels most "them"** — it's usually most visible in their best paragraphs.

---

### Dimension 2 — Vocabulary Register

- **Formality level** — do they use "utilise" or "use"? "Subsequently" or "then"? "Individuals" or "people"?
- **Technical vocabulary** — how much domain jargon, and how do they handle it? Define it? Assume it? Avoid it?
- **Signature words** — collect 8–12 words or phrases they use repeatedly that feel distinctly theirs
- **Words they avoid** — any words/phrases they conspicuously never use that others in their field do?

---

### Dimension 3 — Persona & Authority Stance

How does the author position themselves relative to the reader?

- **Peer** — writes as an equal sharing what they've discovered ("I've been there too...")
- **Mentor** — experienced guide passing down hard-won wisdom ("Here's what I wish someone had told me...")
- **Expert** — authoritative voice presenting conclusions ("The research is clear...")
- **Provocateur** — challenges the reader's assumptions ("Everything you've been told about X is wrong...")

Most authors are a blend. Identify the primary and secondary stance.

Also note: **how do they handle being wrong or uncertain?** Do they admit it openly? Reframe it? Avoid it?

---

### Dimension 4 — Storytelling Style

- **Do they use personal stories?** (First-person anecdotes, "When I was..." moments)
- **Do they use third-party stories?** (Case studies, "A client of mine once...", named examples)
- **Do they use hypotheticals?** ("Imagine you're standing in front of...")
- **Story length** — brief illustrative flashes (1–3 sentences) or developed narratives (full scenes)?
- **Story placement** — do they open with story or use it mid-argument to prove a point?
- **Dialogue** — do they quote people directly, or paraphrase?

---

### Dimension 5 — Argument Structure

How does the author build a case?

- **Deductive** — state the conclusion first, then support it (top-down)
- **Inductive** — build from examples/evidence to the conclusion (bottom-up)
- **Narrative** — tell a story that *becomes* the argument
- **Problem/Solution** — name the pain, then offer the fix
- **Contrast** — "most people do X, but the best do Y"

Also: **how do they handle complexity?** Do they simplify, layer carefully, or lean into nuance?

---

### Dimension 6 — Reader Relationship

How does the author speak *to* the reader?

- **Second person frequency** — how often do they use "you"? Constantly? Occasionally? Almost never?
- **Inclusive "we"** — do they use "we" to put themselves and the reader in the same boat?
- **Rhetorical questions** — do they ask the reader questions, and how often?
- **Assumed knowledge** — what do they assume the reader already knows?
- **Tone toward reader** — warm and encouraging? Challenging and demanding? Matter-of-fact?

---

### Dimension 7 — Humour & Personality

- **Do they use humour?** If so: dry/wry? Self-deprecating? Observational? Absurdist?
- **Do they use cultural references?** (Films, sports, history, pop culture)
- **Asides and parentheticals** — do they drop in small personality moments mid-argument?
- **What makes their writing feel human?** The specific quality that makes it feel *them* and not AI or a textbook.

---

### Dimension 8 — What They're NOT

As important as what they do — what is *absent* from their writing?

- Passive voice? (or do they use it?)
- Hedging and over-qualification?
- Motivational clichés ("unlock your potential", "game-changing", "transformation")?
- Academic throat-clearing?
- Excessive data/statistics?
- Emotional over-sharing?

Naming what the author *doesn't* do is as useful as naming what they do — it gives the
chapter-builder and editor clear guardrails.

---

## Phase 3 — Voice Fingerprint Output

Present the full Voice Fingerprint. This is a living document the author should save and
attach to every writing session.

```
╔══════════════════════════════════════════════════════════════╗
║              AUTHOR VOICE FINGERPRINT                        ║
║              [Author Name / Book Working Title]              ║
╚══════════════════════════════════════════════════════════════╝

━━━ THE ONE-LINE SUMMARY ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[A single sentence capturing the author's voice essence.
Example: "Warm but direct — a smart friend who's done the hard
work and is cutting through the noise to save you time."]

━━━ SENTENCE ARCHITECTURE ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Avg sentence length:    [short / medium / long / mixed]
Paragraph style:        [compact blocks / developed paragraphs / varied]
Signature structures:   [e.g., "Em-dash asides for personality beats",
                         "Fragment sentences for emphasis",
                         "Opens paragraphs with a direct claim"]
Rhythm note:            [How the best paragraphs feel to read aloud]

━━━ VOCABULARY REGISTER ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Formality level:        [1=very casual ←————→ 5=formal] [X/5]
Jargon approach:        [avoids / uses + defines / assumes reader knows]
SIGNATURE WORDS & PHRASES (use these — they're distinctly yours):
  • [word/phrase 1]
  • [word/phrase 2]
  • [word/phrase 3]
  • [word/phrase 4]
  • [word/phrase 5]
  • [word/phrase 6]
  • [word/phrase 7]
  • [word/phrase 8]

━━━ AUTHORITY STANCE ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Primary persona:        [Peer / Mentor / Expert / Provocateur]
Secondary persona:      [if applicable]
How they handle uncertainty: [openly admits / reframes / leans into it]
Confidence level:       [direct assertions / occasional hedges / frequent hedges]

━━━ STORYTELLING STYLE ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Story types used:       [personal / third-party / hypothetical / all three]
Story length:           [flash (1–3 sentences) / medium / full scenes]
Story placement:        [opens chapters / proves points mid-argument / both]
Dialogue:               [uses direct quotes / paraphrases / rarely uses dialogue]

━━━ ARGUMENT STRUCTURE ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Dominant pattern:       [Deductive / Inductive / Narrative / Problem-Solution / Contrast]
How they handle complexity: [simplifies / layers carefully / embraces nuance]
Evidence style:         [data-led / story-led / principle-led / mixed]

━━━ READER RELATIONSHIP ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"You" frequency:        [constant / moderate / rare]
Inclusive "we":         [uses often / occasionally / avoids]
Rhetorical questions:   [frequently / sparingly / not at all]
Tone toward reader:     [warm / challenging / matter-of-fact / encouraging]
Assumed reader knowledge: [describe baseline]

━━━ PERSONALITY & HUMOUR ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Humour style:           [dry / self-deprecating / observational / none]
Cultural references:    [type + frequency]
Human moments:          [the specific quality that makes this feel like a person]

━━━ DO NOT WRITE LIKE THIS ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
(Patterns absent from samples — breaking these = sounds wrong)
  ✗ [Pattern 1 — e.g., "Passive voice constructions"]
  ✗ [Pattern 2 — e.g., "Motivational clichés (game-changing, transformation)"]
  ✗ [Pattern 3 — e.g., "Starting sentences with 'Additionally' or 'Furthermore'"]
  ✗ [Pattern 4 — e.g., "Academic hedging ('it could be argued that...')"]
  ✗ [Pattern 5 — e.g., "Overly long winding sentences without a clear landing"]

━━━ REFERENCE PASSAGES ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
(Best examples from the author's own writing — read these before drafting)

BEST OPENING:
"[Excerpt — the author's best hook from the samples]"

BEST EXPLANATION:
"[Excerpt — clearest logical explanation from samples]"

BEST STORY BEAT:
"[Excerpt — most natural story moment from samples]"

━━━ CALIBRATION NOTE ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[Any caveats — e.g., "Samples skewed toward LinkedIn brevity;
book chapters may need longer story development", or "Voice is
most consistent in argumentative pieces; personal story sections
are less developed — watch for voice drift there."]
══════════════════════════════════════════════════════════════
```

### After presenting the fingerprint

Ask the author two questions:

1. > "Does this feel like you? Any dimensions that are off, or anything important I missed?"
2. > "Is there a piece of writing you've done that you're *most* proud of — the one that sounds exactly right? If so, share it and I'll make sure the fingerprint reflects it."

Revise until the author confirms it's accurate. Then offer:

> "This Voice Fingerprint is now ready to use. You can paste it at the start of any conversation
> with chapter-builder or editor-sharpener and they'll use it as the benchmark for every draft
> and edit."

---

## Calibration Test

Once the fingerprint is confirmed, run a **Calibration Test** to prove it works:

> "Want me to write a short test passage (~200 words) using this fingerprint — on any topic you
> choose — so you can see what it produces before using it on the real chapters?"

If they say yes: write the test passage, then ask:
> "On a scale of 1–10, how much does that sound like you? What would you change?"

Use the feedback to refine the fingerprint before finalising.

---

## Voice Drift Detection

If the author returns later with a chapter that "doesn't feel like me," run a quick **Voice Drift Check**:

Compare the chapter against the fingerprint on 3 fast dimensions:

```
VOICE DRIFT CHECK
─────────────────────────────────────────────────────
Sentence architecture:  [Matches / Drifted — how]
Vocabulary register:    [Matches / Drifted — how]
Authority stance:       [Matches / Drifted — how]

DRIFT DIAGNOSIS:  [What caused the drift — e.g., "This section
                   is more formal than your usual register —
                   likely because the topic felt technical and
                   you shifted into 'expert mode'"]
FIX:              [Specific instruction to restore voice]
─────────────────────────────────────────────────────
```

Then apply the fix — usually a targeted Pass 5 (Voice Pass) from the editor-sharpener.

---

## Integration with Other Skills

**→ chapter-builder**: Paste the Voice Fingerprint into the Chapter Brief under `VOICE/TONE`.
The "One-Line Summary", "Signature Words", "Do Not Write Like This", and "Reference Passages"
sections are the most critical — they give the drafter a concrete target instead of a vague
style description.

**→ editor-sharpener**: Paste the Voice Fingerprint before requesting any edit. The editor will
use the "Do Not Write Like This" list as the fluff/pattern removal guide, and the "Reference
Passages" as the benchmark for what "good" sounds like for this author specifically.

**→ book-architect**: If the author hasn't used book-architect yet, the Voice Fingerprint's
"Authority Stance" and "Reader Relationship" sections will inform the Tone & Style field in the
Positioning Plan.

---

## Quick Commands

| Command | Action |
|---|---|
| `"Build my voice fingerprint"` | Full sample collection + analysis + fingerprint output |
| `"Here are my writing samples"` | Skip the intro, go straight to analysis |
| `"Does this sound like me?"` | Run a Voice Drift Check on a pasted passage |
| `"Update my fingerprint"` | Revise an existing fingerprint with new samples or feedback |
| `"Write a test passage"` | 200-word calibration test in the author's voice on a chosen topic |
| `"What are my signature phrases?"` | Pull just the vocabulary section from the fingerprint |
| `"What should I never write?"` | Pull just the "Do Not Write Like This" section |
| `"I have no writing samples"` | Run the Voice Interview protocol instead |
