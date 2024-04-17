# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Llist:
    def __init__(self):
        self.head = None

    def insert_beginning(self, val):
        new_node = ListNode(val)
        curr = new_node
        curr.next = self.head
        self.head = curr

    def append(self, val):
        new_node = ListNode(val)
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
        if self.head.val == d:
            temp = self.head
            self.head = self.head.next  # i.e. None
            temp.next = None
            temp.val = 0
            print(f"deleted {d}")
            return

        else:
            curr = self.head
            while curr.next:
                if curr.next.val != d:
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
                curr.val = 0
                print(f"delete op {d}")
                return

    def search(self, d):
        if self.head is None:
            print("Empty LL")
            return None
        curr = self.head
        while curr:
            if curr.val != d:
                curr = curr.next
            else:
                print(f'{d} found at {curr}: {curr.val}')
                return curr
        print("Not Found")
        return None

    def display(self):
        curr = self.head
        while curr:
            if curr.next is not None:
                print(curr.val, end=" -> ")
            else:
                print(curr.val)
            curr = curr.next


def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    new_lis = ListNode(-1)
    head = new_lis
    while list1 and list2:
        # print(list1.val, list2.val)
        if list1.val <= list2.val:
            new_lis.val = list1.val
            list1 = list1.next
        elif list1.val > list2.val:
            new_lis.val = list2.val
            list2 = list2.next
        new_lis.next = ListNode(-1)
        new_lis = new_lis.next

    while list1:
        new_lis.val = list1.val
        list1 = list1.next
        new_lis.next = ListNode(-1)
        new_lis = new_lis.next
    while list2:
        new_lis.val = list2.val
        list2 = list2.next
        new_lis.next = ListNode(-1)
        new_lis = new_lis.next
    # print(new_lis)
    curr = head
    print(f"curr0: {curr}")
    while curr.next.next:
        print(f"curr1: {curr}")
        curr = curr.next
    print(f"curr2: {curr}")
    curr.next = None
    return head

x1: ListNode = ListNode(-1)
x2 = ListNode(-1)
temp = None
x1.val = 1
x1.next = ListNode(-1)
temp = x1.next
# x1 = x1.next
temp.val = 2
# x1.next = temp
temp.next = ListNode(-1)
# x1 = x1.next
temp.next.val = 4

temp = None
x2.val = 1
x2.next = ListNode(-1)
temp = x2.next
# x1 = x1.next
temp.val = 3
# x1.next = temp
temp.next = ListNode(-1)
# x1 = x1.next
temp.next.val = 4
# print(x1)
mergeTwoLists(x1, x2)
