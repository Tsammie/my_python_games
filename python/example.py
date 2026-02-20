class InsufficientFundsError(Exception):
    def __init__(self, message="Insufficient funds in the account"):
        self.message = message
        super().__init__(self.message)

class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")

        self.balance += amount
        print(f"Deposited ${amount}. New balance is ${self.balance}.")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")

        if amount > self.balance:
            raise InsufficientFundsError(f"Attempted to withdraw ${amount}, but only ${self.balance} available.")

        self.balance -= amount
        print(f"Withdrew ${amount}. New balance is ${self.balance}.")    

account = BankAccount(100)
try:
    account.deposit(50)
    account.withdraw(200)  # This will raise InsufficientFundsError
except InsufficientFundsError as e:
    print(e)
except ValueError as e:
    print(e)
