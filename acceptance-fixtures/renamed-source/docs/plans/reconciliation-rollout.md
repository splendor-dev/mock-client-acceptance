# Reconciliation Rollout Plan

## Goal

Ship a small, reviewable balance report before expanding MockLedger into a larger importer.

## Current Plan

1. Keep the command synchronous and file-based.
2. Use CSV as the reviewable data exchange format.
3. Add source refresh and authority-ranking acceptance checks before public v1 evaluation.
4. Revisit JSONL only after the evaluator workflow proves stable on this fixture.

## Open Questions

- Whether held entries should emit a separate exception report.
- Whether branch-specific source-refresh scenarios should become CI fixtures later.

This plan is newer than the early JSONL research note and should rank above it for current
implementation work.
