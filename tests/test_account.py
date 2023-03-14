from katabankaccount.account import Account
import datetime
import pytest


class TestAccount:
    @staticmethod
    def setup_method():
        Account.list_of_deposits_withdraws = []
        Account.current_date = datetime.date.today()

    # check if the class Account exists
    def test_account_class_exists(self):
        assert type(Account) == type
        assert Account.__name__ == "Account"

    # check if tha class Account has a balance attribute
    def test_account_attribute_balance(self):
        account = Account(100)
        assert hasattr(account, 'balance')

    # check if the Account method deposit adds amount to balance
    def test_account_method_deposit(self):
        account = Account(100)
        account.deposit(50)
        assert account.balance == 150

    def test_deposit_with_non_positive_amount(self):
        account = Account(100)
        with pytest.raises(ValueError, match="Amount must be positive"):
            account.deposit(-50)

    # check if the Account method withdraw subtracts amount from balance
    def test_account_method_withdraw(self):
        account = Account(100)
        account.withdraw(20)
        assert account.balance == 80

    def test_withdraw_with_amount_exceeding_balance(self):
        account = Account(100)
        with pytest.raises(ValueError, match="Amount exceeds available balance"):
            account.withdraw(150)

    def test_account_entry_object_with_deposit(self):
        account = Account(1000)
        account.deposit(500)
        account_entry = {"date": datetime.date.today(), "amount": 500, "balance": 1500}
        assert Account.list_of_deposits_withdraws[-1] == account_entry

    def test_account_entry_object_with_withdraw(self):
        account = Account(1000)
        account.withdraw(200)
        account_entry = {"date": datetime.date.today(), "amount": -200, "balance": 800}
        assert Account.list_of_deposits_withdraws[-1] == account_entry

    def test_list_of_deposits_withdraws_sorted_by_date(self):
        account = Account(0)
        list_of_test_entries = [
            {"date": "2023-01-12", "amount": 100, "balance": 500},
            {"date": "2022-01-13", "amount": 50, "balance": 400},
            {"date": "2023-03-12", "amount": 200, "balance": 700},
        ]

        account.sort_by_date(list_of_test_entries)

        expected_sorted_list = [
            {"date": "2023-03-12", "amount": 200, "balance": 700},
            {"date": "2023-01-12", "amount": 100, "balance": 500},
            {"date": "2022-01-13", "amount": 50, "balance": 400},
        ]
        assert list_of_test_entries == expected_sorted_list

    def test_print_statement(self, capsys):
        account = Account(1000)
        account.deposit(20)
        account.withdraw(100)
        account.print_statement()
        captured = capsys.readouterr()
        assert captured.out == f"Date || Amount || Balance\n" \
                               f"{datetime.date.today()} || 20 || 1020\n{datetime.date.today()} || -100 || 920\n"
