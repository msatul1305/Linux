def mySqrt(x: int) -> int:
    i = 0
    for i in range(int(x/2) + 2):
        if i*i == x:
            return i
        elif i*i > x:
            break
    if i>=1:
        return i - 1
    else:
        return 0



print(mySqrt(1))
