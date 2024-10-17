from typing import List

class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        
        starts, ends = [], []
        for i in intervals:
            starts.append(i.start)
            ends.append(i.end)
        starts.sort()
        ends.sort()

        start_pointer = 0
        end_pointer = 0
        rooms_in_use = 0
        max_rooms = 0

        while start_pointer < len(starts):
            if starts[start_pointer] < ends[end_pointer]:
                # 가장 빨리 끝나는 미팅이 끝나기 전에 새로운 미팅 시작
                rooms_in_use += 1
                max_rooms = max(max_rooms, rooms_in_use)
                start_pointer += 1
            else:
                # 미팅 끝나면 방을 비움
                rooms_in_use -= 1
                end_pointer += 1
        return max_rooms