# # approach 1: using parent class name
# class Parent(object):
#     # Constructor
#     def __init__(self, name):
#         self.name = name
#
# class Child(Parent):
#     # Constructor
#     def __init__(self, name, age):
#         Parent.name = name
#         self.age = age
#
#     def display(self):
#         print(Parent.name, self.age)
#
# # Driver Code
# obj = Child("Interviewbit", 6)
# obj.display()

# approach 2: using super
class Parent(object):
    # Constructor
    def __init__(self, name):
        self.name = name

class Child(Parent):
    # Constructor
    def __init__(self, name, age):
        '''
        In Python 3.x, we can also use super().__init__(name)
        '''
        super().__init__(name)
        self.age = age

    def display(self):
        # Note that Parent.name cant be used
        # here since super() is used in the constructor
        print(self.name, self.age)

# # Driver Code
obj = Child("Interviewbit1", 6)
obj.display()
