# https://leetcode.com/problems/decode-ways/

class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0

        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1

        for i in range(2, n + 1):
            if s[i-1] != "0": # 1 <= 나 <= 9이면 바로 앞의 substring 케이스들 다 쓸 수 있음
                dp[i] += dp[i-1]
            
            if 10 <= int(s[i-2:i]) <= 26: # 10 <= 나 바로 앞, 나 <= 26이면 앞앞의 substring 케이스들 다 쓸 수 있음
                dp[i] += dp[i-2]

        return dp[n]


print(Solution().numDecodings("12"))  # 2
print(Solution().numDecodings("226"))  # 3
print(Solution().numDecodings("06"))   # 0
print(Solution().numDecodings("10"))   # 1
print(Solution().numDecodings("2101"))   # 1
