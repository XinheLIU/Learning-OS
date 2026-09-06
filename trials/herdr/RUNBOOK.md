# Herdr Trial — RUNBOOK

Last updated: 2026-09-06

**Goal: learn herdr well enough to safely delegate a real repository task to an agent through it —
in 3 hours, across 3 days.** You are both the learner and the tester.

| | |
| :--- | :--- |
| Topic | herdr — the terminal multiplexer for coding agents (v0.8.0 installed) |
| Depth | `standard` (~20–30 min lessons, 2–3 drills each) |
| Budget | 60 min of your attention per day × 3 days |
| Day 3 test | A sealed battery, written before any teaching, opened only at measurement time |

**Why `standard` and not `deep`.** A `deep` lesson runs 60–90 minutes. Three of them would consume
the entire budget and leave nothing for practice, retrieval, or the independence test. At
`standard`, a day fits two lessons plus real practice. Depth serves the budget, not the reverse.

## Safety boundary — read before anything else

herdr manages **your live terminal**, including panes you are working in. These are not
suggestions.

- **Never** stop the server, or close, move, rename, resize, or send input to a pane that existed
  before the trial. Only trial-created panes may be touched or cleaned up.
- Use `--no-focus` for creation, and explicit IDs **captured from returned JSON** — never an ID you
  guessed or predicted.
- **Never run bare `herdr` from inside herdr.**
- The **installed CLI is the syntax authority**, not anyone's memory of it. Discovery starts at
  `herdr --help`, then the relevant command group *without* a mutating subcommand.

If a step would violate any of these, stop and record **NOT RUN**. Do not improvise a substitute.

## Session hygiene — what makes the Day 3 number mean anything

| Session | May see | Must never see |
| :--- | :--- | :--- |
| Battery author (Day 0) | the herdr CLI | any tutoring, any lesson |
| Tutor (Days 1–3) | the CLI, your notes | **the battery** |
| You | everything, at the end | the battery before Day 3 |

**Run each day's tutoring in a fresh session.** A session that has read the battery cannot honestly
teach against it — it will teach to the test without meaning to.

Do **not** print, `cat`, `grep`, hash, summarize, or "just check the length of" the battery before
Day 3. Confirming the file exists is the only permitted interaction.

## Setup

```bash
cd /Users/xhl/GitHub/learning-infra/agent-skill-projects/learning-os
command -v herdr && herdr --version          # expect 0.8.0 or later
echo "HERDR_ENV=${HERDR_ENV:-unset}"          # must be 1 — you must be inside herdr
ls learning/herdr 2>/dev/null && echo "STOP: move it aside first"
if [ -d learning/herdr-v1 ]; then ls learning/herdr-v1/ | head -3; else echo "NOTE: v1 archive is not present in this checkout"; fi
```

If `HERDR_ENV` is unset you are not inside a herdr-managed session, and none of the commands in
this runbook will behave correctly. Start one first.

> **The v1 archive is reference, not input.** When present, `learning/herdr-v1/` holds the earlier
> partial course. This is a clean restart — do not feed it to `/survey` or `/curriculum`, and do not
> read it before Day 1, or you will contaminate your own baseline. It is there so you can compare the
> earlier chain with this v3 output **after** the trial ends. A checkout without that gitignored
> archive is still runnable; record the comparison as NOT AVAILABLE.

---

## Day 0 — build the course and seal the battery (~25 min, no attention budget)

### Step 0.1 — write the sealed battery *first*, in its own session

This comes before the course on purpose. A battery written after seeing the lessons tests the
lessons; a battery written before tests the topic.

**Open a new session** — not this one, not the one that will tutor — and paste:

```
Read the installed herdr CLI surface (herdr --help, then each command group's help without
running any mutating subcommand). Then write an 8-item assessment battery to
~/.learning-os-sealed/herdr-battery.md covering: the object hierarchy and what persists across
detach vs restart; how to target a pane safely without stealing focus; when to use the pane
surface versus the agent surface; and how to tell a finished agent from a stuck one.

Each item: one question, answerable in 1–3 lines or one command, plus the expected answer and a
one-line grading note. Two items must require running a real command and reading its output.

Do not read anything under learning/ or trials/. Do not tell me the contents — reply only with
the item count and the file path.
```

