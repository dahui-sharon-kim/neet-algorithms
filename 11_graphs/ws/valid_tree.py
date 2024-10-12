from typing import List
from collections import defaultdict


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        pre = defaultdict(list)
        for first, second in edges:
            pre[first].append(second)
            pre[second].append(first)

        visited = set()

        def dfs(cur, prev):
            if cur in visited:
                return False

            visited.add(cur)
            for c in pre[cur]:
                if c == prev:
                    continue
                if not dfs(c, cur):
                    return False
            return True

        return dfs(0, -1) and len(visited) == n
