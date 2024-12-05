# https://leetcode.com/problems/counting-bits/description/

from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0] * (n + 1)

        for i in range(1, n + 1):
            res[i] = res[i >> 1] + (i & 1)  # DP
        
        return res

print(Solution().countBits(2))  # [0,1,1]
print(Solution().countBits(5))  # [0,1,1,2,1,2]
