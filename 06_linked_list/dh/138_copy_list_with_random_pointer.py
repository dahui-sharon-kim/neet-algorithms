# https://leetcode.com/problems/copy-list-with-random-pointer/

from typing import Optional

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copied = { None: None }

        cur = head
        while cur:
            copied_node = Node(cur.val)
            copied[cur] = copied_node
            cur = cur.next
        
        cur = head
        while cur:
            copied_node = copied[cur]
            copied_node.next = copied[cur.next]
            copied_node.random = copied[cur.random]
            cur = cur.next
        
        return copied[head]
