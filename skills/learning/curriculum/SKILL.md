---
name: curriculum
description: Design and build a mission-grounded HTML course for a topic. Use when the user wants a study plan, a learning path, a course design, lesson sequencing, or says "/curriculum <topic>" or "/curriculum <topic> --depth=<quick|standard|deep>". Grounds the course in whatever material is already at hand (wiki/, survey.md, notes, sources), captures the mission (why learn this), and produces the full course under learning/<slug>/ — syllabus.md (plan + orchestration) plus the HTML course (index.html shell, lessons/ with checkpoint blocks, recall.html, reference/) that carries the learning experience end to end. Depth parameter controls lesson length and practice intensity.
---

# Curriculum — Course Orchestrator & Builder

Last updated: 2026-09-06

A standalone course **orchestrator and builder**. You plan the whole learning journey and encode that plan into the course itself: every lesson ends in a checkpoint block (completion manifest + what comes next), the recall page carries the return path, and `syllabus.md` carries the orchestration fields (`Next:`, `Gate:`) that tell `/learn` how to route the learner. Planning and authoring happen here so the learner's experience lives in the HTML — chat is reserved for bookkeeping and questions.

You author only Tier 1: `syllabus.md` (the plan, progress tracker, and orchestration contract) plus the HTML course — shell, K/S lessons, recall.html, reference docs. Stage 4–5 entries are loop-entry specs for `/practice`, not lessons. Cognitive load and ICAP are the design inputs: sequence small chunks, automate parts before integration, stamp every lesson with a depth type, an engagement target, and a load budget.

The skill works **standalone** — building or extending a course needs no other skill to have run first. It also works **along** the rest of the system: it reads `survey.md`, `notes.md`, and `retrieval.md` when they exist, and what it authors is exactly what `/learn` and `/recall` consume.

## Storage

Everything lives flat under `learning/<slug>/`. You own `syllabus.md`, `index.html`, `lessons/`, `recall.html`, and the initial `reference/` docs; `/learn` owns `notes.md` (including the consolidated Structural Memory, Micro-Skills, and Playbook sections) and revises the lessons as the learner progresses; `/recall` keeps `recall.html`'s queue in sync with the ledger. If `learning/<slug>/` doesn't exist, create it — don't ask permission.

## The mission comes first

The syllabus opens with a **Mission** — the reason the user is interested in learning the topic. Every lesson should be tied into it. Failing to understand the mission means knowledge acquisition is not grounded in real-world goals, lessons will feel too abstract, and you will have no way of judging what the user should do next. When `survey.md` exists, its Mission Contract and Roadmap are authoritative: preserve them, including uncertainty and scope cuts.

If the mission isn't already clear from `survey.md` or conversation, your first job is to question the user on *why* they want to learn this — interview before planning anything. Push back on vagueness — "to understand X" is not a mission; ask what changes in their life or work. **Also ask: "Do you have a real project or use case we can build toward?"** If yes, design the course as incremental steps toward that deliverable — each stage advances the project, K/S lessons teach what's needed for the next increment, course graduation = project works. One mission per topic. Missions may change as the user develops more skills and knowledge — this is normal: when `/learn` records a shift in `notes.md`, the user comes back here to re-plan; confirm before changing the mission. Full mission rules and template: [references/syllabus-format.md](references/syllabus-format.md).

## Inputs

**Look at what's already in the working directory first — don't start by demanding upstream skills.**

1. **A `wiki/` vault or obvious learning material** (a survey, ingested pages on the topic, curated notes, a sources folder): just begin — ground the course in it. Wiki pages become lesson reading material and primary-source candidates. Never write to `wiki/`.
2. **Something that might be material but you're not sure** (loose files, an unrelated-looking repo): ask — "I found <X> here. Is this the material you want the course built on, or should I research sources myself?"
3. **Nothing:** discuss with the user — mission first, then whether they have materials elsewhere or want you to find sources. Run the **3-question mini-diagnosis** ("What is this for, in your own words?" / "What have you built or read in it?" / "Which part feels most opaque?"), find 2–4 high-trust sources yourself (never trust parametric knowledge alone), and note in the syllabus header what it was built from. Mention `/survey` only as an option when the field is broad enough to need triage — never as a precondition.

