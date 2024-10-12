from typing import List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parents = [i for i in range(len(edges) + 1)]
        ranks = [1 for _ in range(len(edges) + 1)]

        def find(n):
            p = parents[n]
            while parents[p] != p:
                parents[p] = parents[parents[p]]
                p = parents[p]
            return p

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return False

            if ranks[p1] > ranks[p2]:
                parents[p2] = p1
                ranks[p1] += ranks[p2]
            else:
                parents[p1] = p2
                ranks[p2] += ranks[p1]
            return True

        for edge in edges:
            if not union(*edge):
                return edge

        return []
