# Imagine a pack of cards needs to be sorted
# Pick cards one by one from deck and start moving all higher cards to right side.(cards already picked are in sorted order)
lis = [11, 4, 5, 3, 2]

for i in range(1, len(lis)):
    curr = lis[i]  # 4
    j = i-1
    while j >= 0 and lis[j] > curr:
        lis[j+1] = lis[j]
        j = j - 1
    lis[j+1] = curr
print(lis)
