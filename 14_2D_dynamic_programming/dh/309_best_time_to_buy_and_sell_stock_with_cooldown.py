# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/description/

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        length = len(prices)

        if length == 1:
            return 0

        hold = [0] * length # day i에 보유하고 있음: 그 전날부터 보유하고 있거나 오늘 산 경우
        not_hold = [0] * length # day i에 보유하고 있지 않음: 그 전날부터 보유하고 있지 않았거나 어제 판 경우
        cooldown = [0] * length # just sold


        hold[0] = -prices[0]
        
        for i in range(1, length):
            hold[i] = max(hold[i-1], not_hold[i-1] - prices[i])
            not_hold[i] = max(not_hold[i-1], cooldown[i-1])
            cooldown[i] = hold[i-1] + prices[i]
        
        return max(not_hold[length-1], cooldown[length-1])

print(Solution().maxProfit([1,2,3,0,2])) # 3
print(Solution().maxProfit([1])) # 0
