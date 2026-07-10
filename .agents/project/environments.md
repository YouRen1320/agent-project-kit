# Environment Profile

This file describes environment boundaries without storing credentials or secrets.

## Environment Matrix

| Environment | Purpose | Data class | Configuration source | Access owner | Deployment method | Rollback source |
| --- | --- | --- | --- | --- | --- | --- |
| `<ENVIRONMENT_NAME>` | `<PURPOSE>` | `<SYNTHETIC_TEST_PRODUCTION_OR_OTHER>` | `<CONFIG_SOURCE_NAME>` | `<OWNER>` | `<METHOD>` | `<LAST_KNOWN_GOOD_SOURCE>` |

## Endpoint And Dependency Inventory

Use non-secret identifiers only.

| Environment | Dependency | Logical endpoint | Mutation allowed? | Notes |
| --- | --- | --- | --- | --- |
| `<ENVIRONMENT_NAME>` | `<DATABASE_CACHE_QUEUE_STORAGE_OR_API>` | `https://service.example.com` | `<YES_NO_WITH_APPROVAL>` | `<NOTES>` |

## Safety Rules

- Confirm the environment immediately before any build, migration, data repair, deployment, or rollback command.
- Treat production and production-derived data as sensitive even when credentials are not present.
- Never copy production credentials or data into documentation, examples, logs, tickets, or test fixtures.
- Keep secret values in an approved secret manager or environment injection mechanism.
- Use separate credentials, storage, caches, queues, and databases across environments where practical.
- Do not infer that a configuration named `dev` points to a non-production resource; verify the actual target.
- Production mutations require explicit approval, recorded backup, verification, and rollback.

## Promotion Policy

| From | To | Required approval | Required evidence | Compatibility requirement |
| --- | --- | --- | --- | --- |
| `<SOURCE_ENV>` | `<TARGET_ENV>` | `<APPROVER>` | `<TEST_AND_BUILD_EVIDENCE>` | `<REQUIREMENT>` |

## Local-Only Notes

Machine-specific paths, test accounts, and access instructions belong in an ignored local file or approved secret system, not in this shared profile.
