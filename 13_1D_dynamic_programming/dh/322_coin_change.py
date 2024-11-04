# https://leetcode.com/problems/coin-change/description/

from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for i in range(coin, amount+1):
                dp[i] = min(dp[i], dp[i-coin]+1)
        
        return dp[-1] if dp[-1] != amount+1 else -1


print(Solution().coinChange([1,2,5], 11)) # 3 (5 + 5 + 1)
print(Solution().coinChange([2], 3)) # -1
print(Solution().coinChange([1], 0)) # 0
