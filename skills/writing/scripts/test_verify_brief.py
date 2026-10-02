"""Regression scenarios for the public brief-checking interface (stdlib unittest)."""

from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

from verify_brief import verify


FRAME = """---
brief-version: 2
piece: bounded-retry
brief-kind: piece
intent: explain
---
# Brief: Why retries need a limit

Last updated: 2026-10-01

## Question
Why can retries increase load during a failure?
## Reader
Engineers deciding a retry policy for an unavailable service.
## Gain
Distinguish repeated attempts from a successful recovery.
## Answer
Retries consume attempts even when no attempt can succeed.
## Scope
Explain the attempt budget; do not estimate production recovery rates.
"""

LOGIC = """
## Logic nodes
| ID | Statement | Kind | Need |
| :--- | :--- | :--- | :--- |
| n1 | Each attempt consumes one request. | premise | required |
| n2 | Three failed attempts consume three requests. | conclusion | required |
## Logic relations
| From | Relation | To | Reason |
| :--- | :--- | :--- | :--- |
| n1 | supports | n2 | Count one request for each of three attempts. |
## Reading order
| Section | Nodes | Reader task |
| :--- | :--- | :--- |
| Count the requests | n1, n2 | Compute requests without assuming any success. |
## Logic map
```mermaid
flowchart LR
n1["Each attempt consumes one request."]
n2["Three failed attempts consume three requests."]
n1 -->|supports| n2
```
"""

EVIDENCE = """
## Evidence
| ID | Nodes | Kind | Role | Account | Source | Verification | Limits |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| e1 | n1 | external | supports | Specification counts one request per attempt. | spec.md § Attempts | verified | This request model only. |
| e2 | n2 | reasoning | supports | 1 + 1 + 1 = 3. | derivation.md § Count | verified | Does not estimate recovery probability. |
## Selection map
| Material | Disposition | Nodes | Note |
| :--- | :--- | :--- | :--- |
| spec.md § Attempts | core | n1 | Defines the count. |
| derivation.md § Count | core | n2 | Applies it. |
"""

BRIEF = FRAME + LOGIC + EVIDENCE

PLAN = """
## Original contribution
The specification defines individual attempts. The article derives an aggregate attempt budget,
separating consumption from recovery probability through n1 and n2.
## Section plan
| Section | Target length | Evidence treatment | Craft | Transition |
| :--- | :--- | :--- | :--- | :--- |
| Count the requests | 800 | e1: developed, e2: brief | Work through one failed request, then sum attempts. | Close with a bounded budget, leaving recovery probability open. |
## Checkpoints
| Checkpoint | State | Basis |
| :--- | :--- | :--- |
| framework | confirmed | Synthetic author response 2026-10-02: the aggregate-budget thesis and reasoning match my intent. |
| material-plan | delegated | Synthetic author response 2026-10-02: select passages and allocate the agreed 800-word budget. |
"""

ANALYTICAL = BRIEF.replace("brief-kind: piece", "brief-kind: analytical-piece\ntarget-length: 800\nlength-unit: words") + PLAN


