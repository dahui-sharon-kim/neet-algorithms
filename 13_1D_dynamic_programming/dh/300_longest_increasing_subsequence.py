# https://leetcode.com/problems/longest-increasing-subsequence/description/

from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        length = len(nums)
        LIS = [1] * length

        for i in range(length-1, -1, -1):
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])

        return max(LIS)

print(Solution().lengthOfLIS([1,2,4,3])) # 3
print(Solution().lengthOfLIS([10,9,2,5,3,7,101,18])) # 4 (2,3,7,101) / (2,3,7,18)
print(Solution().lengthOfLIS([0,1,0,3,2,3])) # 4
print(Solution().lengthOfLIS([7,7,7,7,7,7,7])) # 1
print(Solution().lengthOfLIS([4,10,4,3,8,9])) # 3
