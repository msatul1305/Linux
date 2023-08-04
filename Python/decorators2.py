import math

class Circle:
    def __init__(self, radius=1):
        self.radius = radius

    # If we add @property, then we don't need to call area() using brackets. It acts like a virtual attribute of class.
    @property
    def area(self):
        return math.pi * self.radius ** 2

obj = Circle(2)
print(obj.area)
