from typing import List
from copy import deepcopy


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        subset = []

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return

            subset.append(nums[i])
            dfs(i + 1)

            subset.pop()
            dfs(i + 1)

        dfs(0)
        return res

    def ineffecient_subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        for i in nums:
            copy = deepcopy(res)
            res.append([])
            for r in res:
                r.append(i)
            res.extend(copy)
        res.append([])
        return res
