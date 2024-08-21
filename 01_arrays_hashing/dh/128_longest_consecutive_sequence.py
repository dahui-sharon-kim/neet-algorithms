# https://leetcode.com/problems/longest-consecutive-sequence/description/

from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        ans = 0

        for num in num_set:
            # Only start counting if it's the beginning of a sequence
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1
                
                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1
                
                ans = max(ans, current_streak)
        
        return ans
