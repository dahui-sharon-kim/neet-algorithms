# https://leetcode.com/problems/partition-equal-subset-sum/

from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        summed = sum(nums)
        if summed % 2:
            return False
        
        target = summed // 2 
        dp = [False] * (target+1)
        dp[0] = True


        for num in nums: 
            for j in range(target, num-1, -1): 
                if dp[j-num]:
                    dp[j] = True 
            
            if dp[target]:
                return True
        
        return dp[target]
            

print(Solution().canPartition([1,5,4,7,5])) # true
print(Solution().canPartition([1,2,3,5])) # false
