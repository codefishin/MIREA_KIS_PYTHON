class BankAccount:
    def __init__(self, account_number=None, balance=0):
        if account_number is None:
            account_number = '1234'
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Внести меньше 0 нельзя")
        self.balance += amount
        return f"{amount} средств успешно зачислены на счет {self.account_number}"

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Вывести меньше 0 нельзя")
        if amount > self.balance:
            raise Exception("Не хватает средств")
        self.balance -= amount
        return f"{amount} средств успешно сняты с счета {self.account_number}"

    def check_balance(self):
        return f"Баланс счета {self.account_number}: {self.balance}"
