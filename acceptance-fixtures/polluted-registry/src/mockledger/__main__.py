from __future__ import annotations

import csv
import sys
from collections import defaultdict
from decimal import Decimal
from pathlib import Path


def summarize(path: Path) -> tuple[dict[str, Decimal], int]:
    balances: dict[str, Decimal] = defaultdict(Decimal)
    exceptions = 0
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            account = row["account"]
            amount = Decimal(row["amount"])
            status = row["status"]
            if status == "posted":
                balances[account] += amount
            else:
                exceptions += 1
    return dict(sorted(balances.items())), exceptions


def main(argv: list[str] | None = None) -> int:
    args = list(sys.argv[1:] if argv is None else argv)
    if len(args) != 1:
        print("Usage: python -m mockledger <accounts.csv>")
        return 2
    balances, exceptions = summarize(Path(args[0]))
    for account, balance in balances.items():
        print(f"{account}: {balance}")
    print(f"exceptions: {exceptions}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
