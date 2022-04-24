import random
import string
from dataclasses import dataclass, field
from typing import Dict

from banking.account import Account


@dataclass
class Bank:
    accounts: Dict[str, Account] = field(default_factory=dict)

    def create_account(self, name: str) -> Account:
        """create a new account

        Args:
            name (str): account name

        Returns:
            account (Account): account object
        """
        number = "".join(random.choices(string.digits, k=12))
        account = Account(name, number)
        self.accounts[number] = account
        return account

    def get_account(self, account_number: str) -> Account:
        """
        get account

        Args:
            account_number (str): account number for 
                which the details are required

        Returns:
            account (Account): account object
        """
        return self.accounts[account_number]
