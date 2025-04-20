# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int] | None:
        s = []
        l = []
        s.append(root)
        while s:
            node = s.pop()
            l.append(node.val)
            if node is None:
                continue
            while node.left is not None:
                s.append(node.left)
            while node.right is not None:
                s.append(node.right)
        return l


x = TreeNode(val=1, left=None, right=None)
x.left = TreeNode(val=2, left=None, right=None)
x.left.left = TreeNode(val=4, left=None, right=None)
x.left.right = TreeNode(val=5, left=None, right=None)
x.left.right.left = TreeNode(val=6, left=None, right=None)
x.left.right.right = TreeNode(val=7, left=None, right=None)
x.right = TreeNode(val=3, left=None, right=None)
x.right.right = TreeNode(val=8, left=None, right=None)
x.right.right.left = TreeNode(val=9, left=None, right=None)
y = Solution()
z = y.inorderTraversal(x)
print(z)
