from typing import List


def print_char(strs: List[str]):
    l1 = len(strs)
    small = 100
    for x in strs:
        if len(x) < small:
            small = len(x)
    l2 = small
    res = ""
    c = 0
    ch = ''
    for i in range(l2):
        for j in range(l1):
            while j < l1 - 1:
                if strs[j][i] == strs[j + 1][i]:
                    j += 1
                    ch = strs[j][i]
                    continue
                else:
                    c = 1
                    break
            if c == 1:
                break
        res += ch
    print(res)


# print_char(["hello", "hepo"])
print_char(['flower', 'flow', 'flight'])
