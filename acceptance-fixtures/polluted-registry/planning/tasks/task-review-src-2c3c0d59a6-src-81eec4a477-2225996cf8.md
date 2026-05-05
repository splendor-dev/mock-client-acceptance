---
schema_version: '1'
kind: task
task_id: task-review-src-2c3c0d59a6-src-81eec4a477-2225996cf8
title: 'Review contradiction: ADR 0001 csv first vs 2026 03 jsonl import note'
status: todo
priority: high
milestone_refs: []
decision_refs: []
question_refs: []
owner: null
created_at: '2026-05-05T20:59:46+00:00'
updated_at: '2026-05-05T20:59:46+00:00'
depends_on: []
source_refs:
- src-2c3c0d59a65c250a511cd498e18356d06306eaf934db52a9e3fccf439577a78a
- src-81eec4a477d0fab3ec40de13760ac3cf5300328ed68c460106ee3a7a2c4a7465
page_refs:
- wiki/sources/src-2c3c0d59a65c250a511cd498e18356d06306eaf934db52a9e3fccf439577a78a.md
- wiki/sources/src-81eec4a477d0fab3ec40de13760ac3cf5300328ed68c460106ee3a7a2c4a7465.md
run_refs:
- state/runs/run-src-81eec4a477d0fab3ec40de13760ac3cf5300328ed68c460106ee3a7a2c4a7465-20260505T205944310033Z.json
---

## Contradiction

Research Note: JSONL Import Path. An early prototype suggested switching MockLedger to JSONL because nested import metadata could be stored alongside each event. This note predates the CSV-first decision and did not account for finance reviewer needs. registered from `docs/research/2026-03-jsonl-import-note.md`.

## Evidence

- `src-81eec4a477d0fab3ec40de13760ac3cf5300328ed68c460106ee3a7a2c4a7465`: ADR-0001: Keep CSV as the First Review Format. Accepted registered from `docs/decisions/ADR-0001-csv-first.md`.
- `src-2c3c0d59a65c250a511cd498e18356d06306eaf934db52a9e3fccf439577a78a`: Research Note: JSONL Import Path. An early prototype suggested switching MockLedger to JSONL because nested import metadata could be stored alongside each event. This note predates the CSV-first decision and did not account for finance reviewer needs.

## Linked Pages

- [ADR 0001 csv first](../../wiki/sources/src-81eec4a477d0fab3ec40de13760ac3cf5300328ed68c460106ee3a7a2c4a7465.md) (`src-81eec4a477d0fab3ec40de13760ac3cf5300328ed68c460106ee3a7a2c4a7465`)
- [2026 03 jsonl import note](../../wiki/sources/src-2c3c0d59a65c250a511cd498e18356d06306eaf934db52a9e3fccf439577a78a.md) (`src-2c3c0d59a65c250a511cd498e18356d06306eaf934db52a9e3fccf439577a78a`)

## Notes

