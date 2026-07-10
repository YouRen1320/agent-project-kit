# Adopting The Kit In An Existing Project

Existing projects may already contain valuable instructions, skills, hooks, and local conventions. Adoption is a merge, not an overwrite.

Invoke `$project-bootstrap` in Codex or `/project-bootstrap` in Claude Code to follow this merge workflow with repository evidence.

## 1. Inventory Existing Guidance

Identify:

- Root and nested `AGENTS.md` files.
- `CLAUDE.md`, `.claude/rules/`, and `.claude/skills/`.
- Existing review, deployment, database, and release documentation.
- CI checks and protected paths.
- Local-only files that must remain ignored.

Back up the current guidance before changing it.

## 2. Choose The Authoritative Source

For every duplicated rule, decide which file owns it. Prefer:

- Root files for durable routing and universal constraints.
- `.agents/project/` for project facts.
- Workflows and runbooks for multi-step procedures.
- Skills for reusable, task-triggered guidance.
- Private systems for credentials and executable operational targets.

## 3. Merge In Safe Order

1. Add `.agents/templates/` and generic references.
2. Add only the workflows and runbooks the project needs.
3. Fill `.agents/project/` from verified evidence.
4. Merge `AGENTS.md` manually.
5. Import shared guidance from `CLAUDE.md` instead of duplicating it.
6. Merge skills by name and remove competing definitions.
7. Add validation scripts and CI after checking local tooling requirements.

Do not replace an established branch, release, or deployment policy with the kit defaults. The project profile must describe the actual policy.

## 4. Resolve Conflicts

When rules disagree:

- Prefer explicit project and user requirements over generic examples.
- Keep the safer gate while the conflict is unresolved.
- Record architecture or policy choices in a decision record.
- Remove obsolete guidance rather than leaving silent compatibility behavior.

## 5. Verify Adoption

- Run `./scripts/validate-project-profile.sh`, then `./scripts/validate.sh`.
- Confirm agent loading from the repository root and an important subdirectory.
- Test routing with sanitized requests for code review, API change, UI change, data mutation, and deployment planning.
- Confirm read-only requests do not trigger edits and high-risk operations pause for approval.

## Rollback

If adoption causes confusion, restore the backed-up instruction files and remove only the newly added kit paths. Do not revert unrelated project work.
