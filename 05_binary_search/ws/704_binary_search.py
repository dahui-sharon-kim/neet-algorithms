import sys
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            idx = left + int((right - left) / 2)
            if nums[idx] == target:
                return idx
            elif nums[idx] < target:
                left = idx + 1
            elif nums[idx] > target:
                right = idx - 1
        return -1


if __name__ == "__main__":
    target = int(sys.argv[1])
    nums = list(map(int, sys.argv[2:]))
    print(Solution().search(nums, target))
