# Course HTML Format — Shell, Lessons & Reference Docs

_Last updated: 2026-09-06_

What `/curriculum` authors: the course shell (`index.html`), a shared component library in `learning/<slug>/assets/`, interactive lessons in `learning/<slug>/lessons/`, the recall page (`recall.html`), and reference docs in `learning/<slug>/reference/`. `/learn` **revises** lessons when the learner diverges from the plan (recalibrated warm-ups, swapped examples, rewritten misconceptions). Lessons are rarely revisited; references are — design accordingly.

Every lesson is anchored to a roadmap checkpoint. It displays `Checkpoint: CP<n>` and an observable
`Capability delta: Before → After`. The first lesson shows the mission, baseline, target output,
whole roadmap, scope cuts, rehearsal method, and next checkpoint before new teaching.

The HTML course carries the learning experience: reading, opening tasks, drills, quizzes, embedded recall. Chat is reserved for post-lesson bookkeeping and user-initiated tutoring — so every lesson must be completable, checkable, and closable **inside the page**.

## Course shell — `index.html`

One page rendering the course: mission, stages, and the lesson list with links. It is the front door the user opens between sessions.

- Renders `syllabus.md` — same stages, same lesson titles, same order. `syllabus.md` is the source of truth for the plan and progress; `index.html` is the lesson-launcher view of it. There is **no `syllabus.html`** — eliminated in v2; the shell reads and renders `syllabus.md` directly via `assets/progress.js`.
- Shows progress: completed lessons visibly distinct from upcoming ones. Progress checkboxes reflect the checkboxes in `syllabus.md` (persisted to `localStorage` as a convenience view; the durable record is the `syllabus.md` checkbox written at bookkeeping).
- Links the course's shared stylesheet from `assets/` (see below) — `index.html` is the first page to link it, and every lesson, `recall.html`, and every reference doc links the same file, so the course looks like one course, not a pile of one-offs.
- Links `recall.html` prominently — the return path is part of the front door, not a hidden page.

## Shared components — `assets/`

The course's reusable parts live in `assets/` and are **linked, never inlined**. This is what makes the pages look like one course and lets `/learn` fix a widget or a colour once instead of in every file.

- **Shared stylesheet first.** `assets/course.css` (one file) holds the entire visual system — palette, typography, layout, component styles. `index.html`, every lesson, and every reference doc link it with `<link rel="stylesheet" href="../assets/course.css">` (adjust the relative path per directory). **Never** paste a `<style>` block into a lesson or duplicate the CSS across files. A reference doc may add a small `@media print` block only for print tuning — never a copy of the shared sheet.
- **Light and dark mode, with a user toggle.** `course.css` defines *both* themes as CSS custom properties — never hard-code a colour outside these variables. A `:root { ... }` block holds the light palette and a `:root[data-theme="dark"] { ... }` block overrides it for dark; default to the OS preference with `@media (prefers-color-scheme: dark)` for visitors who haven't chosen. A shared `assets/theme.js` (linked on every page, like the stylesheet) renders a light/dark switch, sets `data-theme` on `<html>`, and persists the choice in `localStorage` so it holds across pages and sessions — apply the saved theme before first paint to avoid a flash. One toggle, one stylesheet, every page in sync.
- **Reusable widgets are components, not copy-paste.** Anything a second lesson would repeat — a quiz widget, a reveal/warm-up card, the footer/nav — lives once in `assets/` (e.g. `assets/quiz.js`) and is linked with `<script src="../assets/quiz.js" defer>`. Before authoring a lesson, read `assets/` and build from what's there; when a lesson needs something new and reusable, add it to `assets/` and link it. Reuse is the default, not the exception.
- **No dead controls.** If it looks clickable, it works. Every checkbox, button, or toggle you render is wired to real behaviour — never a checkbox that can't be checked or a button that does nothing. Interactive state that should outlive a reload (progress check-ins, theme, revealed answers) persists to `localStorage`; put the wiring in a shared `assets/*.js` (e.g. `assets/progress.js` for the check-in checkboxes) linked on every page, not inlined per lesson. Keep it simple and stupid — plain DOM + `localStorage`, no framework.

## Math — `assets/math.js` + KaTeX

Formulas appear inline (`$...$`) and display (`$$...$$`). Render them with **KaTeX** (fast, correct), loaded from a CDN. Do **not** write math as plain text inside `<pre>`/`<code>` blocks — `G_t = R_{t+1} + γ·R_{t+2}` is unreadable next to real typeset math, and it breaks on subscripts, fractions, and summations.

