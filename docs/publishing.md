# Publishing The Kit

[中文清单](publishing.zh-CN.md)

Use this checklist when turning a local copy into a public GitHub template. Complete the maintainer-specific items before changing repository visibility to public.

## 1. Confirm The Public Boundary

- Review every tracked file rather than only the current diff.
- Run `./scripts/validate.sh` and `./scripts/test.sh`.
- Run a dedicated secret scanner approved by the maintainer.
- Run `EXTRA_DENY_PATTERN='<PRIVATE_IDENTIFIERS>' ./scripts/check-public-safety.sh` with a private pattern covering names, domains, repository identifiers, and infrastructure terms from the source project.
- Confirm examples are fictional and no commit history was copied from a private project.

The built-in checks are guardrails, not proof that a repository contains no secrets or personal data.

## 2. Set Maintainer-Owned Information

- Copy `.github/CODEOWNERS.example` to `.github/CODEOWNERS` and replace every example owner with a real GitHub user or team.
- Choose a monitored private channel for conduct reports, document it in `CODE_OF_CONDUCT.md`, and remove its `PUBLICATION-BLOCKER` comment.
- Enable GitHub private vulnerability reporting before relying on the route described in `SECURITY.md`. If that feature will not be enabled, replace the route with a monitored private security contact. Remove the blocker comment only after the chosen route is real.
- Review the supported-version promise in `SECURITY.md` and the release policy in `CHANGELOG.md`.

Do not invent an owner or publish an unmonitored contact address merely to satisfy the checklist.

## 3. Configure The Repository

- Create the GitHub repository as private first and configure it as `origin`.
- Use `main` as the default branch or update the workflow and documentation consistently.
- Enable the repository's Template repository setting.
- Enable secret scanning and push protection where the hosting plan supports them.
- Protect the default branch and require the validation workflow and maintainer review for trusted instruction paths.
- Restrict GitHub Actions permissions to read-only by default and review each future exception.
- Disable unused repository features so contributors have one clear support path.

## 4. Create The First Release

1. Inspect `git status` and the complete tracked-file list.
2. Confirm the commit author identity is suitable for a public repository.
3. Create the initial commit only after the owner and reporting routes are configured.
4. Push to the private repository and confirm the validation workflow succeeds.
5. Run `python3 scripts/validate-publish-readiness.py`; it must pass before public visibility is enabled.
6. Test “Use this template” with a temporary repository.
7. Fill `.agents/project/` in that temporary repository and verify both agent entry points.
8. Recheck the GitHub settings, then make the repository public.
9. Tag `v0.1.0` and publish release notes based on `CHANGELOG.md`.

## 5. Record The Verification

Keep a short release record containing:

- Validation commands that passed.
- Secret and privacy review performed.
- Template-generation test result.
- Codex and Claude Code loading test result.
- Known limitations and intentional non-goals.
- The maintainer who approved publication.

Do not mark the release complete when any required item is only assumed.
