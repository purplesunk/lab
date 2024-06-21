class BankAccount:
    def __init__(self, account_number, initial_balance):
        self.__account_number = account_number
        self.__balance = initial_balance

    def get_account_number(self):
        return self._BankAccount__account_number

    def get_balance(self):
        return self._BankAccount__balance

    def deposit(self, amount):
        if amount < 1:
            raise ValueError("Cannot deposit zero or negative funds")

        self._BankAccount__balance += amount

    def withdraw(self, amount):
        if amount < 1:
            raise ValueError("Cannot withdraw zero or negative funds")

        if amount > self._BankAccount__balance:
            raise ValueError("Insufficient funds")

        self._BankAccount__balance -= amount
