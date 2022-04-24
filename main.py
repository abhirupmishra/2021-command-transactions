from banking.bank import Bank
from banking.commands import Batch, Deposit, Transfer, Withdrawal
from banking.controller import BankController


def main() -> None:

    # create a bank
    bank = Bank()

    # create a bank controller
    controller = BankController()

    # create some accounts
    account1 = bank.create_account(name="Abhirup")
    account2 = bank.create_account(name="Google")
    account3 = bank.create_account(name="Microsoft")

    # deposit some money in my account
    controller.execute(Deposit(account=account1, amount=100000))
    controller.undo()
    controller.redo()

    # execute a batch of commands
    controller.execute(
        Batch(
            commands=[
                Deposit(account=account2, amount=100000),
                Deposit(account=account3, amount=100000),
                Transfer(from_account=account2, to_account=account1, amount=50000),
            ]
        )
    )

    # undo and redo
    controller.undo()
    controller.undo()
    controller.redo()
    controller.redo()

    # get the money out of my account
    controller.execute(Withdrawal(account=account1, amount=150000))
    print(bank)


if __name__ == "__main__":
    main()
