# https://leetcode.com/problems/pacific-atlantic-water-flow/description/

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(r, c, visit, prev_height):
            if ((r, c) in visit or
                r not in range(ROWS) or
                c not in range(COLS) or
                heights[r][c] < prev_height):
                return
            visit.add((r, c))
            dfs(r+1, c, visit, heights[r][c])
            dfs(r-1, c, visit, heights[r][c])
            dfs(r, c+1, visit, heights[r][c])
            dfs(r, c-1, visit, heights[r][c])

        # 반드시 pacific혹은 atlantic에 갈 수 있는 cell부터 시작해서
        # 더 이상 갈 수 없을 때까지 계속 add 해간다
        
        for c in range(COLS):
            dfs(0, c, pac, heights[0][c]) # 첫 번째 열 
            dfs(ROWS-1, c, atl, heights[ROWS-1][c]) # 마지막 열
        
        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][c]) # 첫 번째 행
            dfs(r, COLS-1, atl, heights[r][c]) # 마지막 행

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
        
        return res
