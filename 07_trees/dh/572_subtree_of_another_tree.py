# https://leetcode.com/problems/subtree-of-another-tree/description/
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def is_same_tree(root, sub_root) -> bool:
            if not root and not sub_root:
              return True
            if not root or not sub_root:
                return False
            if root.val != sub_root.val:
                return False
            return is_same_tree(root.left, sub_root.left) and is_same_tree(root.right, sub_root.right)
    
        def check_subtree(node):
            if not node:
                return False
            if is_same_tree(node, subRoot):
                return True
            return check_subtree(node.left) or check_subtree(node.right)
        
        return check_subtree(root)