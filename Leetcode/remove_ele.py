a = 'xyz'
b = 'abcxyzabc'
j = 0
c = 0
for i in range(len(b)):
    if b[i] == a[j]:
        while b[i] == a[j] and i < len(b) - 1 and j < len(a) - 1:
            i = i + 1
            j = j + 1
        if j == len(a) - 1 and b[i] == a[j]:
            print(i-len(a)+1)
            c = 1
            break
        else:
            j = 0
            continue
if c == 0:
    print(-1)
