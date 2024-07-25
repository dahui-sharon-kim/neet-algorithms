import sys
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def link(self, next=None):
        self.next = next

    def __repr__(self) -> str:
        return f"Node({self.val})"


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        prev = None
        cur = head
        next = head.next
        while cur:
            cur.next = prev
            prev = cur
            cur = next
            if not cur:
                return prev
            next = next.next

        return None


if __name__ == "__main__":
    values = list(map(int, sys.argv[1:]))
    nodes = []
    for idx, val in enumerate(values):
        nodes.append(ListNode(val=val))
        if idx:
            nodes[-2].link(nodes[-1])

    head = nodes[0]
    new_head = Solution().reverseList(head)
    while new_head:
        print(new_head.val)
        new_head = new_head.next
