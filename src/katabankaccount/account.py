class Account:

    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def print_statement(self, amount):
        print(f"|| {amount} || {self.balance}")
