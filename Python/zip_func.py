l1 = [1, 2, 5, 4]
l2 = [6, 9, 0, 3]
x = (zip(l1, l2))
print(list(x))

q1 = ["hello"]
q2 = ["hi"]

print(list(zip(q1, q2)))

k = ["hello", "hi"]
print(list(zip(*k)))

k = ["hi", "hello"]
print(list(zip(*k)))
