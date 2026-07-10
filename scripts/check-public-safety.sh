#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$repo_root"

if ! command -v rg >/dev/null 2>&1; then
  printf 'ripgrep (rg) is required for public-safety validation\n' >&2
  exit 1
fi

common=(--hidden --no-ignore -l --glob '!.git/**' --glob '!scripts/check-public-safety.sh')
failed=0

check() {
  local label="$1"
  local pattern="$2"
  local matches
  local status
  set +e
  matches="$(rg -P "${common[@]}" -e "$pattern" . 2>&1)"
  status=$?
  set -e
  if [[ "$status" -eq 0 ]]; then
    printf '%s detected in:\n%s\n' "$label" "$matches" >&2
    failed=1
  elif [[ "$status" -ne 1 ]]; then
    printf 'public-safety scanner failed during %s check\n' "$label" >&2
    printf '%s\n' "$matches" >&2
    exit 2
  fi
}

check 'private absolute home path' '(/Users/[^/\s]+|/home/[^/\s]+)'
check 'phone-like identifier' '(?<![0-9])1[3-9][0-9]{9}(?![0-9])'
check 'IPv4 address' '(?<![0-9])(?:[0-9]{1,3}\.){3}[0-9]{1,3}(?![0-9])'
check 'private key material' '-----BEGIN (?:[A-Z0-9]+ )*PRIVATE KEY-----'
check 'known token prefix' '(?:AKIA[0-9A-Z]{16}|gh[pousr]_[A-Za-z0-9_]{20,}|github_pat_[A-Za-z0-9_]{20,}|sk-[A-Za-z0-9_-]{20,})'

if [[ -n "${EXTRA_DENY_PATTERN:-}" ]]; then
  check 'caller-supplied private identifier' "$EXTRA_DENY_PATTERN"
fi

if [[ "$failed" -ne 0 ]]; then
  exit 1
fi

printf 'public-safety validation passed\n'
