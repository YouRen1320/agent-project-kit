# Ownership And Escalation

Use `../templates/module-registry.md` to add detailed module records. Every operationally important module should have a named owner or an explicit unowned status.

## Ownership Registry

| Module ID | Module | Primary owner | Backup owner | Repositories or paths | Consumers | Operational contact |
| --- | --- | --- | --- | --- | --- | --- |
| `<MODULE_ID>` | `<MODULE_NAME>` | `<PRIMARY_OWNER>` | `<BACKUP_OWNER>` | `<LOCATIONS>` | `<CONSUMERS>` | `<CONTACT_OR_PROCESS>` |

## Responsibility Rules

- Business rules, authorization, state transitions, and persisted-data correctness belong to the producing domain.
- Client-specific presentation defects belong to that client, while shared contract defects require producer and consumer review.
- Infrastructure modules own transport and availability; originating domains still own the correctness of emitted business events.
- Database schema and migration ownership must be explicit for every persisted domain.
- An unowned critical module is a documented risk and blocks high-risk changes until an approver is identified.

## Review Requirements

| Change | Required reviewers or approvers |
| --- | --- |
| Shared API, event, or schema | Producer owner and every affected consumer owner |
| Authorization or sensitive data | `<SECURITY_OR_DATA_OWNER>` |
| Production migration | `<DATABASE_OWNER>` and `<SERVICE_OWNER>` |
| Deployment process | `<OPERATIONS_OWNER>` |
| Breaking removal | Owners of all known consumers |

## Escalation

When ownership is unclear:

1. Stop irreversible or production-impacting work.
2. Record the affected module, evidence, and decision needed.
3. Escalate to `<ESCALATION_OWNER_OR_PROCESS>`.
4. Resume only after responsibility and approval are explicit.
