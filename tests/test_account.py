from katabankaccount.account import Account
import datetime

def test_list_of_deposits_withdraws_sorted_by_date():
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

def test_print_statement(capsys):
    account = Account(1000)
    account.deposit(20)
    account.print_statement()
    captured = capsys.readouterr()
    assert captured.out == f"Date || Amount || Balance\n{datetime.date.today()} || 20 || 1020\n"

#check if the class Account exists
def test_account_class_exists():
    assert type(Account) == type
    assert Account.__name__ == "Account"

# check if tha class Account has a balance attribute
def test_account_attribute_balance():
    account = Account(100)
    assert hasattr(account, 'balance')

#check if the Account method deposit adds amount to balance
def test_account_method_deposit():
    account = Account(100)
    account.deposit(50)
    assert account.balance == 150

#check if the Account method withdraw subtracts amount from balance
def test_account_method_withdraw():
    account = Account(100)
    account.withdraw(20)
    assert account.balance == 80

def test_account_entry_object_with_deposit():
    account = Account(1000)
    account.deposit(500)
    account_entry = {"date": datetime.date.today(), "amount": 500, "balance": 1500}
    assert Account.list_of_deposits_withdraws[-1] == account_entry

def test_account_entry_object_with_withdraw():
    account = Account(1000)
    account.withdraw(200)
    account_entry = {"date": datetime.date.today(), "amount": -200, "balance": 800}
    assert Account.list_of_deposits_withdraws[-1] == account_entry

