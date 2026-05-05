# Renamed Source Fixture

This directory is a copied Splendor workspace for practicing source path repair. It is not the
healthy repository root.

## Recovery Exercise

From this directory:

```bash
mkdir -p docs/product
cp docs/specs/reconciliation.md docs/product/reconciliation.md
splendor source update-path docs/specs/reconciliation.md docs/product/reconciliation.md --force
splendor ingest --pending
splendor workspace refresh --update-topic-refs --rebuild-index
splendor lint
splendor health
```

The expected result is that the active source path moves to `docs/product/reconciliation.md`
without broad repo discovery. The original file is retained in this fixture so historical run
provenance remains auditable while the active source path is repaired.
