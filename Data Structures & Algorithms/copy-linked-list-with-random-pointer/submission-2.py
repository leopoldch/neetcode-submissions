"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        dummyNode = Node(-1)
        nodes_map = {}
        last = dummyNode
        current_head = head

        while current_head:
            value = current_head.val
            new_node = Node(value)
            nodes_map[current_head] = new_node
            last.next = new_node
            last = new_node
            current_head = current_head.next

        current_head = head
        new_list_head = dummyNode.next

        while current_head:
            
            if current_head.random:
                random_node = nodes_map[current_head.random]
                new_list_head.random = random_node
            
            current_head = current_head.next
            new_list_head = new_list_head.next
        
        return dummyNode.next

        
 



