class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {len(s): 1}

        def check_alphabet(s, i):
            return s[i] == "1" or s[i] == "2" and s[i + 1] in "0123456"

        for i in range(len(s) - 1, -1, -1):
            if s[i] == "0":
                dp[i] = 0
            else:
                dp[i] = dp[i + 1]

            if i + 1 < len(s) and check_alphabet(s, i):
                dp[i] += dp[i + 2]

        return dp[0]
