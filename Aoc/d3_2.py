inp = open("d3.inp", "r")
rows = 140
cols = 140

# array = [[0 for _ in range(cols)] for _ in range(rows)]
i = 0
eligible_indices = []
for x in inp:
    indexes = []
    y = x.split('\n')[0]
    # print(y)
    j = 0
    for val in y:
        # print(val)
        current_index = (i, j)
        if val != '.' and not val.isdigit():
            symbol = val
            # print(symbol)
            index_of_symbol = (i, j)
            # print(index_of_symbol)
            eligible_indices.append((i - 1, j - 1))
            eligible_indices.append((i - 1, j))
            eligible_indices.append((i - 1, j + 1))
            eligible_indices.append((i, j - 1))
            eligible_indices.append((i, j + 1))
            eligible_indices.append((i + 1, j - 1))
            eligible_indices.append((i + 1, j))
            eligible_indices.append((i + 1, j + 1))
        j = j + 1
    i = i + 1
# for items in eligible_indices:
#     print(items)
row = 0
col = 0
file_content = ''
with open("d3.inp", "r") as file:
    file_content = file.read()
file_content = file_content.split("\n")
# print(file_content)
new_file_content = ''
for i in range(rows):
    for j in range(cols):
        # print(file_content[i][j])
        if (i, j) in eligible_indices:
            new_file_content += f'A'
        else:
            new_file_content += f'{file_content[i][j]}'
    new_file_content += '\n'
print(new_file_content)
# inp = open("sample_3.inp", "r")
# i = 0
# for x in inp:
#     indexes = []
#     y = x.split('\n')[0]
#     print(y)
#     j = 0
#     start = 0
#     end = 0
#     for val in y:
#         print(val)
#         if val.isdigit():
#             start = j
#         else:
#             end = j - 1
#         print(start, end)
#         j = j + 1
#     i = i + 1
# ans = 850 + 329 + 13 + 871 + 816 + 697 +
# 53 + 497 + 906 + 735 + 68 + 68 +
# 132 + 844 + 875 + 350 + 336 + 649 +
# 726 + 341 + 358 + 244 + 57 + 738 + 663 + 584 +
# 952 +
# rev_ans =
