from collections import deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def create_binary_tree(nodes: List[int]) -> Optional[TreeNode]:
    if not nodes:
        return None

    root = TreeNode(nodes[0])
    queue = deque()
    queue.append(root)
    index = 1

    while index < len(nodes):
        node = queue.popleft()

        if index < len(nodes) and nodes[index] is not None:
            node.left = TreeNode(nodes[index])
            queue.append(node.left)
        index += 1

        if index < len(nodes) and nodes[index] is not None:
            node.right = TreeNode(nodes[index])
            queue.append(node.right)
        index += 1

    return root


def print_tree(root: Optional[TreeNode]):
    if not root:
        return

    queue = deque()
    queue.append(root)
    results = []
    while queue:
        node = queue.popleft()
        if node:
            results.append(node.val)
            if any([node.left, node.right]):
                queue.append(node.left)
                queue.append(node.right)
        else:
            results.append("null")

    print(results)
