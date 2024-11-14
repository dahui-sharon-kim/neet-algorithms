# https://leetcode.com/problems/longest-common-subsequence/

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        length1 = len(text1)
        length2 = len(text2)

        dp = [[0] * (length1+1) for _ in range(length2+1)]

        for i in range(1,length2+1):
            for j in range(1,length1+1):
                if text1[j-1] == text2[i-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])

        return dp[length2][length1]

print(Solution().longestCommonSubsequence("abcde", "ace")) # 3 (ace)
print(Solution().longestCommonSubsequence("abc", "abc")) # 3 (abc)
print(Solution().longestCommonSubsequence("abc", "def")) # 0
