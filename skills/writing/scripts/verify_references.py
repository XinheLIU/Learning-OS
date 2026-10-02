#!/usr/bin/env python3
"""Verify a document's references resolve, and optionally that it is portable.

Shared by `insert-inline-images`, `package-chapter`, and `archive-materials` — one
definition of what "verified" means, so the three callers cannot drift apart.

Stdlib only. Two check groups:

  references (always)   Markdown ![alt](src), HTML <img src=...>, CSS url(...).
                        Remote (http/https/data:) refs are listed, not checked.

  portability (--portability)
                        Absolute paths, refs escaping the folder, non-portable math
                        delimiters, legacy renderer tags, unlanguaged code fences,
                        malformed content: links.

Usage:
    verify_references.py DOC.md [DOC.html ...]
    verify_references.py --portability DOC.md

Exit 1 if any local reference is broken or any portability check fails.
"""

from __future__ import annotations

import re
import sys
import urllib.parse
from pathlib import Path

MARKDOWN_IMAGE = re.compile(r"!\[[^\]]*\]\(\s*<?([^)\s>]+)>?(?:\s+[\"'][^\"']*[\"'])?\s*\)")
HTML_IMG_SRC = re.compile(r"<(?:img|source)\b[^>]*?\bsrc(?:set)?=[\"']([^\"']+)[\"']", re.IGNORECASE)
CSS_URL = re.compile(r"url\(\s*[\"']?([^\"')]+)[\"']?\s*\)")
IMAGE_EXTENSIONS = (".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg", ".avif")

# (label, pattern, hint) — a hit is a failure.
PORTABILITY_CHECKS = [
    (
        "absolute path",
        re.compile(r"""\]\(/|src=["']/|/Users/|/home/|[A-Za-z]:\\"""),
        "use a relative path from the document",
    ),
    (
        "reference escapes the folder",
        re.compile(r"\]\(\s*<?\.\./"),
        "assets must live beside the content, under ./assets/",
    ),
    (
        "non-portable math delimiter",
        re.compile(r"\\\(|\\\[|\\begin\{equation\}"),
        r"use $…$ for inline and $$…$$ for display",
    ),
    (
        "legacy renderer tag",
        re.compile(r"\{%\s*(mermaid|raw|endraw|img)\b"),
        "use a fenced ```mermaid block",
    ),
    (
        "malformed content: link",
        re.compile(r"\]\(content:(?![a-z0-9]+(-[a-z0-9]+)*\))"),
        "content ids are lowercase kebab-case",
    ),
]


def extract_refs(text: str, suffix: str) -> list[str]:
    refs: list[str] = []
    if suffix == ".md":
        refs += MARKDOWN_IMAGE.findall(text)
    else:
        for srcset in HTML_IMG_SRC.findall(text):
            refs += [part.strip().split(" ")[0] for part in srcset.split(",") if part.strip()]
        refs += [u for u in CSS_URL.findall(text) if u.lower().endswith(IMAGE_EXTENSIONS)]
    return refs


def check_references(doc: Path) -> int:
    """Print one line per reference. Return the count of broken ones."""
    refs = extract_refs(doc.read_text(encoding="utf-8", errors="replace"), doc.suffix.lower())
    if not refs:
        print(f"{doc}: no image references")
        return 0
    broken = 0
    for ref in refs:
        if ref.startswith(("http://", "https://", "data:", "//")):
            print(f"{doc}: REMOTE  {ref[:80]}")
            continue
        resolved = (doc.parent / urllib.parse.unquote(ref)).resolve()
        if resolved.is_file():
            print(f"{doc}: OK      {ref}")
        else:
            print(f"{doc}: BROKEN  {ref}  ->  {resolved}")
            broken += 1
    return broken


def bare_fence_openers(lines: list[str]) -> list[int]:
    """1-indexed line numbers of ``` fences that OPEN a block without a language."""
    openers, in_block = [], False
    for n, line in enumerate(lines, 1):
        if not line.startswith("```"):
            continue
        if in_block:
            in_block = False          # this fence closes; a bare closer is fine
            continue
        in_block = True
        if line.strip() == "```":     # opens with no language
            openers.append(n)
    return openers


def check_portability(doc: Path) -> int:
    """Print one line per violation. Return the count."""
    text = doc.read_text(encoding="utf-8", errors="replace")
    lines = text.splitlines()
    failures = 0

    for label, pattern, hint in PORTABILITY_CHECKS:
        for n, line in enumerate(lines, 1):
            if pattern.search(line):
                print(f"{doc}:{n}: {label.upper()}  {line.strip()[:90]}  ({hint})")
                failures += 1

    for n in bare_fence_openers(lines):
        print(f"{doc}:{n}: UNLANGUAGED FENCE  ```  (add a language, e.g. ```python)")
        failures += 1

    return failures


def main() -> int:
    args = [a for a in sys.argv[1:] if a != "--portability"]
    portability = "--portability" in sys.argv[1:]

    if not args:
        print(__doc__)
        return 2

    broken_total = portability_total = 0
    for doc_arg in args:
        doc = Path(doc_arg)
        if not doc.is_file():
            print(f"error: no such document: {doc}", file=sys.stderr)
            broken_total += 1
            continue
        broken_total += check_references(doc)
        if portability:
            portability_total += check_portability(doc)

    print()
    sys.stdout.flush()          # keep the per-line report ahead of the summary
    if broken_total:
        print(f"{broken_total} broken reference(s)", file=sys.stderr)
    if portability_total:
        print(f"{portability_total} portability violation(s)", file=sys.stderr)
    if not broken_total and not portability_total:
        print("verify-references: zero BROKEN" + (", portability clean" if portability else ""))

    return 1 if (broken_total or portability_total) else 0


if __name__ == "__main__":
    sys.exit(main())
