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

# real but simple class

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

# here __init__ is a constructor.

class Dog:
  def __init__(self,name):
    self.name = name
  def intro(self):
    print(f'{self.name} is a bhusiya from sanothimi')  

d1 = Dog("Mena")

d1.intro()




