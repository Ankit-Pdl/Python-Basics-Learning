# child uses the properties and methods of another class(parent)

# class Parent():
#   pass
# class Child(Parent):
#   pass

# class Animal:
#   def speak(self):
#     print("This animal speaks")

# class Dog(Animal):
#   pass

# c1 = Dog()
# c1.speak()

# constructor with inheritance

# class Person:
#   def __init__(self,name):
#     self.name = name

#   def show(self):
#     print("Name: ",self.name)

# class Student(Person):
#   def __init__(self,name,roll):
#     super().__init__(name)
#     self.roll = roll
#   def display(self):
#         print("Name:", self.name)
#         print("Roll:", self.roll)      

# s = Student("Ankit",31)
# s.display()

# class Parent:
#    def __init__(self):
#       print("Parent constructor called")

# class Child(Parent):
#    def __init__(self):
#       super().__init__()
#       print("Child constructor called")
# c = Child()


# types of inheritance

# single inheritance

# class A:
#   pass
# class B(A):
#   pass


# multilevel

class Grandparent:
  def __init__(self):
    self.family_name = "Poudel"

class Parent(Grandparent):
  pass
class Child(Parent):
  pass

c = Child()
print(c.family_name)
