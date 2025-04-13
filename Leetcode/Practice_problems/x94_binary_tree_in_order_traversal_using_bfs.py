# Definition for a binary tree node.
from queue import Queue
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int] | None:
        q = Queue()
        l = []
        curr_q = list(q.queue)
        q.put(root)
        curr_q = list(q.queue)
        while not q.empty():
            node = q.get()
            l.append(node.val)
            curr_q = list(q.queue)
            if node is None:
                continue
            if node.left is not None:
                q.put(node.left)
                curr_q = list(q.queue)
            if node.right is not None:
                q.put(node.right)
                curr_q = list(q.queue)
        return l

x = TreeNode(val=1, left=None, right=None)
x.right = TreeNode(val=2, left=None, right=None)
x.right.left = TreeNode(val=3, left=None, right=None)
y = Solution()
z = y.inorderTraversal(x)
print(z)
