from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        
        jumps = 0
        current_end = 0
        maximum = 0
        
        for i in range(len(nums) - 1):
            maximum = max(maximum, i + nums[i])
            
            if i == current_end:
                jumps += 1
                current_end = maximum
                
                if current_end >= len(nums) - 1:
                    break
        
        return jumps

print(Solution().jump([2, 3, 1, 1, 4]))  # 2