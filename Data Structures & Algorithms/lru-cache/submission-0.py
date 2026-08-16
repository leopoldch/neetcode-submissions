class Node:

    def __init__(self, key, val, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = Node(-1, -1)
        self.tail = Node(-1,-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.node_map = {}

    def remove(self, node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev
        del self.node_map[node.key]
    
    def add(self, node):
        tmp = self.head.next
        tmp.prev = node 
        self.head.next = node
        node.prev = self.head
        node.next = tmp

        self.node_map[node.key] = node

        if len(self.node_map) > self.capacity:
            self.remove(self.tail.prev)


    def get(self, key: int) -> int:
        if key not in self.node_map:
            return -1

        node = self.node_map[key]
        self.remove(node)
        self.add(node)

        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.node_map:
            node = self.node_map[key]
            node.val = value
            self.remove(node)
            self.add(node)
        else:
            node = Node(key, value)
            self.add(node)







