#   wrapping data + methods together and controlling access to the data

# tei k c++ ma padheko access modifiers, aba pythonic way ma garne ni

#problem without encapsulation

# class BankAccount:
#   def __init__(self,balance):
#     self.balance = balance
#   def __repr__(self):
#     return f"User(username = '{self.balance}')"  

# acc = BankAccount(200)
# acc.balance = -5000
# print(acc)
#note that data can be modified easily. now encapsulation solves this hai

# name ---> Public
#_name ---> Protected
# __name --> private

# using Private Variables

# class BankAccount:
#   def __init__(self,balance):
#     self.__balance = balance

# acc= BankAccount()
# print(acc.__balance)    # error because, balance is private


# class BankAccount:
#   def __init__(self,balance):
#     self.__balance = balance
#   def get_balance(self):
#     return self.__balance

# a1 = BankAccount(20000)
# print(a1.get_balance())


# class BankAccount:
#   def __init__(self,balance):
#     self.__balance = balance
#   def filer_balance(self,amount):
#     if amount>=10459:
#       self.__balance = amount
#       print(f" You satisfy the threshold value. Your balance is: {self.__balance}")
#     else:
#       print("Invalid balance")

# acc = BankAccount(20000)
# acc.filer_balance(304600)


# professional way

# class BankAccount:
#   def __init__(self,balance):
#     self.__balance = balance
#   @property
#   def balance(self):
#     return self.__balance
#   @balance.setter
#   def balance(self,amount):
#     if amount<0:
#       raise ValueError("Balance cannot be negative")
#     self.__balance = amount  

# acc = BankAccount(1000)
# print(acc.balance)
# # acc.balance =2000    

# real world example

class User:
  def __init__(self,age):
    self.age = age
  @property
  def age(self):
    return self.__age
  @age.setter
  def age(self,value):
    if value<18:
      raise ValueError("User must be 18+")
    self.__age = value


u = User(20)
u.age = 2