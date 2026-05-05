# Research Note: JSONL Import Path

An early prototype suggested switching MockLedger to JSONL because nested import metadata could be
stored alongside each event. This note predates the CSV-first decision and did not account for
finance reviewer needs.

## Claim

JSONL should become the primary input format before the first evaluator trial.

## Caveat

This research conflicts with ADR-0001 and the current rollout plan. It is intentionally retained so
Splendor agent handoff can surface a real contradiction and rank current authority above stale but
token-similar material.
