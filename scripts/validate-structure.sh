#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$repo_root"

required=(
  README.md
  README.en.md
  LICENSE
  CHANGELOG.md
  CODE_OF_CONDUCT.md
  AGENTS.md
  CLAUDE.md
  .agent-kit-version
  .gitignore
  .gitattributes
  .editorconfig
  .agents/index.md
  .agents/local/README.md
  .agents/project/overview.md
  .agents/project/repositories.md
  .agents/project/commands.md
  .agents/project/environments.md
  .agents/project/api-conventions.md
  .agents/project/ownership.md
  .agents/workflows/module-delivery.md
  .agents/workflows/code-review.md
  .agents/workflows/ui-change.md
  .agents/workflows/git-release.md
  .agents/runbooks/database-change.md
  .agents/runbooks/server-deploy.md
  .agents/runbooks/production-rollback.md
  .agents/references/api-contract.md
  .agents/references/project-bootstrap.md
  .agents/templates/final-report.md
  .agents/templates/review-report.md
  .agents/templates/deploy-report.md
  .agents/templates/module-registry.md
  .agents/templates/decision-record.md
  .agents/decisions/README.md
  .agents/skills/api-contract/SKILL.md
  .agents/skills/api-contract/agents/openai.yaml
  .agents/skills/project-bootstrap/SKILL.md
  .agents/skills/project-bootstrap/agents/openai.yaml
  .claude/skills/api-contract/SKILL.md
  .claude/skills/project-bootstrap/SKILL.md
  SECURITY.md
  CONTRIBUTING.md
  docs/getting-started.md
  docs/existing-project.md
  docs/customization.md
  docs/how-agents-load-rules.md
  docs/distribution.md
  docs/upgrading.md
  docs/publishing.md
  docs/publishing.zh-CN.md
  examples/single-repo-webapp/README.md
  examples/multi-app-platform/README.md
  examples/existing-project-incremental/README.md
  scripts/validate.sh
  scripts/validate-structure.sh
  scripts/validate-links.py
  scripts/validate-agent-entrypoints.py
  scripts/check-public-safety.sh
  scripts/validate-project-profile.sh
  scripts/validate-publish-readiness.py
  scripts/test.sh
  tests/test_validators.py
  .github/workflows/validate.yml
  .github/dependabot.yml
  .github/CODEOWNERS
  .github/CODEOWNERS.example
  .github/PULL_REQUEST_TEMPLATE.md
  .github/ISSUE_TEMPLATE/config.yml
  .github/ISSUE_TEMPLATE/bug_report.yml
  .github/ISSUE_TEMPLATE/feature_request.yml
)

failed=0
for path in "${required[@]}"; do
  if [[ ! -f "$path" ]]; then
    printf 'missing required file: %s\n' "$path" >&2
    failed=1
  fi
done

if [[ -f CLAUDE.md ]] && ! grep -Eq '^@AGENTS\.md$' CLAUDE.md; then
  printf 'CLAUDE.md must import @AGENTS.md\n' >&2
  failed=1
fi

for skill in .agents/skills/api-contract/SKILL.md .claude/skills/api-contract/SKILL.md; do
  if [[ -f "$skill" ]] && ! grep -Eq '^name: api-contract$' "$skill"; then
    printf 'skill name mismatch: %s\n' "$skill" >&2
    failed=1
  fi
done

if [[ -f .agent-kit-version ]] && ! grep -Eq '^[0-9]+\.[0-9]+\.[0-9]+$' .agent-kit-version; then
  printf '.agent-kit-version must contain one semantic version\n' >&2
  failed=1
fi

for script in scripts/validate.sh scripts/validate-structure.sh scripts/validate-project-profile.sh scripts/validate-publish-readiness.py scripts/check-public-safety.sh scripts/validate-links.py scripts/validate-agent-entrypoints.py scripts/test.sh; do
  if [[ -f "$script" && ! -x "$script" ]]; then
    printf 'validation entry must be executable: %s\n' "$script" >&2
    failed=1
  fi
done

if git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  tracked_local="$(git ls-files .agents/local | grep -v '^.agents/local/README\.md$' || true)"
  if [[ -n "$tracked_local" ]]; then
    printf 'local-only files must not be tracked:\n%s\n' "$tracked_local" >&2
    failed=1
  fi
fi

if find . -name .DS_Store -print -quit | grep -q .; then
  printf 'macOS metadata files must not be committed\n' >&2
  failed=1
fi

if find . -type l -print -quit | grep -q .; then
  printf 'symbolic links are not used so the template remains portable\n' >&2
  failed=1
fi

if [[ "$failed" -ne 0 ]]; then
  exit 1
fi

printf 'structure validation passed\n'
