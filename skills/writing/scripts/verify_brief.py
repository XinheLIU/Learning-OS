#!/usr/bin/env python3
"""Read-only mechanical checks for Markdown briefs. No external dependencies."""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from html import unescape
import json
from pathlib import Path
import re
from typing import TypedDict, cast


class Schema(TypedDict):
    metadata: dict[str, list[str]]
    sections: dict[str, list[str]]
    tables: dict[str, list[str]]
    values: dict[str, list[str]]


SCHEMA = cast(Schema, json.loads(Path(__file__).resolve().parents[1].joinpath("brief-schema.json").read_text()))
STAGES = ("frame", "argument", "examples", "draft", "ship")
ARTICLE_KINDS = {"piece", "analytical-piece"}
CHAPTER_KINDS = {"chapter", "explanatory-chapter", "graduated-chapter"}


@dataclass(frozen=True)
class Row:
    line: int
    cells: dict[str, str]


@dataclass(frozen=True)
class Result:
    kind: str
    legacy: bool
    errors: tuple[str, ...]


def sections(text: str) -> dict[str, str]:
    """Only level-two headings outside fences delimit contract sections."""
    result: dict[str, str] = {}
    current = ""
    fence = ""
    for line in text.splitlines():
        marker = re.match(r"^(`{3,}|~{3,})", line)
        if marker:
            if not fence:
                fence = marker[1]
            elif line.strip() == fence:
                fence = ""
        if not fence and line.startswith("## "):
            current = line[3:].strip()
            result.setdefault(current, "")
        elif current:
            result[current] += line + "\n"
    return result


def metadata(text: str) -> dict[str, str]:
    match = re.match(r"\A---\s*\n(.*?)\n---(?:\n|$)", text, re.S)
    if not match:
        return {}
    # This contract uses flat scalars; sources and other YAML metadata are not interpreted.
    return {key: value.strip().strip("\"'") for key, value in
            re.findall(r"^([\w-]+):[ \t]*([^\n]*)$", match[1], re.M)}


def table(text: str, name: str, errors: list[str]) -> list[Row]:
    headers = SCHEMA["tables"][name]
    rows: list[Row] = []
    found_header = False
    for number, line in enumerate(text.splitlines(), 1):
        if not line.startswith("|"):
            continue
        cells = [cell.strip().strip("`") for cell in re.split(r"(?<!\\)\|", line.strip().strip("|"))]
        if all(re.fullmatch(r":?-+:?", cell) for cell in cells):
            continue
        if not found_header:
            found_header = True
            if cells != headers:
                errors.append(f"{name}: expected columns {', '.join(headers)}")
            continue
        if len(cells) != len(headers):
            errors.append(f"{name} row {number}: expected {len(headers)} cells, got {len(cells)}")
            continue
        row = Row(number, dict(zip(headers, cells)))
        rows.append(row)
        if any(not cell for cell in cells):
            errors.append(f"{name} row {number}: empty cell; use an explicit value or —")
    if not found_header:
        errors.append(f"{name}: missing table")
    return rows


def ids(cell: str) -> set[str]:
    return {value.strip().strip("`") for value in cell.split(",") if value.strip() not in ("", "—", "none")}


def check_graph(body: str, nodes: dict[str, Row], relations: list[Row], errors: list[str]) -> None:
    if body.strip().lower().startswith("none"):
        return
    match = re.fullmatch(r"\s*```mermaid\n(.*?)\n```\s*", body, re.S)
    if not match:
        errors.append("Logic map: use none with a reason, or one derived Mermaid block")
        return
    graph_nodes: dict[str, str] = {}
    graph_edges: list[tuple[str, str, str]] = []
    lines = match[1].splitlines()
    if not lines or lines[0].strip() not in ("flowchart LR", "flowchart TB"):
        errors.append("Logic map: expected flowchart LR or TB")
    for line in lines[1:]:
        line = line.strip()
        if not line:
            continue
        node = re.fullmatch(r'(n[1-9]\d*)\["(.*)"\]', line)
        edge = re.fullmatch(r"(n[1-9]\d*) -->\|([a-z-]+)\| (n[1-9]\d*)", line)
        if node:
            if node[1] in graph_nodes:
                errors.append(f"Logic map: duplicate node {node[1]}")
            graph_nodes[node[1]] = unescape(node[2])
        elif edge:
            graph_edges.append((edge[1], edge[2], edge[3]))
        else:
            errors.append(f"Logic map: unsupported derived-map line: {line}")
    expected_nodes = {key: unescape(row.cells["Statement"]) for key, row in nodes.items()}
    expected_edges = [(row.cells["From"], row.cells["Relation"], row.cells["To"]) for row in relations]
    if graph_nodes != expected_nodes:
        errors.append("Logic map: nodes/statements differ from Logic nodes")
    if sorted(graph_edges) != sorted(expected_edges):
        errors.append("Logic map: edges differ from Logic relations")


