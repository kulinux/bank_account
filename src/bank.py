from account_console import AccountConsole


class BankAccount:
    def __init__(self, console: AccountConsole) -> None:
        self.console = console

    def deposit(self, money: float):
        if money < 0:
            raise WrongAmountException()

    def print_statement(self):
        self.console.print_header()
        # print("Date||Amount||Balance")


class WrongAmountException(Exception):
    pass
