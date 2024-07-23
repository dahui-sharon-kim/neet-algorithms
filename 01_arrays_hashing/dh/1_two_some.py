from typing import List

# https://leetcode.com/problems/two-sum/description/

# Brute-force: O(n^2)
#
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         length = len(nums)

#         for i in range(length - 1):
#             for j in range(i+1, length):
#                 if (nums[i] + nums[j] == target):
#                     return [i, j]

# Hash table
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_index = {}
        
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_to_index:
                return [num_to_index[complement], i]
            num_to_index[num] = i

print(Solution().twoSum([2, 7, 11, 15], 9)) # Output: [0, 1]