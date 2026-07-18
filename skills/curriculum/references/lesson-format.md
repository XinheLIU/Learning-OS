# Course HTML Format — Shell, Lessons & Reference Docs

_Last updated: 2026-07-17_

What `/curriculum` authors: the course shell (`index.html`), the syllabus view (`syllabus.html`), a shared component library in `learning/<slug>/assets/`, interactive lessons in `learning/<slug>/lessons/`, and reference docs in `learning/<slug>/reference/`. `/learn` tutors over these files and **revises** them when the learner diverges from the plan. Lessons are rarely revisited; references are — design accordingly.

## Course shell — `index.html`

One page rendering the course: mission, stages, and the lesson list with links. It is the front door the user opens between sessions.

- Mirrors `syllabus.html` — same stages, same lesson titles, same order. When one changes, the other is updated in the same session (both are *views* of the same plan; `syllabus.html` stays the source of truth for the plan and progress, `index.html` is the lesson-launcher view of it).
- Shows progress: completed lessons visibly distinct from upcoming ones (`/learn` updates this as it checks lessons off).
- Links the course's shared stylesheet from `assets/` (see below) — `index.html` is the first page to link it, and every lesson and reference doc links the same file, so the course looks like one course, not a pile of one-offs.
- Cross-links `syllabus.html` (and vice-versa), so the shell and the syllabus are always one click apart.

## Syllabus view — `syllabus.html`

The plan, rendered as a browsable HTML page rather than a `.md` file — easier to read than raw Markdown, and it links straight into the lessons it schedules.

- A faithful HTML rendering of `syllabus.md`: mission, sources/gaps, and the staged lesson plan with every lesson's type, objective, prerequisites, spec, primary source, ICAP target, and load note visible.
- **Lesson titles are live links into `lessons/*.html`** — the syllabus is the course map: read the plan, click through to the lesson. (The shell's lesson list links the same files; the syllabus additionally shows the *why* — objectives, prerequisites, load notes — that the shell omits.)
- Links the shared stylesheet and `assets/math.js` (see Math, below) so formulas render.
- `/learn` keeps it in sync with `syllabus.md`'s progress checkboxes. The Markdown `syllabus.md` is no longer authored as a separate deliverable — `syllabus.html` **is** the syllabus; keep a Markdown mirror only if a downstream tool demands `.md`.

## Shared components — `assets/`

The course's reusable parts live in `assets/` and are **linked, never inlined**. This is what makes the pages look like one course and lets `/learn` fix a widget or a colour once instead of in every file.

- **Shared stylesheet first.** `assets/course.css` (one file) holds the entire visual system — palette, typography, layout, component styles. `index.html`, every lesson, and every reference doc link it with `<link rel="stylesheet" href="../assets/course.css">` (adjust the relative path per directory). **Never** paste a `<style>` block into a lesson or duplicate the CSS across files. A reference doc may add a small `@media print` block only for print tuning — never a copy of the shared sheet.
- **Reusable widgets are components, not copy-paste.** Anything a second lesson would repeat — a quiz widget, a reveal/warm-up card, the footer/nav — lives once in `assets/` (e.g. `assets/quiz.js`) and is linked with `<script src="../assets/quiz.js" defer>`. Before authoring a lesson, read `assets/` and build from what's there; when a lesson needs something new and reusable, add it to `assets/` and link it. Reuse is the default, not the exception.

## Math — `assets/math.js` + KaTeX

Formulas appear inline (`$...$`) and display (`$$...$$`). Render them with **KaTeX** (fast, correct), loaded from a CDN. Do **not** write math as plain text inside `<pre>`/`<code>` blocks — `G_t = R_{t+1} + γ·R_{t+2}` is unreadable next to real typeset math, and it breaks on subscripts, fractions, and summations.

- `assets/math.js` is the loader: it pulls KaTeX (CSS + JS + auto-render) from `cdn.jsdelivr.net`, then runs `renderMathInElement` over `<main>` to turn `$...$` / `$$...$$` into typeset math. Every page that may contain math links it: `<script src="../assets/math.js" defer></script>`.
- **Author math in LaTeX**, between the right delimiters: inline `$G_t = \sum_{k\ge0}\gamma^k R_{t+k+1}$`, display `$$\nabla_\theta J(\pi_\theta) = \mathbb{E}[\nabla_\theta \log \pi_\theta(a|s)\, Q(s,a)]$$`. KaTeX's supported set: https://katex.org/docs/support_table.
- **Escaping in HTML:** because `$` and `\` are ordinary in HTML but load-bearing for KaTeX, put math inside element text (not attributes), and don't HTML-encode the backslashes. KaTeX auto-render handles the delimiter scanning; you only write the LaTeX.
- Link it on **every** lesson, `syllabus.html`, and any reference doc that contains a formula — a page that conditionally "might have math" should just link it unconditionally, since the loader is a no-op when there's nothing to render.


## Lessons — `lessons/0001-<dash-case-name>.html`

One self-contained HTML file per lesson, numbered in syllabus order, authored from the lesson's spec and grounded in its primary source.

**Every lesson MUST:**

- **Teach one tightly-scoped thing** tied to the mission, completable in one sitting — one chunk, one tangible win.
- **Open with the warm-up** — a retrieval question from a *prior* lesson (spacing), before the new material. **The first lesson of the course has no warm-up** — nothing precedes it to retrieve; it opens with mission framing instead. (If the learner declared relevant prior knowledge, lesson 1 may activate *that* pre-course knowledge, but frame it as such, not as spaced retrieval of a prior lesson.)
- **Be beautiful.** Clean, readable typography and layout; think Tufte. Link the shared stylesheet in `assets/` — never inline a `<style>` block or duplicate the CSS.
- **Name its primary source** — the single highest-trust resource for this topic, from the syllabus — and cite sources inline for every substantive claim. **Each citation is a clickable `<a href>` link to the actual file** (a relative path to the repo file, or its wiki page), not plain `<code>` text — the links are what let the learner verify the claim, and lessons should be littered with them.
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

