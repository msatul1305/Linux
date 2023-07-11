# An iterator is an object.
# It remembers its state i.e., where it is during iteration (see code below to see how)
# __iter__() method initializes an iterator.
# It has a __next__() method which returns the next item in iteration and points to the next element. Upon reaching the end of iterable object __next__() must return StopIteration exception.
# It is also self-iterable.
# Iterators are objects with which we can iterate over iterable objects like lists, strings, etc.
class ArrayList:
    def __init__(self, number_list):
        self.numbers = number_list
    def __iter__(self):
        self.pos = 0
        return self
    def __next__(self):
        if(self.pos < len(self.numbers)):
            self.pos += 1
            return self.numbers[self.pos - 1]
        else:
            raise StopIteration
array_obj = ArrayList([1, 2, 3])
it = iter(array_obj)
print(next(it)) #output: 1
print(next(it)) #output: 2
print(next(it)) #output: 3
print(next(it))
#Throws Exception
#Traceback (most recent call last):
#...
#StopIteration