from collections import deque
import sys
from typing import Optional
from tree import TreeNode, create_binary_tree, print_tree


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def make_list(node: Optional[TreeNode]):
            results = []
            if not node:
                return results
            queue = deque()
            queue.append(node)
            while queue:
                n = queue.popleft()
                if n:
                    results.append(n.val)
                    queue.append(n.left)
                    queue.append(n.right)
                else:
                    results.append("null")
            return results

        if not root:
            return False

        if not subRoot:
            return True

        sub_list = make_list(subRoot)
        queue = deque()
        queue.append(root)
        result = False
        while queue:
            n = queue.popleft()
            if n.left:
                queue.append(n.left)
            if n.right:
                queue.append(n.right)

            if n.val == subRoot.val:
                if make_list(n) == sub_list:
                    return True

        return result


if __name__ == "__main__":
    first_len = int(sys.argv[1])
    list1 = list(map(int, sys.argv[2 : 2 + first_len]))
    list2 = list(map(int, sys.argv[2 + first_len :]))

    p = create_binary_tree(list1)
    q = create_binary_tree(list2)
    print_tree(p)
    print_tree(q)
    print(Solution().isSubtree(p, q))
