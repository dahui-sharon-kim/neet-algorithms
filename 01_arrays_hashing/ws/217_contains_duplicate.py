from typing import List
import sys


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))


if __name__ == "__main__":
    nums = list(map(int, sys.argv[1:]))
    s = Solution()
    print(s.hasDuplicate(nums))
