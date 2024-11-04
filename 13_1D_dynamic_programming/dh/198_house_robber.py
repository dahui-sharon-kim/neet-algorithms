# https://leetcode.com/problems/house-robber/

from typing import List

class Solution:
    # 연달아 두 집을 털 수는 없음
    def rob(self, nums: List[int]) -> int:
        length = len(nums)
        money = [0] * (length + 1)
        money[1] = nums[0]

        for i in range(2, length+1):
            money[i] = max(money[i-1], money[i-2] + nums[i-1])
        
        return money[-1]
        
print(Solution().rob([1,2,3,1])) # 4
print(Solution().rob([2,7,9,3,1])) # 12
print(Solution().rob([1,0,2,4])) # 5
