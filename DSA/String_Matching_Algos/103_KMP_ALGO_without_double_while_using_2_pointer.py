a = "bbaacabcbc"
b = "aabaaac"
def find_lps(s):
    lps = [0] * len(s)
    i = 0
    j = 1
    x = 1
    k = 0
    while i < len(s):
        if j < len(s) and s[k] == s[j]:
            lps[j] = x
            x = x + 1
            j = j + 1
            k = k + 1
            i = i + 1
        else:
            if k!=0:
                k = lps[k-1]
            else:
                if j < len(s):
                    lps[j] = 0
                    x = 1
                    j = j + 1
                    k = 0
                i = i + 1

    return lps
lps = find_lps(b)
print(lps)
i = 0
j = -1

while i < len(a):
    if a[i] == b[j]:
        j = j + 1
    else:
        j = lps[j]
    if j == len(b) - 1:
        print(i-j+1)
        break
    i = i + 1
