from typing import Optional

# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
# Example 2:

# Input: l1 = [0], l2 = [0]
# Output: [0]
# Example 3:

# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]

def node_to_list(head):
    lst = [head.val]
    curr = head.next
    while curr:
        lst.append(curr.val)
        curr = curr.next
    return lst

def list_to_node(lst):
    head = ListNode(lst[0])
    curr = head
    for i in lst[1:]:
        curr.next = ListNode(i)
        curr = curr.next
    return head

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0 # 다음 자리에도 가져갈 것
        dummy = ListNode() # 마지막에 빈 ListNode가 남지 않도록 dummy로 시작
        curr = dummy

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            summed = val1 + val2 + carry
            carry = summed // 10
            new_digit = summed % 10

            curr.next = ListNode(new_digit)
            curr = curr.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return dummy.next

print(node_to_list(Solution().addTwoNumbers(list_to_node([2,4,3]), list_to_node([5,6,4]))))
print(node_to_list(Solution().addTwoNumbers(list_to_node([9,9,9,9,9,9,9]), list_to_node([9,9,9,9]))))