When `learning/<slug>/survey.md` does exist, use it fully:
- **The matrix** → scope. The survey's mainline × stage matrix is the course's territory: cover cells up to each mainline's marked target stage. Items on the survey's stop-early/SKIP list get at most a vocabulary warm-up inside a lesson; cells beyond a mainline's target appear nowhere. Every lesson names the cell it serves.
- **Gap diagnosis** → depth. Big-gap mainlines (current stage far below target) get more Stage 1–2 lessons; mainlines already at `can-apply` may start at Stage 3. Sequencing is what keeps each lesson inside the learner's **zone of proximal development** — every lesson, the user should feel challenged *just enough*.
- **can-apply cells** → exercises. The samples those cells name are the S-lessons' natural worked examples and exercises — don't invent parallel ones without reason.
- **Curated sources** → each lesson's primary source comes from the Read list.

Also read `learning/<slug>/notes.md` if present — records of what's already known shift where the course starts.

## Depth Parameter

The `--depth` parameter controls lesson length and practice intensity. Parse it from the user's command (`/curriculum <topic> --depth=<level>`) or ask if ambiguous. Three levels:

| Level | Lesson length | K-lesson scope | S-lesson drills | Reading depth | When to use |
|-------|--------------|----------------|-----------------|---------------|-------------|
| **quick** | ~10 min | Minimal exposition, core concepts only | 1–2 simple drills per lesson | Summary + key excerpts | Time-constrained; survey a field; quick refresh |
| **standard** (default) | ~20–30 min | Worked examples, one chunk | 2–3 drills with feedback loops | Full sections from primary sources | Normal learning; build working fluency |
| **deep** | ~60–90 min | Extended examples, multiple perspectives, connections | 4–6 drills + synthesis prompts | Multiple sources, compare/contrast, build reference docs | Mastery goal; professional depth; research preparation |

**Quick** sacrifices durability for coverage — useful when the user needs breadth or is exploring. **Standard** balances depth and time — the default for mission-driven learning. **Deep** optimizes for mastery and transfer — lessons include extended readings, source comparison, and synthesis prompts that ask the learner to connect across mainlines.

Depth affects:
- **K-lessons:** quick = compressed summaries; standard = one worked example per concept; deep = multiple examples + compare sources + extend reference docs.
- **S-lessons:** quick = 1–2 drills; standard = 2–3 drills with interleaving; deep = 4–6 drills + transfer variants + synthesis.
- **Reading assignments:** quick = excerpts; standard = full sections; deep = multiple sources + "compare X and Y on Z" prompts.
- **Reference docs:** quick = bullet summaries; standard = worked examples documented; deep = comprehensive with edge cases and source citations.

If the user doesn't specify, default to **standard**. If they say "quick course" or "overview", use **quick**. If they say "deep dive", "mastery", or "professional depth", use **deep**.

## Depth: Knowledge → Skill → Wisdom

To learn at a deep level, the user needs three things:

- **Knowledge**, captured from high-quality, high-trust resources
- **Skills**, acquired through highly-relevant interactive lessons, based on that knowledge
- **Wisdom**, which comes from interacting with other learners and practitioners — testing skills in the real world

Every lesson is typed by which of these it builds, and each mainline climbs the ladder — K before S, S before W.

K/S/W is the *lesson-design* ladder; the survey matrix's four stages are the *mastery* ladder. They align rather than compete: K-lessons serve `can-recall` cells, S-lessons serve `can-apply` (reproduce the cell's named samples) and `can-transfer` (transfer variants at reduced support), W-lessons serve `can-generate` (real-world synthesis). A lesson's cell says *what mastery it climbs toward*; its K/S/W type says *how it teaches*.

