inp = open("d1.inp", "r")
# inp = open("d1.inp", "r")
sum = 0
for x in inp:
    first = 0
    last = 0
    first_index = 0
    last_index = 0
    x1 = x[::-1]
    count = 0
    for ch in x:
        count = count + 1
        if ch.isdigit():
            first = ch
            first_index = count
            break
    count = 0
    for ch in x1:
        count = count + 1
        if ch.isdigit():
            last = ch
            last_index = count
            break
    search = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    d = [0,0,0,0,0,0,0,0,0]
    d1 = [0,0,0,0,0,0,0,0,0]
    last_index = len(x) - last_index + 1
    # noinspection PyRedeclaration

    ind = 0
    for p in search:
        d[ind] = x.find(p)
        ind = ind + 1
    ind = 0
    for p in search:
        d1[ind] = x.rfind(p)
        ind = ind + 1
    print(f'x={x}')
    # print(f'd={d}')
    # print(f'd1={d1}')
    count = 0
    valid_nums = [num for num in d if num!=-1]
    min_index = min(valid_nums) if valid_nums else 10000
    if min_index != 10000:
        min_val = d.index(min_index) + 1
    else:
        min_val = 10000
    max_index = max(d1)
    max_value = d1.index(max_index) + 1
    max_index = max_index + 1
    # print(f'first={int(first)}, last={last}')
    # print(f'first_index={int(first_index)}, last_index={int(last_index)}')
    # print(f'min_index={int(min_index)}, max_index={int(max_index)}')
    # print(f'min_val={int(min_val)}, max_val={int(max_value)}')
    if first_index>min_index:
        first = min_val
    if last_index<max_index:
        last = max_value
    print(f'first={int(first)}, last={last}')
    print()
    sum = sum + 10*int(first)+ int(last)
print(sum)
