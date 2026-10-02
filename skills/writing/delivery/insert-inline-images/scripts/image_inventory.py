#!/usr/bin/env python3
"""Inventory candidate images: format, pixel size, aspect, file size, relative URL.

Stdlib only. Supports PNG, JPEG, GIF, WebP, SVG.

Usage:
    image_inventory.py IMAGE_OR_DIR [IMAGE_OR_DIR ...] [--relative-to TARGET_DOC]

--relative-to computes the URL-encoded relative src to use from TARGET_DOC
(a file path; the src is relative to its parent directory).
"""

from __future__ import annotations

import argparse
import re
import struct
import sys
import urllib.parse
from pathlib import Path

IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg"}


def png_size(data: bytes) -> tuple[int, int] | None:
    if data[:8] != b"\x89PNG\r\n\x1a\n" or len(data) < 24:
        return None
    width, height = struct.unpack(">II", data[16:24])
    return width, height


def gif_size(data: bytes) -> tuple[int, int] | None:
    if data[:6] not in (b"GIF87a", b"GIF89a") or len(data) < 10:
        return None
    width, height = struct.unpack("<HH", data[6:10])
    return width, height


def jpeg_size(data: bytes) -> tuple[int, int] | None:
    # Scan JPEG segments for a Start-Of-Frame marker, which carries dimensions.
    if data[:2] != b"\xff\xd8":
        return None
    offset = 2
    while offset + 9 < len(data):
        if data[offset] != 0xFF:
            offset += 1
            continue
        marker = data[offset + 1]
        if 0xC0 <= marker <= 0xCF and marker not in (0xC4, 0xC8, 0xCC):
            height, width = struct.unpack(">HH", data[offset + 5 : offset + 9])
            return width, height
        segment_length = struct.unpack(">H", data[offset + 2 : offset + 4])[0]
        offset += 2 + segment_length
    return None


def webp_size(data: bytes) -> tuple[int, int] | None:
    if data[:4] != b"RIFF" or data[8:12] != b"WEBP" or len(data) < 30:
        return None
    chunk = data[12:16]
    if chunk == b"VP8X":
        width = int.from_bytes(data[24:27], "little") + 1
        height = int.from_bytes(data[27:30], "little") + 1
        return width, height
    if chunk == b"VP8 ":
        width, height = struct.unpack("<HH", data[26:30])
        return width & 0x3FFF, height & 0x3FFF
    if chunk == b"VP8L":
        bits = int.from_bytes(data[21:25], "little")
        return (bits & 0x3FFF) + 1, ((bits >> 14) & 0x3FFF) + 1
    return None


def svg_size(data: bytes) -> tuple[int, int] | None:
    text = data[:4096].decode("utf-8", errors="ignore")
    viewbox = re.search(r'viewBox=["\']\s*[\d.+-]+[\s,]+[\d.+-]+[\s,]+([\d.]+)[\s,]+([\d.]+)', text)
    if viewbox:
        return round(float(viewbox.group(1))), round(float(viewbox.group(2)))
    width = re.search(r'<svg[^>]*\swidth=["\']([\d.]+)', text)
    height = re.search(r'<svg[^>]*\sheight=["\']([\d.]+)', text)
    if width and height:
        return round(float(width.group(1))), round(float(height.group(1)))
    return None


def read_size(path: Path) -> tuple[str, tuple[int, int] | None]:
    data = path.read_bytes()
    for fmt, parser in (
        ("PNG", png_size),
        ("JPEG", jpeg_size),
        ("GIF", gif_size),
        ("WebP", webp_size),
        ("SVG", svg_size),
    ):
        size = parser(data)
        if size:
            return fmt, size
    return path.suffix.lstrip(".").upper() or "?", None


def describe_aspect(width: int, height: int) -> str:
    ratio = width / height
    if ratio >= 2.4:
        return "ultra-wide banner"
    if ratio >= 1.15:
        return "landscape"
    if ratio > 0.87:
        return "square-ish"
    return "portrait/tall"


def relative_src(image: Path, target_doc: Path) -> str:
    import os

    relative = os.path.relpath(image.resolve(), target_doc.resolve().parent)
    return urllib.parse.quote(relative.replace(os.sep, "/"))


def collect_images(inputs: list[str]) -> list[Path]:
    images: list[Path] = []
    for raw in inputs:
        path = Path(raw)
        if path.is_dir():
            images.extend(
                p for p in sorted(path.rglob("*")) if p.suffix.lower() in IMAGE_EXTENSIONS
            )
        elif path.is_file():
            images.append(path)
        else:
            print(f"warning: not found: {path}", file=sys.stderr)
    return images


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("inputs", nargs="+", help="image files or directories")
    parser.add_argument("--relative-to", type=Path, help="target document to compute src paths for")
    args = parser.parse_args()

    images = collect_images(args.inputs)
    if not images:
        print("no images found", file=sys.stderr)
        return 1

    for image in images:
        fmt, size = read_size(image)
        kilobytes = image.stat().st_size // 1024
        if size:
            width, height = size
            geometry = (
                f"{width}x{height}  {describe_aspect(width, height)}"
                f"  retina-target {width // 2}px"
            )
        else:
            geometry = "unknown size"
        line = f"{image}  |  {fmt}  {geometry}  |  {kilobytes} KB"
        if kilobytes > 500:
            line += "  (heavy: consider compressing for web)"
        if args.relative_to:
            line += f"\n    src: {relative_src(image, args.relative_to)}"
        print(line)
    return 0


if __name__ == "__main__":
    sys.exit(main())
