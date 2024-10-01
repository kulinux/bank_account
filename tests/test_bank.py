from bank import BankAccount
from unittest.mock import Mock


def test_write_header(mocker):
    console = Mock()
    bank_account = BankAccount(console)

    bank_account.print_statement()

    console.print_header.assert_called()
