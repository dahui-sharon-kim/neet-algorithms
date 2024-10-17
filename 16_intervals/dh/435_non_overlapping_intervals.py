# https://leetcode.com/problems/non-overlapping-intervals/

from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1]) # 끝나는 시점 기준으로 오름차순 정렬

        prev_end = intervals[0][1]
        cnt = 0
        for i in intervals[1:]:
            if i[0] < prev_end:
                cnt += 1
            else:
                prev_end = i[1]
        
        return cnt
        

print(Solution().eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]])) # 1 ([1,3] 제거)
print(Solution().eraseOverlapIntervals([[1,2],[1,2],[1,2]])) # 2 ([1,2],[1,2] 제거)
print(Solution().eraseOverlapIntervals([[1,2],[2,3]])) # 0
