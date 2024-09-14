from collections import deque
from tree import TreeNode


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        s = deque()
        s.append((root, root.val))
        while s:
            node, max_val = s.pop()
            if node.val >= max_val:
                count += 1
            if node.left:
                s.append((node.left, max(max_val, node.left.val)))
            if node.right:
                s.append((node.right, max(max_val, node.right.val)))

        return count
