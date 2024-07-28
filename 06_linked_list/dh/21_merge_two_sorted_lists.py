# https://leetcode.com/problems/merge-two-sorted-lists/description/
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
  def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:  
        dummy = ListNode()
        current = dummy

        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next

            current = current.next

        if list1:
            current.next = list1
        elif list2:
            current.next = list2

        return dummy.next

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
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result


solution = Solution()

list1 = to_linked_list([1, 2, 4])
list2 = to_linked_list([1, 3, 4])
merged_list_head = solution.mergeTwoLists(list1, list2)
print(to_list(merged_list_head))  # Output: [1, 1, 2, 3, 4, 4]

list1 = to_linked_list([])
list2 = to_linked_list([])
merged_list_head = solution.mergeTwoLists(list1, list2)
print(to_list(merged_list_head))  # Output: []

list1 = to_linked_list([])
list2 = to_linked_list([0])
merged_list_head = solution.mergeTwoLists(list1, list2)
print(to_list(merged_list_head))  # Output: [0]