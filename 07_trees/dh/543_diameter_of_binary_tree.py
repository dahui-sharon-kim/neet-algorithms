# https://leetcode.com/problems/diameter-of-binary-tree/description/
from typing import Optional
from helper.list_to_tree_node import list_to_tree_node

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:        
        self.max_diameter = 0

        def get_depth(root: Optional[TreeNode]) -> int:
            if not root:
                return 0
            left_depth = get_depth(root.left)
            right_depth = get_depth(root.right)
            self.max_diameter = max(self.max_diameter, left_depth + right_depth)

            return max(left_depth, right_depth) + 1

        get_depth(root)
        return self.max_diameter
        

# print(Solution().diameterOfBinaryTree(list_to_tree_node([1,2,3,4,5])))
# print(Solution().diameterOfBinaryTree(list_to_tree_node([1,2])))
# print(Solution().diameterOfBinaryTree(list_to_tree_node([4,-7,-3,None,None,-9,-3,9,-7,-4,None,6,None,-6,-6,None,None,0,6,5,None,9,None,None,-1,-4,None,None,None,-2])))