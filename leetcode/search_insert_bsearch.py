nums = [1, 3, 5, 6]
target = 7


def f(nums, target):
    # binary search
    l = len(nums)
    low = 0
    high = l
    mid = (low + high) // 2
    while low < high:
        if nums[mid] < target:
            low = mid + 1
        elif nums[mid] > target:
            high = mid - 1
        elif nums[mid] == target:
            return mid
        mid = (low + high) // 2
    return low


print(f(nums, target))
