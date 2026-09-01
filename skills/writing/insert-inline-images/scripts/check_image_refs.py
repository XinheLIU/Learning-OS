#!/usr/bin/env python3
"""Verify every image reference in Markdown/HTML documents resolves to a file on disk.

Stdlib only. Checks Markdown ![alt](src), HTML <img src=...>, and CSS url(...).
Remote (http/https/data:) references are listed but not checked.

Usage:
    check_image_refs.py DOC.md DOC.html [...]

Exit code 1 if any local reference is broken.
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


def extract_refs(text: str, suffix: str) -> list[str]:
    refs: list[str] = []
    if suffix == ".md":
        refs += MARKDOWN_IMAGE.findall(text)
    else:
        for srcset in HTML_IMG_SRC.findall(text):
            refs += [part.strip().split(" ")[0] for part in srcset.split(",") if part.strip()]
        refs += [u for u in CSS_URL.findall(text) if u.lower().endswith(IMAGE_EXTENSIONS)]
    return refs


def main() -> int:
    if len(sys.argv) < 2:
        print(__doc__)
        return 2

    broken_total = 0
    for doc_arg in sys.argv[1:]:
        doc = Path(doc_arg)
        if not doc.is_file():
            print(f"error: no such document: {doc}", file=sys.stderr)
            broken_total += 1
            continue
        refs = extract_refs(doc.read_text(encoding="utf-8", errors="replace"), doc.suffix.lower())
        if not refs:
            print(f"{doc}: no image references")
            continue
        for ref in refs:
            if ref.startswith(("http://", "https://", "data:", "//")):
                print(f"{doc}: REMOTE  {ref[:80]}")
                continue
            resolved = (doc.parent / urllib.parse.unquote(ref)).resolve()
            if resolved.is_file():
                print(f"{doc}: OK      {ref}")
            else:
                print(f"{doc}: BROKEN  {ref}  ->  {resolved}")
                broken_total += 1
    if broken_total:
        print(f"\n{broken_total} broken reference(s)", file=sys.stderr)
    return 1 if broken_total else 0


if __name__ == "__main__":
    sys.exit(main())
