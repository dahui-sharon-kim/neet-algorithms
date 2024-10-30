from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_indexes = {}

        for i in range(len(s)):
            last_indexes[s[i]] = i

        res = []
        count = 0
        size = 0
        for i in range(len(s)):
            size = max(size, last_indexes[s[i]])
            count += 1

            if size == i:
                res.append(count)
                count = 0
        return res