- `assets/math.js` is the loader: it pulls KaTeX (CSS + JS + auto-render) from `cdn.jsdelivr.net`, then runs `renderMathInElement` over `<main>` to turn `$...$` / `$$...$$` into typeset math. Every page that may contain math links it: `<script src="../assets/math.js" defer></script>`.
- **Author math in LaTeX**, between the right delimiters: inline `$G_t = \sum_{k\ge0}\gamma^k R_{t+k+1}$`, display `$$\nabla_\theta J(\pi_\theta) = \mathbb{E}[\nabla_\theta \log \pi_\theta(a|s)\, Q(s,a)]$$`. KaTeX's supported set: https://katex.org/docs/support_table.
- **Escaping in HTML:** because `$` and `\` are ordinary in HTML but load-bearing for KaTeX, put math inside element text (not attributes), and don't HTML-encode the backslashes. KaTeX auto-render handles the delimiter scanning; you only write the LaTeX.
- Link it on **every** lesson, `index.html`, `recall.html`, and any reference doc that contains a formula — a page that conditionally "might have math" should just link it unconditionally, since the loader is a no-op when there's nothing to render.


## Lessons — `lessons/0001-<dash-case-name>.html`

One self-contained HTML file per lesson, numbered in syllabus order, authored from the lesson's spec and grounded in its primary source.

**Every lesson MUST:**

- **Teach one tightly-scoped thing** tied to the mission, completable in one sitting — one chunk, one tangible win.
- **Open with the opening task** — a hands-on command, a small variant to try, observing output *before* any explanation (do first, explain second). **The warm-up comes second** — a retrieval question from a *prior* lesson (spacing), before the new material. **The first lesson of the course has no warm-up** — nothing precedes it to retrieve; it opens with mission framing after the opening task. (If the learner declared relevant prior knowledge, lesson 1 may activate *that* pre-course knowledge, but frame it as such, not as spaced retrieval of a prior lesson.)
- **Be beautiful.** Clean, readable typography and layout; think Tufte. Link the shared stylesheet in `assets/` — never inline a `<style>` block or duplicate the CSS.
- **Name its primary source** — the single highest-trust resource for this topic, from the syllabus — and cite sources for every substantive claim. **Inline, a citation is just a little mark** — a small superscript footnote marker (e.g. `<sup><a href="#src-3">3</a></sup>`), never a verbose path link mid-sentence. A `(see wiki/wiki/concepts/agent-environment-loop.md)` spelled out in the running text is visual noise. **Collect the real materials in a bulleted "Sources" list at the bottom of the lesson**, each entry a clickable `<a href>` to the actual file (a relative path to the repo file, or its wiki page) — that list is what lets the learner verify each claim.
- **Anchor-link** the course shell, `recall.html`, related lessons, and `reference/` docs.
- **Explain code inline.** When a lesson shows a code block, put the comments and explanation *inside* the block — inline comments on the lines they describe — not as prose paragraphs below it. The learner reads each annotation at the exact line it applies to, instead of mapping a paragraph back onto code they've already scrolled past.
- **End with the checkpoint block** (see below) — not a vague "ask the tutor" reminder. The checkpoint is how the lesson closes.
- **Name its checkpoint and capability delta** in the page and connect the opening task, construction,
  and retry to that expected change.

**Per K/S/W type:**

| Type | The HTML contains |
| :--- | :--- |
| **K** | Worked example first, explained with inline code comments (not prose below the block); the one new concept, minimally loaded; links its `reference/` doc; **1–2 check-yourself items** (quiz or short-answer) so the K-lesson closes with learner construction, not just reading |
| **S** | A tight feedback loop: quiz or in-browser task with immediate, ideally automatic feedback; retrieval from memory, not recognition; interleaves the prior schemas named in the spec |
| **W** | The real-world assignment or community engagement, with concrete steps and a debrief plan for the following session |

Operational-memory items use the same feedback loop: cold prompt, learner attempt, answer/reveal, then
an optional timed execution. Recognition alone is not evidence of recall or fluent execution.

**Quiz rules (S-lessons):** answer options must be the same number of words (and characters where possible) — no formatting clues; feedback names *what* was right or wrong, not just that it was; wrong answers get a hint toward reconstruction, never the solution (the prime directive applies inside the HTML too).

**Every reader question is answerable in the page** — no question is decorative. Wire each one with a shared widget in `assets/` (e.g. `assets/quiz.js`), keep it simple and stupid:

- **Auto-checkable questions** (multiple choice, exact/short factual answer, code output): the learner submits, the widget checks against the stored answer and shows the result immediately — a diff/highlight of their input against the correct answer, not just "right/wrong".
- **Short-answer / open questions**: the learner types into a textarea, then hits reveal to see the reference answer beside their own for a simple self-comparison diff — never auto-graded, since there's no single right string. Their draft persists to `localStorage` so a reload doesn't wipe it.

**Revision (`/learn`):** pre-built lessons are a plan, not a prophecy. Before each session, `/learn` re-reads the next lesson against `notes.md` and patches it — recalibrate the warm-up against the actual `retrieval.md` ledger (what is due, what has lapsed), swap an example the learner already knows, adjust difficulty — or rewrites it outright when a recorded misconception or mission shift invalidates it. Patches keep the lesson's number, style, and spec fields.

## The checkpoint block — how a lesson closes

Every lesson ends with a **checkpoint block**: a card that packages what the learner did in the page and tells them exactly what happens next. It replaces "return to chat when done" with a concrete, mechanical handoff.

- **The completion manifest button.** One button (wired by the shared `assets/quiz.js`): *"Copy completion manifest → paste in chat: done L&lt;n&gt;"*. Clicking it collects the lesson's `localStorage` widget state (every quiz answer and its correctness, every drill draft's presence and whether the reference was revealed, timestamps) into a compact JSON block and copies it to the clipboard. The user pastes it into chat with `done L<n>` — that paste *is* the done-signal.
- **What the manifest contains:** `{lesson, items: {<id>: {val, correct} | {draft: bool, revealed: bool}}, completed-at}`. It carries *what the page already knows* — nothing more. `/learn` parses it at bookkeeping and infers assistance from the pattern: locked-correct-first-try reads as `none`; wrong-then-correct as `hint`; revealed-without-draft as `walkthrough`. It is not trusted blindly — an ambiguous pattern earns one spot-probe in chat.
- **The next-step card.** Alongside the button, one card naming what comes next, from the lesson's `Next:` field in `syllabus.md`: the next lesson link, or "run recall first — N items due" when a gate applies, or "bring a real case to `/practice`" at a mainline close. The learner should never finish a lesson and wonder what to do.
- **Tutor escape hatch, demoted.** One line at the bottom: *"Stuck on anything here? Ask the tutor in chat — that conversation is where questions belong."* Present on every lesson, never the focus.

## The recall page — `recall.html`

One course page for the return path: every due retrieval item as a self-contained flashcard. `/recall` (the chat skill) is the planner that points here; the page is where the firings happen.

- **Two data sources, same dual-path pattern as `assets/progress.js`:** fetch `retrieval.md` and render due rows live when served over http; otherwise fall back to an embedded snapshot (`window.<SLUG>_RECALL`) regenerated by `/learn` or `/recall` at every bookkeeping pass. Served beats snapshot when both exist.
- **Per due item:** the cold prompt alone (derived from the row's pointer — a term asks for its definition, a schema for its rule/trigger/transition), a *reveal* button, then self-grade buttons — **got it** / **missed it** / **peeked**. Grades persist to `localStorage`.
- **Cold integrity is enforced by grading, not by hiding:** an item revealed *before* the learner committed an attempt is graded **peeked**, which syncs as assistance `walkthrough` — the honest treatment of a warm retrieval. The page never shows an answer next to its prompt unprompted.
- **A sync block at the bottom:** the same manifest pattern as the checkpoint — *"Copy recall results → paste in chat: sync recall"* — packaging the self-grades for the ledger. `/recall` applies the scheduling rules on that paste.
- **No teaching on the page.** A missed item names the correct answer after the attempt is graded — nothing more. Re-derivation belongs to a lesson revision or a tutor conversation.

## Reference docs — `reference/<name>.html`

The compressed essence of what lessons teach, in a format designed for quick reference — cheat sheets, reference algorithms, syntax cards, pose sequences, glossaries. They should print well.

- **Every K-lesson links one.** `/curriculum` creates the doc alongside the lesson (source-derived compression); `/learn` extends and corrects it as understanding is earned.
- **Compressed, not summarized.** A reference doc is the thing you'd pin above a desk: the syntax table, the decision flowchart, the sequence — not prose about it.
- **Formats that earn a reference doc:** syntax and code snippets; algorithms and flowcharts; exercises and routines; glossaries for any topic with its own nomenclature.
- **The glossary is the first reference most topics earn.** Seeded by `/curriculum` from the domain's terms; `/learn` promotes earned terms from `notes.md` into it. Once it exists, every lesson adheres to its terminology.
- **Update in place** as understanding deepens — stale reference docs are worse than none.
