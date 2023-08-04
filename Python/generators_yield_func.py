# yield also called generators in py
# functions that return an iterable collection of items, one at a time, in a set manner.
# used to create iterators with a different approach.
# They employ the use of yield keyword rather than return to return a generator object.
# generate fibonacci numbers upto n
def fib(n):
    p, q = 0, 1
    while(p < n):
        yield p
        p, q = q, p + q
x = fib(10)    # create generator object

## iterating using __next__(), for Python2, use next()
x.__next__()    # output => 0
x.__next__()    # output => 1
x.__next__()    # output => 1
x.__next__()    # output => 2
x.__next__()    # output => 3
x.__next__()    # output => 5
x.__next__()    # output => 8
x.__next__()    # error

## iterating using loop
for i in fib(10):
    print(i)    # output => 0 1 1 2 3 5 8
