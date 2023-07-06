# list should be sorted for binary search
l = [1, 5, 7, 9, 11, 15, 20]
x = 10
# find x
p = 0
q = len(l)
n = len(l)
def func(l, p,q,n):
    c = 0
    while p<=q and q>0:
        mid = int((p + q)/2)
        if l[mid]>x:
            q = mid
        elif l[mid]<x:
            p = mid
        elif l[mid] == x:
            c = 1
            return mid
    if c == 0:
        return -1
print(func(l,p,q,n))