**K — Knowledge.** Knowledge is all about *acquisition*. For acquiring knowledge, **difficulty is the enemy** — it eats the working memory needed for understanding. K-lessons teach only the knowledge required to acquire the skill that follows: worked examples, one chunk, minimal load, grounded in the syllabus sources (never parametric guesses). Each K-lesson produces or extends a `reference/` doc — the compressed essence that outlives the lesson.

**S — Skill.** If knowledge is all about acquisition, skills are about *durability and flexibility* — making the knowledge stick. For skill acquisition, **difficulty is the tool**: effortful retrieval is what builds storage strength. Distinguish two kinds of learning strength — **fluency strength** (in-the-moment retrieval) and **storage strength** (long-term retention). Fluency gives an illusory sense of mastery; storage strength is the real goal. S-lessons therefore build desirable difficulty in via **retrieval practice** (recall from memory, not recognition), **spacing** (warm-ups retrieve prior lessons), and **interleaving** (mixing related schemas — skills practice only). Every S-exercise runs on a **feedback loop, as tight as possible** — feedback immediately, and ideally automatically.

Interleaving is enforced, not suggested: every `[S]` lesson carries an **`Interleaves:`** field naming at least one schema from a **non-adjacent** prior lesson. Retrieving the lesson immediately before is fluency — the material is still warm — so it does not count. If no non-adjacent prior schema exists yet, the lesson is too early in the course to be an S-lesson.

**W — Wisdom.** Wisdom comes from true real-world interaction — testing skills *outside* the learning environment; it cannot be taught in a lesson, only arranged. So W entries are **loop-entry specs, not lessons**: each names its matrix cell, the shape of the real case to bring, the community or assignment, and the debrief plan — and is executed by `/practice`, closed by `/evaluate` when evidence reaches the cell. The primary vehicle is a **community**: a place, online or offline, where the user can test their skills in the real world — a forum, a subreddit, a real-world class (budget permitting), or a local interest group. Spec W-milestones around high-reputation communities; if the user has opted out of communities (check `notes.md` Preferences), respect it and design a solo real-world assignment instead.

Some topics require more skills than knowledge: theoretical physics skews K; yoga skews S. The mix should follow the mission — and the course MUST end at W, because a course that never leaves the learning environment doesn't serve a real-world mission.

## Output

Two deliverables, produced in order.

### 1. The plan — `syllabus.md`

Per the full template and field rules in [references/syllabus-format.md](references/syllabus-format.md). Shape:

```markdown
# Course: <topic>

<!-- source: survey.md <date> | wiki/ + <material> | mini-diagnosis (no prior material) -->

## Mission            (why · success looks like · constraints · out of scope)
## Sources            (annotated, high-trust; ### Gaps for what's missing)
## Stage 1 — Prerequisite schemas   (warm-up, automate parts)
## Stage 2 — Small chunks            (one new concept per lesson)
## Stage 3 — Combine schemas         (integration only after parts are fluent)
## Stage 4 — Real task               (whole-task, reduced support)
## Stage 5 — Transfer & wisdom       (new domain, no support, real world)
```

Each lesson under its stage carries a checkbox, `[K|S|W]` type, and its fields:
- **Objective** — what the learner can do after this lesson
- **Prerequisites** — what must be understood first
- **Opening task** — a micro-task in the real environment executed *before* explanation (new in v2: supports learning-by-doing earlier)
- **Lesson spec** — concrete per type: K names the worked example + `reference/` doc + 1–2 check-yourself items; S names the exercise, its feedback, and interleaved schemas; W names the assignment or community + debrief plan
- **Primary source** — where the material comes from
- **ICAP target** — Passive/Active/Constructive/Interactive
- **Load note** — cognitive load estimate
- **`Next:`** — what the checkpoint block's next-step card says: the following lesson, a recall gate, or a handoff (`/practice` at a mainline close)
- **`Gate:`** (optional) — a condition on the recall queue that must hold before this lesson starts (e.g. "start only when due items < 5"); `/learn` checks it at `start`

