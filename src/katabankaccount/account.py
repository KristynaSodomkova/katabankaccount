import datetime

def day_stamp():
    day = datetime.date.today()
    return day

class Account:

    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        day = day_stamp()
        self.balance += amount
        return day

    def withdraw(self, amount):
        day = day_stamp()
        self.balance -= amount
        return day

    def print_statement(self, amount):
        print(f"|| Amount || Balance\n|| {amount} || {self.balance}")

