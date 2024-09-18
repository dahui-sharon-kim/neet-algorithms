from typing import List
import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def list_to_tree_node(lst: List):
    if not lst:
        return None

    root = TreeNode(lst[0])
    queue = collections.deque([root]) # queue of tree nodes
    idx = 1

    while queue and idx < len(lst):
        current = queue.popleft()

        if idx < len(lst) and lst[idx] is not None:
            current.left = TreeNode(lst[idx])
            queue.append(current.left)
        idx += 1
        
        if idx < len(lst) and lst[idx] is not None:
            current.right = TreeNode(lst[idx])
            queue.append(current.right)
        idx += 1

    return root

print(list_to_tree_node([1, 2, 3]).right.val)
