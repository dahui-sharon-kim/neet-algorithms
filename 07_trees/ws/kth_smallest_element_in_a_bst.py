from typing import Optional

from tree import TreeNode


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        results = []

        def dfs(node):
            nonlocal results
            if node.left:
                dfs(node.left)

            results.append(node.val)

            if node.right:
                dfs(node.right)

        dfs(root)
        return results[k - 1]
