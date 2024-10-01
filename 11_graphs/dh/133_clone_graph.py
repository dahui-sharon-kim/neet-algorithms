# https://leetcode.com/problems/clone-graph/

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
            
        old_to_new = {}

        def clone(node):
            if node in old_to_new:
                return old_to_new[node]
            copy = Node(node.val)
            old_to_new[node] = copy

            for nei in node.neighbors:
                copy.neighbors.append(clone(nei))
            return copy
        
        return clone(node)