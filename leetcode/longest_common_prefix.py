# from typing import List
#
#
# def longest_common_prefix(strs: List[str]) -> str:
#     i = 0
#     l = len(strs)
#     res = ''
#     l2 = len(strs[0])
#     for j in range(0, l2):
#         for i in range(0, l-1):
#             if j == l2-1 and strs[i][j] == strs[i+1][j]:
#                 res += strs[i][j]
#             elif strs[i][j] == strs[i+1][j]:
#                 res += strs[i][j]
#             else:
#                 return res
#     return res
# # print(longest_common_prefix(["hello", "hepo", "hego"]))
# print(longest_common_prefix(['flower', 'flow', 'flight']))
x = ['flower', 'flo', 'flight']
print(sorted(x))
print(list(zip(*x)))
for x in list(zip(*x)):
    print(set(x))
