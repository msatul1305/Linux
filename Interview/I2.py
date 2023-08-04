# https://www.interviewbit.com/python-interview-questions/
import array
a = array.array([1, 2, 3])
for i in a:
    print(i, end=' ')    #OUTPUT: 1 2 3
# a = array.array('i', [1, 2, 'string'])    #OUTPUT: TypeError: an integer is required (got type str)
# a = [1, 2, 'string']
# for i in a:
#     print(i, end=' ')    #OUTPUT: 1 2 string
