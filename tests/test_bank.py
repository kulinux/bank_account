from bank import BankAccount
from unittest.mock import Mock
from freezegun import freeze_time


def test_write_header():
    console = Mock()
    bank_account = BankAccount(console)

    bank_account.print_statement()

    console.print_header.assert_called()


@freeze_time("2012-01-14")
def test_deposit():
    console = Mock()
    bank_account = BankAccount(console)
    bank_account.deposit(2500)

    bank_account.print_statement()

    console.print_line.assert_called_with("2012-01-14", 2500, 2500)
