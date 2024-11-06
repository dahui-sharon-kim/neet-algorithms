from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        seq = [1] * len(nums)

        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    seq[i] = max(seq[i], 1 + seq[j])
        return max(seq)
