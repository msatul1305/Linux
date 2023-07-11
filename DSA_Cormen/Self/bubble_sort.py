# 2 for loops, swap if a[j]<a[i], i from 0 to n-1, j from i+1 to n
l = [9, 5, 4, 3, 6, 7]
n = len(l)
for i in range(0, n-1):
    for j in range(i+1, n):
        if l[i] > l[j]:
            temp = l[i]
            l[i] = l[j]
            l[j] = temp

print(l)
