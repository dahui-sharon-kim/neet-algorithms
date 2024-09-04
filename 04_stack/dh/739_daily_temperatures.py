# https://leetcode.com/problems/daily-temperatures/

from typing import List

# Monotonic stack

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = [0] * n 
        stack = [] # 아직 자기보다 기온이 더 높은 날을 만나지 못한 날들의 인덱스
        for idx, temperature in enumerate(temperatures):
            # 현재 온도가 스택에 있는 온도들보다 더 높은 동안 계속 수행
            while stack and temperature > temperatures[stack[-1]]:
                i = stack.pop()
                answer[i] = idx - i # 스택에 쌓여 있던 날들이 더 따뜻한 날을 만나기 위해 기다린 날의 수
            stack.append(idx)
        return answer

print(Solution().dailyTemperatures([73,74,75,71,69,72,76,73]))
print(Solution().dailyTemperatures([30,40,50,60]))
print(Solution().dailyTemperatures([30,60,90]))