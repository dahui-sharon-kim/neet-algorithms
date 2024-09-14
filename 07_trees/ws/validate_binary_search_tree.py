from typing import Optional

from tree import TreeNode


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def bfs(node, left, right):
            if not node:
                return True
            if node.val <= left:
                return False
            if node.val >= right:
                return False

            return bfs(node.left, left, node.val) and bfs(node.right, node.val, right)

        return bfs(root, float("-inf"), float("inf"))
