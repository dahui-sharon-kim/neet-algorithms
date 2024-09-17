from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = ListNode(-1)
        head = dummy

        ten = False
        while l1 or l2 or ten:
            first = l1.val if l1 and l1.val else 0
            second = l2.val if l2 and l2.val else 0
            sum = first + second
            if ten:
                sum += 1

            ten = True if sum // 10 else False
            r = sum % 10
            head.next = ListNode(r)
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            head = head.next

        return dummy.next if dummy.next else ListNode()
