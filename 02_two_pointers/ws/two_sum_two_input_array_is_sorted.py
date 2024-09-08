import sys
from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i, start in enumerate(numbers):
            if target - start in numbers[i + 1 :]:
                return [i + 1, numbers.index(target - start, i + 1) + 1]
        return []

    def twoSum2(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        while l < r:
            sum = numbers[l] + numbers[r]

            if sum > target:
                r -= 1
            if sum < target:
                l += 1
            if sum == target:
                return [l + 1, r + 1]

        return []


if __name__ == "__main__":
    target = int(sys.argv[1])
    nums = list(map(int, sys.argv[2:]))
    print(Solution().twoSum2(nums, target))
