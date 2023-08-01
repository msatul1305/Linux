class Queue:
    def __init__(self, n):
        self.q = []
        self.n = n
        self.front = -1
        self.back = -1

    def push(self, e):
        if self.back == self.n:
            print("Overflow")
        else:
            if self.front == -1:
                self.front = 0
            self.back = self.back + 1
            self.q.insert(self.back, e)

    def pop(self):
        if self.front == self.back and self.front != -1:
            self.front = self.back = -1
        elif self.front == -1:
            print("Underflow")
        else:
            if self.back == 0:
                self.back = -1
            self.front = self.front + 1

    def __str__(self):
        return str(self.q[self.front:self.back + 1])


q = Queue(2)
q.push(1)
print(q)
q.push(2)
print(q)
q.pop()
print(q)
q.push(3)
print(q)
q.push(4)
print(q)
q.pop()
print(q)
q.pop()
print(q)
q.pop()
print(q)
