lis = [10, 1, 5, 4, 3, 6, 7, 9]
l1 = []
l1.insert(0, lis[0])
for item in lis[1:]:
    j = 0
    while (item < l1[j]) and (j < len(l1)):
        l1.insert(j+1, l1[j])
        j = j + 1
        # l1[j+1] = l1[j]
    # l1[j] = item
    l1.insert(j+1, item)
print(l1)
