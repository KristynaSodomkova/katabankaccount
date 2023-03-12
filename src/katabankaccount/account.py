import datetime

class Account:
    list_of_deposits_withdraws = []
    def __init__(self, balance):
        self.balance = balance

    @staticmethod
    def day_stamp():
        day = datetime.date.today()
        return day

    def deposit(self, amount):
        day = self.day_stamp()
        self.balance += amount
        account_entry = {"date": day, "amount": amount, "balance": self.balance}
        Account.list_of_deposits_withdraws.append(account_entry)

    def withdraw(self, amount):
        day = self.day_stamp()
        self.balance -= amount


"""
    def print_statement(self):
        print(f"|| Amount || Balance\n|| {self.amount} || {self.balance}")
"""
