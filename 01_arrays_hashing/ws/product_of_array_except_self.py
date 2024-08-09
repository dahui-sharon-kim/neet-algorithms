from collections import defaultdict
import sys
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1 for _ in nums]

        for i in range(1, len(nums)):
            res[i] *= res[i - 1] * nums[i - 1]

        mul = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= mul
            mul *= nums[i]

        return res


if __name__ == "__main__":
    nums = list(map(int, sys.argv[1:]))
    print(Solution().productExceptSelf(nums))
