def min(arr1, arr2):
    l = len(arr1)
    abs_diff = []
    for i in range(l):
        digits_a = [int(digit) for digit in str(arr1[i]) if digit.isdigit()]
        digits_b = [int(digit) for digit in str(arr2[i]) if digit.isdigit()]
        print(digits_a)
        print(digits_b)
        abs_diff.append(sum(abs(x - y) for x, y in zip(digits_a, digits_b)))
        print("abs_diff=", abs_diff)
    abs_diff = sum(abs_diff)
    return abs_diff


arr1 = [2468]
arr2 = [8642]
print(min(arr1, arr2))
