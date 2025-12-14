# class Person:
#   def say_hello(self):
#     print("Hello")

# p1=Person()
# p1.say_hello()    

# class Person:
#   def say_name(self):
#     print(self.name)

# p1 = Person()
# p1.name="Anamika"
# p1.say_name()

# name = 'Anamika'
# class Dog:
  
#   def bark(self):
#     print(self.name);


# d1 = Dog()
# d1.name ="Max"
# d2  = Dog()
# d2.name = "Alex"
# d1.bark()
# d2.bark()

# # real but simple class

# class Person:
#   def __init__(self,name,age):
#     print("constructor called")
#     self.name = name
#     self.age = age
#   def introduce(self):
#     print(f"My name is {self.name} and I am {self.age} years old")

# p1 = Person("Ankit",21)
# p2=Person("Yunisha",20)

# p1.introduce()
# p2.introduce()

# # here __init__ is a constructor.

# class Dog:
#   def __init__(self,name):
#     self.name = name
#   def intro(self):
#     print(f'{self.name} is a bhusiya from sanothimi')  

# d1 = Dog("Mena")

# d1.intro()




# class Dog:
#   def __init__(self,name):
#     self.name = name

# d1 = Dog("Max")
# print(d1.name)


# class Dog:
#   species = 'Canine'
#   def __init__(self,name,age): # constructor
   
#     self.name = name
#     self.age = age

#   def bark(self):
#     print(f"{self.name} is barking")

# my_dog = Dog("Mena",12)
# print(f"My dog's name is {my_dog.name}")
# print(f"{my_dog.name} is a {my_dog.species}")
# my_dog.bark()

# real world example

# class Employee:
#   min_salary = 300000

#   def __init__(self,name,salary):
#    self.name = name
#    self.salary = salary

#   def get_raise(self):
#     self.salary *= 1.05
#   @classmethod
#   def from_string(cls,emp_str):
#     name, salary = emp_str.split("-")
#     return cls(name,int(salary))
#   @staticmethod
#   def is_workday(day):
#     return day.weekday()!= 5 and day.weekday()!=6



# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

#     @classmethod
#     def from_string(cls, data):
#         name, marks = data.split(",")
#         return cls(name, int(marks))
# s1 = Student("Ankit", 85)
# # s2 = Student.from_string("Yunisha,90")

# class Student:
#   college = "TU"
#   @classmethod
#   def __init__(cls):
#     print(cls.college)

#  Student.show_college()    


# class Student:
#   def __init__(self,name,marks):
#     self.name = name
#     self.marks = marks
#   @classmethod
#   def from_string(cls,data):
#     name,marks = data.split(",")
#     return cls(name,int(marks))

# s = Student.from_string("Ankit,54")    
# print(f"{s.name}  {s.marks}")



# managing Shared state safely

# class Employee:
#   count = 0

#   def __init__(self,name):
#     self.name = name
#     type(self).count+=1
#   @classmethod
#   def total_employees(cls):
#     return cls.count 
#   def print_count(self):
#     print(self.count)

# e1 = Employee("Ankit")
# e2 = Employee("Ankita")
# e3 = Employee("Unsaaaa")

# print(Employee.total_employees())
# e4 = Employee("Unsaaaa")

# class User:
#   total_users= 0
#   def __init__(self,username:str)->None:
#     self.username:str = username
#     type(self).total_users +=1
#   @classmethod
#   def get_total_users(cls):
#     return cls.total_users
#   def display(self):
#     print(self.username) 
#   def __repr__(self):
#     return f"User(username = '{self.username}')"  

# u1 = User("Ankit")
# u2 = User("Yunishaa")
# # u1.display()
# # u2.display()
# print(u1)
# print(User.get_total_users())
# practice problem on classmethod
# class User:
#   total_users = 0
#   usernames = []

#   def __init__(self,username):
#     self.username = username
#     User.usernames.append(username)
#     User.total_users+=1
#   def __del__(self):
#     """Called when object is deleted."""
#     type(self).total_users -=1  
#     if self.username in type(self).usernames:
#       type(self).usernames.remove(self.username)


#   @classmethod
#   def get_total_users(cls):
#     return cls.total_users   
  
#   def display(self):
#     print(self.username)
#   @classmethod  
#   def get_all_usernames(cls):
#     return(cls.usernames.copy())
#   def __repr__(self):
#     return f"User(username = '{self.username}')"

# u1 = User("Ankit")
# u2 = User("Nepal")
# print(User.get_total_users())
# print(User.get_all_usernames())
# del u2
# print(User.get_total_users())
# print(User.get_all_usernames())
    
# now learning static method

# class MathUtils:
#   @staticmethod
#   def add(a,b):
#     return a+b
# print(MathUtils.add(5,7))

# class User:
#   def __init__(self,username):
#     self.username = username
#   @staticmethod
#   def is_valid_username(name):
#     return name.isalpha() and len(name)>=4


 


# class User:
#   def __init__(self,username):
#     self.username = username
    
#   @staticmethod
#   def is_valid_username(name):
#     if( name.isalpha() and len(name)>=3):
#       return True
#     else:
#       raise ValueError("Use a valid username")
    
# print(User.is_valid_username("Ankit"))
# print(User.is_valid_username("AP")) 


# class User:
#   total_users= 0
#   def __init__(self,username):
#     if not User.is_valid_username(username):
#       raise ValueError("Invalid Username")
#     self.username = username
#     type(self).total_users+=1
#   @staticmethod
#   def is_valid_username(name):
#     return name.isalpha() and len(name)>=3
#   @classmethod
#   def get_total_users(cls):
#     return cls.total_users
#   def display(self):
#     print(self.username)


# u1 =User("Ankit")
# u1.display()
# print(User.get_total_users())
# # u2= User("Ap")

























