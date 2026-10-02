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


if __name__ == "__main__":
    unittest.main()
