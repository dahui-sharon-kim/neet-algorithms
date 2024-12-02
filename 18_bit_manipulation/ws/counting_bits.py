from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0 for _ in range(n + 1)]
        for i in range(1, n + 1):
            tmp = i
            num = 0
            while tmp:
                num += 1 if tmp & 1 else 0
                tmp >>= 1
            res[i] = num
        return res
