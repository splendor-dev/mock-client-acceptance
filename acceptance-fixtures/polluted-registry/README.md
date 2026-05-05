# Polluted Registry Fixture

This directory is a copied Splendor workspace with intentionally bad curated source state. It is
not the healthy repository root.

## Seeded Problems

- `.mypy_cache/cache.py` is registered as a source even though cache files should be ignored.
- `.codex/session.log` is registered as a source even though local agent scratch files should be
  ignored.
- `docs/specs/reconciliation.md` has two active canonical source versions.

## Recovery Exercise

From this directory:

```bash
splendor lint
splendor source forget --matching ".mypy_cache/**"
splendor source forget --matching ".mypy_cache/**" --apply
splendor source forget --matching ".codex/**"
splendor source forget --matching ".codex/**" --apply
splendor source reconcile docs/specs/reconciliation.md
splendor source reconcile docs/specs/reconciliation.md --current src-3a08737053123b78bdaa39da41a5b91ecb944cd566def926774e9f2d0b6aa0e9 --apply
splendor lint
splendor health
```

The final diagnostics should pass without manual deletion under `state/manifests/sources/`.
