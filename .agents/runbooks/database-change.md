# Database And Persisted-Data Runbook

Use this for schema migrations, data repair, cache or storage cleanup, configuration mutation, and any operation that changes persisted state.

## Hard Gate

Do not run a write until the user or authorized owner confirms:

- Exact environment and target object.
- Reason and approved scope.
- Backup or recovery point.
- Expected affected rows, objects, files, or keys.
- Verification evidence.
- Rollback or forward-recovery plan.

## Change Plan

| Item | Required content |
| --- | --- |
| Target | `<TABLES_COLLECTIONS_KEYS_OBJECTS_OR_CONFIG>` |
| Environment | `<ENVIRONMENT>` |
| Reason | `<REASON>` |
| Preconditions | `<PRECONDITIONS>` |
| Backup | `<METHOD_AND_LOCATION_REFERENCE>` |
| Execution | `<MIGRATION_SCRIPT_OR_APPROVED_OPERATION>` |
| Expected impact | `<EXPECTED_COUNT_AND_USER_IMPACT>` |
| Verification | `<QUERY_LOG_METRIC_OR_FUNCTIONAL_CHECK>` |
| Rollback | `<RESTORE_REVERSE_MIGRATION_OR_FORWARD_RECOVERY>` |
| Owner and approval | `<OWNER_AND_APPROVAL>` |

## Design Rules

- Prefer reviewed, versioned migrations over manual schema edits.
- Separate schema evolution from one-time data repair where practical.
- Favor additive, backward-compatible rollout only when it serves an explicit migration plan.
- Do not keep temporary compatibility fields, triggers, or dual writes without removal criteria and an owner.
- Design large backfills for batching, idempotency, restartability, monitoring, and load control.
- Define behavior for old application versions during deployment and rollback.
- If a change cannot be reversed safely, require a tested forward-recovery path and explicit risk acceptance.

## Execution Rules

- Reconfirm the target immediately before mutation.
- Verify the backup exists and is restorable to the degree required by risk.
- Record start time, operator, change identifier, and actual affected count.
- Stop on unexpected counts, constraint failures, timeouts, replication lag, or application errors.
- Do not hide errors through broad output suppression.
- Keep evidence free of secrets and personal data.

## Verification

Verify both technical and business outcomes:

- Schema or object state is exactly as planned.
- Actual affected count matches the approved range.
- Constraints, indexes, permissions, and application reads/writes behave correctly.
- Historical and newly created data follow the intended rules.
- Error rate, latency, queue depth, and resource use remain acceptable where relevant.

## Rollback

Rollback criteria: `<TRIGGERS>`

Rollback must identify:

- Code-version compatibility.
- Data written after the change began.
- Restore ordering and expected downtime.
- Verification after restore.
- Residual data loss or reconciliation work.

Use `../templates/deploy-report.md` to record the outcome.
