# search for the lowest element in the list and keep adding them to start by swapping the element from its current position
a = [2, 4, 1, 9, 7, 8]
n = len(a)
j = 0
for i in range(len(a)-1):
    small = i
    for j in range(i+1, n):
        if a[j] < a[small]:
            small = j
    temp = a[i]
    a[i] = a[small]
    a[small] = temp
print(a)
