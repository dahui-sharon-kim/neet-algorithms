# loop이 있으면 안 됨
# 방문한 node의 수 == length (즉 모든 node가 최소 하나의 다른 node와 연결되어 있어야 함)

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True
        adjacency = { i: [] for i in range(n) }
        for n1, n2 in edges:
            adjacency[n1].append(n2)
            adjacency[n2].append(n1)
        
        visit = set()
        def dfs(i, prev_node):
            if i in visit:
                return False # loop
            visit.add(i)
            for j in adjacency[i]:
                if j == prev_node:
                    continue
                if not dfs(j, i):
                    return False

            return True

        return dfs(0, -1) and n == len(visit)
