# https://leetcode.com/problems/validate-binary-search-tree/

from typing import Optional
from helper.list_to_tree_node import list_to_tree_node

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def check(node, left_end, right_end):
            if not node:
                return True
            
            if not (left_end < node.val < right_end):
                return False
            # 왼쪽 노드는 바로 이전 노드의 왼쪽 threshold를 그대로 쓰고
            # 오른쪽 노드는 바로 이전 노드의 오른쪽 threshold를 그대로 씀
            return check(node.left, left_end, node.val) and check(node.right, node.val, right_end)
        
        return check(root, -float("inf"), float("inf"))

print(Solution().isValidBST(list_to_tree_node([2,1,3]))) # True
print(Solution().isValidBST(list_to_tree_node([5,1,4,None,None,3,6]))) # False
print(Solution().isValidBST(list_to_tree_node([5,4,6,None,None,3,7]))) # False
        