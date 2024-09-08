import sys
from typing import List


class Solution:
    def maxArea(self, heights: List[int]) -> int:
        result = 0

        left, right = 0, len(heights) - 1

        while left < right:
            area = min(heights[left], heights[right]) * (right - left)
            result = max(result, area)

            if heights[left] < heights[right]:
                left += 1
            elif heights[left] >= heights[right]:
                right -= 1

        return result


if __name__ == "__main__":
    heights = list(map(int, sys.argv[1:]))
    print(Solution().maxArea(heights))
