class Class:
    def __init__(self):
        self.num=100
class Normal(Class):
    def __init__(self):
        super.__init__()
        self.var=200
class Sub(Normal):
    def __init__(self, val, num):
        self.val=val
        self.num=num
child=Sub('100', '200')
print(child.num, child.val)
