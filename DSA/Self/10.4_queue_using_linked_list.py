# back will always point to most recently inserted data
# front will always point to least recently inserted data
# Insertion happens from back of LL(push)
# Deletion also happens from front(pop)
# i.e. queue.push(1), queue.push(2), queue.push(3)
# queue will look like: 1(front)->2->3(back)
# queue.push(4) => 1(front)->2->3->4(back)
# queue.pop() => 2(front)->3->4(back)
