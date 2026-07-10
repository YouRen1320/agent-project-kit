# Git And Release Workflow

Use this for commit, push, merge, pull request, tag, or release work.

## Gates

- Never discard, overwrite, or reformat unrelated user changes.
- Confirm each repository, current branch, upstream, target branch, and remote divergence.
- Confirm required checks and project merge policy before publishing.
- Do not assume direct pushes to the default branch are allowed.
- Destructive history changes, force pushes, branch deletion, and release replacement require explicit approval and a recovery plan.

## Pre-Publication Checklist

For each repository:

1. Confirm changed files are within the agreed scope.
2. Identify unrelated or untracked files and leave them untouched.
3. Refresh remote state before comparing branches.
4. Confirm local work is not unintentionally behind or diverged.
5. Run required checks from `../project/commands.md`.
6. Review the final diff for secrets, generated artifacts, debug code, and accidental edits.
7. Prepare a focused commit message and release or pull-request summary.

## Publication Decision

| Item | Value |
| --- | --- |
| Repository | `<REPOSITORY>` |
| Source branch | `<SOURCE_BRANCH>` |
| Target branch | `<TARGET_BRANCH>` |
| Publication method | `<PULL_REQUEST_DIRECT_PUSH_TAG_OR_OTHER>` |
| Required approvals | `<APPROVALS>` |
| Required checks | `<CHECKS>` |
| Rollback or revert method | `<METHOD>` |

## Multi-Repository Delivery

- Publish in the approved dependency order.
- Record every repository commit and verification result.
- Do not report a coordinated release complete while a required consumer remains unpublished or unverified.
- If a partial release is permitted, document the compatibility window and completion owner.

## Final Report

Include repository, branch, commit, push status, pull-request or merge status, tag or release status, verification, deployment dependency, and unrelated changes left in place.
