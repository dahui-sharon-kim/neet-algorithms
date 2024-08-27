import sys
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            print(nums[left], nums[mid], nums[right])

            if target == nums[mid]:
                return mid

            if nums[left] <= nums[mid]:
                if nums[mid] < target or target < nums[left]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if target < nums[mid] or target > nums[right]:
                    right = mid - 1
                else:
                    left = mid + 1
        return -1


if __name__ == "__main__":
    target = int(sys.argv[1])
    nums = list(map(int, sys.argv[2:]))
    print(Solution().search(nums, target))
