from katabankaccount.account import Account
import datetime
def test_account_class_exists():
    assert type(Account) == type
    assert Account.__name__ == "Account"

def test_account_attribute_balance():
    account = Account(100)
    assert hasattr(account, 'balance')

def test_account_method_deposit():
    account = Account(100)
    account.deposit(50)
    assert account.balance == 150

def test_account_method_withdraw():
    account = Account(100)
    account.withdraw(20)
    assert account.balance == 80

def test_print_statement(capfd):
    account = Account(100)
    account.deposit(20)
    account.print_statement(20)
    captured = capfd.readouterr()
    assert captured.out == "|| Amount || Balance\n|| 20 || 120\n"

def test_withdraw_returns_current_day(monkeypatch):
    mock_date = datetime.date(2023, 3, 10)

    monkeypatch.setattr(datetime.date, 'today', lambda:mock_date)

    account = Account(1000)

    withdrawal_day = account.withdraw(500)

    assert withdrawal_day == mock_date