# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        min_price = float("inf")
        max_profit = 0
        for day_index, price in enumerate(prices):
            price = min(price, min_price)
            max_profit = max(max_profit, price - min_price)
        return max_profit
