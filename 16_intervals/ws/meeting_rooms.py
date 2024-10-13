from typing import List


class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        sorted_intervals = sorted(intervals, key=lambda x: x.start)
        prev = None
        for cur in sorted_intervals:
            if not prev:
                prev = cur
                continue

            if prev.end > cur.start:
                return False
            prev = cur
        return True
