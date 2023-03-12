from katabankaccount.account import Account
import datetime
import pytest #to be able to use pytest fixtures

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

#check the outcome of print_statement method from Account class
def test_print_statement(capfd):
    account = Account(100)
    account.deposit(20)
    account.print_statement()
    captured = capfd.readouterr()
    assert captured.out == "|| Amount || Balance\n|| 20 || 120\n"

#check if withdraw method from Accont returns the current day
@pytest.fixture
def test_withdraw_returns_current_day(monkeypatch):
    mock_date = datetime.date(2023, 3, 10)
    monkeypatch.setattr(datetime.date, 'today', lambda:mock_date)
    account = Account(1000)
    withdrawal_day = account.withdraw(500)
    assert withdrawal_day == mock_date

def test_account_entry_object():
    account = Account(1000)
    account.deposit(500)
    account_entry = {"date": datetime.date.today(), "amount": 200, "balance": 2300}
    assert Account.list_of_deposits_withdraws[-1] == account_entry
