# Learning OS Format Migration Summary

Last updated: 2026-09-06

## Overview

Completed migration to address three core issues:
1. **Unified internal format** — All internal learning memory is now Markdown in consolidated `notes.md`
2. **Simplified handoff** — Reduced complexity by consolidating files
3. **Strengthened learning-by-doing** — Enhanced practice integration throughout
4. **Parameterized course depth** — New `--depth` parameter for lesson length and practice intensity

## Key Changes

### 1. File Format Consolidation

**Before:**
- Multiple separate files: `notes.md`, `terms.md`, `framework.md`, `playbook.md`, `preferences.md`
- HTML artifacts: `syllabus.html`, lesson HTML files
- Mixed formats created confusion about what's "internal memory" vs "human-readable output"

**After:**
- **Single source of truth:** `notes.md` (consolidated Markdown file)
  - Contains: Records, Attempt Log, Terms, Structural Memory, Micro-Skills, Playbook, Preferences, Mastery Snapshot
- **HTML for human consumption:** `index.html` (course shell + lessons)
  - Renders syllabus and lesson content
  - Generated from Markdown sources
- **Removed:** `syllabus.html`, `framework.md`, `playbook.md`, `preferences.md`, `terms.md` as separate files

### 2. Updated File Structure

```
learning/<slug>/
├── survey.md              # Investment matrix (unchanged)
├── syllabus.md            # Lesson sequence source (unchanged)
├── notes.md               # CONSOLIDATED internal memory (new format)
├── retrieval.md           # Spaced repetition ledger (unchanged)
├── case-*.md              # Practice records (unchanged)
├── research-*.md          # Synthesis outputs (unchanged)
└── index.html             # Course shell + rendered lessons (human-facing)
```

### 3. Skill Updates

Updated all learning skills to work with consolidated `notes.md`:

#### curriculum
- Removed `syllabus.html` generation
- Added drill integration in lesson design
- Strengthened connection between K/S lessons and practice
- **NEW:** Added `--depth` parameter (quick/standard/deep)
  - Controls lesson length: ~10min / ~20–30min / ~60–90min
  - Controls drill count: 1–2 / 2–3 / 4–6+ drills
  - Controls reading depth: excerpts / full sections / multiple sources
  - Controls reference docs: summaries / worked examples / comprehensive with citations

#### learn
- Reads/writes consolidated `notes.md` sections
- Added drill mechanism within lessons
- Enhanced scaffolding based on mastery stage
- Promotes earned structure into Structural Memory section
- Adapts to course depth parameter when revising lessons

#### practice
- Works with Micro-Skills section in `notes.md`
- Integrated with curriculum drills
- Records errors for /reflect compression

#### reflect
- Reads/writes Playbook and Structural Memory in `notes.md`
- Compresses errors from practice into micro-goals
- Updates structural map and bumps Iteration counter

#### evaluate
- Reads Structural Memory from `notes.md`
- Writes Mastery Snapshot to `notes.md`
- Checks earned structure against targets

#### recall
- No changes needed (already worked with retrieval.md only)

#### survey
- Seeds Structural Memory section in `notes.md` instead of separate `framework.md`
- Creates `notes.md` if it doesn't exist
- Sets Iteration: 0

### 4. New Depth Parameter

Three depth levels for `/curriculum`:

| Level | Lesson length | Drills | Reading | When to use |
|-------|--------------|--------|---------|-------------|
| **quick** | ~10 min | 1–2 simple | Key excerpts | Time-constrained; survey field; refresh |
| **standard** | ~20–30 min | 2–3 with interleaving | Full sections | Normal learning; working fluency |
| **deep** | ~60–90 min | 4–6 + synthesis | Multiple sources + compare/contrast | Mastery; professional depth; research prep |

Usage: `/curriculum <topic> --depth=<quick|standard|deep>`

Default: **standard** if not specified

### 5. New Reference Documentation

Created comprehensive format specification:
- `skills/learning/learn/references/notes-format.md` — Complete schema for consolidated `notes.md`

Updated existing documentation:
- Removed `framework-format.md` references
- Updated all skill handoff documentation
- Added depth parameter documentation in curriculum

### 6. Learning-by-Doing Enhancements

**Drills in K/S lessons:**
- Each knowledge/skill lesson now includes concrete practice drills
- Drills anchor to survey matrix cells
- Immediate application within lesson flow
- Drill count scales with depth parameter