class BriefContractTests(unittest.TestCase):
    def assert_passes(self, text: str, stage: str) -> None:
        self.assertEqual(verify(text, stage).errors, ())

    def test_framing_can_finish_before_logic_or_evidence(self) -> None:
        self.assert_passes(FRAME, "frame")
        self.assertTrue(verify(FRAME, "argument").errors)
        self.assert_passes(FRAME + LOGIC, "argument")
        self.assertTrue(verify(FRAME + LOGIC, "examples").errors)

    def test_explanation_needs_no_opponent_personal_case_or_cut(self) -> None:
        self.assert_passes(BRIEF, "ship")

    def test_exploration_can_keep_an_open_question(self) -> None:
        text = BRIEF.replace("intent: explain", "intent: explore")
        text = text.replace("| conclusion | required |", "| question | required |")
        text = text.replace("| e2 | n2 | reasoning | supports | 1 + 1 + 1 = 3. | derivation.md § Count | verified | Does not estimate recovery probability. |\n", "")
        self.assert_passes(text, "ship")

    def test_missing_evidence_blocks_ship_not_working_draft(self) -> None:
        text = BRIEF.replace("| reasoning | supports | 1 + 1 + 1 = 3. | derivation.md § Count | verified |", "| gap | supports | Need a calculation. | — | gap |")
        self.assert_passes(text, "examples")
        self.assertTrue(verify(text, "ship").errors)

    def test_open_question_can_name_what_evidence_is_still_needed(self) -> None:
        text = BRIEF.replace("intent: explain", "intent: explore")
        text = text.replace("Three failed attempts consume three requests.", "Can another attempt succeed?")
        text = text.replace("| conclusion | required |", "| question | required |")
        text = text.replace("| reasoning | supports | 1 + 1 + 1 = 3. | derivation.md § Count | verified |", "| gap | explains | Need an observation under recovered service conditions. | — | gap |")
        self.assert_passes(text, "ship")

    def test_unverified_personal_account_is_not_ready_to_ship(self) -> None:
        text = BRIEF.replace("| external | supports |", "| personal | supports |").replace("| verified | This request model", "| unverified | This request model")
        self.assert_passes(text, "examples")
        self.assertTrue(verify(text, "ship").errors)

    def test_author_confirmed_account_has_valid_provenance_state(self) -> None:
        text = BRIEF.replace("| external | supports |", "| personal | supports |").replace("| verified | This request model", "| author-confirmed | This request model")
        self.assert_passes(text, "ship")

    def test_illustration_cannot_prove_a_factual_conclusion(self) -> None:
        text = BRIEF.replace("| reasoning | supports |", "| illustration | supports |").replace("| verified | Does not estimate", "| illustrative | Does not estimate")
        self.assertTrue(verify(text, "examples").errors)

    def test_explaining_a_claim_is_not_sufficient_support(self) -> None:
        text = BRIEF.replace("| reasoning | supports |", "| reasoning | explains |")
        self.assert_passes(text, "examples")
        self.assertTrue(verify(text, "ship").errors)

    def test_graph_cannot_add_reverse_or_drop_a_relation(self) -> None:
        for replacement in ("n2 -->|supports| n1", "", "n1 -->|supports| n2\nn2 -->|limits| n1"):
            with self.subTest(replacement=replacement):
                self.assertTrue(verify(BRIEF.replace("n1 -->|supports| n2\n", replacement + "\n"), "argument").errors)

    def test_graph_cannot_change_a_statement(self) -> None:
        text = BRIEF.replace('n2["Three failed attempts consume three requests."]', 'n2["Retries cause outages."]')
        self.assertTrue(verify(text, "argument").errors)

    def test_changed_node_leaves_detectable_stale_evidence(self) -> None:
        text = BRIEF.replace("| e2 | n2 |", "| e2 | n9 |")
        self.assertTrue(verify(text, "examples").errors)

    def test_required_node_must_appear_in_reading_order(self) -> None:
        text = BRIEF.replace("| Count the requests | n1, n2 |", "| Count the requests | n1 |")
        self.assertTrue(verify(text, "argument").errors)

    def test_duplicate_ids_are_not_silent_overwrites(self) -> None:
        text = BRIEF.replace("| e2 |", "| e1 |")
        self.assertTrue(verify(text, "examples").errors)

    def test_chapter_needs_capability_and_code_decision_not_opponent(self) -> None:
        text = BRIEF.replace("brief-kind: piece\nintent: explain", "brief-kind: chapter")
        self.assertTrue(verify(text, "examples").errors)
        text += "\n## 教学目标\nCompute the request count under a bounded retry budget.\n## Code & math\nnone — the inline arithmetic is already supplied in evidence.\n"
        self.assert_passes(text, "ship")

    def test_legacy_kind_inference_is_conservative(self) -> None:
        chapter = "## 教学目标\n能计算一次 attention。\n"
        piece = "## 议题\nDoes this work?\n## 正方 / 反方\nBoth supplied positions.\n"
        self.assertEqual(verify(chapter).kind, "chapter")
        self.assertEqual(verify(piece).kind, "piece")
        self.assertTrue(verify(chapter + piece).errors)
        self.assertTrue(verify("A draft without framing.").errors)

    def test_analytical_preparation_can_finish_without_article_prose(self) -> None:
        self.assert_passes(ANALYTICAL, "draft")
        self.assertTrue(verify(FRAME + LOGIC, "draft").errors)
        self.assertTrue(verify(BRIEF, "draft").errors)
        self.assert_passes(BRIEF, "examples")
        self.assert_passes(BRIEF, "ship")

    def test_original_contribution_is_required_only_for_analytical_draft_readiness(self) -> None:
        text = ANALYTICAL.replace("## Original contribution", "## Unrelated notes")
        self.assertTrue(verify(text, "draft").errors)
        self.assert_passes(text, "argument")

    def test_analytical_kind_requires_intent(self) -> None:
        self.assertTrue(verify(ANALYTICAL.replace("intent: explain\n", ""), "frame").errors)

    def test_file_count_and_old_piece_kind_do_not_bypass_analytical_readiness(self) -> None:
        text = ANALYTICAL.replace("brief-kind: analytical-piece", "brief-kind: piece\nsource-type: single-source")
        self.assert_passes(text, "draft")
        self.assertTrue(verify(text.replace("| framework | confirmed |", "| framework | pending |"), "draft").errors)

    def test_budget_unit_and_positive_integer_targets(self) -> None:
        for old, new in (("length-unit: words", "length-unit: pages"),
                         ("target-length: 800", "target-length: -800"),
                         ("target-length: 800", "target-length: 0"),
                         ("target-length: 800", "target-length: ²"),
                         ("| 800 |", "| 0 |"), ("| 800 |", "| 800.5 |"),
                         ("target-length: 800\n", ""), ("length-unit: words\n", "")):
            with self.subTest(new=new):
                self.assertTrue(verify(ANALYTICAL.replace(old, new), "draft").errors)
        self.assert_passes(ANALYTICAL.replace("length-unit: words", "length-unit: characters"), "draft")

    def test_unequal_section_budgets_must_sum_to_total(self) -> None:
        text = ANALYTICAL.replace(
            "| Count the requests | n1, n2 | Compute requests without assuming any success. |",
            "| Count the requests | n1 | Understand attempts. |\n| Budget | n2 | Compute the total. |")
        text = text.replace(
            "| Count the requests | 800 | e1: developed, e2: brief | Work through one failed request, then sum attempts. | Close with a bounded budget, leaving recovery probability open. |",
            "| Count the requests | 600 | e1: developed | Work through the failure. | Now aggregate. |\n"
            "| Budget | 200 | e2: brief | Apply the arithmetic. | Close with the bounded total. |")
        self.assert_passes(text, "draft")
        self.assertTrue(verify(text.replace("| 200 |", "| 300 |"), "draft").errors)
        self.assertTrue(verify(text.replace("e1: developed", "e2: developed"), "draft").errors)
        self.assertTrue(verify(text.replace("| Budget | 200", "| Count the requests | 200"), "draft").errors)

    def test_plan_sections_must_follow_reading_order(self) -> None:
        for replacement in ("| Another section | 800 |", "| Count the requests | 400 |"):
            with self.subTest(replacement=replacement):
                self.assertTrue(verify(ANALYTICAL.replace("| Count the requests | 800 |", replacement), "draft").errors)
        row = next(line for line in PLAN.splitlines() if line.startswith("| Count the requests"))
        self.assertTrue(verify(ANALYTICAL.replace(row, row + "\n" + row), "draft").errors)

    def test_selected_evidence_references_and_treatment(self) -> None:
        for replacement in ("e99: developed, e2: brief", "e1: exhaustive, e2: brief",
                            "e1: developed", "—", "e1: developed, e1: brief, e2: brief"):
            with self.subTest(replacement=replacement):
                self.assertTrue(verify(ANALYTICAL.replace("e1: developed, e2: brief", replacement), "draft").errors)

    def test_pending_or_stale_checkpoint_blocks_readiness(self) -> None:
        for name in ("framework", "material-plan"):
            state = "confirmed" if name == "framework" else "delegated"
            for replacement in ("pending", "revisit", "approved"):
                with self.subTest(name=name, replacement=replacement):
                    text = ANALYTICAL.replace(f"| {name} | {state} |", f"| {name} | {replacement} |")
                    self.assertTrue(verify(text, "draft").errors)
        self.assert_passes(ANALYTICAL.replace("| framework | confirmed |", "| framework | delegated |"), "draft")

    def test_checkpoints_require_distinct_rows_and_a_basis(self) -> None:
        row = next(line for line in PLAN.splitlines() if line.startswith("| framework |"))
        for text in (ANALYTICAL.replace(row, ""), ANALYTICAL.replace(row, row + "\n" + row),
                     ANALYTICAL.replace(row, "| framework | confirmed | — |")):
            self.assertTrue(verify(text, "draft").errors)

    def test_central_gap_blocks_drafting_but_open_question_can_remain(self) -> None:
        text = ANALYTICAL.replace("| reasoning | supports | 1 + 1 + 1 = 3. | derivation.md § Count | verified |",
                                  "| gap | supports | Need a calculation. | — | gap |")
        self.assert_passes(text, "examples")
        self.assertTrue(verify(text, "draft").errors)
        self.assert_passes(text.replace("intent: explain", "intent: explore").replace("| conclusion | required |", "| question | required |"), "draft")
        self.assertTrue(verify(ANALYTICAL.replace("| verified |", "| unverified |"), "draft").errors)

    def test_teaching_kinds_do_not_require_analytical_plan(self) -> None:
        for kind in ("chapter", "explanatory-chapter", "graduated-chapter"):
            with self.subTest(kind=kind):
                text = BRIEF.replace("brief-kind: piece\nintent: explain", f"brief-kind: {kind}")
                text += "\n## 教学目标\nCompute the count.\n## Code & math\nnone — inline arithmetic suffices.\n"
                self.assert_passes(text, "examples")
                self.assert_passes(text, "draft")
                self.assertTrue(verify(text.replace("## 教学目标", "## Unrelated"), "draft").errors)

    def test_legacy_read_compatibility_does_not_certify_draft_readiness(self) -> None:
        text = "## 议题\nDoes this work?\n## 正方 / 反方\nBoth supplied positions.\n"
        self.assert_passes(text, "examples")
        self.assertTrue(verify(text, "draft").errors)

    def test_public_cli_is_read_only_and_returns_failure(self) -> None:
        checker = Path(__file__).with_name("verify_brief.py")
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "brief.md"
            path.write_text(BRIEF)
            before = path.read_bytes()
            result = subprocess.run([sys.executable, str(checker), str(path), "--stage", "ship"], capture_output=True, text=True, check=False)
            self.assertEqual(result.returncode, 0, result.stdout)
            self.assertEqual(path.read_bytes(), before)
            path.write_text(FRAME)
            result = subprocess.run([sys.executable, str(checker), str(path)], capture_output=True, text=True, check=False)
            self.assertEqual(result.returncode, 1)

    def test_draft_cli_is_read_only_and_reports_stale_preparation(self) -> None:
        checker = Path(__file__).with_name("verify_brief.py")
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "brief.md"
            for text, code in ((ANALYTICAL, 0), (ANALYTICAL.replace("| framework | confirmed |", "| framework | revisit |"), 1)):
                path.write_text(text)
                before = path.read_bytes()
                result = subprocess.run([sys.executable, str(checker), str(path), "--stage", "draft"], capture_output=True, text=True, check=False)
                self.assertEqual(result.returncode, code, result.stdout)
                self.assertEqual(path.read_bytes(), before)


if __name__ == "__main__":
    unittest.main()
