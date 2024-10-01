from account_console import AccountConsole


def test_table_header(capsys):
    console = AccountConsole()
    console.print_header()

    captured = capsys.readouterr()
    print(captured.out)
    assert captured.out == "Date||Amount||Balance\n"
