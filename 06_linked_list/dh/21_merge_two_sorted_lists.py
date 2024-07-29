# https://leetcode.com/problems/merge-two-sorted-lists/description/
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        plain_list = []

        while list1 or list2:
            if not list2 or (list1 and list1.val < list2.val):
                plain_list.append(list1.val)
                list1 = list1.next
            else:
                plain_list.append(list2.val)
                list2 = list2.next
        
        return to_linked_list(plain_list)
            

def to_linked_list(lst):
    if not lst:
        return None
    head = ListNode(lst[0]) 
    current = head  
    
    for value in lst[1:]:
        current.next = ListNode(value) 
        current = current.next

    return head
