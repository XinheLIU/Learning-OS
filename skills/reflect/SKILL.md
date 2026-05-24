---
name: reflect
description: Look back on cases and models to calibrate, surface gaps, and decide what's next. Use when the user finishes a project, after several practice sessions, when models feel off, or says "/reflect <topic>". Replaces the old frame-calibrate + project-retro + manual-check pipeline.
---

# Reflect

Periodic recalibration. Look at what's been practiced, check if the models hold, surface what's missing, and decide what to work on next. This is the meta-learning loop — it keeps the knowledge base alive rather than a frozen snapshot.

## Philosophy

- **Models decay if not challenged.** Every model file should be re-read with fresh eyes against recent cases.
- **Gaps are more important than confirmations.** Knowing what you *haven't* practiced is more actionable than what you have.
- **Short session, sharp questions.** A reflect session should take 10-15 minutes, not an hour.
- **Don't rewrite everything.** Touch only what's wrong, stale, or missing.

## Flow

### 1. Gather state

Read all files in `topics/<slug>/memory/`:
- `_models.md` (index of all models)
- All `model-*.md` files
- All `case-*.md` files

Count cases, check dates, note which models have been used and which haven't.

### 2. Three questions

Ask these in order:

**a) "Since our last session, what's the most surprising thing you learned?"**
- Surprise means a model was wrong or incomplete. Probe it.
- If nothing was surprising, ask: "What was harder than you expected?"

**b) "Look at our models. Which one feels the weakest right now?"**
- Weak = you couldn't confidently apply it to a new case.
- Weak = you've never actually used it in practice.
- Weak = the boundary conditions are vague.

**c) "What kind of problem are you avoiding?"**
- This surfaces practice gaps. If all cases are classification and none are time series, that's a gap.

### 3. Update models

For any model that needs adjustment:
- Read the current `model-*.md` file
- Ask the user: "What's changed? Sharper boundary? New example? The model doesn't hold at all?"
- Edit the file minimally — don't rewrite working content
- Add a `**Revised:** <date> — <what changed>` line at the bottom

If a model is dead (proven wrong by cases), don't delete it. Move it to an `**Archived:** <reason>` section at the bottom of `_models.md` — the history of wrong models is valuable.

### 4. Surface gaps

Summarize:
- "You've practiced <X> 3 times but never <Y>."
- "Your models cover <A, B, C> but there's nothing for <D>."
- "All your cases are from <domain>. Want to try a <different domain> case?"

Then ask: "What's the next thing you want to practice?" and suggest 2-3 concrete scenarios.

### 5. Update README

Update `**Last session:** <date>` in `topics/<slug>/README.md`.

## When to suggest synthesizing

After 5+ cases and 2+ reflect sessions, mention: "You've built enough to start forming your own position. Want to write a personal playbook for this domain?" If yes, guide the user through writing `topics/<slug>/memory/position.md` (their stance on key controversies) and `topics/<slug>/memory/playbook.md` (their repeatable method). This replaces the old `/playbook` and `/framework-compare` — one conversation, not two commands.

## Warnings

- Don't do a reflect session with 0 cases. It's just navel-gazing.
- Don't rewrite models for minor wording. Only touch what's substantively wrong.
- Don't suggest synthesizing too early. Less than 5 cases = not enough data.
