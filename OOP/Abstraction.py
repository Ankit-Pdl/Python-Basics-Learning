# # showing only essential informations

# # abstract class cannot be instantiated

# from abc import ABC, abstractmethod #abc == abstract base classes

# class Shape(ABC):
#   """Defines the abstract concept of a geometric shape"""

#   @abstractmethod
#   def calculate_area(self)->float:
#     """All shapes must know how to calculate their area"""
#     pass
#   def describe(self):
#     return f"This is a {self.__class__.__name__}."
  
# # Concrete Implementations  
  
# class Circle(Shape):
#   def __init__(self,radius):
#     self.radius = radius
#   def calculate_area(self):
#     return 3.14*(self.radius**2)
  
# class Rectangle(Shape):
#   def __init__(self,width,height):
#     self.width = width
#     self.height = height
#   def calculate_area(self):
#     return self.width*self.height    
  
#   # Client interactions

# def print_area(shape:Shape):
#   """Client code that only relies on the abstract 'Shape' interface.
#   It does not know if it's a Circle or a Rectangle.
#   """  
#   print(f"{shape.describe()} Its area is: {shape.calculate_area():.2f} square units")

# circle = Circle(5)
# rectangle = Rectangle(3,4)
# print_area(circle)
# print_area(rectangle)  
# 
# jumping into the basics
# from abc import ABC,abstractmethod
# class demo(ABC):
#   @abstractmethod
#   def method1(self):
#     print("abstract method")

# obj = demo()    

# from abc import ABC,abstractmethod
# class Vehicle(ABC):
#   @abstractmethod
#   def start_engine(self):
#     pass
#   def print_info(self):
#     print(f"This is a general purpose vehicle.")

# class Car(Vehicle):
#   def start_engine(self):
#     print("Car engine is starting: chick chick")

# class Bike(Vehicle):
#   def start_engine(self):
#     print("Motorcycle started:")

# my_car = Car()
# my_bike = Bike()
# my_car.start_engine()

# my_car.print_info()

# #why abstract class? 
# # common interface for a set of classes



from abc import ABC ,abstractmethod

#   class PaymentMethod(ABC):
#   @abstractmethod
#   def pay(self,amount:float):
#     pass
#   def receipt(self, amount:float):
#     return f"Payment of ${amount:.2f} completed!"
  
# class CreditCard(PaymentMethod):
#   def pay(self,amount:float):
#     return f"Paid ${amount:.2f} using credit card"
# class esewa(PaymentMethod):
#   def pay(self,amount:float):
#     return f"Paid ${amount:.2f} using esewa"
# class khalti(PaymentMethod):
#   def pay(self,amount:float):
#     return f"Paid ${amount:.2f} using khalti"
  
# def checkout(payment:PaymentMethod,amount:float):
#   print(payment.pay(amount))
#   print(payment.receipt(amount))  

# checkout(CreditCard(),100)
# checkout(esewa(),50)
# checkout(khalti(),43) 

class ShippingMethods(ABC):
  @abstractmethod
  def calculate_cost(self,order_weight:float)->float:
    pass
  def track_order(self,order_id:str):
    return f"Tracking order {order_id}. "
  
class StandardShipping(ShippingMethods):
  def calculate_cost(self, order_weight):
     total_cost = 10+(order_weight*9)
     if total_cost.is_integer():
       total_cost = int(total_cost)
     else:
       total_cost = round(total_cost,2)
     return f"Shipping Cost: ${total_cost:.2f}"  


class ExpressShipping(ShippingMethods):
  def calculate_cost(self, order_weight):
     total_cost = 10+(order_weight*2)
     if total_cost.is_integer():
       total_cost = int(total_cost)
     else:
       total_cost = round(total_cost,2)  
       
     return f"Shipping Cost: ${total_cost}"  
class DroneShipping(ShippingMethods):
  def calculate_cost(self , order_weight):
     total_cost = 20+(order_weight*3)
     if total_cost.is_integer():
       total_cost = int(total_cost)
     else:
       total_cost = round(total_cost,2)
     return f"Shipping Cost: ${total_cost}"  
  
class RocketShipping(ShippingMethods):
  def calculate_cost(self, order_weight):
    if order_weight ==0:
      return " You don't have to pay anything for zero weight order"
    total_cost = 10+(order_weight*7)
    if total_cost.is_integer():
       total_cost = int(total_cost)
    else:
       total_cost = round(total_cost,2)
    return f"Shipping Cost : ${total_cost}"  
  
def checkout(reference:ShippingMethods,order_weight:float,order_id:str):
  print(reference.track_order(order_id))
  print(reference.calculate_cost(order_weight))
    


checkout(ExpressShipping(),0,"A")
checkout(DroneShipping(),34.6,"B")
checkout(StandardShipping(),6,"C")
checkout(RocketShipping(),12.2,"Panties")