def check_draft_plan(
    meta: dict[str, str], parts: dict[str, str], nodes: dict[str, Row],
    reading_order: list[Row], evidence: list[Row], errors: list[str],
) -> None:
    """Check the recorded plan; dialogue authenticity and originality require semantic review."""
    for heading in SCHEMA["sections"]["draft"]:
        if parts.get(heading, "").strip() in ("", "—", "none"):
            errors.append(f"{heading}: required at draft stage")
    if meta.get("length-unit") not in SCHEMA["metadata"]["length-unit"]:
        errors.append("length-unit: expected words or characters")
    total = meta.get("target-length", "")
    if not re.fullmatch(r"[1-9]\d*", total):
        errors.append("target-length: expected a positive integer")

    planned = table(parts.get("Section plan", ""), "Section plan", errors)
    if [row.cells["Section"] for row in planned] != [row.cells["Section"] for row in reading_order]:
        errors.append("Section plan: sections must match Reading order exactly once and in order")
    section_nodes = {row.cells["Section"]: ids(row.cells["Nodes"]) for row in reading_order}
    if len(section_nodes) != len(reading_order):
        errors.append("Reading order: duplicate section name")
    evidence_by_id = {row.cells["ID"]: row for row in evidence}
    allocated = 0
    supported: set[str] = set()
    for row in planned:
        cells = row.cells
        length = cells["Target length"]
        if not re.fullmatch(r"[1-9]\d*", length):
            errors.append(f"Section plan row {row.line}: Target length must be a positive integer")
        else:
            allocated += int(length)
        for column in ("Craft", "Transition"):
            if cells[column] in ("", "—", "none"):
                errors.append(f"Section plan row {row.line}: {column} needs a stated purpose")
        treatment = cells["Evidence treatment"]
        if treatment == "—":
            continue
        seen: set[str] = set()
        for item in treatment.split(","):
            match = re.fullmatch(r"(e[1-9]\d*):\s*([a-z]+)", item.strip())
            if not match or match[2] not in SCHEMA["values"]["treatment"]:
                errors.append(f"Section plan row {row.line}: expected e<number>: developed or brief")
                continue
            evidence_id = match[1]
            if evidence_id in seen:
                errors.append(f"Section plan row {row.line}: duplicate evidence {evidence_id}")
            seen.add(evidence_id)
            entry = evidence_by_id.get(evidence_id)
            if entry is None:
                errors.append(f"Section plan row {row.line}: unknown evidence {evidence_id}")
                continue
            refs = ids(entry.cells["Nodes"]) & section_nodes.get(cells["Section"], set())
            if not refs:
                errors.append(f"Section plan row {row.line}: {evidence_id} serves no node in this section")
            for node_id in refs & nodes.keys():
                concept = nodes[node_id].cells["Kind"] == "concept"
                if entry.cells["Role"] == "supports" or (concept and entry.cells["Role"] == "explains"):
                    supported.add(node_id)
    if re.fullmatch(r"[1-9]\d*", total) and allocated != int(total):
        errors.append(f"Section plan: target lengths sum to {allocated}, expected {total}")
    required = {key for key, row in nodes.items()
                if row.cells["Need"] == "required" and row.cells["Kind"] != "question"}
    if missing := required - supported:
        errors.append(f"Section plan: selected evidence does not support required nodes {', '.join(sorted(missing))}")

    checkpoints = table(parts.get("Checkpoints", ""), "Checkpoints", errors)
    names = [row.cells["Checkpoint"] for row in checkpoints]
    if sorted(names) != sorted(SCHEMA["values"]["checkpoint"]):
        errors.append("Checkpoints: framework and material-plan must each appear exactly once")
    for row in checkpoints:
        if row.cells["State"] not in ("confirmed", "delegated"):
            errors.append(f"Checkpoints {row.cells['Checkpoint']}: requires confirmation or delegation")
        if row.cells["Basis"] in ("", "—", "none"):
            errors.append(f"Checkpoints {row.cells['Checkpoint']}: missing author response or delegation basis")


