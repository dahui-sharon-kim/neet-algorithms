# https://leetcode.com/problems/reorder-list/description/

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def find_middle_node(self, head):
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        mid = self.find_middle_node(head)

        prev = None
        next_node = mid

        while next_node:
            temp_node = next_node.next
            next_node.next = prev
            prev = next_node
            next_node = temp_node
        
        
        front, back = head, prev
        while back and back.next:
            temp1, temp2 = front.next, back.next
            front.next = back
            back.next = temp1
            front, back = temp1, temp2
