# https://leetcode.com/problems/climbing-stairs/description/

class Solution:
    def __init__(self):
        self.visited = {0: 1, 1: 1}
    def climbStairs(self, n: int) -> int:
        if n in self.visited:
            return self.visited[n]
        
        self.visited[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        return self.visited[n]
