from collections import deque
d = deque('ghi')
for ele in d:
    print(ele)
d.pop()
print(d)
d.append('x')
print(d)
d.popleft()
print(d)
# d.insert('y')
# print(d)
