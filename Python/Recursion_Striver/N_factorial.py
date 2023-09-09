def fact(N):
    if N==1:
        return 1
    return N * fact(N-1)


N = 5
print(fact(N))
