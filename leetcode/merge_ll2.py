from typing import Optional

from leetcode.merge_ll import ListNode


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        new_lis = head = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                new_lis.next = list1
                list1 = list1.next
                new_lis = list1
            else:
                new_lis.next = list2
                list2 = list2.next
                new_lis = list2

        if list1 or list2:
            new_lis.next = list1 if list1 else list2

        return head.next
