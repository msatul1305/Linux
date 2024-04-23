class Node:
    def __init__(self):
        self.p = None
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = Node()

    # def insert_left(self, val):
    #     temp = Node()
    #     temp.p = val
    #     curr = self.root
    #     if curr.left is None:
    #         curr.left = temp
    #     else:
    #         while curr.left is not None:
    #             curr = curr.left
    #         curr.left = temp
    #
    # def insert_right(self, val):
    #     temp = Node()
    #     temp.p = val
    #     curr = self.root
    #     if curr.right is None:
    #         curr.right = temp
    #     else:
    #         while curr.right is not None:
    #             curr = curr.right
    #         curr.right = temp
    def insert(self, l=None, r=None):
        curr = self.root
        while curr.left:
            curr = curr.left
        if l:
            curr.left = Node()
            # curr = curr.left
            curr.left.p = l
        else:
            curr.left = None
        if r:
            curr.right = Node()
            # curr = curr.right
            curr.right.p = r
        else:
            curr.right = None

    def display(self):
        curr = self.root
        while curr:
            if curr.left:
                print(curr.left.p)
            if curr.right:
                print(curr.right.p)
            curr = curr.left


t = Tree()
t.insert(1, 2)
# t.insert(None, 10)
t.insert(3, 4)
t.insert(5)
t.insert(6, 7)
t.insert(9)
t.display()
