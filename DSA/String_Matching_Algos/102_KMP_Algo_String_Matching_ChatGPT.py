# Knuth-Morris-Pratt Algo
# first find LPS of a, i.e. find all suffixes which match prefix
a = 'aabcadaabe'
b = 'abababcabc'


def longest_perfect_suffix(s):
    lps = [0] * len(s)
    length = 0  # Length of the previous longest prefix suffix
    i = 1

    while i < len(s):
        if s[i] == s[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

    return lps



a_pi_table_or_lps = longest_perfect_suffix(a)  # longest proper prefix, which is also a suffix
print(a_pi_table_or_lps)
