new_arr = []


def rev(arr, a, b):
    if a == b:
        return arr
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = temp
    return rev(arr, a+1, b-1)


arr = [5, 4, 3, 2, 1]
n = len(arr) - 1
print(rev(arr, 0, n))
# rev(arr, n)
