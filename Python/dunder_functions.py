# Dunder functions are like constructor which intialises class object and determines their behaviour
# normally if we print object, it prints bject at main bal bla... but with __repr__, it prints value of string present in objct.
# 1. __init__(self)
# 2. __repr__(self):
# 3. __add__(self, other):


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

# Driver Code
if __name__ == '__main__':

    # object creation
    string1 = String('Hello', "World")

    # print object location
    # print(string1)
    print(string1 +' Geeks')