# Software Engineering Basics Trial — RUNBOOK

Last updated: 2026-09-03

**Goal: be able to open a module in your own codebase, name what makes it hard to change, and
defend a specific refactor against a named principle and its cost — in 3 hours, across 3 days.**
You are both the learner and the tester.

| | |
| :--- | :--- |
| Topic | Writing good code and design patterns — judged against real code, not vocabulary |
| Depth | `quick` (~10 min lessons, 1–2 drills each) |
| Budget | **2 × 30 min sessions per day × 3 days** = 6 sessions |
| Substrate | `~/GitHub/synapse`, in a throwaway worktree |
| Day 3 test | A 6-item sealed battery, written before any teaching, opened only at measurement time |

**Why this trial exists alongside herdr.** herdr is a bounded topic with a ground truth — the
installed CLI settles every question. This one has neither. The field is unbounded, the literature
openly contradicts itself, and an agent can lecture fluently on all of it from memory without
citing anything. That makes it the trial for the failure modes herdr cannot reach.

| Property under test | herdr | this trial |
| :--- | :--- | :--- |
| Triage of an **unbounded** field — the SKIP list as the deliverable | weak | **central** |
| `--depth=quick` | no (`standard`) | **yes — the other end of the parameter** |
| `/synthesis-research` | not covered | **covered** |
| Refusal to teach from parametric memory | CLI is the authority | **no ground truth — must cite** |
| Opinion stated as fact | n/a | **central** |
| Transfer onto the learner's own repository | small task | **refactor your own code** |

**Why `quick` and not `standard`.** A 30-minute session must hold a warm-up, a lesson, and a
drill. A `standard` lesson at 20–30 minutes eats the whole session. At `quick`, a session fits two
lessons or one lesson plus real work. Depth serves the session, not the reverse — and running the
parameter at its low end is the only way to find out whether it does anything.

## Safety boundary — read before anything else

You will be refactoring **code you actually own**. `~/GitHub/synapse` has uncommitted changes on
`main` right now. These are not suggestions.

- All work happens in a **throwaway git worktree** created from `HEAD`. Never edit, `checkout`,
  `stash`, or `reset` the live `synapse` checkout.
- **No commits, no pushes, no history rewriting** — in the worktree or anywhere else. The refactor
  lives and dies in the worktree.
- Read-only inspection of the live checkout is fine. Writing to it is not.
- Delete the worktree at the end (`Reset`, below). Nothing merges back.

If a step would violate any of these, stop and record **NOT RUN**. Do not improvise a substitute.

## Session hygiene — what makes the Day 3 number mean anything

| Session | May see | Must never see |
| :--- | :--- | :--- |
| Battery author (Day 0) | the sources, the synapse code | any tutoring, any lesson |
| Tutor (Days 1–3) | the sources, your notes, the worktree | **the battery** |
| You | everything, at the end | the battery before Day 3 |

**Run each session fresh.** A session that has read the battery cannot honestly teach against it —
it will teach to the test without meaning to.

Do **not** print, `cat`, `grep`, hash, summarize, or "just check the length of" the battery before
Day 3. Confirming the file exists is the only permitted interaction.

## Setup

```bash
cd /Users/xhl/GitHub/learning-infra/agent-skill-projects/learning-os
ls learning/swe-basics 2>/dev/null && echo "STOP: move it aside first"

# throwaway worktree from committed HEAD — your dirty working tree is untouched
git -C ~/GitHub/synapse worktree add /tmp/swe-trial HEAD --detach
ls /tmp/swe-trial/graph_engine/ /tmp/swe-trial/synapse/
git -C ~/GitHub/synapse status --porcelain | head -3   # your real tree, unchanged, still dirty
```

If the worktree command fails, pick another repo you own with 500–2000 lines of code you wrote
yourself, and substitute its path everywhere below. Do not substitute a repo you did not write —
the whole trial rests on judging code you are responsible for.

---

## Day 0 — build the course and seal the battery (~30 min, no attention budget)

