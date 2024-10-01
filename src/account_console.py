class AccountConsole:
    def print_header(self):
        print("Date||Amount||Balance")

    def print_line(self, date: str, amount: int, total: int):
        print(date + "||" + str(amount) + "||" + str(total))
