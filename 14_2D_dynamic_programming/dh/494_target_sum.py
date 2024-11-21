# https://leetcode.com/problems/target-sum/description/

from typing import List

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        offset = sum(nums) # sum은 최소 -offset 최대 offset까지 가능
        dp = [[0] * (2 * offset + 1) for _ in range(len(nums) + 1)]
        
        dp[0][offset] = 1  # Base case: sum of 0 with no elements
        
        for i in range(1, len(nums) + 1):
            for j in range(2 * offset + 1):
                if dp[i - 1][j] != 0:  # Only proceed if there's a way to achieve this sum
                    current_num = nums[i - 1]
                    
                    # Adding the number
                    if j + current_num <= 2 * offset:
                        dp[i][j + current_num] += dp[i - 1][j]
                    
                    # Subtracting the number
                    if j - current_num >= 0:
                        dp[i][j - current_num] += dp[i - 1][j]
        
        # The target sum is located at dp[len(nums)][target + offset]
        return dp[len(nums)][target + offset] if -offset <= target <= offset else 0

print(Solution().findTargetSumWays([1,1,1,1,1], 3)) # 5
print(Solution().findTargetSumWays([1], 1)) # 1
