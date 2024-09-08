from collections import defaultdict
import sys
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = defaultdict(list)

        for n in nums:
            result[n].append(n)

        res = list(result.values())
        res.sort(key=len, reverse=True)

        return [r[0] for r in res[:k]]


if __name__ == "__main__":
    k = int(sys.argv[1])
    nums = list(map(int, sys.argv[2:]))
    print(Solution().topKFrequent(nums, k))
