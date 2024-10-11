from datetime import datetime
from account_console import AccountConsole


class BankAccount:
    def __init__(self, console: AccountConsole, initial: int = 0) -> None:
        self.console = console
        self.initial: int = initial
        self.money: int | None = None

    def deposit(self, money: int):
        if money < 0:
            raise WrongAmountException()
        self.money = money
        self.initial = money

    def withdraw(self, money: int):
        if money < 0:
            raise WrongAmountException()
        self.money = -money
        self.initial = self.initial - money

    def print_statement(self):
        self.console.print_header()
        if isinstance(self.money, int):
            self.console.print_line(
                str(datetime.today().strftime("%Y-%m-%d")), self.money, self.initial
            )


class WrongAmountException(Exception):
    pass
