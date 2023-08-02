class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Llist:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        # if no element in llist
        if self.head is None:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    def remove(self):
        pass

    def search(self):
        pass

    def display(self):
        curr = self.head
        while curr:
            print(curr.data)
            curr = curr.next


ll = Llist()
ll.append(10)
ll.append(20)
ll.append(30)
ll.display()
