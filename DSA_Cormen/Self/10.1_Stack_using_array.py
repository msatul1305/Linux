class Stack:
    def __init__(self, size=100):
        self.stack = []
        self.top = -1
        self.size = size

    def __repr__(self):
        return str(self.stack)

    def push(self, element):
        if self.top == self.size:
            raise RuntimeError("Stack Overflow")
        else:
            self.top = self.top + 1
            self.stack.insert(self.top, element)

    def pop(self):
        if self.top == -1:
            raise RuntimeError("Stack underflow.")
        else:
            self.top = self.top - 1
            self.stack.pop()


x = Stack()
x.push(1)
x.push(2)
x.push(3)
x.pop()
print(x)