Plus a **Cell** field (`<mainline> × <stage>`) when a survey exists, and an **`Interleaves:`** field on every `[S]` lesson.

**Lesson spec adapts to depth:**
- **quick:** K = compressed summary + 1 example; S = 1–2 simple drills; reading = key excerpts.
- **standard:** K = worked example + reference doc; S = 2–3 drills with interleaving; reading = full source sections.
- **deep:** K = multiple examples + source comparison + extended reference; S = 4–6 drills + transfer variants + synthesis; reading = multiple sources with compare/contrast prompts.

**Mini-cases** (new in v2, promoted to lesson files in v3): From Stage 2 onward, every 2–3 lessons may include a `[mini-case]` entry — a simplified real scenario with walkthrough-level scaffolding, lighter than Stage 4 transfer but heavier than isolated S-lessons. Bridges the gap between exercises and full practice. **A mini-case gets its own lesson HTML file** (`lessons/NNNN-*.html` like any other lesson): scenario, guided steps, a self-check, and a checkpoint block like every lesson. In **quick** depth, mini-cases are optional; in **deep** depth, every mini-case includes multiple solution paths and post-case synthesis questions.

`syllabus.md` is the single source of truth for progress **and the orchestration contract**: it carries the Mission Contract, Roadmap, 3–5 checkpoint outcomes, and (for tool-oriented courses) a bounded Memory Budget. Each lesson carries `Checkpoint: CP<n>` and `Capability delta: Before → After`; `/learn` keeps checkboxes in sync and follows the `Next:`/`Gate:` fields to route the learner; `index.html` renders the syllabus (mission, roadmap, sources/gaps, staged lessons) as a browsable course shell.

**Confirm the plan with the user before building** — the syllabus is quick to redo; a built course isn't.

### 2. The course — HTML

Author per [references/lesson-format.md](references/lesson-format.md):

