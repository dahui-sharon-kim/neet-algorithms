# https://leetcode.com/problems/combination-sum/description/

from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        cur_combination = []

        def dfs(i):
            if sum(cur_combination) == target:
                res.append(cur_combination.copy())
                return
            if sum(cur_combination) > target or i >= len(candidates):
                return

            cur_combination.append(candidates[i])
            dfs(i)
            cur_combination.pop()
            dfs(i+1)
        
        dfs(0)
        return res

print(Solution().combinationSum([2,3,6,7], 7)) # [[2,2,3],[7]]
print(Solution().combinationSum([2,3,5], 8)) # [[2,2,2,2],[2,3,3],[3,5]]
print(Solution().combinationSum([2], 1)) # []
