def strStr(self, haystack: str, needle: str) -> int:
    j = 0
    c = 0
    for i in range(len(haystack)):
        if haystack[i] == needle[j]:
            while haystack[i] == needle[j] and i < len(haystack) - 1 and j < len(needle) - 1:
                i = i + 1
                j = j + 1
            if j == len(needle) - 1 and haystack[i] == needle[j]:
                c = 1
                return i-len(needle) + 1
            else:
                j = 0
                continue
    if c == 0:
        return -1
