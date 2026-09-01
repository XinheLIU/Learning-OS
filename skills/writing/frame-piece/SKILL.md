---
name: frame-piece
description: Find the angle before drafting. Reads the materials, proposes contestable angle candidates, then works with the author across multiple rounds until one angle and one cut-list are committed — emits brief.md. Use before writing anything that needs a point of view, or when a draft reads like a summary of its sources. Triggers on 选题, 切入点, "what's my angle", "frame this piece", "what should I write from these notes".
---

Last updated: 2026-09-01

# Frame Piece

## Overview

Materials in, `brief.md` out. This skill decides **what the piece argues and what gets thrown away**. Everything downstream — drafting, review, editing — is a refinement of what happens here.

It never writes prose. It ends when the author has committed to one angle and one cut-list, or has decided the materials don't support a piece yet.

## Hard Rules

1. **Never draft prose.** Not an opening paragraph, not a "quick sample". The output is a brief.
2. **Propose, don't interrogate.** Read the materials first and arrive with drafted candidates. A blank-page "what's your angle?" pushes the hardest work back onto the author, who came here because that work is hard.
3. **Always include the flat candidate, labelled as such** — the thesis the materials already argue. It exists to be seen and rejected.
4. **The material is evidence, not the opponent.** The piece argues about the world, not about the sources. If the 对立面 turns out to be the source's author — the course contradicts itself, the book overclaims, the neuroscience is decorative — that is a *book review*, and the skill has failed. Sources supply ammunition for one side of a question people are actually arguing.
5. **No round cap.** Three or four passes before an angle stops sounding like the source is normal.
6. **The committed angle is in the author's words**, taken from what they said in dialogue — not the skill's draft phrasing.
7. **Never invent the author's positions.** Candidates are proposals; beliefs, mistakes, and vocabulary only enter the brief if the author said them.
8. **Saying "not yet a piece" is a valid ending.** If every candidate is flat and the materials can't support a sharper one, say so and name what's missing.

## Workflow

### Step 1: Read everything, build the section ledger

Read every material in full. List every section of every source — this ledger becomes the selection map in Step 6, so nothing may be skipped at this stage. Note for each: the claim it makes, and whether it carries evidence (data, case, citation) or only assertion.

Then find the **friction** — where angles hide. Two kinds, and the order matters.

**External friction — look here first.** Where the material collides with the reader's present: a technology that did not exist when the material was made, a change in how people work, a practice the field has adopted since, a cost the material never had to price. This is where contestable questions live, because both sides still have live adherents. A 2014 course on how the brain learns meets 2026's assumption that AI compresses learning time — *that collision* is a question. The course by itself is not.

**Internal friction — secondary.** Contradictions between sources, claims asserted without support, advice that conflicts with what practitioners do. These are *ammunition* inside an external question: a course that contradicts itself on depth vs. breadth hands evidence to whichever side needs it. They are a *subject* only for a book review. If a candidate's entire content is internal friction, it is a review — discard it, or push it outward until both sides are held by people who never read the material.

### Step 2: Propose 3–5 angle candidates

A candidate is not a topic, and not a claim standing alone. It is **a question people are currently arguing, plus the side this piece takes**:

| Line | What it states |
| :--- | :--- |
| **议题** | The live question, stated as a question. Someone must be able to answer it both ways. |
| **正方** | The position this piece argues against — at full strength, with who holds it |
| **反方** | The position this piece takes — one contestable sentence |
| **Reader** | Who it serves, and which side they start on |
| **Material** | Which sources arm which side — and what evidence is still missing |
| **Cost** | What taking this side forces you to throw away, and what it costs the reader to agree |

Two tests before a candidate ships:

- **Steelman test.** State 正方 so that its believers would sign it. If 正方 reads as obviously wrong, you built a strawman and the piece has no stakes.
- **Two-sided test.** Could a competent person write the opposite piece from these same materials? If not, this is a fact, not an angle.

The cost line is the honest one: an angle that costs nothing to adopt isn't an angle.

**One candidate is always the flat one, explicitly labelled** — for example: *"[FLAT — the materials' own thesis, included so you can reject it]"*. This is the baseline the system produces by default; naming it in the output is cheaper than warning about it.

Rank the candidates, recommendation first. Recommend the question with the **highest stakes the available material can still arbitrate** — stakes meaning the reader does something different depending on the answer. Sharpness the evidence can't carry is a research gap, not an angle — log it as one rather than recommending it.

### Step 3: Ask the load-bearing questions

Four questions extract what the corpus cannot contain. Ask them in the author's language, one or two at a time, alongside the candidates so the author has something to react against. Full reasoning and follow-ups: [references/framing-questions.md](references/framing-questions.md).

