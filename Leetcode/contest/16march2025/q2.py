from typing import List


def find_min_dis(base_index, pos_indices, neg_indices, siz):
    distances = []
    distances_pos = []
    distances_neg = []
    for k in pos_indices:
        distances_pos.append(abs(k - base_index))
    for k in neg_indices:
        distances_neg.append(abs(k - base_index))
        distances_neg.append(2*siz - base_index + k)
    distances = distances_pos + distances_neg
    if not distances:
        return -1
    return min(distances)

def find_all(nums, num, curr):
    return [i for i, e in enumerate(nums) if e == num and i!=curr]


class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        res = []
        for i in queries:
            positive_indices_found = find_all(nums, nums[i], i)
            negative_indices = [i - len(nums) for i in positive_indices_found]
            res.append(find_min_dis(i, positive_indices_found, negative_indices, len(nums)))
        return res

obj = Solution()
nums = [1,3,1,4,1,3,2]
queries = [0,3,5]
print(obj.solveQueries(nums, queries))
