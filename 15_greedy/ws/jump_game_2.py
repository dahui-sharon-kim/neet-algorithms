from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        local_max = 0
        cur = 0
        count = 0
        for i in range(len(nums) - 1):
            local_max = max(local_max, nums[i] + i)
            if i == cur:
                count += 1
                cur = local_max

        return count
