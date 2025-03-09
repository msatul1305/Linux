from typing import List


class Solution:
    def findMaxSum(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        # curr = 0
        j = 0
        dic = {0: []}
        curr_index = 0
        for num in nums1:
            curr = 0
            while curr < len(nums1):
                if nums1[curr] < num:
                    if curr_index not in dic.keys():
                        dic.update({curr_index: []})
                    dic[curr_index].append(curr)
                curr = curr + 1
            curr_index = curr_index + 1
        print()
        op = []
        for i in range(len(nums2)):
            sub_arr = []
            if i in dic.keys():
                for x in dic[i]:
                    sub_arr.append(nums2[x])
                print()
            else:
                sub_arr = [0]
            sub_arr.sort()
            sm = 0
            for i in range(k):
                if len(sub_arr) - i - 1 >= 0:
                    sm = sm + sub_arr[len(sub_arr) - i - 1]
            op.append(sm)
        print()
        return op


nums1 = [2, 2, 2, 2]
nums2 = [3, 1, 2, 3]
k = 1
obj = Solution()
x = obj.findMaxSum(nums1, nums2, k)
print(x)