- **「为什么是现在？同样的问题三年前问，答案会不一样吗？」** — asked **first**, because it generates the 议题. Material is usually timeless; questions are not. If nothing has changed, the piece has no occasion and will open with a definition.
- **「读这些材料时，哪一句让你想反驳？」** — a disagreement sits at the intersection of material and author, which is where a side lives. Push it outward: not "the course is wrong here", but "the course's advice fails under condition X".
- **「这个领域里大部分人相信什么，而你不相信？」** — this is 正方. A piece with no opponent is a summary with better paragraphs; an opponent nobody defends is a strawman.
- **「你自己在这件事上判断错过什么？」** — earned authority. The mistake the author actually made is the one example no source can supply and no competitor can copy.

Then the ordinary framing questions — reader, what they already know, register, what should change in their behaviour after. These are configuration; ask them last and quickly.

### Step 4: Sharpen — loop until commitment

`propose → author reacts → sharpen or discard → re-propose`. Each round, test surviving candidates:

- **Could the source author have written this?** If yes, it's still the source's thesis.
- **Is the opponent the source itself?** If 正方 amounts to "the course is right", the piece is a review. Push the question outward until both sides are held by people who never read the material.
- **Could a competent person argue the other side from these same materials?** If not, it's a fact, not an angle.
- **What does it cost the reader to agree?** If nothing, it's a platitude.
- **Whose sentence is this?** If the author wouldn't say it out loud, it isn't theirs yet.

Keep the loop open until the author commits. Do not settle a round early because the candidate is "good enough" — the whole cost of this skill is paid here.

### Step 5: Build the argument ladder

A committed angle is not yet a piece. An angle with no structure hands `write-content` one sentence plus a pile of dispositioned sections — which forces the drafter to invent the argument out of the corpus. That is the disease this skill exists to cure, recurring one level down.

So before the selection map, build the ladder **with the author**:

| Layer | What it holds | Test |
| :--- | :--- | :--- |
| **主题（层 0）** | The committed angle, one sentence. 正方 sits here too — the counter-position argues against the 主题, never against a single 论点. | — |
| **一层论点** | 2–4 pillars, each one contestable sentence. | **Sufficiency:** if the reader grants all of them, does 主题 follow? **Independence:** does dropping one leave the rest standing? An uncontestable pillar is background, not a pillar. |
| **二层：机制** | For each pillar, why it holds — two or three lines. | Answers "why is this true", not "what else is true". |
| **三层：具体展开** | What discharges each 二层 line: a source section, the author's own incident, or a `gap`. | Every 二层 line has one. A line with nothing under it *is* a `gap` and must be labelled, not asserted. |

Three rules the ladder exists to enforce:

- **Anchor every author marker to a node.** A verbatim quote sitting loose in the brief gets used as decoration. Pinned to one 二层 line it becomes that claim's evidence — and its absence from that spot in the draft becomes a reviewable defect.
- **The opponent's strongest objection earns its own 一层论点.** If 正方 has one question the piece must answer, it is a pillar. Burying it under `gap` is how a piece ships with its weakest joint unaddressed.
- **Layers are settled one at a time, and out loud.** Say which pillars are committed and which are still open at the end of every round. Without that, the dialogue reads as sideways drift even when it is converging.

### Step 6: Build the selection map

Disposition **every section from the Step 1 ledger** against the committed angle:

| Disposition | Meaning |
| :--- | :--- |
| `core` | Carries the argument |
| `support` | One example, citation, or counter-objection |
| `cut` | True but off-mainline — most content lands here |
| `gap` | The angle needs it; the materials lack it |

Key every `core` and `support` row to **the ladder node it discharges** (`二层 2.2`). A section that supports the angle but no specific node is decoration — demote it to `cut`. Also note **which side the section arms**. The strongest pieces cite the material against the position it was written to support — a course's own biology chapter is often the sharpest evidence for the 反方 it never considered.

A selection map with nothing under `cut` means the angle is still the corpus's own thesis — go back to Step 4. `gap` entries are the research plan; route them to `/synthesis-research` or another capture round.

### Step 7: Write the brief

Write `drafts/<piece-slug>/brief.md` per [references/brief-format.md](references/brief-format.md). Report to the author: the committed angle, the core/support/cut/gap counts, and the top gaps that need filling before drafting.

## Handoff

The brief is the reviewable unit — killing a bad angle here costs minutes; discovering it in a finished draft costs the draft.

- **Next:** `write-content` drafts from the brief, using only `core` + `support`.
- **Back here:** when `review-draft` returns the verdict "reframe or kill", re-enter at Step 4 with the draft as new evidence about what the angle actually supports.