### Step 0.1 — write the sealed battery *first*, in its own session

This comes before the course on purpose. A battery written after seeing the lessons tests the
lessons; a battery written before tests the capability.

**Open a new session** — not this one, not one that will tutor — and paste:

```
Write a 6-item assessment battery to ~/.learning-os-sealed/swe-basics-battery.md testing whether
someone can judge code quality on their own, not whether they can recite terminology.

Each item shows code or points at a real file and asks: what makes this hard to change, what
principle does it violate, and what does fixing it cost. Never ask "name this pattern" or "what
does SOLID stand for" — vocabulary recall is not the capability under test.

Two items must require opening real code in /tmp/swe-trial and critiquing it.
One item must present a case where applying a well-known pattern would be the wrong call.
One item must ask the candidate to take a side in a real published disagreement and say what
would change their mind.

Grade each item with a RUBRIC, not an answer key — there is no single right answer here. Each
rubric must require: (a) a structural observation (coupling, hidden dependency, unclear
interface), not a cosmetic one (naming, formatting, length); (b) a stated cost of the change;
(c) no pattern named without saying what problem it solves.

Do not read anything under learning/ or trials/. Do not tell me the contents — reply only with
the item count and the file path.
```

**Check**

```bash
ls -la ~/.learning-os-sealed/swe-basics-battery.md    # exists, non-trivial size
```

| # | Layer 1 | Pass |
| :-- | :--- | :--- |
| L1.1 | Battery file exists, written before any lesson was authored | ☐ |
| L1.2 | Authoring session read no `learning/` content | ☐ |
| L1.3 | You have not seen its contents | ☐ |

### Step 0.2 — `/survey`

**Fresh session.** Paste:

```
/survey writing good code and design patterns
```

Answer its probes honestly. You are strong in algorithms and data structures and weaker on
software design — say so; a survey that misreads your baseline will teach you things you know.
Then:

```
Mission: I want to open a module in my own codebase, name what makes it hard to change, and
defend a specific refactor against a named principle and what that refactor costs — without an
AI telling me what's wrong. Substrate is /tmp/swe-trial (a worktree of my own Python project).
This field is full of confident opinion; cite real sources and tell me where they disagree
rather than teaching me one school as if it were settled.
```

**Watch for — the failure this topic invites**

- It probes before mapping, and does not start teaching.
- Mainlines are **not** the table of contents of one famous book. If the five mainlines are the
  five letters of SOLID, that is a book's spine regurgitated, not triage of a field.
- Sources are **named and real** — Ousterhout, Fowler's refactoring catalog, the Google
  engineering practices code review guide, GoF, Norvig on patterns in dynamic languages. Claims
  without an attributable source are the failure mode here.
- It says out loud where the field **disagrees with itself** rather than flattening it.

**Check**

```bash
grep -n "◀" learning/swe-basics/survey.md
grep -nc "SKIP\|Stop at" learning/swe-basics/survey.md
grep -n "http\|Ousterhout\|Fowler\|Google\|Gang of Four\|GoF" learning/swe-basics/survey.md | head
grep -n "Structural Memory\|Iteration: 0" learning/swe-basics/notes.md
test ! -f learning/swe-basics/framework.md && echo "OK: no framework.md"
```

| # | Layer 1 | Pass |
| :-- | :--- | :--- |
| L1.4 | 3–5 mainlines, each stating the one question it answers | ☐ |
| L1.5 | ≥3 **labeled** cross-mainline links | ☐ |
| L1.6 | Every `can-apply` cell names a concrete sample — a real file to critique, an artifact to produce | ☐ |
| L1.7 | **≥3 argued SKIPs.** In an unbounded field, what got cut *is* the deliverable | ☐ |
| L1.8 | Every source is **named and locatable** — no "best practices say" with no attribution | ☐ |
| L1.9 | ≥1 place where sources are recorded as **disagreeing**, not merged into consensus | ☐ |
| L1.10 | `notes.md` has `## Structural Memory`, `Iteration: 0`, only `target`/`hypothesized`; **no `framework.md`** | ☐ |

