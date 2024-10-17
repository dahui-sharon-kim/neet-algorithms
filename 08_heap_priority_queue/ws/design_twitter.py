from typing import List
import heapq
from collections import defaultdict


class Twitter:
    def __init__(self):
        self.posts = defaultdict(list)
        self.followers = defaultdict(set)
        self.timestamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts[userId].append((self.timestamp, tweetId))
        self.timestamp -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        posts = []
        for f in self.followers[userId]:
            if self.posts[f]:
                posts.extend(self.posts[f])
        if self.posts[userId]:
            posts.extend(self.posts[userId])

        heapq.heapify(posts)
        res = []
        for _ in range(10):
            if not posts:
                break
            _, post_id = heapq.heappop(posts)
            res.append(post_id)
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        if followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)
