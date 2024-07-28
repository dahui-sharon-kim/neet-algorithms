# https://leetcode.com/problems/reverse-linked-list/description/

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return to_linked_list(to_list(head)[::-1])

def to_linked_list(lst):
    if not lst:
        return None
    head = ListNode(lst[0])
    current = head

    for value in lst[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

def to_list(node):
    lst = []
    while node:
        lst.append(node.val)
        node = node.next
    return lst
