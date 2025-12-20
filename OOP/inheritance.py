def section(name):
  print(f"\n=== {name} ===")

# Single Inheritance
class Animal:
  def speak(self):
    return "generic sound"

class Dog(Animal):
  def speak(self):
    return "woof"

# Multilevel Inheritance
class Vehicle:
  def move(self):
    return "moving"

class Car(Vehicle):
  def move(self):
    return "car moving"

class ElectricCar(Car):
  def charge(self):
    return "charging"

# Multiple Inheritance
class Flyer:
  def fly(self):
    return "flying"

class Swimmer:
  def swim(self):
    return "swimming"

class Duck(Flyer, Swimmer):
  def sound(self):
    return "quack"

# Hierarchical Inheritance
class Shape:
  def area(self):
    raise NotImplementedError

class Circle(Shape):
  def __init__(self, r):
    self.r = r
  def area(self):
    return 3.14159 * self.r * self.r

class Rectangle(Shape):
  def __init__(self, w, h):
    self.w = w
    self.h = h
  def area(self):
    return self.w * self.h

class Triangle(Shape):
  def __init__(self, b, h):
    self.b = b
    self.h = h
  def area(self):
    return 0.5 * self.b * self.h

# Hybrid (Diamond) Inheritance demonstrating MRO
class A:
  def who(self):
    return "A"

class B(A):
  def who(self):
    return "B->" + super().who()

class C(A):
  def who(self):
    return "C->" + super().who()

class D(B, C):
  def who(self):
    return "D->" + super().who()


def main():
  section("Single Inheritance")
  d = Dog()
  print("Dog speaks:", d.speak())
  print("Dog is Animal:", isinstance(d, Animal))

  section("Multilevel Inheritance")
  e = ElectricCar()
  print("ElectricCar move:", e.move())
  print("ElectricCar:", e.charge())

  section("Multiple Inheritance")
  duck = Duck()
  print("Duck fly:", duck.fly())
  print("Duck swim:", duck.swim())
  print("Duck sound:", duck.sound())

  section("Hierarchical Inheritance")
  shapes = [Circle(3), Rectangle(4, 5), Triangle(6, 2)]
  for s in shapes:
    print(type(s).__name__, "area:", s.area())

  section("Hybrid (Diamond) Inheritance")
  obj = D()
  print("D who:", obj.who())
  print("D MRO:", [cls.__name__ for cls in D.mro()])


if __name__ == "__main__":
  main()
