# A decorator allows a user to modify the behavior of a function or a class without modifying its source code directly.
# The syntax for using a decorator is to place the decorator function above the function or class that needs to be modified using @symbol,
# and then to call the decorator function with the function or class as an argument.

# Decorators are usually used to add functionality such as logging, timing, caching, or authentication to existing functions.
def add_prefix(func):
    def wrapper(string):
        return "Prefix: " + func(string)
    return wrapper

@add_prefix
def my_func(string):
    return string

print(my_func("Hello"))




# eg 2
def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function {func.__name__} with arguments {args} and {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@log_decorator
def my_function(x, y):
    return x + y

result = my_function(3, 5)  # Calling function my_function with arguments (3, 5) and {}
print(result)  # 8



# Chaining Decorators -  gfg
# code for testing decorator chaining
def decor1(func):
    def inner():
        x = func()
        return x * x
    return inner

def decor(func):
    def inner():
        x = func()
        return 2 * x
    return inner

@decor1
@decor
def num():
    return 10

@decor
@decor1
def num2():
    return 10

print(num())
print(num2())