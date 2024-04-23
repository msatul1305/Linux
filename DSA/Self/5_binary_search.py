# list should be sorted for binary search
l = [1, 5, 7, 9, 11, 15, 20]
x = 5
# find x
p = 0
q = len(l) -1
n = len(l)
def func(l, p,q):
    while p<=q:
        mid = int((p + q)/2)
        if l[mid]>x:
            q = mid -1
        elif l[mid]<x:
            p = mid +1
        elif l[mid] == x:
            return mid
    return -1
print(func(l,p,q))
