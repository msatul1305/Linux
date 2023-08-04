# Duck Typing is a way of programming in which an object passed into a function or method supports all method signatures and attributes expected of that object at run time.
# since in python we donot have data types defined, all methods are duck typed
# “If it looks like a duck and quacks like a duck, it’s a duck”

def add(x:int, y:int):
    return x+y

print(add(1.1,2.2))
