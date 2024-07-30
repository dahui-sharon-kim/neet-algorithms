from typing import List
import sys


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for idx, num in enumerate(nums):
            try:
                second = nums.index(target - num, idx + 1)
                return [idx, second]
            except ValueError:
                continue
        raise ValueError("Not exist.")


if __name__ == "__main__":
    target = int(sys.argv[1])
    nums = list(map(int, sys.argv[2:]))
    s = Solution()
    print(s.twoSum(nums, target))
