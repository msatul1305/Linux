class ListNode:
    def __init__(self, value):
        self.val = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add_at_head(self, value):
        new_node = ListNode(value)
        new_node.next = self.head
        self.head = new_node

    def add_at_tail(self, value):
        new_node = ListNode(value)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.val, end=" -> ")
            current = current.next
        print("None")

    def deleteDuplicates(self):
        head = self.head
        lis = head
        curr_val = head.val
        curr = head
        while curr:
            while curr.next and curr.next.val == curr_val:
                curr = curr.next
            if curr.next:
                head.next = curr.next
                curr_val = curr.next.val
                head = head.next
            if not curr.next:
                head.next = None
            curr = curr.next
        return lis


# Example usage
linked_list = LinkedList()
linked_list.add_at_tail(1)
linked_list.add_at_tail(1)
linked_list.add_at_tail(2)
linked_list.add_at_tail(3)
linked_list.add_at_tail(3)
# linked_list.display()
linked_list.deleteDuplicates()
linked_list.display()

