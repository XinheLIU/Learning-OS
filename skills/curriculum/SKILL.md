---
name: curriculum
description: Turn a survey's learning mainline into a staged, resumable syllabus. Use when the user wants a study plan, a learning path, lesson sequencing for a topic, or says "/curriculum <topic>". Reads memory/survey.md; writes memory/syllabus.md, which /learn sessions execute lesson by lesson.
---

# Curriculum — Syllabus Designer

A standalone planner. Cognitive load and ICAP are the design inputs: sequence small chunks, automate parts before integration, and stamp every lesson with an engagement target and a load budget. Planning happens here so `/learn` can be a pure tutor.

## Inputs

Read `topics/<slug>/memory/survey.md`:
- **Learning mainline** → scope. The syllabus covers **DEEP subtopics only**. SKIM subtopics get at most a vocabulary warm-up inside a lesson; SKIP subtopics appear nowhere.
- **Prior-knowledge diagnosis** → depth. Novice subtopics get more Stage 1–2 lessons; practitioner subtopics may start at Stage 3.

If `survey.md` is absent, don't block: run a **3-question mini-diagnosis** ("What is this for, in your own words?" / "What have you built or read in it?" / "Which part feels most opaque?") and note in the syllabus header that it was built without a survey. Offer `/survey` for the full gate.

If `wiki/` pages exist for the topic, map lessons to them as reading material. Never write to `wiki/`.

## Output

Write `topics/<slug>/memory/syllabus.md`:

```markdown
---
layer: framework
---
# Syllabus: <topic>

<!-- source: survey.md <date> | mini-diagnosis (no survey) -->

## Stage 1 — Prerequisite schemas   (warm-up, automate parts)
## Stage 2 — Small chunks            (one new concept per lesson)
## Stage 3 — Combine schemas         (integration only after parts are fluent)
## Stage 4 — Real task               (whole-task, reduced support)
## Stage 5 — Transfer                (new domain, no support)
```

Each lesson under its stage:

```markdown
- [ ] Lesson <n>: <title>
  - Objectives: <1-2 lines, testable>
  - Prerequisites: <prior lessons / schemas assumed>
  - Warm-up: <retrieval of the prerequisite, 1 question>
  - Examples: <worked example or wiki/ page to use as material>
  - Exercise: <what the learner constructs>
  - Reflection prompt: <self-explanation question>
  - ICAP target: <P/A → C | C | C → I>
  - Load note: <what is deliberately deferred and why>
```

## Hard constraints

- **DEEP rows only.** Every lesson MUST trace to a DEEP mainline row.
- **Prerequisites before integration.** No Stage 3+ lesson may depend on a schema not covered in an earlier lesson. Order within stages by dependency, not by topic aesthetics.
- **One new concept per Stage 2 lesson.** If a lesson's objectives contain two new concepts, split it.
- **Every lesson carries an ICAP target and a load note.** No exceptions — these are what `/learn` calibrates against.
- **ICAP targets rise with the diagnosis:** novice subtopics start P/A → C; practitioner subtopics may start at C; C → I appears only in Stages 3–5.
- **Resumable:** lessons are checkboxes. `/learn` picks up at the first unchecked lesson and checks it off when its construction closes.

## Exit

Recommend `/learn <slug>` to start Stage 1. Update `topics/<slug>/README.md` last-session date.

## Contract test

Given a fixture `survey.md`: the syllabus covers DEEP rows only; every lesson carries an ICAP target and a load note; stage order respects prerequisites-before-integration.

## Boundaries

- vs `/survey`: survey decides **what** deserves time (strategic); curriculum decides **how** to sequence it (tactical). Curriculum never re-triages the mainline — if the mainline looks wrong, send the user back to `/survey`.
- vs `/learn`: curriculum plans; learn tutors. Curriculum never runs a lesson.
