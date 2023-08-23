needle = "pi"
haystack = "mississippi"


def count(s):
    c = 0
    x = len(s) - 1
    for i in s:
        c = c + ord(i) * (10**x)
        x = x - 1
    return c


asum = count(needle)
for i in range(len(haystack)):
    bsum = count(haystack[i:i + len(needle)])
    if bsum == asum:
        print(i)
        break
print(-1)
