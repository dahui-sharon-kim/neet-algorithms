from list_node import ListNode, create_head
from typing import Optional
import sys


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        tmp = head
        while tmp and tmp.next is not slow:
            tmp = tmp.next
        tmp.next = None

        prev = None
        cur = slow
        next = slow.next
        while cur:
            cur.next = prev
            prev = cur
            cur = next
            if not cur:
                slow = prev
                break
            next = next.next

        first = head
        last = head
        while first and slow:
            tmp = first.next
            first.next = slow
            tmp2 = slow.next
            slow.next = tmp
            slow = tmp2
            first = tmp

            last = last.next
            if last.next:
                last = last.next

        if slow:
            last.next = slow


if __name__ == "__main__":
    values = list(map(int, sys.argv[1:]))
    head = create_head(values)
    Solution().reorderList(head)
    print(head)
