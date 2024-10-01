import bank
import pytest


def test_negative():
    bank_account = bank.BankAccount()
    with pytest.raises(bank.WrongAmountException):
        bank_account.deposit(-1)


def test_no_error_on_positive():
    bank_account = bank.BankAccount()
    bank_account.deposit(44)


def test_print_table_header(capsys):
    bank_account = bank.BankAccount()
    bank_account.print_statement()

    captured = capsys.readouterr()
    print(captured.out)
    assert captured.out == "Date||Amount||Balance\n"
