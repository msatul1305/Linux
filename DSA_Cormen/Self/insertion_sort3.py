lis = [11, 4, 5, 3, 2]

for i in range(1, len(lis)):
    curr = lis[i]  # 4
    j = i-1
    while j >= 0 and lis[j] > curr:
        lis[j+1] = lis[j]
        j = j - 1
    lis[j+1] = curr
print(lis)
