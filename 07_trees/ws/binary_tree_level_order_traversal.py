from typing import Optional, List
from collections import defaultdict, deque

from tree import TreeNode


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        results = defaultdict(list)
        q = deque()
        q.append((root, 1))
        while q:
            node, depth = q.popleft()
            results[depth].append(node.val)
            if node.left:
                q.append((node.left, depth + 1))
            if node.right:
                q.append((node.right, depth + 1))
        return list(results.values())
