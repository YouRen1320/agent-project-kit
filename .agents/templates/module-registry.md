# Module Registry Template

Use this to define stable responsibility boundaries and locate all consumers before changes.

## Module Index

| Module ID | Name | Business boundary | Primary owner | Backup owner | Producers | Consumers | Criticality |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `<MODULE_ID>` | `<MODULE_NAME>` | `<BOUNDARY>` | `<OWNER>` | `<BACKUP>` | `<PRODUCERS>` | `<CONSUMERS>` | `<LEVEL>` |

## Module Detail

### `<MODULE_ID>` — `<MODULE_NAME>`

| Item | Content |
| --- | --- |
| Goal | `<USER_OR_BUSINESS_OUTCOME>` |
| In scope | `<CAPABILITIES>` |
| Out of scope | `<NON_GOALS>` |
| Entry points | `<PAGES_ROUTES_COMMANDS_OR_EVENTS>` |
| Source locations | `<REPOSITORIES_AND_PATHS>` |
| API, events, or schemas | `<CONTRACTS>` |
| Persisted data | `<TABLES_COLLECTIONS_OBJECTS_OR_NONE>` |
| Authorization boundary | `<AUTHORIZATION_RULE>` |
| State model | `<STATES_AND_TRANSITIONS_OR_NONE>` |
| External dependencies | `<DEPENDENCIES_OR_NONE>` |
| Required verification | `<SCENARIOS_AND_COMMANDS>` |
| Common failure ownership | `<TRIAGE_RULE>` |

## Maintenance Rules

- Update the registry with the same change that moves a responsibility or contract.
- Do not assign the same business rule to multiple modules without naming the authoritative producer.
- Mark unknown ownership explicitly; do not use a guessed person or team.
- Keep implementation paths current and remove retired consumers after their migration completes.
