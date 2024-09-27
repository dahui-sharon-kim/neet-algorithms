from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = [[]]

        for n in nums:
            perms = []
            for p in res:
                for i in range(len(p) + 1):
                    copy = p.copy()
                    copy.insert(i, n)
                    perms.append(copy)
            res = perms

        return res
