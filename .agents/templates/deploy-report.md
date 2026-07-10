# Deployment And Rollback Report Template

```md
Change:
- ID: <CHANGE_ID>
- Environment: <ENVIRONMENT>
- Components: <COMPONENTS>
- Source revisions / artifacts: <IDENTIFIERS>

Approval and window:
- Authorized by: <OWNER>
- Started: <TIME>
- Completed: <TIME>

Execution:
- Strategy: <STRATEGY>
- Steps completed: <SUMMARY>
- Actual scope: <SCOPE>

Verification:
- Health checks: <RESULT_AND_EVIDENCE>
- Business smoke tests: <RESULT_AND_EVIDENCE>
- Monitoring observation: <RESULT_AND_DURATION>
- Unverified: <ITEM_AND_REASON>

Data and configuration:
- Migration or mutation: <NONE_OR_SUMMARY>
- Actual affected count: <COUNT_OR_NOT_APPLICABLE>
- Backup / recovery point: <REFERENCE>

Rollback:
- Trigger: <TRIGGER>
- Last known good: <IDENTIFIER>
- Status: <NOT_USED_READY_EXECUTED>
- Verification after rollback: <RESULT_OR_NOT_APPLICABLE>

Compatibility compromises:
- <NONE_OR_COMPROMISE_AND_REMOVAL_PLAN>

Remaining risk / follow-up:
- <RISK_OWNER_AND_NEXT_STEP>
```

Never include secret values, private keys, credentials, personal data, or unrestricted infrastructure details.
