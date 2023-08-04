def lower_decor(func_arg):
    def wrap():
        func = func_arg()
        string_lowercase = func.lower()
        return string_lowercase
    return wrap

@lower_decor
def hello1():
    return "Str1"

print(hello1())
# print(f)


# decorator function to convert to lowercase
# def lowercase_decorator(function):
#     def wrapper():
#         func = function()
#         string_lowercase = func.lower()
#         return string_lowercase
#     return wrapper
# # decorator function to split words
# def splitter_decorator(function):
#     def wrapper():
#         func = function()
#         string_split = func.split()
#         return string_split
#     return wrapper
# @splitter_decorator # this is executed next
# @lowercase_decorator # this is executed first
# def hello():
#     return 'Hello World'
# print(hello())   # output => [ 'hello' , 'world' ]

# class hello:
#     def __init__(self):
#         print("hello2")
# h = hello()
