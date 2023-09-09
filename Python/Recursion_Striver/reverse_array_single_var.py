new_arr = []

# n = len(arr)
def swap(arr, i, n):
    temp = arr[i]
    arr[i] = arr[n]
    arr[n] = temp

def rev(arr, i):
    if i>=n/2:
        return arr
    swap(arr, i, n-i)
    return rev(arr, i+1)


arr = [5, 4, 3, 2, 1]
n = len(arr) - 1
print(rev(arr, 0))
# rev(arr, n)
