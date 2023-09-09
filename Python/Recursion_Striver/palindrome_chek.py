def pal(s, i):
    if i>=n/2:
        return True
    if s[i] == s[n-i]:
        return pal(s, i+1)
    else:
        return False


s = 'araara'
n = len(s) - 1
print(pal(s, 0))
# rev(arr, n)
