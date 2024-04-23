# Knuth-Morris-Pratt Algo
# first find LPS of a, i.e. find all suffixes which match prefix
# a = 'aaaabaacd'
# b = 'abababcabc'
b = "aabaaabaaac"
a = "aabaaac"

def longest_perfect_suffix(s):
    lps = [0]*len(s)
    i = 1
    while i < len(s):
        j = 0
        x = 1
        if s[i] == s[j]:
            while i < len(s) and s[i] == s[j]:
                lps[i] = x
                x = x + 1
                i = i + 1
                j = j + 1
        i = i + 1
    return lps


a_pi_table_or_lps = longest_perfect_suffix(a)  # longest proper prefix, which is also a suffix
print(a_pi_table_or_lps)
