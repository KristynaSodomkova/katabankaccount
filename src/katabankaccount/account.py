import datetime

class Account:

    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        day = datetime.date.today()
        self.balance += amount
        return day

    def withdraw(self, amount):
        day = datetime.date.today()
        self.balance -= amount
        return day

    def print_statement(self, amount):
        print(f"|| Amount || Balance\n|| {amount} || {self.balance}")

