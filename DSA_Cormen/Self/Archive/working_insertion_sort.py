lis = [1, 5, 4, 3, 6, 7, 9]
# lis = [10, 1, 5, 4, 3, 6, 7, 9]
l1 = []
l1.insert(0, lis[0])
# l1= [1]
for item in lis[1:]:
    j = 0
    for j in range(len(l1)+1):
        if l1[j] > item:
            l1[j+1] = l1[j]
    l1.insert(j, lis[0])
