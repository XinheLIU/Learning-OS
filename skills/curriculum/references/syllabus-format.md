# syllabus.html Format

_Last updated: 2026-07-17_

`learning/<slug>/syllabus.html` is the single course document, rendered as a browsable HTML page: mission, sources, and the staged lesson plan. `/curriculum` authors it; `/learn` only checks lessons off. Each lesson title is a live link into `lessons/*.html`, so the syllabus doubles as the course map. If it runs past what one screen per stage can hold, the course is over-scoped — cut lessons, don't grow the page. The Markdown template below is the *content* spec; `syllabus.html` renders that content as HTML (linking the shared stylesheet and `assets/math.js`), not as a `.md` file.

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

## Sources

- [{Title} — {author}]({url})
  {What it covers and when to reach for it. Which lessons use it.}
- …

### Gaps
- {Area the mission needs but no good source covers yet — drives future search}

## Stage 1 — Prerequisite schemas   (warm-up, automate parts)

- [ ] Lesson 1: {title}  [K]
  - Objective: {1 line, testable}
  - Prerequisites: {prior lessons / schemas assumed — "none" for lesson 1}
  - Lesson spec: {what the HTML contains — warm-up retrieval question; the one chunk;
    the worked example; which reference/ doc it creates or extends}
  - Primary source: {the single best source for this lesson, from ## Sources}
  - ICAP target: P/A → C
  - Load note: {what is deliberately deferred and why}

## Stage 2 — Small chunks            (one new concept per lesson)
## Stage 3 — Combine schemas         (integration only after parts are fluent)
## Stage 4 — Real task               (whole-task, reduced support)
## Stage 5 — Transfer & wisdom       (new domain, no support, real world)
```

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

Every lesson block carries all six fields — type, objective, prerequisites, spec, primary source, ICAP target, load note. The spec must be concrete enough to author the HTML lesson from directly — and for `/learn` to judge, later, whether the built lesson still fits the learner:

- **[K]** spec names the worked example and the `reference/` doc it creates or extends.
- **[S]** spec names the interactive exercise (quiz / in-browser task), what feedback it gives, and which prior schemas it interleaves.
- **[W]** spec names the real-world assignment or the high-reputation community to engage, and what the debrief next session covers. If the user has opted out of communities (see `notes.md` Preferences), design a solo real-world assignment instead.
