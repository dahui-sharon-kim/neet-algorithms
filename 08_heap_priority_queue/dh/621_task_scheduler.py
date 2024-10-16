# https://leetcode.com/problems/task-scheduler/
from collections import Counter, deque
from typing import List
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        max_heap = [-cnt for cnt in count.values()]
        heapq.heapify(max_heap)

        time = 0
        queue = deque() # [-cnt, queue에서 꺼낼 수 있는 시간]의 쌍

        while max_heap or queue:
            time += 1
            
            if max_heap:
                cnt = 1 + heapq.heappop(max_heap)
                if cnt: # cnt == 0이면 queue에 넣지 않음
                    queue.append([cnt, time+n])
            if queue and queue[0][1] == time:
                heapq.heappush(max_heap, queue.popleft()[0])
        return time


        return tasks

print(Solution().leastInterval(["A","A","A","B","B","B"], 2))
print(Solution().leastInterval(["A","C","A","B","D","B"], 1))