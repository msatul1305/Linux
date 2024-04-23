# In merge function, we assume that subarrays are sorted i.e. sublist 0 to p and q to n are already sorted.
# if n=odd, 2nd part of list has more elements.
# n = 8
# p = 3 [0,1,2,3] = n/2
# q = 4 [4,5,6,7] = n/2

# n = 9
# p = 4 [0,1,2,3] = n/2
# q = 4 [4,5,6,7,8] = n/2
def merge(lis, p, q, r):
    """"
    Arguments:
    A -- a list/array containing the sublists/subarrays to be merged
    p -- index of the beginning of the first sublist/subarray
    q -- index of the end of the first sublist/subarray;
    the second sublist/subarray starts at index q+1
    r -- index of the end of the second sublist/subarray
    """
    n = len(lis)
    # p = 0
    # if n % 2 == 0:
    #     q = int(n/2) + 1
    # else:
    #     q = int(n/2-1)
    # q = int(n/2)
    ini_q = q
    p = p
    r = r
    i = 0    # index into left sublist/subarray
    j = 0    # index into right sublist/subarray
    k = p    # index into a[p: r+1]

    new_lis = []
    k = 0
    while p < ini_q and q < n:
        if lis[p] <= lis[q]:
            new_lis.insert(k, lis[p])
            p = p + 1
        elif lis[p] > lis[q]:
            new_lis.insert(k, lis[q])
            q = q + 1
        k = k + 1

    while p < ini_q and k < n:
        new_lis.insert(k, lis[p])
        k = k + 1
        p = p + 1
    while q < n and k < n:
        new_lis.insert(k, lis[q])
        k = k + 1
        q = q + 1

    print(new_lis)

# lis = [2, 4, 6, 7, 5, 8, 9, 10]
# lis = [2, 4, 6, 5, 7, 8, 9]
# merge(lis)

def merge_sort(l, a, b):
    a = 0
    b = n/2
    merge_sort(l, a, b)
    merge_sort(l, b, n)
    merge(l[a:b])


l = [7,1,3,4,5,2]
# print(l[a:b])
merge_sort(l, len(l))