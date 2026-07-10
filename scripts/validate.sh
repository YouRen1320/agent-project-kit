#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

"$repo_root/scripts/validate-structure.sh"
python3 "$repo_root/scripts/validate-links.py"
python3 "$repo_root/scripts/validate-agent-entrypoints.py"
"$repo_root/scripts/check-public-safety.sh"

printf 'all validations passed\n'
