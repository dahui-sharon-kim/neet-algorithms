# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder and not inorder:
            return None
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        # in-order에서 왼쪽 서브트리는 [:mid] (len=mid-1)
        # pre-order에서 왼쪽 서브트리는 index=1인 노드부터 시작해 len=mid-1이 되도록 슬라이싱한 배열
        root.left, root.right = self.buildTree(preorder[1:mid+1], inorder[:mid]), self.buildTree(preorder[mid+1:], inorder[mid+1:])
        return root
