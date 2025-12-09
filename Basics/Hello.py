

# data types:

# variables = temporary storage for data
# name = 'Ankit\n'
# age = 21
# is_student = True
# height = '5\'6'
# print(name, age, is_student, height)

# Dynamic Typing:
 
 # no need to dynamically declare data types

# x= 5
# x= 'hello'

# print(x)
# types in pythons

# messages = "Hello, World!"# string
# pi = 3.14 # float
# is_Valid = False # boolean
# count = 42 # integer
# print(type(messages))
# print(type(pi))
# print(type(is_Valid))
# print(type(count))

# # tuples = immutable collection of items
# coordinates = (10.0,20.0)
# print(type(coordinates))

# my_list = [1,2,3,4,5] # mutable collection of items
# print(type(my_list))

# my_dict = {'name': 'Ankit', 'age': 21} # key-value pairs
# print(type(my_dict))


#complext type in python

# z= 2+ 4j;
# print(type(z))

# z2 = complex(2,4)
# print(type(z2))

# #using f string print

# name = 'Ankit'
# age =21
# print(f'my name is {name} and my age is {age}')

# Sequence Types
# Lists, Tuples, and Ranges

# list
# my_list = [1,2,3,4,5]
# my_list[0] = 10
# print(my_list)

#tuple

# my_tuple = (1,2,3,4,5)
# my_tuple[0] = 10 # This will raise an error since tuples are immutable

# print(my_tuple)


#range
# my_range = range(1,10)
# for num in my_range:
#   print('anamika')  

#none type
email=None
name = None
print(type(name))

if email is None:
    print("Email is not provided.")
else:  
    print("Email is provided.")