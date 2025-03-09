from typing import List


class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        for fruit in fruits:
            ind = 0
            for basket in baskets:
                if basket >= fruit:
                    baskets.pop(ind)
                    break
                ind = ind + 1
        return len(baskets)


fruits = [3, 6, 1]
baskets = [6, 4, 7]
obj = Solution()
un = obj.numOfUnplacedFruits(fruits, baskets)
print(un)
