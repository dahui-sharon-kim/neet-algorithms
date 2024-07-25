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
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False

        visited = set()

        traveler = head
        while traveler:
            if traveler.val in visited:
                return True
            visited.add(traveler.val)
            traveler = traveler.next

        return False


if __name__ == "__main__":
    index = int(sys.argv[1])
    values = list(map(int, sys.argv[2:]))
    nodes = []
    for idx, val in enumerate(values):
        nodes.append(ListNode(val=val))
        if idx:
            nodes[-2].link(nodes[-1])

    if index != -1:
        nodes[-1].link(nodes[index])
    head = nodes[0]

    print(Solution().hasCycle(head))