**Check**

```bash
ls -la ~/.learning-os-sealed/herdr-battery.md    # exists, non-trivial size
```

| # | Layer 1 | Pass |
| :-- | :--- | :--- |
| L1.1 | Battery file exists, written before any lesson was authored | ☐ |
| L1.2 | Authoring session read no `learning/` content | ☐ |
| L1.3 | You have not seen its contents | ☐ |

### Step 0.2 — `/survey`

**Fresh session.** Paste:

```
/survey herdr
```

Answer its probes honestly — you are a genuine novice on this restart. Then:

```
Mission: I want to hand a real repository task to a coding agent through herdr and know it ran
safely — without stealing my focus, without touching panes I'm working in, and knowing whether
the agent finished or is stuck. Target can-transfer on safe delegation. The installed CLI is the
syntax authority; don't teach me from memory of other multiplexers.
```

**Watch for**

- It probes before mapping, and does not start teaching.
- It grounds the map in `herdr --help` output, not in tmux/screen analogies.
- Targets **differ per mainline** — a survey where every row targets `can-transfer` didn't triage.

**Check**

```bash
grep -n "◀" learning/herdr/survey.md
grep -n "SKIP\|Stop at" learning/herdr/survey.md
grep -n "Structural Memory\|Iteration: 0" learning/herdr/notes.md
test ! -f learning/herdr/framework.md && echo "OK: no framework.md"
```

| # | Layer 1 | Pass |
| :-- | :--- | :--- |
| L1.4 | 3–5 mainlines, each stating the one question it answers | ☐ |
| L1.5 | ≥3 **labeled** cross-mainline links | ☐ |
| L1.6 | Every `can-apply` cell names a concrete sample (a command to run, an outcome to produce) | ☐ |
| L1.7 | Targets differ across mainlines; ≥1 argued SKIP / stop-early | ☐ |
| L1.8 | `notes.md` has `## Structural Memory`, `Iteration: 0`, only `target`/`hypothesized` | ☐ |
| L1.9 | **No `framework.md`** (v3 contract: Structural Memory lives in `notes.md`) | ☐ |

### Step 0.3 — `/curriculum`

**Paste this**

```
/curriculum herdr --depth=standard
```

When it asks about a real project:

```
Real case: I want to delegate an actual task in /Users/xhl/GitHub/learning-infra/agent-skill-projects/learning-os to a named agent
through herdr and read back its result — without disturbing any pane I already have open.
```

Approve the syllabus when asked. **Expect roughly this shape** — if it diverges wildly, that is
worth noting, not silently accepting:

| | Type | Covers |
| :-- | :--- | :--- |
| L1 | `[K]` | session → workspace → tab → pane; the agent as a pane *occupant*, not a layout level; detach vs restart |
| L2 | `[K]` | explicit targeting: returned IDs over guessed ones, `--no-focus`, `pane run` / `wait-output` / `read` |
| L3 | `[S]` | pane surface vs agent surface; agent identity and lifecycle; `done` vs `idle` vs `unknown` |
| W | spec | a one-page runbook for safely delegating a real repo task — **loop-entry spec, no lesson file** |

**Check**

```bash
grep -n "Load note" learning/herdr/syllabus.md | head -4
grep -n "Opening task" learning/herdr/syllabus.md | head -4
grep -c "mini-case" learning/herdr/syllabus.md
grep -n "Interleaves:" learning/herdr/syllabus.md
ls learning/herdr/lessons/
test ! -f learning/herdr/syllabus.html && echo "OK: no syllabus.html"
open learning/herdr/index.html
```

