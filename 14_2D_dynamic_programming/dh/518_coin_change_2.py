# https://leetcode.com/problems/coin-change-ii/description/

from typing import List

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1 

        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] += dp[x - coin]
        return dp[amount] 


print(Solution().change(5, [1,2,5])) # 4
print(Solution().change(3, [2])) # 0
print(Solution().change(10, [10])) # 1
