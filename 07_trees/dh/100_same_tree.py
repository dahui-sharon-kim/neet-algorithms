# https://leetcode.com/problems/same-tree/description/

from typing import Optional
from helper.list_to_tree_node import list_to_tree_node

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
  
# print(Solution().isSameTree(list_to_tree_node([1, 2, 3]), list_to_tree_node([1, 2, 3])))