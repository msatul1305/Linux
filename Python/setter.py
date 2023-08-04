import math

class Circle:
    def __init__(self, radius=1):
        self.radius = radius

    # If we add @property, then we donot need to call area() using brackets. It acts like a virtual attribute of class.
    @property
    def area(self):
        return math.pi * self.radius ** 2
    
    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, diameter):
        self.radius = diameter / 2


obj = Circle(2)
print(obj.area)

obj.radius = 2
print(obj.diameter)
obj.diameter = 10
print(obj.radius)
