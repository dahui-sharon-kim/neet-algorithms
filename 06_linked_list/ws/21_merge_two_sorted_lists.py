import sys
from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def link(self, next=None):
        self.next = next

    def __repr__(self) -> str:
        return f"Node({self.val})"


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        merged = ListNode()
        head = merged

        while list1 and list2:
            first = list1.val
            second = list2.val

            if first < second:
                merged.next = list1
                list1 = list1.next
            else:
                merged.next = list2
                list2 = list2.next

            merged = merged.next

        if list1:
            merged.next = list1
        elif list2:
            merged.next = list2

        return head.next


def create_list(numbers: List[int]) -> Optional[ListNode]:
    if not numbers:
        return None
    nodes = []
    for idx, val in enumerate(numbers):
        nodes.append(ListNode(val=val))
        if idx:
            nodes[-2].next = nodes[-1]
    return nodes[0]


def print_list(head: Optional[ListNode]):
    print("start")
    while head:
        print(head.val)
        head = head.next
    print("end")


if __name__ == "__main__":
    first_len = int(sys.argv[1])
    list1 = list(map(int, sys.argv[2 : 2 + first_len]))
    list2 = list(map(int, sys.argv[2 + first_len :]))
    list1 = create_list(list1)
    list2 = create_list(list2)

    head = Solution().mergeTwoLists(list1, list2)
    print_list(head)
