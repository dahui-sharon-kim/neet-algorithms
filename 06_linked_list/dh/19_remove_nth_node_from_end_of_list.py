# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def go_n_steps_ahead(node: Optional[ListNode], n: int) -> Optional[ListNode]:
            curr = node
            for _ in range(n):
                if curr:
                    curr = curr.next
            return curr

        slow, fast = head, go_n_steps_ahead(head, n)

        if not fast:
            return head.next

        while fast.next:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next

        return head
