# inp = open("d4.inp", "r")
fil = "d4.inp"
inp = open(fil, "r")
sm = 0
lines = sum(1 for _ in open(fil))
d = {i: 1 for i in range(1, lines+1)}
d[0] = 1
no_of_copies = []
for x in inp:
    # print(x)
    x = x.replace("  ", " ")
    y = x.split(": ")[1].strip()
    current_card_num = int(x.split(':')[0].split(" ")[1])
    my_nums = y.split("|")[0].strip().split(" ")
    my_nums = [item for item in my_nums if item != '']
    winning_nums = y.split("|")[1].strip().split(" ")
    winning_nums = [item for item in winning_nums if item != '']
    # print(f'my_nums: {my_nums}')
    # print(f'winning_nums: {winning_nums}')
    winning_numbers_count = 0
    for val in my_nums:
        if val in winning_nums:
            winning_numbers_count = winning_numbers_count + 1
    print(f'card {current_card_num} => winning_numbers_count: {winning_numbers_count}')
    # sm = sm + matching*d[i]
    i = current_card_num + 1
    while i < current_card_num + winning_numbers_count + 1 and i < lines:
        d[i] = d[i] + 1 * d[current_card_num]
        i = i + 1
    # for i in range(current_card_num + 1, current_card_num + matching + 1):
    print()
    # sm = sm + card_score
for val in d.values():
    sm = sm + val
print(d)
print(f'final sm={sm - 1}')  # 8054116 = too low
# 18619
