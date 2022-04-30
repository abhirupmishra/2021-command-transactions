"""
Transaction
"""
# pylint: disable=missing-function-docstring
from abc import ABC


class Transaction(ABC):
    """
    Abstract transaction class
    """
    currency: str = "USD"
    currency_symbol: str = "$"

    def execute(self) -> None:
        raise NotImplementedError()

    def undo(self) -> None:
        raise NotImplementedError()

    def redo(self) -> None:
        raise NotImplementedError()
