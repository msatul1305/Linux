from typing import List

from Interview.aqr_capital.dp import max_score


class Solution:
    def maxSum(self, nums: List[int]) -> int:
        used = []
        max_sum = 0
        for elem in nums:
            if elem >=0 and elem not in used:
                max_sum = max_sum + elem
                used.append(elem)
        if len(used) == 0:
            return sorted(nums)[-1]
        return max_sum

nums = [-20, 20]
obj = Solution()
x = obj.maxSum(nums)
print(x)