def verify(text: str, stage: str = "examples") -> Result:
    if stage not in STAGES:
        raise ValueError(f"unknown stage: {stage}")
    errors: list[str] = []
    meta, parts = metadata(text), sections(text)
    legacy = meta.get("brief-version", "1") == "1"
    kind = meta.get("brief-kind", "")
    if legacy and not kind:
        teaching = "教学目标" in parts
        opposing = "正方" in text and "反方" in text
        if teaching != opposing:
            kind = "chapter" if teaching else "piece"
        else:
            errors.append("brief-kind: ambiguous legacy brief; clarify before use")
    if kind not in SCHEMA["metadata"]["brief-kind"]:
        errors.append("brief-kind: expected a supported article or chapter kind")
    if legacy:
        # Legacy layout and evidence remain read-compatible, not silently migrated or certified.
        if kind == "chapter" and not parts.get("教学目标", "").strip():
            errors.append("教学目标: required for chapter")
        if kind == "piece" and not any(parts.get(key, "").strip() for key in ("议题", "Angle", "Question")):
            errors.append("legacy piece: missing question or angle")
        if stage == "draft":
            errors.append("draft: legacy compatibility is not readiness; assess equivalent preparation manually")
        return Result(kind, True, tuple(errors))
    if meta.get("brief-version") != "2":
        errors.append("brief-version: unsupported version")
    if kind in ARTICLE_KINDS and meta.get("intent") not in SCHEMA["metadata"]["intent"]:
        errors.append("intent: expected argue, explain or explore")
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", meta.get("piece", "")):
        errors.append("piece: expected a stable kebab-case slug")
    if not re.search(r"Last updated: \d{4}-\d{2}-\d{2}", text):
        errors.append("Last updated: missing date")
    for phase in STAGES[: min(STAGES.index(stage), 2) + 1]:
        for heading in SCHEMA["sections"][phase]:
            if not parts.get(heading, "").strip():
                errors.append(f"{heading}: required at {phase} stage")
    if kind in CHAPTER_KINDS and not parts.get("教学目标", "").strip():
        errors.append("教学目标: required for chapter")
    if stage == "frame":
        return Result(kind, False, tuple(errors))

    def rows(name: str) -> list[Row]:
        return table(parts.get(name, ""), name, errors)

    def enum(row: Row, column: str, key: str, name: str) -> None:
        if row.cells[column] not in SCHEMA["values"][key]:
            errors.append(f"{name} row {row.line}: invalid {column} {row.cells[column]}")

    node_rows = rows("Logic nodes")
    nodes: dict[str, Row] = {}
    for row in node_rows:
        node_id = row.cells["ID"]
        if not re.fullmatch(r"n[1-9]\d*", node_id) or node_id in nodes:
            errors.append(f"Logic nodes: invalid or duplicate ID {node_id}")
        nodes[node_id] = row
        enum(row, "Kind", "node-kind", "Logic nodes")
        enum(row, "Need", "need", "Logic nodes")
    if not nodes:
        errors.append("Logic nodes: at least one node is required")

    def references(cell: str, location: str, required: bool = True) -> set[str]:
        referenced = ids(cell)
        if required and not referenced:
            errors.append(f"{location}: missing node reference")
        if unknown := referenced - nodes.keys():
            errors.append(f"{location}: unknown nodes {', '.join(sorted(unknown))}")
        return referenced

    relations = rows("Logic relations")
    seen_edges: set[tuple[str, str, str]] = set()
    for row in relations:
        enum(row, "Relation", "relation", "Logic relations")
        references(row.cells["From"], "Logic relations From")
        references(row.cells["To"], "Logic relations To")
        edge = (row.cells["From"], row.cells["Relation"], row.cells["To"])
        if edge in seen_edges or edge[0] == edge[2]:
            errors.append(f"Logic relations: duplicate or self relation {edge}")
        seen_edges.add(edge)
    required_nodes = {key for key, row in nodes.items() if row.cells["Need"] == "required"}
    needs_evidence = {key for key in required_nodes if nodes[key].cells["Kind"] != "question"}
    covered: set[str] = set()
    reading_order = rows("Reading order")
    for row in reading_order:
        covered.update(references(row.cells["Nodes"], "Reading order"))
    if missing := required_nodes - covered:
        errors.append(f"Reading order: missing required nodes {', '.join(sorted(missing))}")
    check_graph(parts.get("Logic map", ""), nodes, relations, errors)
    if stage == "argument":
        return Result(kind, False, tuple(errors))

    covered.clear()
    supported: set[str] = set()
    evidence_ids: set[str] = set()
    evidence = rows("Evidence")
    for row in evidence:
        cells = row.cells
        if not re.fullmatch(r"e[1-9]\d*", cells["ID"]) or cells["ID"] in evidence_ids:
            errors.append(f"Evidence: invalid or duplicate ID {cells['ID']}")
        evidence_ids.add(cells["ID"])
        refs = references(cells["Nodes"], f"Evidence {cells['ID']}")
        for column, key in (("Kind", "evidence-kind"), ("Role", "role"), ("Verification", "verification")):
            enum(row, column, key, "Evidence")
        evidence_kind, state, role = cells["Kind"], cells["Verification"], cells["Role"]
        permitted = {"personal": {"author-confirmed", "unverified"}, "illustration": {"illustrative"},
                     "gap": {"gap"}, "external": {"verified", "unverified"}, "reasoning": {"verified", "unverified"}}
        if state not in permitted.get(evidence_kind, set()):
            errors.append(f"Evidence {cells['ID']}: kind/verification mismatch")
        if evidence_kind == "illustration" and role != "explains":
            errors.append(f"Evidence {cells['ID']}: illustration can only explain, not prove facts")
        if evidence_kind != "gap" and cells["Source"] in ("—", "none"):
            errors.append(f"Evidence {cells['ID']}: missing source")
        covered.update(refs)
        for node_id in refs & nodes.keys():
            concept = nodes[node_id].cells["Kind"] == "concept"
            if role == "supports" or (concept and role == "explains"):
                supported.add(node_id)
        if stage in ("draft", "ship") and refs & needs_evidence and state in ("unverified", "gap"):
            errors.append(f"Evidence {cells['ID']}: unresolved evidence on a required node")
    if missing := needs_evidence - covered:
        errors.append(f"Evidence: missing evidence or gap for {', '.join(sorted(missing))}")
    if stage in ("draft", "ship") and (missing := needs_evidence - supported):
        errors.append(f"Evidence: no suitable support/explanation for {', '.join(sorted(missing))}")
    for row in rows("Selection map"):
        enum(row, "Disposition", "disposition", "Selection map")
        references(row.cells["Nodes"], "Selection map", row.cells["Disposition"] in ("core", "support"))
    if kind in CHAPTER_KINDS:
        code = parts.get("Code & math", "")
        if not code.strip().lower().startswith("none"):
            for row in rows("Code & math"):
                references(row.cells["Nodes"], "Code & math", row.cells["Placement"] != "cut")
                if row.cells["Source"] in ("—", "none") or row.cells["Placement"] in ("—", "none"):
                    errors.append("Code & math: source and placement required")
    if stage == "draft" and kind in ARTICLE_KINDS:
        check_draft_plan(meta, parts, nodes, reading_order, evidence, errors)
    return Result(kind, False, tuple(errors))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("brief", type=Path)
    parser.add_argument("--stage", choices=STAGES, default="examples")
    args = parser.parse_args()
    result = verify(args.brief.read_text(), args.stage)
    for error in result.errors:
        print(f"{args.brief}: {error}")
    if result.errors:
        return 1
    scope = "legacy read compatibility only; semantic review required" if result.legacy else f"v2 {args.stage} structure"
    print(f"OK: {result.kind}; {scope}. This is not a ship verdict.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
