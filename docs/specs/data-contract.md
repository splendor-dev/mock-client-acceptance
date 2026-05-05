# Data Contract Note

MockLedger's account event file is intentionally small and reviewable. Each row must include:

- `account`: account bucket to report
- `amount`: decimal amount as text
- `status`: `posted` or `held`
- `note`: human-readable review context

This note is not yet a curated Splendor source. It exists to give evaluator PR history a realistic
documentation-only change that should not alter the healthy baseline workspace.
