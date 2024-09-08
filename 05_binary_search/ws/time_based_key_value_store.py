from collections import defaultdict


class TimeMap:

    def __init__(self):
        self.map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        values = self.map[key]

        left, right = 0, len(values) - 1
        res = ""

        while left <= right:
            mid = left + (right - left) // 2

            v, ts = values[mid]
            if ts > timestamp:
                right = mid - 1
            else:
                res = v
                left = mid + 1

        return res


map = TimeMap()

map.set("test", "one", 10)
map.set("test", "two", 20)
map.set("test", "three", 30)
print(map.get("test", 15))
print(map.get("test", 25))
print(map.get("test", 35))
