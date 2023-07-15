# (a, b) * (c, d) where b == c then only matrix multiplication possible
x1 = [[1, 2, 3], [4, 5, 6]]
x2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

a = len(x1)
b = len(x1[0])
c = len(x2[0])
x3 = [[0 for j in range(c)] for i in range(a)]
for i in range(a):
    for j in range(b):
        for k in range(c):
            x3[i][j] += (x1[i][k]*x2[k][j])
print(x3)
