# Production Rollback Runbook

Use this for a failed deployment, severe regression, unsafe data operation, or production incident requiring restoration.

## Required Confirmation

| Item | Required content |
| --- | --- |
| Incident or change ID | `<ID>` |
| Failed component | `<COMPONENT>` |
| Current impact | `<USERS_DATA_AND_AVAILABILITY>` |
| Last known good state | `<VERSION_CONFIG_OR_BACKUP>` |
| Rollback trigger | `<EVIDENCE>` |
| Data implications | `<NONE_COMPATIBLE_RESTORE_OR_RECONCILE>` |
| Authorized lead | `<OWNER>` |
| Verification plan | `<CHECKS>` |

## Principles

- Restore the smallest failed scope that returns the system to a safe state.
- Code rollback does not automatically reverse schema, data, configuration, cache, queue, or external side effects.
- Preserve logs and evidence needed for diagnosis while avoiding secrets and personal data.
- Prefer the documented recovery path; do not invent an irreversible shortcut under pressure.
- If the previous version cannot read data produced by the new version, stop and choose data restore or forward recovery explicitly.

## Execution Phases

1. Stabilize impact and pause further rollout or mutation.
2. Capture current versions, configuration identifiers, metrics, and relevant errors.
3. Confirm the recovery point and dependency order.
4. Execute the approved rollback through the project operations system.
5. Restore traffic or scheduled processing gradually where supported.
6. Verify technical health and critical business journeys.
7. Reconcile delayed, duplicated, or partially processed work.

## Verification

- Active versions and configuration match the recovery plan.
- Availability, errors, latency, and resource use are acceptable.
- Critical reads, writes, authentication, authorization, and workflows succeed.
- Data integrity and event processing are consistent.
- No failed component remains partially promoted.

## Closeout

Use `../templates/deploy-report.md` and record:

- Verified recovery evidence.
- Remaining risk and unverified items.
- Data reconciliation or customer communication still required.
- Compatibility compromises introduced by rollback.
- Follow-up owner and decision-record need.
