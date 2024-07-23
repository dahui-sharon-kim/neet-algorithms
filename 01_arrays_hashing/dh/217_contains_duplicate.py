from typing import List

# https://leetcode.com/problems/contains-duplicate/description/

# hash table
# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         used_nums = {}
#         for i in nums:
#             if i in used_nums:
#                 return True
#             used_nums[i] = 1
#         return False

# set을 사용
class Solution:
  def containsDuplicate(self, nums: List[int]) -> bool:
    used_nums = set()
    for i in nums:
      if i in used_nums:
        return True
      used_nums.add(i)
    return False
  
print(Solution().containsDuplicate([1,2,3,1])) # Output: True
print(Solution().containsDuplicate([1,2,3,4])) # Output: False
print(Solution().containsDuplicate([1,1,1,3,3,4,3,2,4,2])) # Output: True