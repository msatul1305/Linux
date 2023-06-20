# A descriptor in Python is a protocol that allows objects to define customized behavior when they are accessed, assigned, or deleted. It is a way to define how attribute access is handled in a class. Descriptors are mainly used for managing and controlling access to attributes in Python classes.
# A descriptor is implemented by defining methods such as __get__, __set__, and __delete__ in a descriptor class. These methods define the behavior when an attribute is accessed, assigned, or deleted.
# When an attribute is accessed, the __get__ method is called. It takes three arguments: the instance of the class accessing the attribute, the class itself, and an optional owner object. The __get__ method returns the value of the attribute or performs any other desired action.
# When an attribute is assigned a value, the __set__ method is called. It takes the same three arguments as __get__, along with the value being assigned. The __set__ method is responsible for storing the assigned value or performing any other necessary actions.
# When an attribute is deleted using the del statement, the __delete__ method is called. It takes two arguments: the instance of the class and the owner object. The __delete__ method performs any necessary cleanup or deletion of the attribute.
# Descriptors can be used to implement various behaviors, such as data validation, lazy attribute initialization, computed properties, and more. They provide a flexible way to customize attribute access in Python classes.
# List of all descriptors py:
# In Python, there are three types of descriptors that can be used to define attribute access behavior:
# Data Descriptors:
# property: A built-in Python descriptor that allows defining getter, setter, and deleter methods for attribute access.
# dataclasses.field: A descriptor used in Python's dataclasses module to define fields with default values and other attributes.
# Non-Data Descriptors:
# staticmethod: A built-in Python descriptor that allows a method to be accessed directly from the class, rather than through an instance.
# classmethod: A built-in Python descriptor that allows a method to receive the class as the first argument, rather than the instance.
# abc.abstractproperty: A descriptor used in the abc module to define abstract properties.
# enum.Enum: A descriptor used in the enum module to define enumeration members.
# Get-only Descriptors:
# __get__: A method that can be defined in a custom descriptor class to handle attribute access.
# __set__: A method that can be defined in a custom descriptor class to handle attribute assignment.
# __delete__: A method that can be defined in a custom descriptor class to handle attribute deletion.
# These descriptors can be used individually or in combination to define custom attribute access behavior in Python classes. It's worth noting that the descriptors mentioned above are commonly used, but you can also create your own custom descriptors by defining the __get__, __set__, and __delete__ methods in a descriptor class according to your specific requirements.
# Here are some examples of descriptors in Python:
# Property Descriptor:
# The property descriptor allows you to define getter, setter, and deleter methods for attribute access.


class Circle:
    def __init__(self, radius):
        self._radius = radius
    
    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise ValueError("Radius must be positive")
        self._radius = value
    
    @radius.deleter
    def radius(self):
        del self._radius

# Usage:
c = Circle(5)
print(c.radius)  # Output: 5
c.radius = 10
print(c.radius)  # Output: 10
del c.radius
print(c.radius)  # Raises AttributeError


# Static Method Descriptor:
# The staticmethod descriptor allows you to define methods that can be accessed directly from the class.

class MathUtils:
    @staticmethod
    def add(x, y):
        return x + y

# Usage:
print(MathUtils.add(2, 3))  # Output: 5

# Class Method Descriptor:
#
# The classmethod descriptor allows you to define methods that receive the class as the first argument.


class Person:
    count = 0
    
    def __init__(self, name):
        self.name = name
        Person.count += 1
    
    @classmethod
    def get_count(cls):
        return cls.count

# Usage:
p1 = Person("Alice")
p2 = Person("Bob")
print(Person.get_count())  # Output: 2


# Custom Descriptor:
#
# You can create your own custom descriptor by defining the __get__, __set__, and __delete__ methods.

class Celsius:
    def __init__(self, temperature=0):
        self._temperature = temperature
    
    def to_fahrenheit(self):
        return (self._temperature * 9/5) + 32
    
    def __get__(self, instance, owner):
        return self._temperature
    
    def __set__(self, instance, value):
        if value < -273.15:
            raise ValueError("Temperature value is too low")
        self._temperature = value

class Temperature:
    celsius = Celsius()
    
# Usage:
t = Temperature()
t.celsius = 25
print(t.celsius)  # Output: 25
# print(t.celsius.to_fahrenheit())  # Output: 77.0
t.celsius = -300  # Raises ValueError

