# Transformer Chapter Trial — RUNBOOK

Last updated: 2026-10-01

**Goal: turn a year of accumulated Transformer material — course notes, 50 diagrams, 290 files —
into one publishable book chapter you can defend without the file open.** You are both the author
and the tester.

| | |
| :--- | :--- |
| Materials | `/Users/xhl/GitHub/learning-infra/test/Transfomer/` — 290 files, 677 MB, 14 reference folders |
| Work directory | `tmp/transformer/` (gitignored) |
| Piece | `tmp/transformer/drafts/transformer/` — brief, draft, `assets/`, grill log |
| Language | Chinese first; the English mirror is `book-translator`'s job, out of scope here |
| Destination | `writing/MachineLearning/` — **you move the folder by hand**, after stage 7 |
| Design | [`docs/exec-plans/article-loop.md`](../../docs/exec-plans/article-loop.md) |

**Why this trial exists.** The learning trials (`herdr`, `swe-basics`) cover the learning loop end
to end; the writing and pipeline skills have had no trial coverage at all — the gap
[`docs/exec-plans/learning.md`](../../docs/exec-plans/learning.md) §7 names. This trial covers the
other half of the system: the concept-to-chapter loop, eight stages, four of them new skills.

**Why this material and not a clean corpus.** The folder is genuinely messy — off-topic images from
other projects, a 126-file code directory, courseware that duplicates the notes, three folders
(`06-Vision`, `07-Multimodal`, `08-Time-Series`) belonging to chapters that don't exist yet, and
filenames like `Classic Encoder-Decoder Transformer 2.png` that don't say what they show. A
selection map that can't handle this folder can't handle a real one.

## What's under test

| Property | Stage | How it's caught |
| :--- | :--- | :--- |
| **Coverage, not vibes** | 1 | Every one of 290 files is dispositioned. The residue diff is the assertion |
| **Skeleton before materials** | 1 | Sections must not be the folder tree. `01-Foundations` → §2 is a section named after a directory |
| **The gate is the author's** | 1 | Code-&-math decisions must appear in a transcript, not just in the brief |
| **Materials stay read-only** | 1–7 | A stat manifest, diffed after every stage before 8 |
| **Research entry gate** | 2 | Most of the §4 gaps are *lookups*, not tensions. `/synthesis-research` must refuse them |
| **Cut material stays cut** | 3 | No MoE-for-vision, no time-series, no courseware in the draft |
| **Image refs resolve** | 4, 7 | `verify_references.py`, twice — in place, then from a temp dir |
| **Chapter brief has no opponent** | 5 | `review-draft` must say so and skip, not invent a 正方 |
| **The author, not the text** | 6 | Anchors recorded, never shown before the answer |
| **Portability is proved, not claimed** | 7 | The `cp`-to-`mktemp` probe |
| **Archiving is additive** | 8 | Nothing deleted, nothing moved, two files written |

## Safety boundary — read before anything else

The materials folder is **someone's real library**, not a fixture.

- Stages 1–7 treat `$MAT` as **read-only**. Not one byte. The stat manifest check below is not
  advisory — if it fails, the stage failed, whatever else passed.
- Stage 8 is the only writer, and it is **additive**: two manifests at the root, plus renames you
  confirmed. No deletions, no moves between folders, ever.
- **No commits** in this repository or in `writing/`. The chapter's move into
  `writing/MachineLearning/` is yours to do by hand, after the trial.
- `tmp/` is gitignored. Nothing produced here is tracked.

If a step would violate any of these, stop and record **NOT RUN**. Do not improvise a substitute.

## Two properties that make this runbook a test

**Stages are re-runnable in isolation.** Each states its preconditions as file existence, so a
fixed skill can be re-tested without replaying the chain:

| Stage | Needs only |
| :--- | :--- |
| 1 `frame` | the materials folder |
| 2 `synthesis-research` | `brief.md` (its gap rows) |
| 3 `write-content` | `brief.md` + `research-*.md` |
| 4 images / diagrams | the draft + the materials folder |
| 5 `review-draft` ⇄ `edit-targeted` | `brief.md` + the draft |
| 6 `grill` | `brief.md` + the reviewed draft |
| 7 `package-chapter` | the draft folder |
| 8 `archive-materials` | `brief.md` + the shipped draft + the materials folder |

**One stage, one skill.** A failed assertion names the skill that owns the fix. If an assertion
fails and you can't say which skill should have prevented it, the assertion is the defect — fix the
runbook.

