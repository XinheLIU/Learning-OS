---
name: frame
description: Choose one worthwhile question for an article or teaching chapter. Use for 选题, 定题, 切入点, framing a piece, or unclear reader benefit. Record the reader, question, provisional answer and scope in the shared brief before developing the framework.
---

# Frame

Last updated: 2026-10-02

Choose the question and reader outcome that justify the piece. Record framing in the
[shared brief](references/brief-format.md); logic and material selection have their own owners.

## Workflow

1. **Read before proposing.** Accept materials, a question, author experience, an outline, a draft
   or prior specification. Read relevant `writing-memory/index.md` entries and latest snapshots
   when present. Distinguish a new question from an extension or correction of an earlier piece.
   Reuse material maps and inspect relevant passages; sources are evidence, not a table of contents.
2. **Resolve only missing intent.** Establish the reader's situation and knowledge, the gain, why
   the author cares, the provisional answer and scope. Reuse supplied constraints and statements.
   When multiple angles remain, propose concrete alternatives with gains and tradeoffs; use
   [framing-questions.md](references/framing-questions.md) for missing judgments. A rough length
   constraint may limit scope now; excerpt treatment and section budgets come later.
3. **Choose the track by intended output.**

   | Kind | Preparation route |
   | :--- | :--- |
   | `analytical-piece` | `develop-argument` with `pre-write-grill` as needed → framework checkpoint → `develop-examples` → material-plan checkpoint |
   | `explanatory-chapter` | `define-audience` → `outcome-design` → `sequence-design` → `develop-examples` |
   | `graduated-chapter` | `assess-readiness` → `elevate-draft` → `add-pedagogy` |
   | legacy `piece` / `chapter` | infer the intended analytical, summary or teaching task from the request; preserve existing preparation |

   Analytical pieces may `argue`, `explain` or `explore`. Original synthesis requires analytical
   preparation regardless of source-file count. Faithful summaries need no original synthesis.
   Chapters add a teaching capability; read [chapter-format.md](references/chapter-format.md).
4. **Write the framing sections.** Use `drafts/<piece>/brief.md` when artifact creation is in scope.
   Record Question, Reader, Gain, Answer and Scope plus known metadata. Import a prior specification
   once instead of maintaining a second mandatory document. Label proposed author judgments as
   provisional until accepted or covered by explicit delegation. No article prose is written here.
5. **Continue to the concrete framework.** Under an authorized analytical workflow, framing feeds
   `develop-argument`; do not insert a separate approval ceremony for transcribing settled intent.
   The author reviews the completed framework at checkpoint 1. Ask sooner only when unresolved
   intent prevents useful progress. A standalone framing request ends with its framing result.

## Author ownership and compatibility

- The author's judgments and personal experiences retain their wording and provenance. A bounded
  unanswered question is valid for exploration. Missing facts are recorded, not invented.
- Reader gain is necessary for every track. Analytical originality is tested during framework
  development; teaching and faithful explanation need no new synthesis or manufactured opponent.
- Use `earned` learner records for proposed personal markers, with source/assistance pointers.
  A `target` is not a belief and a `connect` node does not establish mastery. Drop unrecognized markers.
- Preserve existing logic and evidence. Changed framing names the downstream rows and passages
  that need reconsideration; reopen only affected checkpoints under the shared rules.
- Materials remain read-only. Legacy briefs and book plans remain usable without bulk migration.

## Completion and handoffs

Question, Reader, Gain, Answer and Scope are concrete; kind and applicable intent are recorded.
Run `python3 <learning-os>/skills/writing/scripts/verify_brief.py <brief> --stage frame` for a v2
brief. This checks structure, not reader value. Continue through the chosen track only within
workflow scope. Significant understanding changes may go to `snapshot-writing` when authorized.

## Contract test

Reuse prior intent without another specification or confirmation. An exploration may frame an
open question; a teaching chapter needs no opponent. Preserve snapshot provenance, leave source
materials unchanged, and hand the provisional framing to framework development without drafting.
