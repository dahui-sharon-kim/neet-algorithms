from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # Answer 1: in-order recursive 이용 (왼쪽 서브트리 -> 자기자신 -> 오른쪽 서브트리)
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = 0
        self.result = None

        def in_order(node):
            if not node or self.result is not None:
                return
            in_order(node.left) # 왼쪽 서브트리 끝까지 가기
            # 왼쪽 서브트리를 전부 다 방문한 후에 다시 원래 node를 재방문했을 때 count 1 증가
            self.count += 1
            if self.count == k:
                self.result = node.val
                return
            in_order(node.right) # 오른쪽 서브트리 끝까지 가기
        
        in_order(root)
        return self.result
    
    # Answer 2: iterative
    def kthSmallest2(self, root: Optional[TreeNode], k: int) -> int:
        n = 0
        stack = []
        cur = root
        
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left

            cur = stack.pop()
            n += 1
            if n == k:
                return cur.val
            cur = cur.right