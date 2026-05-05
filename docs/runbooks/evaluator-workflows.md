# Evaluator Workflows

## Healthy Baseline

```bash
splendor lint
splendor health
splendor brief --agent-context "balance reconciliation rollout"
splendor suggest-next "reconciliation contradictions"
```

The healthy baseline should pass diagnostics and rank the reconciliation spec, rollout plan,
ADR-0001, and held-entry policy above the stale JSONL research note.

## Source Refresh Scenario

Use branch `scenario/source-refresh-lifecycle` to review a changed curated source:

```bash
git switch scenario/source-refresh-lifecycle
splendor source freshness
splendor workspace refresh --changed --ingest --prune-superseded --update-topic-refs --rebuild-index
splendor lint
splendor health
```

## Polluted Registry Scenario

Copy `acceptance-fixtures/polluted-registry/` to a temporary working directory and follow its
README. The fixture includes intentionally bad source manifests for ignored cache and local-agent
paths, plus duplicate active versions for one curated source.

## Renamed Source Scenario

Copy `acceptance-fixtures/renamed-source/` to a temporary working directory and follow its README.
The fixture models a curated source whose file moved without broad repo discovery.
