# https://leetcode.com/problems/binary-tree-right-side-view/

from typing import Optional, List
from collections import deque
from helper.list_to_tree_node import list_to_tree_node

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = deque()
        q.append(root)

        while q:
            q_length = len(q)
            level = []
            for _ in range(q_length):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                res.append(level.pop())
        return res

print(Solution().rightSideView(list_to_tree_node([1,2,3,None,5,None,4])))
                