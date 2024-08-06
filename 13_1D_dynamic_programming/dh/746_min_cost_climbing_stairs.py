from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        
        if n == 0:
            return 0
        elif n == 1:
            return cost[0]
        
        dp = [0] * n
        dp[0] = cost[0]
        dp[1] = cost[1] # index 0, 1은 initalize한다
        
        for i in range(2, n):
            dp[i] = cost[i] + min(dp[i-1], dp[i-2])
        
        return min(dp[n-1], dp[n-2])
