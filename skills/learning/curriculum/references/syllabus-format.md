# syllabus.md Format

_Last updated: 2026-09-06_

`learning/<slug>/syllabus.md` is the single course document and the source of truth for the plan and progress: mission, sources, and the staged lesson plan. `/curriculum` authors it; `/learn` checks lessons off at bookkeeping; `/evaluate` closes Stage 4–5 loop-entry checkboxes. `index.html` renders it directly via `assets/progress.js` — there is **no `syllabus.html`** (eliminated in v2; one source of truth, no three-way sync). Each lesson title links into `lessons/*.html`, so the shell doubles as the course map. If it runs past what one screen per stage can hold, the course is over-scoped — cut lessons, don't grow the page.

## Full template

```markdown
# Course: {Topic}

<!-- source: survey.md {date} | mini-diagnosis (no survey) -->

## Mission

**Why:** {1–3 sentences. The concrete real-world goal. What changes in the user's
life or work when they have this? Avoid "to understand X" — push for the outcome.}

**Success looks like:**
- {A specific, observable thing the user will be able to do}
- {Another}

**Constraints:** {time, budget, prior commitments, learning preferences}

**Out of scope:** {adjacent topics explicitly deferred — protects focus}

## Mission Contract & Roadmap

When `survey.md` exists, carry its decisions into the syllabus rather than silently re-diagnosing:

- **Baseline evidence:** {work, reading, performance, or probe}
- **Why now:** {concrete relevance}
- **Capability gap:** {current state → desired state}
- **Non-goals:** {explicit cuts}
- **Remaining uncertainty:** {what is unresolved}

### Roadmap
- **Whole field:** {useful orientation}
- **Critical path:** {selected sequence}
- **In scope:** {topics}
- **Deferred / skipped:** {topics and reason}

### Checkpoints
- **CP1:** Before: {baseline capability}. After: {observable change}.
- **CP2:** Before: {baseline capability}. After: {observable change}.
- **CP3:** Before: {baseline capability}. After: {observable change}.

Use 3–5 checkpoints and preserve their identifiers in lesson specs.

## Memory Budget

For tool-oriented courses, list only the bounded operational set that merits active rehearsal:

| id | item | class | mode | example | failure consequence | target fluency | introduced | revisited |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| {id} | {command / shortcut / pattern / recovery action} | core | recognition / recall / execution | {example} | {consequence} | {target} | {lesson} | {lessons or sessions} |

## Sources

- [{Title} — {author}]({url})
  {What it covers and when to reach for it. Which lessons use it.}
- …

### Gaps
- {Area the mission needs but no good source covers yet — drives future search}

## Stage 1 — Prerequisite schemas   (warm-up, automate parts)

- [ ] Lesson 1: {title}  [K]
  - Cell: {mainline × stage, from the survey matrix — omit when no survey exists}
  - Objective: {1 line, testable}
  - Prerequisites: {prior lessons / schemas assumed — "none" for lesson 1}
  - Opening task: {a micro-task in the real environment executed *before* explanation}
  - Lesson spec: {what the HTML contains — opening task; warm-up retrieval question
    (none for lesson 1); the one chunk; the worked example; the 1–2 check-yourself
    items; which reference/ doc it creates or extends}
  - Primary source: {the single best source for this lesson, from ## Sources}
  - ICAP target: P/A → C
  - Load note: {what is deliberately deferred and why}
  - Next: {what the checkpoint's next-step card says — e.g. "Lesson 2", or
    "recall first if queue > 5", or "bring a real case to /practice"}

## Stage 2 — Small chunks            (one new concept per lesson)

- [ ] Lesson 4: {title}  [S]
  - Cell: {mainline × stage}
  - Objective: {1 line, testable}
  - Prerequisites: {prior lessons / schemas assumed}
  - Interleaves: {≥1 schema from a NON-ADJACENT prior lesson, named — e.g. "two-state-machine (L1)"}
  - Opening task: {a micro-task in the real environment executed *before* explanation}
  - Lesson spec: {the exercise, the feedback it gives, how the interleaved schema is mixed in}
  - Primary source: {the single best source for this lesson, from ## Sources}
  - ICAP target: C → I
  - Load note: {what is deliberately deferred and why}
  - Next: {what the checkpoint's next-step card says}

## Stage 3 — Combine schemas         (integration only after parts are fluent)
## Stage 4 — Real task               (whole-task, reduced support — loop-entry specs from here on)
## Stage 5 — Transfer & wisdom       (new domain, no support, real world — loop-entry specs)
```

