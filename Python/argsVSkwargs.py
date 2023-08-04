# *args
#
# *args is a special syntax used in the function definition to pass variable-length arguments.
# “*” means variable length and “args” is the name used by convention. You can use any other.
def multiply(a, b, *argv):
    mul = a * b
    for num in argv:
        mul *= num
    return mul
print(multiply(1, 2, 3, 4, 5)) #output: 120

# **kwargs
# **kwargs is a special syntax used in the function definition to pass variable-length ***keyworded*** arguments.
# Here, also, “kwargs” is used just by convention. You can use any other name.
# Keyworded argument means a variable that has a name when passed to a function.
# It is actually a dictionary of the variable names and its value.
def tellArguments(**kwargs):
    for key, value in kwargs.items():
        print(key + ": " + value)
tellArguments(arg1 = "argument 1", arg2 = "argument 2", arg3 = "argument 3")
#output:
# arg1: argument 1
# arg2: argument 2
# arg3: argument 3
