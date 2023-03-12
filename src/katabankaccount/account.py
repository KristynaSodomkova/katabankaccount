import datetime

def day_stamp():
    day = datetime.date.today()
    return day

class Account:
    list_of_deposits_withdraws = []
    def __init__(self, balance):
        self.balance = balance
        self.deposit_amount = 0
        self.withdraw_amount = 0
        self.statement = {}

    def deposit(self, amount):
        day = day_stamp()
        self.balance += amount
        self.deposit_amount = amount
        account_entry = {"date": day, "amount": amount, "balance": self.balance}
        Account.list_of_deposits_withdraws.append(account_entry)
        return amount

    def withdraw(self, amount):
        day = day_stamp()
        self.balance -= amount
        self.withdraw_amount = amount
        return amount

    def print_statement(self):
        print(f"|| Amount || Balance\n|| {self.deposit_amount} || {self.balance}")

