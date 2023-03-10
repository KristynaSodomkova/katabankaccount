from katabankaccount.account import Account
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
    account.print_statement()
    captured = capfd.readouterr()
    assert captured.out == "|| 20 || 120\n"