inp = open("sample_3.inp", "r")
rows = 10
cols = 10
eligible_indices = [[(0, 2), (0, 3), (0, 4), (1, 2), (1, 4), (2, 2), (2, 3), (2, 4)],
                    [(2, 5), (2, 6), (2, 7), (3, 5), (3, 7), (4, 5), (4, 6), (4, 7)],
                    [(3, 2), (3, 3), (3, 4), (4, 2), (4, 4), (5, 2), (5, 3), (5, 4)],
                    [(4, 4), (4, 5), (4, 6), (5, 4), (5, 6), (6, 4), (6, 5), (6, 6)],
                    [(7, 2), (7, 3), (7, 4), (8, 2), (8, 4), (9, 2), (9, 3), (9, 4)],
                    [(7, 4), (7, 5), (7, 6), (8, 4), (8, 6), (9, 4), (9, 5), (9, 6)]]
print(eligible_indices)
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
            print(f'{row_num}, {start}, {end - 1}')
            indices_of_values.append((row_num, start, end - 1))
        i = i + 1
    row_num = row_num + 1
print(indices_of_values)
for val in indices_of_values:
    if val[1]:
        print()
