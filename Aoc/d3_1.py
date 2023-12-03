import re

inp = open("sample_3.inp", "r")
rows = 10
cols = 10
sum = 0
# array = [[0 for _ in range(cols)] for _ in range(rows)]
i = 0
for x in inp:
    indexes = []
    y = x.split('\n')[0]
    # indexes.append()
    # print(y)
    y = ''.join(y.split('.'))
    print(y)
    pattern = r'[^a-zA-Z0-9\s]'
    y = re.sub(pattern, '', y)
    # print(y)
    for val in y:
        # print(val)
        if val.isdigit():
            sum = sum + int(val)
print(sum)
