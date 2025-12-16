# SHipping system with encapsulation and Abstract class

# from abc import ABC, abstractmethod
# class ShippingMethod(ABC):
#   _tracking_counter = 1
#   def __init__(self):
#     self._base_cost = 0
#     self._per_kg  = 0 # protected value ho haii
#   @abstractmethod
#   def calculate_cost(self,order_weight:float):
#     pass
#   def track_order(self):
#     order_number = ShippingMethod._tracking_counter 
#     ShippingMethod._tracking_counter +=1
#     return f"Order number {order_number}."

# # concrete classes:
# class StandardShipping(ShippingMethod):
#   def __init__(self):
#     self._base_cost = 5
#     self._per_kg = 2


#   def calculate_cost(self, order_weight):
#     if order_weight<0:
#       raise ValueError("order weight cannot be negative")
#     total_cost = self._base_cost+(self._per_kg*order_weight)
#     total_cost = int(total_cost) if total_cost.is_integer() else round(total_cost,2)
#     return f"Shipping cost :${total_cost}."
  

# class ExpressShipping(ShippingMethod):
#     def __init__(self):
#         super().__init__()
#         self._base_cost = 10
#         self._per_kg_cost = 2

#     def calculate_cost(self, order_weight):
#         if order_weight < 0:
#             raise ValueError("Order weight cannot be negative")
        
#         total_cost = self._base_cost + self._per_kg_cost * order_weight
#         total_cost = int(total_cost) if total_cost.is_integer() else round(total_cost, 2)
#         return f"Shipping Cost: ${total_cost}"

# def checkout(shipping:ShippingMethod,order_weight:float):
#    print(shipping.track_order())
#    print(shipping.calculate_cost(order_weight)) 
#    print("\n") 
   

# checkout(StandardShipping(),30,"Hex_234")
# checkout(ExpressShipping(),3.5,"RGB-987")   


# question number 2:

# 🎯 Scenario: E-commerce Discount System

# An e-commerce website applies different discount strategies to orders.

# Available discounts:

# No Discount

# Seasonal Discount (10%)

# Premium User Discount (20%)


from abc import ABC, abstractmethod

class DiscountPolicy(ABC):
    def __init__(self):
        self._rate = 0  # protected

    @abstractmethod
    def apply_discount(self, amount: float):
        pass

    def _format_amount(self, value: float):
        return int(value) if value.is_integer() else value

    def display_policy(self):
        return "Generic Discount Policy"


class NoDiscount(DiscountPolicy):
    def __init__(self):
        super().__init__()
        self._rate = 0

    def apply_discount(self, amount):
        amount = float(amount)
        return self._format_amount(amount)

    def display_policy(self):
        return "No Discount"


class SeasonalDiscount(DiscountPolicy):
    def __init__(self):
        super().__init__()
        self._rate = 0.10  # 10%

    def apply_discount(self, amount):
        amount = float(amount)
        final_price = amount - (amount * self._rate)
        return self._format_amount(final_price)

    def display_policy(self):
        return "Seasonal Discount (10%)"


def checkout(shopping: DiscountPolicy, amount):
    print(shopping.display_policy())
    print("Final Price:", shopping.apply_discount(amount))
    print("-" * 29)


checkout(NoDiscount(), 500)
checkout(SeasonalDiscount(), 1000)
checkout(SeasonalDiscount(), 199.99)


         