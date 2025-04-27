from pandas.io.formats.format import return_docstring

a = [1,2,3,50,40,10]

def fun(a):
    # k = 0
    for i in range(a):
        x = 100 - a[i]
        if x in a[i:]:
            return True

print(fun(a))