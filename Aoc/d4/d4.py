inp = open("d4.inp", "r")
# inp = open("sample.inp", "r")
sum = 0
for x in inp:
    # print(x)
    y = x.split(": ")[1].strip()
    my_nums = y.split("|")[0].strip().split(" ")
    my_nums = [item for item in my_nums if item != '']
    winning_nums = y.split("|")[1].strip().split(" ")
    winning_nums = [item for item in winning_nums if item != '']
    print(f'my_nums: {my_nums}')
    print(f'winning_nums: {winning_nums}')
    card_score = 0
    for val in my_nums:
        if val in winning_nums:
            if card_score == 0:
                card_score = 1
            else:
                card_score = card_score*2
    print(f"card_score={card_score}")
    sum = sum + card_score
print(sum)

# 18619
