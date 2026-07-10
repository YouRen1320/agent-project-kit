#!/usr/bin/env python3
"""Check local evidence required before the kit repository becomes public."""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
BLOCKER_MARKER = "PUBLICATION-BLOCKER"
PLACEHOLDER_RE = re.compile(r"YOUR_|REPLACE_|<[A-Z][A-Z0-9_]*>")
PRIVATE_CONTACT_RE = re.compile(r"\]\((?:mailto:|https://)[^)]+\)", re.IGNORECASE)


def run(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        args,
        cwd=ROOT,
        check=False,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )


def main() -> int:
    errors: list[str] = []

    validation = run("./scripts/validate.sh")
    if validation.returncode != 0:
        errors.append("repository validation failed:\n" + validation.stdout.rstrip())

    version = (ROOT / ".agent-kit-version").read_text(encoding="utf-8").strip()
    changelog = (ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
    release_heading = re.compile(
        rf"^## \[{re.escape(version)}\] - \d{{4}}-\d{{2}}-\d{{2}}$", re.MULTILINE
    )
    if not release_heading.search(changelog):
        errors.append(f"CHANGELOG.md has no dated release heading for version {version}")

    codeowners_path = ROOT / ".github" / "CODEOWNERS"
    if not codeowners_path.is_file():
        errors.append(".github/CODEOWNERS is missing; configure real maintainers")
    else:
        codeowners = codeowners_path.read_text(encoding="utf-8")
        rules = [
            line.strip()
            for line in codeowners.splitlines()
            if line.strip() and not line.lstrip().startswith("#")
        ]
        if not rules or not all("@" in rule for rule in rules):
            errors.append(".github/CODEOWNERS must contain owner rules with GitHub users or teams")
        if PLACEHOLDER_RE.search(codeowners):
            errors.append(".github/CODEOWNERS still contains a placeholder")

    security = (ROOT / "SECURITY.md").read_text(encoding="utf-8")
    if BLOCKER_MARKER in security:
        errors.append("SECURITY.md still contains a publication blocker")
    elif "private vulnerability-reporting feature" not in security and not PRIVATE_CONTACT_RE.search(
        security
    ):
        errors.append("SECURITY.md has no explicit private reporting route")

    conduct = (ROOT / "CODE_OF_CONDUCT.md").read_text(encoding="utf-8")
    if BLOCKER_MARKER in conduct:
        errors.append("CODE_OF_CONDUCT.md still contains a publication blocker")
    elif not PRIVATE_CONTACT_RE.search(conduct):
        errors.append("CODE_OF_CONDUCT.md has no monitored private contact link")

    inside_git = run("git", "rev-parse", "--is-inside-work-tree")
    if inside_git.returncode != 0 or inside_git.stdout.strip() != "true":
        errors.append("the kit is not inside a Git worktree")
    else:
        head = run("git", "rev-parse", "--verify", "HEAD")
        if head.returncode != 0:
            errors.append("the repository has no initial commit")

        branch = run("git", "branch", "--show-current")
        if branch.returncode != 0 or branch.stdout.strip() != "main":
            errors.append("the publication branch must be main")

        origin = run("git", "remote", "get-url", "origin")
        if origin.returncode != 0 or not origin.stdout.strip():
            errors.append("the repository has no origin remote")
        elif "github.com" not in origin.stdout.lower():
            errors.append("origin must point to the intended GitHub repository")

        status = run("git", "status", "--porcelain=v1")
        if status.returncode != 0:
            errors.append("Git status could not be read")
        elif status.stdout.strip():
            errors.append("the Git worktree is not clean")

    if errors:
        print("publication readiness failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print("local publication-readiness validation passed")
    print("hosting settings and remote CI still require verification on GitHub")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