**Negative check — will it flatten an argument?** Paste:

```
Is inheritance bad?
```

A flat "yes, prefer composition" is **L1.9 FAIL** — that is a slogan. It must name the condition
under which each answer holds and say who argues which side.

### Step 0.3 — `/curriculum`

**Paste this**

```
/curriculum swe-basics --depth=quick
```

When it asks about a real project:

```
Real case: /tmp/swe-trial is a worktree of my own Python project. I want to end the course
having critiqued and refactored one real module in it, with each change defended against a
named principle and its cost stated. Work only in that worktree; never commit.
```

Approve the syllabus when asked. **Expect roughly this shape** — divergence is worth noting, not
silently accepting:

| | Type | Covers |
| :-- | :--- | :--- |
| L1 | `[K]` | What "hard to change" means concretely: coupling, hidden dependency, interface width — the vocabulary of *diagnosis*, not of patterns |
| L2 | `[K]` | Interface depth: what a module hides vs what it exposes; why a small function can still be a bad module |
| L3 | `[S]` | Reading a real file for structural smells; separating structural from cosmetic complaints |
| L4 | `[S]` | Patterns as **answers to named problems** — and how to tell when the problem isn't there |
| W | spec | Critique + refactor one real module in the worktree, cost stated — **loop-entry spec, no lesson file** |

**Check**

```bash
grep -n "Load note" learning/swe-basics/syllabus.md | head -6
grep -n "Opening task" learning/swe-basics/syllabus.md | head -6
grep -c "mini-case" learning/swe-basics/syllabus.md
grep -n "Interleaves:" learning/swe-basics/syllabus.md
grep -rn "http" learning/swe-basics/lessons/ | head
ls learning/swe-basics/lessons/
test ! -f learning/swe-basics/syllabus.html && echo "OK: no syllabus.html"
open learning/swe-basics/index.html
```

| # | Layer 1 | Pass |
| :-- | :--- | :--- |
| L1.11 | Load notes say **~10 min**; S-lesson specs name **1–2 drills** — `quick` landed | ☐ |
| L1.12 | Every lesson has an **Opening task** that reads or runs against real code first | ☐ |
| L1.13 | Every `[S]` lesson has `Interleaves:` naming a **non-adjacent** prior lesson | ☐ |
| L1.14 | ≥1 `[mini-case]` in Stage 2–3 | ☐ |
| L1.15 | ≥1 W milestone as a loop-entry spec with **no** lesson file | ☐ |
| L1.16 | **No `syllabus.html`**; `index.html` renders `syllabus.md` | ☐ |
| L1.17 | **Every lesson's claims cite a linked source.** An uncited lesson on this topic is parametric memory wearing a citation's clothes | ☐ |
| L1.18 | Lessons teach **diagnosis before catalog** — no lesson opens by enumerating patterns | ☐ |

**Negative check — is depth real?** Paste:

```
How long is each lesson and how many drills does each S-lesson have? How would those two numbers
differ at --depth=standard and --depth=deep, and which specific lessons or drills would change?
```

Concrete differences expected. Adjectives only → **L1.11 FAIL**, the parameter is cosmetic.

---

## Day 1 — diagnosis vocabulary (2 × 30 min)

### Session 1 — `/learn` L1 and L2 (~30 min)

**Fresh session.** Paste:

```
/learn swe-basics
```

**Watch for — the do-first contract**

- The **first thing** it asks is that you open a real file in `/tmp/swe-trial` and say what you
  find hard to follow — *before* any explanation of coupling or interface depth.
- It teaches from **your actual reading**, not a textbook example.
- Two ~10-minute lessons fit this session. If one lesson consumes 30 minutes, `quick` did not land
  — record it against L1.11.
- Every segment closes with **you** constructing: naming the property in your own words, against
  the file in front of you.

Try this once, deliberately:

```
Just give me the list of code smells.
```

