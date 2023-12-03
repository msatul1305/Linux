inp = open("sample_3.inp", "r")
rows = 10
cols = 10

array = [[0 for _ in range(cols)] for _ in range(rows)]
i = 0
for x in inp:
    y = x.split('\n')[0]
    j = 0
    for z in y:
        array[i][j] = z
        j = j + 1
    i = i + 1
indices_of_values = []
row_num = 0
for row in array:
    # print(row)
    start = 0
    end = 0
    i = 0
    while i < len(row):
        # print(row[i])
        if f'{row[i]}'.isdigit():
            # print(row[i])
            start = i
            while f'{row[i]}'.isdigit():
                i = i + 1
                end = i
                if not f'{row[i]}'.isdigit():
                    break
            print(f'{row_num}, {start}, {end-1}')
            indices_of_values.append((row_num, start, end-1))
        i = i + 1
    row_num = row_num + 1
print(indices_of_values)