- **`index.html`** — the course shell: mission, stages, lesson list with links and progress (rendered from `syllabus.md`). Links the shared stylesheet in `assets/` that every lesson and reference doc also links. Includes JavaScript to parse syllabus.md and display checkboxes dynamically — no three-way sync required. Links `recall.html` prominently — the return path is part of the front door.
- **`assets/`** — the shared component library: one stylesheet (`assets/course.css`), a math loader (`assets/math.js`, KaTeX via CDN), a syllabus parser (`assets/progress.js`), plus any reusable widget (quiz, warm-up card, footer/nav). The quiz widget (`assets/quiz.js`) also powers the checkpoint manifest (collect `localStorage` widget state → copyable JSON) and the recall page's self-grade buttons. Lessons **link** these; they never inline CSS, hand-roll math, or copy-paste a widget. See [references/lesson-format.md](references/lesson-format.md).
- **`lessons/0001-*.html`** — one file per **K/S lesson and every mini-case** (Stages 1–3, plus any Stage 4 lesson that still teaches), from its spec, grounded in its primary source: links the shared stylesheet + math loader, **opening task first** (do-before-explain), warm-up second (except lesson 1), one chunk, math authored as `$...$`/`$$...$$` LaTeX, claims cited as clickable links to the source files, K/S-typed interactivity (K-lessons get 1–2 check-yourself items), **ends in a checkpoint block** (completion-manifest button + next-step card from the lesson's `Next:` field + a demoted tutor escape line), anchor-linked to shell, recall.html, and references. Lesson length and drill count follow the depth parameter: quick = ~10min + 1–2 drills; standard = ~20–30min + 2–3 drills; deep = ~60–90min + 4–6 drills + synthesis. **Stage 4–5 loop-entry specs get no lesson file** — they render in `index.html` as milestones carrying their spec, marked "closed by `/practice` + `/evaluate`".
- **`recall.html`** — the return-path page: due retrieval items as self-contained flashcards (prompt alone, answer behind a reveal, self-grade buttons, a sync block for copying results back to chat). Renders `retrieval.md` live over http and falls back to an embedded snapshot (`window.<SLUG>_RECALL`) that `/learn` and `/recall` regenerate at every bookkeeping pass. Format and cold-integrity rules: [references/lesson-format.md](references/lesson-format.md).
- **`reference/*.html`** — the docs the K-lessons link: cheat sheets, glossary seed. Compressed, print-worthy; link the shared stylesheet and math loader. In **deep** mode, reference docs include edge cases, source citations, and cross-mainline connections.

**No `syllabus.html` file** — eliminated in v2. `index.html` reads and renders `syllabus.md` directly.

Open `index.html` for the user when done.

These lessons are a plan, not a prophecy — `/learn` recalibrates each one against `notes.md` (and its warm-up against `retrieval.md`) before opening it. Build them source-faithful and spec-faithful; don't try to predict the learner.

## Hard constraints

- **Mission before lessons.** No syllabus without a populated Mission section. If the user has a real project/use case, record it and design the course as incremental steps toward that deliverable.
- **Depth parameter parsed or defaulted.** Parse `--depth=<quick|standard|deep>` from the command or ask if ambiguous. Default to **standard** if not specified.
- **Lesson length and drill count match depth.** quick = ~10min + 1–2 drills; standard = ~20–30min + 2–3 drills; deep = ~60–90min + 4–6 drills + synthesis. Reading assignments and reference docs scale accordingly.
- **In-matrix cells only** (when a survey exists). Every lesson MUST name the matrix cell it serves (`<mainline> × <stage>`, at or below that mainline's target) and serve the mission. Stop-early/SKIP items appear nowhere.
- **K before S before W** per subtopic. No skill lesson before its knowledge lesson; no wisdom milestone before the skill exists.
- **Prerequisites before integration.** No Stage 3+ lesson may depend on a schema not covered earlier. Order by dependency, not topic aesthetics.
- **One new concept per Stage 2 lesson.** Two new concepts in one objective → split it.
- **Every lesson carries type, opening task, ICAP target, and load note.** No exceptions — these are what `/learn` calibrates against.
- **Opening task is hands-on** — a command to run, a small variant to try, observing output before explanation. Not "think about X" or "read this" — do first, explain second.
- **Every lesson ends in a checkpoint block** — completion-manifest button + next-step card quoting the lesson's `Next:` field + a demoted tutor escape line. A lesson the learner can't close inside the page is a contract violation.
- **Every `[S]` lesson carries `Interleaves:`** naming ≥1 schema from a non-adjacent prior lesson. Absent, empty, or naming only the immediately preceding lesson is a contract violation.
- **Mini-cases in Stage 2–3** — every 2–3 lessons, insert a `[mini-case]` entry with a simplified real scenario, authored as its own lesson file. Optional in quick depth; mandatory with multiple solution paths in deep depth.
- **ICAP targets rise with the diagnosis:** novice subtopics start P/A → C; practitioner subtopics may start at C; C → I appears only in Stages 3–5.
- **At least one W milestone**, tied to the mission, in Stage 4–5 — specced as a loop-entry, not authored as a lesson.
- **Author Tier 1 only.** HTML lesson files exist only for K/S lessons and mini-cases. A W entry with a lesson file is a contract violation — wisdom is arranged, not authored.
- **Resumable:** lessons are checkboxes in `syllabus.md`. `/learn` picks up at the first unchecked lesson and checks it off when its checkpoint bookkeeping completes; loop-entry checkboxes are checked by `/evaluate` when evidence reaches their cell; `index.html` reflects the same progress by reading syllabus.md.
- **Orchestration is authored, not improvised.** Every lesson carries a `Next:` field its checkpoint card quotes verbatim, and recall-sensitive lessons carry a `Gate:` field `/learn` enforces. A course whose lessons end without saying what comes next is unfinished.
- **The return path is built.** `recall.html` exists, links from the shell, and renders due items from `retrieval.md` with an embedded snapshot fallback. A course without its recall page is unfinished.
- **Plan confirmed before build.** Don't author the HTML course until the user has approved the syllabus.
- **No syllabus.html file.** `index.html` renders `syllabus.md` directly — eliminated duplication and three-way sync.

## Exit

Open `index.html`; recommend `/learn <slug>` to open Stage 1's first lesson.

## Contract test

Given a fixture `survey.md`: the syllabus opens with a populated Mission (including project context if present); depth parameter is parsed or defaulted to standard; covers only cells at or below each mainline's target stage; every lesson carries a matrix cell, a K/S/W type, an opening task, an ICAP target, a load note, and a `Next:` field; lesson length and drill count match the depth parameter (quick = ~10min + 1–2 drills; standard = ~20–30min + 2–3 drills; deep = ~60–90min + 4–6 drills); every `[S]` lesson carries an `Interleaves:` field naming ≥1 schema from a non-adjacent prior lesson — an `[S]` lesson whose field is absent, empty, or names only the adjacent lesson is rejected; K precedes S precedes W per subtopic; ≥1 mini-case exists in Stage 2–3 with its own lesson file (optional in quick, mandatory with multiple solution paths in deep); ≥1 W milestone exists as a loop-entry spec naming its real-case shape and community/assignment; stage order respects prerequisites-before-integration; after approval, `index.html` + one HTML file per K/S lesson and mini-case exist — and none for Stage 4–5 loop-entry specs — all linking the shared stylesheet in `assets/` with no inline `<style>`, every K-lesson links a `reference/` doc and carries 1–2 check-yourself items, every lesson HTML opens with the opening task before explanation and ends in a checkpoint block (manifest button + next-step card), and `recall.html` exists, links from the shell, and renders due items with an embedded snapshot fallback. Reference docs in deep mode include edge cases and source citations. **No `syllabus.html` file exists.** Given a `wiki/` vault and no survey: the course begins without demanding `/survey`, and lessons cite wiki pages as material.

## Handoffs

**In:** mission (interviewed or from `survey.md`) + whatever material exists — `survey.md`, notes.md (including Structural Memory section), `wiki/`, or fresh sources. Never demands `/survey` first.

**Out:**
- Syllabus approved + course built → `syllabus.md` (with `Next:`/`Gate:` orchestration fields), `index.html`, K/S `lessons/` with checkpoint blocks, `recall.html`, seeded `reference/` → `/learn <slug>` opens Stage 1.
- Stage 4–5 loop-entry specs written → real-case shapes + communities → executed later by `/practice`, closed by `/evaluate`.
- The recall page and lesson warm-up blocks → due items from `retrieval.md`, planned and synced by `/recall`.
- Mainlines or target stages look wrong during planning → back to `/survey` — never re-triage here.

## Boundaries

- vs `/survey`: survey decides **what** deserves time (strategic triage); curriculum decides **how** to sequence it (tactical) and **when** each piece of the loop runs (orchestration). Curriculum never re-triages the matrix — if the mainlines or target stages look wrong, send the user back to `/survey`.
- vs `/learn`: curriculum designs, orchestrates, and builds the course; learn runs sessions over it (open lessons, do checkpoint bookkeeping, answer questions) and revises lessons as the learner diverges. Curriculum never runs a session; learn never restructures the course (that's a re-run of `/curriculum`).
- vs `/recall`: curriculum builds the recall page and the warm-up blocks it feeds; recall plans what's due and syncs results. Curriculum never reschedules items.
- vs `/practice`: curriculum *specs* the real-world work (Stage 4–5 loop-entries); practice *runs* it. Curriculum authors no transfer content — a transfer task with a worked answer is an oxymoron.
