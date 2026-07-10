# Agent Project Kit Guidance

## Scope

- This file applies to the whole repository.
- A nested `AGENTS.md` or `AGENTS.override.md` may add narrower rules for its subtree.
- Project facts belong in `.agents/project/`; reusable procedures belong elsewhere under `.agents/`.

## Start Here

Before acting:

1. Read `.agents/index.md`.
2. Read `.agents/project/overview.md` and the project files relevant to the request.
3. Inspect the current worktree and preserve unrelated user changes.
4. Classify the request and follow the matching workflow or runbook.

This public repository intentionally ships `.agents/project/` as an unconfigured template. When maintaining the kit itself, use `./scripts/validate.sh` as the authoritative check and treat project-profile placeholders as template content. In an adopted application repository, complete the profile and run `./scripts/validate-project-profile.sh` before relying on its commands or environment facts.

## Mandatory Routing

| Request | Required guidance | Gate |
| --- | --- | --- |
| Initialize the kit, adopt it into an existing repository, or complete the project profile | `.agents/references/project-bootstrap.md` | Inventory existing guidance and repository evidence; compare merge options before structural changes. |
| Business module, API/data contract, state machine, data model, directory architecture, or cross-component change | `.agents/workflows/module-delivery.md` | Compare viable options and wait for explicit confirmation before implementation. |
| Code review, audit, or regression review | `.agents/workflows/code-review.md` | Report findings first; do not edit unless asked. |
| UI-only styling, layout, or interaction change | `.agents/workflows/ui-change.md` | Define visual scope and verification before editing. |
| Commit, merge, push, PR, or release | `.agents/workflows/git-release.md` | Confirm branch, remote state, checks, and repository policy. |
| Database, persisted-data, cache, or object-storage mutation | `.agents/runbooks/database-change.md` | Confirm environment, backup, expected impact, verification, and rollback. |
| Deployment | `.agents/runbooks/server-deploy.md` | Confirm target, artifact, verification, and rollback. |
| Production rollback | `.agents/runbooks/production-rollback.md` | Confirm failed component and last known good state. |

## Required Planning for Major Changes

Before implementation:

- Define the goal, affected scope, assumptions, and explicit non-goals.
- Describe the current problem using repository evidence.
- Present two or three viable options when reasonable.
- Compare implementation cost, migration cost, risk, rollback difficulty, and long-term maintainability.
- Recommend one option and wait for the user's selection.
- Define measurable completion criteria.

Treat architecture, data-model, API-contract, directory, cross-component, and destructive changes as major.

## Safety and Quality

- Never copy secrets, credentials, personal data, production dumps, or private infrastructure details into tracked files.
- Keep local-only material under `.agents/local/`; prefer a secret manager or environment variables for real credentials.
- Confirm the target environment before commands that can change external state.
- Do not overwrite or revert user changes unless explicitly requested.
- Avoid opportunistic refactors outside the agreed scope.
- Separate verified evidence from judgment and unverified claims.
- In an adopted project, use verified commands from `.agents/project/commands.md`; do not invent commands when the repository provides them.

## Final Delivery

Use `.agents/templates/final-report.md`. Always state:

- What changed and where.
- What was verified and what was not.
- Deployment or data status when relevant.
- Compatibility compromises.
- Intentional non-goals or work deliberately left undone.

## Validation Commands

- Maintaining this kit: run `./scripts/validate.sh` and `./scripts/test.sh`.
- Adopting the kit into a product: run `./scripts/validate-project-profile.sh`, then `./scripts/validate.sh`, plus the verified project commands in `.agents/project/commands.md`.
- Publishing this kit: run `python3 scripts/validate-publish-readiness.py` only after maintainer configuration, a clean commit, and `origin` exist.
- Never report a command as passed unless its current output was observed.

## Maintaining This Kit

- Keep this router concise.
- Register new guidance in `.agents/index.md`.
- Put detailed procedures in workflows, runbooks, references, or skills rather than duplicating them here.
- Keep Codex and Claude skill entry points aligned while maintaining one authoritative reference.
