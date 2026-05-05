# ADR-0001: Keep CSV as the First Review Format

## Status

Accepted

## Context

MockLedger needs to be inspectable by product, finance, and agent evaluators. CSV is less expressive
than JSONL but easier for non-engineering reviewers to inspect during acceptance runs.

## Decision

Use CSV for the v0.1 account event input. Do not introduce JSONL until there is a demonstrated
need for nested event metadata.

## Consequences

- Splendor source refresh scenarios can use small text diffs that are easy to review.
- Research notes arguing for JSONL remain useful historical context, but they are not current
authority.
