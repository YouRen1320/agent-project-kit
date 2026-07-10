#!/usr/bin/env python3
"""Validate common repository-relative Markdown link and image targets."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parent.parent
INLINE_LINK_RE = re.compile(r"!?\[[^\]]*\]\((<[^>]+>|[^)\s]+)(?:\s+[^)]*)?\)")
REFERENCE_USE_RE = re.compile(r"!?\[([^\]]*)\]\[([^\]]*)\]")
REFERENCE_DEF_RE = re.compile(r"^\s*\[([^\]]+)\]:\s*(<[^>]+>|\S+)", re.MULTILINE)
SKIP_PREFIXES = ("http://", "https://", "mailto:", "#")


def markdown_files() -> list[Path]:
    return sorted(path for path in ROOT.rglob("*.md") if ".git" not in path.parts)


def without_fenced_code(text: str) -> str:
    kept: list[str] = []
    fence: str | None = None
    for line in text.splitlines(keepends=True):
        marker = line.lstrip()[:3]
        if marker in {"```", "~~~"}:
            fence = None if fence == marker else marker if fence is None else fence
            continue
        if fence is None:
            kept.append(line)
    return "".join(kept)


def target_from(raw: str) -> str:
    raw = raw.strip()
    if raw.startswith("<") and raw.endswith(">"):
        return raw[1:-1]
    return raw


def validate_target(source: Path, raw: str, errors: list[str]) -> None:
    raw = target_from(raw)
    if not raw or raw.lower().startswith(SKIP_PREFIXES):
        return
    target_text = unquote(raw.split("#", 1)[0])
    if not target_text or "<" in target_text or ">" in target_text:
        return
    target = (source.parent / target_text).resolve()
    try:
        target.relative_to(ROOT)
    except ValueError:
        errors.append(f"{source.relative_to(ROOT)}: link escapes repository: {raw}")
        return
    if not target.exists():
        errors.append(f"{source.relative_to(ROOT)}: missing target: {raw}")


def main() -> int:
    errors: list[str] = []
    for source in markdown_files():
        text = without_fenced_code(source.read_text(encoding="utf-8"))
        definitions = {
            match.group(1).strip().lower(): match.group(2)
            for match in REFERENCE_DEF_RE.finditer(text)
        }
        for match in INLINE_LINK_RE.finditer(text):
            validate_target(source, match.group(1), errors)
        for match in REFERENCE_USE_RE.finditer(text):
            label = (match.group(2) or match.group(1)).strip().lower()
            if label not in definitions:
                errors.append(f"{source.relative_to(ROOT)}: missing reference definition: {label}")
                continue
            validate_target(source, definitions[label], errors)

    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print("repository-relative link and image target validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