| # | Layer 1 | Pass |
| :-- | :--- | :--- |
| L1.10 | Load notes say **~20–30 min**; S-lesson specs name **2–3 drills** — depth landed | ☐ |
| L1.11 | Every lesson has an **Opening task** that runs a real `herdr` command | ☐ |
| L1.12 | Every `[S]` lesson has `Interleaves:` naming a **non-adjacent** prior lesson | ☐ |
| L1.13 | ≥1 mini-case in Stage 2–3 **with its own lesson file** (v3) | ☐ |
| L1.14 | ≥1 W milestone as a loop-entry spec with **no** lesson file | ☐ |
| L1.15 | **No `syllabus.html`**; `index.html` renders `syllabus.md` | ☐ |
| L1.16 | Lessons cite the **installed CLI's** output, not remembered syntax | ☐ |
| L1.16b | Every lesson ends in a **checkpoint block** (manifest button + next-step card) | ☐ |
| L1.16c | `recall.html` exists and links from `index.html`; `assets/recall.js` present | ☐ |
| L1.16d | `syllabus.md` lessons carry `Next:` fields; L3 carries a recall `Gate:` | ☐ |

**Negative check — is depth real?** Paste:

```
How long is each lesson and how many drills does each S-lesson have? How would those two numbers
differ at --depth=quick and --depth=deep, and which specific lessons or drills would change?
```

Concrete differences expected. Adjectives only → **L1.10 FAIL**, the parameter is cosmetic.

---

## Day 1 — topology and safe targeting (~60 min)

### Step 1.1 — `/learn` L1 (~22 min)

**Fresh session.** Paste:

```
/learn herdr
```

**Watch for — the v3 start contract**

- It revises the lesson against `notes.md`, opens it (`open lessons/0001-*.html`), reports any due
  recall items — and **stops**. No tutoring in chat.
- The **lesson itself** runs the do-first contract: the opening task (run `herdr workspace list`,
  `herdr pane list`) sits at the top of the page, before any explanation of the hierarchy.
- You work the page: opening task, reading, the Check-yourself quiz. Answers lock in the browser.

Then close the lesson from its checkpoint block: click **Copy completion manifest** and paste:

```
done L1
<pasted manifest>
```

**Watch for — bookkeeping, not re-teaching**

- It parses the manifest, infers assistance from the pattern (locked-correct-first-try → `none`),
  writes the Attempt Log / records / terms, promotes nodes, opens ledger rows, checks the syllabus
  box — and says what's next. At most **one** spot-probe question, and only if the pattern is
  ambiguous. It does not re-quiz the lesson.

Try this once, deliberately, **after** `done L1`:

```
Just tell me the full object hierarchy.
```

In tutor mode it must still decompose and hint, not recite.

**Check**

```bash
grep -n "## Attempt Log" -A 4 learning/herdr/notes.md
grep -n "assistance:" learning/herdr/notes.md | tail -3
cat learning/herdr/retrieval.md
```

| # | Layer 1 | Pass |
| :-- | :--- | :--- |
| L1.17 | Opening task ran **before** the first explanation — in the page, not chat | ☐ |
| L1.18 | The quiz items actually happened in the browser (count them in the manifest) | ☐ |
| L1.19 | ≥1 Attempt Log line with a valid assistance enum inferred from the manifest | ☐ |
| L1.20 | A `none`/`hint` construction → node `earned` **with your own gloss** + a `retrieval.md` row | ☐ |
| L1.21 | Nothing `earned` from a coached item (revealed-without-draft → `walkthrough`, no row) | ☐ |
| L1.22 | No standalone `drills-*.md` / `playbook.md` / `framework.md`; consolidated sections are in `notes.md` | ☐ |
| L1.23 | No pre-existing pane was touched | ☐ |
| L1.23b | `done` bookkeeping did not re-teach; ≤1 spot-probe | ☐ |

| # | Layer 2 — answer honestly | Answer |
| :-- | :--- | :--- |
| L2.1 | Did the page make you run and predict before it explained? | ☐ yes ☐ no |
| L2.2 | When you demanded the hierarchy outright (tutor mode), did it refuse and decompose? | ☐ yes ☐ no |
| L2.3 | Can you now state what survives a detach but not a server stop? | ☐ yes ☐ no |

### Step 1.2 — `/learn` L2 (~22 min)

**Paste this**

```
/learn herdr
```

**Watch for**

- Opens the revised L2 page and stops. The **page** opens with the opening task, then a warm-up
  retrieving L1, closed-book — not a re-explanation.
- The targeting invariant is *practiced in the page*, not just stated: you create a pane with
  `--no-focus`, capture its ID **from the returned JSON**, and act on that ID.
- Your focus never moves. If it does, that is a finding — record it.

