# list n, chunk size c
# output = list of list
# 10 -> 2*5, 11 -> 2*6
l =[1,2,3,4,5,6,7,8,9,10,11]
x = {}
c = 5
def f(l, ini, fin):
        return l[ini: fin]
ini = 0
fin = 5
while fin<len(l):
    print(f(l, ini, fin))
    ini = fin
    fin = fin + c
if ini<len(l):
    print(l[ini:len(l)])

# s1 = 'radar'
# s2 = 'drara'
# # a -2

# iter

# class A:
#     def __init__(self, __x):
#         pass
# class B(A):
#     def __init__(self, x):
#         super.__init__(x)
#         pass
#
# obj = B(1)

# T -> tid, cid, pid, amount
# C -> cid, cname, city
# P -> pid, pname
#
# # for city, those products total amount>500
# select sum(amount)>500 from T, C, P
# where T.pid = P.pid group by C.city
# inner join on T.pid = P.pid and  T.cid = C.cid
#
# # products never sold in past
# select P.id from P, T
# where T.tid = Null
# inner join on T.pid = P.pid
