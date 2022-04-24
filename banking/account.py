"""
Account
"""

from dataclasses import dataclass

from errors import InsufficientBalance


@dataclass
class Account:
    """
    Account
    """

    name: str
    number: str
    balance: int = 0

    def deposit(self, amount: int) -> None:
        """
        deposit to account

        Args:
            amount (int): amount that needs to be deposited
        """
        self.balance += amount

    def withdraw(self, amount: int) -> None:
        if amount > self.balance:
            raise InsufficientBalance()
        self.balance -= amount
