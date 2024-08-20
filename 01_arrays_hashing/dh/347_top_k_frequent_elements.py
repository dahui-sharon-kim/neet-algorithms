# https://leetcode.com/problems/top-k-frequent-elements/description/
from typing import List
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_used = defaultdict(int)
        for num in nums:
            nums_used[num] += 1
        sorted_nums = sorted(nums_used.keys(), key=lambda x: nums_used[x], reverse=True)
        return sorted_nums[:k]
