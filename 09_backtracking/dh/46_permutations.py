# https://leetcode.com/problems/permutations/
from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms = [[]]
        for n in nums:
            new_perms = []
            for p in perms:
                for i in range(len(p)+1):
                    p_copy = p.copy()
                    p_copy.insert(i, n)
                    new_perms.append(p_copy)
            perms = new_perms
        return perms
    
        # if len(nums) == 0:
        #     return [[]]
        # perms = self.permute(nums[1:])
        # res = []

        # for p in perms:
        #     for i in range(len(p)+1): # i를 끼워넣을 수 있는 공간들 [^2^3^]
        #         p_copy = p.copy()
        #         p_copy.insert(i, nums[0])
        #         res.append(p_copy)
        
        # return res
            

print(Solution().permute([1,2,3])) # [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
print(Solution().permute([0,1])) # [[0,1],[1,0]]
print(Solution().permute([1])) # [[1]]