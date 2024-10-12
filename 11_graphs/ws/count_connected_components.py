from typing import List
from collections import defaultdict


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if not edges:
            return n

        pre = defaultdict(list)
        for first, second in edges:
            pre[first].append(second)
            pre[second].append(first)

        def dfs(cur, prev, visited):
            if cur in visited:
                return

            visited.add(cur)
            for c in pre[cur]:
                if c == prev:
                    continue
                dfs(c, cur, visited)
            del pre[cur]

        count = 0
        for i in range(n):
            if i in pre:
                dfs(i, -1, set())
                count += 1
        return count
