# Project Bootstrap Reference

Use this reference to configure Agent Project Kit in a new repository or merge it into an existing repository. The outcome is an evidence-backed project profile and working Codex and Claude Code entry points, not a generic copy of template placeholders.

## 1. Classify The Adoption

Choose one path before editing:

| Situation | Approach |
| --- | --- |
| New repository created from the template | Complete the profile, remove inapplicable guidance, and replace template ownership and product documentation |
| Existing repository with agent guidance | Inventory and merge; never overwrite root instructions or skills blindly |
| Existing repository without agent guidance | Add the reusable core, then build the profile from repository evidence |
| Agent Project Kit repository itself | Maintain template placeholders; use kit validation rather than filling the profile with a real product |

State the goal, affected files, assumptions, and explicit non-goals. If adoption changes an established directory structure, policy, or cross-agent contract, compare viable merge strategies and obtain approval before editing.

## 2. Inventory Evidence

Inspect before writing:

- Product README, architecture documents, manifests, and source entry points.
- Build, lint, test, run, migration, and release configuration.
- Components, repositories, generated sources, and independently delivered consumers.
- Environment boundaries and configuration sources without reading or copying secret values.
- API schemas, client wrappers, events, uploads, error formats, and authentication context.
- Existing `AGENTS.md`, `CLAUDE.md`, `.agents/`, `.claude/`, hooks, and CI policy.
- Ownership evidence such as CODEOWNERS, team documentation, or repository settings.

Do not guess missing commands, owners, targets, or policies. Record an unknown with a follow-up owner instead.

## 3. Complete The Project Profile

Populate each file from evidence:

| File | Required outcome |
| --- | --- |
| `../project/overview.md` | Product purpose, users, components, invariants, scope, and delivery model |
| `../project/repositories.md` | Repository/component inventory, producers, consumers, and excluded sources |
| `../project/commands.md` | Commands that were found and verified, including prerequisites and expected results |
| `../project/environments.md` | Environment purpose, data class, configuration source, approval, and rollback boundary |
| `../project/api-conventions.md` | Paths, envelopes, identity, errors, compatibility, and generation rules |
| `../project/ownership.md` | Primary and backup ownership, escalation, and cross-component review rules |

Remove a field only when it cannot apply. Do not replace a meaningful unknown with invented content merely to make validation pass.

## 4. Reconcile Agent Guidance

- Keep root `AGENTS.md` concise and limited to durable routing, hard gates, commands, and final-report expectations.
- Keep `CLAUDE.md` importing `@AGENTS.md`; place only Claude-specific differences below the import.
- Preserve useful existing rules in the closest valid scope.
- Remove duplicate or contradictory copies after selecting one authoritative source.
- Keep task-specific procedures in workflows, runbooks, references, or skills.
- Keep secrets and private operations outside tracked instruction files.

When two existing rules conflict, document the alternatives, risks, migration impact, rollback, and recommended authoritative rule. Wait for the user or owner to decide.

## 5. Select Procedures And Skills

- Retain workflows that match actual development and review work.
- Retain database, deployment, and rollback runbooks whenever those operations are possible, even if executable commands remain in a private operations system.
- Remove irrelevant technology examples rather than presenting them as project facts.
- Add a skill only for a focused workflow that should load on demand.
- Keep matching Codex and Claude skill entry points aligned when both clients are supported.

## 6. Replace Template Ownership

For a repository created from the template, replace:

- Product README and support path.
- `.github/CODEOWNERS` users or teams.
- Security reporting and conduct reporting routes.
- Supported-version and release statements.
- Issue labels, branch names, CI commands, and protection expectations when they differ.

Do not leave the template maintainer responsible for a generated project's code or reports.

## 7. Verify Adoption

Run from the repository root:

```sh
./scripts/validate-project-profile.sh
./scripts/validate.sh
```

Then verify behavior:

- Start Codex at the root and an important subdirectory; confirm it identifies `AGENTS.md`, `.agents/index.md`, and the expected repository skills.
- In Claude Code, use `/memory` to confirm `CLAUDE.md` and its imported guidance, then invoke one project skill directly.
- Try sanitized review, API-change, UI-change, data-change, and deployment prompts; confirm each routes to the expected gate.
- Run the real project commands recorded in `../project/commands.md` for the affected components.

## Completion Criteria

Adoption is complete only when:

- The project profile contains no unresolved template placeholders.
- Commands and ownership are evidence-backed or explicitly marked unknown with follow-up ownership.
- Existing instructions were preserved, deliberately superseded, or explicitly removed.
- Codex and Claude Code load the intended guidance and skills.
- Required repository validation and project checks pass.
- Compatibility compromises, unverified areas, and intentional non-goals are reported.

Use `../templates/final-report.md` for the adoption report.
