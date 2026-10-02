---
name: pre-write-grill
description: Establish complete shared understanding before writing begins. Use for 开题确认, intensive upfront questioning about topic, scope, length, materials, examples, and structure. The mandatory gate before material processing and drafting.
---

# Pre-Write Grill

Last updated: 2026-10-01

Reach shared understanding on what to write and how deep before processing materials or drafting prose. This is the upfront intensive questioning phase that prevents misaligned output.

## Purpose

Establish explicit agreement on:
- **Topic selection** - which question from possible angles
- **Scope boundaries** - what's in, what's excluded
- **Target length** - depth and coverage expectation
- **Material priorities** - which of the author's sources to emphasize
- **Example specifications** - what concrete cases to develop
- **Structure approach** - endorsed logical flow

**Contract:** Downstream skills (`frame`, `map-materials`, `write-content`) do not run until these elements are confirmed.

## When to Use

**Trigger this skill when:**
- Author has scattered materials without a clear unified question
- Multiple interpretations or angles exist
- Original argumentative or exploratory piece (not faithful summary of single source)
- Synthesis across author's materials into argued position

**Skip this skill when:**
- Faithful summary/explanation of single external source (no synthesis needed)
- Author has already provided explicit detailed specification
- Targeted edit of existing draft (not new piece)

## Workflow

### Step 1: Initial Read (Light Touch)

Read materials enough to identify:
- What types of materials exist (drafts, notes, references, data)
- What broad themes emerge
- What 2-3 distinct angles are possible

Do NOT:
- Create exhaustive 24-row catalogs yet
- Search external sources yet
- Process every detail

This is reconnaissance only. Deep processing happens after topic confirmed.

### Step 2: Present Candidate Angles

Show 2-3 concrete topic angles with explicit trade-offs:

```markdown
**Angle 1: [Question]**
- Reader benefit: [specific gain]
- Requires: [what materials/evidence needed]
- Excludes: [what this won't cover]
- Estimated scope: [length/depth]

**Angle 2: [Question]**
- Reader benefit: [different gain]
- Requires: [different evidence mix]
- Excludes: [different boundaries]
- Estimated scope: [different scale]
```

Ask: "Which angle serves your intent?"

**Allow "none of these" responses.** If author rejects all angles, probe deeper with [questioning framework](references/questioning-framework.md).

### Step 3: Grill on Scope

Once angle selected, grill systematically:

**Scope boundaries:**
- "What specifically is IN scope for this piece?"
- "What related topics are explicitly OUT of scope?"
- "Where should this piece stop?"

**Target length and depth:**
- "Is this an 800-word argument, a 3000-word deep dive, or something else?"
- "How much depth on each major point?"
- Present rough structural options (3-section vs 5-section, etc.)

**Material priorities:**
- Show the author's materials list (from Step 1 light read)
- "Which of these should be primary evidence?"
- "Which are supporting? Which are peripheral?"

**Example specifications:**
- "What concrete examples should this develop?"
- "Do you want to use your personal projects/experiences?"
- "External cases? Which kinds?"

**Logical structure:**
- Present 2 structural approaches matching the angle
- "Linear explanation A→B→C, or dialectical setup→objection→resolution?"
- Ask: "Does this structure serve the question?"

### Step 4: Iterative Refinement

Continue questioning until author explicitly confirms. Signals that shared understanding is reached:
- Author provides concrete decisions, not vague preferences
- Boundaries are explicit, not implied
- Author says "yes, proceed" or equivalent

**Allow trust delegation:** If author says "I trust your judgment on [X]", record that delegation and skip detailed sub-questions on X.

**Detect misalignment early:** If author's answers contradict each other or the selected angle, surface the contradiction and resolve it now.

### Step 5: Write Specification Summary

Produce a confirmed specification document:

```markdown
# Writing Specification: [piece-name]

Last updated: YYYY-MM-DD

## Confirmed Topic
[The selected angle's question]

## Scope
**In scope:**
- [specific topic 1]
- [specific topic 2]

**Out of scope:**
- [excluded topic 1]
- [excluded topic 2]

## Target Length
[e.g., "3000-word deep dive" or "800-word focused argument"]

## Material Priorities
**Primary (core evidence):**
- material1.md - [why primary]
- material3.md - [why primary]

**Supporting:**
- material2.md - [supporting role]

**Peripheral (note but don't deep-dive):**
- material4-6.md - [why peripheral]

## Example Specifications
- Author's ByteDance transformation project (personal)
- External: EvenUp legal AI, Intercom Fin (already known from materials)
- Avoid: generic AI hype examples

## Endorsed Structure
[3-section argue: current stage → strategic implications → personal positioning]
OR
[5-section explore: phenomenon → theory A → theory B → evidence → implications]

## Special Constraints
[Any author-specific requirements, e.g., "Must cite QJE 2025 paper", "Avoid jargon", "Target Chinese audience"]
```

