---
name: frame
description: Choose one worthwhile question for an article or teaching chapter. Use for 选题, 定题, 切入点, framing a piece, or a draft whose reader benefit is unclear. Connect a familiar reader situation to a specific gain in understanding; record the author's judgment and scope in brief.md.
---

# Frame

Last updated: 2026-10-01

Decide which question deserves this piece. Finish with an author-owned question, reader benefit,
provisional answer and scope. Logic development and evidence selection have their own skills.

## Workflow

### Input: From pre-write-grill or direct

**With pre-write-grill specification (preferred for original articles):**
- Confirmed topic, scope, length, material priorities, examples, structure already established
- Frame's job: translate that specification into formal brief sections
- Minimal additional questioning needed

**Without pre-write-grill (for single-source summaries, clear requests):**
- Follow legacy workflow below
- When multiple interpretations exist, consider calling `/pre-write-grill` first

### Steps

1. **Read before proposing.** Accept a question, experience, draft, materials, writing snapshot, or
   pre-write-grill specification. Read relevant `writing-memory/index.md` entries and their latest
   snapshots when present; distinguish a new question from an extension or correction of an earlier
   piece. When a material map exists, inspect promising sources. Treat sources as evidence, not as
   the table of contents.

2. **With specification: translate to brief format.** If pre-write-grill provided confirmed topic,
   scope, length, material priorities, and structure, directly populate the brief sections:
   - Question from confirmed topic
   - Reader/Gain from specification
   - Answer and Scope from confirmed boundaries
   - Intent from structure type
   Skip redundant re-questioning. Confirm only that the brief reflects the specification accurately.

3. **Without specification: establish framing through questioning.**
   - Name the reader's situation: what decision, confusion or task makes this matter to them?
   - Establish why the author cares separately
   - When multiple angles exist, present 2-3 candidates with explicit trade-offs (reader benefit,
     required evidence, exclusions, estimated scope)
   - Use [framing-questions.md](references/framing-questions.md) when the question or author's
     answer is unclear
   - Always confirm scope boundaries, target length/depth explicitly

4. **Settle the purpose and scope.** For `piece`, select `argue`, `explain` or `explore` according
   to the main reader benefit. For `chapter`, state `教学目标` as a capability. A piece can explain
   a mechanism while arguing a judgment; split it only if it promises independent reader outcomes.
   Record one central question, what the reader gains, the author's answer (including uncertainty),
   and what this piece leaves out. A bounded unanswered question is a valid exploratory outcome.

5. **Confirm before proceeding.** Present the framing summary and ask: "Does this brief capture your
   intent? Ready to proceed to logic development?" Only continue after explicit author confirmation.

6. **Write only the framing sections** of `drafts/<piece>/brief.md` using
   [brief-format.md](references/brief-format.md). For a chapter also read
   [chapter-format.md](references/chapter-format.md). Preserve existing logic and evidence; when
   framing changes, name which downstream nodes need reconsideration rather than erasing them.

## Author ownership

- The author determines judgments and personal experiences. A proposed answer stays labelled as
  a proposal until accepted; already stated or confirmed judgments need no second approval.
- Familiarity means a recognizable reader problem. Freshness means a concrete gain in explanation,
  evidence, connection, judgment or boundary. Neither novelty to the entire field nor an opponent
  is mandatory. Explain why *this reader* needs the piece.
- An argumentative piece engages actual objections fairly. An explanatory or exploratory piece
  need not manufacture a dispute, a current event or a forced conclusion.
- When learning records are available, propose author markers from `earned` records only, keeping
  their wording and evidence/assistance pointers. Unrecognized markers are dropped. A `target`
  is not a belief; a `connect` node can locate a concept but does not establish teaching mastery.
- Materials remain read-only. No prose is drafted here. Missing sources or an unresolved answer
  are recorded honestly; they do not prevent a useful question from being framed.

## Completion and handoffs

Done when Question, Reader, Gain, Answer and Scope are concrete and reflect the author's stated
intent; `brief-kind` and, for pieces, `intent` are set. Check with
`python3 <learning-os>/skills/writing/scripts/verify_brief.py <brief> --stage frame`.
The checker verifies structure; the dialogue establishes whether the gain is worthwhile.

- Structure needed → `develop-argument`; a supplied valid structure can be retained.
- A substantive change in understanding → `snapshot-writing`, within the user's authorized scope.
- A single-skill request ends here. An authorized writing workflow continues through the missing
  stages; ask only for a new judgment, unclear scope or missing personal fact.

## Contract test

An explanation without an opponent and an exploration without a settled answer can both finish.
The brief states one reader outcome, no invented author belief and no drafted paragraphs. A
related snapshot is reused with its pointer and the proposed new gain; materials remain unchanged.
