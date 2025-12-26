from abc import ABC, abstractmethod

# ------------------------------
# Abstract Base Class
# ------------------------------
class Account(ABC):
    def __init__(self, account_number, holder_name, balance=0):
        self._account_number = account_number     # protected
        self._holder_name = holder_name
        self._balance = balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposited Rs.{amount}. New Balance: Rs.{self._balance}")
        else:
            print("Invalid deposit amount")

    def get_balance(self):
        return self._balance

    @abstractmethod
    def withdraw(self, amount):
        pass   # must be implemented by child classes


# ------------------------------
# Savings Account
# ------------------------------
class SavingsAccount(Account):
    def __init__(self, account_number, holder_name, balance=0, interest_rate=0.05):
        super().__init__(account_number, holder_name, balance)
        self.interest_rate = interest_rate

    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
            print(f"Withdrawn Rs.{amount}. Balance: Rs.{self._balance}")
        else:
            print("Insufficient balance")

    def add_interest(self):
        interest = self._balance * self.interest_rate
        self._balance += interest
        print(f"Interest Added: Rs.{interest}")


# ------------------------------
# Current Account
# ------------------------------
class CurrentAccount(Account):
    def __init__(self, account_number, holder_name, balance=0, overdraft_limit=5000):
        super().__init__(account_number, holder_name, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= self._balance + self.overdraft_limit:
            self._balance -= amount
            print(f"Withdrawn Rs.{amount}. Balance: Rs.{self._balance}")
        else:
            print("Overdraft limit exceeded")


# ------------------------------
# Main Program
# ------------------------------
if __name__ == "__main__":
    savings = SavingsAccount("S101", "Ankit Poudel", 10000)
    current = CurrentAccount("C202", "Ankit Poudel", 5000)

    print("\n--- Savings Account ---")
    savings.deposit(2000)
    savings.withdraw(3000)
    savings.add_interest()

    print("\n--- Current Account ---")
    current.withdraw(8000)
    current.deposit(1000)

    print("\nFinal Balances:")
    print("Savings:", savings.get_balance())
    print("Current:", current.get_balance())
