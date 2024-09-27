# https://leetcode.com/problems/combination-sum-ii/

from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        temp = []

        def helper(i):
            if sum(temp) == target:
                ans.append(temp.copy())
                return
            if i >= len(candidates) or sum(temp) > target:
                return
            
            temp.append(candidates[i])
            helper(i+1)
            temp.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            helper(i+1)

        helper(0)
        return ans

print(Solution().combinationSum2([10,1,2,7,6,1,8],8)) #[[1,1,6],[1,7],[2,6],[8]]
print(Solution().combinationSum2([2,5,2,1,2],5)) # [[1,2,2],[5]]