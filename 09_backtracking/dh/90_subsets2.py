# https://leetcode.com/problems/subsets-ii/

from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        temp = []
        nums.sort()
        def helper(i):
            if i >= len(nums):
                if temp.copy() in ans:
                    return
                ans.append(temp.copy())
                return
            # nums[i]를 넣기로 한 케이스에서는 nums[i]와 같은 값이 몇 개 있든 nums[i]가 하나라도 있는 모든 케이스를 커버함
            temp.append(nums[i])
            helper(i+1)
            # nums[i]를 넣지 않기로 한 케이스에서는 nums[i]를 하나도 포함하면 안 됨
            popped = temp.pop()
            if (temp and popped == temp[-1]):
                helper(i+2)
            else:
                helper(i+1)
        helper(0)
        return ans

print(Solution().subsetsWithDup([1,1,2,2])) # [[],[1],[1,1],[1,1,2],[1,1,2,2],[1,2],[1,2,2],[2],[2,2]]
print(Solution().subsetsWithDup([4,4,4,1,4])) # [[],[1],[1,4],[1,4,4],[1,4,4,4],[1,4,4,4,4],[4],[4,4],[4,4,4],[4,4,4,4]]
print(Solution().subsetsWithDup([1,2,2])) # [[],[1],[1,2],[1,2,2],[2],[2,2]]
print(Solution().subsetsWithDup([0])) # [[0], []]
