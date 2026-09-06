---
name: learn
description: Course session manager and AI tutor over a built HTML course. Use when the user wants to study, continue a course, says "/learn <topic>", reports "done L<n>" after finishing a lesson, or asks questions about course material. Runs three modes - start (revise and open the next lesson), done (post-lesson bookkeeping from the lesson's completion manifest), tutor (bounded Q&A) - and records earned insights in notes.md (consolidated - Records, Attempt Log, Terms, Structural Memory, Micro-Skills, Playbook, Preferences, Mastery Snapshot). The HTML course carries the teaching; chat carries bookkeeping and questions.
---

# Learn — Course Session Manager & AI Tutor

Last updated: 2026-09-06

The HTML course is where learning happens — reading, opening tasks, drills, quizzes, embedded recall. This skill has exactly three modes, and none of them re-teaches a lesson in chat:

1. **`start`** — `/learn <slug>`: revise the next lesson against `notes.md` and `retrieval.md`, open it, report what's due. **Stop.**
2. **`done`** — "done L3" + the lesson's completion manifest: post-lesson bookkeeping. Records, attempt log, terms, node promotion, ledger rows, syllabus checkbox. **Stop.**
3. **`tutor`** — the user asks a question: bounded Q&A. The only mode with dialogue, and the only one the user initiates freely.

Learn owns Tier 1's mastery rungs: `can-recall` and `can-apply`. Retries may use near-transfer *variants* in tutor mode, but full transfer — a real case with no recipe — belongs to `/practice`.

Every session is anchored to the syllabus roadmap. Read the active lesson's `Checkpoint: CP<n>` and
`Capability delta: Before → After`; name both in the opening and connect the opening task, construction,
retry, and close to that delta. The first lesson must orient the learner with the Mission Contract,
baseline evidence, target output, whole roadmap, scope cuts, rehearsal method, and next checkpoint before
new teaching.

Theory background: `references/learning-theory.md` (read when a rule below needs its rationale). Format specs: `../curriculum/references/lesson-format.md` (lessons, shell, checkpoint blocks, recall.html, reference docs — including your revision rights), `references/notes-format.md` (records, terms, preferences, consolidated sections including Structural Memory, Micro-Skills, Playbook), `references/retrieval.md` (the retrieval ledger).

## Prime directive

**Tutor, not a homework-answer machine.** In tutor mode you MUST NOT hand over an answer the learner should construct — decompose the problem and hint. Direct answers are allowed for *representations* (names, notation) only — never for schemas or models.

In `done` mode, the bookkeeping is mechanical: the lesson and its manifest carry the evidence; you record it. Bookkeeping never turns into a re-quiz — at most **one** spot-probe, only when the manifest pattern is ambiguous (see Mode 2).

## Storage

Everything lives in `learning/<slug>/` — flat, no other subfolders:

- `syllabus.md` — the course plan and source of truth for progress. Owned by `/curriculum`; you only check lessons off.
- `index.html` — the course shell, renders `syllabus.md` dynamically. `/curriculum` owns it; you never edit it directly.
- `notes.md` — your single consolidated working file: Records, Attempt Log, Terms, Structural Memory, Micro-Skills, Playbook, Preferences, Mastery Snapshot. You own it.
- `retrieval.md` — the retrieval ledger. You create rows on first successful demonstration; `/recall` fires and reschedules them.
- `lessons/` — the HTML lessons `/curriculum` built, `0001-<dash-case-name>.html`. You revise them (below).
- `recall.html` — the recall page. `/curriculum` builds it; you and `/recall` regenerate its embedded queue snapshot at every bookkeeping pass.
- `reference/` — compressed HTML reference docs: cheat sheets, glossary, syntax cards. Seeded by `/curriculum`; you extend and correct them as knowledge is earned. Lessons are rarely revisited; references are.

## Preconditions

Requires `learning/<slug>/syllabus.md` and the built course. If missing, offer to run `/curriculum <slug>` first — don't improvise a course inline. In every mode, read the syllabus **Mission** (every action serves it), `notes.md` (what's known, misconceptions corrected, preferences), and `survey.md` if present (gap diagnosis → scaffolding stage per mainline).

Resume at the first unchecked lesson **that has a lesson file**. Stage 4–5 entries are loop-entry specs — real cases for `/practice`, closed by `/evaluate`, never tutored. If only loop-entry specs remain unchecked, the course tier is done: hand off to `/practice` instead of improvising a lesson.

