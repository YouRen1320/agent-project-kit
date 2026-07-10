# Deployment Runbook Template

This is an abstract safety template. Project-specific targets, credentials, hostnames, commands, and executable deployment details belong in an approved private operations system, not in this shared document.

## Hard Gate

Do not deploy until the authorized owner confirms:

- Target environment and component scope.
- Source revision and immutable artifact identity.
- Dependency and migration order.
- Required approvals and maintenance window.
- Health checks and business smoke tests.
- Last known good version and rollback trigger.
- User impact and communication plan.

## Deployment Plan

| Item | Required content |
| --- | --- |
| Change identifier | `<CHANGE_OR_RELEASE_ID>` |
| Environment | `<TARGET_ENVIRONMENT>` |
| Components | `<COMPONENTS>` |
| Source revisions | `<COMMITS_OR_TAGS>` |
| Artifacts | `<IMMUTABLE_ARTIFACT_IDENTIFIERS>` |
| Dependencies | `<DATABASE_CONFIG_QUEUE_CLIENT_OR_NONE>` |
| Strategy | `<ROLLING_BLUE_GREEN_CANARY_OR_OTHER>` |
| Approval | `<APPROVER_AND_EVIDENCE>` |
| Verification | `<HEALTH_AND_BUSINESS_CHECKS>` |
| Rollback | `<LAST_KNOWN_GOOD_AND_PROCESS_REFERENCE>` |

## Pre-Deployment Checks

- Repository and artifact verification passed.
- No unresolved high-severity findings block release.
- Configuration is present without exposing secret values.
- Capacity, compatibility, and migration prerequisites are satisfied.
- Monitoring and alerting are active.
- Rollback assets and access are available.
- Independently deployed consumers are compatible with the rollout order.

## Safe Execution Phases

1. Record the starting state and active versions.
2. Apply approved prerequisites in dependency order.
3. Release to the smallest safe scope supported by the platform.
4. Run health checks before increasing exposure.
5. Run agreed business smoke tests.
6. Observe metrics and logs for the agreed period.
7. Complete rollout only if success criteria remain satisfied.

Do not improvise a new target, deployment method, data mutation, or compatibility behavior during execution. Pause for approval if the plan no longer matches reality.

## Verification Matrix

| Check | Expected result | Evidence source | Result |
| --- | --- | --- | --- |
| Availability | `<EXPECTED>` | `<METRIC_OR_HEALTH_SOURCE>` | `<PASS_FAIL>` |
| Critical user journey | `<EXPECTED>` | `<SMOKE_TEST_SOURCE>` | `<PASS_FAIL>` |
| Error and latency budget | `<EXPECTED>` | `<OBSERVABILITY_SOURCE>` | `<PASS_FAIL>` |
| Data and contract compatibility | `<EXPECTED>` | `<VALIDATION_SOURCE>` | `<PASS_FAIL>` |

## Rollback

Rollback immediately when `<ROLLBACK_TRIGGERS>` occurs, unless an authorized incident lead approves a safer alternative.

Confirm during rollback:

- The correct last known good artifacts and configuration.
- Whether data written by the new version is backward-compatible.
- Restore order for dependent components.
- Health and business verification after traffic returns.
- Remaining reconciliation or user communication.

## Reporting

Use `../templates/deploy-report.md`. Never include credentials, secret values, private keys, personal data, or unrestricted infrastructure details.