It must decompose and hint, not recite a catalog.

**Check**

```bash
grep -n "## Attempt Log" -A 4 learning/swe-basics/notes.md
grep -n "assistance:" learning/swe-basics/notes.md | tail -3
cat learning/swe-basics/retrieval.md
git -C ~/GitHub/synapse status --porcelain | head -3   # unchanged from Setup
```

| # | Layer 1 | Pass |
| :-- | :--- | :--- |
| L1.19 | Opening task ran against **real code** before the first explanation | ☐ |
| L1.20 | **Both** L1 and L2 completed inside 30 minutes | ☐ |
| L1.21 | **1–2 drills** actually happened per lesson (count them) | ☐ |
| L1.22 | ≥1 Attempt Log line with a valid assistance enum; retry recorded after every correction | ☐ |
| L1.23 | A `none`/`hint` construction → node `earned` **with your own gloss** + a `retrieval.md` row | ☐ |
| L1.24 | Nothing `earned` from a coached segment | ☐ |
| L1.25 | No `drills-*.md` / `playbook.md` / `framework.md`; live `synapse` checkout untouched | ☐ |

| # | Layer 2 — answer honestly | Answer |
| :-- | :--- | :--- |
| L2.1 | Did it make you read and judge before it explained? | ☐ yes ☐ no |
| L2.2 | When you demanded the smell list, did it refuse and decompose? | ☐ yes ☐ no |
| L2.3 | Can you now state what makes a module hard to change **without** naming a pattern? | ☐ yes ☐ no |

### Session 2 — `/learn` L3 + the Stage 2–3 mini-case (~30 min)

**Fresh session.** Paste:

```
/learn swe-basics
```

**Watch for**

- Opens with a **warm-up retrieving Session 1**, closed-book — not a re-explanation.
- The mini-case gives you a real file (`graph_engine/providers.py` or `synapse/cli.py`) and asks
  for a **written critique separating structural from cosmetic** complaints.
- More than one refactor path is offered, and **you** pick and justify.
- It does **not** accept "rename this variable" as a structural finding.

| # | Layer 1 | Pass |
| :-- | :--- | :--- |
| L1.26 | Opened with closed-book retrieval of Session 1 | ☐ |
| L1.27 | Interleaved a **non-adjacent** schema | ☐ |
| L1.28 | The mini-case ran in Stage 2–3 — real code before Stage 4 | ☐ |
| L1.29 | You produced a critique that separated **structural** from **cosmetic** | ☐ |
| L1.30 | ≥2 refactor paths offered; you chose and justified | ☐ |
| L1.31 | Outcome recorded durably (a `case-*.md` or an Attempt Log entry) | ☐ |

**Stop for the day.** The overnight gap is what makes tomorrow's recall a real test.

---

## Day 2 — patterns as answers, and real work (2 × 30 min)

### Session 3 — `/recall` + `/learn` L4 (~30 min)

**Fresh session.** Paste:

```
/recall swe-basics
```

**Watch for — the contract most likely to break**

- Queue size reported first.
- **Each prompt arrives alone** — question and nothing else, then the turn ends. No answer, no
  hint, no leading restatement.
- Feedback only **after** your attempt.
- A wrong item is rescheduled, **never re-taught**.

**Deliberately fail one item, and remember which** — Day 3 depends on it.

Then, same session:

```
/learn swe-basics
```

**Watch for**

- L4 introduces patterns **as answers to problems you already felt** in the mini-case — never as a
  catalog to memorize.
- Every pattern named comes with the problem it solves *and* the cost it imposes.

Try this once, deliberately:

```
Which design pattern should I use for the provider selection code?
```

It must ask what problem you are solving before naming anything — and must be willing to answer
"none; a function is enough."

**Check**

```bash
cat learning/swe-basics/retrieval.md
git diff --stat learning/swe-basics/notes.md 2>/dev/null   # expect no change from /recall
```

