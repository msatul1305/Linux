b1 = [1, 1, 0, 0, 1]
b2 = [1, 0, 1, 0, 1]
c = [0, 0, 0, 0, 0, 0]
#  diff size?
n = len(b1)
carry = 0
for i in range(n-1, -1, -1):
    if b1[i] + b2[i] + carry == 2:
        c[i] = 0
        carry = 1
    elif b1[i] + b2[i] + carry == 3:
        c[i] = 1
        carry = 1
    else:
        c[i+1] = b1[i] + b2[i] + carry
        carry = 0
c[0] = carry
print(c)
