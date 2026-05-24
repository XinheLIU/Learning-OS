---
name: survey
description: Survey a domain before learning. Use when the user wants to explore a new field, figure out what's worth learning, or says "/survey <topic>". Replaces the old scout command with a structured research flow.
---

# Survey

Landscape scan before model-building. The goal is to have a structured overview of a domain — history, key people, current state, controversies, business impact — so the user can decide what's worth diving into. This feeds directly into `/learn`.

## Philosophy

- **Two entry points, one output.** User has notes/context → organize and structure. User knows little → web research driven by 5 standardized questions.
- **Breadth, not depth.** A survey is a map, not a textbook. It should take 20-30 minutes to consume.
- **People matter.** Names, contributions, why they matter, what they argue about. A field is shaped by its key figures.
- **Hand off cleanly.** The survey ends with a recommendation: what to `/learn` first.

## Flow

### 1. Auto-init

If `topics/<slug>/` doesn't exist, create it with `memory/` subdirectory and a minimal README. Don't ask permission.

### 2. Determine entry path

Ask: "How much do you already know about <topic>? Have you read anything, done any projects, or have notes you want me to organize?"

- **Path A — User has context:** They describe what they know, paste notes, or point to resources. Your job is to organize, structure, and identify gaps. Skip the web research for what they already have covered, fill in only what's missing.
- **Path B — User knows little:** Full web research driven by the 5 questions below. Run searches in parallel where possible.

### 3. The 5 questions

Answer these in order. For Path A, ask the user first — only research what they can't answer. For Path B, research all 5.

**Q1: Recent 5-year development**
- What's changed in this field since ~2021?
- What breakthroughs, papers, or tools shifted the landscape?
- What's the trajectory — accelerating, plateauing, or pivoting?

**Q2: History and key people**
- Who built this field? What did they contribute, how, and why?
- What problems were they trying to solve at the time?
- Give a story-telling overview — not just a timeline, but the narrative arc.

**Q3: Status quo and controversies**
- What's the current SOTA? Who are the key people/groups right now?
- What are the open problems nobody has solved?
- What do practitioners argue about? (Schools of thought, competing approaches)

**Q4: Business and future impact**
- What's the business impact in the next 5 years?
- Which industries are betting on this? Where's the money going?
- What's the longer-term trajectory beyond 5 years?

**Q5: Overall framework**
- Synthesize everything above into a Mermaid diagram showing the structure of the field
- Include: historical roots → key branches → current schools → open problems → future directions
- This is the "map" the user will refer back to

### 4. Write survey

Write `topics/<slug>/memory/survey.md`:

```markdown
# <Topic> — Landscape Survey

**Date:** <today>
**Sources:** <list of key sources consulted>

## Recent 5-Year Development (2021–)
<3-5 paragraphs>

## History & Key People
<4-6 paragraphs, story-telling style. Names, contributions, motivations.>

## Current State & Controversies
**SOTA:** <2-3 lines>
**Key people/groups now:** <list>
**Open problems:**
- <problem 1>
- <problem 2>
**Controversies:**
- <controversy 1 — who argues what>
- <controversy 2>

## Business & Future Impact
<2-3 paragraphs covering near-term (5yr) and longer-term>

## Domain Map

'''mermaid
<Mermaid diagram of the field's structure>
'''
```

### 5. Recommend next

End with 2-3 concrete suggestions:
- "Based on this survey, I'd recommend `/learn <slug>` starting with <subtopic> — it's the most foundational."
- "The biggest controversy right now is <X>. Worth forming your own position on it."
- "<Subtopic Y> seems overhyped relative to its actual impact. Maybe skip it for now."

### 6. Update README

Update `topics/<slug>/README.md`:
```markdown
# <Topic>
- Slug: `<slug>`
- Started: <date>
- Surveyed: <date>
- Last session: <date>
```

## Warnings

- Don't spend more than 30 minutes on a survey. It's a map, not a dissertation.
- Don't research everything if the user already knows parts. Fill gaps, don't re-litigate what they have.
- Don't force the Mermaid diagram to be perfect. A rough map is better than no map.
- If web research yields conflicting information, note the conflict — don't pick a winner silently.
- This is NOT the learn step. Don't build models here. Just map the terrain.
