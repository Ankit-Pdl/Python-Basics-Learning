# aaile samma padheko kura implement gardim na khussa

from abc import ABC,abstractmethod
#Abstraction

class DiscountPolicy(ABC):
  @abstractmethod
  def apply_discount(self,amount:float)->float:
    pass

# concrete class(Disocunt)

class NoDiscount(DiscountPolicy):
  def apply_discount(self, amount):
    return amount

class StudentDiscount(DiscountPolicy):
  def apply_discount(self, amount):
    return amount *0.5 # 50% off

#some encapsulation

class Ride:
  Base_Fare =50
  Per_Km_Rate = 25

  def __init__(self,distance_km:float,discount_policy:DiscountPolicy):
    self.__distance = distance_km
    self.__discount_policy = discount_policy
  def calculate_fare(self):
    total = self.Base_Fare + (self.__distance*self.Per_Km_Rate)
    return self.__discount_policy.apply_discount(total)
  def get_distance(self):
    return self.__distance

# service controller

class RideService:
  total_earning = 0
  @classmethod
  def complete_ride(cls,ride:Ride):
    fare = ride.calculate_fare()
    cls.total_earning += fare
    return fare

# Functions User INterface ko lagi


def choose_discount():
  print("\nChoose discount type:")
  print("1. No Discount")
  print("2. Student Discount")
  choice = input("Enter choice: ")
  if choice =='2':
    return StudentDiscount()
  return NoDiscount()


def main():
  print("🚕 Welcome to Smart Ride System 🚕")
  while True:
    try:
      distance =float(input("\nEnter distance(km): "))
      discount = choose_discount()
      ride = Ride(distance,discount)
      fare = RideService.complete_ride(ride)
      print(f"Distance: {ride.get_distance()} km")
      print(f"Final Fare: Rs {fare:.2f}")
      print(f"Total Company Earnings: Rs {RideService.total_earning:.2f}")  
    except ValueError:
       print("❌ Invalid input. Try again.")
    cont = input("\nAnother ride? (y/n): ").lower()
    if cont != "y":
            print("👋 Service closed.")
            break   

# Entry Point
if __name__ =="__main__":
  main()