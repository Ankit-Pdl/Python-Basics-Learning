from abc import ABC,abstractmethod
#Abstraction
class BankAccount(ABC):
  def __init__(self,holder_name:str,balance:float):
    self.holder_name = holder_name
    self._balance = balance # protected variable

  @abstractmethod
  def calculate_interest(self):
    pass
  def deposit(self,amount):
    if amount<=1000:
      raise ValueError("Deposit must be at least 1000 Rupees")
    self._balance+=amount
  def withdraw(self,amount:float):
    if amount>self._balance:
      raise ValueError("Insufficient balance")
    elif amount<=500:
      raise ValueError("Withdrawl amount must be at least 500 Rupees")
    self._balance -=amount

  def get_balance(self):
    return self._balance

# account types haru ni rakhdim na yesso


class SavingsAccount(BankAccount):
  INTEREST_RATE =0.04

  def calculate_interest(self):
    return self._balance*self.INTEREST_RATE
  
class CurrentAccount(BankAccount):
  INTEREST_RATE = 0.01
  def calculate_interest(self):
    return self._balance*self.INTEREST_RATE

class Bank:
  total_account = 0    

  @classmethod
  def open_account(cls):
    name = input("Enter account holder name: ")
    balance = float(input("Enter initial balance: "))
    print("\n Account Type:")
    print("1. Savings")
    print("2. Current")
    choice = input("Choose type: ")
    if choice =="1":
      account = SavingsAccount(name,balance)
    else:
      account = CurrentAccount(name,balance)
    cls.total_account +=1
    return account

#UI

def main():
  print("🏛️Welcome to APY NOVA Bank System:🏛️")
  account = Bank.open_account()
  while True:
    print("\n1. Deposit")  
    print("2.. Withdraw")  
    print("3. Check Balance")  
    print("4. Calculate Interest")  
    print("5. Exit")
    choice = input("Choose Option: ")
    try:
      if choice =="1":
        amount = float(input("Amount to deposit:"))
        account.deposit(amount)
        print("Deposit Succesfull")
      elif choice =="2":
        amount = float(input("Amount to withdraw: "))
        account.withdraw(amount)
        print("Withdraw Succesfull")
      elif choice =="3":
        print(f"Current Balance: Rs {account.get_balance():.2f}")
      elif choice =="4":
        interest = account.calculate_interest()
        print(f"Interest Earned: Rs {interest:.2f}")
      elif choice =="5":
         print("👋 Thank you for banking with us")
         break
      else:
        print("Invalid choice")

    except ValueError as e:
      print("❌ Error:", e)
      

if __name__ == "__main__":
    main()      
              
     
      
