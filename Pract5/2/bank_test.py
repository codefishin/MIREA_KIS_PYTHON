import bank as BankAcc
import pytest

@pytest.fixture()
def empty_bank():
    return BankAcc.BankAccount()

@pytest.fixture()
def bank():
    return BankAcc.BankAccount('1234', 10)


def test_empty_bank(empty_bank):
    with pytest.raises(Exception):
        empty_bank.withdraw(100)
    with pytest.raises(ValueError):
        empty_bank.withdraw(-100)
    with pytest.raises(ValueError):
        empty_bank.deposit(-100)
    assert empty_bank.check_balance() == "Баланс счета 1234: 0"


def test_withdraw(bank):
    with pytest.raises(Exception):
        bank.withdraw(100)
    with pytest.raises(ValueError):
        bank.withdraw(-100)
    assert bank.withdraw(10) == '10 средств успешно сняты с счета 1234'

def test_deposit(bank):
    assert bank.deposit(10) == '10 средств успешно зачислены на счет 1234'
    with pytest.raises(ValueError):
        bank.deposit(-10)

def test_check(bank):
    assert bank.check_balance() == "Баланс счета 1234: 10"
    assert bank.deposit(10) == '10 средств успешно зачислены на счет 1234'
    assert bank.check_balance() == "Баланс счета 1234: 20"
    assert bank.withdraw(10) == '10 средств успешно сняты с счета 1234'
    assert bank.check_balance() == "Баланс счета 1234: 10"


# 2
def user_input():
    account = input('Введите название аккаунта')
    amount = input('Введите ваш баланс')
    return BankAcc.BankAccount(account, amount)

def test_user(monkeypatch):
    inputs = [2, 100]
    def my_input(x):
        return inputs.pop()

    monkeypatch.setattr('builtins.input', my_input)
    assert user_input().check_balance() == "Баланс счета 100: 2"
