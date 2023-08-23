def strStr(haystack: str, needle: str) -> int:
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
            elif j < len(s):
                lps[j] = 0
                x = 1
                j = j + 1
                k = 0
            i = i + 1
        return lps
    lps = find_lps(needle)
    i = 0
    j = 0

    while i < len(haystack):
        if haystack[i] == needle[j]:
            j = j + 1
            i = i + 1
        if j == len(needle):
            return i-j
        elif i < len(haystack) and haystack[i] != needle[j]:
            if j!=0:
                j = lps[j-1]
            else:
                i = i + 1
    return -1

print(strStr("aabaaabaaac","aabaaac"))
