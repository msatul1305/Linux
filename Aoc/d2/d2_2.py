inp = open("d2.inp", "r")
sm = 0
for x in inp:
    game_number = int(x.split(":")[0].split("Game ")[1])
    x1 = x.replace(f'Game {game_number}: ', '')
    x1 = x1.split(';')
    print(x1)
    min_red = 0
    min_blue = 0
    min_green = 0
    for val in x1:
        v = val.split(",")
        red = 0
        blue = 0
        green = 0
        for color in v:
            if 'blue' in color:
                blue = int(color.split("blue")[0])
            elif 'red' in color:
                red = int(color.split("red")[0])
            elif 'green' in color:
                green = int(color.split("green")[0])
        # print(f"red={red}")
        # print(f"blue={blue}")
        # print(f"green={green}")
        if red > min_red:
            min_red = red
        if blue > min_blue:
            min_blue = blue
        if green > min_green:
            min_green = green
    power_set = min_red*min_green*min_blue
    print(f"min_red={min_red}")
    print(f"min_blue={min_blue}")
    print(f"min_green={min_green}")
    print(f'power_set={power_set}')
    sm = sm + power_set
print(sm)
