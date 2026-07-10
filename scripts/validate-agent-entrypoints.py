#!/usr/bin/env python3
"""Validate shared Codex and Claude Code instruction and skill entry points."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
CODEX_SKILL_ROOT = ROOT / ".agents" / "skills"
CLAUDE_SKILL_ROOT = ROOT / ".claude" / "skills"
FRONTMATTER_RE = re.compile(r"\A---\n(.*?)\n---\n", re.DOTALL)
PATH_RE = re.compile(r"`([^`\n]+\.md)`")
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def parse_skill(path: Path, errors: list[str]) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    match = FRONTMATTER_RE.match(text)
    if not match:
        errors.append(f"{path.relative_to(ROOT)}: missing YAML frontmatter")
        return {}

    metadata: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if ":" not in line:
            errors.append(f"{path.relative_to(ROOT)}: invalid frontmatter line: {line}")
            continue
        key, value = line.split(":", 1)
        metadata[key.strip()] = value.strip()

    name = metadata.get("name", "")
    description = metadata.get("description", "")
    if not NAME_RE.fullmatch(name):
        errors.append(f"{path.relative_to(ROOT)}: invalid or missing skill name")
    if name and path.parent.name != name:
        errors.append(f"{path.relative_to(ROOT)}: directory and skill name differ")
    if not description:
        errors.append(f"{path.relative_to(ROOT)}: missing skill description")

    body = text[match.end() :]
    for raw in PATH_RE.findall(body):
        if raw.startswith(("http://", "https://")):
            continue
        target = (path.parent / raw).resolve()
        try:
            target.relative_to(ROOT)
        except ValueError:
            errors.append(f"{path.relative_to(ROOT)}: reference escapes repository: {raw}")
            continue
        if not target.is_file():
            errors.append(f"{path.relative_to(ROOT)}: missing referenced file: {raw}")

    return metadata


def main() -> int:
    errors: list[str] = []

    claude_lines = [
        line.strip()
        for line in (ROOT / "CLAUDE.md").read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
    if not claude_lines or claude_lines[0] != "@AGENTS.md":
        errors.append("CLAUDE.md must begin with @AGENTS.md")

    codex_skills = {path.parent.name: path for path in CODEX_SKILL_ROOT.glob("*/SKILL.md")}
    claude_skills = {path.parent.name: path for path in CLAUDE_SKILL_ROOT.glob("*/SKILL.md")}
    if not codex_skills:
        errors.append("no Codex repository skills were found")
    if codex_skills.keys() != claude_skills.keys():
        only_codex = sorted(codex_skills.keys() - claude_skills.keys())
        only_claude = sorted(claude_skills.keys() - codex_skills.keys())
        if only_codex:
            errors.append("skills missing from Claude Code: " + ", ".join(only_codex))
        if only_claude:
            errors.append("skills missing from Codex: " + ", ".join(only_claude))

    index = (ROOT / ".agents" / "index.md").read_text(encoding="utf-8")
    for skill_name in sorted(codex_skills.keys() | claude_skills.keys()):
        codex_path = codex_skills.get(skill_name)
        claude_path = claude_skills.get(skill_name)
        codex_metadata = parse_skill(codex_path, errors) if codex_path else {}
        claude_metadata = parse_skill(claude_path, errors) if claude_path else {}
        if codex_metadata and claude_metadata and codex_metadata != claude_metadata:
            errors.append(f"Codex and Claude metadata differ for {skill_name}")

        if codex_path:
            openai_path = codex_path.parent / "agents" / "openai.yaml"
            if not openai_path.is_file():
                errors.append(f"{openai_path.relative_to(ROOT)} is missing")
            else:
                openai_yaml = openai_path.read_text(encoding="utf-8")
                for key in ("display_name:", "short_description:", "default_prompt:"):
                    if key not in openai_yaml:
                        errors.append(
                            f"{openai_path.relative_to(ROOT)} is missing {key.rstrip(':')}"
                        )
                if f"${skill_name}" not in openai_yaml:
                    errors.append(
                        f"{openai_path.relative_to(ROOT)} default prompt must mention ${skill_name}"
                    )

        for entry in (
            f"skills/{skill_name}/SKILL.md",
            f"../.claude/skills/{skill_name}/SKILL.md",
        ):
            if entry not in index:
                errors.append(f".agents/index.md does not register {entry}")

    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print("agent entrypoint validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
