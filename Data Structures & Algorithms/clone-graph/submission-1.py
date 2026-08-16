"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:return
        visited = {}

        def cloneGraph(node): # O(nodes)
            if node in visited:
                return visited[node]

            newNode = Node(node.val)
            visited[node] = newNode

            for neigh in node.neighbors: # O(neigh)
                newNeighbor = cloneGraph(neigh)
                newNode.neighbors.append(newNeighbor)
            
            return newNode
        
        # O(nodes*vertex)
        # space : O(nodes) + nb of calls O(2*connections)
        
        return cloneGraph(node)