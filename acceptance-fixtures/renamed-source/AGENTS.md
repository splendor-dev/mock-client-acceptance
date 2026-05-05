# MockLedger Agent Rules

## Source of Truth

- Treat this repository as a public acceptance target, not as a production service.
- Keep `main` healthy for first-time evaluators.
- Keep intentionally broken Splendor state in scenario branches or `acceptance-fixtures/`.
- Prefer deterministic file changes over hidden local state.

## Commands

- Run the CLI: `python -m mockledger data/accounts.csv`
- Run Splendor diagnostics: `splendor lint` and `splendor health`
- Agent handoff: `splendor brief --agent-context "balance reconciliation rollout"`
- Ranked next actions: `splendor suggest-next "reconciliation contradictions"`

## Change Rules

- Human-authored authority docs live under `docs/`.
- Splendor-generated wiki and state should be reviewed before publishing.
- Do not commit local caches, virtual environments, or agent scratch directories.
- When modeling failure scenarios, keep healthy `main` usable and document the recovery command.
