# MockLedger Acceptance Repository

MockLedger is a deliberately small CLI/data project used as Splendor's public mock client
acceptance target. It is realistic enough for evaluator workflows without containing private
client material.

The default branch is intentionally healthy. Broken source registries and repair exercises live in
scenario branches or under `acceptance-fixtures/`.

## Project

MockLedger reads a CSV of account events and reports account balances plus exception counts. The
project is small on purpose, but its documentation has the same authority shape as a real client
repository:

- product specs in `docs/specs/`
- implementation plans in `docs/plans/`
- decision records in `docs/decisions/`
- contradictory research notes in `docs/research/`
- operator runbooks in `docs/runbooks/`

## Local CLI

```bash
python -m mockledger data/accounts.csv
```

## Splendor Acceptance Commands

Run these from the repository root after installing Splendor:

```bash
splendor lint
splendor health
splendor brief --agent-context "balance reconciliation rollout"
splendor suggest-next "reconciliation contradictions"
```

The expected baseline is that `splendor lint` and `splendor health` pass on `main`.

## Acceptance Scenarios

- Healthy first run: clone `main`, run the commands above, and inspect the current authority docs.
- Source refresh: use the `scenario/source-refresh-lifecycle` branch to exercise changed curated
  sources, superseded summaries, topic-ref migration, and lint/health recovery.
- Polluted registry: use `acceptance-fixtures/polluted-registry/` as a copied workspace fixture
  and recover it with the documented `splendor source forget` and `splendor source reconcile`
  commands in that fixture's README.
- Moved source repair: use `acceptance-fixtures/renamed-source/` to practice path repair without
  broad rediscovery.

This repository is linked from Splendor issue
https://github.com/splendor-dev/splendor/issues/114.
