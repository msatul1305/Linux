# inp = ["5", "Alice Bob Cacey Deepak Emma", "10 14", "11 12", "10 15", "12 16", "14 16"]
# inp = ["3", "Neil Angel Alok", "1 10", "7 9", "7 10"]
inp = ['2', '15 16 1 Janet', '16 18 0 ', '18 20 1 Cody']
names = inp[1].split()
pairs = inp[2:]

data_dict = {}
for i, name in enumerate(names):
    key, value = map(int, pairs[i].split())
    data_dict[name] = (key, value)

values = inp[2:2+int(inp[0])]
output = []
x = []
for val in values:
    x.append(int(val.split(" ")[0]))
    x.append(int(val.split(" ")[1]))
y = list(set(x))
y.sort()
lis = [f'{inp[0]}']
for k in range(len(y)-1):
    # print(y[k], y[k+1], end='')
    op1 = f'{y[k]} {y[k+1]}'
    count = 0
    names = []
    for key, val in data_dict.items():
        if val[0] <= y[k] and val[1] >= y[k+1]:
            count = count + 1
            names.append(key)
            names.sort()
    # print(' ', count, names)
    listToStr = ' '.join([str(elem) for i, elem in enumerate(names)])
    op2 = f'{count} {listToStr}'
    op = f'{op1} {op2}'
    lis.append(op)
print(lis)
