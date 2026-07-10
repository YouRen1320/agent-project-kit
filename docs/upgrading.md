# Upgrading Agent Project Kit

Repositories created from a GitHub template do not automatically receive later template changes. Track the adopted version in `.agent-kit-version` and review each release deliberately.

## Upgrade Process

1. Read `CHANGELOG.md` from the target release.
2. Compare the target kit with the adopting repository's current agent files.
3. Classify differences as reusable core updates, project customizations, or local-only material.
4. Merge generic workflows and templates without overwriting project facts.
5. Review root routing changes manually.
6. Keep Codex and Claude skill entry points aligned.
7. Run `./scripts/validate.sh` and agent-loading smoke tests.
8. Update `.agent-kit-version` only after verification.

## Breaking Changes

A release is breaking when it changes routing semantics, required project-profile fields, skill names, safety gates, or the structure expected by validation scripts.

For a breaking upgrade, document:

- Affected files and behavior.
- Migration steps and expected manual decisions.
- Compatibility window, if any.
- Rollback to the previous kit version.
- Removal criteria for temporary bridges.

## Rollback

Restore the previously recorded agent-kit files and `.agent-kit-version`, then rerun the old validation. Preserve project-specific changes and unrelated source work.

## Future Automation

An updater may be added after the file manifest and merge semantics stabilize. It must never overwrite existing root instructions, project profiles, or local-only material without a reviewed diff and explicit approval.
