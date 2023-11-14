def longest_palindromic_arrangement(s):
    countr = {}
    for char in s:
        countr[char] = countr.get(char, 0) + 1
    len = 0
    is_odd = False
    for c in countr.values():
        len += c // 2 * 2
        if c % 2 == 1:
            is_odd = True
    if is_odd:
        len += 1
    return len


print(longest_palindromic_arrangement('abccccddeeefg'))
