inp = open("sample_3.inp", "r")
# for y in inp:
#     for z in y:
        # print(z)
rows = 10
cols = 10
sum = 0
# array = [[0 for _ in range(cols)] for _ in range(rows)]
i = 0
for x in inp:
    indexes = []
    y = x.split('\n')[0]
    print(y)
