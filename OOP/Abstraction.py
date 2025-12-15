# showing only essential informations

# abstract class cannot be instantiated

from abc import ABC, abstractmethod

class Shape(ABC):
  """Defines the abstract concept of a geometric shape"""

  @abstractmethod
  def calculate_area(self)->float:
    """All shapes must know how to calculate their area"""
    pass
  def describe(self):
    return f"This is a {self.__class__.__name__}."
  
# Concrete Implementations  
  
class Circle(Shape):
  def __init__(self,radius):
    self.radius = radius
  def calculate_area(self):
    return 3.14*(self.radius**2)
  
class Rectangle(Shape):
  def __init__(self,width,height):
    self.width = width
    self.height = height
  def calculate_area(self):
    return self.width*self.height    
  
  # Client interactions

def print_area(shape:Shape):
  """Client code that only relies on the abstract 'Shape' interface.
  It does not know if it's a Circle or a Rectangle.
  """  
  print(f"{shape.describe()} Its area is: {shape.calculate_area():.2f} square units")

circle = Circle(5)
rectangle = Rectangle(3,4)
print_area(circle)
print_area(rectangle)      