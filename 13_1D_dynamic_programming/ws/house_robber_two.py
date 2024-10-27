from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(numbers):
            first, second = 0, 0
            for n in numbers:
                temp = max(n + first, second)
                first = second
                second = temp
            return second

        return max(nums[0], helper(nums[1:]), helper(nums[:-1]))