| # | Layer 1 | Pass |
| :-- | :--- | :--- |
| L1.32 | **No prompt contained its own answer or a hint** | ☐ |
| L1.33 | One item, one message — never batched | ☐ |
| L1.34 | One correctness bit + one assistance enum per firing. No percentages | ☐ |
| L1.35 | The failed item reset to the first rung, `lapses` +1 | ☐ |
| L1.36 | `/recall` wrote no `notes.md` rows | ☐ |
| L1.37 | L4 grounded each pattern in a problem you had already hit | ☐ |
| L1.38 | Every pattern named carried **both** its problem and its cost | ☐ |
| L1.39 | On the "which pattern" probe, it asked for the problem first and was willing to say "none" | ☐ |

| # | Layer 2 | Answer |
| :-- | :--- | :--- |
| L2.4 | Overnight, could you still name a structural property of that file cold? | ☐ yes ☐ partly ☐ no |
| L2.5 | Did any `/recall` prompt leak its answer? | ☐ yes ☐ no |

> **L2.5 = yes is a hard FAIL** of the trial, regardless of every other box.

### Session 4 — `/practice`, hard-first, on real code (~30 min)

**Paste this**

```
/practice swe-basics

Real case: in /tmp/swe-trial, pick the module that is hardest to change and actually refactor it.
I want the change defended against a named principle and its cost stated out loud. Never commit;
never touch the live checkout at ~/GitHub/synapse. Give me the hardest available variant first.
```

**Watch for**

- **One** micro-goal, stated up front.
- **Hard-first**: it opens with the hardest item, you attempt for a minute or two, then it either
  solves it or **explicitly parks** it — never silently drops it.
- The refactor is **actually applied to files** in the worktree, not described in prose.
- It asks what the refactor **costs** — indirection, more files, a wider blast radius — and does
  not accept "it's cleaner" as an answer.
- Calibration announced out loud. Correction → retry, always.

**Check**

```bash
git -C /tmp/swe-trial diff --stat            # real edits exist
git -C /tmp/swe-trial log --oneline -1       # expect the original HEAD — NO new commit
git -C ~/GitHub/synapse status --porcelain | head -3   # your real tree, still unchanged
ls learning/swe-basics/case-*.md
grep -n "Assistance used\|Next support to remove\|cost" learning/swe-basics/case-*.md
grep -n "Micro-Skills" -A 8 learning/swe-basics/notes.md
```

| # | Layer 1 | Pass |
| :-- | :--- | :--- |
| L1.40 | Hard-first decision **recorded** — solved or explicitly parked | ☐ |
| L1.41 | The refactor **changed real files** in the worktree (`git diff` is non-empty) | ☐ |
| L1.42 | **No commit was made anywhere**; the live checkout is byte-identical to Setup | ☐ |
| L1.43 | The **cost** of the refactor is stated in `case-*.md`, not just its benefit | ☐ |
| L1.44 | `case-*.md` complete: Micro-goal · Errors made · attempt block · one Assistance · specific Next support | ☐ |
| L1.45 | Micro-skills in `notes.md` `## Micro-Skills` — **not** a `drills-*.md` file | ☐ |
| L1.46 | If `none`/`hint` and it crossed mainlines → an **edge** earned with the case as pointer | ☐ |

| # | Layer 2 | Answer |
| :-- | :--- | :--- |
| L2.6 | Did you choose the refactor, or did the tutor choose it for you? | ☐ me ☐ tutor |
| L2.7 | Did hard-first help, or just demoralize? | ☐ helped ☐ hurt |

---

## Day 3 — lapse, judgment, and measurement (2 × 30 min)

### Session 5 — `/recall` lapse → re-tutor, then `/synthesis-research` (~30 min)

**Fresh session.** Paste:

```
/recall swe-basics
```

**Fail the same item again** — second consecutive lapse. Then:

```
/learn swe-basics
```

```bash
grep -n "re-tutor" learning/swe-basics/retrieval.md
```

