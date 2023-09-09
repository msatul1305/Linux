def pal(i):
    if i>=n/2:
        return True
    if s[i] != s[n-i]:
        return False
    return pal(i+1)


s = 'araabara'
n = len(s) - 1
print(pal(0))
# rev(arr, n)