**Tighter practice loop:**
- Micro-skills tracked in notes.md
- Error compression in /reflect
- Next practice session starts with compressed micro-goals

**Scaffolding by stage:**
- Novice (none/can-recall): heavy scaffolding, worked samples
- Practitioner (can-apply+): minimal scaffolding, transfer focus

## Migration Path (for existing courses)

If you have existing `learning/<slug>/` directories:

1. **Manual consolidation** (one-time):
   ```bash
   # Combine files into notes.md following the new format
   # Order: Records, Attempt Log, Terms, Structural Memory, 
   #        Micro-Skills, Playbook, Preferences, Mastery Snapshot
   ```

2. **framework.md → Structural Memory:**
   - Copy Map, Layers, Missing-links, Frontier into Structural Memory section
   - Preserve `earned`/`target` status and iteration counter

3. **Remove obsolete files:**
   ```bash
   rm learning/<slug>/framework.md
   rm learning/<slug>/playbook.md
   rm learning/<slug>/terms.md
   rm learning/<slug>/preferences.md
   rm learning/<slug>/syllabus.html  # if exists
   ```

4. **Keep unchanged:**
   - `survey.md`, `syllabus.md`, `retrieval.md`
   - All `case-*.md` and `research-*.md` files
   - `index.html` (will be regenerated by /learn or /curriculum)

5. **Rebuild with depth parameter:**
   - Re-run `/curriculum <slug> --depth=<level>` to regenerate lessons with proper drill counts

## Contract Violations to Watch

Skills now enforce:
- `/curriculum` must parse or default depth parameter
- Lesson length and drill count must match depth parameter
- `/learn` and `/practice` never write separate framework/playbook files
- `/reflect` updates Structural Memory in place, bumps Iteration once per session
- `/evaluate` writes Mastery Snapshot to notes.md only
- `/survey` seeds Structural Memory at Iteration: 0 with target/hypothesized only
- No skill creates HTML for lessons except as rendering from Markdown source

## Testing

Two end-to-end runbooks. You run them yourself, step by step; see
[`trials/README.md`](trials/README.md) for the protocol.

- [`trials/herdr/RUNBOOK.md`](trials/herdr/RUNBOOK.md) — herdr at `--depth=standard`, 60 min/day
  across three days.
- [`trials/swe-basics/RUNBOOK.md`](trials/swe-basics/RUNBOOK.md) — writing good code and design
  patterns at `--depth=quick`, 2 × 30 min/day across three days, against the learner's own repo.

Both end in a sealed-battery independence test. Running them at opposite ends of `--depth` is what
proves the parameter changes lesson length and drill count rather than only prose.

It asserts the v2 contract directly: no `framework.md`, `playbook.md`, `drills-*.md`, or
`syllabus.html`; consolidated `notes.md` sections; opening tasks before explanation; Stage 2–3
mini-cases; and that `--depth` changes lesson length and drill count rather than just prose.

The earlier v1 course is archived at `learning/herdr-v1/`. Comparing it against the v2 run — same
topic, same three-hour budget — is the migration's real test.

The old `test-cases/` fixture tree was removed on 2026-09-02; every contract it encoded is now
stated in its skill's `## Contract test` block and exercised live by the runbook.

## What came next — v3 (2026-09-06)

This document describes the v2 consolidation. The next redesign — **HTML-first learning** — moved
the learning experience itself into the course: checkpoint blocks and completion manifests in every
lesson, `recall.html` for the return path, mini-cases promoted to lesson files, `Next:`/`Gate:`
orchestration fields in `syllabus.md`, and `/learn` + `/recall` reshaped around bookkeeping and
planning. See the [2026-09-06 changelog entry](CHANGELOG.md#2026-09-06) and
[`skills/learning/README.md`](skills/learning/README.md) for the current contract.

## Benefits

1. **Clearer separation:** MD = internal, HTML = human-facing
2. **Simpler handoffs:** One file to read/write instead of 4-5
3. **Stronger practice:** Drills embedded in lessons, micro-skills tracked, errors compressed
4. **Less confusion:** No more "which file holds X?"
5. **Easier debugging:** Single timeline in one consolidated file
6. **Flexible depth:** Users can choose course intensity (quick/standard/deep) based on time budget and mastery goals
