target = 2
nums = [1, 3, 4, 5]

if target in nums:
    print(nums.index(target))
else:
    for i in range(len(nums)):
        if nums[i] > target:
            print(i)
            break
