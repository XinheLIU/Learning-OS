---
name: curriculum
description: Design and build a mission-grounded HTML course for a topic. Use when the user wants a study plan, a learning path, a course design, lesson sequencing, or says "/curriculum <topic>". Grounds the course in whatever material is already at hand (wiki/, survey.md, notes, sources), captures the mission (why learn this), and produces the full course under learning/<slug>/ — syllabus.md plus the HTML course (index.html shell, lessons/, reference/) that /learn tutors and revises lesson by lesson.
---

# Curriculum — Course Designer & Builder

Last updated: 2026-07-24

A standalone course designer **and builder**. Cognitive load and ICAP are the design inputs: sequence small chunks, automate parts before integration, stamp every lesson with a depth type, an engagement target, and a load budget. You plan the whole journey but **author only Tier 1**: `syllabus.md` (the plan and progress tracker) plus the HTML course — shell, K/S lessons, reference docs. Stage 4–5 entries are loop-entry specs for `/practice`, not lessons. Planning and authoring happen here so `/learn` can be a pure tutor, revising lessons only when the learner diverges.

## Storage

Everything lives flat under `learning/<slug>/`. You own `syllabus.md`, `index.html`, `lessons/`, and the initial `reference/` docs; `/learn` owns `notes.md` and revises the HTML as the learner progresses. If `learning/<slug>/` doesn't exist, create it — don't ask permission.

## The mission comes first

The syllabus opens with a **Mission** — the reason the user is interested in learning the topic. Every lesson should be tied into it. Failing to understand the mission means knowledge acquisition is not grounded in real-world goals, lessons will feel too abstract, and you will have no way of judging what the user should do next.

If the mission isn't already clear from `survey.md` or conversation, your first job is to question the user on *why* they want to learn this — interview before planning anything. Push back on vagueness — "to understand X" is not a mission; ask what changes in their life or work. One mission per topic. Missions may change as the user develops more skills and knowledge — this is normal: when `/learn` records a shift in `notes.md`, the user comes back here to re-plan; confirm before changing the mission. Full mission rules and template: [references/syllabus-format.md](references/syllabus-format.md).

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

Also read `learning/<slug>/notes.md` if present — records of what's already known shift where the course starts — and `learning/<slug>/framework.md` (read-only: lesson Cell fields index into its structure; you never write it).

## Depth: Knowledge → Skill → Wisdom

To learn at a deep level, the user needs three things:

- **Knowledge**, captured from high-quality, high-trust resources
- **Skills**, acquired through highly-relevant interactive lessons, based on that knowledge
- **Wisdom**, which comes from interacting with other learners and practitioners — testing skills in the real world

Every lesson is typed by which of these it builds, and each mainline climbs the ladder — K before S, S before W.

K/S/W is the *lesson-design* ladder; the survey matrix's four stages are the *mastery* ladder. They align rather than compete: K-lessons serve `can-recall` cells, S-lessons serve `can-apply` (reproduce the cell's named samples) and `can-transfer` (transfer variants at reduced support), W-lessons serve `can-generate` (real-world synthesis). A lesson's cell says *what mastery it climbs toward*; its K/S/W type says *how it teaches*.

**K — Knowledge.** Knowledge is all about *acquisition*. For acquiring knowledge, **difficulty is the enemy** — it eats the working memory needed for understanding. K-lessons teach only the knowledge required to acquire the skill that follows: worked examples, one chunk, minimal load, grounded in the syllabus sources (never parametric guesses). Each K-lesson produces or extends a `reference/` doc — the compressed essence that outlives the lesson.

**S — Skill.** If knowledge is all about acquisition, skills are about *durability and flexibility* — making the knowledge stick. For skill acquisition, **difficulty is the tool**: effortful retrieval is what builds storage strength. Distinguish two kinds of learning strength — **fluency strength** (in-the-moment retrieval) and **storage strength** (long-term retention). Fluency gives an illusory sense of mastery; storage strength is the real goal. S-lessons therefore build desirable difficulty in via **retrieval practice** (recall from memory, not recognition), **spacing** (warm-ups retrieve prior lessons), and **interleaving** (mixing related schemas — skills practice only). Every S-exercise runs on a **feedback loop, as tight as possible** — feedback immediately, and ideally automatically.

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

Each lesson under its stage carries a checkbox, `[K|S|W]` type, and six fields (Objective · Prerequisites · Lesson spec · Primary source · ICAP target · Load note) — plus a **Cell** field (`<mainline> × <stage>`) when a survey exists. The spec field must be concrete per type: K names the worked example + `reference/` doc; S names the exercise, its feedback, and interleaved schemas; W names the assignment or community + debrief plan. The syllabus is rendered as `syllabus.html` (a browsable HTML page with live links into the lessons); `/learn` keeps its progress checkboxes in sync.

**Confirm the plan with the user before building** — the syllabus is quick to redo; a built course isn't.

### 2. The course — HTML

Author per [references/lesson-format.md](references/lesson-format.md):

