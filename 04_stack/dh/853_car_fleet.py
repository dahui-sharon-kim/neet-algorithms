# https://leetcode.com/problems/car-fleet/

from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # 출발선에서 먼 순서 = 도착점에서 가까운 순서대로 정렬
        new_list = sorted(zip(position, speed), key=lambda x: x[0], reverse=True)

        stack = []

        for pos, spd in new_list:
            time_to_target = (target - pos) / spd

            if not stack or time_to_target > stack[-1]:
                stack.append(time_to_target)
        
        return len(stack)

print(Solution().carFleet(12,[10,8,0,5,3],[2,4,1,1,3]))
