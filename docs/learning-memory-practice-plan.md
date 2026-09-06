# Learning System Plan: Retrieval, Muscle Memory, and Memory Palaces

_Last updated: 2026-09-06_

## Analysis

The learning system currently emphasizes understanding, structured progression, and evidence of mastery, but it does not make repeated exposure a first-class course activity. That leaves high-frequency operational knowledge—such as tmux or Herdr shortcuts, command forms, and recovery sequences—to incidental recall. Learners may understand a lesson while still being slow or error-prone when using the tool.

Rote repetition is useful when the target is a small set of essential actions. It should be deliberate, spaced, and tied to real use, with feedback that distinguishes recognition from unaided recall and fluent execution. Memorization should support the mission rather than expand the syllabus indiscriminately.

The system also lacks a gradual introduction to memory-palace technique. An Agent can coach the learner through selecting familiar locations, assigning vivid retrieval cues, rehearsing them, and periodically testing recall. This should be an optional method introduced in small steps, then applied to high-value command groups rather than presented as a one-time explanation.

## Plan

### 1. Define a memory budget for each course

- During `/curriculum`, identify a short must-know set: commands, shortcuts, patterns, and recovery actions required for the mission.
- Classify each item as recognition, recall, or fluent execution; only the latter two receive active drills.
- Mark items as core, useful, or reference-only so memorization does not consume the whole course.
- Carry item identifiers, examples, and failure consequences into the syllabus and learner notes.

### 2. Add retrieval practice to `/learn`

- Introduce key items early, immediately after their first meaningful use.
- Run brief cold-recall prompts before showing answers: “What is the shortcut?”, “Type the command,” or “Recover from this state.”
- Mix recognition, free recall, and timed execution; require the learner to explain when an action is appropriate.
- Schedule revisits across later lessons and sessions, with shorter intervals after errors and longer intervals after reliable recall.
- Log attempts, errors, latency, and confidence in `notes.md`; promote stable items only after repeated successful retrieval in context.

### 3. Introduce a Memory-Palace coach

- Add an Agent-guided sequence that teaches one technique at a time: choose a familiar route, define fixed loci, create unusual associations, place a small command set, then walk and retrieve it.
- Start with 3–5 items and verify that the learner can reconstruct the route without prompts before adding more.
- Keep the palace tied to a command family or workflow (for example, session navigation, pane management, and recovery), not an undifferentiated list.
- Rehearse the palace through the same cold-recall and execution drills used elsewhere; treat imagery as a cue, not evidence of mastery by itself.
- Let the learner decline or replace the technique if it feels unnatural, while preserving ordinary spaced retrieval.

### 4. Show progress and keep scope visible

- Add a syllabus section listing must-know items, their target fluency, and the lesson/checkpoint where each is introduced and revisited.
- At each checkpoint, report before → after operational change, such as “Before: searches for the key binding. After: invokes it from memory in a live session and can recover when it fails.”
- In the first lesson, explain why these items matter, how they will be rehearsed, and which field knowledge remains reference-only.
- Surface due reviews at lesson openings without interrupting the main conceptual sequence.

### 5. Update contracts and verification

- Extend `/curriculum` and `/learn` contracts, syllabus format, and notes schema with memory-item and rehearsal fields.
- Add eval fixtures for command selection, cold recall, spaced retries, execution fluency, and the staged memory-palace introduction.
- Verify that errors change scheduling, answers are withheld until an attempt, and memorization claims require behavioral evidence.
- Document the workflow in the learning README and execution plan; keep it file-based and dependency-free.

## Acceptance Criteria

- Every tool-oriented course identifies a bounded must-know set and target fluency.
- Learners attempt essential shortcuts and commands from memory before seeing answers, across multiple later sessions.
- The system records recall and execution evidence and adapts review timing after errors.
- A learner can complete a staged 3–5 item memory-palace exercise, or continue with ordinary retrieval if they opt out.
- Syllabus and lessons show each memory checkpoint and its before → after operational outcome.
- Existing conceptual learning, survey, curriculum, and learn contract tests continue to pass.

## Implementation Status

Implemented as a unified contract update across `/survey`, `/curriculum`, `/learn`, `/recall`, and
`/practice`, with syllabus/notes/retrieval format changes, README and execution-plan documentation, and
expanded evaluation fixtures. The implementation remains file-based and dependency-free; no standalone
validator was added.
