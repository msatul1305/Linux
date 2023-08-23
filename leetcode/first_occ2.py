def strStr(haystack: str, needle: str) -> int:
    def find_lps(s):
        len1 = 0 
        lps = [0] * len(s)
        i = 1
        while i < len(s):
            if s[i] == s[len1]:
                len1 += 1
                lps[i] = len1
                i += 1
            else:
                if len1 != 0:
                    len1 = lps[len1-1]
                else:
                    lps[i] = 0
                    i += 1
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
