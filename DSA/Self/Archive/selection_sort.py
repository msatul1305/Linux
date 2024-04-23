# search for the lowest element in the list and keep adding them to start by swapping the element from its current position
def find_lowest(lis, start, n):
    low = lis[start]
    low_index = start
    for i in range(start, n):
        if low > lis[i]:
            low = lis[i]
            low_index = i
    return low, low_index

lis = [2, 4, 1, 9, 7, 8]
n = len(lis)
j = 0
for i in range(len(lis)):
    low, low_index = find_lowest(lis, i, n)
    lis[low_index] = lis[j]
    lis[j] = low
    j += 1
print(lis)
