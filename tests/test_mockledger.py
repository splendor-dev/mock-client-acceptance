from decimal import Decimal
from pathlib import Path

from mockledger.__main__ import summarize


def test_summarize_accounts_excludes_held_entries() -> None:
    balances, exceptions = summarize(Path("data/accounts.csv"))

    assert balances == {
        "cash": Decimal("1207.75"),
        "deferred": Decimal("88.00"),
        "receivables": Decimal("310.50"),
    }
    assert exceptions == 2
