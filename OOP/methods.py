# factory methods
# method that creates objects for us instead of calling a constructor

# job is to manage the creation of objects

# the problem:

# The client code(main application logic)
# def plan_delivery(transport_type,destination):
#   if transport_type =="road":
#     vechile = Truck() # directly call the constructor
#   elif transport_type=="sea":
#     vechile = Ship()
#   else:
#     raise ValueError("Unknown transport type.")
    
    
#   vehicle.deliver(destination)
      
# from abc import ABC, abstractmethod
# # Product Interface
# class Transport(ABC):
#   @abstractmethod
#   def deliver(self)->str:
#     pass

# class Truck(Transport):
#   def deliver(self)->str:
#     return "Delivering by road in truck."

# class Ship(Transport):
#   def deliver(self)->str:
#     return "Delivering by sea in ship."

# class LogisticsFactory(ABC):
#   @abstractmethod
#   def create_transport(self)->Transport:
#   # The factory method  is abstract; subclass must implement it.
#    pass
#   def plan_delivery(self,destination:str):
#     transport = self.create_transport()
#     return f"Planning shipment to {destination}.\nStatus{transport.deliver()}"
  
# # Concrete Creators
# class RoadLogisticsFactory(LogisticsFactory):
#   def create_transport(self)->Truck:
#     return Truck()
  
# class SeaLogisticsFactory(LogisticsFactory):
#     def create_transport(self) -> Ship:
#         # This subclass decides to return a Ship.
#         return Ship()  
    
# # Client Code (Usage)
# road_planner = RoadLogisticsFactory()
# print(road_planner.plan_delivery("Paris"))
# # Output:
# # Planning shipment to Paris.
# # Status: Delivering by road in a Truck.
# print("-" * 20)

# sea_planner = SeaLogisticsFactory()
# print(sea_planner.plan_delivery("Dubai"))
# # Output:
# # Planning shipment to Dubai.
# # Status: Delivering by sea in a Ship.    

# # I Will comeback to this shortly, first I need to work with some important OOP concepts


      






































# class Animal:
#   def __init__(self,name):
#     self.name = name
#   @classmethod
#   def create(cls,animal_type,name):
#     if animal_type == "dog":
#       return Dog(name)   
#     elif animal_type =="cat":
#       return Cat(name)
#     else:
#       raise ValueError("Unknown animal")
    
#   def __repr__(self):
#      return f"User(name = '{self.name}'"

# class Dog(Animal):
#   def speak(self):
#     return "Bhow"
# class Cat(Animal):
#   pass

# a1 = Animal.create("dog","Max")
# # a2 = Animal.create("cat","Luna")
# print(a1.speak())