Close with the checkpoint manifest: `done L2` + paste.

| # | Layer 1 | Pass |
| :-- | :--- | :--- |
| L1.24 | The page opened with closed-book retrieval of L1 (warm-up block) | ☐ |
| L1.25 | You captured a real pane ID from returned JSON and used it — never a predicted ID | ☐ |
| L1.26 | Your focus stayed put throughout | ☐ |
| L1.27 | If a misconception was recorded at `done L1`, this lesson was patched before opening | ☐ |

### Step 1.3 — the Stage 2–3 mini-case (~16 min)

The mini-case is a lesson file in v3. Paste:

```
/learn herdr
```

It opens `lessons/0004-mini-case-wait-and-read.html`. Work the scenario in your terminal, write
your command sequence in the page, compare against the reference, then `done mini-1` + paste.

**Watch for**

- A real scenario at walkthrough scaffolding — heavier than a drill, lighter than tomorrow's case.
- Two paths offered (`wait-output --match` vs polling `read`), and you pick and justify in the page.

| # | Layer 1 | Pass |
| :-- | :--- | :--- |
| L1.28 | The mini-case ran in Stage 2–3 as its own lesson file — real work before Stage 4 | ☐ |
| L1.29 | Outcome recorded durably (a `case-*.md` or an Attempt Log entry) after `done mini-1` | ☐ |
| L1.30 | Only trial-created panes were used | ☐ |

**Stop for the day.** The overnight gap is what makes tomorrow's recall a real test.

---

## Day 2 — agent surface and hard-first practice (~60 min)

### Step 2.1 — `/recall` (~12 min)

**Fresh session.** Paste:

```
/recall herdr
```

Before opening the page, capture a checksum so the no-`notes.md`-write assertion below is real
(the course directory is gitignored, so `git diff` cannot establish it):

```bash
shasum -a 256 learning/herdr/notes.md > /tmp/herdr-notes-before-recall.sha256
```

**Watch for — the v3 planner contract**

- Queue size reported first — counts and courses only, **no answers anywhere in chat**.
- It refreshes the `recall.html` queue and opens the page. The retrieval happens in the browser:
  each card shows the prompt alone; you answer from memory, then reveal, then grade yourself.
- Revealing before grading marks the item **peeked** — honest, not a clean pass.

**Deliberately fail one item, and remember which** — Day 3 depends on it.

Then sync: click **Copy recall results** and paste:

```
sync recall
<pasted manifest>
```

**Check**

```bash
cat learning/herdr/retrieval.md
shasum -a 256 learning/herdr/notes.md | diff - /tmp/herdr-notes-before-recall.sha256 && echo "OK: notes.md unchanged"
```

| # | Layer 1 | Pass |
| :-- | :--- | :--- |
| L1.31 | **No chat message contained an item's answer or a hint** | ☐ |
| L1.32 | Page cards showed the prompt alone until you revealed | ☐ |
| L1.33 | One correctness bit + one assistance enum per synced firing. No percentages | ☐ |
| L1.34 | The failed item reset to the first rung, `lapses` +1 | ☐ |
| L1.35 | `notes.md` untouched; no new rows created | ☐ |
| L1.35b | A peeked-first item synced as `walkthrough` (state `coached`), never `none` | ☐ |

| # | Layer 2 | Answer |
| :-- | :--- | :--- |
| L2.4 | Overnight, could you still state the targeting invariant cold? | ☐ yes ☐ partly ☐ no |
| L2.5 | Did any prompt leak its answer — in chat or on the page before your attempt? | ☐ yes ☐ no |

> **L2.5 = yes is a hard FAIL** of the trial, regardless of every other box.

### Step 2.2 — `/learn` L3, the agent surface (~23 min)

**Paste this**

```
/learn herdr
```

**Watch for**

- L3 has a recall gate (`Gate: start only when due recall items < 5`) — if your queue was longer,
  `/learn` should have routed you to `recall.html` first.
- The page's warm-up interleaves a **non-adjacent** schema (L1's topology, not L2's targeting).
- You start a **named** agent in a trial-created pane with the installed CLI's current shape
  (`herdr agent start <name> --kind <kind> --pane <returned-id>`), prompt it, wait, and read the
  result. Do not copy the older positional form from archived material.
