from account_console import AccountConsole
from bank import BankAccount, WrongAmountException
from freezegun import freeze_time
import pytest


def bank() -> BankAccount:
    return BankAccount(AccountConsole())


def test_negative():
    bank_account = bank()
    with pytest.raises(WrongAmountException):
        bank_account.deposit(-1)


def test_no_error_on_positive():
    bank_account = bank()
    bank_account.deposit(44)


def test_print_table_header(capsys):
    bank_account = bank()
    bank_account.print_statement()

    captured = capsys.readouterr()
    assert captured.out == "Date||Amount||Balance\n"


@freeze_time("2012-01-14")
def test_deposit(capsys):
    bank_account = bank()
    bank_account.deposit(2500)
    bank_account.print_statement()

    captured = capsys.readouterr()
    assert captured.out == "Date||Amount||Balance\n" "2012-01-14||2500||2500\n"
