# https://leetcode.com/problems/edit-distance/description/

class Solution:
    def minDistance(self, word1, word2):
        m, n = len(word1), len(word2)
        
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # 초기화
        for i in range(m + 1):
            dp[i][0] = i  # word1의 글자를 다 지우는 것
        for j in range(n + 1):
            dp[0][j] = j  # word1에 word2의 모든 글자를 다 넣는 것
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]: 
                    dp[i][j] = dp[i - 1][j - 1]
                else: 
                    dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
        
        return dp[m][n]
