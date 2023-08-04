class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Llist:
    def __init__(self):
        self.head = None

    def insert_beginning(self, data):
        new_node = Node(data)
        curr = new_node
        curr.next = self.head
        self.head = curr

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

    def remove(self, d):
        if self.head is None:
            print("Empty LL")
            return None

        # for first element
        if self.head.data == d:
            temp = self.head
            self.head = self.head.next  # i.e. None
            temp.next = None
            temp.data = 0
            print(f"deleted {d}")
            return

        else:
            curr = self.head
            while curr.next:
                if curr.next.data != d:
                    curr = curr.next
                else:
                    break
            if not curr.next:
                print("Not found")
                return
            else:
                prev = curr     # to shift prev.next to curr.next
                curr = curr.next    # to delete curr
                prev.next = curr.next
                curr.next = None
                curr.data = 0
                print(f"delete op {d}")
                return

    def search(self, d):
        if self.head is None:
            print("Empty LL")
            return None
        curr = self.head
        while curr:
            if curr.data != d:
                curr = curr.next
            else:
                print(f'{d} found at {curr}: {curr.data}')
                return curr
        print("Not Found")
        return None

    def display(self):
        curr = self.head
        while curr:
            if curr.next is not None:
                print(curr.data, end=" -> ")
            else:
                print(curr.data)
            curr = curr.next


ll = Llist()
ll.search(100)
ll.append(10)
ll.append(20)
ll.append(30)
ll.display()
ll.search(20)
ll.search(30)
ll.search(0)
ll.search(10)
ll.display()
ll.insert_beginning(1)
ll.display()
ll.insert_beginning(3)
ll.display()
ll.remove(2)
ll.remove(30)
ll.display()
ll.remove(20)
ll.display()
ll.remove(20)
ll.remove(10)
ll.display()