Ask: **"Confirmed? Shall I proceed to framing and writing?"**

Only proceed after explicit author confirmation.

## Handoffs

**Output:** Confirmed specification document

**Next skill:**
1. `/frame` - writes `brief.md` consuming this specification
2. `/map-materials` - now runs AFTER topic known, focusing on confirmed priorities
3. Evidence development and external search happen during `/develop-examples`, not during exploration

**Contract:** If specification is not confirmed, do not proceed to downstream skills. Ask clarifying questions instead.

## Completion Criteria

Done when:
- ✅ One topic angle selected from presented options
- ✅ Scope boundaries explicitly stated (in/out)
- ✅ Target length/depth confirmed
- ✅ Material priorities categorized (primary/supporting/peripheral)
- ✅ Example specifications stated
- ✅ Logical structure endorsed
- ✅ Author explicitly confirms: "yes, proceed"

Not done when:
- ❌ Author gave vague preferences without concrete decisions
- ❌ Boundaries implied but not explicit
- ❌ "Whatever you think is best" without delegation acknowledgment
- ❌ Structural contradictions unresolved

## Boundaries and Ownership

**This skill owns:** Establishing shared understanding before downstream work begins.

**This skill does NOT:**
- Write the formal `brief.md` (that's `/frame`'s job)
- Create exhaustive material maps (that's `/map-materials` after confirmation)
- Draft prose (that's `/write-content`)
- Search external sources (that's evidence development)
- Make unilateral decisions on ambiguous points

**Author owns:**
- Final topic selection
- Judgments and scope boundaries
- Personal experience inclusion decisions
- Material relevance assessment

## Common Failure Modes

**Failure: Insufficient questioning**
- Symptom: Downstream draft doesn't match author's intent
- Fix: Grill more aggressively on boundaries and examples

**Failure: Over-questioning fluent authors**
- Symptom: Author says "stop asking, just write it"
- Fix: Accept delegation explicitly; record "author delegates [X] decisions"

**Failure: Accepting vague answers**
- Symptom: "Make it comprehensive" or "whatever you think"
- Fix: Present concrete options with trade-offs; force choice

**Failure: Skipping material prioritization**
- Symptom: Downstream map processes everything equally
- Fix: Always ask "which materials are primary?"

## Example Execution

**Input:** Author provides 8 material files about AI opportunities, asks "where am I and what should I do?"

**Step 1 Light Read:** 
- Identified: personal background (quant, Goldman, ByteDance), market analysis drafts, external papers
- Themes: AI adoption stages, ToB vs ToC, personal capability

**Step 2 Present Angles:**

Angle 1: "此时此刻，恰如彼时彼刻：身处 AI 机会窗口，懂技术也懂企业的人该积累什么？"
- Argumentative, personal positioning, 3000 words
- Emphasizes author's dual background
- Needs: personal project examples, enterprise transformation evidence

Angle 2: "AI 的 1995 时刻：为什么现在仍是早期，个人如何抓住窗口"
- Explanatory, market analysis, 2000 words  
- Emphasizes timing and opportunity structure
- Needs: historical parallels, adoption data

Angle 3: "从量化到 AI Agent：一个技术人的转型复盘"
- Reflective narrative, personal journey, 4000 words
- Emphasizes career transition lessons
- Needs: deep personal stories, decision rationale

Author selects: **Angle 1**

**Step 3 Grill:**

Q: "Target length for Angle 1?"
A: "3000-word deep argument, not surface listicle"

Q: "Which of your 8 materials are primary evidence?"
A: "My ByteDance transformation notes (material 1), personal capability reflection (material 2). The market analysis drafts (3,4) are supporting context. External papers (5-8) validate but aren't the core."

Q: "Personal examples - use your real projects?"
A: "Yes, ByteDance enterprise AI rollout, but keep company details generic. Also my current agent engineering work."

Q: "Structure: linear build (stage→strategy→action) or dialectical (objection→response)?"
A: "Linear build, 4 sections: stage judgment, company formation analysis, ToC vs ToB trade-offs, personal positioning."

Q: "What's explicitly out of scope?"
A: "Technical AI capabilities tutorial, fundraising advice, comprehensive industry survey"

**Step 4 Confirm:**

[Present specification summary]

Q: "Confirmed? Proceed to framing and writing?"
A: "Yes, confirmed."

**Output:** Specification document → handoff to `/frame`

## Contract Test

Given scattered materials without clear question, present at least 2 distinct angles with explicit trade-offs. Given author confirmation of topic + scope + length + material priorities + examples + structure, produce specification document and hand off to `/frame`. Never proceed to material mapping or drafting before confirmation. When author answers are contradictory, surface the contradiction rather than guessing which to follow.
