---
name: learn
description: Build mental models for a new domain through interview. Use when the user wants to learn a topic, start a new domain, understand a field, or says "/learn <topic>". Replaces the old scout → radar-frame → term-map → radar-check pipeline with a single conversation-driven flow.
---

# Learn

A conversation-driven skill for building mental models in a new domain. No templates, no fixed count of models. The AI interviews the user, models emerge from cases, and short memory files capture what's earned.

## Philosophy

- **Interview before instructing.** Ask what the user already knows, what they've done, what confuses them. Don't lecture into a void.
- **Models emerge from cases.** Don't pre-decide "5 models." Some domains have 3, some have 7. Let the conversation surface them.
- **Short files.** One idea per memory file. If it's longer than a screen, split it.
- **HITL by default.** The user names the models, the user explains the concepts. The AI sharpens, challenges, connects.

## Flow

### 0. Check survey

If `topics/<slug>/memory/survey.md` exists, read it first — it has the landscape context. If it doesn't exist, ask: "No survey yet for <slug>. Want to `/survey <slug>` first to map the terrain, or jump straight into model-building?" Don't block on this, but recommend it if the user seems new to the domain.

### 1. Auto-init

If `topics/<slug>/` doesn't exist, create it with `memory/` subdirectory and a minimal README. Don't ask permission — just do it.

```
topics/<slug>/
  memory/          ← all knowledge goes here (flat, no subfolders)
  README.md        ← auto-generated, minimal
```

### 2. Interview (the core)

Ask these questions in sequence. Don't ask all at once. Let each answer shape the next question.

**a) Establish baseline**
- "What do you already know about <topic>?"
- "Have you done any projects in this area? Which ones?"
- "What made you want to learn this now?"

**b) Surface the core problem**
- "If you had to explain to a colleague what this field *solves*, what would you say?"
- Push back if it's vague: "That sounds broad — what's the hardest part specifically?"

**c) Build models iteratively**
- "Think of a time something worked well. Why did it work? What principle was operating?"
- "Think of a time it went wrong. What did you miss?"
- "If you had to name that pattern, what would you call it?"

For each model the user proposes:
- Ask: "What's a concrete example where this model applies?"
- Ask: "When does this model *fail* or mislead?"
- Ask: "What other model does this connect to or conflict with?"

When the user runs dry, suggest: "I think we have 3 models so far. Is there a fourth, or does this feel complete?"

**d) Surface controversies**
- "What do practitioners argue about in this field?"
- "Where do you find yourself disagreeing with common advice?"

### 3. Write memories

After the interview, write one file per model to `topics/<slug>/memory/`. Let the user's own words drive the content — you're sharpening, not replacing.

Memory file format (short, no frontmatter needed):
```markdown
# <Model Name>

**What it is:** <1-2 sentences>

**Why it matters:** <1 sentence — what decision does this model inform?>

**Example:** <1 concrete case, 2-3 lines>

**When it fails:** <boundary condition>

**Connects to:** [[other-model]], [[another-model]]
```

Also write `topics/<slug>/memory/_models.md` — a 3-4 line index of all models, like a table of contents.

### 4. Update README

Update `topics/<slug>/README.md` with current state. Keep it minimal:
```markdown
# <Topic>
- Slug: `<slug>`
- Started: <date>
- Models: N (list names)
- Last session: <date>
```

## Warnings

- Don't force 5 models. If the user surfaces 3 solid ones, stop.
- Don't write a model the user didn't earn. If they can't give a concrete example, it's not their model yet.
- Don't over-write. A model file should be readable in 30 seconds.
- Don't ask all interview questions at once. One at a time, let answers shape the next.
