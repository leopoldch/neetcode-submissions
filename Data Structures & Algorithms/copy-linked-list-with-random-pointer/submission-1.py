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
        nodes_associations = {}
        last = dummyNode
        current_head = head

        index=0
        while current_head:
            nodes_associations[current_head] = index
            value = current_head.val
            new_node = Node(value)
            nodes_map[index] = new_node
            last.next = new_node
            last = new_node
            current_head = current_head.next
            index+=1

        current_head = head
        new_list_head = dummyNode.next

        while current_head:
            
            if current_head.random:
                index = nodes_associations[current_head.random]
                random_node = nodes_map[index]
                new_list_head.random = random_node
            
            current_head = current_head.next
            new_list_head = new_list_head.next
        
        return dummyNode.next

        
 



