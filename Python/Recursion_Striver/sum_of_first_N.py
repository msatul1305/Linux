def s(N):
    if N==1:
        return 1
    return N + s(N-1)


N = 10
print(s(N))
