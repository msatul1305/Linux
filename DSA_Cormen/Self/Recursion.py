def fc(n):
    n = n + 1
    if n == 3:
        return
    if n>=0:
        fc(n)
    print(n)


fc(0)