- The distinction that matters gets *demonstrated*, not asserted: `done` (finished, unseen) vs
  `idle` (seen) vs `unknown` (herdr cannot classify — **not** proof of success).

Close with `done L3` + manifest. Expect the next-step message to name `/practice`.

| # | Layer 1 | Pass |
| :-- | :--- | :--- |
| L1.36 | Page warm-up interleaved a non-adjacent schema (spaced retrieval) | ☐ |
| L1.37 | You drove a real named agent through start → prompt → wait → read | ☐ |
| L1.38 | The `done` / `idle` / `unknown` distinction was demonstrated against live state | ☐ |

### Step 2.3 — `/practice`, hard-first (~25 min)

**Paste this**

```
/practice herdr

Real case: delegate a small but genuine task in /Users/xhl/GitHub/learning-infra/agent-skill-projects/learning-os to a named agent
through herdr, wait for it, and read back its result — without disturbing any pane I already
have open. Give me the hardest available variant first.
```

**Watch for**

- **One** micro-goal, stated up front.
- **Hard-first**: it opens with the hardest item, you attempt for a minute or two, then it either
  solves it or **explicitly parks** it — never silently drops it.
- Calibration announced out loud. Correction → retry, always.

**Check**

```bash
ls learning/herdr/case-*.md
grep -n "Assistance used\|Next support to remove" learning/herdr/case-*.md
grep -n "Micro-Skills" -A 8 learning/herdr/notes.md
```

| # | Layer 1 | Pass |
| :-- | :--- | :--- |
| L1.39 | Hard-first decision **recorded** — solved or explicitly parked | ☐ |
| L1.40 | `case-*.md` complete: Micro-goal · Errors made · attempt block · one Assistance · specific Next support | ☐ |
| L1.41 | Micro-skills in `notes.md` `## Micro-Skills` — **not** a `drills-*.md` file | ☐ |
| L1.42 | If `none`/`hint` and it crossed mainlines → an **edge** earned with the case as pointer | ☐ |
| L1.43 | No pre-existing pane disturbed; trial panes cleaned up | ☐ |

| # | Layer 2 | Answer |
| :-- | :--- | :--- |
| L2.6 | Did you drive the agent, or did the tutor drive it for you? | ☐ me ☐ tutor |
| L2.7 | Did hard-first help, or just demoralize? | ☐ helped ☐ hurt |

---

## Day 3 — lapse, sealed battery, gating (~60 min)

### Step 3.1 — `/recall`, lapse → re-tutor (~8 min)

**Paste this**

```
/recall herdr
```

Open `recall.html`, **fail the same item again** — second consecutive lapse — then `sync recall`
with the manifest.

```bash
grep -n "re-tutor" learning/herdr/retrieval.md
```

| # | Layer 1 | Pass |
| :-- | :--- | :--- |
| L1.44 | Second consecutive lapse → row flagged `state: re-tutor` | ☐ |
| L1.45 | **Nothing taught it** — not chat, not the page. Rescheduled only | ☐ |
| L1.46 | A refreshed queue **excludes** the `re-tutor` row | ☐ |

### Step 3.2 — `/learn` folds it into the next lesson (~8 min)

**Paste this**

```
/learn herdr
```

| # | Layer 1 | Pass |
| :-- | :--- | :--- |
| L1.47 | The `re-tutor` item was revised into the next lesson's warm-up/review — re-taught in the page, not chat | ☐ |
| L1.48 | Row reset to first rung, `state: active`, `streak` 0, **`lapses` preserved** | ☐ |

### Step 3.3 — the sealed battery (~30 min) — **the whole trial points here**

**Close every tutoring session first.** Then, alone, with no material open and no agent helping:

```bash
open ~/.learning-os-sealed/herdr-battery.md
```

Work all 8 items. Two require running real commands — run them. Write your answers down **before**
looking at any expected answer. Then grade yourself against the grading notes.

```
Battery score: ____ / 8      Items requiring a real command: ____ / 2
```