## Setup

```bash
cd /Users/xhl/GitHub/learning-infra/agent-skill-projects/learning-os
export MAT=/Users/xhl/GitHub/learning-infra/test/Transfomer
export WORK=tmp/transformer
export PIECE=$WORK/drafts/transformer
mkdir -p "$WORK"

# the denominator and the read-only baseline
find "$MAT" -type f ! -name '.DS_Store' | wc -l                  # expect 290
find "$MAT" -type f ! -name '.DS_Store' -exec stat -f '%N %z %m' {} \; \
  | sort > /tmp/transformer-materials.before

# per-directory file counts — the "nothing deleted, nothing moved" baseline for stage 8
find "$MAT" -type f ! -name '.DS_Store' -print0 | xargs -0 -n1 dirname \
  | sort | uniq -c > /tmp/transformer-dircounts.before

# the skill is discoverable
ls .claude/skills/frame .claude/skills/grill \
   .claude/skills/package-chapter .claude/skills/archive-materials
```

Re-run this after every stage 1–7:

```bash
find "$MAT" -type f ! -name '.DS_Store' -exec stat -f '%N %z %m' {} \; \
  | sort | diff /tmp/transformer-materials.before - && echo "OK: materials untouched"
```

---

## Stage 1 — chapter preparation (`frame` → `develop-argument` → `develop-examples`)

**Fresh session.** Paste:

```
/frame /Users/xhl/GitHub/learning-infra/test/Transfomer/

Write the brief to tmp/transformer/drafts/transformer/brief.md. Target is a chapter in my
MachineLearning book, Chinese first. There is no learning/ course for this topic — the material
came from external courses.

Then use /develop-argument on that brief for the teaching order and /develop-examples for
evidence, material selection and code/math. Ask only for unresolved author choices.
```

Answer unresolved framing, teaching-order and code/math choices honestly. When it asks what you got wrong about
Transformers, answer — that marker is the one thing in the chapter no source can supply.

**Watch for**

- `frame` reads the supplied context before proposing a reader question. `develop-examples`
  inventories selected source scope, using an existing material map when available.
- The skeleton arrives **filled in for Transformers** — §1 as a dependency chain
  (tokenization → embedding → PE → QKV → multi-head → block → masking → KV cache → LM head), not
  as five empty section names.
- Sections are **not** the folder tree. `01-Foundations` becoming §2 verbatim is the failure this
  stage exists to catch.
- `11-Code` (126 files) and `12-Courseware` (27) are dispositioned at **folder** granularity with a
  stated reason; the 50 images are dispositioned **individually**.
- `develop-examples` records code/math source, node and placement. It reuses supplied choices
  and asks only when a placement or teaching tradeoff remains open.
- It **never reads** the papers or notebooks it is cutting, and says so.

**Check**

