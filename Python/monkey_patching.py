# Monkey patching is a technique used to dynamically update the behavior of a piece of code at run-time.

class MonkeyPatch:
    def __init__(self, n1):
        self.n1 = n1

    def add(self, other):
        self.n1 += other
        return (self.n1 + other)
    def __repr__(self):
        return f'{self.n1}'
def sub(self):
    return self.n1 - 10




obj1 = MonkeyPatch(100)
obj1.add(20)
print(obj1)
MonkeyPatch.sub = sub
print(obj1.sub())



# Eg2:
# new_monk.py
class A:
    def hello(self):
        print (" The hello() function is being called")

def monkey_f(self):
    print ("monkey_f() is being called")

# replacing address of "func" with "monkey_f"
A.hello = monkey_f
obj = A()

# calling function "func" whose address got replaced
# with function "monkey_f()"
obj.hello()



