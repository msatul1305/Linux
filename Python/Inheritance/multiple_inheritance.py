# Parent class1
class Parent1:
    def parent1_func(self):
        print("Hi I am first Parent")

# Parent class2
class Parent2:
    def parent2_func(self):
        print("Hi I am second Parent")

# Child class
class Child(Parent1, Parent2):
    def child_func(self):
        self.parent1_func()
        self.parent2_func()

# Driver's code
obj1 = Child()
obj1.child_func()
