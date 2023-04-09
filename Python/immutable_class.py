# In Python, you can create an immutable class by using the namedtuple function from the collections module or by
# creating a class and defining its __slots__ attribute
from collections import namedtuple

Person = namedtuple('Person', ['name', 'age'])

p1 = Person('Alice', 30)
p2 = Person('Bob', 25)

print(p1.name, p1.age)  # Output: Alice 30
print(p2.name, p2.age)  # Output: Bob 25

# Attempting to modify an attribute will raise an AttributeError
try:
    p1.age = 35
except AttributeError as e:
    print(e)  # Output: can't set attribute
# Reasons NOT to use a Namedtuple
# Before Python 3.7 it was frequent to see namedtuples being used as immutable objects. It can be tricky in many ways,
# one of them is that the __eq__ method between namedtuples does not consider the objects' classes. For example:
from collections import namedtuple

ImmutableTuple = namedtuple("ImmutableTuple", ["a", "b"])
ImmutableTuple2 = namedtuple("ImmutableTuple2", ["a", "c"])

obj1 = ImmutableTuple(a=1, b=2)
obj2 = ImmutableTuple2(a=1, c=2)

print(obj1 == obj2) # will be True
# As you see, even if the types of obj1 and obj2 are different,
# even if their fields' names are different, obj1 == obj2 still gives True.
# That's because the __eq__ method used is the tuple's one, which compares only the values of the fields given
# their positions. That can be a huge source of errors, specially if you are subclassing these classes.


# And here's an example using a custom class with __slots__:
class Person:
    __slots__ = ['name', 'age']

    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person('Alice', 30)
p2 = Person('Bob', 25)

print(p1.name, p1.age)  # Output: Alice 30
print(p2.name, p2.age)  # Output: Bob 25

# Attempting to add a new attribute will raise an AttributeError
try:
    p1.height = 170
except AttributeError as e:
    print(e)  # Output: 'Person' object has no attribute 'height'


