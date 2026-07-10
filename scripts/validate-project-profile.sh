#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$repo_root"

if ! command -v rg >/dev/null 2>&1; then
  printf 'ripgrep (rg) is required for project-profile validation\n' >&2
  exit 1
fi

set +e
matches="$(rg -l '<[A-Z][A-Z0-9_]*>' .agents/project 2>&1)"
status=$?
set -e

if [[ "$status" -eq 0 ]]; then
  printf 'project profile still contains placeholders in:\n%s\n' "$matches" >&2
  printf 'replace or explicitly remove every applicable placeholder before relying on this kit in an adopted project\n' >&2
  exit 1
fi

if [[ "$status" -ne 1 ]]; then
  printf 'project-profile scanner failed\n%s\n' "$matches" >&2
  exit 2
fi

printf 'project-profile validation passed\n'
