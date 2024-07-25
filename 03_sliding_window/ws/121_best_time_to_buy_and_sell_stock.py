import sys
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        for i in range(len(prices) - 1):
            profit = max(prices[i + 1 :]) - prices[i]
            result = max(result, profit)
        return result


if __name__ == "__main__":
    prices = list(map(int, sys.argv[1:]))
    print(Solution().maxProfit(prices))
