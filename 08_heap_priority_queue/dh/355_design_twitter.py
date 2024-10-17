from collections import defaultdict
from typing import List
import heapq

class Twitter:

    def __init__(self):
        self.count = 0
        self.tweet_map = defaultdict(list) # userId -> List[count, tweetIds]
        self.follow_map = defaultdict(set) # userId -> Set[followeeId]

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweet_map[userId].append([self.count, tweetId])
        self.count -= 1 # 점점 더 recent가 되니까 min heap에 들어갈 때 decrement해서 들어가도록.

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        min_heap = []
        self.follow_map[userId].add(userId)

        for followee_id in self.follow_map[userId]:
            if followee_id in self.tweet_map:
                idx = len(self.tweet_map[followee_id]) - 1 # last index
                count, tweet_id = self.tweet_map[followee_id][idx]
                min_heap.append([count, tweet_id, followee_id, idx - 1])

        heapq.heapify(min_heap)

        while min_heap and len(res) < 10:
            count, tweet_id, followee_id, idx = heapq.heappop(min_heap)
            res.append(tweet_id)

            if idx >= 0:
                count, tweet_id = self.tweet_map[followee_id][idx]
                heapq.heappush(min_heap, [count, tweet_id, followee_id, idx - 1])
        
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follow_map[followerId].add(followeeId)        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follow_map[followerId]:
            self.follow_map[followerId].remove(followeeId)