| # | Layer 2 — the trial's real question | Answer |
| :-- | :--- | :--- |
| L2.8 | Did you score ≥ 6/8 **unaided**? | ☐ yes ☐ no |
| L2.9 | Both command-execution items: did you produce working commands from memory? | ☐ yes ☐ one ☐ neither |
| L2.10 | Could you now delegate a real repo task through herdr with no reference open? | ☐ yes ☐ no |

> **L2.8 is what three hours was spent to answer.** Everything upstream exists to produce a `yes`.
> Record the honest number. A generous self-grade makes the whole trial worthless.

### Step 3.4 — `/evaluate` and the tier gate (~8 min)

**Paste this**

```
/evaluate herdr
```

Give it your battery result as evidence when it asks.

**Watch for**

- Every claim cites a file + assistance value; **no percentages**.
- **Scrutinize the tier gate.** A loop-tier close must cite an **outside-domain or own-project
  case** *and* an **earned cross-mainline edge**. Missing either → it names the gap rather than
  rounding up.

```bash
grep -n "Mastery Snapshot" -A 20 learning/herdr/notes.md
grep -nE "[0-9]+%" learning/herdr/notes.md      # expect NO output
```

| # | Layer 1 | Pass |
| :-- | :--- | :--- |
| L1.49 | Every level cites evidence + `[assistance: …]`; zero percentages | ☐ |
| L1.50 | Coached evidence capped at `can-recall` | ☐ |
| L1.51 | A tier close cites **all** criteria — or the gap is named and the close refused | ☐ |
| L1.52 | Read-mostly honored: no record edits, no Structural Memory writes | ☐ |

**Negative check.** Paste:

```
Close the loop tier for the main mainline.
```

If the criteria aren't all met it must **refuse and name what's missing**. If it closes anyway →
**L1.51 FAIL**, the gate is decorative.

### Step 3.5 — `/reflect` (~10–15 min)

**Paste this**

```
/reflect herdr
```

| # | Layer 1 | Pass |
| :-- | :--- | :--- |
| L1.53 | Recurring error across ≥2 cases → named next micro-goal | ☐ |
| L1.54 | Drift reported on **both** axes (breadth and depth) | ☐ |
| L1.55 | `Iteration` bumped exactly once; no `target` → `earned` flip here | ☐ |
| L1.56 | Playbook refused below 5 cases, or written only after a steelman survived | ☐ |

---

## Verdict

```bash
cd /Users/xhl/GitHub/learning-infra/agent-skill-projects/learning-os
ls learning/herdr/
test ! -f learning/herdr/framework.md  && echo "OK no framework.md"
test ! -f learning/herdr/playbook.md   && echo "OK no playbook.md"
test ! -f learning/herdr/syllabus.html && echo "OK no syllabus.html"
ls learning/herdr/drills-*.md 2>/dev/null || echo "OK no drills-*.md"
ls learning/herdr/case-*.md | wc -l    # expect >= 1 (the real /practice case)
grep -n "mini-1\|wait-and-read" learning/herdr/notes.md    # mini-case outcome is durable
```

| Result | Condition |
| :--- | :--- |
| **PASS** | Every Layer 1 ticked, **and** L2.5 = no, **and** L2.8 = yes |
| **FAIL** | Any Layer 1 unticked, or L2.5 = yes, or L2.8 = no |

**Verdict:** ☐ PASS ☐ FAIL — failing IDs: ______________

### Two things worth writing down

1. **Did you actually learn herdr?** L2.8 and L2.10 answer this. It is the point; the rest is
   instrumentation.
2. **Did v3 beat v1?** If `learning/herdr-v1/` is available, compare it with `learning/herdr/`
   side by side. Same topic, same budget. Did opening tasks, mini-cases, checkpoint manifests, and
   consolidated `notes.md` produce better retention on the battery — or just a differently-shaped
   pile of files? If the archive is absent, mark this comparison NOT AVAILABLE.

**Layer 3** (never gates): what did this make you do that reading `herdr --help` would not have,
and where did it waste your attention?

## Reset

Only if you want to run the trial again from scratch:

```bash
# Remove only the current trial course; this keeps any v1 archive if one exists.
rm -rf learning/herdr
# and have a fresh session rewrite ~/.learning-os-sealed/herdr-battery.md
```

Do **not** delete `learning/herdr-v1/` if it exists — it is the surviving record of the earlier chain.
