from collections import deque
import sys
from typing import Optional
from tree import TreeNode, create_binary_tree, print_tree


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        result = 0
        if not root:
            return result

        stack = deque()
        stack.append((root, 1))
        while stack:
            node, depth = stack.pop()
            result = max(result, depth)

            if node.left:
                stack.append((node.left, depth + 1))
            if node.right:
                stack.append((node.right, depth + 1))

        return result


if __name__ == "__main__":
    nodes = list(map(int, sys.argv[1:]))
    root = create_binary_tree(nodes)
    print_tree(root)
    print(Solution().maxDepth(root))
