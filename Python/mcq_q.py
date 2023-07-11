# l1 = [1,2,3,4,5]
# l1.pop(1)
# print(l1)
#
# a = 10
# b = 2
# print(a**b)

class X:
    def __init__(self):
        self.__num1 = 5
        self.num2 = 2

    def display_values(self):
        print(self.__num1, self.num2)
class Y(X):
    def __init__(self):
        super().__init__()
        self.__num1 = 1
        self.num2 = 6
    def display_values(self):
        print(self.__num1, self.num2)

obj = Y()
X.display_values(self=obj)
