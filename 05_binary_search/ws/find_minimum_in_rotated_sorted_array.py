import sys
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        res = 1001
        while left < right:
            mid = left + (right - left) // 2
            res = min(res, nums[mid])

            if nums[right] < nums[mid]:
                left = mid + 1
            else:
                right = mid - 1

        return min(res, nums[left])


if __name__ == "__main__":
    nums = list(map(int, sys.argv[1:]))
    print(nums)
    print(Solution().findMin(nums))
