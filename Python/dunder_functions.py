# Dunder functions are like constructor which intialises class object and determines their behaviour
# normally if we print object, it prints bject at main bal bla... but with __repr__, it prints value of string present in objct.
# 1. __init__(self)
# 2. __repr__(self):
# 3. __add__(self, other):
# 4. __iter__()

# 4. __iter__() is used

# Some more operations and their corresponding dunders:
# a < b : a.__lt__(b)
# a != b: a.__ne__(b)
# a % b: a.__mod__(b)
# def f(x): return x**2 : f.__call__(5)
# lis = [1,2,3,4], len(lis): lis.__len__()
# lis[-1]: lis.__getitem__(-1)

# there is no destructor in python, Everything is a pointer/object in python. we don't have any control
# of memory management in py.
# declare our own string class
class String:

    # magic method to initiate object
    def __init__(self, s1, s2):
        self.s1 = s1
        self.s2 = s2
    # print our string object
    def __repr__(self):
        return 'Object: {}'.format(self.s1)
    def __add__(self, other):
        return self.s1 + other
    def __eq__(self, other):
        pass

# Driver Code
if __name__ == '__main__':

    # object creation
    string1 = String('Hello', "World")

    # print object location
    # print(string1)
    print(string1 +' Geeks')


# dunder repr vs dunder str
# __repr__() is used for debugging and development purposes, while __str__() is used for display purposes.
# __repr__() should return a string that, when evaluated by Python, can be used to recreate the object. On the other
# hand, __str__() should return a human-readable string that represents the object.
# If an object does not have a __str__() method, but does have a __repr__() method, the __repr__() method will be used
# as a fallback for display purposes.
# If an object does not have a __repr__() method, but does have a __str__() method, the __str__() method will be used
# as a fallback for debugging purposes.
# if object has both, print(obj) will print obj.__str__().
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"
    def __repr__(self):
        return f"{self.name} : {self.age}"

p = Person("Alice", 30)
print(p.__str__())
print(p.__repr__())
print(p)
print(str(p))
print(repr(p))
