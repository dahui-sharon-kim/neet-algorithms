from collections import deque
import sys
from typing import Optional
from tree import TreeNode, create_binary_tree, print_tree


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def depth(node: Optional[TreeNode]):
            if not node:
                return 0
            return max(depth(node.left), depth(node.right)) + 1

        queue = deque()
        queue.append(root)

        while queue:
            node = queue.popleft()
            if abs(depth(node.right) - depth(node.left)) > 1:
                return False
            if node.right:
                queue.append(node.right)
            if node.left:
                queue.append(node.left)

        return True


if __name__ == "__main__":
    nodes = list(map(int, sys.argv[1:]))
    root = create_binary_tree(nodes)
    print_tree(root)
    print(Solution().isBalanced(root))