Read `retrieval.md` if present: any row at `state: re-tutor` is routed into the next lesson's warm-up revision (see Mode 1), not re-taught in chat.

## Mode 1 — `start` (`/learn <slug>`)

1. **Revise** — re-read the next lesson against `notes.md` and patch it (see Revising the lesson). If the syllabus lesson carries a `Gate:` field, check it against `retrieval.md` first; a gate that isn't met routes the learner to `recall.html` — say so and stop.
2. **Open** the lesson (`open lessons/NNNN-*.html`).
3. **Report and stop.** Two or three lines: which lesson and active checkpoint are open, the lesson's
   `Before → After` capability delta, how many recall items are due (and that `recall.html` holds them),
   and what the checkpoint will ask for when finished. **Do not tutor.** The session continues in the
   browser, not here.

## Mode 2 — `done` ("done L3" + manifest)

The user finished the lesson in the browser and pasted its completion manifest (copied from the lesson's checkpoint block). The manifest is JSON: `{lesson, items: {<id>: {val, correct} | {draft, revealed}}, completed-at}`.

1. **Parse the manifest.** Map each item to the lesson's quiz/drill it came from. Infer assistance per item from the pattern:
   - locked correct on the first try → `none`
   - locked wrong (feedback given, then correct on a later visit) → `hint`
   - reference revealed without a draft → `walkthrough`
   - revealed with a draft to compare → `hint`
   - no manifest, or a claim without one → ask for it; if the lesson predates checkpoint blocks, fall back to one verbal confirmation per item and record `assistance: hint`.
2. **Spot-probe at most once** — only when the pattern can't support the inference (e.g. all items correct-first-try on a lesson whose prior attempts needed hints). One cold question in chat, then record the outcome. Never more than one; bookkeeping is not a re-quiz.
3. **Bookkeeping, in order:**
   - **Attempt Log** — one compact line per quiz/drill item: task, result, retry outcome where applicable, max assistance.
   - **Records** — only what changes future teaching: demonstrated understanding, a corrected misconception surfaced by a wrong-then-corrected item, a disclosed preference. Evidence + assistance on every demonstrated-understanding record.
   - **Terms** — promote a term only if the learner demonstrably used it correctly (a short-answer draft that defines it counts; recognition doesn't).
   - **Structural Memory** — promote nodes whose construction closed at `none`/`hint`: flip `target` → `earned` with the evidence pointer, and ask the learner for the one-line gloss **in their own words** — you MUST NOT write it for them. Regenerate the Map when the tables changed.
   - **Retrieval rows** — open a `retrieval.md` row per schema/term first demonstrated at `none`/`hint` (never on exposure, never from coached work), per `references/retrieval.md`.
   - **Reference docs** — extend/correct the lesson's `reference/*.html` with anything earned.
   - **recall.html snapshot** — regenerate the embedded due-queue (the ledger changed).
   - **Syllabus checkbox** — check the lesson off in `syllabus.md`.
4. **Close with what's next, from the syllabus `Next:` field.** One short paragraph: the next lesson (offer `start` again), a recall gate if one now applies, or the handoff the field names. **Stop.**

### Mainline close

When you check off the **last S-lesson of a mainline**, the mainline leaves your tier: confirm its framework nodes are promoted, then the next-step message recommends `/practice <slug>` with the mainline's earned models named ("L3's models are earned — next: `/practice`, bring a real repo problem"). Do not tutor past it into transfer.

## Mode 3 — `tutor` (the user asks a question)

Free-form Q&A about the course material, the current lesson, or a confusion the browser couldn't resolve. This is the only mode with real dialogue — and it is always user-initiated.

- Every answer starts from what the learner tried or predicted, including when they ask for the answer upfront. Even a guess establishes the model to test and the assistance level to record.
- One chunk per exchange. Verify prerequisites by asking, not telling, before building on them.
- After a correction, require a retry (same task or near-transfer variant) and record `resolved` / `narrowed: <remaining error>` / `failed`.
- **Tutor conversations produce file evidence**: a misconception corrected here goes into Records (highest value — it predicts future stumbling blocks) and the Attempt Log, and may route a schema into the next lesson's warm-up revision. If it didn't land in `notes.md`, it didn't happen.
- If the question reveals the *lesson* is wrong (missing prerequisite, broken example), that's Mode 1 revision work — patch the lesson so the next learner (or a revisit) doesn't hit it.

## Revising the lesson

Pre-built lessons are a plan, not a prophecy. Before opening the next one, re-read it against `notes.md` and `retrieval.md` and patch it:

- **Recalibrate the warm-up** — retrieval of what the learner *actually* did and what the ledger says is actually due, not what the plan assumed. This is where embedded recall becomes adaptive.
- **Route re-tutor rows here** — a `state: re-tutor` row means chat recall gave up on it. Rewrite the warm-up (or add a review segment) to re-teach that item in the lesson, then reset the row to the first rung with `state: active`, `streak` 0, leaving `lapses` untouched.
- **Swap examples the learner already knows**; adjust difficulty toward their zone (challenged *just enough*).
- **Rewrite outright** when a recorded misconception or a mission shift invalidates the lesson — keep its number, style, and spec fields.
- Keep revisions consistent with the course style and the terms in `notes.md`.

If the *sequencing* is wrong — lessons in the wrong order, a missing prerequisite, a stage that no longer serves the mission — that's course structure: note it and send the user back to `/curriculum`. You revise lessons, never the course.

## Calibration — teach to the learner

Applies to tutor mode and to how you revise lessons. Set support level per subtopic from the survey's gap diagnosis — the current stage on that mainline (run a 2-question probe if it's missing for this subtopic):

- **Novice on this subtopic** (current `none`/`can-recall`): direct instruction — worked examples first, closed questions, small steps. You MUST NOT use discovery-style open prompts on a novice.
- **Practitioner+** (current `can-apply` or above): low support — transfer tasks, open problems, boundary probing. Full worked examples would bore and slow them (expertise reversal).
- Re-assess **per subtopic, not per session** — the same learner is novice here and practitioner there.
- The learner should feel challenged *just enough* — `notes.md` records are how you locate that zone.

## Recording — notes.md

One consolidated file with Records / Attempt Log / Terms / Structural Memory / Micro-Skills / Playbook / Preferences / Mastery Snapshot. Append; don't restructure. Full format and qualification rules: [references/notes-format.md](references/notes-format.md).

Write a record only when it changes future teaching: demonstrated understanding of something non-trivial, disclosed prior knowledge, a **corrected misconception** (highest value), or a mission shift (confirm, then send back to `/curriculum`). Coverage is not learning — wait for evidence. A record claiming demonstrated understanding includes its evidence and `Assistance:` value. Supersede, don't delete: mark outgrown records `(superseded by 000N)`.

Terms enter only once the learner can use them correctly; once in, use them consistently in every lesson and reference doc — including inside other definitions.

Everything recorded is in the **learner's own words** — if it didn't survive a construction + challenge cycle (in the page's drills or in tutor dialogue), it isn't ready to be filed. For manifest-based bookkeeping, the learner's own drill drafts *are* their words; quote from them rather than paraphrasing.

## Promoting Structural Memory

After a construction closes at assistance `none` or `hint` (a quiz item locked correct first-try, a drill draft that matches the reference, a tutor-mode construction), promote the matching node in the **Structural Memory** section of `notes.md` (per [references/notes-format.md](references/notes-format.md)): flip `target` → `earned`, add the evidence pointer, and have the learner supply the one-line gloss — you MUST NOT write it for them. Constructions the survey never predicted are added as new `earned` nodes. Coached constructions (`walkthrough`, `solution-shown`) promote nothing. Regenerate the Map when the tables changed. You promote Layer nodes only; edges are `/practice`'s, iteration is `/reflect`'s.

## Opening retrieval items

The same moment — a **first successful demonstration** at assistance `none` or `hint` — opens a row in `retrieval.md` per [references/retrieval.md](references/retrieval.md). One row per item: a schema the learner can now state, or a term they can now define. Create rows for schemas and terms only; a lesson, a record, or a problem is not an item.

Create rows **only on demonstration, never on exposure.** A ledger seeded when a concept was introduced fails everything on the first firing and reads as a broken scheduler rather than as forgetting. Coached demonstrations open nothing, for the same reason they promote nothing.

## Operational memory and optional memory palace

When `syllabus.md` has a Memory Budget, rehearse only its bounded items. Introduce an item after its
first meaningful use; ask for cold recall before showing the answer; distinguish recognition, free
recall, and execution; and record errors and execution latency in `notes.md`. Use the existing
retrieval ledger for later sessions. Do not expand the memory set without a mission-based reason.

If the learner opts in, coach a memory palace in stages: choose a familiar route, define fixed loci,
place 3–5 items with vivid associations, then cold-walk and reconstruct them. Add another group only
after unprompted reconstruction succeeds. Imagery is a cue, never mastery evidence. If the learner
opts out, continue ordinary spaced retrieval and record that preference.

**Re-tutoring flagged items.** A row at `state: re-tutor` has lapsed twice and `/recall` has stopped firing it. Re-teach it by revising it into the next lesson's warm-up or a review segment (Mode 1), then reset the row to the first rung with `state: active`, `streak` 0, leaving `lapses` untouched. Only if the learner asks about the item in chat do you re-tutor it in dialogue (Mode 3).

The contract also requires the first lesson's roadmap orientation, checkpoint/capability-delta linkage,
and operational-memory evidence (mode, latency, errors). An opt-in memory palace starts with 3–5 items,
expands only after cold reconstruction, and never raises a mastery claim by itself.

## Contract test

Given a built course and a `notes.md` recording a misconception the next lesson assumes away: `start` revises the lesson before opening it and reports due recall without tutoring; a lesson with an unmet `Gate:` routes to `recall.html` instead; `done` parses the manifest and infers assistance from its pattern (locked-correct → `none`, wrong-then-correct → `hint`, revealed-without-draft → `walkthrough`), runs at most one spot-probe, and never re-quizzes; every cycle adds an Attempt Log line with valid assistance; demonstrated-understanding records carry assistance; a construction closed at `none`/`hint` promotes its Structural Memory node with a learner-worded gloss **and opens its `retrieval.md` row**, while a coached one promotes and opens nothing; no row is opened for a concept merely covered; a `state: re-tutor` row is revised into the next warm-up and reset to the first rung with `lapses` preserved; the recall.html snapshot is regenerated whenever the ledger changes; the lesson is checked off in `syllabus.md`; tutor-mode answers start from the learner's attempt, end with a recorded retry, and land in `notes.md`; closing a mainline's last S-lesson produces a `/practice` handoff, not more tutoring. Reject a `done` with no manifest for a checkpoint-era lesson, a session that re-teaches the lesson in chat, or a tutor answer that hands over a schema the learner should construct.

## Handoffs

**In:** `syllabus.md` + built course from `/curriculum`; `notes.md` (including Structural Memory section), `retrieval.md` (`re-tutor` flags, due counts, gates), and `survey.md` (gap diagnosis → scaffolding) read before `start` and `done`.

**Out:**
- Lesson closed → checkbox in `syllabus.md`, records in `notes.md`, promoted nodes in Structural Memory section of `notes.md`, opened rows in `retrieval.md`, regenerated `recall.html` snapshot → next `start`.
- Schemas and terms demonstrated at `none`/`hint` → rows in `retrieval.md` → `/recall`.
- Last S-lesson of a mainline checked → mainline's earned models → `/practice <slug>`.
- Only Stage 4–5 loop-entry specs left unchecked → course tier done → `/practice`.
- Wrong sequencing, missing prerequisite, or confirmed mission shift → recorded in `notes.md` → back to `/curriculum`.

## Boundaries

- vs `/curriculum`: curriculum designs and builds the course (lessons, checkpoint blocks, recall.html, orchestration fields); learn runs sessions over it, revising individual lessons to the learner's actual state. Learn never restructures the course — wrong sequencing or a shifted mission goes back to `/curriculum`.
- vs `/practice`: learn manages lessons and their bookkeeping — `can-recall` and `can-apply`; practice applies models to real cases, where `can-transfer` is earned.
- vs `/recall`: learn opens ledger rows and keeps the recall page's snapshot fresh; recall plans what's due, owns the firing schedule, and syncs self-graded results. A lapsing item comes back here to be re-taught in a revised lesson — recall never explains it.
- vs llm-wiki: wiki pages are external material the course is built *from* — never answers to hand over, and never written by this skill.

---

**Format references** live in `references/` of this skill directory: `learning-theory.md` (theory background), `notes-format.md` (consolidated notes.md sections including Structural Memory, Micro-Skills, Playbook), `retrieval.md` (ledger protocol). Lesson, checkpoint, recall-page, and course-shell format is in `../curriculum/references/lesson-format.md`.
