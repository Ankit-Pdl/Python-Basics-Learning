# defining a function
# def calc(params):
#   return params;

# print(calc("Nepal"))

# def add(a,b):
#   print(f'Function is being called')
#   return a+b

# sum = add(5,6)
# print(sum)

# def states(a,b):
#   return a+b,a-b,a//b,a**b

# add,diff,div,expo = states(4,13)
# print(f"{add}, {diff}, {div}, {expo}")

# default parameter

# def greet(name="Anamika"):
#   return name;

# print(greet("Unsaaa"))




# variable number of arguments

# def add_all(*nums):
#   return sum(nums)

# val = add_all(1,2,3,4,5,6,7,8,67,9)
# print(val)

# def student_info(**details):
#   print(details)

# boyfrined = "Ankit"
# student_info(name="Yalina", age= 21,country="Nepal")
# print(type(student_info))


# docstrings

# def add(a,b):
#   """Return sum of 2 numbers"""
#   return a+b

# print(add(3,4))


# a = 5
# def test():
#   print(a)
# test()  


# Lamda Functions

# square = lambda x:x*x
# print(square(5))


# numbers = [1,2,3,4,5]
# even_Numbers = list(filter(lambda x:x%2==0,numbers))
# doubles = list(map(lambda  x:x**2,numbers))
# print(f'Power 2: {doubles}')
# print(even_Numbers)


# def add(a,b):
#  return a+b

# x = add(34,56)
# y=add(12,x)
# print(x,y)

# def outer_function(func):
#   def wrapper():
#     print("Before calling function")
#     func()
#     print("After calling function")
#   return wrapper

# def say_hello():
#   print("Hello!!!")

# wrapped = outer_function(say_hello)
# wrapped()  
  

#python decorators

# def div(a,b):
  
#   print(a/b)

# def smart_div(func):
#   def inner(a,b):
#     if b>a:
#      a,b = b,a
#     return func(a,b)
#   return inner # name should not be the same


# div = smart_div(div)
# div(2,5)

# def hello():
#   print("Hello world")


# def myDecorator(func):
#   def wrapper():
#     print('Before Function')
#     func()
#     print("After function")
#   return wrapper


# def addition(a,b):
#   return a,b

# def decAddition(func):
#   def wrapper_addition(a,b):
#     x,y = func(a,b)
#     x+=25
#     y-=12
#     print(f'sum of new {x} and {y} is: {x+y} ')
#   return wrapper_addition



# add_New = decAddition(addition)
# add_New(23,43)



# def greet(name):
#   return f"Hello {name}"

# def excited_wrapper(func):
#   def wrapper(*args,**kwargs):
#     original = func(*args,**kwargs)
#     return original.upper() + "😁"
#   return wrapper

# greet = excited_wrapper(greet)
# print(greet("Ankit"))

# logging decorator


# def log(func):
#   def wrapper(*args,**kwargs):
#     print(f"calling {func.__name__}")
#     return func(*args,**kwargs)
#   return wrapper

# @log
# def add(a,b):
#   return a+b

# print(add(4,5))

# def square(args):
#    return args**2

# print(square(5))

# def addTwoNumbers(a,b):
#   return a+b

# print(addTwoNumbers(34,45))


# def checkEvenStatus(number):
#   if number%2==0:
#     return f"{number} is even"
#   else :
#     return f"{number} is odd"
# print(checkEvenStatus(23)  )

#program that takes a list and returns a largest element

# def findLargest(userList):
#   x= userList[0]
#   for i in userList:
#     if i>x:
#       x=i
#   return x

# checkNum= [1,2,3,64,56,67,123] 

# def findLargest(lst):
#   return max(lst)

# print(findLargest(checkNum))  


# def inRever(userString):
#   return "".join(reversed(userString))

# string = "Anamika"
# print(inRever(string))



# def inRever(input):
#   reversed_output = ''
#   for i in input:
#     reversed_output =  i+ reversed_output
#   return reversed_output
  
