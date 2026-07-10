# Module Delivery Workflow

Use this workflow for business features, API or data contracts, state models, directory architecture, cross-component changes, and deployment-sensitive work.

## Hard Gate

Do not implement a major or breaking change until the review below is complete and the user has explicitly approved the open decisions and completion criteria.

## 1. Read Project Context

Read the relevant files in `../project/` and inspect the actual repositories. Confirm:

- Applicable agent instructions and module ownership.
- Current branches, remotes, and unrelated working-tree changes.
- Authoritative build, test, and release commands.
- Environment and data boundaries.
- External systems or tools needed for verification.

Do not replace repository evidence with placeholders or assumptions.

## 2. Define Goal And Scope

| Item | Content |
| --- | --- |
| Goal | `<USER_OR_BUSINESS_OUTCOME>` |
| Affected users or roles | `<USERS_OR_ROLES>` |
| Affected components | `<REPOSITORIES_SERVICES_CLIENTS_OR_JOBS>` |
| Affected data or contracts | `<DATA_API_EVENT_CONFIG_OR_NONE>` |
| Constraints | `<CONSTRAINTS>` |
| Explicit non-goals | `<NON_GOALS>` |

State the ideal target state before discussing legacy constraints or phased migration.

## 3. Investigate Current State

Trace entry points, implementation, consumers, persisted data, permissions, configuration, and delivery boundaries.

| Area | Current behavior | Required change | Evidence | Risk |
| --- | --- | --- | --- | --- |
| `<AREA>` | `<CURRENT>` | `<CHANGE>` | `<FILES_TESTS_LOGS_OR_DOCS>` | `<RISK>` |

For shared contracts, list every producer and consumer. For status changes, document allowed transitions, guards, side effects, and invalid transitions.

## 4. Compare Viable Options

When multiple reasonable approaches exist, compare two or three options.

| Option | Implementation cost | Migration cost | Risk | Rollback difficulty | Long-term maintainability |
| --- | --- | --- | --- | --- | --- |
| `<OPTION_A>` | `<COST>` | `<COST>` | `<RISK>` | `<DIFFICULTY>` | `<ASSESSMENT>` |
| `<OPTION_B>` | `<COST>` | `<COST>` | `<RISK>` | `<DIFFICULTY>` | `<ASSESSMENT>` |
| `<OPTION_C_OR_NONE>` | `<COST>` | `<COST>` | `<RISK>` | `<DIFFICULTY>` | `<ASSESSMENT>` |

The recommendation must state:

- Why it best meets the agreed goal.
- Whether it is the ideal target or an intentional phase.
- Breaking impact and affected consumers.
- Compatibility behavior and its removal criteria.
- Migration and rollback approach.

## 5. Confirm Decisions

| Decision | Recommendation | User decision |
| --- | --- | --- |
| `<DECISION>` | `<RECOMMENDATION>` | `<APPROVED_REJECTED_OR_PENDING>` |

Wait for explicit confirmation when a decision changes architecture, data models, API contracts, directory structure, cross-component behavior, production data, or compatibility policy.

## 6. Plan Data, Migration, And Rollback

If persisted data, storage, cache, configuration, or external state changes, also use `../runbooks/database-change.md` where applicable.

| Object | Environment | Change | Backup | Expected impact | Verification | Rollback |
| --- | --- | --- | --- | --- | --- | --- |
| `<OBJECT>` | `<ENVIRONMENT>` | `<CHANGE>` | `<BACKUP>` | `<ROWS_FILES_KEYS_OR_USERS>` | `<EVIDENCE>` | `<ROLLBACK>` |

If rollback is impossible or lossy, say so before implementation and define a forward-recovery plan.

## 7. Define Completion Criteria

Before editing, agree on observable completion criteria:

- Required behavior and error cases.
- Affected producers and consumers updated.
- Authorization and server-side validation preserved.
- Historical data and migration outcome verified.
- Required static checks, tests, builds, and smoke scenarios pass.
- Deployment or publication status is explicit.
- Compatibility compromises and removal plan are documented.
- Unverified items and intentional non-goals are documented.

## 8. Implement Within Scope

- Preserve user-owned and unrelated changes.
- Keep edits limited to the approved scope.
- Update producers before or with consumers according to the agreed rollout plan.
- Add concise intent-level comments only where behavior, mappings, data sources, or side effects are non-obvious.
- Surface newly discovered decision points instead of silently choosing a materially different design.

## 9. Review And Verify

Perform, as applicable:

- Diff and conflict-marker checks.
- Static analysis, unit tests, integration tests, and builds from `../project/commands.md`.
- Positive, negative, permission, status-transition, concurrency, and historical-data scenarios.
- Contract checks for every consumer.
- Visual or device verification for user-facing behavior.
- Rollback review or rehearsal proportionate to risk.

Separate verified evidence from inference and untested claims.

## 10. Deliver

Use `../templates/final-report.md`. Report each repository independently and include deployment, data, compatibility, and non-goal status.

## Pause Conditions

Pause and return to review if:

- A new component or consumer is discovered.
- Scope or completion criteria materially change.
- Legacy data changes the design.
- Authorization or state semantics are unclear.
- A destructive or production mutation becomes necessary.
- A merge conflict requires a non-obvious product or architecture decision.
- Verification contradicts the approved design.