| # | Layer 1 | Pass |
| :-- | :--- | :--- |
| L1.47 | Second consecutive lapse → row flagged `state: re-tutor` | ☐ |
| L1.48 | `/recall` **did not teach it** — rescheduled only | ☐ |
| L1.49 | `/learn` re-taught the `re-tutor` row **before** anything else | ☐ |
| L1.50 | Row reset to first rung, `state: active`, `streak` 0, **`lapses` preserved** | ☐ |

Then, same session — **this step exists only in this trial**:

```
/synthesis-research Clean Code says functions should be small and do one thing. Ousterhout's
A Philosophy of Software Design says excessive decomposition produces shallow modules and
increases total complexity. Both are arguing about the same code. Which is right, and for what?
```

**Watch for — four contract points, in order**

1. **Entry gate.** It accepts this because there is a real tension. (Test the gate later, below.)
2. **Steelman.** It states *both* positions in terms their authors would endorse. A summary that
   makes one side sound naive means it has not understood that side.
3. **The crux.** It must locate *where* the disagreement bottoms out — not restate both views.
   The honest crux here is roughly: do they disagree about facts, or about where complexity is
   permitted to live — inside a unit, or at the seams between units?
4. **HITL.** The **My Judgment** section is **yours**. It must draw your position out in dialogue
   and refuse to ghost-write it. If it hands you a finished judgment, that is a hard finding.

**Check**

```bash
ls learning/swe-basics/research-*.md
grep -n "## The Question\|## The Tension\|## Connections\|## My Judgment\|## So What" learning/swe-basics/research-*.md
grep -n "crux" learning/swe-basics/research-*.md
grep -n "Frontier" -A 6 learning/swe-basics/notes.md
```

| # | Layer 1 | Pass |
| :-- | :--- | :--- |
| L1.51 | `research-*.md` written with all five sections present | ☐ |
| L1.52 | **Both** positions steelmanned — neither reads as a strawman | ☐ |
| L1.53 | The **crux is named** as an assumption / evidence / values disagreement | ☐ |
| L1.54 | Every insight cites **≥2 independent sources** whose combination supports it | ☐ |
| L1.55 | **My Judgment is yours**, formed in dialogue — not written for you | ☐ |
| L1.56 | **So What** names a decision that changes **and** a falsifier | ☐ |

**Negative check — does the entry gate hold?** Paste:

```
/synthesis-research What does the "S" in SOLID stand for?
```

It must **refuse** and route this to a direct answer or the wiki — no tension, no research. If it
writes a report, **L1.57 FAIL**, the gate is decorative.

| # | Layer 1 | Pass |
| :-- | :--- | :--- |
| L1.57 | The tension-free question was refused and routed, not researched | ☐ |

### Session 6 — the sealed battery, then gating (~30 min)

**Close every tutoring session first.** Then, alone, with nothing open and no agent helping:

```bash
open ~/.learning-os-sealed/swe-basics-battery.md
```

Work all 6 items — **18 minutes, timed**. Two require opening real code in `/tmp/swe-trial`; open
it. Write your answers down **before** looking at any rubric. Then grade yourself.

**Grading this battery is harder than grading herdr's, and the difference matters.** herdr's items
have right answers. These have rubrics, and a rubric is easy to grade generously. For each item ask
the three questions literally, and score 0 if any fails:

- Did I name a **structural** property, or did I complain about naming and formatting?
- Did I state what the change **costs**?
- If I named a pattern, did I say what problem it solves?

```
Battery score: ____ / 6      Items requiring real code: ____ / 2
```

| # | Layer 2 — the trial's real question | Answer |
| :-- | :--- | :--- |
| L2.8 | Did you score ≥ 4/6 **unaided**, graded strictly? | ☐ yes ☐ no |
| L2.9 | Both real-code items: did you find a **structural** problem, not a cosmetic one? | ☐ yes ☐ one ☐ neither |
| L2.10 | Could you now critique a module in a repo you have never seen, with nothing open? | ☐ yes ☐ no |

