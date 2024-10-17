# https://neetcode.io/problems/meeting-schedule

from typing import List

class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    def interval_to_list(self, interval:Interval) -> List:
        return [interval.start, interval.end]

    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
            
        intervals.sort(key=lambda x:x.end)
        prev_end = intervals[0].end

        for interval in intervals[1:]:
            if interval.start < prev_end:
                return False
            else:
                prev_end = interval.end
        return True

print(Solution().canAttendMeetings([Interval(0,30),Interval(5,10),Interval(15,20)])) # False
print(Solution().canAttendMeetings([Interval(5,8),Interval(9,15)])) # True
