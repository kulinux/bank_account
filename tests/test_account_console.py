from account_console import AccountConsole


def test_table_header(capsys):
    console = AccountConsole()
    console.print_header()

    captured = capsys.readouterr()
    print(captured.out)
    assert captured.out == "Date||Amount||Balance\n"


def test_print_line(capsys):
    console = AccountConsole()
    console.print_line("date", 4, 5)

    captured = capsys.readouterr()
    print(captured.out)
    assert captured.out == "date||4||5\n"