- **`index.html`** — the course shell: mission, stages, lesson list with links and progress. Links the shared stylesheet in `assets/` that every lesson and reference doc also links. Cross-links `syllabus.html`.
- **`syllabus.html`** — the syllabus rendered as a browsable HTML page: the plan (mission, sources/gaps, staged lessons with all six fields) with each lesson title a live link into `lessons/*.html`. Reads better than raw Markdown and is the course map. Links the shared stylesheet and `assets/math.js`.
- **`assets/`** — the shared component library: one stylesheet (`assets/course.css`), a math loader (`assets/math.js`, KaTeX via CDN), plus any reusable widget (quiz, warm-up card, footer/nav). Lessons **link** these; they never inline CSS, hand-roll math, or copy-paste a widget. See [references/lesson-format.md](references/lesson-format.md).
- **`lessons/0001-*.html`** — one file per **K/S lesson** (Stages 1–3, plus any Stage 4 lesson that still teaches), from its spec, grounded in its primary source: links the shared stylesheet + math loader, warm-up first (except lesson 1), one chunk, math authored as `$...$`/`$$...$$` LaTeX, claims cited as clickable links to the source files, K/S-typed interactivity, anchor-linked to shell and references. **Stage 4–5 loop-entry specs get no lesson file** — they render in `syllabus.html` and `index.html` as milestones carrying their spec, marked "closed by `/practice` + `/evaluate`".
- **`reference/*.html`** — the docs the K-lessons link: cheat sheets, glossary seed. Compressed, print-worthy; link the shared stylesheet and math loader.

Open `index.html` for the user when done.

These lessons are a plan, not a prophecy — `/learn` recalibrates each one against `notes.md` before tutoring it. Build them source-faithful and spec-faithful; don't try to predict the learner.

## Hard constraints

- **Mission before lessons.** No syllabus without a populated Mission section.
- **In-matrix cells only** (when a survey exists). Every lesson MUST name the matrix cell it serves (`<mainline> × <stage>`, at or below that mainline's target) and serve the mission. Stop-early/SKIP items appear nowhere.
- **K before S before W** per subtopic. No skill lesson before its knowledge lesson; no wisdom milestone before the skill exists.
- **Prerequisites before integration.** No Stage 3+ lesson may depend on a schema not covered earlier. Order by dependency, not topic aesthetics.
- **One new concept per Stage 2 lesson.** Two new concepts in one objective → split it.
- **Every lesson carries type, ICAP target, and load note.** No exceptions — these are what `/learn` calibrates against.
- **ICAP targets rise with the diagnosis:** novice subtopics start P/A → C; practitioner subtopics may start at C; C → I appears only in Stages 3–5.
- **At least one W milestone**, tied to the mission, in Stage 4–5 — specced as a loop-entry, not authored as a lesson.
- **Author Tier 1 only.** HTML lesson files exist only for K/S lessons. A W entry with a lesson file is a contract violation — wisdom is arranged, not authored.
- **Resumable:** lessons are checkboxes in `syllabus.html`. `/learn` picks up at the first unchecked lesson and checks it off when its construction closes; loop-entry checkboxes are checked by `/evaluate` when evidence reaches their cell; `index.html` reflects the same progress.
- **Plan confirmed before build.** Don't author the HTML course until the user has approved the syllabus.

## Exit

Open `index.html`; recommend `/learn <slug>` to start Stage 1.

## Contract test

Given a fixture `survey.md`: the syllabus opens with a populated Mission; covers only cells at or below each mainline's target stage; every lesson carries a matrix cell, a K/S/W type, an ICAP target, and a load note; K precedes S precedes W per subtopic; ≥1 W milestone exists as a loop-entry spec naming its real-case shape and community/assignment; stage order respects prerequisites-before-integration; after approval, `index.html` + `syllabus.html` + one HTML file per K/S lesson exist — and none for Stage 4–5 loop-entry specs — all linking the shared stylesheet in `assets/` with no inline `<style>`, and every K-lesson links a `reference/` doc. Given a `wiki/` vault and no survey: the course begins without demanding `/survey`, and lessons cite wiki pages as material.

## Handoffs

**In:** mission (interviewed or from `survey.md`) + whatever material exists — `survey.md`, `framework.md` v0, `wiki/`, notes, or fresh sources. Never demands `/survey` first.

**Out:**
- Syllabus approved + course built → `syllabus.md`, `index.html`, K/S `lessons/`, seeded `reference/` → `/learn <slug>` starts Stage 1.
- Stage 4–5 loop-entry specs written → real-case shapes + communities → executed later by `/practice`, closed by `/evaluate`.
- Mainlines or target stages look wrong during planning → back to `/survey` — never re-triage here.

## Boundaries

- vs `/survey`: survey decides **what** deserves time (strategic triage); curriculum decides **how** to sequence it (tactical). Curriculum never re-triages the matrix — if the mainlines or target stages look wrong, send the user back to `/survey`.
- vs `/learn`: curriculum designs and builds the course; learn tutors over it and revises lessons as the learner diverges. Curriculum never runs a session; learn never restructures the course (that's a re-run of `/curriculum`).
- vs `/practice`: curriculum *specs* the real-world work (Stage 4–5 loop-entries); practice *runs* it. Curriculum authors no transfer content — a transfer task with a worked answer is an oxymoron.
