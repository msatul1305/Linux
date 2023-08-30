def addBinary(a: str, b: str):
    n1 = len(a) - 1
    n2 = len(b) - 1
    carry = 0
    a = [int(item) for item in a]
    b = [int(item) for item in b]
    c = []
    i = n1
    j = n2
    while i >= 0 and j >=0:
        if a[i] + b[j] + carry == 2:
            c.insert(0, 0)
            carry = 1
        elif a[i] + b[j] + carry == 3:
            c.insert(0, 1)
            carry = 1
        else:
            c.insert(0, a[i]+b[j]+carry)
            carry = 0
        i = i - 1
        j = j - 1
    while i>=0:
        if a[i] + carry == 2:
            c.insert(0, 0)
            carry = 1
        else:
            c.insert(0, a[i] + carry)
            carry = 0
        i = i - 1
    while j>=0:
        if b[j] + carry == 2:
            c.insert(0, 0)
            carry = 1
        else:
            c.insert(0, b[j] + carry)
            carry = 0
        j = j - 1
    if carry !=0:
        c.insert(0, carry)
    d = ""
    for x in c:
        d = d + str(x)
    return d


a = "101111"
b = "10"
print(addBinary(a, b))