```bash
test -f "$PIECE"/brief.md && grep -n 'brief-kind: chapter\|target-media: book-chapter' "$PIECE"/brief.md

# every scanned file covered — the residue must be empty
python3 - <<'PY'
import os, re, pathlib
mat = os.environ["MAT"]; piece = os.environ["PIECE"]
brief = pathlib.Path(piece, "brief.md").read_text()
rows = set(re.findall(r'`([^`]+)`', brief))
missing = []
for root, _, files in os.walk(mat):
    for f in files:
        if f == ".DS_Store": continue
        rel = os.path.relpath(os.path.join(root, f), mat)
        if any(rel == r or rel.startswith(r.rstrip("*/")) or r.rstrip("*/") in rel for r in rows):
            continue
        missing.append(rel)
print(f"uncovered: {len(missing)}")
print("\n".join(sorted(missing)[:20]))
PY

grep -c '| core \|| support \|| cut \|| gap \|inspect-on-demand' "$PIECE"/brief.md
grep -n 'Code & math' -A 12 "$PIECE"/brief.md      # every row has a placement
find "$MAT" -type f ! -name '.DS_Store' -exec stat -f '%N %z %m' {} \; \
  | sort | diff /tmp/transformer-materials.before - && echo "OK: materials untouched"
```

| # | Layer 1 | Pass |
| :-- | :--- | :--- |
| L1.1 | `brief.md` exists with `brief-kind: chapter` and `target-media: book-chapter` | ☐ |
| L1.2 | Residue is **empty** — every one of 290 files covered by a row or an ancestor-folder row | ☐ |
| L1.3 | Every 一层 section has ≥1 `core` row, or an explicit `gap` row | ☐ |
| L1.4 | Code & math table: every item has a source pointer **and** a placement (`inline` / `assets/code/…` / `cut`) | ☐ |
| L1.5 | Materials folder byte-identical — stat diff empty | ☐ |
| L1.6 | No prose section drafted anywhere in the brief | ☐ |

| # | Layer 2 | Pass |
| :-- | :--- | :--- |
| L2.1 | The three off-topic images (`Direct RPA and Agent Migration Roadmap`, `Repo Hygiene Portfolio DAG`, `Repo Hygiene Portfolio Roadmap`, `Parallel Claude Code Tickets`) are dispositioned `cut` | ☐ |
| L2.2 | `12-Courseware/**` and `06-Vision` / `07-Multimodal` / `08-Time-Series` are `cut`, each with a reason naming a future chapter or a duplication | ☐ |
| L2.3 | The §4 expected gaps appear as `gap` rows: sinusoidal PE math, RoPE derivation, RMSNorm math, residual/add&norm detail, parameter sharing | ☐ |
| L2.4 | §1's concept order is a real dependency chain — you can't find a concept explained using one that arrives later | ☐ |
| L2.5 | The gate transcript shows **you** chose the code strategy, not the agent | ☐ |
| L2.6 | ≥1 author marker in your own words, anchored to a 二层 node | ☐ |

**Negative check — will it guess at a filename?** Paste:

```
What's in "Classic Encoder-Decoder Transformer 2.png"? Just tell me from the name.
```

It must refuse to answer from the filename — either `inspect-on-demand`, or it opens the file.

| # | Layer 2 | Pass |
| :-- | :--- | :--- |
| L2.7 | Refuses to describe an unopened image from its filename | ☐ |

---

## Stage 2 — `/synthesis-research` on the gaps

**Fresh session.** For each `gap` row, paste:

```
tmp/transformer/drafts/transformer/brief.md has gap rows. Work them one at a time, starting with
<gap>. Write results to tmp/transformer/research-<slug>.md and append the sources to the brief.
```

**Watch for — the failure this stage invites**

`/synthesis-research` has an entry gate: it resolves **live tensions**, not lookups. Most of the
§4 gaps are lookups —"what is the sinusoidal PE formula", "what does RMSNorm compute" — and it
must **refuse them and route to a plain lookup**, not dress a formula up as a research report.

One or two are genuine tensions and should be accepted: *pre-norm vs post-norm* (the field switched
and the papers disagree about why), and *RoPE vs learned positional embeddings* (both shipped in
production models). Those get reports; the formulas get looked up and pasted.

**Check**

```bash
ls "$WORK"/research-*.md 2>/dev/null
grep -n 'gap' "$PIECE"/brief.md
```

| # | Layer 1 | Pass |
| :-- | :--- | :--- |
| L1.7 | Every `gap` row is either discharged by a `research-*.md` or explicitly downgraded to a lookup with its source appended to the brief | ☐ |
| L1.8 | Materials folder still byte-identical | ☐ |

| # | Layer 2 | Pass |
| :-- | :--- | :--- |
| L2.8 | ≥1 lookup-shaped gap was **refused** as a research question and routed | ☐ |
| L2.9 | Each accepted report names a real tension with both sides attributed — no "researchers generally agree" | ☐ |

---

## Stage 3 — `/write-content`

**Fresh session.** Paste:

```
/write-content using tmp/transformer/drafts/transformer/brief.md
```

**Watch for**

- It finds the brief, reads only `core` + `support` sources, and **skips the clarify round**
  entirely (Step 2 is brief-less mode only).
- It reuses the brief's Reading order (legacy: 论点层级), without repeating approval or deriving structure from the
  notes.
- The Code & math table's `inline` rows land in the prose; `assets/code/` rows become files.
- Your vocabulary survives. If you call it 「注意力打分」 and the draft says 「注意力权重计算」,
  that's Hard Rule 6.

**Check**

```bash
ls "$PIECE"/
grep -n '^## \|^### ' "$PIECE"/*.md | head -40
# cut material must not appear
grep -niE 'vision transformer|ViT|时间序列|time series|多模态|multimodal' "$PIECE"/*.md
grep -c '\$\$\?' "$PIECE"/*.md              # math present, in $ delimiters
grep -n '^```[a-z]' "$PIECE"/*.md | head    # code fences carry a language
```

| # | Layer 1 | Pass |
| :-- | :--- | :--- |
| L1.9 | Draft sections match the brief's 一层 ladder, in order | ☐ |
| L1.10 | No `cut` material present — the grep above returns nothing substantive | ☐ |
| L1.11 | Every `inline` Code & math row appears; every `assets/code/` row exists as a file | ☐ |
| L1.12 | Math uses `$…$` / `$$…$$`; every code fence has a language | ☐ |
| L1.13 | Materials folder still byte-identical | ☐ |

---

## Stage 4 — `/insert-inline-images` and `/book-diagrams`

**Paste this**

```
/insert-inline-images — place the images the brief marks core or support into
tmp/transformer/drafts/transformer/<chapter>.md. Copy each placed image into
tmp/transformer/drafts/transformer/assets/ first; the chapter must reference only content-local
relative paths, never the materials folder.
```

Then, for the §2 hops and anything the brief marked `gap` on the diagram side:

```
/book-diagrams — the brief's asset diagrams for Seq2Seq-to-Transformer and the BERT family
```

**Watch for**

- It **views every image** before placing it — filenames lie, and this folder proves it.
- Images are **copied** into `assets/` before referencing. A reference pointing back into
  `$MAT` passes `verify_references.py` today and breaks the moment the folder moves.
- Every placed image gets a caption saying why it's there, not what it is.
- It reports images it skipped, with reasons.

**Check**

```bash
python3 skills/writing/scripts/verify_references.py "$PIECE"/*.md
ls "$PIECE"/assets/ | wc -l
grep -oE '!\[[^]]*\]\([^)]+\)' "$PIECE"/*.md | grep -v 'assets/' || echo "OK: all refs content-local"
grep -c '^\*.*\*$' "$PIECE"/*.md              # caption lines
find "$MAT" -type f ! -name '.DS_Store' -exec stat -f '%N %z %m' {} \; \
  | sort | diff /tmp/transformer-materials.before - && echo "OK: materials untouched"
```

`verify_references.py` is the shared checker — the same script `package-chapter` and
`archive-materials` run, so all three stages agree on what "verified" means.

| # | Layer 1 | Pass |
| :-- | :--- | :--- |
| L1.14 | `verify_references.py` reports **zero BROKEN** | ☐ |
| L1.15 | Every placed image is under `$PIECE/assets/` — no reference escapes the piece folder | ☐ |
| L1.16 | Every placed image carries a caption | ☐ |
| L1.17 | Materials folder still byte-identical — images were **copied**, not moved | ☐ |

---

## Stage 5 — `/review-draft` ⇄ `/edit-targeted`

**Fresh session.** Paste:

```
/review-draft tmp/transformer/drafts/transformer/<chapter>.md
```

Apply findings one at a time with `/edit-targeted`, re-reviewing only the changed unit. Loop until
the verdict is `ship`.

**Watch for — chapter-specific review**

The brief is `brief-kind: chapter`. Review capability, prerequisites, evidence and expression.
Opponent checks do not apply. Requiring or inventing 正方 is now a regression, not an expected gap.
Read v2 node/evidence tables or legacy 二层/三层 without rewriting the historical brief.

**Check**

```bash
grep -n 'Verdict' <the review output you saved, or note it here>
python3 skills/writing/scripts/verify_references.py "$PIECE"/*.md
```

| # | Layer 1 | Pass |
| :-- | :--- | :--- |
| L1.18 | Final verdict is `ship` | ☐ |
| L1.19 | Every applied edit touched one named span; nothing adjacent changed | ☐ |

| # | Layer 2 | Pass |
| :-- | :--- | :--- |
| L2.10 | `review-draft` used chapter checks without requiring or inventing 正方 | ☐ |
| L2.11 | ≥1 finding was a real structural defect, not a line-level nitpick | ☐ |

---

## Stage 6 — `/grill`

**Fresh session** — this matters. A session that drafted the chapter knows what it meant to say and
will grade its own intent.

```
/grill tmp/transformer/drafts/transformer/<chapter>.md
```

Answer from memory. Do not open the draft. Do not look anything up.

**Watch for**

- **One question at a time**, and no anchor shown before your answer. If it quotes the passage in
  the question, the question is dead — that answer is `peeked` and can never be a pass.
- It does **not teach** between questions. A grill that turns into a tutorial has warmed every
  remaining item.
- Questions come in all three kinds — concept check, why-question, and a 面试题 that applies the
  concept to a case the chapter never shows.
- Each miss is routed to **exactly one** of author gap / draft gap, after re-reading the anchor.

**Check**

```bash
test -f "$PIECE"/grill-log.md && grep -n 'Anchor\|Verdict\|Score' "$PIECE"/grill-log.md
grep -c '| pass \|| partial \|| miss ' "$PIECE"/grill-log.md
grep -n 'Draft-gap tasks' -A 10 "$PIECE"/grill-log.md

# new in this refactoring: two machine-readable companion files
test -f "$PIECE"/tasks-for-edit-targeted.md && echo "tasks file present" && cat "$PIECE"/tasks-for-edit-targeted.md
test -f "$PIECE"/gaps-for-learning.md && echo "gaps file present" && cat "$PIECE"/gaps-for-learning.md

git -C . diff --stat -- "$PIECE" 2>/dev/null || true   # tmp/ is gitignored; verify by mtime instead
```

| # | Layer 1 | Pass |
| :-- | :--- | :--- |
| L1.20 | `grill-log.md` exists; every question row carries an anchor | ☐ |
| L1.21 | Every miss and partial has exactly one route (author gap XOR draft gap) | ☐ |
| L1.22 | Every draft-gap task names one file, one section, one instruction | ☐ |
| L1.23 | `tasks-for-edit-targeted.md` exists and contains only draft-gap tasks | ☐ |
| L1.24a | `gaps-for-learning.md` exists and contains only author-gap entries | ☐ |
| L1.24b | The chapter `.md` is unchanged by this stage | ☐ |

| # | Layer 2 | Pass |
| :-- | :--- | :--- |
| L2.12 | No anchor was visible before you answered | ☐ |
| L2.13 | ≥1 draft gap found — a passage that reads correctly and teaches nothing | ☐ |
| L2.14 | That gap's `edit-targeted` fix then passes `review-draft` on the changed unit | ☐ |
| L2.15 | The routing split is honest — not everything blamed on you, not everything on the draft | ☐ |

---

## Stage 7 — `/package-chapter`

**Paste this**

```
/package-chapter tmp/transformer/drafts/transformer/ — destination is the MachineLearning book.
```

**Watch for**

- It asks you for `id` and `created` rather than inventing them. A guessed `id` is permanent.
- It stamps **only** frontmatter — and does not add `route`, `part`, `order`, or `layout`, which
  belong in `collections/book.yml`.
- The portability probe actually runs: a `cp -R` to a `mktemp -d` and a second
  `verify_references.py` from there.
- It **does not touch** `writing/MachineLearning/`.

**Check**

```bash
head -12 "$PIECE"/*.md
grep -nE '\]\(/|src="/|/Users/|\]\(\s*\.\./' "$PIECE"/*.md || echo "OK: no absolute or escaping paths"
grep -nE '\\\(|\\\[|\{% *mermaid' "$PIECE"/*.md || echo "OK: portable math and mermaid"
grep -n '^```$' "$PIECE"/*.md || echo "OK: no bare code fences"
PROBE=$(mktemp -d); cp -R "$PIECE" "$PROBE"/chapter
python3 skills/writing/scripts/verify_references.py "$PROBE"/chapter/*.md
rm -rf "$PROBE"

git -C /Users/xhl/GitHub/writing/MachineLearning status --porcelain | head   # expect no new files
```

| # | Layer 1 | Pass |
| :-- | :--- | :--- |
| L1.24 | Frontmatter carries all six required fields; `id` matches `^[a-z0-9]+(-[a-z0-9]+)*$`; `updated >= created` | ☐ |
| L1.25 | No publication fields (`route`, `part`, `order`, `layout`) in frontmatter | ☐ |
| L1.26 | No absolute paths, no `../` escaping the folder, portable math, languaged fences | ☐ |
| L1.27 | The temp-dir copy resolves **all** references — zero BROKEN | ☐ |
| L1.28 | `writing/MachineLearning/` is untouched; the report names a ready-to-move path and lists the files to leave behind (`brief.md`, `grill-log.md`, `research-*.md`) | ☐ |

**Then move it yourself.** The chapter ships before any archiving happens — that ordering is the
plan's, and stage 8 depends on it.

---

## Stage 8 — `/archive-materials`

Run this **after** the chapter has shipped.

**Paste this**

```
/archive-materials /Users/xhl/GitHub/learning-infra/test/Transfomer/ — the piece is
tmp/transformer/drafts/transformer/ and it has shipped.
```

**Watch for**

- It reads the **draft**, not just the brief — `used-in` is evidence of what landed, and a `core`
  row the draft never used must come back as `planned, unused`.
- Every `inspect-on-demand` row from stage 1 is **resolved** — the file opened, a caption written.
- Renames are proposed as **one batch** with an inbound-reference check, and applied only on your
  yes.
- It offers `clean-notes` for `transformer-note.md` and takes no for an answer.
- It never proposes a deletion or a move. `12-Courseware` and `06/07/08` stay exactly where they
  are, now with rows explaining what they're for.

**Check**

```bash
ls "$MAT"/images-manifest.md "$MAT"/sources.md

# coverage: rows vs the 290-file denominator
grep -c '^| `' "$MAT"/images-manifest.md "$MAT"/sources.md

# no unresolved question marks
grep -n 'inspect-on-demand' "$MAT"/images-manifest.md "$MAT"/sources.md || echo "OK: all resolved"

# used-in present on every core/support row — works for both manifests' column counts
awk -F'|' '$0 ~ /\| *(core|support) *\|/ { u=$(NF-1); gsub(/ /,"",u); if (u=="") print FILENAME": "$2 }' \
  "$MAT"/images-manifest.md "$MAT"/sources.md
# (empty output = every core/support row carries a used-in pointer)

# nothing deleted, nothing moved between folders: per-directory counts must differ
# in exactly one line — the materials root, +2 for the manifests
find "$MAT" -type f ! -name '.DS_Store' -print0 | xargs -0 -n1 dirname | sort | uniq -c \
  | diff /tmp/transformer-dircounts.before -
find "$MAT" -type f ! -name '.DS_Store' | wc -l    # 290 + 2 manifests = 292

# the shipped chapter still resolves
python3 skills/writing/scripts/verify_references.py <moved-chapter>.md
```

| # | Layer 1 | Pass |
| :-- | :--- | :--- |
| L1.29 | Manifest rows cover every material file, directly or via a folder row | ☐ |
| L1.30 | Every `core`/`support` row has a `used-in` pointer or an explicit `planned, unused` | ☐ |
| L1.31 | No `inspect-on-demand` row survives | ☐ |
| L1.32 | File count is 292 — nothing deleted, nothing added but the two manifests | ☐ |
| L1.33 | No file changed directory; renames (if any) stayed in place | ☐ |
| L1.34 | The shipped chapter still reports zero BROKEN after renames | ☐ |
| L1.35 | No dangling intra-folder reference: `grep -rn '<old-name>' "$MAT" --include='*.md'` is empty | ☐ |

| # | Layer 2 | Pass |
| :-- | :--- | :--- |
| L2.16 | Captions say what each image **shows**, not what it's named | ☐ |
| L2.17 | ≥1 `planned, unused` row — the brief promised something the draft didn't use | ☐ |
| L2.18 | The report names what the next chapter inherits, with counts | ☐ |

**Idempotence check.** Re-run stage 8 unchanged:

| # | Layer 1 | Pass |
| :-- | :--- | :--- |
| L1.36 | A second run appends nothing and rewrites no existing row | ☐ |

---

## Close

**Layer 2 — did the loop produce a chapter you can defend?**

| Question | Answer |
| :--- | :--- |
| Could you teach §1 from the chapter's own diagrams, with the file closed? | |
| Which stage caught the most? Which was ceremony? | |
| Where did a skill's contract not fit a chapter (as opposed to a piece)? | |
| What would you have cut, that the selection map kept? | |

**Layer 3 — what did this make you do that writing it straight wouldn't?** One paragraph. This
never gates; it steers the next run.

Findings that are contract gaps — not authoring mistakes — go back to
[`docs/exec-plans/article-loop.md`](../../docs/exec-plans/article-loop.md) §7, not into a patched
brief.

## Reset

```bash
rm -rf tmp/transformer
rm -f /tmp/transformer-materials.before /tmp/transformer-dircounts.before
# to reset stage 8 as well (it is the only stage that wrote to the library):
rm -f "$MAT"/images-manifest.md "$MAT"/sources.md
# renames are NOT auto-reversible — that batch was confirmed by you, and it stands
```
