# https://leetcode.com/problems/word-break/description/

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        length = len(s)
        word_set = set(wordDict)
        dp = [False] * (length + 1)
        dp[0] = True  # 빈 문자열 ""는 segment 가능

        for i in range(1, length+1):
            for j in range(i):
                if dp[j] == True and s[j:i] in wordDict:
                    dp[i] = True
        
        return dp[-1]
