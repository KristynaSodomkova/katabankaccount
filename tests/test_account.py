from katabankaccount.account import Account
def test_account_class_exists():
    assert type(Account) == type
    assert Account.__name__ == "Account"
