import sys
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        filtered = set(nums)
        result = 0

        for num in filtered:
            length = 1
            while (num + length) in filtered:
                length += 1
            result = max(result, length)
        return result


if __name__ == "__main__":
    nums = list(map(int, sys.argv[1:]))
    print(Solution().longestConsecutive(nums))