Stage 4–5 entries are **loop-entry specs, not lessons**: same checkbox and fields, but no `lessons/*.html` file is authored for them. Their checkbox is closed by `/evaluate` when `/practice` evidence reaches the named cell — never by a tutoring session.

## Mission rules

- **One mission per topic.** Two unrelated goals → two topics under `learning/`.
- **Concrete over abstract.** "Ship a Rust CLI to my team" beats "learn Rust"; "run a half marathon by October" beats "get fitter".
- **Push back on vagueness.** If the user cannot articulate why, interview before planning anything. A bad mission is worse than no mission — it steers every lesson wrong.
- **Revise when reality shifts.** When `/learn` records a mission shift in `notes.md`, the user comes back here; update the Mission and re-plan affected stages. Don't leave a stale mission steering sessions.
- **Keep it short.** If the Mission section runs past a screen, it has stopped being a compass and started being a plan.

## Sources rules

- **High-trust only.** Primary sources, recognised experts, peer-reviewed work. If it's marketing dressed as education, leave it out. Never trust parametric knowledge alone.
- **Annotate every entry.** A bare link is useless in three months — one line on what it covers and when to reach for it.
- **Surface gaps explicitly.** The `### Gaps` section drives future search; an empty gaps section on a fresh course is suspicious.
- **Prune ruthlessly.** A source that turned out wrong, shallow, or off-mission is removed, not buried. Five sharp sources beat thirty mediocre ones.
- When a survey exists, this section is distilled from its Read list — don't re-research.

## Lesson-spec rules

Every lesson block carries its fields — type, objective, prerequisites, opening task, spec, primary source, ICAP target, load note — plus the matrix cell it serves when a survey exists, `Interleaves:` on every `[S]` lesson, and a `Next:` pointer. The spec must be concrete enough to author the HTML lesson from directly — and for `/learn` to judge, later, whether the built lesson still fits the learner:

- **[K]** spec names the worked example, the 1–2 check-yourself items, and the `reference/` doc it creates or extends.
- **[S]** spec names the interactive exercise (quiz / in-browser task), what feedback it gives, and which prior schemas it interleaves. The `Interleaves:` field is mandatory and names ≥1 schema from a **non-adjacent** prior lesson. Retrieving the lesson immediately before is fluency practice — the material is still warm — so it does not satisfy the field. Absent, empty, or adjacent-only is a contract violation, not a warning.
- **[W]** spec is a loop-entry: it names the real-world assignment or the high-reputation community to engage, the shape of the real case to bring to `/practice`, and what the debrief covers. No HTML lesson is authored for it; `/evaluate` closes its checkbox on evidence. If the user has opted out of communities (see `notes.md` Preferences), design a solo real-world assignment instead.
- **Opening task is hands-on** — a command to run, a small variant to try, observing output before explanation. Not "think about X" or "read this" — do first, explain second. It is the first thing in the lesson HTML, before the warm-up.
- **`Next:`** names what the checkpoint block's next-step card says: the following lesson, a recall gate ("recall first if queue > 5"), or a handoff ("bring a real case to `/practice`" at a mainline close). One line; the checkpoint card quotes it verbatim.
- **`Gate:` (optional)** — a condition that must hold before this lesson starts, expressed against the recall queue (e.g. "start only when due items < 5"). `/learn` checks it at `start` and routes the learner to `recall.html` first when it isn't met.
- **`Checkpoint:`** — the `CP<n>` outcome this lesson advances.
- **`Capability delta:`** — the observable `Before → After` change expected from this lesson.
- **`Memory items:`** — operational-memory IDs rehearsed or introduced, when applicable.
- The first lesson must orient the learner with the mission, baseline, target output, full roadmap,
  out-of-scope areas, rehearsal method, and next checkpoint before new material.
