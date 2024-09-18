from helper.list_to_tree_node import list_to_tree_node

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        cur = root
        while cur:
            if p.val < cur.val and q.val < cur.val:
                cur = cur.left
            elif p.val > cur.val and q.val > cur.val:
                cur = cur.right
            else:
                return cur

print(Solution().lowestCommonAncestor(list_to_tree_node([6,2,8,0,4,7,9,None,None,3,5]), TreeNode(2), TreeNode(4)).val)
