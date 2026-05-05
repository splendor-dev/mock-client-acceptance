# Reconciliation Spec

MockLedger must produce a daily account balance report from CSV event data. Posted entries update
account balances. Held entries are excluded from balances and counted as exceptions.

## Requirements

- Report balances sorted by account name.
- Preserve exact decimal arithmetic for all amounts.
- Count held entries as exceptions.
- Keep input data in CSV so non-engineering reviewers can audit it.
- Treat this spec as the current product authority for balance behavior.

## Acceptance

The command `python -m mockledger data/accounts.csv` should print one line per account followed by
an exception count.

## Late Change

This fixture-only edit creates a second active canonical version for reconciliation practice.
