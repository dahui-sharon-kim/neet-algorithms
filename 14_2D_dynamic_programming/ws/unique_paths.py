class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1] * n] * m

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if i == m - 1 or j == n - 1:
                    dp[i][j] = 1
                    continue
                dp[i][j] = dp[i + 1][j] + dp[i][j + 1]

        return dp[0][0]