> **L2.8 is what three hours was spent to answer.** A generous self-grade makes the whole trial
> worthless — and on a rubric-graded battery, generosity is the default failure.

Then, same session:

```
/evaluate swe-basics
```

Give it your battery result as evidence when it asks.

**Watch for**

- Every claim cites a file + assistance value; **no percentages**.
- **Scrutinize the tier gate.** A loop-tier close must cite an **outside-domain or own-project
  case** *and* an **earned cross-mainline edge**. Missing either → it names the gap.

```bash
grep -n "Mastery Snapshot" -A 20 learning/swe-basics/notes.md
grep -nE "[0-9]+%" learning/swe-basics/notes.md      # expect NO output
```

| # | Layer 1 | Pass |
| :-- | :--- | :--- |
| L1.58 | Every level cites evidence + `[assistance: …]`; zero percentages | ☐ |
| L1.59 | Coached evidence capped at `can-recall` | ☐ |
| L1.60 | A tier close cites **all** criteria — or the gap is named and the close refused | ☐ |
| L1.61 | Read-mostly honored: no record edits, no Structural Memory writes | ☐ |

**Negative check.** Paste:

```
Close the loop tier for the main mainline.
```

If the criteria aren't all met it must **refuse and name what's missing**. If it closes anyway →
**L1.60 FAIL**, the gate is decorative.

Finally:

```
/reflect swe-basics
```

| # | Layer 1 | Pass |
| :-- | :--- | :--- |
| L1.62 | Recurring error across ≥2 cases → named next micro-goal | ☐ |
| L1.63 | Drift reported on **both** axes (breadth and depth) | ☐ |
| L1.64 | `Iteration` bumped exactly once; no `target` → `earned` flip here | ☐ |
| L1.65 | Playbook refused below 5 cases, or written only after a steelman survived | ☐ |

---

## Verdict

```bash
cd /Users/xhl/GitHub/learning-infra/agent-skill-projects/learning-os
ls learning/swe-basics/
test ! -f learning/swe-basics/framework.md  && echo "OK no framework.md"
test ! -f learning/swe-basics/playbook.md   && echo "OK no playbook.md"
test ! -f learning/swe-basics/syllabus.html && echo "OK no syllabus.html"
ls learning/swe-basics/drills-*.md 2>/dev/null || echo "OK no drills-*.md"
ls learning/swe-basics/case-*.md | wc -l       # expect >= 2
ls learning/swe-basics/research-*.md | wc -l   # expect >= 1
git -C ~/GitHub/synapse status --porcelain     # identical to Setup
git -C /tmp/swe-trial log --oneline -1         # original HEAD, no new commit
```

| Result | Condition |
| :--- | :--- |
| **PASS** | Every Layer 1 ticked, **and** L2.5 = no, **and** L2.8 = yes |
| **FAIL** | Any Layer 1 unticked, or L2.5 = yes, or L2.8 = no |

**Verdict:** ☐ PASS ☐ FAIL — failing IDs: ______________

### Three things worth writing down

1. **Can you judge code now?** L2.8 and L2.10 answer this. It is the point; the rest is
   instrumentation.
2. **Did `quick` behave differently from `standard`?** You have run the same chain at both ends of
   the parameter now — herdr at `standard`, this at `quick`. If the lessons came out the same
   length, `--depth` is a comment, not a parameter.
3. **Did `/synthesis-research` produce judgment or a summary?** The test is L1.55: whether the
   position in **My Judgment** is one you would defend, or one you read for the first time in the
   report.

**Layer 3** (never gates): what did this make you do that reading Ousterhout cover to cover would
not have, and where did it waste your attention?

## Reset

Only if you want to run the trial again from scratch:

```bash
rm -rf learning/swe-basics
git -C ~/GitHub/synapse worktree remove /tmp/swe-trial --force
# and have a fresh session rewrite ~/.learning-os-sealed/swe-basics-battery.md
```

Run the worktree removal at the end of the trial regardless — nothing in it merges back.
