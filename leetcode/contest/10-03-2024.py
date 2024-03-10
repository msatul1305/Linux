apple = [1, 8, 3, 3, 5]
capacity = [3, 9, 5, 1, 9]

# sorted(apple, reverse=True)
apple.sort(reverse=True)
capacity.sort(reverse=True)
print(apple)
print(capacity)

# while i < len(capacity):
j = 0


def return_no_of_boxes(apple, capacity):
    no_of_box = 0
    j = 0
    i = 0
    for i in range(0, len(apple)):
        while apple[i] != 0:
            if capacity[j] >= apple[i]:
                capacity[j] = capacity[j] - apple[i]
                apple[i] = 0
                no_of_box = no_of_box + 1
            else:
                apple[i] = apple[i] - capacity[j]
                capacity[j] = 0
                j = j + 1

    return j + 1


print(return_no_of_boxes(apple, capacity))
