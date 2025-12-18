# property, Getter and Setter

# class User:
#   def __init__(self,age):
#     self.age = age

# u = User(20)
# print(u.age)
# # problem: data can be modified easily, control over the data is lost

#solution : using @property 

class User:
    def __init__(self, age):
        self.age = age   # looks public, but controlled

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age cannot be negative")
        self._age = value

u = User(20)
u.age = 25        # setter called
print(u.age)      # getter called
