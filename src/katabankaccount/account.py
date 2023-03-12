import datetime

def day_stamp():
    day = datetime.date.today()
    return day

list_of_deposits_withdraws = []

class Account:

    def __init__(self, balance):
        self.balance = balance
        self.deposit_amount = 0
        self.withdraw_amount = 0
        self.statement = {}

    def deposit(self, amount):
        day = day_stamp()
        self.balance += amount
        self.deposit_amount = amount
        account_entry = {}
        list_of_deposits_withdraws.append(account_entry)
        return day, amount

    def withdraw(self, amount):
        day = day_stamp()
        self.balance -= amount
        self.withdraw_amount = amount
        return day, amount

    def print_statement(self):
        print(f"|| Amount || Balance\n|| {self.deposit_amount} || {self.balance}")

