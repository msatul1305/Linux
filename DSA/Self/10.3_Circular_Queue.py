class Queue:
    def __init__(self, n):
        self.q = [None] * n
        self.n = n
        self.front = -1
        self.back = -1

    def enqueue(self, e):
        if self.back == self.front - 1:
            print("Overflow")
        elif self.back == self.n - 1 and self.front == 0:
            print("Overflow")
        else:
            if self.front == -1:
                self.front = 0
            if self.back == self.n - 1 and self.front != 0:
                self.back = 0
            else:
                self.back = self.back + 1
            self.q[self.back] = e

    def dequeue(self):
        if self.front == self.back and self.front != -1:
            self.front = self.back = -1
        elif self.front == self.n - 1:
            self.front = 0
        elif self.front == self.back:
            print("Underflow")
        else:
            self.front = self.front + 1

    def __str__(self):
        if self.front <= self.back:
            return str(self.q[self.front:self.back + 1])
        elif self.front > self.back:
            return str(self.q[self.front:self.n] + self.q[:self.back+1])


q = Queue(3)
q.enqueue(1)
print(q)
q.enqueue(2)
print(q)
q.enqueue(3)
print(q)
q.enqueue(4)
print(q)
q.dequeue()
print(q)
q.enqueue(3)
print(q)
q.enqueue(4)
print(q)
q.dequeue()
print(q)
q.dequeue()
print(q)
q.dequeue()
print(q)
q.dequeue()
print(q)
