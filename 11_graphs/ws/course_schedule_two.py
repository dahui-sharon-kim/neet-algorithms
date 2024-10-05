from collections import defaultdict
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        pre = defaultdict(list)

        for first, second in prerequisites:
            pre[first].append(second)

        visited, cycling = set(), set()
        output = []

        def dfs(course):
            if course in visited:
                return True
            if course in cycling:
                return False

            cycling.add(course)
            for c in pre[course]:
                if not dfs(c):
                    return False
            cycling.remove(course)
            visited.add(course)
            output.append(course)
            return True

        for course in range(numCourses):
            if not dfs(course):
                return []
        return output
