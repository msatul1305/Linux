# top will always point to most recently inserted data
# Insertion happens to front of LL(push)
# Deletion also happens from front(pop)
# i.e. stack.push(1), stack.push(2), stack.push(3)
# stack will look like: 3(top)->2-> 1.
# stack.push(4) => 4(top)->3->2->1
# stack.pop() => 3(top)->2-> 1
