nums = [2, 2, 1, 3, 3, 5, 5, 6, 7, 6, 7]

found = []


def f(nums: list):
    for i in range(len(nums)):
        if nums[i] not in found:
            if nums[i] not in nums[i + 1:]:
                    return nums[i]
            else:
                found.append(nums[i])


print(f(nums))
