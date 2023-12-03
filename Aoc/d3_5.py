f = "d3.inp"
# f = "sample.inp"
# rows = 10
# cols = 10
inp = open(f, "r")
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
        if val != '.' and not val.isdigit() and i<140 and j<140:
            symbol = val
            # print(symbol)
            index_of_symbol = (i, j)
            # print(index_of_symbol)
            eligible_indices.append((i-1, j-1))
            eligible_indices.append((i-1, j))
            eligible_indices.append((i-1, j+1))
            eligible_indices.append((i, j-1))
            eligible_indices.append((i, j+1))
            eligible_indices.append((i+1, j-1))
            eligible_indices.append((i+1, j))
            eligible_indices.append((i+1, j+1))
        j = j + 1
    i = i + 1
print(eligible_indices)
# for items in eligible_indices:
#     print(items)
row = 0
col = 0
file_content = ''
with open(f, "r") as file:
    file_content = file.read()
file_content = file_content.split("\n")
# print(file_content)
sm = 0
new_file_content = ''
current_num = False
for i in range(rows):
    new_file_content += f'{i+1}: '
    for j in range(cols):
        # print(file_content[i][j])
        if file_content[i][j].isdigit():
            sm = sm*10 + int(file_content[i][j])
        if (i, j) not in eligible_indices:
            new_file_content += f'0'
        else:
            new_file_content+=f'{file_content[i][j]}'
            current_num = True
    new_file_content+='\n'
print(new_file_content)
# ans = 850 + 329 + 13 + 871 + 816 + 697 +
#       53 + 497 + 906 + 735 + 68 + 68 +
#       132 + 
# # new_file_content = new_file_content.split('\n')
# # print(new_file_content)
# new_file_content2 = ''
# for i in range(rows):
#     for j in range(cols):
#         if new_file_content[i][j].isdigit() and j>0 and j<14:
#             new_file_content2+= file_content[i][j-1]
#             new_file_content2+= file_content[i][j+1]
#         else:
#             new_file_content2[i][j] = new_file_content[i][j]
# print(new_file_content2)

