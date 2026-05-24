---
name: practice
description: Apply mental models to a concrete scenario. Use when the user faces a specific problem, wants to work through a case, describes a situation they're stuck on, or says "/practice <scenario>". Replaces the old schema-card + mechanism-map pipeline.
---

# Practice

Apply known mental models to a concrete problem. The AI helps the user work through a real scenario, maps it to models, and saves the case. If no model fits cleanly, that's valuable signal — a model may be wrong or a new one is emerging.

## Philosophy

- **Work on real cases, not hypotheticals.** The user should bring something they actually encountered.
- **The AI asks, doesn't prescribe.** "Which model do you think applies here?" before "I think X applies."
- **Failure is data.** If a model fails to explain the case, that's more valuable than a clean fit.
- **Short case files.** One case, one file. Readable in 60 seconds.

## Flow

### 1. Load context

Read `topics/<slug>/memory/_models.md` to know what models exist. If no models exist yet, say: "No models yet for <slug>. Want to `/learn` first, or should we work through this and extract models as we go?"

### 2. Understand the scenario

Ask the user to describe the situation concretely:
- "What happened? What were you trying to do?"
- "What did you try? What worked, what didn't?"
- "What's the specific moment where you got stuck or things went wrong?"

Don't let them stay abstract. "Data loading is slow" → "Show me the pipeline. What's the bottleneck?" Push for specifics.

### 3. Map to models

- "Looking at our models for <slug>, which one(s) do you think apply here?"
- If the user's unsure: "Here's what I see. <Model X> seems relevant because <reason>. Does that feel right?"
- If no model fits: "This doesn't cleanly match any of our models. That might mean we're missing one — want to name what's operating here?"

### 4. Work through it

Apply the model(s) to the problem:
- "Given <Model X>, what's the standard move here?"
- "What's the risk of that approach in this specific case?"
- "Is there a second model that suggests a different move?"

If the user wants to go deep on one model (old "mechanism map" territory), do it here — draw the mechanism, walk through boundary cases, find edge cases from the user's own experience.

### 5. Capture the case

Write `topics/<slug>/memory/case-<short-slug>.md`:

```markdown
# Case: <Title>

**Date:** <today>
**Scenario:** <2-3 lines — what happened, what was at stake>
**Models applied:** [[model-1]], [[model-2]]
**What worked:** <2-3 lines>
**What didn't / surprised:** <2-3 lines>
**Takeaway:** <1 line — what would you do differently next time?>
```

### 6. Check models

After the case, ask:
- "Did <Model X> hold up, or did this case reveal a crack in it?"
- If the model needs updating, update `topics/<slug>/memory/<model-slug>.md` and note the change.

Signal to escalate: if a case reveals a model is wrong or incomplete, suggest `/reflect <slug>` to recalibrate.

## Warnings

- Don't write a case for something trivial. If the user solved it in 30 seconds, there's no pattern worth capturing.
- Don't force a model onto a case. A clean "none of our models fit" is more honest than a stretched fit.
- Don't go deep on mechanism unless the user wants to. Some cases just need a quick model match.
