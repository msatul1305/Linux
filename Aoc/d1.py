inp = open("sample.inp", "r")
# inp = open("d1.inp", "r")
sum = 0
for x in inp:
    first = 0
    last = 0
    x1 = x[::-1]
    print(f'x={x}')
    for ch in x:
        if ch.isdigit():
            first = ch
            break
    for ch in x1:
        if ch.isdigit():
            last = ch
            break
    print(int(first), int(last))
    sum = sum + 10*int(first)+ int(last)
print(sum)