# print(inRever("ankit"))  

# userNumber = int(input("Enter a number maximum upto 100 "))
# def calcFactorial(number):
#   fact = 1
#   if number>=0:
#     while number!= 1:
#      if number == 0 or number == 1:
#        return fact
#      fact = fact *number
#      number-=1
#   else : 
#     print("number cannot be negative ")
#   return fact


# print(f'Factorial of {userNumber} is {calcFactorial(userNumber)}')

# now a good practice
# RED = "\033[91m"
# RESET = "\033[0m"
# def calcFactorial(number):
#   if number<0:
#     print( RED + "Error: Negative number not allowed"+RESET)
#     return None
#   fact = 1
#   for i in range(2,number+1):
#     fact*=i
#   return fact

# userNumber = int(input("Enter a number: "))
# result  = calcFactorial(userNumber)

# if result is not None:
#   print(f'Factorial of {userNumber} is {result}')


# def calcFactorial(number):
#   if number<0 :
#     raise ValueError("Number cannot be negative ")
#   else:
#     fact = 1
#     for i in range(2,number+1):
#       fact*=i
#   return fact

# inp = int(input("Enter a number "))
# print(calcFactorial(inp))     


# def intro(name,age):
#   return f"My name is {name} and I am {age}"

# name = input("Enter a name:  ")
# try:
#    age = int(input("Enter your age: "))
# except ValueError:
#    print("Invalid input! Age must be a number.")
#    exit()



# print(intro(name,age))

# a better way to do the upper code :::


# def intro(name:str,age:int) ->str:
#   """Retrun a formatted introduction message"""
#   return f" My name is {name} and I am {age} years old."

# def get_valid_age()->int:
#   """Continuously prompt the user until they enter a valid integer age."""
#   while True:
#     age_input = input("Enter your age: ").strip() # strip filters the string
#     if age_input.isdigit():
#       return int(age_input)
#     print("\033[91mError: Please enter a valid number for age.\033[0m")

# def main():
#   name = input("Enter your name: ").strip().title().upper()
#   age = get_valid_age()
#   print(intro(name,age))

# if __name__ == "__main__":
#      main()


# program that takes a list of number and returns a list with only even numbers


# userIterate = int(input("Enter number of items you want : "))
# userList = []
# for i in range(0,userIterate):
#  userList.append(int(input(f"Enter item : ")) ) 

#  new_list =[x for x in userList if x%2==0]

# print(new_list)

# a better way:

# def get_even_number() :
#   """ Collects numbers from user and return a list of even numbers"""

#   try:
#     n = int(input("how many numbers would you like to enter? "))
#   except ValueError:
#     print("Please enter a valid number! ")
#     return []

#   numbers = []
#   for _ in range(n):
#     while True:
#       try:
#         num = int(input("Enter a number"))
#         numbers.append(num)
#         break
#       except ValueError:
#         print("Invalid Input. Please enter an integer.")

#   even_numbers = [num for num in numbers if num%2 ==0]
#   return even_numbers



# if __name__ == "__main__":
  
#   evens = get_even_number()
#   print("Even numbers:",evens)

# program to find the number of iterations of an element in a list
# userList = []
# n = int(input("Enter iterations: "))
# while n!=0:
#  userList.append(int(input("Enter the elements in the list ")))
#  n-=1
# def count_iteration(userList):
#     checkUser = int(input("tell me which number you want to check:"))
#     count = 0
#     for i in userList:
#        if i == checkUser:
#           count+=1
#     return count

# print(f"Your choosen number has been repeated { count_iteration(userList) } times")

# much better way:

def count_iteration(lst,number):
  """Counts how many times 'number' occurs in 'list'"""
  return lst.count(number)

userList = [int(input("Enter element: ")) for _ in range(int(input("How many numbers?")))]




if __name__ == "__main__":
  nums_to_check = int(input("Which number do you want to check?"))
  print(f"The number {nums_to_check} has been repeated {count_iteration(userList,nums_to_check)} times.")
