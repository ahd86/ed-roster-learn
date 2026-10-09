# Working style (learning project)
- Before editing, explain the plan and the why; wait for my OK.
- Keep each change small: one concern, under ~200 lines.
- After each change, explain the diff and name one concept I should understand.
- Never run git push, change .github/ or deploy/ files, or add a dependency without asking.
- Tests: pytest. Run them after every change and show me the output.
- Fictional data only. Never generate real names, emails or Monash Health identifiers.
- This is a learning project: when I ask how something works, teach; don't just do it.
- Stay in plan or manual permission mode unless I say otherwise.

   # Scope
   - This app is a configurable clinical roster for any service (ED first, then HITH and others).
   - Team-specific details (roles, periods, shift times, streams, rules) belong in config, never in code. No `if team == ...`.
   - If a service needs something config can't express, propose a general feature, not a special case.