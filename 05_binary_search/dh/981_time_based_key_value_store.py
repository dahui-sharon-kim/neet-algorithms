# https://leetcode.com/problems/time-based-key-value-timedict/description/

from typing import List
from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.timedict = defaultdict(list)
        
    def find(self, timestamp: int, arr: List[tuple]):
        l, r = 0, len(arr)-1
        candidate = ""
        while l <= r:
            mid = (l + r) // 2
            if arr[mid][0] == timestamp:
                return arr[mid][1]
            elif arr[mid][0] < timestamp:
                candidate = arr[mid][1]
                l = mid + 1
            else:
                r = mid - 1
        return candidate

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timedict[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        return self.find(timestamp, self.timedict[key])


ans = []
time_map = TimeMap()
ans.append(time_map.set("foo", "bar", 1)) # None
ans.append(time_map.get("foo", 1))  # "bar"
ans.append(time_map.get("foo", 3))  # "bar"
ans.append(time_map.set("foo", "bar2", 4)) # None
ans.append(time_map.get("foo", 4))  # "bar2"
ans.append(time_map.get("foo", 5))  # "bar2"

print(ans)
