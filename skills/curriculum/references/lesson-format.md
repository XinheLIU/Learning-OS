# Course HTML Format — Shell, Lessons & Reference Docs

What `/curriculum` authors: the course shell (`index.html`), interactive lessons in `learning/<slug>/lessons/`, and reference docs in `learning/<slug>/reference/`. `/learn` tutors over these files and **revises** them when the learner diverges from the plan. Lessons are rarely revisited; references are — design accordingly.

## Course shell — `index.html`

One page rendering the course: mission, stages, and the lesson list with links. It is the front door the user opens between sessions.

- Mirrors `syllabus.md` — same stages, same lesson titles, same order. When one changes, the other is updated in the same session (the shell is a *view*; `syllabus.md` stays the source of truth for progress).
- Shows progress: completed lessons visibly distinct from upcoming ones (`/learn` updates this as it checks lessons off).
- Establishes the course's shared style — a `<style>` block every lesson reuses, so the course looks like one course, not a pile of one-offs.

## Lessons — `lessons/0001-<dash-case-name>.html`

One self-contained HTML file per lesson, numbered in syllabus order, authored from the lesson's spec and grounded in its primary source.

**Every lesson MUST:**

- **Teach one tightly-scoped thing** tied to the mission, completable in one sitting — one chunk, one tangible win.
- **Open with the warm-up** — a retrieval question from a *prior* lesson (spacing), before the new material.
- **Be beautiful.** Clean, readable typography and layout; think Tufte. Reuse the shell's style.
- **Name its primary source** — the single highest-trust resource for this topic, from the syllabus — and cite sources inline for every substantive claim (citations are what make a lesson trustworthy).
- **Anchor-link** the course shell, related lessons, and `reference/` docs.
- **End with a follow-up reminder:** the agent is the tutor — ask it anything unclear.

**Per K/S/W type:**

| Type | The HTML contains |
| :--- | :--- |
| **K** | Worked example first; the one new concept, minimally loaded; links its `reference/` doc |
| **S** | A tight feedback loop: quiz or in-browser task with immediate, ideally automatic feedback; retrieval from memory, not recognition; interleaves the prior schemas named in the spec |
| **W** | The real-world assignment or community engagement, with concrete steps and a debrief plan for the following session |

**Quiz rules (S-lessons):** answer options must be the same number of words (and characters where possible) — no formatting clues; feedback names *what* was right or wrong, not just that it was; wrong answers get a hint toward reconstruction, never the solution (the prime directive applies inside the HTML too).

**Revision (`/learn`):** pre-built lessons are a plan, not a prophecy. Before each session, `/learn` re-reads the next lesson against `notes.md` and patches it — recalibrate the warm-up, swap an example the learner already knows, adjust difficulty — or rewrites it outright when a recorded misconception or mission shift invalidates it. Patches keep the lesson's number, style, and spec fields.

## Reference docs — `reference/<name>.html`

The compressed essence of what lessons teach, in a format designed for quick reference — cheat sheets, reference algorithms, syntax cards, pose sequences, glossaries. They should print well.

- **Every K-lesson links one.** `/curriculum` creates the doc alongside the lesson (source-derived compression); `/learn` extends and corrects it as understanding is earned.
- **Compressed, not summarized.** A reference doc is the thing you'd pin above a desk: the syntax table, the decision flowchart, the sequence — not prose about it.
- **Formats that earn a reference doc:** syntax and code snippets; algorithms and flowcharts; exercises and routines; glossaries for any topic with its own nomenclature.
- **The glossary is the first reference most topics earn.** Seeded by `/curriculum` from the domain's terms; `/learn` promotes earned terms from `notes.md` into it. Once it exists, every lesson adheres to its terminology.
- **Update in place** as understanding deepens — stale reference docs are worse than none.

