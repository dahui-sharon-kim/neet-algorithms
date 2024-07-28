from collections import deque
import sys
from typing import Optional
from tree import TreeNode, create_binary_tree, print_tree


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = deque()
        if root:
            queue.append(root)

        while queue:
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            node.left, node.right = node.right, node.left

        return root


if __name__ == "__main__":
    nodes = list(map(int, sys.argv[1:]))
    root = create_binary_tree(nodes)
    print_tree(root)
    print_tree(Solution().invertTree(root))
