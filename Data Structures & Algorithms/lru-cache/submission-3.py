class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache_map = {}

        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    def remove(self, node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev
    
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = node
        nxt.prev = node
        node.next = nxt
        node.prev = prev

    def get(self, key: int) -> int:
        if key in self.cache_map:
            self.remove(self.cache_map[key])
            self.insert(self.cache_map[key])
            return self.cache_map[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache_map:
            self.remove(self.cache_map[key])

        self.cache_map[key] = Node(key, value)
        self.insert(self.cache_map[key])

        if len(self.cache_map) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache_map[lru.key]       
