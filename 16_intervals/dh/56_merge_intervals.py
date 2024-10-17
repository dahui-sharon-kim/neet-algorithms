from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])

        res = []
        for interval in intervals:
            if not res or res[-1][1] < interval[0]: # 안 겹침
                res.append(interval)
            else:
                res[-1][1] = max(res[-1][1], interval[1])

        return res

print(Solution().merge([[1,3],[2,6],[8,10],[15,18]])) # [[1,6],[8,10],[15,18]]
print(Solution().merge([[1,4],[4,5]])) # [[1,5]]
