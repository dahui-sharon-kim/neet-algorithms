from collections import defaultdict
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre = defaultdict(list)

        for first, second in prerequisites:
            pre[first].append(second)

        visited = set()

        def dfs(course):
            if course in visited:
                return False
            if pre[course] == []:
                return True

            visited.add(course)
            for c in pre[course]:
                if not dfs(c):
                    return False
            visited.remove(course)
            pre[course] = []
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False
        return True
