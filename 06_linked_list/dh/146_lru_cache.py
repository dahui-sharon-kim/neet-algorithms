# https://leetcode.com/problems/lru-cache/description/

class DNode: # Doubly-linked node
    def __init__(self, key=0, value=0):
        self.key, self.value = key, value
        self.prev = self.next = None
        
class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}  # key -> node
        self.capacity = capacity
        # left와 right는 dummy nodes
        # left는 LRU, right는 most recently used
        self.left, self.right = DNode(), DNode()
        self.left.next, self.right.prev = self.right, self.left
 
    def remove(self, node: DNode) -> None:
        prv, nxt = node.prev, node.next
        prv.next, nxt.prev = nxt, prv
    
    def insert(self, node: DNode) -> None:
        before, after = self.right.prev, self.right
        before.next = after.prev = node
        node.next, node.prev = after, before
    
    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            # 지우고 다시 넣음
            self.remove(node)
            self.insert(node)
            return node.value
        return -1
    
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = DNode(key, value)
        self.insert(self.cache[key])

        if (len(self.cache)) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
