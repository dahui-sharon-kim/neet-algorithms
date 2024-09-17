from list_node import ListNode, create_head
from typing import Optional
import sys


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        slow = dummy
        fast = head
        for _ in range(n):
            fast = fast.next

        while fast:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next

        return dummy.next


if __name__ == "__main__":
    n = int(sys.argv[1])
    values = list(map(int, sys.argv[2:]))
    head = create_head(values)
    print(Solution().removeNthFromEnd(head, n))
