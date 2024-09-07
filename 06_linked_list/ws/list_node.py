from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def link(self, next=None):
        self.next = next

    def __repr__(self) -> str:
        return f"Node({self.val}) -> {self.next if self.next else 'None'}"


def create_head(values: List[int]) -> Optional[ListNode]:
    if not values:
        return None

    nodes = []
    for idx, val in enumerate(values):
        nodes.append(ListNode(val=val))
        if idx:
            nodes[-2].link(nodes[-1])
    return nodes[0]
