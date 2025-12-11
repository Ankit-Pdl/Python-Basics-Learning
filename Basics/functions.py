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



def greet(name):
  return f"Hello {name}"

def excited_wrapper(func):
  def wrapper(*args,**kwargs):
    original = func(*args,**kwargs)
    return original.upper() + "😁"
  return wrapper

greet = excited_wrapper(greet)
print(greet("Ankit"))




