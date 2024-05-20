n1 = int(input())
for n in range(n1):
    x, y = input().split()
    x = int(x)
    y = int(y)
    # print(f"x={x}")
    # print(f"y={y}")
    sy = int(y/2) + (y%2)
    # print(f"sy={sy}")
    left_space = 15*sy - 4*y
    # print(f"left_space={left_space}")
    if left_space>=x: #15,0; 8,2
        print(sy)
        # print("case1")
    else:
        if (left_space-x) % 15 !=0:
            print(sy+int(abs((left_space-x)/15))+1)
        else:
            print(sy+int(abs((left_space-x)/15)))
        # print("c2")
