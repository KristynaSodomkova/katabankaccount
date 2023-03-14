import datetime


class Account:
    list_of_deposits_withdraws = []

    def __init__(self, balance):
        self.balance = balance

    @staticmethod
    def day_stamp():
        day = datetime.date.today()
        return day

    @staticmethod
    def create_account_entry(day, amount, balance):
        account_entry = {"date": day, "amount": amount, "balance": balance}
        return account_entry

    @staticmethod
    def sort_by_date(list_to_sort):
        return list_to_sort.sort(key=lambda x: x['date'], reverse=True)

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        day = self.day_stamp()
        self.balance += amount
        account_entry = self.create_account_entry(day, amount, self.balance)
        Account.list_of_deposits_withdraws.append(account_entry)

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        if amount > self.balance:
            raise ValueError("Amount exceeds available balance")
        day = self.day_stamp()
        self.balance -= amount
        amount = amount*(-1)
        account_entry = self.create_account_entry(day, amount, self.balance)
        Account.list_of_deposits_withdraws.append(account_entry)

    @staticmethod
    def print_statement():
        Account.sort_by_date(Account.list_of_deposits_withdraws)
        print("Date || Amount || Balance")
        for entry in Account.list_of_deposits_withdraws:
            print(f"{entry['date']} || {entry['amount']} || {entry['balance']}")
