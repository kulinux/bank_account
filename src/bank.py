class BankAccount:
    def deposit(self, money):
        if money < 0:
            raise WrongAmountException()
        print("foo " + str(money))

    def print_statement(self):
        print("Date||Amount||Balance")


class WrongAmountException(Exception):
    pass
