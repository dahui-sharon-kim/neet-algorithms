from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}

        def dfs(i, buy):
            if i >= len(prices):
                return 0

            if (i, buy) in dp:
                return dp[(i, buy)]

            cooldown = dfs(i + 1, buy)
            if buy:
                buy_price = dfs(i + 1, not buy) - prices[i]
                dp[(i, buy)] = max(cooldown, buy_price)
            else:
                sell_price = dfs(i + 2, not buy) + prices[i]
                dp[(i, buy)] = max(cooldown, sell_price)
            return dp[(i, buy)]

        return dfs(0, True)
