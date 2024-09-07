from typing import Optional


class Node:
    def __init__(self, val, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        cache = {}
        tmp = head
        new_head = None
        while tmp:
            cache[tmp] = Node(tmp.val)
            if not new_head:
                new_head = cache[tmp]
            tmp = tmp.next

        tmp = head
        while tmp:
            node = cache[tmp]
            if tmp.next:
                node.next = cache[tmp.next]
            if tmp.random:
                node.random = cache[tmp.random]
            tmp = tmp.next

        return new_head
