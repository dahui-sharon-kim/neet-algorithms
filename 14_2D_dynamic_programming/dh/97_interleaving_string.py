# https://leetcode.com/problems/interleaving-string/

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # Check if lengths match
        if len(s1) + len(s2) != len(s3):
            return False

        # Create a 2D DP array initialized to False
        dp = [[False] * (len(s2) + 1) for _ in range(len(s1) + 1)]
        dp[0][0] = True

        # Fill in the DP table
        for i in range(len(s1) + 1):
            for j in range(len(s2) + 1):
                if i > 0 and s1[i - 1] == s3[i + j - 1]:
                    dp[i][j] = dp[i][j] or dp[i - 1][j]
                if j > 0 and s2[j - 1] == s3[i + j - 1]:
                    dp[i][j] = dp[i][j] or dp[i][j - 1]

        # Result is in the bottom-right cell
        return dp[len(s1)][len(s2)]

# Test cases
print(Solution().isInterleave("aabcc", "dbbca", "aadbbcbcac"))  # True
print(Solution().isInterleave("aabcc", "dbbca", "aadbbbaccc"))  # False
print(Solution().isInterleave("", "", ""))  # True
