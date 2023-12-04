inp = open("d2.inp", "r")
sm = 0
for x in inp:
    game_number = int(x.split(":")[0].split("Game ")[1])
    x1 = x.replace(f'Game {game_number}: ', '')
    x1 = x1.split(';')
    # print(x1)
    possible = True
    for val in x1:
        v = val.split(",")
        red = 0
        blue = 0
        green = 0
        for color in v:
            # print(color)
            if 'blue' in color:
                blue = int(color.split("blue")[0])
            elif 'red' in color:
                red = int(color.split("red")[0])
            elif 'green' in color:
                green = int(color.split("green")[0])
        # print(f"red={red}")
        # print(f"blue={blue}")
        # print(f"green={green}")
        # print("\n")
        if red>12 or green>13 or blue>14:
            possible = False
            break
    print(possible)
    if possible:
        sm = sm + game_number
print(sm)
