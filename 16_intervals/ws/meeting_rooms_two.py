from typing import List
import heapq


class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda x: x.start)
        h = [intervals[0].end]

        for i in range(1, len(intervals)):
            if h[0] <= intervals[i].start:
                heapq.heappop(h)
            heapq.heappush(h, intervals[i].end)
        return len(h)
