class Node:
    def __init__(self, key, val, next=None, prev=None) -> None:
        self.key = key
        self.val = val
        self.next, self.prev = next, prev


class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next, self.tail.prev = self.tail, self.head

    def remove(self, node: Node):
        prv, nxt = node.prev, node.next
        prv.next, nxt.prev = nxt, prv

    def insert(self, node: Node):
        prv, nxt = self.tail.prev, self.tail
        prv.next, nxt.prev = node, node
        node.prev, node.next = prv, nxt

    def get(self, key: int) -> int:
        if not self.cache.get(key):
            return -1

        node = self.cache[key]
        self.remove(node)
        self.insert(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if node := self.cache.get(key):
            self.remove(node)

        node = Node(key, value)
        self.cache[key] = node
        self.insert(node)

        if len(self.cache) > self.capacity:
            node = self.head.next
            self.remove(node)
            del self.cache[node.key]
