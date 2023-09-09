def merge_sort(a, m, b, n):
    """
    Do not return anything, modify nums1 in-place instead.
    """
    i = m - 1
    j = n - 1
    k = m + n - 1
    while k>=0:
        if a[i] < b[j]:
            a[k] = b[j]
            k = k - 1
            j = j - 1
        else:
            a[k] = a[i]
            k = k - 1
            i = i - 1
    while j>=0:
        a[k] = b[j]
        j = j  - 1
        k = k - 1

# a = [1, 2, 5, 6, 0, 0, 0, 0]
# b = [1, 3, 4, 7]
# a = [1, 2, 3, 0, 0, 0]
# b = [2,5,6]
# a = [2, 0]
# b = [1]
# a = [1,2,4,5,6,0]
# b = [3]
a = [0]
b = [1]
x = merge_sort(a, 0, b, 1)
print(x)
