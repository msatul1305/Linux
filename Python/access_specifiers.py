# to demonstrate access specifiers
class InterviewbitEmployee:

    # protected members
    _emp_name = None
    _age = None

    # private members
    __branch = None

    # constructor
    def __init__(self, emp_name, age, branch):
        self._emp_name = emp_name
        self._age = age
        self.__branch = branch

    #public member
    def display(self):
        print(self._emp_name +" "+self._age+" "+self.__branch)

x = InterviewbitEmployee("yash", '20', "cse")
x.display()
