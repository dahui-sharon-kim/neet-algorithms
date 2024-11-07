# https://leetcode.com/problems/house-robber-ii/description/

from typing import List

class Solution:
    # 연달아 두 집을 털 수는 없고 첫 번쨰 집과 마지막 집은 서로 이웃임.
    def helper(self, nums: List[int]) -> int:
        length = len(nums)
        money = [0] * (length + 1)
        money[1] = nums[0]

        for i in range(2, length+1):
            money[i] = max(money[i-1], money[i-2] + nums[i-1])
        
        return money[-1]

    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(self.helper(nums[1:]), self.helper(nums[:-1]))
        
print(Solution().rob([2,3,2])) # 3
print(Solution().rob([1,2,3,1])) # 4
print(Solution().rob([1,2,3])) # 3
print(Solution().rob([0])) # 3
