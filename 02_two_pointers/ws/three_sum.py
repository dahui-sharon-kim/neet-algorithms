import sys
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = set()
        nums.sort()
        for i in range(len(nums) - 2):
            l = i + 1
            r = len(nums) - 1
            while l < r:
                sum = nums[i] + nums[l] + nums[r]

                if sum > 0:
                    r -= 1
                elif sum < 0:
                    l += 1
                else:
                    results.add((nums[i], nums[l], nums[r]))
                    l += 1
                    r -= 1

        return [list(res) for res in results]


if __name__ == "__main__":
    nums = list(map(int, sys.argv[1:]))
    print(Solution().threeSum(nums))
