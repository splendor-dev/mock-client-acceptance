# Evaluator Checklist

Use this checklist when validating a new Splendor build against MockLedger.

1. Confirm `main` passes `splendor lint` and `splendor health`.
2. Confirm `brief --agent-context "balance reconciliation rollout"` ranks current authority above
   historical JSONL research.
3. Run the source-refresh scenario branch and verify it returns to passing diagnostics.
4. Copy the polluted-registry fixture and recover it without manual edits under
   `state/manifests/sources/`.
5. Record the Splendor version and the acceptance tag used for the run.

This checklist is deliberately human-facing and is not part of the curated source set.
