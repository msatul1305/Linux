# inp = open("d5.inp", "r")
inp = open("sample.inp", "r")
i = 0
for x in inp:
    print(x)
    if i == 0:
        seeds = x.split("seeds: ")[1].split(" ")
        print(seeds)

    i = i + 1
