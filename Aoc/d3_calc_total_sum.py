import re

inp = open("d3_updated.inp", "r")
# inp = open("d3_updated.inp", "r")
sum = 0
i = 0
d = {}
for y in inp:
    # print(y)
    pattern = r'[^a-zA-Z0-9.\s]'
    clean_string = re.sub(pattern, '.', y)
    # print(clean_string)
    clean_string = clean_string.split(".")
    # print(clean_string)
    for x in clean_string:
        if x.isdigit():
            sum = sum + int(x)
    # print(f'row {i+1} sum: {sum}')
    d[i+1] = sum
    i = i + 1
print(sum)
output = 601371 - 62835
print(output)  # 5538536 - too high
# row1_sum = 4495
# row2_sum = 3495
# print(row1_sum + row2_sum)
# print(d)
i = 2
d1 = {1: d[1]}
while i <= 140:
    d1[i] = d[i] - d[i-1]
    i = i + 1
print(d1)
