# Project Commands

Replace every placeholder with commands verified from repository configuration. Do not invent commands from framework conventions.

## Command Matrix

| Component | Setup | Lint or static check | Unit tests | Integration tests | Build | Local run |
| --- | --- | --- | --- | --- | --- | --- |
| `<COMPONENT_ID>` | `<SETUP_COMMAND>` | `<LINT_COMMAND>` | `<UNIT_TEST_COMMAND>` | `<INTEGRATION_TEST_COMMAND>` | `<BUILD_COMMAND>` | `<RUN_COMMAND>` |

## Targeted Verification

| Change type | Minimum command or check | Expected evidence |
| --- | --- | --- |
| Documentation only | `<DOC_CHECK_COMMAND>` | No broken references or invalid formatting |
| Backend or service | `<BACKEND_CHECK_COMMAND>` | Compile and relevant tests pass |
| Frontend or client | `<FRONTEND_CHECK_COMMAND>` | Static check, build, and affected UI smoke pass |
| Shared contract | `<CONTRACT_CHECK_COMMAND>` | Producer and all consumers validate |
| Database migration | `<MIGRATION_CHECK_COMMAND>` | Validate, dry run where supported, and rollback review |

## Command Safety

- Read the command source before running it, especially scripts that mutate data or publish artifacts.
- Confirm the target environment for any command that can reach external systems.
- Use the project's declared package manager and lockfile.
- Do not install or upgrade dependencies outside the agreed change scope.
- Do not suppress errors broadly or report a build as passed when output was incomplete.
- Capture the exact command and result for failed or high-risk verification.

## Unavailable Commands

If a required check cannot run, report:

- Command: `<COMMAND>`
- Blocker: `<BLOCKER>`
- Substitute evidence: `<EVIDENCE_OR_NONE>`
- Residual risk: `<RISK>`
