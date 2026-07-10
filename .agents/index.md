# Agent Procedure Index

This directory is the canonical project procedure library. The repository-level agent instruction file should stay small and route task-specific work here.

## Read Order

1. Read the repository's active agent instructions.
2. Read the relevant files under `project/`.
3. Select the matching workflow or runbook below.
4. Use the linked template for the review or final report.

If project placeholders are incomplete, investigate the repository first. Do not guess deployment targets, data environments, owners, or branch policy.

## Project Profile

| Document | Purpose |
| --- | --- |
| `project/overview.md` | Product purpose, architecture, scope, invariants, and project-level non-goals |
| `project/repositories.md` | Repository/component inventory and cross-repository dependencies |
| `project/commands.md` | Authoritative setup, lint, test, build, and local-run commands |
| `project/environments.md` | Environment boundaries, configuration sources, access, and safety rules |
| `project/api-conventions.md` | Project API paths, envelopes, authentication, versioning, and compatibility rules |
| `project/ownership.md` | Module ownership, escalation, and cross-team review expectations |

## Workflows

| Request type | Required document | Gate |
| --- | --- | --- |
| Business feature, API/data contract, status model, directory architecture, or cross-component change | `workflows/module-delivery.md` | Review goal, impact, options, recommendation, migration, rollback, and completion criteria; wait for explicit approval before implementation |
| Code review, audit, regression check, or risk assessment | `workflows/code-review.md` | Read-only by default; findings first |
| Styling, layout, accessibility, interaction, or responsive UI work | `workflows/ui-change.md` | Define visual scope and verification; broad redesigns require option approval |
| Commit, push, merge, pull request, tag, or release work | `workflows/git-release.md` | Confirm repository state, target branch, verification, and merge policy before publishing |

## Runbooks

| Operation | Required document | Gate |
| --- | --- | --- |
| Schema migration, persisted-data repair, cache cleanup, or storage mutation | `runbooks/database-change.md` | Confirm environment, backup, expected impact, verification, and rollback before writes |
| Deployment or environment promotion | `runbooks/server-deploy.md` | Confirm target, artifact, dependencies, health checks, and rollback before execution |
| Production rollback or incident recovery | `runbooks/production-rollback.md` | Confirm failed component, last known good state, user impact, data implications, and verification |

## Templates And References

| Document | Use |
| --- | --- |
| `templates/final-report.md` | Final delivery report |
| `templates/review-report.md` | Code review report |
| `templates/deploy-report.md` | Deployment or rollback report |
| `templates/module-registry.md` | Project module and consumer registry |
| `templates/decision-record.md` | Long-lived architecture or policy decision |
| `references/api-contract.md` | Generic API contract review discipline |
| `references/project-bootstrap.md` | New-project setup and existing-project adoption discipline |
| `decisions/README.md` | Decision-record storage and maintenance rules |

## Skills

| Platform | Entry point | Authoritative guidance |
| --- | --- | --- |
| Codex | `skills/api-contract/SKILL.md` | `references/api-contract.md` and `project/api-conventions.md` |
| Claude Code | `../.claude/skills/api-contract/SKILL.md` | The same `.agents/` references |
| Codex | `skills/project-bootstrap/SKILL.md` | `references/project-bootstrap.md` |
| Claude Code | `../.claude/skills/project-bootstrap/SKILL.md` | The same `.agents/` reference |

Skill entry points should stay concise. Keep detailed policy in one shared reference and validate both platform entries after changes.

## Local-Only Boundary

`local/` is ignored except for its safety README. Do not use it as a long-term credential or data archive; prefer approved secret and operations systems.

## Maintenance Rules

- Keep stable policy separate from environment-specific facts and incident history.
- Register every shared workflow, runbook, template, and reference in this index.
- Put target-specific commands and facts in `project/`, not in generic workflows.
- Never store secrets, tokens, credentials, private keys, personal data, or database dumps in this library.
- Mark unverified claims explicitly and include a source or owner for operational facts.
- Remove stale guidance instead of keeping silent compatibility behavior.
