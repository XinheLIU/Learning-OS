---
name: evaluate
description: Evidence-backed mastery snapshot for a topic. Use when the user asks how well they know something, wants a mastery check, a progress assessment, or says "/evaluate <topic>". Read-mostly - assigns rubric levels (can-recall to can-generate) only where evidence files support them. Never numeric scores.
---

# Evaluate — Learning Evaluator

A standalone, read-mostly assessor: a snapshot of **how deep mastery actually is**, separate from the feedback loop. The core discipline is *evidence before claims* — a level may only be claimed with a pointer to an evidence file. Self-reported competence doesn't count.

## Rules

- **No numeric scores, ever.** "Schemas 92%" is LLM confabulation. Rubric levels with evidence only.
- **Read-mostly.** The only write is the Mastery Snapshot section in `notes.md`. No record edits, no recommendations engine — that's `/reflect`.
- **No evidence → lowest supportable level.** When in doubt, round down.

## The rubric

| Level | Evidence required |
| :--- | :--- |
| can-recall | correct restatement in session |
| can-apply | a `case-*.md` where the model was used successfully |
| can-transfer | a case from a *different* domain |
| can-teach | learner explanation that survived tutor challenge (ICAP-I) |
| can-generate | a `/research` report (judgment + so-what) or novel model |

Levels are cumulative — claiming `can-transfer` implies `can-apply` evidence exists too.

## Flow

### 1. Gather evidence

Read everything in `learning/<slug>/`: `notes.md` (records + terms — the earned nodes), `syllabus.md` (checked lessons), all `case-*.md`, any `research-*.md`. Build the map: which cases used which records (via Models-applied fields), which explanations survived challenge, which research outputs exist.

### 2. Assess per node

For each knowledge node (every record and term in `notes.md`):
- Find the strongest level the evidence supports; record the pointer.
- For `can-recall` where no session evidence exists, you MAY probe live: "In one line, what does <model> say?" — one question per node, no tutoring here.
- A node with no evidence at all is reported as **unassessed**, not zero.

### 3. Write the snapshot

- In `notes.md`, write/replace a summary section:

```markdown
## Mastery Snapshot — <date>
| Node | Mastery | Evidence |
| :--- | :--- | :--- |
| record 0003 (model X) | can-transfer | case-y (different domain) |
| term: <schema Z> | can-recall | restated this session |
| record 0005 (model W) | unassessed | — |

**Depth distribution:** N terms · N schemas/models · N frameworks (playbook, research)
```

### 4. Report the depth gauge

State the depth distribution and what it means: notes that are mostly terms are vocabulary, not understanding; mastery concentrated at `can-recall` means models were filed but never used. One or two sentences — the trajectory response belongs to `/reflect`.

Suggest `/reflect <slug>` if the snapshot shows drift or stagnation.

## Contract test

Given fixture models + cases: every claimed mastery level cites an evidence file; nodes without evidence stay at the lowest supportable level; output contains no percentages.

## Boundaries

- vs `/reflect`: **evaluate measures state; reflect changes trajectory.** Evaluate never edits models, never sets micro-goals, never writes the playbook. Reflect consumes this snapshot but never writes mastery levels itself.
- vs `/practice`: practice produces the evidence; evaluate only reads it.
